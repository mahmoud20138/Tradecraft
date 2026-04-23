---
name: smc-python-library
description: smartmoneyconcepts — Python library implementing ICT/SMC indicators on OHLC DataFrames. 8 indicators: FVG, Swing Highs/Lows, BOS/CHoCH, Order Blocks, Liquidity, Previous High/Low, Sessions (kill zones), Retracements. pip install smartmoneyconcepts → 
kind: reference
category: trading/strategies
status: active
tags: [ict, library, order-blocks, python, smc, strategies, trading]
related_skills: [price-action, xtrading-analyze, capitulation-mean-reversion, mtf-confluence-scorer, poc-bounce-strategy]
---

# smc-python-library

USE FOR:
  - "SMC indicators in Python"
  - "FVG / order block / BOS / CHoCH detection in code"
  - "ICT kill zones in Python"
  - "smart money concepts library"
  - "programmatic SMC analysis on OHLC data"
  - "liquidity sweeps detection Python"
tags: [SMC, ICT, Python, FVG, order-blocks, BOS, CHoCH, liquidity, swing-highs-lows, kill-zones]
kind: library
category: ict-smart-money

---

## What Is smartmoneyconcepts?

Python library implementing all core ICT/SMC indicators on OHLC DataFrames.
- Repo: https://github.com/joshyattridge/smart-money-concepts
- Install: `pip install smartmoneyconcepts`
- Input: pandas DataFrame with columns `["open", "high", "low", "close", "volume"]`

---

## Installation

```bash
pip install smartmoneyconcepts
```

```python
from smartmoneyconcepts import smc
import pandas as pd
```

---

## Full API Reference

### 1. Fair Value Gap (FVG)

```python
fvg = smc.fvg(ohlc, join_consecutive=False)
```

**Returns per row:**
- `FVG`: `1` (bullish gap) · `-1` (bearish gap) · `NaN` (no gap)
- `Top`: upper boundary of the gap
- `Bottom`: lower boundary of the gap
- `MitigatedIndex`: candle index that closed/filled the gap

**Concept:**
```
Bullish FVG:  candle[i-1].high < candle[i+1].low   → gap above
Bearish FVG:  candle[i-1].low  > candle[i+1].high  → gap below
```

**Parameters:**
- `join_consecutive=True`: merges adjacent FVGs → single zone (highest top, lowest bottom)

---

### 2. Swing Highs and Lows

```python
swings = smc.swing_highs_lows(ohlc, swing_length=50)
```

**Returns:**
- `HighLow`: `1` (swing high) · `-1` (swing low) · `NaN`
- `Level`: price of the swing point

**Concept:**
```
Swing High: highest high within swing_length candles before AND after
Swing Low:  lowest low  within swing_length candles before AND after
```

---

### 3. Break of Structure (BOS) & Change of Character (CHoCH)

```python
# Requires swing_highs_lows output first
swings = smc.swing_highs_lows(ohlc, swing_length=50)
structure = smc.bos_choch(ohlc, swings, close_break=True)
```

**Returns:**
- `BOS`: `1` (bullish BOS) · `-1` (bearish BOS)
- `CHOCH`: `1` (bullish CHoCH) · `-1` (bearish CHoCH)
- `Level`: price level that was broken
- `BrokenIndex`: candle that broke the level

**`close_break` parameter:**
```
True  → break confirmed only when candle CLOSES beyond level
False → break on wick touch (high/low crosses level)
```

**BOS vs CHoCH:**
```
BOS   → continuation: structure break in direction of trend
CHoCH → reversal: structure break AGAINST current trend direction
```

---

### 4. Order Blocks (OB)

```python
swings = smc.swing_highs_lows(ohlc, swing_length=50)
ob = smc.ob(ohlc, swings, close_mitigation=False)
```

**Returns:**
- `OB`: `1` (bullish OB) · `-1` (bearish OB)
- `Top`: upper boundary
- `Bottom`: lower boundary
- `OBVolume`: sum of current + 2 previous candle volumes
- `Percentage`: strength = `min(highVol, lowVol) / max(highVol, lowVol)`

**Strength interpretation:**
```
Percentage → 1.0 (100%) = equal bull/bear volume = strongest OB
Percentage → 0.1 (10%)  = highly imbalanced = weaker OB
```

