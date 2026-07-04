---
layout: default
title: 配置指南
---

# 配置指南

Horizon 通过两个文件进行配置：`.env` 文件用于存放 API 密钥，`data/config.json` 文件用于配置信息源、AI 提供者和过滤选项。

## AI 提供者

配置用于对内容进行评分和摘要的 AI 模型。

`api_key_env` 始终是一个环境变量名，而不是 API 密钥值。
将密钥存储在 `.env` 或 shell 环境中，然后将 `api_key_env` 指向
该变量：

```bash
OPENAI_API_KEY=sk-your-key
GOOGLE_API_KEY=your-gemini-key
```

Horizon 启动时，环境变量具有更高优先级，因为
`data/config.json` 不存储密钥本身。在本地 VS Code 运行时，请在
仓库根目录创建 `.env` 文件，并从同一根目录启动 Horizon。

常见的 API 密钥变量名：

| 提供者 | `api_key_env` 值 |
| --- | --- |
| Anthropic | `ANTHROPIC_API_KEY` |
| OpenAI | `OPENAI_API_KEY` |
| Azure OpenAI | `AZURE_OPENAI_API_KEY` |
| Gemini | `GOOGLE_API_KEY` |
| MiniMax | `MINIMAX_API_KEY` |
| 阿里云 DashScope | `DASHSCOPE_API_KEY` |
| 豆包 | `DOUBAO_API_KEY` |
| DeepSeek | `DEEPSEEK_API_KEY` |

**Anthropic Claude**：

```json
{
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4.5-20250929",
    "api_key_env": "ANTHROPIC_API_KEY",
    "throttle_sec": 0
  }
}
```

**OpenAI**：

```json
{
  "ai": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key_env": "OPENAI_API_KEY",
    "throttle_sec": 0
  }
}
```

**Gemini**：

```json
{
  "ai": {
    "provider": "gemini",
    "model": "gemini-2.0-flash",
    "api_key_env": "GOOGLE_API_KEY",
    "throttle_sec": 0
  }
}
```

**Azure OpenAI**：

```json
{
  "ai": {
    "provider": "azure",
    "model": "gpt-4o-production",
    "api_key_env": "AZURE_OPENAI_API_KEY",
    "azure_endpoint_env": "AZURE_OPENAI_ENDPOINT",
    "api_version": "2024-10-21",
    "throttle_sec": 0
  }
}
```

在 `.env` 中设置 `AZURE_OPENAI_API_KEY` 和 `AZURE_OPENAI_ENDPOINT`。`model` 字段应为你的 Azure 部署名称，而不仅仅是基础模型系列名称。

**MiniMax**：

```json
{
  "ai": {
    "provider": "minimax",
    "model": "MiniMax-M3",
    "api_key_env": "MINIMAX_API_KEY",
    "throttle_sec": 0
  }
}
```

可用模型：`MiniMax-M3`、`MiniMax-M2.7`、`MiniMax-M2.7-highspeed`

**阿里云 DashScope**（兼容 OpenAI 协议）：

```json
{
  "ai": {
    "provider": "ali",
    "model": "qwen-plus",
    "api_key_env": "DASHSCOPE_API_KEY",
    "throttle_sec": 0
  }
}
```

