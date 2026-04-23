---
name: risk-calendar-trade-filter
description: >
  Determines when NOT to trade by mapping event blackout zones, session quality windows, and
  risk filters. Use this skill whenever the user asks "should I trade today", "is it safe to trade",
  "any events to avoid", "blackout zones", "when not to trade", "trade filter", "event risk",
  "news blackout", "rollover time", "low liquidity", "end of month", "NFP week", "FOMC week",
  or any question about trading timing safety. This is a pre-trade safety gate that should be
  checked before any entry. Works with market-news-impact for event data and session-profiler
  for session quality.
kind: reference
category: trading/risk
status: active
tags: [calendar, filter, news, risk, risk-and-portfolio, trade, trading]
related_skills: [drawdown-playbook, real-time-risk-monitor, risk-and-portfolio, risk-of-ruin, session-profiler]
---

# Risk Calendar & Trade Filter

## Overview
The "when NOT to trade" skill. Maps dangerous time windows, event blackout zones, low-liquidity
periods, and structural market hazards. Prevents entries during conditions that historically
produce poor outcomes.

---

## 1. Event Blackout Engine

```python
from datetime import datetime, timedelta
from typing import Optional

class EventBlackout:
    """Define no-trade zones around high-impact events."""

    # Default blackout windows (hours before/after event)
    BLACKOUT_RULES = {
        "HIGH": {"before_hours": 2, "after_hours": 1, "action": "NO TRADE"},
        "MEDIUM": {"before_hours": 0.5, "after_hours": 0.5, "action": "REDUCE SIZE"},
        "LOW": {"before_hours": 0, "after_hours": 0, "action": "NORMAL"},
    }

    # Special extended blackout events
    EXTENDED_BLACKOUTS = {
        "Non-Farm Payrolls":    {"before_hours": 4, "after_hours": 2},
        "FOMC Rate Decision":   {"before_hours": 6, "after_hours": 3},
        "ECB Rate Decision":    {"before_hours": 4, "after_hours": 2},
        "BOE Rate Decision":    {"before_hours": 4, "after_hours": 2},
        "BOJ Rate Decision":    {"before_hours": 4, "after_hours": 2},
        "Fed Chair Speech":     {"before_hours": 2, "after_hours": 2},
        "CPI y/y":              {"before_hours": 3, "after_hours": 1},
    }

    @staticmethod
    def check_blackout(event_name: str, event_time: datetime, impact: str, now: datetime = None) -> dict:
        now = now or datetime.utcnow()
        blackout = EventBlackout.EXTENDED_BLACKOUTS.get(event_name, EventBlackout.BLACKOUT_RULES.get(impact, {}))
        before = timedelta(hours=blackout.get("before_hours", 0))
        after = timedelta(hours=blackout.get("after_hours", 0))
        in_blackout = (event_time - before) <= now <= (event_time + after)
        return {
            "event": event_name,
            "event_time": event_time.isoformat(),
            "blackout_start": (event_time - before).isoformat(),
            "blackout_end": (event_time + after).isoformat(),
            "in_blackout": in_blackout,
            "action": "NO TRADE" if in_blackout and impact == "HIGH" else "REDUCE SIZE" if in_blackout else "CLEAR",
        }

    @staticmethod
    def check_all_events(events: list[dict], now: datetime = None) -> dict:
        now = now or datetime.utcnow()
        active_blackouts = []
        upcoming_blackouts = []
        for event in events:
            result = EventBlackout.check_blackout(
                event["name"], datetime.fromisoformat(event["datetime"]), event.get("impact", "MEDIUM"), now
            )
            if result["in_blackout"]:
                active_blackouts.append(result)
            elif datetime.fromisoformat(result["blackout_start"]) - now < timedelta(hours=6):
                upcoming_blackouts.append(result)
        return {
            "status": "BLOCKED" if any(b["action"] == "NO TRADE" for b in active_blackouts) else "REDUCED" if active_blackouts else "CLEAR",
            "active_blackouts": active_blackouts,
            "upcoming_blackouts": upcoming_blackouts,
        }
```

---

## 2. Structural Risk Filters

```python
class StructuralFilters:
    """Time-based structural risk filters."""

    @staticmethod
    def check_all(now: datetime = None) -> list[dict]:
        now = now or datetime.utcnow()
        filters = []

        # Weekend gap risk
        if now.weekday() == 4 and now.hour >= 19:
            filters.append({"filter": "friday_close", "action": "NO NEW TRADES", "reason": "Weekend gap risk — close or hedge positions"})

        # Sunday open thin liquidity
        if now.weekday() == 6 or (now.weekday() == 0 and now.hour < 2):
            filters.append({"filter": "sunday_open", "action": "NO TRADE", "reason": "Thin liquidity, wide spreads, potential gaps"})

        # Rollover period (21:00-00:00 UTC)
        if 21 <= now.hour or now.hour < 1:
            filters.append({"filter": "rollover", "action": "CAUTION", "reason": "Swap charges applied, spreads may widen"})

        # End of month / quarter rebalancing
        import calendar
        last_day = calendar.monthrange(now.year, now.month)[1]
        if now.day >= last_day - 2:
            filters.append({"filter": "month_end", "action": "CAUTION", "reason": "Month-end rebalancing flows — unusual volatility possible"})
        if now.month in [3, 6, 9, 12] and now.day >= last_day - 4:
            filters.append({"filter": "quarter_end", "action": "CAUTION", "reason": "Quarter-end — institutional rebalancing"})

        # Holiday thin markets
        # Major holidays check would use a calendar API — simplified here
        if now.month == 12 and now.day >= 23:
            filters.append({"filter": "xmas", "action": "NO TRADE", "reason": "Christmas — markets closed or extremely thin"})
        if now.month == 1 and now.day <= 2:
            filters.append({"filter": "new_year", "action": "NO TRADE", "reason": "New Year — thin markets"})

        # NFP week Friday
        if now.weekday() == 4:
            # First Friday of month = NFP day
            if 1 <= now.day <= 7:
                filters.append({"filter": "nfp_day", "action": "EXTREME CAUTION", "reason": "NFP day — expect extreme volatility in USD pairs"})

        return filters
```

---

## 3. Master Trade Filter

```python
def should_i_trade(events: list[dict] = None, now: datetime = None) -> dict:
    """
    Master function: combines all filters into a single go/no-go decision.
    Call this before EVERY trade entry.
    """
    now = now or datetime.utcnow()
    structural = StructuralFilters.check_all(now)
    event_check = EventBlackout.check_all_events(events or [], now)

    all_warnings = structural + event_check.get("active_blackouts", [])
    blockers = [w for w in all_warnings if w.get("action") in ["NO TRADE", "NO NEW TRADES", "BLOCKED"]]
    cautions = [w for w in all_warnings if w.get("action") in ["CAUTION", "REDUCE SIZE", "EXTREME CAUTION", "REDUCED"]]

    if blockers:
        verdict = "NO — do NOT trade right now"
    elif cautions:
        verdict = "YES with CAUTION — reduce position size"
    else:
        verdict = "CLEAR — safe to trade"

    return {
        "verdict": verdict,
        "can_trade": len(blockers) == 0,
        "blockers": blockers,
        "cautions": cautions,
        "upcoming_risks": event_check.get("upcoming_blackouts", []),
        "checked_at": now.isoformat(),
    }
```

---

## Usage Conventions

1. **Call `should_i_trade()` before EVERY entry** — non-negotiable
2. **Respect blackout zones** — even if the setup looks perfect
3. **Reduce size during caution periods** — don't skip the trade, just size down
4. **No new positions on Friday after 19:00 UTC** — gap risk is real
