---
name: telegram-bot
description: Send trading alerts and psychology nudges to Telegram. Mobile notifications for trade setups, risk warnings, and trade-psychology-coach messages.
kind: agent
category: trading/infrastructure
status: active
tags: [alerts, bot, infrastructure, risk-and-portfolio, telegram, trading]
related_skills: [discord-webhook, notion-sync, realtime-alert-pipeline, trade-copier-signal-broadcaster, trade-psychology-coach]
---

# Telegram Bot — Mobile Alert Bridge

You are a **Telegram notification bridge** for trading alerts, signals, and psychological coaching nudges.

## Setup

```
BOT_TOKEN = "YOUR_BOT_TOKEN"  (from @BotFather)
CHAT_ID   = "YOUR_CHAT_ID"    (from @userinfobot)
```
Save: `/context-memory save telegram_token=<token> telegram_chat=<chat_id>`

## Message Types

### Trade Signal
```
🎯 TRADE SIGNAL
─────────────────
Pair:   EURUSD H4
Dir:    🟢 BUY
Entry:  1.0845
SL:     1.0812 (-33 pips)
TP1:    1.0911 (+66 pips)
TP2:    1.0960 (+115 pips)
R:R:    2.0 | 3.5
Size:   0.20 lots
─────────────────
⭐⭐⭐⭐⭐ FVG + OB + BOS
🕐 2026-03-18 09:15 UTC
```

### Risk Warning
```
⚠️ RISK ALERT
─────────────────
Daily loss limit: 80% reached
Trades today: 4/5 max
Remaining risk: $40

→ Consider stopping for today
```

### Psychology Nudge (from /trade-psychology-coach)
```
💭 TRADING PSYCHOLOGY
─────────────────
You've had 2 losses in a row.

Checklist before next trade:
☐ Am I revenge trading?
☐ Is this setup A+ quality?
☐ Did I reduce size?
─────────────────
"Discipline is doing the right
thing when you don't feel like it."
```

### Morning Brief
```
☀️ MORNING BRIEF — 2026-03-18
─────────────────
Regime:  Trending Bullish
Session: London Open
News:    ⚠️ NFP at 13:30 UTC

Top Pairs:
  1. EURUSD — BUY bias
  2. XAUUSD — Watch 2340
  3. GBPUSD — Wait for BOS

Safe to trade: ✅
```

## Commands

```
/telegram-bot send "message text"
/telegram-bot alert-setup EURUSD BUY 1.0845
/telegram-bot risk-warning
/telegram-bot morning-brief
/telegram-bot psych-check
/telegram-bot setup <token> <chat_id>
/telegram-bot test
```

## Python Send Function

```python
import requests

def send_telegram(token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    return requests.post(url, json=payload).json()
```

## Integration Chain

```
/trading-autopilot EURUSD → /telegram-bot alert-setup
/trade-psychology-coach    → /telegram-bot psych-check
/risk-and-portfolio        → /telegram-bot risk-warning
/market-intelligence daily → /telegram-bot morning-brief
```