---

### 5. Liquidity

```python
swings = smc.swing_highs_lows(ohlc, swing_length=50)
liq = smc.liquidity(ohlc, swings, range_percent=0.01)
```

**Returns:**
- `Liquidity`: `1` (buy-side) · `-1` (sell-side)
- `Level`: price of liquidity cluster
- `End`: index of last swing in the cluster
- `Swept`: index of candle that swept the liquidity

**Concept:**
```
Multiple swing highs within range_percent (1%) of each other
→ clustered stops/liquidity pool above = buy-side liquidity
→ price will likely sweep these before reversing
```

---

### 6. Previous High and Low

```python
prev_hl = smc.previous_high_low(ohlc, time_frame="1D")
```

**Returns:**
- `PreviousHigh` · `PreviousLow`
- `BrokenHigh`: `1` when price breaks prior period high
- `BrokenLow`: `1` when price breaks prior period low

**Supported timeframes:** `"15m"` · `"1H"` · `"4H"` · `"1D"` · `"1W"` · `"1M"`

---

### 7. Sessions (Kill Zones)

```python
session = smc.sessions(ohlc, session="London open kill zone",
                        start_time=None, end_time=None, time_zone="UTC")
```

**Built-in sessions:**
```
"Sydney"                    "Tokyo"
"London"                    "New York"
"Asian kill zone"           "London open kill zone"
"New York kill zone"        "london close kill zone"
"Custom"                    → requires start_time + end_time "HH:MM"
```

**Returns:**
- `Active`: `1` if candle is within session · `0` if not
- `High`: session high so far
- `Low`: session low so far

---

### 8. Retracements

```python
swings = smc.swing_highs_lows(ohlc, swing_length=50)
ret = smc.retracements(ohlc, swings)
```

**Returns:**
- `Direction`: `1` (bullish move) · `-1` (bearish move)
- `CurrentRetracement%`: current retracement from last swing
- `DeepestRetracement%`: max retracement seen in this move

---

## Complete Usage Example

```python
from smartmoneyconcepts import smc
import pandas as pd

# Load OHLCV data (lowercase columns required)
df = pd.read_csv("EURUSD_H1.csv")
df.columns = ["open", "high", "low", "close", "volume"]

# Step 1: Swing structure (prerequisite for most indicators)
swings = smc.swing_highs_lows(df, swing_length=20)

# Step 2: Market structure
structure = smc.bos_choch(df, swings, close_break=True)

# Step 3: Order blocks
ob = smc.ob(df, swings, close_mitigation=False)

# Step 4: Fair value gaps
fvg = smc.fvg(df, join_consecutive=True)

# Step 5: Liquidity pools
liq = smc.liquidity(df, swings, range_percent=0.005)

# Step 6: Session filter (only trade London open kill zone)
session = smc.sessions(df, session="London open kill zone")

# Step 7: Previous day high/low
prev_hl = smc.previous_high_low(df, time_frame="1D")

# Combine: find bullish OBs that are active during London kill zone
bullish_ob = ob[ob["OB"] == 1]
london_active = session[session["Active"] == 1]
confluence = bullish_ob.index.intersection(london_active.index)
print(f"Bullish OBs during London KZ: {len(confluence)}")
```

---

## ICT Strategy Pattern: OB + FVG + BOS Confluence

```python
def find_confluences(df, swing_length=20):
    swings  = smc.swing_highs_lows(df, swing_length)
    bos     = smc.bos_choch(df, swings, close_break=True)
    ob      = smc.ob(df, swings)
    fvg     = smc.fvg(df)
    liq     = smc.liquidity(df, swings, range_percent=0.005)

    signals = []
    for i in df.index:
        bullish = (
            ob.loc[i, "OB"] == 1 if i in ob.index else False,      # Bullish OB
            fvg.loc[i, "FVG"] == 1 if i in fvg.index else False,   # Bullish FVG
            bos.loc[i, "BOS"] == 1 if i in bos.index else False,   # BOS up
        )
        if all(bullish):
            signals.append({"index": i, "type": "LONG", "level": ob.loc[i, "Bottom"]})

    return pd.DataFrame(signals)
```


---
