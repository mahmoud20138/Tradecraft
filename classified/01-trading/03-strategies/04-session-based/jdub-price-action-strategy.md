---
name: jdub-price-action-strategy
description: >
  Jdub Trades' 3-step price action framework: Direction, Location, Execution.
  Three-bar confirmation entry pattern (lead, reaction, confirmation candle).
  Key POIs: old highs/lows, PDH/PDL, opening print/previous day close.
  Two-timeframe rule for entry alignment. 9:30 AM NY open M5 scalping variant.
  1-minute Opening Range Break & Retest scalping (no bias needed).
  USE FOR: Jdub Trades strategy, three bar entry, three bar confirmation,
  direction location execution, PDH PDL trading, opening print trading,
  previous day high low retest, break and retest entry, price action
  day trading momentum, simple price action strategy, 9:30 AM scalp,
  NY open scalping, opening print scalp, first 90 minutes, gap fill trade,
  opening range candle, ORC break retest, 1 minute scalping, M1 scalp,
  opening range breakout, no bias scalping strategy.
user-invocable: false
related_skills:
  - price-action
  - session-scalping
  - technical-analysis
  - ict-smart-money
tags:
  - trading
  - strategy
  - price-action
  - jdub
  - direction
  - location
  - execution
skill_level: intermediate
kind: strategy
category: trading/strategies
status: active
---
> **Skill:** Jdub Price Action Strategy  |  **Domain:** trading  |  **Category:** strategy  |  **Level:** intermediate
> **Tags:** `trading`, `strategy`, `price-action`, `jdub`, `direction`, `location`, `execution`


# Jdub Trades — Direction, Location, Execution Strategy

> Source: "Steal My Exact Price Action Strategy (Simple & Proven)" by Jdub Trades (7 years trading experience)

---

## Core Framework

Three sequential steps that MUST be followed in order. Skipping any step = trading blindly.

```
Step 1: DIRECTION  -->  Step 2: LOCATION  -->  Step 3: EXECUTION
 (Who controls?)       (Where to trade?)       (When to enter?)
```

---

## Step 1: Direction — Who Is in Control?

Determine the market trend on the higher timeframe before anything else.

**Three market states:**
| State | Structure | Action |
|-------|-----------|--------|
| Uptrend | Higher highs + higher lows | Look for longs |
| Downtrend | Lower highs + lower lows | Look for shorts |
| Consolidation | Range-bound, no clear direction | Hands off / cautious |

**Rules:**
- Only trade trending markets — trending markets offer the best opportunities
- If the higher TF is unclear, drop one timeframe lower (e.g., Daily unclear -> check 1H)
- If still unclear after dropping one TF, do NOT trade
- Check the past 20-40 sessions on the daily chart for trend assessment

---

## Step 2: Location — Where to Place Trades

Identify key Points of Interest (POIs) where risk is lowest and reward is highest.

### POI 1: Old Highs and Old Lows
- Classic swing highs/lows with liquidity above and below
- Use as: entry zones (break+retest), profit targets, stop-loss placement
- After a sweep of these levels, look for reversal entries in the opposite direction
- These are your external liquidity levels

### POI 2: Previous Day Highs and Previous Day Lows (PDH/PDL)
- Fresh levels marked every day — heavy liquidity concentration
- **No directional bias needed** — tradeable both long and short
- Act as support/resistance with multiple touches over time
- Very high reaction rate when price revisits these levels
- Best setups: break above PDH then retest from above = long; rejection at PDH = short to PDL

### POI 3: Opening Print + Previous Day Close
- **Opening print** = first candle of NY session open (9:30 AM EST) — heavy liquidity
- **Previous day close** = 4:00 PM EST close
- Gaps between close and open create imbalances; price gravitates toward gap fill
- Best on NYSE instruments (stocks, S&P, Nasdaq futures)
- Pattern: Gap up -> push higher -> retrace to fill gap at opening print -> reaction

---

## Step 3: Execution — When and How to Enter

### Timeframe Alignment (Two-Timeframe Rule)

