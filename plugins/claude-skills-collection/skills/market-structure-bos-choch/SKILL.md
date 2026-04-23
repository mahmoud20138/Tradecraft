---
name: market-structure-bos-choch
description: >
  Market structure analysis — Break of Structure (BOS), Change of Character (CHoCH), premium/
  discount, market structure shifts, and candle-close swing validation (Jonathan Jarvis method).
  Use for "BOS", "break of structure", "CHoCH", "change of character", "market structure shift",
  "MSS", "structure break", "higher high higher low", "lower high lower low", "internal structure",
  "swing structure", "valid high", "valid low", "candle close validation", "mechanical structure",
  "Norfolk FX", or any market structure concept. Works on all assets (Forex, crypto, indices) and
  all timeframes. Core SMC/ICT concept. Works with liquidity-order-flow-mapper, ict-smart-money,
  smc-beginner-pro-guide, and price-action.
kind: reference
category: trading/strategies
status: active
tags: [bos, choch, crypto, forex, ict, market, strategies, structure]
related_skills: [ict-smart-money, liquidity-analysis, smc-beginner-pro-guide, ict-trading-tool, smart-money-trap-detector]
---

# Market Structure — BOS & CHoCH

## Candle-Close Validation Method (Jonathan Jarvis / Norfolk FX)

> Source: "Master Market Structure Anywhere (In 5 Seconds)" — Jonathan Jarvis (Mar 2026)

A fully mechanical system for identifying valid swing highs/lows that removes subjectivity. Works identically across **any asset** (Forex, crypto, indices) and **any timeframe** (Monthly to 1-minute).

### Core Rules

**Bullish structure — finding valid highs:**
1. After an upward move, find the **first candle that closes below the previous candle's low**
2. The highest point before that close-down = **valid high**
3. If no close-down occurs between swings, intermediate peaks are **NOT valid highs**

**Bearish structure — finding valid lows:**
1. After a downward move, find the **first candle that closes above the previous candle's high**
2. The lowest point before that close-up = **valid low**
3. If no close-up occurs between swings, intermediate troughs are **NOT valid lows**

**Identifying current swing points:**
- **Current low (bullish):** The low of the last close-down candle before the most recent BOS upward
- **Current high (bearish):** The high of the last close-up candle before the most recent BOS downward

### BOS vs CHoCH with Candle-Close Validation

| Event | Definition | Marking |
|-------|-----------|---------|
| **BOS** | Price breaks a valid high/low in the **same** trend direction (continuation) | Solid line |
| **CHoCH** | **First** BOS that reverses direction (bullish → bearish or vice versa) | Dashed line |
| **2nd BOS** | Second break in the new direction after CHoCH — typically more profitable | Solid line |

**After CHoCH:** Switch your validation method:
- Was bullish (looking for close-downs) → Now bearish (look for close-ups)
- Was bearish (looking for close-ups) → Now bullish (look for close-downs)

### Imbalance Zones

- **Imbalance** = aggressive move leaving unfilled price action (similar to FVG)
- When price pulls back into an imbalance and continues, the **remaining unfilled portion** = **leftover imbalance**
- These leftover zones act as high-probability areas of interest for entries
- Mark imbalance zones between the close-down/close-up candle and the BOS candle

### Multi-Timeframe Application

The same candle-close logic applies identically on all timeframes:
- **Monthly/Weekly** → overall directional bias (cleaner, more reliable)
- **4H/1H** → trading timeframe structure
- **5M/1M** → scalping entries (more noise but same mechanical rules)

Use multi-TF confluence: align monthly bias → weekly structure → 4H entries.

### Python Implementation (Candle-Close Method)

