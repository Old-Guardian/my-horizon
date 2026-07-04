"""RSS feed scraper implementation."""

import calendar
import hashlib
import logging
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List, Optional
from email.utils import parsedate_to_datetime
import httpx
import feedparser

from .base import BaseScraper
from ..models import ContentItem, SourceType, RSSSourceConfig

logger = logging.getLogger(__name__)


@dataclass
class RSSFeedStats:
    """Per-feed diagnostics from the most recent RSS fetch."""

    name: str
    url: str
    status_code: Optional[int] = None
    error: Optional[str] = None
    parsed_entries: int = 0
    returned_items: int = 0
    skipped_old_items: int = 0
    undated_fallback_items: int = 0
    latest_parsed_date: Optional[datetime] = None
    limited_items: int = 0


class RSSScraper(BaseScraper):
    """Scraper for RSS/Atom feeds."""

    def __init__(self, sources: List[RSSSourceConfig], http_client: httpx.AsyncClient):
        """Initialize RSS scraper.

        Args:
            sources: List of RSS feed configurations
            http_client: Shared async HTTP client
        """
        super().__init__({"sources": sources}, http_client)
        self.feed_stats: List[RSSFeedStats] = []

    async def fetch(self, since: datetime) -> List[ContentItem]:
        """Fetch RSS feed items.

        Args:
            since: Only fetch items published after this time

        Returns:
            List[ContentItem]: Fetched content items
        """
        items = []
        sources = self.config["sources"]
        self.feed_stats = []

        for source in sources:
            if not source.enabled:
                continue

            feed_items = await self._fetch_feed(source, since)
            items.extend(feed_items)

        return items

    async def _fetch_feed(
        self, source: RSSSourceConfig, since: datetime
    ) -> List[ContentItem]:
        """Fetch items from a single RSS feed.

        Args:
            source: RSS feed configuration
            since: Only fetch items after this time

        Returns:
            List[ContentItem]: Feed content items
        """
        items = []
        stats = RSSFeedStats(name=source.name, url=str(source.url))

        try:
            # Expand environment variables in URL (e.g. ${LWN_TOKEN})
            feed_url = re.sub(
                r"\$\{(\w+)\}",
                lambda m: os.environ.get(m.group(1), m.group(0)).strip(),
                str(source.url),
            )

            # Fetch feed content
            response = await self.client.get(feed_url, follow_redirects=True)
            stats.status_code = response.status_code
            response.raise_for_status()

            # Parse feed
            feed = feedparser.parse(response.text)
            stats.parsed_entries = len(feed.entries)
            fetch_time = datetime.now(timezone.utc)

            for entry in feed.entries:
                # Parse published date
                published_at = self._parse_date(entry)
                metadata = {
                    "feed_name": source.name,
                    "category": source.category,
                    "tags": [tag.term for tag in entry.get("tags", [])],
                }

                if published_at:
                    stats.latest_parsed_date = self._max_datetime(
                        stats.latest_parsed_date,
                        published_at,
                    )
                    if published_at < since:
                        stats.skipped_old_items += 1
                        continue
                else:
                    published_at = fetch_time
                    stats.undated_fallback_items += 1
                    metadata["date_source"] = "fetch_time_fallback"

                # Generate unique ID from feed URL and entry ID
                feed_id = str(source.url).split("//")[1].replace("/", "_")
                entry_id = entry.get("id", entry.get("link", ""))
                entry_hash = hashlib.sha256(str(entry_id).encode("utf-8")).hexdigest()[
                    :16
                ]

                # Extract content
                content = self._extract_content(entry)

                item = ContentItem(
                    id=self._generate_id("rss", feed_id, entry_hash),
                    source_type=SourceType.RSS,
                    title=entry.get("title", "Untitled"),
                    url=entry.get("link", str(source.url)),
                    content=content,
                    author=entry.get("author", source.name),
                    published_at=published_at,
                    metadata=metadata,
                )
                items.append(item)

            if source.fetch_limit is not None and len(items) > source.fetch_limit:
                stats.limited_items = len(items) - source.fetch_limit
                items = items[: source.fetch_limit]
            stats.returned_items = len(items)

        except httpx.HTTPStatusError as e:
            stats.error = str(e)
            if e.response is not None:
                stats.status_code = e.response.status_code
            logger.warning("Error fetching RSS feed %s: %s", source.name, e)
        except httpx.HTTPError as e:
            stats.error = str(e)
            logger.warning("Error fetching RSS feed %s: %s", source.name, e)
        except Exception as e:
            stats.error = str(e)
            logger.warning("Error parsing RSS feed %s: %s", source.name, e)
        finally:
            self.feed_stats.append(stats)

        return items

    def _parse_date(self, entry: dict) -> Optional[datetime]:
        """Parse publication date from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            datetime: Parsed publication date or None
        """
        # Try different date fields
        for field in ["published", "updated", "created"]:
            if field in entry:
                try:
                    # Try parsing structured time first
                    if f"{field}_parsed" in entry and entry[f"{field}_parsed"]:
                        return datetime.fromtimestamp(
                            calendar.timegm(entry[f"{field}_parsed"]), tz=timezone.utc
                        )
                    # Fallback to string parsing
                    date_str = entry[field]
                    return self._ensure_aware(parsedate_to_datetime(date_str))
                except Exception:
                    continue

        return None

    @staticmethod
    def _ensure_aware(value: datetime) -> datetime:
        """Return an aware datetime so comparisons against UTC windows are safe."""
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)
        return value

    @staticmethod
    def _max_datetime(
        current: Optional[datetime], candidate: datetime
    ) -> datetime:
        if current is None or candidate > current:
            return candidate
        return current

    def _extract_content(self, entry: dict) -> str:
        """Extract text content from feed entry.

        Args:
            entry: Feed entry data

        Returns:
            str: Extracted text content
        """
        # Try different content fields
        if "summary" in entry:
            return entry.summary
        if "description" in entry:
            return entry.description
        if "content" in entry and entry.content:
            # content is usually a list
            return entry.content[0].get("value", "")

        return ""