Entry timeframe should be ~2 timeframes below the narrative/location timeframe.

| Narrative TF | Entry TF | Style |
|-------------|----------|-------|
| Weekly / Daily | Daily / 4H | Position trading, long-term |
| 4H / 1H | 1H / 15M | Swing trading, longer day trades |
| 15M | 5M / 1M | Day trading / momentum trading |

**Why:** Going too far apart (e.g., Daily narrative -> 1M entry = 6 TFs) causes confusion. You lose context of the higher TF thesis by the time you reach the entry TF.

### The Three-Bar Confirmation Entry

The core entry model. Price must be pulling back into a key POI on the lower timeframe.

**Candle 1 — Lead Candle:**
- Pushes price toward the key level (down for long setups, up for short setups)
- Evaluate: How aggressive is the move? Big candle = strong opposition. Small body = weak pullback (better for reversal)

**Candle 2 — Reaction Candle (MOST IMPORTANT):**
- Watch form in real time at the key level
- Bullish: Are buyers stepping in? Price keeps getting pushed back above the level despite selling pressure?
- Close above the POI = bullish. Flip to green = even better
- Color matters less than the reaction quality at the level

**Candle 3 — Confirmation Candle:**
- Confirms if the setup works or fails
- Closes above C2 high = fairly bullish, expect continuation
- Closes above C1 high = VERY bullish, strong continuation
- Big wick rejection / closes at lows / turns red = setup FAILING, expect breakdown

### Entry Models (Conservative to Aggressive)

| Entry | Trigger | Stop | Probability |
|-------|---------|------|-------------|
| Conservative | C3 closes bullish | Below C3 low | Highest |
| Standard | C2 closes, enter immediately | Below C2 low | Medium (no confirmation yet) |
| Aggressive | C3 breaks C2 high while forming | Below C2 low | Lower (requires strong direction + location) |

**When to use aggressive entry:** ONLY when Step 1 (direction) and Step 2 (location) are crystal clear. Strong HTF trend + price at key level with multiple confluences.

### Bearish Three-Bar (Inverse)

Same pattern inverted for short setups:
- Lead candle pushes up into resistance/level
- Reaction candle: sellers step in, weak closure, close below level
- Confirmation candle: breaks below reaction candle low, bearish close
- Entry: short with stop above confirmation area

---

## Decision Flowchart

```
1. Check Direction (higher TF)
   ├── Uptrend (HH/HL)  -->  Look for LONGS only
   ├── Downtrend (LH/LL) -->  Look for SHORTS only
   └── Unclear/Range     -->  Drop 1 TF or STAY OUT

2. Mark Location (POIs on narrative TF)
   ├── Old highs/lows (swing structure)
   ├── PDH / PDL
   └── Opening print / prev day close

3. Execute (entry TF, ~2 TFs below narrative)
   ├── Wait for price to reach POI
   ├── Watch three-bar pattern form
   │   ├── Lead --> Reaction (buyers/sellers?) --> Confirmation
   │   └── If C3 confirms --> ENTER with stop below pattern
   └── If C3 fails --> NO TRADE, wait for next setup
```

---

## Implementation

