---
name: notion-sync
description: Sync trade journal entries, analysis notes, and skill outputs to Notion. Bidirectional — read watchlists from Notion, write trade logs back.
kind: integration
category: trading/infrastructure
status: active
tags: [infrastructure, notion, sync, trading]
related_skills: [discord-webhook, realtime-alert-pipeline, telegram-bot, trade-copier-signal-broadcaster]
---

# Notion Sync — Knowledge Base Bridge

You are a **Notion integration bridge** for syncing trading data, journal entries, and analysis to Notion databases.

## Setup

```
NOTION_TOKEN    = "secret_YOUR_TOKEN"
JOURNAL_DB_ID   = "your-journal-database-id"
WATCHLIST_DB_ID = "your-watchlist-database-id"
ANALYSIS_DB_ID  = "your-analysis-database-id"
```
Save: `/context-memory save notion_token=<token> notion_journal_db=<id>`

## Sync Operations

### Push trade journal entry
```
/notion-sync push-trade
  pair: EURUSD
  direction: BUY
  entry: 1.0845
  sl: 1.0812
  tp: 1.0911
  result: +66 pips (+$132)
  notes: "Clean FVG fill, BOS confirmed"
  rating: 5
```

### Pull watchlist from Notion
```
/notion-sync pull-watchlist
→ Returns: [EURUSD, XAUUSD, GBPUSD, USDJPY]
→ Auto-injects into /trading-brain as active pairs
```

### Push analysis notes
```
/notion-sync push-analysis
  source: trading-brain
  pair: XAUUSD
  content: [output from /trading-brain]
```

### Sync EOD summary
```
/notion-sync eod-summary
→ Reads from /trade-journal-analytics
→ Creates daily summary page in Notion
```

## Notion Database Schemas

### Trade Journal DB
| Property | Type | Example |
|---|---|---|
| Date | Date | 2026-03-18 |
| Pair | Select | EURUSD |
| Direction | Select | BUY |
| Entry | Number | 1.0845 |
| SL | Number | 1.0812 |
| TP | Number | 1.0911 |
| Result (pips) | Number | +66 |
| Result ($) | Number | +132 |
| Strategy | Select | ICT Smart Money |
| Rating | Select | ⭐⭐⭐⭐⭐ |
| Notes | Text | Clean FVG fill |
| Session | Select | London |

### Watchlist DB
| Property | Type |
|---|---|
| Pair | Title |
| Bias | Select (BUY/SELL/NEUTRAL) |
| Key Level | Number |
| Last Updated | Date |

## Python API Client

```python
from notion_client import Client

class NotionSync:
    def __init__(self, token: str):
        self.client = Client(auth=token)

    def push_trade(self, db_id: str, trade: dict):
        return self.client.pages.create(
            parent={"database_id": db_id},
            properties={
                "Pair":   {"select": {"name": trade["pair"]}},
                "Entry":  {"number": trade["entry"]},
                "Result": {"number": trade["result_pips"]},
                "Date":   {"date": {"start": trade["date"]}},
            }
        )

    def pull_watchlist(self, db_id: str):
        results = self.client.databases.query(database_id=db_id)
        return [r["properties"]["Pair"]["title"][0]["text"]["content"]
                for r in results["results"]]
```

## Integration Chain

```
/trade-journal-analytics EOD → /notion-sync eod-summary
/notion-sync pull-watchlist  → /trading-brain (auto-populates pairs)
/trading-brain EURUSD        → /notion-sync push-analysis
```