使用 [DashScope 兼容模式](https://help.aliyun.com/zh/dashscope/developer-reference/use-dashscope-by-calling-openai-api) 的接口地址。在 `.env` 中设置 `DASHSCOPE_API_KEY`。可选：设置 `base_url` 以覆盖默认地址 `https://dashscope.aliyuncs.com/compatible-mode/v1`。

### AI 限速

如果你的模型有严格的每分钟请求上限，可以在 `data/config.json` 中降低评分速度：

```json
{
  "ai": {
    "throttle_sec": 4.5
  }
}
```

- `throttle_sec`：每评分一条内容后的等待秒数。默认值为 `0`。
- `4.5` 是一个合理的起始值，适用于大约每分钟 15 次请求的免费套餐模型。
- 如果你有足够的吞吐量余量并希望获得最高速度，请将其设回 `0`。

### AI 并发

默认情况下，AI 评分和内容增强逐条依次进行。如果你的 API 端点支持并发请求，可以提高吞吐量：

```json
{
  "ai": {
    "analysis_concurrency": 4,
    "enrichment_concurrency": 2
  }
}
```

- `analysis_concurrency`：并行评分的条目数。默认值为 `1`。
- `enrichment_concurrency`：并行增强的高分条目数。默认值为 `1`。
- 两个值都会被限制在最低 `1`。
- 每条条目已有的重试行为保持不变。
- 无论并发度如何，结果顺序保持不变。
- 如果同时使用了 `throttle_sec`，每个并发任务在处理完一条后各自独立等待。

**自定义 Base URL**（用于代理）：

```json
{
  "ai": {
    "provider": "anthropic",
    "base_url": "https://your-proxy.com/v1",
    ...
  }
}
```

对于兼容 OpenAI 的网关，Horizon 默认会发送 `temperature` 参数。如果较新的推理风格模型拒绝该参数（例如返回 `temperature is deprecated for this model` 错误），Horizon 会重试一次（不携带该参数），并记住该能力用于后续请求。

## 信息源

所有信息源均在 `config.json` 的顶层 `sources` 键下配置。

### GitHub

```json
{
  "sources": {
    "github": [
      {
        "type": "user_events",
        "username": "gvanrossum",
        "enabled": true
      },
      {
        "type": "repo_releases",
        "owner": "python",
        "repo": "cpython",
        "enabled": true
      }
    ]
  }
}
```

### Hacker News

```json
{
  "sources": {
    "hackernews": {
      "enabled": true,
      "fetch_top_stories": 30,
      "min_score": 100
    }
  }
}
```

### RSS 订阅源

```json
{
  "sources": {
    "rss": [
      {
        "name": "Blog Name",
        "url": "https://example.com/feed.xml",
        "enabled": true,
        "category": "ai-ml"
      }
    ]
  }
}
```

### Reddit

```json
{
  "sources": {
    "reddit": {
      "enabled": true,
      "fetch_comments": 5,
      "subreddits": [
        {
          "subreddit": "MachineLearning",
          "sort": "hot",
          "fetch_limit": 25,
          "min_score": 10
        }
      ],
      "users": [
        {
          "username": "spez",
          "sort": "new",
          "fetch_limit": 10
        }
      ]
    }
  }
}
```

### Telegram

Telegram 抓取使用公开的网页预览地址 `https://t.me/s/<channel>`，因此无需 API 密钥。仅支持公开频道。

```json
{
  "sources": {
    "telegram": {
      "enabled": true,
      "channels": [
        {
          "channel": "zaihuapd",
          "enabled": true,
          "fetch_limit": 20
        }
      ]
    }
  }
}
```

- `enabled` — 全局启用或禁用 Telegram 抓取
- `channels` — 要监控的公开 Telegram 频道列表
- `channel` — Telegram 频道用户名，仅填名称本身，不含 `@` 前缀或完整的 `https://t.me/` URL
- `fetch_limit` — 每次运行每个频道最多检查的最近消息数量（默认值：`20`）

### Twitter

需要一个 [Apify](https://apify.com) 账户。在 `.env` 文件中设置 `APIFY_TOKEN`。免费套餐包含每月 $5 的额度，大约可以抓取 20,000 条推文。

```json
{
  "sources": {
    "twitter": {
      "enabled": true,
      "users": ["karpathy", "ylecun"],
      "fetch_limit": 10,
      "fetch_reply_text": false,
      "max_replies_per_tweet": 3,
      "max_tweets_to_expand": 10,
      "reply_min_likes": 5
    }
  }
}
```

- `users` — 要监控的 Twitter 用户名，不含 `@` 前缀
- `fetch_limit` — 每次运行最多抓取的推文数（所有用户合计；由于 actor 限制，最低为 100）
- `fetch_reply_text` — 当为 `true` 时，获取重要推文的实际回复内容，并追加到 `--- Top Comments ---` 下方，以便 AI 可以结合社区讨论进行评分。默认禁用。
- `max_replies_per_tweet` — 每条推文最多追加的回复行数（默认值：3）
- `max_tweets_to_expand` — 每次运行最多展开回复的推文数量上限，用于控制 Apify 额度消耗（默认值：10）
- `reply_min_likes` — 仅包含至少获得此点赞数的回复（默认值：0）

该抓取器默认使用 `altimis/scweet` actor。如有需要，可以通过 `actor_id` 覆盖。

### OpenBB 金融新闻

当你想通过一个 SDK 从 yfinance、Benzinga、FMP、Intrinio、Tiingo、SEC 或 Federal Reserve 等提供者获取股票或宏观新闻时，OpenBB 非常实用。

在启用该信息源之前，请先安装可选依赖：

```bash
uv sync --extra openbb
```

如果你的平台在构建传递依赖时遇到困难，建议使用：

```bash
uv pip install --only-binary=:all: openbb openbb-benzinga
```

```json
{
  "sources": {
    "openbb": {
      "enabled": true,
      "watchlists": [
        {
          "name": "megacaps",
          "enabled": true,
          "provider": "yfinance",
          "fetch_limit": 20,
          "category": "equities",
          "symbols": ["AAPL", "MSFT", "NVDA", "GOOGL", "AMZN", "META", "TSLA"]
        }
      ]
    }
  }
}
```

- `enabled` — 全局启用或禁用 OpenBB 信息源
- `watchlists` — 命名的股票分组列表；每个 watchlist 每次运行会发起一次 `news.company()` 调用
- `name` — 在 Horizon 元数据和选择统计中显示的标签
- `provider` — OpenBB 提供者名称，例如 `yfinance` 或 `benzinga`
- `fetch_limit` — 该 watchlist 请求的最大新闻条数
- `category` — 可选标签，存储到拉取的条目上
- `symbols` — 一起抓取的股票代码；按提供者对股票代码分组，以保持请求高效

OpenBB 提供者的凭据由 OpenBB SDK 本身处理，使用其自己的环境变量或用户设置。Horizon 不会通过 `data/config.json` 传递这些密钥。

### OSS Insight（GitHub 趋势仓库）

从 [OSS Insight](https://ossinsight.io) 的公开 API 拉取星标增长最快的仓库，该 API 聚合了 GitHub 的 WatchEvents。这对于发现当前正在迅速获得星标的仓库非常有用，无需抓取 GitHub Trending 或查询 BigQuery。

```json
{
  "sources": {
    "ossinsight": {
      "enabled": true,
      "period": "past_24_hours",
      "languages": ["All", "Python", "TypeScript"],
      "keywords": [],
      "min_stars": 10,
      "max_items": 30
    }
  }
}
```

- `period` — 星标增长排名的时间窗口。支持的值：`past_24_hours`、`past_28_days`。（`past_7_days` 目前上游存在问题。）
- `languages` — 要查询的主要编程语言分类。使用 `"All"` 获取完整排名，或使用任何 GitHub 语言标签，如 `"Python"`、`"TypeScript"`、`"Rust"`、`"Jupyter Notebook"`。抓取器会为每种语言发起一个请求，然后合并结果。
- `keywords` — 可选的关键词列表（不区分大小写），用于匹配 `description`、`collection_names` 和 `repo_name`。只有包含至少一个关键词的仓库才会通过筛选。留空则收录所有 trending 仓库。
- `min_stars` — 过滤掉在该时间周期内获得星标数少于该值的仓库。
- `max_items` — 按 `stars_gained` 降序排序合并后的最终上限。

无需 API 密钥。

## 过滤

内容评分范围为 0-10：

- **9-10**：突破性 — 重大突破、范式转变
- **7-8**：高价值 — 重要进展、深度技术内容
- **5-6**：有趣 — 值得了解但不紧急
- **3-4**：低优先级 — 一般性或常规内容
- **0-2**：噪音 — 垃圾信息、无关内容或琐碎内容

```json
{
  "filtering": {
    "ai_score_threshold": 7.0,
    "time_window_hours": 24,
    "max_items": 20,
    "category_groups": {
      "ai": {
        "name": "AI / Machine Learning",
        "limit": 5,
        "categories": ["ai-news", "ai-tools", "machine-learning", "llm"]
      },
      "finance": {
        "name": "Finance",
        "limit": 5,
        "categories": ["finance", "equities", "crypto"]
      }
    },
    "default_group": "other",
    "default_group_limit": 3
  }
}
```

- `ai_score_threshold`：仅保留评分 >= 此值的内容
- `time_window_hours`：抓取过去 N 小时内的内容
- `max_items`：在所有分组限制应用之后的最终全局上限（可选）
- `category_groups`：可选的分组配额映射。每个分组必须有正数的
  `limit` 和非空的 `categories` 列表。每个分组内的条目按 AI 分数从高到低保留。
- `category_groups.*.name`：可选，在运行日志中使用的显示名称
- `default_group`：未匹配任何配置分组的条目所属的组键。默认值为 `other`。
- `default_group_limit`：可选，用于未匹配条目的正数上限。如果省略，
  未匹配条目将不受限制（除非设置了 `max_items`）。

均衡摘要过滤在 AI 评分阈值过滤和主题
去重之后、内容增强之前执行。这可以减少增强调用，只处理
可能出现在最终摘要中的条目。

分组匹配使用存储在 `ContentItem.metadata.category` 中的来源类别。
RSS 源通过 `sources.rss[].category` 暴露该字段，OpenBB watchlist
通过 `sources.openbb.watchlists[].category` 暴露。没有类别的来源将进入
默认分组。

如果同一类别出现在多个分组中，Horizon 会记录一条警告，并使用
配置顺序中第一个出现的分组。同时省略 `category_groups` 和
`max_items` 将保留之前的过滤行为。

## 环境变量替换

`data/config.json` 中的任何字符串值都支持 `${VAR_NAME}` 语法。变量在运行时从环境（包括从 `.env` 加载的值）中展开。这让你可以将密钥、特定租户的端点以及私有 URL 保留在已检入版本控制的 JSON 文件之外。

示例：

```json
{
  "ai": {
    "base_url": "${HORIZON_AI_BASE_URL}"
  },
  "sources": {
    "rss": [
      {
        "name": "LWN.net",
        "url": "https://lwn.net/headlines/full_text?key=${LWN_KEY}",
        "enabled": true
      }
    ]
  },
  "webhook": {
    "url_env": "HORIZON_WEBHOOK_URL",
    "headers": "Authorization: Bearer ${HORIZON_WEBHOOK_TOKEN}"
  }
}
```

- `${NAME}` 仅在 `NAME` 是有效的标识符（如 `LWN_KEY` 或 `HORIZON_AI_BASE_URL`）时才会被替换。
- 未设置的变量会保留为 `${NAME}` 而不会变成空字符串，这样配置错误会在下游直接暴露出来。
- 变量展开会递归作用于字典、列表和元组；非字符串值保持不变。

## 邮件订阅

邮件发送是可选的，除非 `email.enabled` 为 `true`，否则不会启用。Horizon 使用 SMTP 发送每日摘要，使用 IMAP 检查订阅/退订请求。

```json
{
  "email": {
    "enabled": true,
    "smtp_server": "smtp.qq.com",
    "smtp_port": 465,
    "smtp_username": null,
    "imap_enabled": true,
    "imap_server": "imap.qq.com",
    "imap_port": 993,
    "email_address": "xxx@qq.com",
    "password_env": "EMAIL_PASSWORD",
    "sender_name": "Horizon Daily",
    "subscribe_keyword": "SUBSCRIBE",
    "unsubscribe_keyword": "UNSUBSCRIBE"
  }
}
```