```python
import pandas as pd
import numpy as np


def detect_three_bar_confirmation(df: pd.DataFrame, levels: list[float],
                                   tolerance_atr_mult: float = 0.5) -> list[dict]:
    """Detect three-bar confirmation patterns at key levels.

    Args:
        df: OHLCV DataFrame
        levels: Key price levels (PDH, PDL, old highs/lows, etc.)
        tolerance_atr_mult: How close price must be to level (in ATR multiples)

    Returns:
        List of detected three-bar signals with entry/stop/strength
    """
    atr = (df["high"] - df["low"]).rolling(14).mean()
    signals = []

    for level in levels:
        for i in range(2, min(20, len(df))):
            idx = len(df) - i
            if idx < 2:
                continue
            lead = df.iloc[idx - 2]
            reaction = df.iloc[idx - 1]
            confirm = df.iloc[idx]
            tol = atr.iloc[idx] * tolerance_atr_mult

            # Bullish: lead pushes down to level, reaction holds above, confirm breaks higher
            if (lead["low"] <= level + tol
                and lead["close"] < lead["open"]
                and reaction["close"] > level
                and confirm["close"] > reaction["high"]
                and confirm["close"] > confirm["open"]):
                strength = "STRONG" if confirm["close"] > lead["high"] else "MODERATE"
                signals.append({
                    "type": "bullish_three_bar", "level": level, "idx": idx,
                    "entry": round(confirm["close"], 5),
                    "stop": round(min(lead["low"], reaction["low"]) - atr.iloc[idx] * 0.1, 5),
                    "strength": strength,
                    "signal": f"BUY - three-bar at {level} ({strength})"
                })

            # Bearish: lead pushes up to level, reaction holds below, confirm breaks lower
            if (lead["high"] >= level - tol
                and lead["close"] > lead["open"]
                and reaction["close"] < level
                and confirm["close"] < reaction["low"]
                and confirm["close"] < confirm["open"]):
                strength = "STRONG" if confirm["close"] < lead["low"] else "MODERATE"
                signals.append({
                    "type": "bearish_three_bar", "level": level, "idx": idx,
                    "entry": round(confirm["close"], 5),
                    "stop": round(max(lead["high"], reaction["high"]) + atr.iloc[idx] * 0.1, 5),
                    "strength": strength,
                    "signal": f"SELL - three-bar at {level} ({strength})"
                })

    return signals


def get_daily_pois(df_daily: pd.DataFrame) -> dict:
    """Extract key Points of Interest from daily data.

    Returns PDH, PDL, previous day close, and old swing highs/lows.
    """
    if len(df_daily) < 2:
        return {}

    prev = df_daily.iloc[-2]
    pois = {
        "pdh": prev["high"],
        "pdl": prev["low"],
        "prev_close": prev["close"],
    }

    # Old swing highs/lows (last 20 sessions)
    from scipy.signal import argrelextrema
    recent = df_daily.tail(20)
    swing_highs = argrelextrema(recent["high"].values, np.greater, order=3)[0]
    swing_lows = argrelextrema(recent["low"].values, np.less, order=3)[0]

    pois["old_highs"] = [round(recent["high"].iloc[h], 5) for h in swing_highs]
    pois["old_lows"] = [round(recent["low"].iloc[l], 5) for l in swing_lows]

    return pois
```

---

## 9:30 AM Open Scalp — Time-Specific Application

> Source: "The Best 9:30 AM 5 Minute Scalping Strategy (Simple & Proven)" by Jdub Trades

Same DLE framework applied to the NY open window only.

### Rules
- **Timeframe:** M5 entries only
- **Window:** 9:30–11:00 AM EST (13:30–15:00 UTC) — close all positions by 11 AM regardless
- **Instruments:** Equities and US indices (USTECm, US500m, US30m, individual stocks)

### Pre-Market Checklist (before 9:30 AM)
Mark these levels BEFORE the open — no marking during live price action:
1. PDH and PDL
2. Previous day close (4:00 PM EST)
3. Pre-market high and low
4. H1 trend direction (bullish = HH/HL; bearish = LH/LL)

### Opening Print Setup
- **Opening Print** = the M5 candle that closes at 9:35 AM (first complete 5-min candle)
- Mark its high and low — primary POI for the entire morning session
- **Gap fill bias:** If 9:30 open ≠ previous close, expect first move to fill gap before trend resumes
- **Entry model:** Same 3-bar confirmation at the opening print level or PDH/PDL

### Gap Fill Logic
```python
def gap_fill_bias(open_930: float, prev_close: float, atr_daily: float) -> dict:
    gap = open_930 - prev_close
    gap_pct_atr = abs(gap) / atr_daily
    return {
        "gap_present": gap_pct_atr > 0.1,
        "gap_direction": "UP" if gap > 0 else "DOWN",
        "fill_target": prev_close,
        "bias": "Expect price to fill toward prev_close FIRST before trending",
        "note": "Only trade WITH trend after gap fill completes",
    }
```

