---
name: capitulation-mean-reversion
description: >
  Lance Breitstein's $100M+ capitulation mean reversion framework — 7-variable checklist,
  slope analysis for waterfalls, "Right Side of the V" entry method, multi-variable mental
  rubric scoring, and prior-bar-highs/lows trailing system. Covers the complete decision
  framework from scanning to entry to trade management. Source: Chart Fanatics interview
  (Market Wizard, Trillium's top trader 2020-2021).
  Use this skill for "capitulation trade", "Lance Breitstein", "Breitstein strategy",
  "right side of the V", "waterfall mean reversion", "capitulation bounce", "slope analysis",
  "prior bar highs entry", "capitulation volume", "extreme mean reversion", "panic bounce",
  "asymptotic selloff", "multi-variable rubric", "V-bottom trade", "capitulation checklist",
  "waterfall pattern", "boring stock panic", "equilibrium reversion", "expected value framework",
  "extreme move bounce", "forced liquidation trade", "volume capitulation entry",
  "market wizard strategy", "institutional capitulation".
  Works with mean-reversion-engine, market-regime-classifier, risk-and-portfolio,
  volume-profile-strategy, and trading-brain.
kind: reference
category: trading/strategies
status: active
tags: [capitulation, mean, mean-reversion, regime, reversion, risk-and-portfolio, strategies, trading]
related_skills: [price-action, xtrading-analyze, market-regime-classifier, mean-reversion-engine, mtf-confluence-scorer]
---

# Lance Breitstein's Capitulation Mean Reversion Framework

> **Source:** Lance Breitstein — verified $100M+ trader, Trillium Capital's #1 trader (2020 & 2021),
> all-time firm PNL record holder, adviser to SMB Capital, featured in Jack Schwager's upcoming
> *Market Wizards: The Next Generation*. Chart Fanatics interview (March 2026).

## Core Philosophy

Markets are extremely efficient. The starting price is usually the RIGHT price. The strategy
focuses on identifying moments when price has moved FAR from equilibrium and stacking variables
to create massive positive expected value for the reversion trade.

**Expected Value Formula:**
```
EV = (Win Rate x Reward) - (Loss Rate x Risk)
```

The entire system is about shifting EVERY component of this equation in your favor simultaneously.

---

## The 7-Variable Checklist

At any given moment, Lance is constantly weighing ALL factors dynamically. Each variable is
scored on a mental 0-10 scale.

### Variable 1: Size of Move
- S&P down 1 penny? Not interesting. S&P down $100? Very interesting.
- The LARGER the move from equilibrium, the more appealing for mean reversion.
- Measure in % terms AND absolute terms relative to normal ranges.

### Variable 2: Speed / Rate of Change (THE MOST IMPORTANT)
- A 5% move over a year = not interesting.
- A 5% move in 1 minute = extremely interesting.
- **Slope analysis grades:**

| Slope    | Description             | Tradeable?                                    |
|----------|-------------------------|-----------------------------------------------|
| -0.5     | Slow, steady decline    | **NO** — grinding, not capitulating            |
| -1       | Moderate acceleration   | Getting interesting                            |
| -3       | Sharp selloff           | Good setup territory                           |
| -10      | Asymptotic waterfall    | **BEST setups** — "we love this"               |

- **The ideal pattern:** Boring/stable -> steady decline -> acceleration -> WATERFALL (asymptotic).
- Rate of change CRESCENDO is the key visual signature.

### Variable 3: News Presence
- **No news = best.** The move is purely technical/sentiment-driven, equilibrium hasn't changed.
- Fundamental news that changes fair value SHIFTS the equilibrium — less appealing for reversion.
- Old/stale news driving fresh panic = still acceptable (news already priced in prior move).

### Variable 4: Number of Days/Bars in a Row
- Efficient market theory says each day is independent 50/50. **Lance says this is absolutely not true.**
- S&P down 3% for 8 days straight? The probability of bouncing on day 9 is FAR above 50%.
- More consecutive directional bars = higher probability of reversal.
- **This is a fractal** — applies on 2-min bars, hourly, daily, weekly.

### Variable 5: Forced Buying/Selling
- Forced liquidations (margin calls, redemptions, loss of borrow).
- When hedge funds MUST sell billions regardless of price, the clearing mechanism creates
  extreme dislocation from fair value.
- COVID crash was a textbook example of forced selling creating capitulation opportunities.

### Variable 6: Sentiment
- Euphoria = "nothing can ever go wrong" = short opportunity.
- Despair = "nothing will ever go right again" = long opportunity.
- Truth is always somewhere in the middle.
- Sentiment EXTREMES are what create the best mean reversion setups.

### Variable 7: Diversification / Market Cap / "Boringness"
- **The more boring and stable = the better the mean reversion trade.**
- Ranking (safest to riskiest for mean reversion):
  1. Government bonds (quantifiable par value, near-zero default risk)
  2. S&P 500 / diversified indices
  3. Large-cap blue chips (Bank of America, Apple)
  4. Mid-caps with analyst coverage
  5. Small/micro-caps (least safe, but can produce biggest moves)
  6. Crypto/Bitcoin (no cash flows, but increasingly institutionalized)

- **Sub-factors within this variable:**
  - How quantitative/calculable is fair value? (Bonds > stocks > crypto)
  - How many "eyes" are on it? (More attention = faster mean reversion)
  - How stable historically? (Low ATR relative to current move = better)
  - What are normal average trading ranges? (Current bars should be MULTIPLES of normal)

### Bonus Variable: Long vs Short (Structural Asymmetry)
- **Longs have a $0 floor** = maximum loss is capped.
- **Shorts have unlimited risk** = no upper bound.
- This structural difference means long-side capitulation trades are inherently safer.
- Short-side waterfall plays require SMALLER size to compensate for tail risk.

---

## The Mental Rubric / Scoring System

Lance runs a mental tally across all variables, each scored 0-10:

```
Example:  Rate of Change = 9
          Daily Chart     = 9
          Intraday Setup  = 6
          Boringness      = 2
          ────────────────────
          TOTAL           = 26
```

### Grade Thresholds

| Score  | Grade    | Action                                              |
|--------|----------|-----------------------------------------------------|
| 35-40+ | A++ / A+ | Max conviction, aggressive sizing, exponential bet   |
| 26-34  | A / B+   | Strong trade, meaningful size                        |
| 20-25  | B / C+   | Acceptable, moderate-to-small size                   |
| 15-19  | C        | Marginal, very small size if taken at all             |
| <15    | NO TRADE | **Pass.** Not enough variables aligned               |

### Additional Variables to Score (Beyond Core 7)
- Daily chart structure (support levels, trend context)
- Intraday chart pattern quality
- Distance from Bollinger Band (above upper or below lower)
- Distance from 20-period moving average
- Number of legs in the move (3+ legs = much better)
- Sector behavior (is the whole sector weak, or just this stock?)
- Seasonal patterns
- Comparable stocks' behavior
- Volume relative to average (capitulation volume = massive spike)

**Critical insight:** No single variable makes or breaks the trade. It's the COMBINATION.
Like drafting a basketball player: "tall" matters, but tall + no arms + no coordination = bad pick.

---

## Entry Method: The "Right Side of the V"

### The #1 Rule: Do NOT Buy the Front Side

Buying on the way DOWN leads to:
1. Buy here, stop out. Buy again, stop out. Buy again, stop out.
2. Losses accumulate. When the REAL turn comes, you're licking wounds and miss it.
3. Worst case: you flip to the other side at the exact bottom/top.

**Wait for the TURN.**

### Three Ways to Define the Turn

#### Method 1: Break of Trendline
```
Price action:     \
                   \
                    \     <-- Trendline drawn across the declining highs/lows
                     \
                      \  /  <-- Break above trendline = ENTRY
                       \/
```
- Draw the trendline connecting the declining price action.
- Entry triggers when price breaks above (for longs) or below (for shorts) that trendline.

#### Method 2: Break of Prior Bar Highs (Most Common)
```
Price action:  |    |    |    |
               |H   |H   |H   |H
               ||   ||   ||   ||
               |L   |L   |L   |L ← LOWEST BAR

Entry: When price breaks ABOVE the HIGH of the prior bar after the lowest bar.
Stop:  LOW of the move (the lowest point).
```
- The prior day's/bar's high is already defined = can set limit/stop orders in advance.
- Very hands-off for higher timeframe traders.
- **Works as a fractal**: 2-min, 5-min, hourly, daily bars.

#### Method 3: Break of Lower-Lows / Lower-Highs Pattern
```
     HH
    / \
   /   \        ← HIGHER HIGH forms
  HL    \       ← HIGHER LOW holds
         \
    LL    LL    ← Was making LOWER LOWS
   LH   LH     ← Was making LOWER HIGHS
```
- When the pattern shifts from lower-lows/lower-highs to higher-highs/higher-lows.
- Entry on confirmation of the higher high.
- Stop: violation of the higher low.

#### Exception: Intra-Bar Turn (Extreme Scenarios Only)
- If Apple drops from $100 to $1 in one bar, waiting for prior bar highs at $98 makes no sense.
- In the MOST EXTREME waterfalls (95+ score), buy the intra-bar reversal.
- **Use significantly smaller size** when buying front-side / intra-bar.
- Reserve for truly exceptional capitulations (Bitcoin 5% in 4 minutes, etc.).

---

## Stop Loss & Trade Management

### Stop Placement
- **Primary stop:** Low of the move (for longs) / High of the move (for shorts).
- **Pattern stop:** If using Method 3, stop = violation of the higher low pattern.
- **Wick consideration:** Large wicks increase stop distance. Factor this into position sizing
  and whether the R:R is still acceptable.

### Trailing System
- **For longs:** Trail using PRIOR BAR LOWS. Each new bar that holds a higher low, your
  stop moves up to that bar's low.
- **For shorts:** Trail using PRIOR BAR HIGHS. Each new bar that holds a lower high, your
  stop moves down to that bar's high.
- This simple trailing system captured Lance's best trade of his career.

### Profit Target / Equilibrium
- **20-period Moving Average (Bollinger midline)** = the equilibrium/mean reversion target.
- Base case: 50% retracement of the capitulation move.
- Strong setups: 80-100% retracement (full round-trip back to equilibrium).
- Weaker setups: smaller, choppier bounce — often doesn't reach the MA.

### Win Rate Estimation by Setup Quality

| Setup Quality | Estimated Win Rate | Expected Retracement |
|---------------|-------------------|---------------------|
| A++ (score 40) | 80-90%           | 80-100% to MA       |
| A (score 30+)  | 70-80%           | 50-80% retracement   |
| B (score 25)   | 60-70%           | 40-60% retracement   |
| C (score 20)   | 50-55%           | 20-40% retracement   |
| Below C        | <50% (coin flip)  | **Don't trade**      |

**Key insight:** Even 1:1 R:R is profitable with 70-80% win rate. You don't need huge R:R
on every trade — the high win rate on A-grade setups drives the PnL.

---

## Real-World Examples & Pattern Library

### Example 1: OCLR (Oct 27, 2016) — Grade: A
- **Setup:** Boring semiconductor, stable off open. Slope crescendoed from -0.5 to waterfall.
- **Volume:** Massive capitulation spike. Stock fell ~20%.
- **Daily context:** Normal ATR ~30 cents. Now moving 30 cents PER BAR.
- **Entry:** Break of prior bar highs at ~$7.25.
- **Stop:** Low of move.
- **Exit:** Trailed prior bar lows, stopped out near 20MA at ~$7.57.
- **Result:** ~30 cent gain, ~1:1 R:R, estimated 70-80% win rate.
- **Lesson:** Textbook pattern. Prior bar highs held cleanly all the way down.

### Example 2: NGD (Jan 31, 2017) — Grade: C
- **Setup:** Gold stock (boring sector). Had news prior day, wider ATR. 25%+ total decline.
- **Issue:** Large wick on reversal candle = 13 cent stop distance.
- **Not as clean:** Didn't crescendo as dramatically. Less stable off open.
- **Result:** Weaker bounce (as expected from lower grade).
- **Lesson:** Quality of variables directly correlates to bounce quality.

### Example 3: KODK/Kodak (Jul 29, 2020) — Grade: A++ (95/100)
- **Setup:** Ultra-boring $2 stock. Operation Warp Speed news + massive short squeeze. $2 -> $60.
- **Daily:** Volume so extreme prior bars' volume is invisible on chart.
- **Intraday:** 7 consecutive green bars, massive distance from MA ($26 MA vs $60 price).
- **Entry:** Short the break of prior bar lows.
- **Result:** ~$20/share gain, ~3:1 R:R, ~70%+ win rate.
- **Risk factor:** Short side = uncapped risk. Used smaller size despite A++ grade.
- **Lesson:** Best trade of 2020 for many. One of the most extreme examples of the framework.

### Example 4: UAMY (Oct 2025) — Grade: B+ / A-
- **Setup:** Rare earth stock, historically boring (20-30 cents). Doubled in 1-2 weeks on trade war.
- **Daily bars expanding:** $1 range -> $3 -> $4 -> $5 range bars.
- **Cleanly held prior bar lows:** 8-9 consecutive bars up.
- **Entry:** Short break of prior bar lows at ~$15.50.
- **Deductions:** Short side, low market cap, less liquid.
- **Result:** ~$3/share gain. Trailing prior bar highs.

### Example 5: Bitcoin (Nov 2025) — Grade: A (Swing Long)
- **Setup:** 3 legs down, 30%+ decline over weeks. Stable -> panicked 5% in 4 minutes at 2:30am.
- **Daily:** Highest volume flush, most extended below Bollinger. Normal bar range $1-2K, this bar $8K.
- **Entry:** Had blind bids in (front-side, small size). Added on trend break above MA.
- **Intra-bar bounce:** Nearly 100% retracement on the flush candle.
- **Swing management:** Still holding core, trailing prior bar lows.
- **Deduction:** Bitcoin not quantifiable (no cash flows), but institutionalized.

---

## Scanning / Finding Setups

### Daily Chart Filters
```
Scan for:
1. Price BELOW lower Bollinger Band (20, 2.0)
2. Price ABOVE upper Bollinger Band (20, 2.0)
3. Consecutive UP days >= 4 (for short setups)
4. Consecutive DOWN days >= 4 (for long setups)
5. Volume > 3x 20-day average volume
6. Distance from 20MA > 2x ATR(14)
7. ATR expansion: today's range > 3x ATR(14)
```

### Intraday Filters
```
Scan for:
1. Holding prior bar highs (declining, clean waterfall)
2. Holding prior bar lows (rising, clean melt-up)
3. Volume capitulation spike (> 5x average bar volume)
4. Distance from intraday VWAP or Bollinger midline
5. Multiple ATR moves from open
```

### Mindset
- Never pre-commit to specific tickers. Trade whatever offers the BEST opportunity.
- Move to where the extreme setups are — different stocks/products each day.
- Pocket aces (A++ setups) are rare. Most days are B/C setups or no-trades.

---

## Python Implementation

```python
import pandas as pd
import numpy as np
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CapitulationScore:
    """Multi-variable rubric for scoring capitulation setups."""
    size_of_move: float = 0        # 0-10
    rate_of_change: float = 0      # 0-10 (THE most important)
    news_absence: float = 0        # 0-10 (10 = no news)
    consecutive_bars: float = 0    # 0-10
    forced_flow: float = 0         # 0-10
    sentiment_extreme: float = 0   # 0-10
    boringness: float = 0          # 0-10
    daily_chart: float = 0         # 0-10
    intraday_setup: float = 0      # 0-10
    volume_capitulation: float = 0 # 0-10
    distance_from_ma: float = 0    # 0-10
    num_legs: float = 0            # 0-10
    long_vs_short: float = 0       # 0-10 (10 = long with $0 floor, lower for shorts)

    @property
    def total_score(self) -> float:
        return sum([
            self.size_of_move, self.rate_of_change, self.news_absence,
            self.consecutive_bars, self.forced_flow, self.sentiment_extreme,
            self.boringness, self.daily_chart, self.intraday_setup,
            self.volume_capitulation, self.distance_from_ma, self.num_legs,
            self.long_vs_short
        ])

    @property
    def max_possible(self) -> float:
        return 130.0  # 13 variables x 10

    @property
    def normalized_score(self) -> float:
        """Normalized to 0-100 scale."""
        return round((self.total_score / self.max_possible) * 100, 1)

    @property
    def grade(self) -> str:
        s = self.normalized_score
        if s >= 80: return "A++"
        if s >= 70: return "A+"
        if s >= 60: return "A"
        if s >= 50: return "B+"
        if s >= 40: return "B"
        if s >= 30: return "C+"
        if s >= 25: return "C"
        return "NO TRADE"

    @property
    def action(self) -> str:
        g = self.grade
        if g in ("A++", "A+"): return "MAX SIZE — exponential bet sizing"
        if g in ("A", "B+"):   return "Meaningful size — strong conviction"
        if g in ("B", "C+"):   return "Small size — acceptable but marginal"
        if g == "C":           return "Very small or skip"
        return "DO NOT TRADE"

    @property
    def estimated_win_rate(self) -> str:
        s = self.normalized_score
        if s >= 70: return "75-90%"
        if s >= 55: return "65-75%"
        if s >= 40: return "55-65%"
        if s >= 25: return "45-55%"
        return "<45% (coin flip or worse)"

    @property
    def expected_retracement(self) -> str:
        s = self.normalized_score
        if s >= 70: return "80-100% to MA"
        if s >= 55: return "50-80%"
        if s >= 40: return "30-50%"
        return "<30% (weak or no bounce)"


class CapitulationDetector:
    """Detect capitulation setups using Breitstein's framework."""

    @staticmethod
    def detect_waterfall(df: pd.DataFrame, bb_period: int = 20, bb_std: float = 2.0) -> dict:
        """
        Analyze price action for capitulation/waterfall pattern.
        df must have columns: open, high, low, close, volume
        """
        close = df["close"]
        high = df["high"]
        low = df["low"]
        volume = df["volume"]

        # Bollinger Bands
        ma = close.rolling(bb_period).mean()
        std = close.rolling(bb_period).std()
        upper_bb = ma + bb_std * std
        lower_bb = ma - bb_std * std

        # ATR for range measurement
        tr = pd.concat([
            high - low,
            (high - close.shift(1)).abs(),
            (low - close.shift(1)).abs()
        ], axis=1).max(axis=1)
        atr = tr.rolling(14).mean()

        current = df.iloc[-1]
        prev = df.iloc[-2] if len(df) > 1 else current

        # --- Score each variable ---
        score = CapitulationScore()

        # 1. Size of move: how far from MA in ATR multiples
        dist_from_ma = abs(current["close"] - ma.iloc[-1])
        atr_multiples = dist_from_ma / atr.iloc[-1] if atr.iloc[-1] > 0 else 0
        score.distance_from_ma = min(10, atr_multiples * 2)
        score.size_of_move = min(10, atr_multiples * 2.5)

        # 2. Rate of change / slope analysis
        if len(df) >= 5:
            recent_bars = df.tail(5)
            bar_ranges = (recent_bars["high"] - recent_bars["low"]).values
            range_acceleration = bar_ranges[-1] / (np.mean(bar_ranges[:-1]) + 1e-10)
            score.rate_of_change = min(10, range_acceleration * 2)

        # 3. Consecutive bars in same direction
        direction = "down" if current["close"] < ma.iloc[-1] else "up"
        consecutive = 0
        for i in range(len(df) - 1, 0, -1):
            if direction == "down" and df.iloc[i]["close"] < df.iloc[i]["open"]:
                consecutive += 1
            elif direction == "up" and df.iloc[i]["close"] > df.iloc[i]["open"]:
                consecutive += 1
            else:
                break
        score.consecutive_bars = min(10, consecutive * 1.5)

        # 4. Volume capitulation
        avg_vol = volume.rolling(20).mean().iloc[-1]
        vol_ratio = current["volume"] / avg_vol if avg_vol > 0 else 1
        score.volume_capitulation = min(10, vol_ratio * 2)

        # 5. Bollinger Band breach
        below_lower = current["close"] < lower_bb.iloc[-1]
        above_upper = current["close"] > upper_bb.iloc[-1]

        # 6. Prior bar highs/lows pattern (clean waterfall check)
        holding_prior_bar = True
        if direction == "down":
            for i in range(len(df) - 1, max(0, len(df) - 6), -1):
                if i > 0 and df.iloc[i]["high"] > df.iloc[i-1]["high"]:
                    holding_prior_bar = False
                    break
        else:
            for i in range(len(df) - 1, max(0, len(df) - 6), -1):
                if i > 0 and df.iloc[i]["low"] < df.iloc[i-1]["low"]:
                    holding_prior_bar = False
                    break

        # 7. Determine signal
        is_capitulating = (
            (below_lower or above_upper) and
            vol_ratio > 2.0 and
            consecutive >= 3 and
            atr_multiples > 1.5
        )

        # Entry levels
        if direction == "down" and is_capitulating:
            entry_level = prev["high"]  # Break of prior bar high
            stop_level = df.tail(10)["low"].min()  # Low of move
            target_level = ma.iloc[-1]  # 20MA equilibrium
        elif direction == "up" and is_capitulating:
            entry_level = prev["low"]  # Break of prior bar low
            stop_level = df.tail(10)["high"].max()  # High of move
            target_level = ma.iloc[-1]
        else:
            entry_level = stop_level = target_level = None

        risk = abs(entry_level - stop_level) if entry_level and stop_level else 0
        reward = abs(target_level - entry_level) if entry_level and target_level else 0
        rr_ratio = round(reward / risk, 2) if risk > 0 else 0

        return {
            "is_capitulating": is_capitulating,
            "direction": "LONG (buy the panic)" if direction == "down" else "SHORT (sell the euphoria)",
            "score": score,
            "grade": score.grade,
            "normalized_score": score.normalized_score,
            "action": score.action,
            "estimated_win_rate": score.estimated_win_rate,
            "expected_retracement": score.expected_retracement,
            "entry": round(entry_level, 5) if entry_level else None,
            "stop": round(stop_level, 5) if stop_level else None,
            "target_ma": round(target_level, 5) if target_level else None,
            "risk_reward": rr_ratio,
            "bb_lower": round(lower_bb.iloc[-1], 5),
            "bb_upper": round(upper_bb.iloc[-1], 5),
            "ma_20": round(ma.iloc[-1], 5),
            "atr_multiples_from_ma": round(atr_multiples, 2),
            "volume_ratio": round(vol_ratio, 2),
            "consecutive_bars": consecutive,
            "holding_prior_bar_pattern": holding_prior_bar,
            "slope_assessment": (
                "WATERFALL (asymptotic)" if score.rate_of_change >= 8 else
                "Sharp selloff" if score.rate_of_change >= 5 else
                "Moderate acceleration" if score.rate_of_change >= 3 else
                "Slow/steady (AVOID)"
            ),
        }

    @staticmethod
    def trail_prior_bar(df: pd.DataFrame, direction: str = "long") -> dict:
        """
        Calculate trailing stop using prior bar lows (long) or prior bar highs (short).
        """
        current = df.iloc[-1]
        prev = df.iloc[-2] if len(df) > 1 else current

        if direction == "long":
            trail_stop = prev["low"]
            status = "HOLD" if current["close"] > trail_stop else "STOPPED OUT"
        else:
            trail_stop = prev["high"]
            status = "HOLD" if current["close"] < trail_stop else "STOPPED OUT"

        return {
            "direction": direction,
            "trail_stop": round(trail_stop, 5),
            "current_price": round(current["close"], 5),
            "status": status,
        }

    @staticmethod
    def scan_capitulation_candidates(
        symbols_data: dict,
        min_consecutive: int = 3,
        min_volume_ratio: float = 2.0,
        min_atr_multiples: float = 1.5
    ) -> list:
        """
        Scan multiple symbols for capitulation setups.
        symbols_data: dict of {symbol: DataFrame}
        Returns sorted list of candidates by score.
        """
        candidates = []
        detector = CapitulationDetector()

        for symbol, df in symbols_data.items():
            try:
                result = detector.detect_waterfall(df)
                if result["is_capitulating"]:
                    candidates.append({
                        "symbol": symbol,
                        **result
                    })
            except Exception:
                continue

        # Sort by normalized score (best first)
        candidates.sort(key=lambda x: x["normalized_score"], reverse=True)
        return candidates
```

---

## Key Psychology & Discipline Rules

### The Front-Side Trap (What Most Traders Do Wrong)
1. Buy on the way down -> stop out
2. Buy again lower -> stop out again
3. Buy AGAIN during acceleration -> hold too long -> big loss
4. When the REAL turn comes -> licking wounds, miss the trade
5. **Worst case:** Flip to the other side at the exact bottom

### Lance's Self-Talk System
> "Don't buy the front side. Don't buy the front side. Wait for the turn. Wait for the turn."

- Even after 15 years and $100M+ profits, he STILL fights these emotions daily.
- Every day: "Lance, don't be a dumbass. Fight those emotions."
- The David Goggins analogy: greatness requires fighting your base nature EVERY SINGLE DAY.
- Awareness increases over time, but the battle never ends.

### Sizing by Conviction
- **A++ trades:** Exponential bet sizing. This is where the big money is made.
- **B trades:** Standard risk. Acceptable but not career-defining.
- **C trades:** Tiny size. Almost not worth the screen time.
- **No trade:** Walk away. Selectivity IS the edge.

### When Setup Quality Predicts Outcome
- Higher-grade setups -> stronger, cleaner bounces (to MA or beyond).
- Lower-grade setups -> weaker, choppier bounces (or no bounce at all).
- Your rubric score directly correlates to expected outcome quality.

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| `mean-reversion-engine` | Use Bollinger/RSI for quantitative confirmation alongside this framework |
| `market-regime-classifier` | Capitulation trades work in ALL regimes (unlike standard mean reversion) |
| `risk-and-portfolio` | Scale position size to rubric grade (A++ = max, C = minimum) |
| `volume-profile-strategy` | Volume capitulation spike is a key variable in the scoring rubric |
| `trading-brain` | Route extreme-move alerts to this capitulation framework |
| `mt5-ea-code-generator` | Can codify the prior-bar-highs/lows trailing system as an EA |
| `trade-journal-analytics` | Log rubric scores alongside trades to refine the scoring system over time |

---

## Quick Reference Card

```
CAPITULATION TRADE CHECKLIST:
[] Size of move: How many ATRs from equilibrium?
[] Rate of change: Waterfall or grind? (Need waterfall)
[] News: No news = best. Old news = acceptable.
[] Consecutive bars: 4+ in same direction?
[] Forced flow: Evidence of liquidations/margin calls?
[] Sentiment: At an extreme?
[] Boringness: Was this a boring/stable security before?
[] Volume: Capitulation spike (>2x average)?
[] Daily chart: Does higher TF support the trade?
[] Bollinger: Beyond the bands?
[] Distance from MA: Multiple ATRs away?
[] Number of legs: 3+ legs in the move?

ENTRY: Right Side of V (break prior bar highs/lows)
STOP: Low/high of the move
TRAIL: Prior bar lows (long) / Prior bar highs (short)
TARGET: 20-period moving average (equilibrium)

GRADE -> SIZE:
A++ = Max  |  A = Strong  |  B = Small  |  C = Tiny  |  <C = NO TRADE
```
