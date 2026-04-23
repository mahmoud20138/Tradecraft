---
name: asian-session-scalper
description: >
  Tokyo session low-volatility scalping setups — range-bound strategies for the quietest session.
  Use for "Asian scalp", "Tokyo session trade", "Asian range", "night scalping", "low vol scalp",
  "Asian session strategy", or any Tokyo-session-specific trading. Works with session-profiler.
kind: reference
category: trading/strategies
status: active
tags: [asian, scalper, scalping, session, strategies, trading, volatility]
related_skills: [jdub-price-action-strategy, session-scalping, gap-trading-strategy, grid-trading-engine, session-profiler]
---

# Asian Session Scalper

```python
import pandas as pd, numpy as np

class AsianSessionScalper:
    @staticmethod
    def range_fade(df: pd.DataFrame) -> dict:
        """Fade the range during Tokyo session — buy lows, sell highs of the range."""
        df = df.copy()
        df["hour"] = df.index.hour
        asian = df[(df["hour"] >= 0) & (df["hour"] < 7)]
        if len(asian) < 10: return {"error": "Insufficient Asian data"}
        range_high = asian["high"].rolling(20).max().iloc[-1]
        range_low = asian["low"].rolling(20).min().iloc[-1]
        mid = (range_high + range_low) / 2
        current = df.iloc[-1]["close"]
        atr = (asian["high"] - asian["low"]).mean()
        return {
            "strategy": "asian_range_fade",
            "range_high": round(range_high, 5), "range_low": round(range_low, 5),
            "midpoint": round(mid, 5),
            "signal": "BUY (near range low)" if current < range_low + atr * 0.3 else
                     "SELL (near range high)" if current > range_high - atr * 0.3 else "WAIT (mid-range)",
            "stop_pips": round(atr * 10000 * 1.5, 1),
            "target_pips": round(atr * 10000 * 1.0, 1),
            "best_pairs": ["USDJPY", "EURJPY", "AUDJPY", "AUDNZD"],
            "avoid": ["GBPUSD", "EURUSD (low liquidity in Asia)"],
        }
```

---

## Asian Breakout Strategy

```python
    @staticmethod
    def asian_breakout(df: pd.DataFrame, buffer_pips: float = 3.0) -> dict:
        """Trade the breakout of the Asian range during London open."""
        df = df.copy()
        df["hour"] = df.index.hour
        asian = df[(df["hour"] >= 0) & (df["hour"] < 7)]
        if len(asian) < 10: return {"error": "Insufficient Asian data"}
        range_high = asian["high"].max()
        range_low = asian["low"].min()
        range_size = range_high - range_low
        pip_size = 0.0001 if range_size < 1 else 0.01
        buffer = buffer_pips * pip_size
        return {
            "strategy": "asian_breakout",
            "buy_stop": round(range_high + buffer, 5),
            "sell_stop": round(range_low - buffer, 5),
            "stop_loss_pips": round(range_size / pip_size * 0.5, 1),
            "tp1_pips": round(range_size / pip_size * 1.0, 1),
            "tp2_pips": round(range_size / pip_size * 1.5, 1),
            "range_size_pips": round(range_size / pip_size, 1),
            "valid": range_size / pip_size < 40,  # Skip if range too wide
            "best_time": "07:00-09:00 UTC (London open)",
            "best_pairs": ["GBPJPY", "EURJPY", "USDJPY", "GBPUSD"],
        }
```

## Session Timing Reference

| Session | UTC Hours | Characteristics |
|---------|-----------|-----------------|
| Tokyo | 00:00-07:00 | Low volatility, range-bound, JPY pairs active |
| London Open | 07:00-09:00 | Breakout of Asian range, highest volatility spike |
| London | 07:00-16:00 | Trend development, EUR/GBP pairs active |
| NY Overlap | 12:00-16:00 | Highest liquidity, major reversals |

## Rules

1. **Only scalp in Asian session** (00:00-07:00 UTC) for range-fade strategy
2. **Avoid Mondays** — Asian ranges are unreliable after weekend gaps
3. **Skip news nights** — BOJ, RBA, RBNZ releases destroy Asian ranges
4. **Max 3 trades per session** — low volatility means low opportunity count
5. **Tight stops** — 1.5x ATR max; if stopped, do not re-enter same direction
