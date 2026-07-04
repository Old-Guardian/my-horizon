from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

import httpx

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper


def _client_for_feed(feed: str) -> AsyncMock:
    response = MagicMock()
    response.text = feed
    response.status_code = 200
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    return client


def test_rss_ids_are_deterministic() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    client = _client_for_feed(feed)
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    first = asyncio.run(scraper.fetch(since))[0].id
    second = asyncio.run(scraper.fetch(since))[0].id

    assert first == second
    assert first == "rss:example.com_feed.xml:5e2d5d1e58e94d76"


def test_undated_rss_entries_use_fetch_time_fallback() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Undated Item</title>
        <link>https://example.com/undated</link>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], _client_for_feed(feed))
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))

    assert len(items) == 1
    assert items[0].metadata["date_source"] == "fetch_time_fallback"
    assert items[0].published_at.tzinfo is not None
    assert scraper.feed_stats[0].parsed_entries == 1
    assert scraper.feed_stats[0].returned_items == 1
    assert scraper.feed_stats[0].undated_fallback_items == 1


def test_old_dated_rss_entries_are_skipped() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>old-entry</guid>
        <title>Old Item</title>
        <link>https://example.com/old</link>
        <pubDate>Thu, 23 Apr 2026 12:00:00 GMT</pubDate>
      </item>
    </channel></rss>
    """
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], _client_for_feed(feed))
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))

    assert items == []
    assert scraper.feed_stats[0].parsed_entries == 1
    assert scraper.feed_stats[0].returned_items == 0
    assert scraper.feed_stats[0].skipped_old_items == 1
    assert scraper.feed_stats[0].latest_parsed_date == datetime(
        2026, 4, 23, 12, 0, tzinfo=timezone.utc
    )


def test_rss_fetch_limit_caps_after_filtering() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>new-1</guid>
        <title>New 1</title>
        <link>https://example.com/new-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
      </item>
      <item>
        <guid>old-entry</guid>
        <title>Old</title>
        <link>https://example.com/old</link>
        <pubDate>Thu, 23 Apr 2026 12:00:00 GMT</pubDate>
      </item>
      <item>
        <guid>new-2</guid>
        <title>New 2</title>
        <link>https://example.com/new-2</link>
        <pubDate>Fri, 24 Apr 2026 13:00:00 GMT</pubDate>
      </item>
      <item>
        <guid>new-3</guid>
        <title>New 3</title>
        <link>https://example.com/new-3</link>
        <pubDate>Fri, 24 Apr 2026 14:00:00 GMT</pubDate>
      </item>
    </channel></rss>
    """
    source = RSSSourceConfig(
        name="Test", url="https://example.com/feed.xml", fetch_limit=2
    )
    scraper = RSSScraper([source], _client_for_feed(feed))
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    items = asyncio.run(scraper.fetch(since))

    assert [item.title for item in items] == ["New 1", "New 2"]
    assert scraper.feed_stats[0].parsed_entries == 4
    assert scraper.feed_stats[0].returned_items == 2
    assert scraper.feed_stats[0].skipped_old_items == 1
    assert scraper.feed_stats[0].limited_items == 1


def test_rss_feed_stats_record_errors() -> None:
    request = httpx.Request("GET", "https://example.com/feed.xml")
    error = httpx.RequestError("connection failed", request=request)
    client = AsyncMock()
    client.get.side_effect = error
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)

    items = asyncio.run(scraper.fetch(datetime(2026, 4, 24, tzinfo=timezone.utc)))

    assert items == []
    assert scraper.feed_stats[0].parsed_entries == 0
    assert scraper.feed_stats[0].returned_items == 0
    assert "connection failed" in scraper.feed_stats[0].error