### 9:30 AM Scalp Entry Checklist
```
1. H1/D1 trend direction confirmed?          Y/N
2. PDH, PDL, prev_close marked?              Y/N
3. Opening print (9:35 M5 candle) marked?    Y/N
4. Gap present → gap fill likely first?      Y/N
5. Price at key level (POI)?                 Y/N
6. 3-bar confirmation forming?               Y/N
7. Time before 11:00 AM EST?                 Y/N
→ ENTER only if all Yes
```

---

## Daily Bias Framework — Finding Direction Before the Session
*Source: "The Ultimate Daily Pattern Trading Strategy (How To Find Daily Bias)" — Jdub Trades*

### Prior Day Candle Bias Signals

Read the previous daily candle every morning to set bias:

| Prior Day Candle | Signal |
|------------------|--------|
| Closed bullish, above prior high | Bullish — look for continuation longs |
| Closed bearish, below prior low | Bearish — look for continuation shorts |
| Long wick rejection at resistance | Bearish — sellers showing strength |
| Long wick rejection at support | Bullish — buyers showing strength |
| Doji / indecision at key level | No bias — wait for next candle to resolve |
| Closed inside prior day range | Range-bound — trade extremes only |

**Rule:** No clear candle signal = no daily bias = no trade. Skip the day.

### Daily Dealing Range (Premium / Discount)

```
Top of range (PDH, swing high, D1 resistance) = Premium zone
Midpoint = Fair Value
Bottom of range (PDL, swing low, D1 support)  = Discount zone

Bullish bias + Price in Discount → A+ long setup
Bearish bias + Price in Premium  → A+ short setup
```

### Daily Location Quality Ranking

| Grade | Location | Condition |
|-------|----------|-----------|
| A+ | D1 OB or D1 FVG | Fresh (first touch) + aligned with bias |
| A | PDH / PDL | Confirmed BOS in same direction |
| B | Weekly open level | General trend direction aligned |
| C | Old swing high/low | Multiple prior touches — avoid |

**Weekly open rule:** Price above weekly open = bullish weekly bias; below = bearish. Monday's high/low acts as reference range for the week.

### Daily Bias Entry Model

```
1. D1 bias confirmed (bullish/bearish from prior candle + structure)
2. Price at key daily location (PDL, D1 OB, D1 FVG, weekly open)
3. Drop to H1 chart
4. Wait for H1 CHoCH in the direction of D1 bias
5. H1 displacement candle + H1 FVG formed
6. Enter at H1 FVG | Stop: below D1 location (distal line)
7. Target: next D1 level (PDH, swing high, D1 supply zone)
```

H1 CHoCH inside a D1 zone = institutional engagement confirmed = entry trigger.

### Pre-Session Daily Bias Checklist

```
[] D1 swing structure: HH/HL (bullish) or LH/LL (bearish)?
[] Prior day candle: what did it do? (BOS, rejection, inside bar)
[] Where is price in the dealing range? (Premium / Discount / Neutral)
[] BIAS: Bullish / Bearish / No bias (wait)
[] Key levels marked: PDH, PDL, D1 OB/FVG if present
[] Price alerts set at key levels
[] At session open: price at level? → watch H1 CHoCH + 3-bar → enter
                     price NOT at level? → wait, do not force
```

**One trade per day is enough** — the daily framework produces 1–3 setups per week; selectivity is the edge.

---

## 1-Minute Opening Range Break & Retest Scalp

> Source: "My Simple 1 Minute Scalping Strategy To Make $10,000/Month (Backtested Results)" — Jdub Trades

A **no-bias, fully mechanical** variant — simpler than DLE, doesn't require directional conviction.

### 3-Step Checklist

```
Step 1: Mark PDH + PDL (daily TF) → these are your TARGETS
Step 2: Mark Opening Range Candle high + low (M1 or M5 at 9:30 AM EST)
Step 3: Wait for break + retest + confirmation → enter toward PDH or PDL
```

### Opening Range Candle (ORC)