```python
import pandas as pd, numpy as np


class CandleCloseStructure:
    """Mechanical structure mapping via candle-close validation (Jonathan Jarvis method).
    A valid high requires a candle closing below the previous candle's low after an up-move.
    A valid low requires a candle closing above the previous candle's high after a down-move.
    """

    @staticmethod
    def find_valid_swings(df: pd.DataFrame) -> dict:
        closes = df["close"].values
        highs = df["high"].values
        lows = df["low"].values
        valid_highs, valid_lows = [], []
        trend = "bullish"  # start assumption

        for i in range(1, len(df)):
            if trend == "bullish":
                # Look for close below previous candle's low → creates valid high
                if closes[i] < lows[i - 1]:
                    # Valid high = highest point before this close-down
                    lookback = highs[:i + 1]
                    peak_idx = int(np.argmax(lookback[max(0, i - 20):i]) + max(0, i - 20))
                    valid_highs.append({"idx": peak_idx, "price": float(highs[peak_idx]),
                                        "confirmed_at": i})
            else:
                # Look for close above previous candle's high → creates valid low
                if closes[i] > highs[i - 1]:
                    lookback = lows[:i + 1]
                    trough_idx = int(np.argmin(lookback[max(0, i - 20):i]) + max(0, i - 20))
                    valid_lows.append({"idx": trough_idx, "price": float(lows[trough_idx]),
                                       "confirmed_at": i})

            # Detect BOS/CHoCH to switch trend
            if valid_highs and trend == "bullish":
                if closes[i] < valid_lows[-1]["price"] if valid_lows else False:
                    trend = "bearish"
            elif valid_lows and trend == "bearish":
                if closes[i] > valid_highs[-1]["price"] if valid_highs else False:
                    trend = "bullish"

        return {"valid_highs": valid_highs[-5:], "valid_lows": valid_lows[-5:], "current_trend": trend}
```

### Alternative: Scipy-Based Swing Detection

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class MarketStructure:

    @staticmethod
    def analyze(df: pd.DataFrame, order: int = 5) -> dict:
        highs = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows = argrelextrema(df["low"].values, np.less, order=order)[0]
        swing_highs = [(int(i), df["high"].iloc[i]) for i in highs]
        swing_lows = [(int(i), df["low"].iloc[i]) for i in lows]
        events = []

        # Detect BOS and CHoCH
        for i in range(1, len(swing_highs)):
            if swing_highs[i][1] > swing_highs[i-1][1]:
                events.append({"type": "BOS_BULLISH", "idx": swing_highs[i][0], "price": round(swing_highs[i][1], 5),
                              "meaning": "Break of Structure UP — bullish continuation"})

        for i in range(1, len(swing_lows)):
            if swing_lows[i][1] < swing_lows[i-1][1]:
                events.append({"type": "BOS_BEARISH", "idx": swing_lows[i][0], "price": round(swing_lows[i][1], 5),
                              "meaning": "Break of Structure DOWN — bearish continuation"})

        # CHoCH: trend change
        for i in range(1, min(len(swing_highs), len(swing_lows))):
            if i < len(swing_highs) and i < len(swing_lows):
                prev_trend_up = swing_highs[i-1][1] > swing_highs[max(0,i-2)][1] if i >= 2 else True
                curr_break_down = swing_lows[i][1] < swing_lows[i-1][1]
                if prev_trend_up and curr_break_down:
                    events.append({"type": "CHoCH_BEARISH", "idx": swing_lows[i][0], "price": round(swing_lows[i][1], 5),
                                  "meaning": "Change of Character — trend shifting bearish"})

        # Current structure
        if len(swing_highs) >= 2 and len(swing_lows) >= 2:
            hh = swing_highs[-1][1] > swing_highs[-2][1]
            hl = swing_lows[-1][1] > swing_lows[-2][1]
            lh = swing_highs[-1][1] < swing_highs[-2][1]
            ll = swing_lows[-1][1] < swing_lows[-2][1]
            structure = "BULLISH (HH+HL)" if hh and hl else "BEARISH (LH+LL)" if lh and ll else "TRANSITIONING"
        else:
            structure = "INSUFFICIENT DATA"

        return {
            "current_structure": structure,
            "swing_highs": swing_highs[-5:],
            "swing_lows": swing_lows[-5:],
            "recent_events": sorted(events, key=lambda e: e["idx"])[-5:],
            "latest_event": events[-1] if events else None,
        }
```
