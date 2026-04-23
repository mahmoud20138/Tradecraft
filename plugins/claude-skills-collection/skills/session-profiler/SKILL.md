---
name: session-profiler
description: >
  Statistical analysis of trading sessions — London, New York, Tokyo, and their overlaps.
  Use this skill whenever the user asks about "best time to trade", "session analysis",
  "London session", "New York session", "Tokyo session", "Asian session", "session overlap",
  "session open patterns", "London open", "NY open", "session statistics", "when is the market
  most active", "session volatility", "what session are we in", "killzone", "ICT killzone",
  or any question about trading session behavior, timing, and statistical tendencies.
  Works with execution-algo-trading for entry timing and risk-calendar-trade-filter for session-based
  filters.
kind: analyzer
category: trading/strategies
status: active
tags: [ict, profiler, risk-and-portfolio, session, strategies, trading, volatility]
related_skills: [jdub-price-action-strategy, session-scalping, asian-session-scalper, gap-trading-strategy, grid-trading-engine]
---

# Session Profiler

## Overview
Statistical profiles of major trading sessions with historical tendencies, volatility patterns,
and pair-specific behavior. Use for optimal entry timing and understanding session-driven flows.

---

## 1. Session Definitions

```python
from datetime import datetime, time, timedelta
from typing import Optional
import pandas as pd
import numpy as np

SESSIONS = {
    "tokyo": {
        "name": "Tokyo / Asian",
        "open_utc": time(0, 0), "close_utc": time(9, 0),
        "peak_utc": (time(1, 0), time(6, 0)),
        "primary_pairs": ["USDJPY", "EURJPY", "GBPJPY", "AUDJPY", "AUDUSD", "NZDUSD"],
        "characteristics": "Low volatility, range-bound. Good for range strategies.",
    },
    "london": {
        "name": "London / European",
        "open_utc": time(7, 0), "close_utc": time(16, 0),
        "peak_utc": (time(7, 0), time(11, 0)),
        "primary_pairs": ["EURUSD", "GBPUSD", "EURGBP", "EURJPY", "GBPJPY", "USDCHF"],
        "characteristics": "Highest volume session. Breakouts from Asian range. Most trending moves.",
    },
    "new_york": {
        "name": "New York / US",
        "open_utc": time(13, 0), "close_utc": time(22, 0),
        "peak_utc": (time(13, 0), time(17, 0)),
        "primary_pairs": ["EURUSD", "GBPUSD", "USDJPY", "USDCAD", "USDCHF", "XAUUSD"],
        "characteristics": "Second highest volume. Major economic releases. Often reverses London moves.",
    },
    "london_ny_overlap": {
        "name": "London-NY Overlap",
        "open_utc": time(13, 0), "close_utc": time(16, 0),
        "peak_utc": (time(13, 0), time(16, 0)),
        "primary_pairs": ["ALL"],
        "characteristics": "Highest volatility window of the day. Maximum liquidity.",
    },
}

# ICT Killzones
ICT_KILLZONES = {
    "asian_kz":     {"start": time(0, 0), "end": time(4, 0), "name": "Asian Killzone"},
    "london_kz":    {"start": time(7, 0), "end": time(10, 0), "name": "London Open Killzone"},
    "ny_kz":        {"start": time(13, 0), "end": time(16, 0), "name": "NY Open Killzone"},
    "london_close": {"start": time(15, 0), "end": time(16, 0), "name": "London Close Killzone"},
}

def current_session(now: datetime = None) -> dict:
    """Determine current active session(s)."""
    now = now or datetime.utcnow()
    t = now.time()
    active = []
    for key, session in SESSIONS.items():
        if session["open_utc"] <= t <= session["close_utc"]:
            in_peak = session["peak_utc"][0] <= t <= session["peak_utc"][1]
            active.append({"session": key, "name": session["name"], "in_peak": in_peak})
    killzones = []
    for key, kz in ICT_KILLZONES.items():
        if kz["start"] <= t <= kz["end"]:
            killzones.append(kz["name"])
    return {"active_sessions": active, "killzones": killzones, "time_utc": now.strftime("%H:%M")}
```

---

## 2. Session Statistics Engine

```python
class SessionProfiler:
    """Compute statistical profiles per session from historical data."""

    @staticmethod
    def session_stats(df: pd.DataFrame, pair: str = "") -> dict:
        """Compute per-session statistics from OHLCV data."""
        df = df.copy()
        df["hour"] = df.index.hour
        df["session"] = df["hour"].apply(lambda h:
            "tokyo" if 0 <= h < 7 else
            "london" if 7 <= h < 13 else
            "ny_overlap" if 13 <= h < 16 else
            "ny_late" if 16 <= h < 22 else "off_hours"
        )
        df["range"] = df["high"] - df["low"]
        df["body"] = abs(df["close"] - df["open"])
        df["direction"] = np.where(df["close"] > df["open"], 1, -1)

        stats = {}
        for session in ["tokyo", "london", "ny_overlap", "ny_late"]:
            s = df[df["session"] == session]
            if s.empty:
                continue
            stats[session] = {
                "avg_range_pips": round(s["range"].mean() * 10000, 1),
                "max_range_pips": round(s["range"].max() * 10000, 1),
                "avg_body_pips": round(s["body"].mean() * 10000, 1),
                "bullish_pct": round((s["direction"] == 1).mean() * 100, 1),
                "bearish_pct": round((s["direction"] == -1).mean() * 100, 1),
                "bars_analyzed": len(s),
                "avg_volume": round(s["volume"].mean(), 0) if "volume" in s.columns else 0,
            }
        return {"pair": pair, "session_stats": stats}

    @staticmethod
    def session_open_patterns(df: pd.DataFrame) -> dict:
        """Analyze behavior around session opens."""
        df = df.copy()
        df["hour"] = df.index.hour
        patterns = {}

        for session, open_hour in [("london", 7), ("new_york", 13)]:
            opens = df[df["hour"] == open_hour]
            if opens.empty:
                continue
            # First hour direction
            first_hour_up = (opens["close"] > opens["open"]).mean()
            # Continuation: does the first hour direction hold?
            patterns[session] = {
                "first_bar_bullish_pct": round(first_hour_up * 100, 1),
                "avg_first_bar_range": round((opens["high"] - opens["low"]).mean() * 10000, 1),
                "note": f"{session.title()} open tends {'bullish' if first_hour_up > 0.55 else 'bearish' if first_hour_up < 0.45 else 'neutral'}",
            }
        return patterns

    @staticmethod
    def day_of_week_profile(df: pd.DataFrame) -> pd.DataFrame:
        """Statistical profile by day of week."""
        df = df.copy()
        df["dow"] = df.index.day_name()
        df["range"] = df["high"] - df["low"]
        return df.groupby("dow").agg(
            avg_range=("range", lambda x: round(x.mean() * 10000, 1)),
            bullish_pct=("close", lambda x: round((x > x.shift(1)).mean() * 100, 1)),
            avg_volume=("volume", "mean"),
        ).reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

    @staticmethod
    def hourly_volatility_profile(df: pd.DataFrame) -> pd.DataFrame:
        """Hourly volatility distribution — which hours move most."""
        df = df.copy()
        df["hour"] = df.index.hour
        df["range"] = df["high"] - df["low"]
        return df.groupby("hour").agg(
            avg_range=("range", lambda x: round(x.mean() * 10000, 1)),
            max_range=("range", lambda x: round(x.max() * 10000, 1)),
        )
```

---

## Usage: Check session context before every trade. A breakout strategy at 3AM UTC in EURUSD will fail — save it for London open.