- The first M1 (or M5) candle at exactly 9:30 AM EST
- Mark its high (ORC-H) and low (ORC-L)
- This is your trigger zone for the entire morning session

### Entry Rules

**Bullish (long):**
1. Price breaks ABOVE ORC-H with **displacement** (impulsive candle, not a wick poke)
2. Price pulls back and **retests** ORC-H from above
3. **Confirmation candle** shows buyers defending the level (bullish close above ORC-H)
4. Enter long | Stop: just below ORC-L | Target: PDH

**Bearish (short):**
1. Price breaks BELOW ORC-L with displacement
2. Price pulls back and retests ORC-L from below
3. Confirmation candle shows sellers defending (bearish close below ORC-L)
4. Enter short | Stop: just above ORC-H | Target: PDL

### Key Filters

- **Displacement is mandatory** — slow/weak breaks = no trade
- **Confirmation at retest** — don't enter blind; need price action reaction at the level
- **If price opens above PDH** — can't target PDH for longs; use 1:2 R:R or next key level
- **No-trade rule** — if no clean break + retest forms within first 30–60 min, skip the day
- **Window:** First ~2 hours of NY session (9:30–11:30 AM EST)

### Trade Management

| Action | When |
|--------|------|
| Entry | After confirmation candle at ORC retest |
| Stop Loss | Just beyond opposite side of ORC |
| Partial TP (50%) | At LOD/HOD (nearest swing extreme) |
| Final TP | At PDH or PDL |

### Implementation

```python
import pandas as pd
import numpy as np
from datetime import time


def orc_break_retest_signal(df_m1: pd.DataFrame, pdh: float, pdl: float,
                             session_start: str = "09:30") -> dict:
    """Detect Opening Range Candle break & retest setup on M1 data.

    Args:
        df_m1: M1 OHLCV DataFrame with datetime index (EST timezone)
        pdh: Previous day high
        pdl: Previous day low
        session_start: NY session open time (default 09:30)

    Returns:
        Signal dict with entry, stop, targets, or None if no setup
    """
    # Find the opening range candle (first M1 candle at session open)
    today = df_m1.index[-1].date()
    open_time = pd.Timestamp(f"{today} {session_start}")
    orc_mask = (df_m1.index >= open_time) & (df_m1.index < open_time + pd.Timedelta(minutes=1))
    orc = df_m1.loc[orc_mask]
    if orc.empty:
        return {"signal": "NO_SETUP", "reason": "No ORC candle found"}

    orc_high = orc["high"].max()
    orc_low = orc["low"].min()

    # Get candles after ORC
    post_orc = df_m1.loc[df_m1.index > orc.index[-1]]
    if len(post_orc) < 3:
        return {"signal": "WAIT", "reason": "Not enough candles after ORC"}

    # Check for break above ORC-H with displacement
    broke_above = False
    broke_below = False
    break_idx = None

    for i, (idx, row) in enumerate(post_orc.iterrows()):
        body = abs(row["close"] - row["open"])
        candle_range = row["high"] - row["low"]
        is_displacement = body > candle_range * 0.6  # 60%+ body = displacement

        if row["close"] > orc_high and is_displacement and not broke_above:
            broke_above = True
            break_idx = i
            break

        if row["close"] < orc_low and is_displacement and not broke_below:
            broke_below = True
            break_idx = i
            break

    if not broke_above and not broke_below:
        return {"signal": "NO_SETUP", "reason": "No displacement break of ORC"}

    # Look for retest after break
    post_break = post_orc.iloc[break_idx + 1:]
    if len(post_break) < 2:
        return {"signal": "WAIT", "reason": "Waiting for retest"}

    atr = (post_orc["high"] - post_orc["low"]).mean()
    tol = atr * 0.3

    if broke_above:
        # Look for pullback to ORC-H
        for i, (idx, row) in enumerate(post_break.iterrows()):
            if row["low"] <= orc_high + tol:
                # Check next candle for confirmation
                if i + 1 < len(post_break):
                    confirm = post_break.iloc[i + 1]
                    if confirm["close"] > orc_high and confirm["close"] > confirm["open"]:
                        return {
                            "signal": "BUY",
                            "entry": round(confirm["close"], 5),
                            "stop": round(orc_low - atr * 0.1, 5),
                            "tp1": round(post_orc["high"].max(), 5),  # HOD
                            "tp2": round(pdh, 5),
                            "orc_high": round(orc_high, 5),
                            "orc_low": round(orc_low, 5),
                            "rr_to_pdh": round((pdh - confirm["close"]) / (confirm["close"] - orc_low), 1),
                        }
                return {"signal": "WAIT", "reason": "Retest found, waiting for confirmation"}

    if broke_below:
        for i, (idx, row) in enumerate(post_break.iterrows()):
            if row["high"] >= orc_low - tol:
                if i + 1 < len(post_break):
                    confirm = post_break.iloc[i + 1]
                    if confirm["close"] < orc_low and confirm["close"] < confirm["open"]:
                        return {
                            "signal": "SELL",
                            "entry": round(confirm["close"], 5),
                            "stop": round(orc_high + atr * 0.1, 5),
                            "tp1": round(post_orc["low"].min(), 5),  # LOD
                            "tp2": round(pdl, 5),
                            "orc_high": round(orc_high, 5),
                            "orc_low": round(orc_low, 5),
                            "rr_to_pdl": round((confirm["close"] - pdl) / (orc_high - confirm["close"]), 1),
                        }
                return {"signal": "WAIT", "reason": "Retest found, waiting for confirmation"}

    return {"signal": "NO_SETUP", "reason": "No retest of ORC level found"}
```

