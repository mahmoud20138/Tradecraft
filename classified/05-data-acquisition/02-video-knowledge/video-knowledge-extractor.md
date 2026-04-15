---
name: video-knowledge-extractor
description: >
  Extract knowledge from any YouTube video and automatically inject it into the most
  relevant skill files. USE FOR: "watch this video and add to skills", "extract and save",
  "learn from video", "add video knowledge to skills", "youtube to skill", "update skills
  from video", "extract and route knowledge", or any YouTube URL shared by the user.
  This skill ORCHESTRATES: fetch video → extract content → identify related skills → inject knowledge.
kind: orchestrator
category: data/media
status: active
tags: [data, extractor, knowledge, media, video]
---

# Video → Knowledge → Skills Pipeline

## When to Trigger
- User shares a YouTube URL
- User says "add to skills", "learn from this", "extract and save"
- Any video about trading, AI, development, or any topic matching existing skills

## Full Pipeline

```
YouTube URL
    │
    ├── 1. FETCH METADATA  (yt-dlp / oEmbed API)
    │       title, channel, duration, chapters
    │
    ├── 2. EXTRACT CONTENT (3-tier fallback)
    │       ├── youtube-transcript-api  (fastest)
    │       ├── yt-dlp subtitle download
    │       └── WebSearch for summaries/articles about the video
    │
    ├── 3. SYNTHESIZE KNOWLEDGE (Claude)
    │       ├── Core concepts & definitions
    │       ├── Key formulas / code examples
    │       ├── Practical applications
    │       ├── Structured tables & comparisons
    │       └── Trading/domain relevance
    │
    └── 4. ROUTE TO SKILLS (auto-inject)
            ├── Scan skill files for topic overlap
            ├── Append knowledge block to matching skill(s)
            └── Report: "Added to [skill-file] → [section]"
```

## Skill Routing Map

| Video Topic | Target Skill File | Section |
|-------------|------------------|---------|
| Markov chains, statistics, time series, probability | `trading.md` | quant-backtesting / statistics-timeseries |
| ICT, SMC, order flow, liquidity, FVG | `trading.md` | ict-smart-money |
| Risk, drawdown, Kelly, Monte Carlo | `trading.md` | risk-and-portfolio |
| Backtesting, quant, ML, RL, neural nets | `trading.md` | quant-backtesting |
| Macro, news, sentiment, regime | `trading.md` | market-intelligence |
| Price action, patterns, Elliott Wave | `trading.md` | price-action-chart-analysis |
| MT5, EA, MQL5, automation | `trading.md` | mt5-trading-tools |
| Options, futures, crypto, forex | `trading.md` | asset-classes |
| Claude Code, AI agents, MCP, hooks | `claude-ai-tools.md` | — |
| Web dev, UI, architecture, testing | `development.md` | — |
| YouTube, video, web scraping | `media-web.md` | — |

## Knowledge Block Format

```markdown
---
