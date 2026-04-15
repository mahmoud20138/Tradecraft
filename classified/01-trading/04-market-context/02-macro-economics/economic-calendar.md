---
name: economic-calendar
description: >
  Economic calendar data: high-impact event detection, news avoidance windows,
  pre-event volatility expansion, post-event fade, event-driven trade setup.
  USE FOR: economic calendar, economic events, news events, NFP, CPI, FOMC, GDP,
  PMI, retail sales, high impact news, news avoidance, pre-news, post-news,
  event risk, news trading, data release, central bank, interest rate decision.
related_skills:
  - market-intelligence
  - news-intelligence
  - strategy-selection
tags:
  - trading
  - data
  - calendar
  - news
  - high-impact
  - avoidance
skill_level: beginner
kind: reference
category: trading/data
status: active
---
> **Skill:** Economic Calendar  |  **Domain:** trading  |  **Category:** data  |  **Level:** beginner
> **Tags:** `trading`, `data`, `calendar`, `news`, `high-impact`, `avoidance`


# Economic Calendar

## High-Impact Events by Currency
| Event | Currency | Frequency | Typical Impact |
|-------|----------|-----------|----------------|
| NFP (Non-Farm Payrolls) | USD | Monthly (1st Fri) | 50–150 pips |
| FOMC Rate Decision | USD | 8x/year | 50–200 pips |
| CPI (Inflation) | USD/EUR/GBP | Monthly | 30–100 pips |
| GDP | USD/EUR/GBP | Quarterly | 20–80 pips |
| PMI (Mfg/Services) | Multi | Monthly | 20–60 pips |
| BoE/ECB/BoJ Decision | GBP/EUR/JPY | 8x/year | 50–150 pips |
| EIA Oil Inventory | OIL | Weekly (Wed 14:30 UTC) | $0.50–2.00 |

## News Avoidance Windows
```python
from datetime import datetime, timedelta

def is_news_blackout(event_time: datetime, current_time: datetime,
                     impact: str = "HIGH") -> bool:
    """Should we avoid trading near this news event?"""
    windows = {"HIGH": (30, 15), "MEDIUM": (15, 5), "LOW": (5, 0)}  # (before_min, after_min)
    before, after = windows.get(impact, (30, 15))
    start = event_time - timedelta(minutes=before)
    end   = event_time + timedelta(minutes=after)
    return start <= current_time <= end

def news_risk_level(minutes_to_event: float) -> str:
    if minutes_to_event < 5:   return "EXTREME — do not trade"
    if minutes_to_event < 15:  return "HIGH — reduce size 50%"
    if minutes_to_event < 30:  return "ELEVATED — tight stops"
    return "NORMAL"
```

## Fetch Calendar (Investing.com scrape)
```python
import requests
from bs4 import BeautifulSoup

def get_todays_events(min_impact: str = "high") -> list:
    """Scrape Investing.com economic calendar for today's events."""
    # Note: Use WebSearch tool to get current day's events
    # WebSearch query: f"site:investing.com economic calendar today {min_impact} impact"
    pass

# Alternative: use Brave Search via WebSearch tool
CALENDAR_QUERY = "economic calendar high impact events today forex"
```

## Pre-Event Volatility Strategy
- **30 min before high-impact**: Spreads widen, stops get hunted — close scalps
- **Straddle setup**: Place buy stop + sell stop at current price ±(avg_range/3) before NFP
- **Post-event fade**: If spike > 2× ATR, fade back within 5–15 min (70% fill rate)

## Key UTC Times (Daily Schedule)
```python
DAILY_EVENTS = {
    "00:30": "AUD data (RBA related)",
    "07:00": "EUR data + London open",
    "09:30": "GBP data",
    "12:30": "USD major data (CPI, NFP, retail)",
    "13:30": "NYSE open — US equity data",
    "14:30": "EIA oil inventory (Wednesday only)",
    "18:00": "FOMC (when scheduled)",
    "22:00": "NZD/AUD data + NY close",
}
```

---

## Related Skills

- [Market Intelligence](../market-intelligence.md)
- [News Data Stream](../news-intelligence.md)
- [Strategy Selection](../strategy-selection.md)