### ORC vs DLE — When to Use Which

| Condition | Use ORC Break & Retest | Use DLE |
|-----------|----------------------|---------|
| No clear trend / bias | Yes — no bias needed | No — needs direction |
| Strong trending day | Either works | Preferred (higher conviction) |
| First 30 min of session | Yes — designed for this | Yes (9:30 AM variant) |
| Instrument | Stocks, indices, forex | Same |
| Timeframe | M1 primary | M5 primary |
| Complexity tolerance | Simple / mechanical | More nuanced |

### ORC Backtest Reference (TSLA, 1 week, 100 shares)
- 5 days: 3 wins, 1 loss, 1 no-trade
- Win rate: 75% (of trades taken)
- Total P&L: +$538 (+$376, +$199.50, +$247.50, -$285)
- Average winner: +$274.33 | Average loser: -$285 | Profit factor: 2.89

---

## M1 Three-Timeframe DLE Scalp
*Source: "The Easiest 1 Minute Scalping Strategy That Actually Works" — Jdub Trades (128K views)*

DLE applied across three timeframes for the tightest possible entries:

```
D1/H1  → DIRECTION  (who controls? HH/HL or LH/LL)
M5/M15 → LOCATION   (which key level is price targeting?)
M1     → EXECUTION  (three-bar confirmation, enter fast)
```

**M1 vs M5 strategy comparison:**

| Attribute | M5 Strategy | M1 Strategy |
|-----------|------------|------------|
| Entry TF | M5 | M1 |
| Setup TF | H1/D1 | M5/M15 |
| Stop size (SPX) | 10–30 pts | 5–15 pts |
| Typical RR | 1:2 to 1:4 | 1:3 to 1:6 |
| Confirm speed | 5 min per candle | 1 min per candle |
| Best for | Beginners | Experienced / fast execution |

**M1 limit order entry:**
- Pre-place limit BUY at C2 high (long) or limit SELL at C2 low (short)
- Avoids chasing — M1 candles close fast; manual entry at C3 close = late fill

**M1 time stop:** Exit stalled scalp after 10–15 min (vs 20–30 min on M5).

**Same rules:** 11:00 AM EST hard close; gap fill first; no bias = no trade.

---

## Related Skills

- [Price Action Strategies](../price-action.md)
- [Session Scalping](../session-scalping.md)
- [Technical Analysis](../technical-analysis.md)
- [Ict Smart Money](../ict-smart-money.md)
