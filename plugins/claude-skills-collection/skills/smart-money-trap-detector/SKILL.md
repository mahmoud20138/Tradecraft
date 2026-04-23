---
name: smart-money-trap-detector
description: >
  Detect fake breakouts, stop hunts, liquidity grabs, and institutional traps. Use for "fake
  breakout", "trap", "stop hunt", "liquidity grab", "bull trap", "bear trap", "false break",
  "smart money trap", "institutional trap", "fakeout", or any trap/fake-out detection.
  Works with liquidity-order-flow-mapper and market-structure-bos-choch.
kind: analyzer
category: trading/strategies
status: active
tags: [breakout, detector, money, smart, smart-money, strategies, trading, trap]
related_skills: [ict-smart-money, liquidity-analysis, smc-beginner-pro-guide, ict-trading-tool, market-structure-bos-choch]
---

# Smart Money Trap Detector

```python
import pandas as pd, numpy as np

class TrapDetector:
    @staticmethod
    def detect_traps(df: pd.DataFrame, lookback: int = 20) -> list[dict]:
        traps = []
        atr = (df["high"] - df["low"]).rolling(14).mean()
        high_n = df["high"].rolling(lookback).max()
        low_n = df["low"].rolling(lookback).min()
        for i in range(lookback + 1, len(df)):
            bar = df.iloc[i]
            prev = df.iloc[i - 1]
            # Bull trap: breaks above resistance then closes below
            if bar["high"] > high_n.iloc[i - 1] and bar["close"] < high_n.iloc[i - 1]:
                wick = bar["high"] - max(bar["open"], bar["close"])
                if wick > atr.iloc[i]:
                    traps.append({"type": "bull_trap", "time": df.index[i], "level": round(high_n.iloc[i-1], 5),
                                 "wick_pips": round(wick * 10000, 1), "signal": "SELL — false breakout above resistance"})
            # Bear trap: breaks below support then closes above
            if bar["low"] < low_n.iloc[i - 1] and bar["close"] > low_n.iloc[i - 1]:
                wick = min(bar["open"], bar["close"]) - bar["low"]
                if wick > atr.iloc[i]:
                    traps.append({"type": "bear_trap", "time": df.index[i], "level": round(low_n.iloc[i-1], 5),
                                 "wick_pips": round(wick * 10000, 1), "signal": "BUY — false breakout below support"})
        return traps[-10:]

    @staticmethod
    def trap_probability(df: pd.DataFrame, lookback: int = 100) -> dict:
        """Historical trap frequency — helps calibrate breakout vs trap expectations."""
        traps = TrapDetector.detect_traps(df, 20)
        high_breaks = ((df["high"] > df["high"].rolling(20).max().shift(1))).sum()
        low_breaks = ((df["low"] < df["low"].rolling(20).min().shift(1))).sum()
        bull_traps = sum(1 for t in traps if t["type"] == "bull_trap")
        bear_traps = sum(1 for t in traps if t["type"] == "bear_trap")
        return {
            "total_breakouts_up": int(high_breaks),
            "bull_trap_pct": round(bull_traps / max(high_breaks, 1) * 100, 1),
            "total_breakouts_down": int(low_breaks),
            "bear_trap_pct": round(bear_traps / max(low_breaks, 1) * 100, 1),
            "recommendation": "High trap rate — wait for retest confirmation" if (bull_traps + bear_traps) / max(high_breaks + low_breaks, 1) > 0.4 else "Low trap rate — breakouts tend to follow through",
        }
```

## Automated Fake Breakout Filter via Liquidity Sweep (CodeTrading)

> Source: "Automated Break Out Detection in Python" by CodeTrading (Nov 2025)

A Python-automated approach to filtering fake breakouts:
- Simple breakout (close above pivot high) has high failure rate — price often reverts
- **Liquidity sweep confirmation:** The pivot low between the resistance level and breakout candle must be LOWER than all previous pivot lows in the lookback window
- This sweep indicates stop-loss hunting occurred before the breakout → higher probability of genuine move
- Additional filter: EMA trend confirmation (15+ candles all above/below EMA)
- Tested on 20 years EURUSD hourly data with positive results
- Best used as automated alert, not standalone strategy

For full implementation details, see `breakout-strategy-engine` skill.

## Delta Ladder for Fake Move Detection (Trading IQ)

> Source: "I Built an Indicator that exposes FAKE Moves EVERYTIME" by Trading IQ (Mar 2026)

The Delta Ladder indicator (free on TradingView) exposes fake moves by showing delta at each price level within a candle:
- **Fake bullish move:** Price makes higher high + higher low, but delta ladder shows heavy red (sellers dominating) = absorption, move won't hold
- **Delta momentum divergence:** Price rising strongly but delta falling off candle-to-candle = weakening conviction, potential reversal
- Complements structural fake breakout detection (see `breakout-strategy-engine`) with volume-based confirmation

For full delta ladder analysis methods, see `order-flow-delta-strategy`.
