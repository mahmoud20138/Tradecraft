---
name: discord-webhook
description: Send trading alerts, signals, and analysis summaries to Discord via webhook. Integrates with realtime-alert-pipeline, trading-brain, and trade-journal-analytics.
kind: integration
category: trading/infrastructure
status: active
tags: [alerts, discord, hooks, infrastructure, trading, webhook]
related_skills: [notion-sync, realtime-alert-pipeline, telegram-bot, trade-copier-signal-broadcaster, trading-brain]
---

# Discord Webhook — Alert Bridge

You are a **Discord integration bridge** for trading alerts and skill outputs.

## Setup

```python
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN"
```
Save your webhook URL: `/context-memory save discord_webhook=<your_url>`

## Message Templates

### Trade Alert
```json
{
  "embeds": [{
    "title": "🎯 Trade Setup Alert",
    "color": 3066993,
    "fields": [
      {"name": "Pair", "value": "EURUSD", "inline": true},
      {"name": "Direction", "value": "🟢 BUY", "inline": true},
      {"name": "Entry", "value": "1.0845", "inline": true},
      {"name": "Stop Loss", "value": "1.0812", "inline": true},
      {"name": "Take Profit", "value": "1.0911", "inline": true},
      {"name": "R:R", "value": "2.0", "inline": true},
      {"name": "Confluence", "value": "⭐⭐⭐⭐⭐ FVG+OB+BOS", "inline": false}
    ],
    "timestamp": "2026-03-18T09:00:00Z"
  }]
}
```

### Daily Brief
```json
{
  "embeds": [{
    "title": "📊 Morning Trading Brief",
    "color": 5793266,
    "description": "[market-intelligence summary]",
    "fields": [
      {"name": "Regime", "value": "Trending Bullish", "inline": true},
      {"name": "Safe to Trade", "value": "✅ Yes", "inline": true},
      {"name": "Top Setup", "value": "EURUSD BUY @ 1.0845", "inline": false}
    ]
  }]
}
```

### Journal Summary
```json
{
  "embeds": [{
    "title": "📓 End of Day Summary",
    "color": 15158332,
    "fields": [
      {"name": "Trades", "value": "3", "inline": true},
      {"name": "P&L", "value": "+$145 (+1.45%)", "inline": true},
      {"name": "Win Rate", "value": "2/3 (67%)", "inline": true}
    ]
  }]
}
```

## Commands

```
/discord-webhook send-alert "EURUSD BUY 1.0845 SL 1.0812 TP 1.0911"
/discord-webhook send-brief          (sends morning brief from /market-intelligence)
/discord-webhook send-journal        (sends EOD summary from /trade-journal-analytics)
/discord-webhook test                (sends test message)
/discord-webhook setup <webhook_url> (saves webhook URL)
```

## Integration with Skills

Chain with:
```
/trading-brain EURUSD → /discord-webhook send-alert
/market-intelligence daily → /discord-webhook send-brief
/trade-journal-analytics EOD → /discord-webhook send-journal
```

## Python Send Function

```python
import requests, json

def send_discord_alert(webhook_url: str, embed: dict):
    payload = {"embeds": [embed]}
    response = requests.post(webhook_url, json=payload)
    return response.status_code == 204
```
