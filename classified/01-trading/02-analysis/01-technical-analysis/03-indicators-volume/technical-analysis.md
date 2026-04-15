---
name: technical-analysis
description: >
  Complete technical analysis knowledge base covering candlestick patterns, chart patterns, technical
  indicators, support/resistance, Fibonacci levels, pivot points, and supply/demand zones. Includes
  Python strategy engines for Fibonacci retracement/extension, Ichimoku cloud signals, MA ribbons,
  pivot point strategies, momentum/ROC, divergences (regular and hidden), Heikin-Ashi candles,
  Renko bricks, volume profile (POC/VAH/VAL), trend following systems, and mean reversion setups.
  Trigger when analyzing charts, identifying patterns, using indicators like RSI, MACD, Bollinger
  Bands, Stochastic, ADX, Ichimoku, ATR, or any technical analysis concept.
  USE FOR: candlestick patterns, hammer pattern, shooting star, doji, marubozu, spinning top,
  engulfing pattern, harami, tweezer top bottom, piercing line, dark cloud cover, morning star,
  evening star, three white soldiers, three black crows, abandoned baby, chart patterns, head and
  shoulders, double top double bottom, triple top triple bottom, ascending triangle, descending
  triangle, symmetrical triangle, bull flag bear flag, pennant, wedge, cup and handle, Fibonacci
  retracement, Fibonacci extension, pivot points, support resistance, supply demand zones, how to
  identify reversal, continuation patterns, measured move targets, moving averages SMA EMA DEMA
  TEMA HMA, MACD signals, ADX trend strength, Parabolic SAR, Ichimoku cloud components signals,
  RSI divergence failure swings, Stochastic oscillator, CCI, Williams %R, ROC, OBV on balance
  volume, VWAP bands, accumulation distribution, MFI money flow, CMF Chaikin, Volume Profile POC
  VAH VAL, Bollinger Bands %B bandwidth squeeze, ATR multipliers, Keltner Channels, Donchian
  Channels, multi-timeframe analysis, Elliott Wave rules guidelines, Fibonacci wave relationships,
  harmonic patterns ABCD Gartley Butterfly Bat Crab Shark Cypher, Market Profile auction market
  theory TPO, golden cross, death cross, OBV, money flow, golden ratio, Fibonacci strategy engine,
  Ichimoku complete strategy, MA ribbon strategy, moving average crossover ribbon, pivot point
  bounce, momentum trading, rate of change ROC, RSI divergence, MACD divergence, hidden divergence,
  Heikin Ashi candles, Renko bricks, volume profile strategy, trend following system, mean reversion
  setup, MA crossover strategy, triple MA alignment, turtle breakout, ADX trend rider, supertrend
  indicator, Bollinger bounce, RSI extreme fade, z-score reversion, indicator-based entry exit rules.
  MTF CONFLUENCE: "multi-timeframe analysis", "MTF confluence", "timeframe alignment",
  "higher timeframe bias", "are timeframes aligned", "confluence score", "top-down analysis",
  "HTF/LTF alignment", "which timeframes agree", "heat map", "confluence heat map",
  "timeframe weight", "multi-pair confluence scan".
related_skills:
  - technical-analysis
  - price-action
  - chart-vision
  - ict-smart-money
  - liquidity-analysis
tags:
  - trading
  - analysis
  - technical
  - supply-demand
  - fibonacci
  - vwap
  - pivots
  - candlestick
skill_level: intermediate
kind: analyzer
category: trading/strategies
status: active
---
> **Skill:** Technical Analysis  |  **Domain:** trading  |  **Category:** analysis  |  **Level:** intermediate
> **Tags:** `trading`, `analysis`, `technical`, `supply-demand`, `fibonacci`, `vwap`, `pivots`, `candlestick`


# Technical Analysis

---

## 1. Candlestick Patterns

### Reading Candlesticks
```
       High ──── ┐
                 │ Upper Wick (Shadow)
       Open ─── [█] Body (Bullish: Close > Open = White/Green)
       Close ── [█]
                 │ Lower Wick (Shadow)
       Low  ──── ┘

Body Color:
  Green/White = Close ABOVE Open (Bullish)
  Red/Black   = Close BELOW Open (Bearish)
```

---

### Single Candlestick Patterns

#### Hammer (Bullish Reversal)
- **Shape**: Small body at top, long lower wick (≥2× body), little/no upper wick
- **Context**: Must appear at BOTTOM of downtrend
- **Signal**: Bulls pushed price back up from lows; rejection of lower prices
- **Reliability**: 60–65%
- **Confirmation**: Next candle closes above hammer body
- **Colors**: Green hammer more bullish than red hammer (both valid)

#### Inverted Hammer (Bullish Reversal)
- **Shape**: Small body at bottom, long upper wick (≥2× body)
- **Context**: At bottom of downtrend
- **Signal**: Initial buying attempt; needs confirmation
- **Reliability**: 55–60%
- **Confirmation**: Next candle closes bullish

#### Hanging Man (Bearish Reversal)
- **Shape**: Identical to Hammer but at TOP of uptrend
- **Context**: Must appear at TOP of uptrend (context = opposite signal)
- **Signal**: Intraday selling pressure; warning of reversal
- **Reliability**: 55–60%

#### Shooting Star (Bearish Reversal)
- **Shape**: Small body at bottom, long upper wick (≥2× body), little/no lower wick
- **Context**: At TOP of uptrend
- **Signal**: Bears pushed price back from highs; rejection of higher prices
- **Reliability**: 65–70%
- **Confirmation**: Next candle closes below shooting star body

#### Doji Patterns
| Doji Type | Shape | Signal | Reliability |
|-----------|-------|--------|-------------|
| **Standard Doji** | Open ≈ Close, equal wicks | Indecision | 50% (needs context) |
| **Long-Legged Doji** | Very long upper & lower wicks | High volatility indecision | 55% |
| **Gravestone Doji** | Open=Close at LOW, long upper wick | Bearish reversal at tops | 65% |
| **Dragonfly Doji** | Open=Close at HIGH, long lower wick | Bullish reversal at bottoms | 65% |
| **Four Price Doji** | All four prices identical | Extreme indecision (illiquid) | N/A |
| **Rickshaw Man** | Open≈Close in middle, very long wicks | Major indecision | 55% |

#### Marubozu (Strong Momentum)
| Type | Shape | Signal | Reliability |
|------|-------|--------|-------------|
| **Bullish Marubozu** | Large green body, NO wicks | Strong bullish momentum | 75–80% |
| **Bearish Marubozu** | Large red body, NO wicks | Strong bearish momentum | 75–80% |
| **Opening Marubozu** | No opening wick, has closing wick | Momentum fading at close | 60% |
| **Closing Marubozu** | No closing wick, has opening wick | Strong closing momentum | 65% |

#### Spinning Top
- **Shape**: Small body (any color), significant upper AND lower wicks
- **Signal**: Indecision; neither bulls nor bears in control
- **Reliability**: 45–50% (needs strong context)
- **Use**: Warning of trend pause or reversal when in extended trend

#### Belt Hold
- **Bullish**: Opens at low of session (no lower wick), rallies strongly
- **Bearish**: Opens at high of session (no upper wick), falls strongly
- **Reliability**: 55–60%

---

### Double Candlestick Patterns

#### Bullish Engulfing (★★★★ Reversal)
- **Setup**: Small bearish candle followed by large bullish candle that completely engulfs it
- **Rules**: Green body must cover entire red body (wicks optional)
- **Context**: Must be at bottom of downtrend or key support
- **Reliability**: 72–78%
- **Strength Factors**: Higher volume on bullish candle, larger relative size, at major S/R

#### Bearish Engulfing (★★★★ Reversal)
- **Setup**: Small bullish candle followed by large bearish candle that engulfs it
- **Context**: Must be at top of uptrend or key resistance
- **Reliability**: 72–78%

#### Bullish Harami (Reversal)
- **Setup**: Large bearish candle followed by small bullish candle INSIDE prior body
- **Signal**: Selling momentum slowing; potential reversal
- **Reliability**: 55–65%
- **Note**: Harami = "pregnant" in Japanese; small candle is "baby"

#### Bearish Harami (Reversal)
- **Setup**: Large bullish candle followed by small bearish candle inside prior body
- **Reliability**: 55–65%

#### Harami Cross
- **Setup**: Harami where second candle is a Doji
- **Reliability**: 65–70% (doji = more indecision = stronger signal)

#### Tweezer Top (Bearish Reversal)
- **Setup**: Two candles with equal HIGHS (±1–2 ticks acceptable)
- **Context**: At resistance or top of uptrend
- **Reliability**: 60–68%
- **Signal**: Double rejection at same price = strong resistance

#### Tweezer Bottom (Bullish Reversal)
- **Setup**: Two candles with equal LOWS
- **Context**: At support or bottom of downtrend
- **Reliability**: 60–68%

#### Piercing Line (Bullish Reversal)
- **Setup**: Large bearish candle, followed by bullish candle that opens BELOW prior low but closes MORE THAN 50% into prior bearish body
- **Context**: At support/bottom of trend
- **Reliability**: 65–70%

#### Dark Cloud Cover (Bearish Reversal)
- **Setup**: Large bullish candle, followed by bearish candle that opens ABOVE prior high but closes MORE THAN 50% into prior bullish body
- **Context**: At resistance/top of trend
- **Reliability**: 65–70%

#### On Neck / In Neck (Continuation)
- **On Neck**: Gap down open, closes at or near prior candle LOW (weak bullish)
- **In Neck**: Closes slightly into prior body (stronger)
- **Signal**: Continuation of downtrend
- **Reliability**: 55%

---

### Triple Candlestick Patterns

#### Morning Star (★★★★★ Bullish Reversal)
```
Candle 1: Large bearish (downtrend continuation)
Candle 2: Small body (gap down optional), star candle (indecision)
Candle 3: Large bullish, closes >50% into Candle 1's body

★ Most reliable triple candlestick pattern ★
Reliability: 78–83%
```

#### Evening Star (★★★★★ Bearish Reversal)
```
Candle 1: Large bullish (uptrend continuation)
Candle 2: Small body (gap up optional), star candle
Candle 3: Large bearish, closes >50% into Candle 1's body

Reliability: 78–83%
```

#### Morning Doji Star (Higher Reliability)
- Same as Morning Star but Candle 2 is a Doji
- **Reliability**: 83–87% (doji increases significance)

#### Evening Doji Star
- Same as Evening Star but Candle 2 is a Doji
- **Reliability**: 83–87%

#### Three White Soldiers (Bullish Continuation/Reversal)
- **Setup**: Three consecutive large bullish candles, each opening in prior body and closing higher
- **Requirements**: Each close near session high, minimal wicks
- **Context**: After downtrend = strong reversal; during uptrend = continuation
- **Reliability**: 70–75%
- **Warning**: After large prior move = exhaustion signal

#### Three Black Crows (Bearish Continuation/Reversal)
- **Setup**: Three consecutive large bearish candles, each opening in prior body and closing lower
- **Reliability**: 70–75%

#### Abandoned Baby (Strongest Reversal Signal)
- **Bullish Setup**: Bearish marubozu → Doji with gap down → Bullish marubozu with gap up
- **Bearish Setup**: Bullish marubozu → Doji with gap up → Bearish marubozu with gap down
- **Key**: TRUE gaps required (no overlap including wicks)
- **Reliability**: 85–90% (rare but highly reliable)

#### Three Inside Up (Bullish)
- Bearish candle → small bullish inside → bullish candle closes above first candle's body
- Essentially Harami + confirmation
- **Reliability**: 65–70%

#### Three Inside Down (Bearish)
- Bullish candle → small bearish inside → bearish candle closes below first candle
- **Reliability**: 65–70%

#### Upside/Downside Tasuki Gap (Continuation)
- Gap in direction of trend + candle that partially fills gap
- **Signal**: Continuation of trend
- **Reliability**: 55–60%

#### Rising Three Methods / Falling Three Methods
- **Rising**: Large bullish candle → 3 small bearish candles (stay within range) → large bullish close above first candle high
- **Signal**: Brief consolidation before trend continuation
- **Reliability**: 70–75%

### Proven Multi-Candle Trading Patterns
> Source: "The BEST Candlestick Pattern Guide" — Data Trader (2.5M views, tested across career)

#### Three-Bar Continuation Pattern
```
Candle 1: Large body, bigger than average (sets direction)
Candle 2: Small opposite-color candle, body < 50% of Candle 1's body
Candle 3: Large candle same color as C1, closes beyond C2's close

Bullish: Large green → small red → large green (uptrend continuation)
Bearish: Large red → small green → large red (downtrend continuation)

Entry: Close of Candle 3
SL: Bottom wick of Candle 2 (bullish) / Top wick of C2 (bearish)
Best when: Forming during established trend, not at reversals
```

#### Three-Bar Reversal Pattern
```
Candle 1: Large full body (establishes current trend)
Candle 2: Small body, SAME color as C1
Candle 3: Large full body, OPPOSITE color to C1 & C2

Strong signal: C3 body >= C1 body (higher success rate)
Weak signal:  C3 body < C1 body (lower probability)

Bullish: Two red candles → large green (downtrend reversal)
Bearish: Two green candles → large red (uptrend reversal)

Entry: Close of Candle 3
SL: Lows of C2 (bullish) / Highs of C2 (bearish)
```

#### Breakout Candles Pattern
```
Setup: 3+ small consolidation candles → 1 large breakout candle
  - Consolidation candle color doesn't matter — size does (all small)
  - More consolidation candles = higher probability breakout
  - Breakout candle must have clearly larger body than consolidation candles

Entry: Close of breakout candle
SL: Opening price of breakout candle
Direction: Continue in direction of breakout candle
```

#### Shrinking Candles Pattern (Momentum Exhaustion)
```
Setup: 3+ consecutive same-color candles, each SMALLER than the last
  → followed by large opposite-color candle

Shows: Trend gradually weakening → reversal confirmation
Strong signal: C4 closes beyond C2 (deeper reversal)

Bullish: 3+ shrinking red candles → large green candle
Bearish: 3+ shrinking green candles → large red candle

Entry: Close of the reversal candle
SL: Beyond the previous candle's extreme
```

#### Combining Patterns with Key Levels (Strategy)
```
Step 1: Identify key level (S/R, trendline, Fib, or confluence zone)
Step 2: Wait for price to interact with the key level
Step 3: Look for one of the 6 patterns at that level:
  - Engulfing, Pin Bar, 3-Bar Continuation, 3-Bar Reversal,
    Breakout Candles, Shrinking Candles
Step 4: Enter on pattern completion, SL per pattern rules
Step 5: TP at 2:1 RR minimum

Note: Patterns work best on 1H+ timeframes. Less effective on LTF.
Confluence level (multiple key levels intersecting) = highest probability.
```

---

## 2. Chart Patterns

### Reversal Patterns

#### Head and Shoulders (H&S)
```
          Left    Head   Right
Shoulder:  ▲       ▲       ▲
           |      |||      |
Neckline: ─┴──────┴┴──────┴─

Measured Move: Distance from Head to Neckline
  Target = Neckline − (Head − Neckline)

Rules:
- Left shoulder: rally, pullback
- Head: higher rally, deeper pullback
- Right shoulder: lower rally, break below neckline
- Volume: decreasing through right shoulder
- Neckline break: high volume confirmation

Reliability: 83–85%
Retest: ~45% of breakouts retest neckline
```

#### Inverse Head and Shoulders (Bullish)
- Mirror image of H&S
- **Reliability**: 83–85%
- **Target**: Breakout price + Head-to-Neckline distance

#### Double Top (★★★★)
```
   Peak 1  Peak 2
     ▲        ▲
    / \      / \
   /   \    /   \
──/─────\──/─────\──  Support/Neckline
          \/

Rules:
- Two peaks at approximately SAME price level (±1–3%)
- Valley between = neckline/support
- Volume: higher on left peak than right peak
- Breakdown: close below neckline = confirmation

Target = Neckline − (Peak − Neckline)
Reliability: 75–80%
Time between peaks: minimum 2 weeks for swing trading
```

#### Double Bottom (Bullish)
- Mirror image; "W" shape
- **Reliability**: 75–80%
- **Target**: Breakout + (Neckline − Trough)

#### Triple Top / Triple Bottom
- Three tests of same level before breakdown/breakout
- **Reliability**: 80–85% (more tests = stronger level)
- **Target**: Same measured move as double top/bottom

#### Rounding Bottom (Saucer)
- Gradual, curved reversal from down to uptrend
- **Time**: Weeks to months (long-term pattern)
- **Reliability**: 75%
- **Target**: Breakout + depth of saucer

---

### Continuation Patterns

#### Ascending Triangle (Bullish Continuation/Reversal)
```
Resistance: ─────────────────── (Flat top)
           /   /   /   /
          /   /   /   /         (Rising support)

Rules:
- Flat upper resistance + rising lower support
- Bullish in uptrend; reversal if at bottom of downtrend
- Breakout: above resistance with volume
- Target = Resistance + Height of triangle (at widest)

Reliability: 72–75%
False breakout rate: ~25%
```

#### Descending Triangle (Bearish)
- Flat support + declining resistance
- **Reliability**: 72–75%
- **Target**: Flat support − Triangle height

#### Symmetrical Triangle
- Converging trendlines (lower highs + higher lows)
- **Breakout direction**: Usually continues prior trend (75%)
- **Target**: Breakout point ± widest point of triangle
- **Reliability**: 65–70%
- **Timing**: Breakout typically occurs 50–75% through triangle

#### Bull Flag (★★★★★)
```
Flag Pole:  ╱  Strong, sharp rally (pole)
           ╱
          ╱───╮
              │╲  Flag: tight, orderly pullback
              │ ╲  (parallel channel, 20–40% pullback of pole)
              ╰──╱  Breakout: above flag resistance
                 ╱
                ╱   Target = Flag Breakout + Flag Pole Length

Volume: Heavy on pole, light during flag, heavy on breakout
Reliability: 80–85%
Duration of flag: 1–4 weeks ideal
```

#### Bear Flag (Bearish Continuation)
- Sharp decline (pole) + brief upward consolidation (flag)
- **Reliability**: 80–85%
- **Target**: Flag breakdown − pole length

#### Bull Pennant
- Similar to bull flag but consolidation forms symmetrical triangle (not channel)
- **Reliability**: 78–82%
- **Target**: Same measured move as bull flag

#### Bear Pennant
- Sharp decline + converging triangle consolidation
- **Reliability**: 78–82%

#### Rising Wedge (Bearish)
- Both support and resistance sloping up, but converging
- **Bias**: Bearish (upward move losing momentum)
- **Breakdown**: Through lower trendline
- **Target**: Start of wedge (beginning of pattern)
- **Reliability**: 70–75%

#### Falling Wedge (Bullish)
- Both lines sloping down, converging
- **Bias**: Bullish reversal or continuation
- **Breakout**: Through upper trendline
- **Reliability**: 70–75%

#### Cup and Handle (★★★★)
```
Cup:         ╭──────────────╮
            ╱                ╲
           ╱                  ╲
          ╱                    ╲
                               Handle: 5–15% pullback
                               Breakout: above cup rim

Rules:
- Cup: U-shaped (rounded), not V-shaped
- Depth: 15–30% from rim to bottom (max 50%)
- Handle: forms in upper 50% of cup; <15% pullback
- Volume: heavy at breakout above handle resistance
- Duration: Cup = weeks to months; Handle = 1–4 weeks

Target = Handle breakout + Cup depth
Reliability: 75–80%
```

#### Inverse Cup and Handle (Bearish)
- Upside-down cup formation
- **Reliability**: 70–75%

---

## 3. Support, Resistance & Fibonacci

### Support and Resistance Basics
```
Resistance → Price ceiling; sellers dominate
Support    → Price floor; buyers dominate
```

**Role Reversal**: Broken resistance becomes support; broken support becomes resistance

**Strength Factors**:
1. Number of times tested (more = stronger)
2. Time since level formed (older = more significant)
3. Volume at the level (higher = more significant)
4. Price reaction magnitude (larger rejection = stronger)
5. Clean vs. messy level (clean round numbers stronger)

### Fibonacci Retracement Levels
```
Key Levels (from swing high to swing low or vice versa):
  23.6% → Minor support/resistance (weak)
  38.2% → Moderate pullback level
  50.0% → Psychological midpoint (not true Fibonacci but widely watched)
  61.8% → "Golden Ratio" — MOST IMPORTANT level
  78.6% → Deep retracement (= √0.618)
  88.6% → Very deep (= 0.886 = √0.786); used in harmonic patterns

Entry Strategy:
  Conservative: Wait for price to react at Fibonacci level + candle confirmation
  Aggressive: Enter directly at Fibonacci level with tight stop
  
Stop Loss: Just beyond next Fibonacci level (e.g., short at 61.8%, stop above 78.6%)
```

### Fibonacci Extension Levels (Profit Targets)
```
Common extension targets after retracement:
  127.2% = 1st extension (= √1.272)
  138.2%
  161.8% = Most common major target
  200.0% = Double the prior move
  261.8% = Strong extension target

How to Draw:
  Uptrend: From swing low (A) to swing high (B) to retracement low (C)
  Target = C + (A to B distance × extension %)
```

### Fibonacci Time Zones
```
After swing high or low, count forward:
Bars 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
→ Significant reactions likely at these time intervals (Fibonacci sequence)
```

### Pivot Points

#### Standard Pivot Points
```
PP = (High + Low + Close) ÷ 3

R3 = High + 2(PP − Low)
R2 = PP + (High − Low)
R1 = 2(PP) − Low
PP = Pivot Point
S1 = 2(PP) − High
S2 = PP − (High − Low)
S3 = Low − 2(High − PP)
```

#### Fibonacci Pivot Points
```
PP = (High + Low + Close) ÷ 3
R1 = PP + 0.382 × (High − Low)
R2 = PP + 0.618 × (High − Low)
R3 = PP + 1.000 × (High − Low)
S1 = PP − 0.382 × (High − Low)
S2 = PP − 0.618 × (High − Low)
S3 = PP − 1.000 × (High − Low)
```

#### Camarilla Pivot Points
```
R4 = Close + (High − Low) × 1.5
R3 = Close + (High − Low) × 1.25
R2 = Close + (High − Low) × 1.1666
R1 = Close + (High − Low) × 1.0833
S1 = Close − (High − Low) × 1.0833
S2 = Close − (High − Low) × 1.1666
S3 = Close − (High − Low) × 1.25
S4 = Close − (High − Low) × 1.5

Strategy: Fade at R3/S3; Breakout trade at R4/S4
```

### Timeframe-Based Pivots
| Pivot Period | Chart Timeframe | Best For |
|-------------|-----------------|---------|
| Daily pivots | 15m–1h charts | Day trading |
| Weekly pivots | 4h–Daily charts | Swing trading |
| Monthly pivots | Daily–Weekly | Position trading |

---

## 4. Supply and Demand Zones

### What Creates Supply/Demand Zones
- **Demand Zone**: Area where strong buying previously occurred → price left rapidly upward
- **Supply Zone**: Area where strong selling occurred → price left rapidly downward
- Key characteristic: **The stronger and faster the departure, the stronger the zone**

### Identifying Quality Zones
```
High-Quality Demand Zone (4 criteria):
  ✓ Price departed quickly and strongly (large candles away from zone)
  ✓ Zone has NOT been revisited before current test
  ✓ Located at a lower timeframe support or key price level
  ✓ Formed at the beginning of a significant upswing

Lower-Quality Zone:
  ✗ Zone has been tested multiple times (each test = weaker zone)
  ✗ Price left slowly with small candles
  ✗ Zone is far from current market structure
```

### Supply/Demand Zone Trading
```
Entry at Demand Zone:
  1. Mark zone boundaries (base of zone to top)
  2. Wait for price to return to zone
  3. Look for bullish reaction candle (engulfing, hammer, pin bar)
  4. Enter long; stop below zone low
  5. Target: Next supply zone above

Entry at Supply Zone:
  1. Mark zone boundaries
  2. Wait for price to reach zone
  3. Look for bearish reaction candle
  4. Enter short; stop above zone high
  5. Target: Next demand zone below
```

### Zone Strength Factors
| Factor | Stronger | Weaker |
|--------|----------|--------|
| Number of visits | First test | 3+ tests |
| Departure strength | Large, fast candles | Small, slow candles |
| Time since formation | Recent | Old (months/years) |
| Higher TF alignment | Yes | No |
| Volume at departure | High | Low |

### A+ Supply & Demand Execution Framework (3-Step)
> Source: Trade with Pat — 284K views, 121-trade backtest: **79% win rate, 2,100% P&L**

#### Step 1: Identify Institutional Demand/Supply Zone
```
Demand Zone Identification:
  - Look for 3+ consecutive large same-color candles (impulsive move)
  - 60+ pip move on forex = institutional activity (retail can't move this)
  - Draw zone on the CANDLE BODY before the impulsive move (accumulation)

Zone Drawing Rules:
  Large pre-move candle → Draw zone on BODY ONLY (tighter, cleaner)
  Small pre-move candle → Draw WICK TO WICK
  Multiple small candles → Group together as one zone

Required Confluence at Zone:
  1. Fair Value Gap (FVG) — candles before and after don't cover the big candle
  2. Historical S/R flip — zone was previously resistance, now support (or vice versa)
  3. Both = "confluence stack" → highest probability
```

#### Step 2: Trend Confirmation (3 Methods)
```
Method A — Swing Structure:
  Uptrend: HH + HL sequence with breaks of structure
  Downtrend: LH + LL sequence

Method B — EMA Filter:
  Price above EMA with SEPARATION = trend confirmed
  Price crossing above/below EMA repeatedly with no gap = choppy → SKIP

Method C — Higher TF Alignment:
  Go to next HTF (e.g., H1 → H4) and confirm same swing structure
  Both TFs trending same direction = green light
```

#### Step 3: Entry Conditions
```
MOMENTUM FILTER (Critical):
  ✓ SLOW approach to zone — mixed candles, small bodies = TRADE
  ✗ FAST approach — one big candle slamming into zone = DO NOT TRADE

Entry Trigger:
  1. Candle closes INSIDE zone or WICKS into zone
  2. Wait for NEXT candle to be positive (green for demand, red for supply)
  3. Enter on confirmation candle

Invalidation:
  If candle CLOSES BELOW zone (demand) or ABOVE zone (supply) → SKIP

Stop Loss:
  Option A: Tight to zone boundary
  Option B: Below nearest wick + below EMA (dual protection)

Take Profit:
  Default: 1:1 RR | Better: target recent swing H/L (1.4-1.8 RR)
  Advanced: trailing stop — exit when candle CLOSES below trail (not wick)
```

### 6 Keys to Valid Demand/Supply Zones (Loss Avoidance Filter)
```
1. UNTESTED ZONE (Fresh Only)
   - Only trade on FIRST test — already-tested zones have drastically lower hold rate

2. CANDLE CLOSE POSITION
   - Wicking into zone = VALID | Closing inside zone = VALID
   - Closing BELOW zone (demand) = INVALIDATED → do not trade

3. CONFLUENCE STACK
   - Zone aligns with EMA S/R + historical S/R flip = stacked → highest probability

4. LOWEST DEMAND IS STRONGEST
   - Multiple demand zones → LOWEST one holds best (deepest institutional accumulation)
   - Inverse for supply: HIGHEST supply zone is strongest

5. DISCOUNTED PRICE (Fib Filter)
   - Draw Fib retracement from swing low to swing high
   - Entry must be BELOW 50% for demand (ABOVE 50% for supply)

6. BREAK OF STRUCTURE REQUIRED
   - Confirm BOS exists before entering at zone
   - If last swing high NOT broken → trend weakening → zone will likely fail
   - No BOS = no trade (hard filter)
```

### Opening Range Breakout + Supply/Demand Combo
> Source: Trade with Pat — used daily on livestream
```
Setup (Intraday, 5m chart):
  1. At 9:30 AM EST, mark range of first 3 five-minute candles (wick to wick)
  2. Wait for price to BREAK AND CLOSE outside range (top = buy, bottom = sell)
  3. This sets directional bias for the session

Execution:
  4. After breakout confirms direction, wait for RETRACE to demand zone (if long)
  5. Do NOT enter on breakout candle — wait for pullback to zone
  6. Enter on positive reaction candle at demand zone
  7. SL below zone, TP at recent structure or trailing stop
```

---

## 5. Trend Indicators

### Simple Moving Average (SMA)
```
SMA(n) = (P₁ + P₂ + ... + Pₙ) ÷ n

Key Levels:
  20 SMA  → Short-term trend (day trading)
  50 SMA  → Medium-term trend (swing trading)
  100 SMA → Medium-long trend
  200 SMA → Long-term trend (bull/bear market line)

Signals:
  Price > 200 SMA → Bullish bias
  Price < 200 SMA → Bearish bias
  Golden Cross: 50 SMA crosses above 200 SMA → Bullish
  Death Cross: 50 SMA crosses below 200 SMA → Bearish
```

### Exponential Moving Average (EMA)
```
EMA = Price × k + EMA(prev) × (1 − k)
k = 2 ÷ (n + 1)

EMA responds faster to recent price changes than SMA
Key Levels: 9, 21, 50, 100, 200 EMA
```

### Double Exponential MA (DEMA)
```
DEMA = 2 × EMA(n) − EMA(EMA(n))
→ Reduces EMA lag; smoother than EMA
```

### Triple Exponential MA (TEMA)
```
EMA1 = EMA(n)
EMA2 = EMA(EMA1)
EMA3 = EMA(EMA2)
TEMA = 3 × EMA1 − 3 × EMA2 + EMA3
→ Minimal lag; good for trending markets
```

### Hull Moving Average (HMA)
```
WMA1 = WMA(n/2) × 2
WMA2 = WMA(n)
Raw HMA = WMA1 − WMA2
HMA = WMA(√n, Raw HMA)

→ Near-zero lag; very smooth; best for trend following
Crossover signals less whipsaw than EMA
```

### MA Signal System
| Condition | Signal |
|-----------|--------|
| Price > all MAs, MAs aligned up | Strong uptrend |
| Price < all MAs, MAs aligned down | Strong downtrend |
| Price crosses above 20 EMA | Short-term bullish |
| 9 EMA crosses above 21 EMA | Momentum shift bullish |
| 50 EMA crosses above 200 EMA (Golden Cross) | Long-term bullish |
| MAs converging / flat | Choppy, ranging market |

---

### MACD (Moving Average Convergence Divergence)
```
Standard Settings: 12, 26, 9

MACD Line = EMA(12) − EMA(26)
Signal Line = EMA(9) of MACD Line
Histogram = MACD Line − Signal Line

Signals:
1. Signal Line Crossover:
   MACD crosses above Signal → Bullish entry
   MACD crosses below Signal → Bearish entry

2. Zero Line Cross:
   MACD crosses above 0 → Bullish (trend confirmation)
   MACD crosses below 0 → Bearish

3. Histogram Divergence:
   Price makes new high, histogram lower → Bearish divergence
   Price makes new low, histogram higher → Bullish divergence

4. Centerline Strategies:
   Buy pullbacks to 0 line in uptrend
   Sell rallies to 0 line in downtrend

Best Timeframes: Daily for swing, 1h for day trading
Weakness: Lagging indicator; poor in ranging markets
```

---

### ADX (Average Directional Index)
```
ADX measures TREND STRENGTH (not direction)
Range: 0–100

Calculation:
  +DM = Current High − Previous High (if positive)
  −DM = Previous Low − Current Low (if positive)
  TR = max(High−Low, |High−PrevClose|, |Low−PrevClose|)
  +DI = 100 × EMA(+DM) ÷ EMA(TR)
  −DI = 100 × EMA(−DM) ÷ EMA(TR)
  DX = 100 × |+DI − −DI| ÷ (+DI + −DI)
  ADX = EMA(DX, 14)

ADX Interpretation:
  < 20  → Weak/absent trend (ranging market)
  20–25 → Trend beginning to form
  25–40 → Moderate trend (use trend-following strategies)
  40–60 → Strong trend
  60+   → Very strong trend (potential exhaustion watch)

Direction via DI Lines:
  +DI > −DI → Uptrend
  −DI > +DI → Downtrend
  +DI crosses above −DI → Bullish signal
  −DI crosses above +DI → Bearish signal

Best Use: Filter for trend-following strategies
Only use breakout/trend strategies when ADX > 25
```

---

### Parabolic SAR
```
Settings: Step = 0.02, Max = 0.20

Interpretation:
  Dots below price → Uptrend; use as trailing stop
  Dots above price → Downtrend; use as trailing stop
  Price crosses dots → Trend reversal signal

Formula:
  Rising SAR(t) = SAR(t-1) + AF × (EP − SAR(t-1))
  AF starts at 0.02, increases by 0.02 each new high, max 0.20
  EP = Extreme point (highest high in uptrend)

Use:
  ✓ Excellent trailing stop in strong trends
  ✓ Clear visual signals
  ✗ Poor in sideways/choppy markets (whipsaws)
  
Best combined with: ADX > 25 to confirm trending condition
```

---

### Ichimoku Cloud (Ichimoku Kinko Hyo)

#### Five Components
```
1. Tenkan-sen (Conversion Line) = (9H + 9L) ÷ 2
   → 9-period midpoint; short-term trend

2. Kijun-sen (Base Line) = (26H + 26L) ÷ 2
   → 26-period midpoint; medium-term trend/support

3. Senkou Span A (Leading A) = (Tenkan + Kijun) ÷ 2, plotted 26 periods AHEAD
   → Forms top or bottom of Cloud (Kumo)

4. Senkou Span B (Leading B) = (52H + 52L) ÷ 2, plotted 26 periods AHEAD
   → Forms other edge of Cloud

5. Chikou Span (Lagging Span) = Current Close, plotted 26 periods BEHIND
   → Confirms trend; most important confirmation tool
```

#### Cloud (Kumo) Interpretation
```
Price ABOVE Cloud → Bullish (trend bias = long)
Price BELOW Cloud → Bearish (trend bias = short)
Price INSIDE Cloud → Neutral / Consolidation

Green Cloud (Span A > Span B) → Bullish sentiment
Red Cloud (Span B > Span A) → Bearish sentiment

Thick Cloud → Strong support/resistance
Thin Cloud → Weak support/resistance (easier to break through)
```

#### Ichimoku Signals
| Signal | Condition | Strength |
|--------|-----------|----------|
| **TK Cross Bullish** | Tenkan crosses above Kijun | Moderate |
| **TK Cross Bearish** | Tenkan crosses below Kijun | Moderate |
| **Strong Bullish** | TK cross above Cloud + Chikou above price | Strong |
| **Strong Bearish** | TK cross below Cloud + Chikou below price | Strong |
| **Cloud Support** | Price pullback to top of Cloud holds | Bullish |
| **Cloud Resistance** | Price rally to bottom of Cloud fails | Bearish |
| **Kumo Twist** | Cloud changes from red to green ahead | Bullish shift |
| **Chikou Confirm** | Chikou in open space (no obstruction) | Confirmation |

#### Perfect Ichimoku Buy Setup
```
All 5 criteria must be met:
  ✓ Price above Cloud
  ✓ Cloud is green (Span A > Span B)
  ✓ Tenkan above Kijun
  ✓ Chikou above price from 26 periods ago
  ✓ Price pulling back to Tenkan/Kijun for entry
```

---

## 6. Momentum Indicators

### RSI (Relative Strength Index)
```
Settings: 14 periods (default)

RSI = 100 − (100 ÷ (1 + RS))
RS = Average Gain ÷ Average Loss (over 14 periods)

Levels:
  RSI > 70 → Overbought (potential reversal short)
  RSI < 30 → Oversold (potential reversal long)
  RSI = 50 → Midpoint (trend confirmation)
  
Trend Trading:
  RSI 40–90 range in uptrends (buy dips to 40–50)
  RSI 10–60 range in downtrends (sell rallies to 50–60)
```

#### RSI Divergence
```
Regular Bullish Divergence:
  Price: Lower Low → Lower Low
  RSI:   Lower Low → HIGHER Low
  Signal: Bullish reversal

Regular Bearish Divergence:
  Price: Higher High → Higher High
  RSI:   Higher High → LOWER High
  Signal: Bearish reversal

Hidden Bullish Divergence (Continuation):
  Price: Higher Low
  RSI:   Lower Low
  Signal: Uptrend continuation (buy the dip)

Hidden Bearish Divergence (Continuation):
  Price: Lower High
  RSI:   Higher High
  Signal: Downtrend continuation (sell the rally)
```

#### RSI Failure Swings
```
Bullish Failure Swing (Strong Signal):
  1. RSI falls below 30 (oversold)
  2. RSI bounces above 30
  3. RSI pulls back but STAYS ABOVE 30 (failure)
  4. RSI breaks above recent peak → BUY SIGNAL

Bearish Failure Swing:
  1. RSI rises above 70 (overbought)
  2. RSI dips below 70
  3. RSI bounces but STAYS BELOW 70 (failure)
  4. RSI breaks below recent trough → SELL SIGNAL
```

---

### Stochastic Oscillator
```
Settings: %K=14, %D=3, Smooth=3

Fast Stochastic:
  %K = (Current Close − Lowest Low) ÷ (Highest High − Lowest Low) × 100
  %D = 3-period SMA of %K

Slow Stochastic (recommended):
  Slow %K = Fast %D
  Slow %D = 3-period SMA of Slow %K

Levels:
  Above 80 → Overbought
  Below 20 → Oversold

Signals:
  %K crosses above %D in oversold territory → Buy
  %K crosses below %D in overbought territory → Sell
  Divergence with price → Reversal warning
  
Stochastic RSI: Applies RSI formula to Stochastic → more sensitive
```

---

### CCI (Commodity Channel Index)
```
Settings: 14 or 20 periods

CCI = (Typical Price − SMA) ÷ (0.015 × Mean Deviation)
Typical Price = (High + Low + Close) ÷ 3

Levels:
  > +100 → Overbought / Strong trend (buy in strong uptrend)
  < −100 → Oversold / Strong downtrend (sell in downtrend)
  0 line → Neutral

Signals:
  Crosses above +100 → Bullish breakout
  Crosses below −100 → Bearish breakout
  Returns to 0 from extreme → Possible reversal
  Divergence → Leading reversal signal

Use: Good for cyclical markets; works well on commodities
```

---

### Williams %R
```
Settings: 14 periods

%R = (Highest High − Close) ÷ (Highest High − Lowest Low) × (−100)

Range: 0 to −100 (note: inverted scale)
  0 to −20   → Overbought
  −80 to −100 → Oversold

Signals (similar to Stochastic):
  Exit from overbought (below −20) → Sell
  Exit from oversold (above −80) → Buy
  Divergence → Reversal signal
  
Note: Very similar to Stochastic; choose one, not both
```

---

### Rate of Change (ROC)
```
Settings: 12 periods (daily), 9 (weekly)

ROC = ((Close − Close[n]) ÷ Close[n]) × 100

Signals:
  ROC > 0 → Upward momentum
  ROC < 0 → Downward momentum
  Zero line cross → Momentum shift
  Divergence → Reversal warning
  
Use: Relative Strength comparison across assets; momentum ranking
```

---

## 7. Volume Indicators

### OBV (On-Balance Volume)
```
If Close > Previous Close: OBV = OBV(prev) + Volume
If Close < Previous Close: OBV = OBV(prev) − Volume
If Close = Previous Close: OBV = OBV(prev)

Interpretation:
  OBV rising + Price rising → Confirmed uptrend
  OBV falling + Price falling → Confirmed downtrend
  OBV rising + Price flat → Accumulation (bullish)
  OBV falling + Price flat → Distribution (bearish)
  OBV diverges from price → Reversal warning

Key Insight: OBV should CONFIRM price action; divergence = warning
```

---

### VWAP (Volume-Weighted Average Price)
```
VWAP = Σ(Typical Price × Volume) ÷ Σ Volume
Resets each trading session

VWAP Bands (Standard Deviation bands):
  VWAP ± 1 SD → Contains ~68% of price action
  VWAP ± 2 SD → Contains ~95% of price action
  VWAP ± 3 SD → Extreme deviation (mean reversion opportunity)

Trading Strategies:
  Above VWAP → Bullish; buy pullbacks to VWAP
  Below VWAP → Bearish; sell rallies to VWAP
  
  Institutional benchmark: Many algos and funds use VWAP
  Price above VWAP = Buyers in control
  Price below VWAP = Sellers in control

Day Trading Use:
  Open above VWAP → Long bias
  VWAP as support → Buy at VWAP, stop below
  VWAP as resistance → Sell at VWAP, stop above

Mean Reversion:
  Price at ±2 SD → Fade toward VWAP
  Price at ±3 SD → Strong mean reversion signal
```

---

### Accumulation/Distribution Line (A/D)
```
Money Flow Multiplier = ((Close − Low) − (High − Close)) ÷ (High − Low)
Money Flow Volume = MFM × Volume
A/D = Previous A/D + Current Money Flow Volume

Interpretation:
  A/D rising → Accumulation (buying pressure)
  A/D falling → Distribution (selling pressure)
  Divergence from price → Strong reversal signal

Key: Accounts for WHERE close is within bar's range
```

---

### MFI (Money Flow Index)
```
Settings: 14 periods

Typical Price = (H + L + C) ÷ 3
Money Flow = Typical Price × Volume
Positive MF: TP > Previous TP
Negative MF: TP < Previous TP

MFI = 100 − (100 ÷ (1 + (14-day Positive MF ÷ 14-day Negative MF)))

Levels:
  > 80 → Overbought
  < 20 → Oversold

Think of MFI as "Volume-Weighted RSI"
Divergence more significant due to volume confirmation
```

---

### CMF (Chaikin Money Flow)
```
Settings: 20 periods

CMF = 20-period Sum of (Money Flow Volume) ÷ 20-period Sum of Volume
Money Flow Volume = ((Close−Low) − (High−Close)) ÷ (High−Low) × Volume

Range: −1 to +1
  > 0 → Buying pressure; bullish
  < 0 → Selling pressure; bearish
  > +0.25 → Strong buying
  < −0.25 → Strong selling

Use: Confirm breakouts and trend direction
```

---

### Volume Profile
> Enhanced with: "The ONLY Volume Profile Trading Guide" — Trader Dale (396K views, 67% win rate over 9 yrs)

```
Key Levels:
  POC (Point of Control) → Price level with MOST volume traded
  VAH (Value Area High) → Upper boundary of Value Area
  VAL (Value Area Low) → Lower boundary of Value Area
  Value Area → Contains 68–70% of total session volume
  HVN (High Volume Nodes) → Significant volume clusters → secondary entry points
  LVN (Low Volume Nodes) → Sparse trading areas → rejection/fast-move zones

Types:
  Session VP → Volume profile for single session
  Fixed Range VP → User-defined time range
  Visible Range VP → Current chart view
  Composite VP → Multiple sessions combined
```

#### Four Volume Profile Shapes
```
D-SHAPED (Balanced Market) — ~70% of trading is rotation
  Shape: Heavy volume middle, low at edges
  Trade: Short from top border, Long from bottom border → TP at opposite POC
  Signals: Consolidation or pause/end of trend

P-SHAPED (Buyers Active)
  Shape: Heavy volume at TOP, low at bottom
  VALIDATION: Price MUST close ABOVE 50% of daily range (else invalid!)
  Trade: Long from POC or volume bumps in low-volume zone
  Signals: Uptrend in progress or rejection of lower prices

B-SHAPED (Sellers Active)
  Shape: Heavy volume at BOTTOM, low at top
  VALIDATION: Price MUST close BELOW 50% of daily range (else invalid!)
  Trade: Short from POC or volume bumps in high-volume zone
  Pro tip: Trade from BEGINNING of heavy zone, not exact POC (40% fewer missed trades)

THIN PROFILE (Very Strong Trend)
  Shape: Thin line with scattered small volume bumps (no central heavy zone)
  Why: Strong/fast trend — institutions can't build large positions
  Trade: Volume bumps = aggressive institutional entry points → pullback entries
  In uptrend: bumps = strong support. In downtrend: bumps = strong resistance.
```

#### Volume Profile Entry Optimization
```
Traditional: Trade at exact POC → misses many trades
Better (Trader Dale method): Trade from BEGINNING (edge) of heavy volume zone
  → ~40% fewer missed trades, better risk/reward, enters before consolidation

Volume bumps in low-volume zones are AS IMPORTANT as POC:
  Even small bumps = decisive institutional activity
  Price respects these because institutions stepped in aggressively
```

#### Highest-Probability VP Setup: Support-Turned-Resistance + Volume Cluster
```
1. Identify thin profile with significant volume cluster at a price level
2. Check if that level was historical support (or resistance)
3. Price broke through it → support flips to resistance (or vice versa)
4. Now you have DUAL confirmation at same level:
   - Volume cluster (institutional activity)
   - Price action (S/R flip)
5. Trade the level with high confidence

Macro rule: Don't trade against strong macro-news moves.
  Institutions ignore technicals during news shocks → wait for stabilization.
```

#### Volume Profile Decision Tree
```
D-shaped → Short resistance, Long support (rotation play)
P-shaped (close > 50% range) → Long at POC/bumps
B-shaped (close < 50% range) → Short at POC/bumps
Thin → Trade volume bumps as trend-pullback entries
Then: Is there S/R flip + volume cluster confluence? → 2X confirmation
```

---

## 8. Volatility Indicators

### Bollinger Bands
```
Settings: 20 SMA, ±2 Standard Deviations

Upper Band = 20 SMA + (2 × SD)
Middle Band = 20 SMA
Lower Band = 20 SMA − (2 × SD)

Key Metrics:
  %B = (Price − Lower Band) ÷ (Upper Band − Lower Band)
    %B > 1 → Price above upper band
    %B = 0.5 → Price at middle band
    %B < 0 → Price below lower band

  Bandwidth = (Upper − Lower) ÷ Middle × 100
    Expanding → Increasing volatility
    Contracting → Decreasing volatility (squeeze = explosive move incoming)

BB Squeeze:
  Bandwidth at 6-month low → Imminent breakout
  Direction of breakout confirmed by volume and price action

Strategies:
  Mean Reversion: Buy lower band, sell upper band (ranging markets only)
  Trend Following: Price rides upper band = uptrend; sell first close inside band
  Squeeze: Enter breakout direction with momentum confirmation
  W-Bottom: Two touches of lower band; second higher → bullish reversal
  M-Top: Two touches of upper band; second lower → bearish reversal
```

---

### ATR (Average True Range)
```
Settings: 14 periods (standard)

True Range = max(High−Low, |High−PrevClose|, |Low−PrevClose|)
ATR = EMA(True Range, 14)

ATR Multipliers for Stop Loss:
  Conservative: 2.0× ATR
  Standard: 2.5× ATR
  Aggressive: 1.5× ATR
  Volatile markets: 3.0× ATR

ATR Position Sizing:
  Dollar Risk ÷ (ATR × Multiplier) = Number of Shares/Contracts

ATR-Based Targets:
  Target 1: 1.5× ATR from entry
  Target 2: 3.0× ATR from entry
  Target 3: 5.0× ATR from entry

ATR Channel:
  Upper = Price + (1.5 × ATR)
  Lower = Price − (1.5 × ATR)
  Price outside channel = volatility expansion
```

---

### Keltner Channels
```
Settings: EMA=20, ATR=10, Multiplier=2

Middle Line = 20 EMA
Upper Channel = 20 EMA + (2 × ATR)
Lower Channel = 20 EMA − (2 × ATR)

Signals:
  Price above upper channel → Strong uptrend / overbought
  Price below lower channel → Strong downtrend / oversold
  Price re-enters from upper → Potential reversal
  
Combined with Bollinger Bands:
  BB inside Keltner Channels → SQUEEZE (low volatility)
  BB outside Keltner Channels → Expansion phase
  Squeeze + Momentum direction → Best breakout setups
```

---

### Donchian Channels
```
Settings: 20 periods (day), 55 periods (Turtle Trading)

Upper = Highest High of n periods
Lower = Lowest Low of n periods
Middle = (Upper + Lower) ÷ 2

Turtle Trading System:
  Entry: Price breaks 55-period Donchian high/low
  Exit: Price breaks 20-period Donchian in opposite direction
  Stop: 2× ATR from entry
  
Breakout Signals:
  New 20-day high → Short-term bullish
  New 55-day high → Longer-term bullish breakout
  New 52-week high → Major bullish breakout signal
```

---

## 9. Multi-Timeframe Analysis Framework

### The 3-Timeframe System
```
For Each Trading Style:

Day Trading:
  Higher TF: Daily (trend bias)
  Middle TF: 1-hour (setup confirmation)
  Lower TF: 15-minute (entry timing)

Swing Trading:
  Higher TF: Weekly (trend bias)
  Middle TF: Daily (setup confirmation)
  Lower TF: 4-hour (entry timing)

Scalping:
  Higher TF: 15-minute (trend bias)
  Middle TF: 5-minute (setup)
  Lower TF: 1-minute (entry timing)
```

### MTF Analysis Process
```
Step 1: Higher TF → Determine primary trend direction
  Is price above/below key MAs?
  What phase is the market in?
  Are we at key HTF support/resistance?

Step 2: Middle TF → Find setup
  Is there a pullback in direction of HTF trend?
  Is a pattern forming at key level?
  Are momentum indicators aligned?

Step 3: Lower TF → Time entry
  Look for trigger candle at LTF level
  Entry after confirmation of reversal
  Set stop just beyond LTF structure
```

### Top-Down Analysis — Direction, Location, Execution (DLE)
> Source: "The Top Down Analysis Strategy I Will Use For Life" — Jdub Trades ($140K month)

**Three sequential steps (MUST go in order — never start from execution):**
```
Direction (HTF) → Location (MTF) → Execution (LTF)
 Who controls?     Where to trade?    When to enter?
```

**TF Cheat Sheet by Trading Style:**

| Style | Direction (HTF) | Location (MTF) | Execution (LTF) |
|-------|----------------|----------------|-----------------|
| Swing trading | Daily | 1H | 15M |
| Day trading | 4H | 15M / 1H | 5M |
| Scalping | 1H | 15M | 1M |

**Three-Chart Layout (TradingView):**
- Left panel: HTF (direction) — check trend (HH/HL = bullish, LH/LL = bearish)
- Top-right: MTF (location) — mark key levels (PDH/PDL, swing H/L, old H/L)
- Bottom-right: LTF (execution) — wait for entry trigger at key level

**Critical rule:** If HTF is bullish and LTF shows a short setup → DON'T TAKE IT. Wait for LTF alignment with HTF direction. Trading against HTF trend is the #1 reason setups fail despite looking "perfect" on the entry TF.

**DLE Workflow:**
```
1. HTF: Is it trending? (HH/HL or LH/LL) → set bias
2. MTF: Where are the key levels? (PDH, PDL, swing H/L) → set location
3. LTF: Is price at the key level? → wait for break + retest + confirmation → enter
4. Target: HTF key levels (look left on HTF for next objective)
```

---

## 10. Elliott Wave Theory

### Elliott Wave Rules (MUST be satisfied)
```
5-wave Impulse:
  Rule 1: Wave 2 NEVER retraces more than 100% of Wave 1
  Rule 2: Wave 3 is NEVER the shortest impulse wave
  Rule 3: Wave 4 NEVER overlaps into Wave 1 price territory
           (Exception: Diagonal triangles in Wave 1 or 5)
```

### Elliott Wave Guidelines
```
Wave 1: Often muted; not widely recognized
Wave 2: Typically 50–61.8% retracement of Wave 1
Wave 3: Longest and strongest; 161.8% of Wave 1 common
Wave 4: Typically 38.2% retracement of Wave 3
Wave 5: Often equals Wave 1 in length; or 61.8% of W1+W3

Corrective Waves (A-B-C):
  Zigzag: Sharp correction (5-3-5)
  Flat: Sideways correction (3-3-5)
  Triangle: Converging correction (3-3-3-3-3)
  Complex: Combination of above (X waves connecting)
```

### Fibonacci Relationships in Elliott
| Wave | Typical Fibonacci Relationship |
|------|-------------------------------|
| Wave 2 | 50%, 61.8%, 78.6% retrace of Wave 1 |
| Wave 3 | 161.8%, 261.8% of Wave 1 (from end of W2) |
| Wave 4 | 38.2%, 50% retrace of Wave 3 |
| Wave 5 | 61.8% or 100% of Wave 1 (from end of W4) |
| Wave A | 100% of Wave 5 often |
| Wave B | 50%, 61.8%, 78.6% retrace of Wave A |
| Wave C | 100%, 127.2%, 161.8% of Wave A |

### Wave Personality & Psychology
> Sources: "Elliott Wave Trading Was Impossible Until I Discovered These Price Action Clues" — The Secret Mindset (877K views); "Elliott Wave Basics Course" — Elliott Wave Street (live webinar)

**Impulse Waves (1-2-3-4-5):**
```
Wave 1: Least predictive. Sentiment still bearish — most see it as bear rally.
         Sellers add shorts. Subdivides into 5 smaller waves.
         Sometimes appears as leading diagonal (W4 can overlap W1 in diagonals).

Wave 2: Deep retracement (50%, 61.8%, or 78.6% of W1). Sellers feel assured downtrend continues.
         MUST NOT break below W1 start. Forms zigzag or flat (ABC pattern).
         KEY RULE: Must be SLOW. Fast W2 = NOT a real corrective wave = AVOID.
         Slow price = institutions accumulating. Fast price = no big buyer support.

Wave 3: Biggest, most powerful. Best profit opportunity (1:3 to 1:5 RR).
         Sellers' stops triggered at W1 high → fuels momentum.
         Very shallow pullbacks — don't wait for retracement, enter ASAP.
         Projection: 1.618x W1 (most common) or 2.618x W1.
         Usually the extended wave among W1/W3/W5.

Wave 4: Shallow retracement (38.2% or 50% of W3). Profit-taking wave.
         Range-bound, whipsawing, directionless — generates false breakouts.
         Often forms triangle, flat, or zigzag. AVOID new positions here.
         MUST NOT overlap W1 territory (unbreakable rule).
         If W4 is fast → do NOT trade it. Same speed rule as W2.

Wave 5: Final impulse leg. "Retail wave" — everyone bullish, extreme valuations.
         Momentum weaker than W3. Look for RSI/MACD/Stochastic divergence.
         Lower volume than W3 = trend weakening, lock in profits.
         Projection: 100% of W1 (most common) or 61.8% of W1 (from end of W4).
```

**Corrective Waves (A-B-C):**
```
Wave A: Sharp move, similar psychology to W1. Most traders still bullish.
         Subdivides as 5-wave or 3-wave pattern.

Wave B: BULL TRAP — draws in longs thinking trend is healthy.
         Often creates double top near W5 high (fails to breach it).
         Retraces 50%, 61.8%, or 78.6% of Wave A.
         Best trade: FADE Wave B near its terminal point.

Wave C: Final corrective leg. Conviction shifts — uptrend deemed over.
         Projection: 100% of A (most common), then 127.2% of A, then 161.8% of A.
```

### Alternation Rule (W2 vs W4)
```
W2 and W4 must differ in as many ways as possible:
  Price:   W2 deep (61-78%) vs W4 shallow (38%) or vice versa
  Time:    W2 fast vs W4 slow or vice versa
  Pattern: W2 zigzag vs W4 triangle/flat or vice versa
If W2 is simple ABC → expect W4 to be complex (triangle/combination)
```

### Corrective Wave Speed Rule (Critical Filter)
> Source: Elliott Wave Street — "this advice will save you years of frustration"

```
SLOW corrective wave → HIGH probability setup (institutions accumulating)
FAST corrective wave → LOW probability → DO NOT TRADE

Why: Slow = big institutions buying against the correction (price can't fall fast)
     Fast = no institutional support → trend likely continues against you

Apply to: W2, W4, Wave B, any ABC you plan to trade
Visual check: Compare speed of corrective move vs previous impulse move
Indicator check: Look for divergence between A and C legs (RSI/MACD)
```

### Elliott Wave Trading Strategy
```
Best Trades (in order of probability):
  1. After W2 ABC completion → ride W3 (highest RR: 1:3 to 1:5)
  2. Fade Wave B near W5 high → ride Wave C
  3. After W4 completion → ride W5 (weaker than W3)

Entry Rules:
  1. Identify 5-wave impulse completion (W1)
  2. Wait for SLOW 3-wave (ABC) corrective move
  3. Confirm: divergence between A and C, or candlestick reversal at C
  4. Enter at C completion OR when price clears W1 high/low
  5. SL: below/above the corrective wave extreme
  6. TP: previous swing high (W1 high), then project W3 target

Counter-Trend Trades (advanced — only after mastering trend-following):
  Most aggressive: Sell at W5 completion + rejection/reversal signal
  Moderate:        Sell after 5-wave sequence completes + first impulse down
  Conservative:    Sell after 3-wave bounce (ABC) completes = trend trade in new direction

Fractal Application:
  - Same wave structure repeats on ALL timeframes (monthly to 15-sec)
  - Degrees are visible on same chart — no need to switch TF to label
  - HTF wave count → MTF setup → LTF entry (same DLE framework)
  - Weekly/Monthly: find where you are in the cycle
  - Daily/4H: identify current wave for swing trades
  - 1M/5M: scalp entries at ABC completions
```

### Corrective Pattern Types
```
Single Zigzag:  ABC (5-3-5) — sharp, deep correction
Double Zigzag:  WXY (W=first zigzag, X=connector, Y=second zigzag)
Flat:           ABC — B retraces 90-138.2% of A (tricky: fast B leg)
Triangle:       ABCDE — converging, usually in W4 position
Combination:    Mix of above connected by X waves

Leading Diagonal: Occurs in W1 or W5 position.
  Looks like wedge (expanding or contracting).
  W4 CAN overlap W1 territory (exception to normal rule).
  Still 5-wave structure but with overlapping waves.
```

### Elliott Wave Quick Checklist
```
□ W1, W3, W5 are trending (impulse). W2, W4 are corrections
□ W3 must NOT be shortest of W1/W3/W5 (need not be longest)
□ W2 can retrace up to 99% of W1 (never 100%)
□ W4 never enters W1 price territory (except leading diagonal)
□ W4 should not enter W2 price area
□ W2 and W4 display alternation (price, time, pattern)
□ Corrective waves you trade MUST be slow (speed filter)
□ Look for W5 divergence on RSI/MACD + lower volume
□ Beginners: ONLY trade with trend (buy W2/W4 completions)
```

---

## 11. Harmonic Patterns

### ABCD Pattern
```
AB = CD (time and price symmetry)
BC: 61.8% or 78.6% of AB
CD: 127.2% or 161.8% of BC

Bullish ABCD: Buy at D
Bearish ABCD: Sell at D
Stop: Beyond D by structure
Target: B level (38.2% and 61.8% of AD)
```

### Gartley Pattern
```
XA: Initial move
AB: 61.8% retrace of XA
BC: 38.2–88.6% retrace of AB
CD: 78.6% retrace of XA (PRZ = Potential Reversal Zone)
Note: BC can project 127.2–161.8% to locate D

Bullish Gartley: Buy at D (78.6% of XA)
Stop: Below X
Target 1: 61.8% of CD
Target 2: 127.2% of CD
Reliability: 65–70%
```

### Butterfly Pattern
```
XA: Initial move
AB: 78.6% retrace of XA
BC: 38.2–88.6% retrace of AB
CD: 127.2% OR 161.8% extension of XA (beyond X)
PRZ: 127.2–161.8% of XA

Reliability: 70–75%
Note: D extends BEYOND X (unlike Gartley)
```

### Bat Pattern
```
AB: 38.2–50% retrace of XA (key differentiator from Gartley)
BC: 38.2–88.6% retrace of AB
CD: 88.6% retrace of XA (PRZ)

Reliability: 72–78%
Tighter stops than Gartley; high accuracy
```

### Crab Pattern
```
AB: 38.2–61.8% retrace of XA
BC: 38.2–88.6% retrace of AB
CD: 161.8% extension of XA (deepest extension)
PRZ: 161.8% of XA

Reliability: 65–70%
Most extreme extension; use tight stops
```

### Shark Pattern
```
Initial 0X move
X to A: Any move
A to B: 113% extension of 0A
B to C: 88.6% retrace of 0B or 161.8% of AB
PRZ at C: 88.6% of 0X or 113% of XA
```

### Cypher Pattern
```
XA: Initial move
AB: 38.2–61.8% retrace of XA
BC: 127.2–141.4% extension of XA
CD: 78.6% retrace of XC (PRZ)

Reliability: 70–75%
```

### Harmonic Pattern Trading Rules
```
Entry: At PRZ (Potential Reversal Zone)
Confirmation: Wait for reversal candle at PRZ
Stop: Beyond the extreme of pattern (D or X depending on pattern)
Target 1: 38.2% retrace of CD
Target 2: 61.8% retrace of CD  
Target 3: Full retracement to AB or beyond

Risk Management: Risk 1–1.5% per harmonic trade
Timeframes: Best on 1h, 4h, Daily charts
```

---

## 12. Market Profile / Auction Market Theory

### Key Concepts
```
TPO (Time Price Opportunity): Letter assigned to each price traded in a given period
Initial Balance (IB): Price range of first 1 hour; sets the day's range expectation
Value Area: Price range containing 70% of volume/TPOs
POC: Most frequently traded price
```

### Market Profile Day Types
| Day Type | Characteristics | Trading Approach |
|----------|----------------|-----------------|
| **Normal** | Opens, finds value near open | Range trade IB extremes |
| **Normal Variation** | Breaks IB in one direction | Trade breakout direction |
| **Trend Day** | Strong directional move; range expands all day | Trend follow; don't fade |
| **Double Distribution** | Two distinct value areas | Trade between distributions |
| **Neutral** | Balanced; rotates but no breakout | Fade extremes |
| **Spike and Distribution** | Gap + auction finding value | Trade inside distribution |

### Auction Market Theory Principles
```
1. Markets are always in the process of facilitating trade
2. Price moves to FIND responsive buyers and sellers
3. Price moves AWAY from value to advertise opportunity
4. When price finds two-sided trade, it consolidates (value)
5. When price fails to find trade, it moves away (trend)

Auction Phases:
  Initiation → Price moves to discover new value
  Responsive → Participants respond at extremes (mean reversion)
  Facilitation → Price rotates within value area

Trading Signals:
  Price above prior day VAH → Bullish; long opportunities
  Price below prior day VAL → Bearish; short opportunities
  Price returns to prior POC → Magnet effect
  Price breaks out of prior day range + volume → Trending day
```

### Market Profile vs. Volume Profile
| Feature | Market Profile | Volume Profile |
|---------|---------------|---------------|
| Unit | TPO (time) | Volume |
| POC | Most TIME spent | Most VOLUME traded |
| Data need | TPO letters | Actual volume by price |
| Best use | Auction analysis | Liquidity analysis |
| Preference | Futures traders | Stock/equity traders |

---

## 13. Reference Files

### [references/mtf-confluence.md](references/mtf-confluence.md)
Load for: multi-timeframe confluence scoring, timeframe bias calculation, TF weight system, confluence heat maps, multi-pair scanning.

---

## 14. Pattern Reliability Summary Table

| Pattern | Type | Reliability | Best Context |
|---------|------|-------------|-------------|
| Abandoned Baby | Reversal | 85–90% | After extended trend |
| Morning/Evening Doji Star | Reversal | 83–87% | At key S/R |
| Morning/Evening Star | Reversal | 78–83% | At key S/R |
| Three White/Black Soldiers | Rev/Cont | 70–75% | After consolidation |
| Head & Shoulders | Reversal | 83–85% | At market tops/bottoms |
| Bullish/Bearish Engulfing | Reversal | 72–78% | At key levels |
| Cup & Handle | Continuation | 75–80% | After consolidation |
| Bull/Bear Flag | Continuation | 80–85% | Mid-trend |
| Double Top/Bottom | Reversal | 75–80% | Extended trend |
| Ascending/Descending Triangle | Continuation | 72–75% | In established trend |
| Hammer/Shooting Star | Reversal | 60–70% | At clear S/R |
| Doji | Indecision | 50–65% | Requires confirmation |

---

## 15. Python Strategy Engines

### Fibonacci Strategy Engine

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

FIB_LEVELS = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
FIB_EXTENSIONS = [1.0, 1.272, 1.414, 1.618, 2.0, 2.618]

class FibonacciEngine:

    @staticmethod
    def retracement(swing_high: float, swing_low: float, direction: str = "up") -> dict:
        diff = swing_high - swing_low
        levels = {}
        for fib in FIB_LEVELS:
            if direction == "up":
                levels[f"{fib:.3f}"] = round(swing_high - fib * diff, 5)
            else:
                levels[f"{fib:.3f}"] = round(swing_low + fib * diff, 5)
        return {
            "direction": direction, "swing_high": swing_high, "swing_low": swing_low,
            "levels": levels,
            "golden_zone": f"{levels['0.618']} — {levels['0.786']}",
            "strategy": "Buy at 0.618-0.786 in uptrend, sell at 0.618-0.786 in downtrend",
        }

    @staticmethod
    def extension(point_a: float, point_b: float, point_c: float) -> dict:
        diff = abs(point_b - point_a)
        direction = 1 if point_b > point_a else -1
        levels = {}
        for ext in FIB_EXTENSIONS:
            levels[f"{ext:.3f}"] = round(point_c + direction * diff * ext, 5)
        return {"extensions": levels, "primary_target": levels["1.618"]}

    @staticmethod
    def auto_fib(df: pd.DataFrame, order: int = 10) -> dict:
        """Automatically detect last major swing and compute fibs."""
        highs = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows = argrelextrema(df["low"].values, np.less, order=order)[0]
        if len(highs) == 0 or len(lows) == 0:
            return {"error": "No swings found"}
        last_high = df["high"].iloc[highs[-1]]
        last_low = df["low"].iloc[lows[-1]]
        last_high_idx = highs[-1]
        last_low_idx = lows[-1]
        direction = "up" if last_low_idx < last_high_idx else "down"
        return FibonacciEngine.retracement(last_high, last_low, direction)

    @staticmethod
    def cluster_zones(fibs_list: list[dict], tolerance: float = 0.0005) -> list[dict]:
        """Find confluence zones where multiple fib levels cluster together."""
        all_levels = []
        for fib_set in fibs_list:
            for level_name, price in fib_set.get("levels", {}).items():
                all_levels.append(price)
        all_levels.sort()
        clusters = []
        i = 0
        while i < len(all_levels):
            cluster = [all_levels[i]]
            while i + 1 < len(all_levels) and all_levels[i + 1] - all_levels[i] < tolerance:
                i += 1
                cluster.append(all_levels[i])
            if len(cluster) >= 2:
                clusters.append({
                    "zone_center": round(np.mean(cluster), 5),
                    "zone_width": round(max(cluster) - min(cluster), 5),
                    "n_fibs_confluent": len(cluster),
                    "strength": "STRONG" if len(cluster) >= 3 else "MODERATE",
                })
            i += 1
        return sorted(clusters, key=lambda c: c["n_fibs_confluent"], reverse=True)
```

---

### Ichimoku Complete Strategy

```python
import pandas as pd, numpy as np

class IchimokuStrategy:
    @staticmethod
    def compute(df: pd.DataFrame, tenkan: int = 9, kijun: int = 26, senkou_b: int = 52) -> pd.DataFrame:
        d = df.copy()
        d["tenkan"] = (df["high"].rolling(tenkan).max() + df["low"].rolling(tenkan).min()) / 2
        d["kijun"] = (df["high"].rolling(kijun).max() + df["low"].rolling(kijun).min()) / 2
        d["senkou_a"] = ((d["tenkan"] + d["kijun"]) / 2).shift(kijun)
        d["senkou_b"] = ((df["high"].rolling(senkou_b).max() + df["low"].rolling(senkou_b).min()) / 2).shift(kijun)
        d["chikou"] = df["close"].shift(-kijun)
        return d

    @staticmethod
    def full_signal(df: pd.DataFrame) -> dict:
        d = IchimokuStrategy.compute(df)
        c = d.iloc[-1]; p = d.iloc[-2]
        above_cloud = c["close"] > max(c["senkou_a"], c["senkou_b"])
        below_cloud = c["close"] < min(c["senkou_a"], c["senkou_b"])
        tk_cross_up = c["tenkan"] > c["kijun"] and p["tenkan"] <= p["kijun"]
        tk_cross_down = c["tenkan"] < c["kijun"] and p["tenkan"] >= p["kijun"]
        kumo_bullish = c["senkou_a"] > c["senkou_b"]
        chikou_above = d["chikou"].iloc[-kijun if len(d) > 26 else -1] > d["close"].iloc[-kijun if len(d) > 26 else -1] if len(d) > 26 else False

        # 5-element confirmation
        bull_count = sum([above_cloud, c["tenkan"] > c["kijun"], kumo_bullish, tk_cross_up, chikou_above])
        bear_count = sum([below_cloud, c["tenkan"] < c["kijun"], not kumo_bullish, tk_cross_down, not chikou_above])

        return {
            "strategy": "ichimoku_complete",
            "above_cloud": above_cloud, "below_cloud": below_cloud,
            "tk_cross": "BULLISH" if tk_cross_up else "BEARISH" if tk_cross_down else "NONE",
            "kumo_color": "BULLISH" if kumo_bullish else "BEARISH",
            "bullish_confirmations": bull_count,
            "bearish_confirmations": bear_count,
            "signal": "STRONG BUY" if bull_count >= 4 else "BUY" if bull_count >= 3 and above_cloud
                     else "STRONG SELL" if bear_count >= 4 else "SELL" if bear_count >= 3 and below_cloud
                     else "WAIT — inside cloud or mixed signals",
            "kumo_support": round(min(c["senkou_a"], c["senkou_b"]), 5),
            "kumo_resistance": round(max(c["senkou_a"], c["senkou_b"]), 5),
        }
```

---

### MA Ribbon Strategy

```python
import pandas as pd, numpy as np

class MARibbonStrategy:
    @staticmethod
    def compute_ribbon(df: pd.DataFrame, periods: list[int] = None) -> pd.DataFrame:
        periods = periods or [8, 13, 21, 34, 55, 89, 144, 200]
        result = df.copy()
        for p in periods:
            result[f"ema_{p}"] = df["close"].ewm(span=p).mean()
        return result

    @staticmethod
    def ribbon_signal(df: pd.DataFrame) -> dict:
        r = MARibbonStrategy.compute_ribbon(df)
        ema_cols = [c for c in r.columns if c.startswith("ema_")]
        last_values = [r[c].iloc[-1] for c in ema_cols]
        # Check alignment
        all_bullish = all(last_values[i] > last_values[i+1] for i in range(len(last_values)-1))
        all_bearish = all(last_values[i] < last_values[i+1] for i in range(len(last_values)-1))
        # Compression: all MAs close together
        spread = (max(last_values) - min(last_values)) / max(last_values) * 100
        compressed = spread < 0.5
        # Expansion
        prev_spread = (max(r[c].iloc[-10] for c in ema_cols) - min(r[c].iloc[-10] for c in ema_cols)) / max(r[c].iloc[-10] for c in ema_cols) * 100
        expanding = spread > prev_spread * 1.3
        return {
            "strategy": "ma_ribbon",
            "fully_bullish": all_bullish, "fully_bearish": all_bearish,
            "spread_pct": round(spread, 3),
            "compressed": compressed, "expanding": expanding,
            "signal": "STRONG BUY — full ribbon alignment" if all_bullish and expanding
                     else "STRONG SELL — full ribbon alignment" if all_bearish and expanding
                     else "BREAKOUT IMMINENT — ribbon compressed" if compressed
                     else "BUY BIAS" if all_bullish else "SELL BIAS" if all_bearish else "MIXED",
        }
```

---

### Pivot Point Strategies

```python
import pandas as pd, numpy as np

class PivotPointStrategies:

    @staticmethod
    def classic(high: float, low: float, close: float) -> dict:
        p = (high + low + close) / 3
        return {"pivot": round(p, 5), "r1": round(2*p - low, 5), "s1": round(2*p - high, 5),
                "r2": round(p + (high - low), 5), "s2": round(p - (high - low), 5),
                "r3": round(high + 2*(p - low), 5), "s3": round(low - 2*(high - p), 5), "method": "classic"}

    @staticmethod
    def fibonacci(high: float, low: float, close: float) -> dict:
        p = (high + low + close) / 3
        r = high - low
        return {"pivot": round(p, 5), "r1": round(p + 0.382*r, 5), "s1": round(p - 0.382*r, 5),
                "r2": round(p + 0.618*r, 5), "s2": round(p - 0.618*r, 5),
                "r3": round(p + r, 5), "s3": round(p - r, 5), "method": "fibonacci"}

    @staticmethod
    def camarilla(high: float, low: float, close: float) -> dict:
        r = high - low
        return {"r4": round(close + r*1.1/2, 5), "r3": round(close + r*1.1/4, 5),
                "r2": round(close + r*1.1/6, 5), "r1": round(close + r*1.1/12, 5),
                "s1": round(close - r*1.1/12, 5), "s2": round(close - r*1.1/6, 5),
                "s3": round(close - r*1.1/4, 5), "s4": round(close - r*1.1/2, 5),
                "method": "camarilla",
                "strategy": "Buy S3, TP at S2/S1. Sell R3, TP at R2/R1. Breakout beyond R4/S4."}

    @staticmethod
    def woodie(high: float, low: float, close: float) -> dict:
        p = (high + low + 2*close) / 4
        return {"pivot": round(p, 5), "r1": round(2*p - low, 5), "s1": round(2*p - high, 5),
                "r2": round(p + (high - low), 5), "s2": round(p - (high - low), 5), "method": "woodie"}

    @staticmethod
    def all_pivots(high: float, low: float, close: float, current_price: float) -> dict:
        classic = PivotPointStrategies.classic(high, low, close)
        fib = PivotPointStrategies.fibonacci(high, low, close)
        cam = PivotPointStrategies.camarilla(high, low, close)
        # Find nearest level
        all_levels = [(k, v) for k, v in {**classic, **fib}.items() if isinstance(v, float)]
        nearest = min(all_levels, key=lambda x: abs(x[1] - current_price))
        return {
            "classic": classic, "fibonacci": fib, "camarilla": cam,
            "nearest_level": {"name": nearest[0], "price": nearest[1], "distance_pips": round(abs(nearest[1] - current_price) * 10000, 1)},
            "above_pivot": current_price > classic["pivot"],
            "bias": "BULLISH (above pivot)" if current_price > classic["pivot"] else "BEARISH (below pivot)",
        }
```

---

### Momentum & ROC Strategy

```python
import pandas as pd, numpy as np

class MomentumStrategies:

    @staticmethod
    def rate_of_change(df: pd.DataFrame, periods: list[int] = [5, 10, 20]) -> dict:
        close = df["close"]
        rocs = {}
        for p in periods:
            roc = ((close - close.shift(p)) / close.shift(p)) * 100
            rocs[f"roc_{p}"] = round(roc.iloc[-1], 3)
        # Multi-period momentum score
        avg_roc = np.mean(list(rocs.values()))
        return {
            "strategy": "rate_of_change",
            **rocs,
            "avg_momentum": round(avg_roc, 3),
            "signal": "STRONG BUY" if avg_roc > 1.0 else "BUY" if avg_roc > 0.3
                     else "STRONG SELL" if avg_roc < -1.0 else "SELL" if avg_roc < -0.3
                     else "NEUTRAL",
            "accelerating": rocs.get(f"roc_{periods[0]}", 0) > rocs.get(f"roc_{periods[-1]}", 0),
        }

    @staticmethod
    def williams_r(df: pd.DataFrame, period: int = 14) -> dict:
        high = df["high"].rolling(period).max()
        low = df["low"].rolling(period).min()
        wr = -100 * (high - df["close"]) / (high - low).replace(0, np.nan)
        return {
            "strategy": "williams_r",
            "value": round(wr.iloc[-1], 1),
            "overbought": wr.iloc[-1] > -20,
            "oversold": wr.iloc[-1] < -80,
            "signal": "SELL (overbought)" if wr.iloc[-1] > -20 else "BUY (oversold)" if wr.iloc[-1] < -80 else "NEUTRAL",
        }

    @staticmethod
    def cci_strategy(df: pd.DataFrame, period: int = 20) -> dict:
        tp = (df["high"] + df["low"] + df["close"]) / 3
        sma = tp.rolling(period).mean()
        mad = tp.rolling(period).apply(lambda x: np.abs(x - x.mean()).mean())
        cci = (tp - sma) / (0.015 * mad)
        return {
            "strategy": "cci",
            "value": round(cci.iloc[-1], 1),
            "signal": "BUY" if cci.iloc[-1] < -100 else "SELL" if cci.iloc[-1] > 100 else "NEUTRAL",
            "trend_strength": "STRONG" if abs(cci.iloc[-1]) > 200 else "MODERATE" if abs(cci.iloc[-1]) > 100 else "WEAK",
        }

    @staticmethod
    def momentum_composite(df: pd.DataFrame) -> dict:
        roc = MomentumStrategies.rate_of_change(df)
        wr = MomentumStrategies.williams_r(df)
        cci = MomentumStrategies.cci_strategy(df)
        scores = []
        for s in [roc, wr, cci]:
            if "BUY" in s["signal"]: scores.append(1)
            elif "SELL" in s["signal"]: scores.append(-1)
            else: scores.append(0)
        avg = np.mean(scores)
        return {
            "roc": roc, "williams_r": wr, "cci": cci,
            "composite_score": round(avg, 2),
            "consensus": "BUY" if avg > 0.3 else "SELL" if avg < -0.3 else "MIXED",
        }
```

---

### Divergence Strategy Engine

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class DivergenceEngine:

    @staticmethod
    def detect_all(df: pd.DataFrame) -> dict:
        close = df["close"]
        rsi = DivergenceEngine._rsi(close)
        macd_line = close.ewm(span=12).mean() - close.ewm(span=26).mean()

        results = []
        for indicator, name in [(rsi, "RSI"), (macd_line, "MACD")]:
            reg = DivergenceEngine._find_divergences(close, indicator, "regular")
            hid = DivergenceEngine._find_divergences(close, indicator, "hidden")
            results.extend([{**d, "indicator": name} for d in reg + hid])

        return {
            "divergences": results[-10:],
            "latest": results[-1] if results else None,
            "bullish_count": sum(1 for d in results if "bullish" in d["type"]),
            "bearish_count": sum(1 for d in results if "bearish" in d["type"]),
        }

    @staticmethod
    def _rsi(close: pd.Series, period: int = 14) -> pd.Series:
        delta = close.diff()
        gain = delta.where(delta > 0, 0).rolling(period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        return 100 - 100 / (1 + gain / loss.replace(0, np.nan))

    @staticmethod
    def _find_divergences(price: pd.Series, indicator: pd.Series, div_type: str) -> list:
        order = 5
        p_lows = argrelextrema(price.values, np.less, order=order)[0]
        p_highs = argrelextrema(price.values, np.greater, order=order)[0]
        i_lows = argrelextrema(indicator.values, np.less, order=order)[0]
        i_highs = argrelextrema(indicator.values, np.greater, order=order)[0]
        divs = []

        if div_type == "regular":
            # Bullish: price lower low, indicator higher low
            for i in range(len(p_lows) - 1):
                idx1, idx2 = p_lows[-2], p_lows[-1]
                if price.iloc[idx2] < price.iloc[idx1]:
                    nearest_i = min(i_lows, key=lambda x: abs(x - idx2)) if len(i_lows) > 0 else idx2
                    nearest_i_prev = min(i_lows, key=lambda x: abs(x - idx1)) if len(i_lows) > 0 else idx1
                    if indicator.iloc[nearest_i] > indicator.iloc[nearest_i_prev]:
                        divs.append({"type": "regular_bullish", "idx": int(idx2), "signal": "BUY — regular bullish divergence", "reliability": 0.72})
                break
            # Bearish: price higher high, indicator lower high
            for i in range(len(p_highs) - 1):
                idx1, idx2 = p_highs[-2], p_highs[-1]
                if price.iloc[idx2] > price.iloc[idx1]:
                    nearest_i = min(i_highs, key=lambda x: abs(x - idx2)) if len(i_highs) > 0 else idx2
                    nearest_i_prev = min(i_highs, key=lambda x: abs(x - idx1)) if len(i_highs) > 0 else idx1
                    if indicator.iloc[nearest_i] < indicator.iloc[nearest_i_prev]:
                        divs.append({"type": "regular_bearish", "idx": int(idx2), "signal": "SELL — regular bearish divergence", "reliability": 0.72})
                break

        elif div_type == "hidden":
            # Hidden bullish: price higher low, indicator lower low (trend continuation)
            if len(p_lows) >= 2:
                idx1, idx2 = p_lows[-2], p_lows[-1]
                if price.iloc[idx2] > price.iloc[idx1]:
                    nearest_i = min(i_lows, key=lambda x: abs(x - idx2)) if len(i_lows) > 0 else idx2
                    nearest_i_prev = min(i_lows, key=lambda x: abs(x - idx1)) if len(i_lows) > 0 else idx1
                    if indicator.iloc[nearest_i] < indicator.iloc[nearest_i_prev]:
                        divs.append({"type": "hidden_bullish", "idx": int(idx2), "signal": "BUY — hidden bullish (trend continuation)", "reliability": 0.65})

        return divs
```

---

### Heikin Ashi & Renko Strategies

```python
import pandas as pd, numpy as np

class HeikinAshiStrategy:
    @staticmethod
    def compute_ha(df: pd.DataFrame) -> pd.DataFrame:
        ha = df.copy()
        ha["ha_close"] = (df["open"] + df["high"] + df["low"] + df["close"]) / 4
        ha["ha_open"] = 0.0
        ha.iloc[0, ha.columns.get_loc("ha_open")] = (df.iloc[0]["open"] + df.iloc[0]["close"]) / 2
        for i in range(1, len(ha)):
            ha.iloc[i, ha.columns.get_loc("ha_open")] = (ha.iloc[i-1]["ha_open"] + ha.iloc[i-1]["ha_close"]) / 2
        ha["ha_high"] = ha[["high", "ha_open", "ha_close"]].max(axis=1)
        ha["ha_low"] = ha[["low", "ha_open", "ha_close"]].min(axis=1)
        return ha

    @staticmethod
    def ha_signal(df: pd.DataFrame) -> dict:
        ha = HeikinAshiStrategy.compute_ha(df)
        last = ha.iloc[-1]
        prev = ha.iloc[-2]
        bullish = last["ha_close"] > last["ha_open"]
        no_lower_wick = last["ha_low"] == min(last["ha_open"], last["ha_close"])
        strong_bull = bullish and no_lower_wick
        bearish = last["ha_close"] < last["ha_open"]
        no_upper_wick = last["ha_high"] == max(last["ha_open"], last["ha_close"])
        strong_bear = bearish and no_upper_wick
        # Trend change
        prev_bull = prev["ha_close"] > prev["ha_open"]
        reversal_up = bullish and not prev_bull
        reversal_down = bearish and prev_bull
        return {
            "strategy": "heikin_ashi",
            "current": "STRONG BULLISH" if strong_bull else "BULLISH" if bullish else "STRONG BEARISH" if strong_bear else "BEARISH",
            "reversal_signal": "BUY REVERSAL" if reversal_up else "SELL REVERSAL" if reversal_down else "CONTINUATION",
            "no_lower_wick": no_lower_wick,
            "no_upper_wick": no_upper_wick,
            "note": "No wick = strong momentum. Both wicks = indecision.",
        }

class RenkoStrategy:
    @staticmethod
    def compute_renko(close: pd.Series, brick_size: float) -> pd.DataFrame:
        bricks = []
        current = close.iloc[0]
        for price in close:
            while price >= current + brick_size:
                current += brick_size
                bricks.append({"price": current, "direction": "up"})
            while price <= current - brick_size:
                current -= brick_size
                bricks.append({"price": current, "direction": "down"})
        return pd.DataFrame(bricks)

    @staticmethod
    def renko_signal(close: pd.Series, brick_size: float) -> dict:
        renko = RenkoStrategy.compute_renko(close, brick_size)
        if renko.empty: return {"signal": "NO BRICKS"}
        last_3 = renko.tail(3)
        all_up = all(last_3["direction"] == "up")
        all_down = all(last_3["direction"] == "down")
        reversal = len(renko) >= 2 and renko.iloc[-1]["direction"] != renko.iloc[-2]["direction"]
        return {
            "strategy": "renko",
            "n_bricks": len(renko),
            "last_direction": renko.iloc[-1]["direction"],
            "signal": "STRONG BUY" if all_up else "STRONG SELL" if all_down else "REVERSAL" if reversal else "MIXED",
            "brick_size": brick_size,
        }
```

---

### Volume Profile Strategy

```python
import pandas as pd, numpy as np

class VolumeProfile:

    @staticmethod
    def compute(df: pd.DataFrame, n_bins: int = 50) -> dict:
        """Build volume profile: volume distributed across price levels."""
        price_range = df["high"].max() - df["low"].min()
        bin_size = price_range / n_bins
        bins = np.arange(df["low"].min(), df["high"].max() + bin_size, bin_size)
        profile = pd.Series(0.0, index=bins[:-1])

        for _, row in df.iterrows():
            bar_bins = bins[(bins >= row["low"]) & (bins < row["high"])]
            vol_per_bin = row["volume"] / max(len(bar_bins), 1)
            for b in bar_bins:
                if b in profile.index:
                    profile[b] += vol_per_bin

        poc = profile.idxmax()
        total_vol = profile.sum()
        # Value Area: 70% of volume around POC
        sorted_profile = profile.sort_values(ascending=False)
        va_vol = 0
        va_levels = []
        for level, vol in sorted_profile.items():
            va_levels.append(level)
            va_vol += vol
            if va_vol >= total_vol * 0.70:
                break
        vah = max(va_levels)
        val = min(va_levels)

        # High/Low volume nodes
        threshold_high = profile.quantile(0.8)
        threshold_low = profile.quantile(0.2)
        hvn = profile[profile > threshold_high].index.tolist()
        lvn = profile[profile < threshold_low].index.tolist()

        current = df.iloc[-1]["close"]
        return {
            "poc": round(poc, 5),
            "value_area_high": round(vah, 5),
            "value_area_low": round(val, 5),
            "current_vs_va": "ABOVE VA" if current > vah else "BELOW VA" if current < val else "INSIDE VA",
            "high_volume_nodes": [round(h, 5) for h in hvn[:5]],
            "low_volume_nodes": [round(l, 5) for l in lvn[:5]],
            "strategy": "Buy at VAL, sell at VAH when inside VA. Breakout trade when outside VA.",
            "poc_acts_as": "Magnet — price tends to return to POC",
            "lvn_acts_as": "Price moves quickly through LVN — fast moves expected",
        }
```

---

### Trend Following Systems

Research: Jegadeesh & Titman documented ~1% monthly alpha. 2024 SSRN study: 15.19% CAGR, 6.18% annualized alpha (1991-2024).

```python
import pandas as pd, numpy as np

class TrendFollowingSystems:

    @staticmethod
    def ma_crossover(df: pd.DataFrame, fast: int = 20, slow: int = 50, use_ema: bool = True) -> dict:
        """Classic MA crossover — golden/death cross. Most researched strategy in finance."""
        close = df["close"]
        ma_fn = lambda s, p: s.ewm(span=p).mean() if use_ema else s.rolling(p).mean()
        fast_ma = ma_fn(close, fast)
        slow_ma = ma_fn(close, slow)
        cross_up = (fast_ma.iloc[-1] > slow_ma.iloc[-1]) and (fast_ma.iloc[-2] <= slow_ma.iloc[-2])
        cross_down = (fast_ma.iloc[-1] < slow_ma.iloc[-1]) and (fast_ma.iloc[-2] >= slow_ma.iloc[-2])
        trend = "BULLISH" if fast_ma.iloc[-1] > slow_ma.iloc[-1] else "BEARISH"
        return {
            "strategy": f"{'EMA' if use_ema else 'SMA'}_{fast}/{slow}_crossover",
            "trend": trend, "cross_up": cross_up, "cross_down": cross_down,
            "fast_ma": round(fast_ma.iloc[-1], 5), "slow_ma": round(slow_ma.iloc[-1], 5),
            "distance_pct": round((fast_ma.iloc[-1] / slow_ma.iloc[-1] - 1) * 100, 3),
            "signal": "BUY" if cross_up else "SELL" if cross_down else f"HOLD {trend}",
        }

    @staticmethod
    def triple_ma(df: pd.DataFrame, fast: int = 10, mid: int = 20, slow: int = 50) -> dict:
        """Triple MA alignment — strongest when all 3 aligned."""
        close = df["close"]
        f = close.ewm(span=fast).mean().iloc[-1]
        m = close.ewm(span=mid).mean().iloc[-1]
        s = close.ewm(span=slow).mean().iloc[-1]
        aligned_up = f > m > s
        aligned_down = f < m < s
        return {
            "strategy": f"triple_ema_{fast}/{mid}/{slow}",
            "aligned_bullish": aligned_up, "aligned_bearish": aligned_down,
            "signal": "STRONG BUY" if aligned_up else "STRONG SELL" if aligned_down else "NO ALIGNMENT — wait",
            "fast": round(f, 5), "mid": round(m, 5), "slow": round(s, 5),
        }

    @staticmethod
    def turtle_breakout(df: pd.DataFrame, entry_period: int = 20, exit_period: int = 10,
                         atr_mult: float = 2.0) -> dict:
        """Turtle Trading System — Richard Dennis' famous trend system."""
        high_entry = df["high"].rolling(entry_period).max().shift(1)
        low_entry = df["low"].rolling(entry_period).min().shift(1)
        high_exit = df["high"].rolling(exit_period).max().shift(1)
        low_exit = df["low"].rolling(exit_period).min().shift(1)
        atr = ((df["high"] - df["low"]).rolling(20).mean())
        current = df.iloc[-1]
        return {
            "strategy": f"turtle_{entry_period}/{exit_period}",
            "long_entry": round(high_entry.iloc[-1], 5),
            "short_entry": round(low_entry.iloc[-1], 5),
            "long_exit": round(low_exit.iloc[-1], 5),
            "short_exit": round(high_exit.iloc[-1], 5),
            "long_signal": current["close"] > high_entry.iloc[-1],
            "short_signal": current["close"] < low_entry.iloc[-1],
            "atr_stop": round(atr.iloc[-1] * atr_mult, 5),
            "unit_size_note": "Position = 1% risk / (ATR * point_value)",
        }

    @staticmethod
    def adx_trend_rider(df: pd.DataFrame, adx_threshold: int = 25) -> dict:
        """ADX-filtered trend riding — only trade when ADX confirms trend strength."""
        close = df["close"]
        plus_dm = df["high"].diff().clip(lower=0).rolling(14).mean()
        minus_dm = (-df["low"].diff()).clip(lower=0).rolling(14).mean()
        atr = (df["high"] - df["low"]).rolling(14).mean()
        plus_di = 100 * plus_dm / atr.replace(0, np.nan)
        minus_di = 100 * minus_dm / atr.replace(0, np.nan)
        dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di).replace(0, np.nan)
        adx = dx.rolling(14).mean()
        trending = adx.iloc[-1] > adx_threshold
        direction = "LONG" if plus_di.iloc[-1] > minus_di.iloc[-1] else "SHORT"
        return {
            "strategy": "adx_trend_rider",
            "adx": round(adx.iloc[-1], 1),
            "plus_di": round(plus_di.iloc[-1], 1),
            "minus_di": round(minus_di.iloc[-1], 1),
            "trending": trending,
            "direction": direction if trending else "FLAT — no trend",
            "signal": f"{direction} — ADX={adx.iloc[-1]:.0f}" if trending else "NO TRADE — ADX below threshold",
        }

    @staticmethod
    def supertrend(df: pd.DataFrame, period: int = 10, multiplier: float = 3.0) -> dict:
        """Supertrend indicator strategy — popular in Indian and crypto markets."""
        hl2 = (df["high"] + df["low"]) / 2
        atr = ((df["high"] - df["low"]).rolling(period).mean())
        upper = hl2 + multiplier * atr
        lower = hl2 - multiplier * atr
        trend = pd.Series(0, index=df.index)
        for i in range(1, len(df)):
            if df["close"].iloc[i] > upper.iloc[i - 1]:
                trend.iloc[i] = 1
            elif df["close"].iloc[i] < lower.iloc[i - 1]:
                trend.iloc[i] = -1
            else:
                trend.iloc[i] = trend.iloc[i - 1]
        return {
            "strategy": f"supertrend_{period}_{multiplier}",
            "trend": "BULLISH" if trend.iloc[-1] == 1 else "BEARISH",
            "level": round(lower.iloc[-1] if trend.iloc[-1] == 1 else upper.iloc[-1], 5),
            "signal": "BUY" if trend.iloc[-1] == 1 and trend.iloc[-2] == -1 else
                     "SELL" if trend.iloc[-1] == -1 and trend.iloc[-2] == 1 else
                     f"HOLD {'LONG' if trend.iloc[-1] == 1 else 'SHORT'}",
        }

    @staticmethod
    def scan_all(df: pd.DataFrame, symbol: str = "") -> dict:
        return {
            "symbol": symbol,
            "ma_20_50": TrendFollowingSystems.ma_crossover(df, 20, 50),
            "ma_50_200": TrendFollowingSystems.ma_crossover(df, 50, 200),
            "triple_ma": TrendFollowingSystems.triple_ma(df),
            "turtle": TrendFollowingSystems.turtle_breakout(df),
            "adx_rider": TrendFollowingSystems.adx_trend_rider(df),
            "supertrend": TrendFollowingSystems.supertrend(df),
        }
```

---

### Mean Reversion Engine

CRITICAL: Only use in RANGING regimes. Mean reversion in trends = catching knives.

```python
import pandas as pd
import numpy as np

class MeanReversionEngine:

    @staticmethod
    def bollinger_bounce(df: pd.DataFrame, period: int = 20, std_mult: float = 2.0) -> dict:
        """Buy at lower band, sell at upper band. Classic range strategy."""
        close = df["close"]
        mid = close.rolling(period).mean()
        std = close.rolling(period).std()
        upper = mid + std_mult * std
        lower = mid - std_mult * std
        pct_b = (close - lower) / (upper - lower)

        current = df.iloc[-1]
        return {
            "strategy": "bollinger_bounce",
            "upper": round(upper.iloc[-1], 5),
            "middle": round(mid.iloc[-1], 5),
            "lower": round(lower.iloc[-1], 5),
            "pct_b": round(pct_b.iloc[-1], 3),
            "signal": "BUY (at lower band)" if pct_b.iloc[-1] < 0.05 else
                     "SELL (at upper band)" if pct_b.iloc[-1] > 0.95 else "WAIT",
            "target": round(mid.iloc[-1], 5),
            "stop": round(lower.iloc[-1] - (upper.iloc[-1] - lower.iloc[-1]) * 0.25, 5) if pct_b.iloc[-1] < 0.05
                   else round(upper.iloc[-1] + (upper.iloc[-1] - lower.iloc[-1]) * 0.25, 5),
        }

    @staticmethod
    def rsi_extreme_fade(df: pd.DataFrame, period: int = 14,
                         oversold: float = 25, overbought: float = 75) -> dict:
        """Fade RSI extremes with divergence confirmation."""
        close = df["close"]
        delta = close.diff()
        gain = delta.where(delta > 0, 0).rolling(period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        rsi = 100 - (100 / (1 + gain / loss.replace(0, np.nan)))

        # Divergence: price makes new low but RSI makes higher low (bullish)
        price_lower = close.iloc[-1] < close.rolling(20).min().iloc[-5]
        rsi_higher = rsi.iloc[-1] > rsi.rolling(20).min().iloc[-5]
        bull_divergence = price_lower and rsi_higher and rsi.iloc[-1] < 40

        price_higher = close.iloc[-1] > close.rolling(20).max().iloc[-5]
        rsi_lower = rsi.iloc[-1] < rsi.rolling(20).max().iloc[-5]
        bear_divergence = price_higher and rsi_lower and rsi.iloc[-1] > 60

        return {
            "strategy": "rsi_extreme_fade",
            "rsi": round(rsi.iloc[-1], 1),
            "oversold": rsi.iloc[-1] < oversold,
            "overbought": rsi.iloc[-1] > overbought,
            "bullish_divergence": bull_divergence,
            "bearish_divergence": bear_divergence,
            "signal": "BUY (oversold + divergence)" if rsi.iloc[-1] < oversold and bull_divergence
                     else "BUY (oversold)" if rsi.iloc[-1] < oversold
                     else "SELL (overbought + divergence)" if rsi.iloc[-1] > overbought and bear_divergence
                     else "SELL (overbought)" if rsi.iloc[-1] > overbought
                     else "WAIT",
            "quality": "A+" if bull_divergence or bear_divergence else "B",
        }

    @staticmethod
    def zscore_reversion(df: pd.DataFrame, lookback: int = 60,
                         entry_z: float = 2.0, exit_z: float = 0.5) -> dict:
        """Z-score based reversion with configurable thresholds."""
        close = df["close"]
        mean = close.rolling(lookback).mean()
        std = close.rolling(lookback).std()
        z = (close - mean) / std.replace(0, np.nan)

        return {
            "strategy": "zscore_reversion",
            "z_score": round(z.iloc[-1], 3),
            "mean": round(mean.iloc[-1], 5),
            "signal": "BUY (z < -2)" if z.iloc[-1] < -entry_z
                     else "SELL (z > 2)" if z.iloc[-1] > entry_z
                     else "EXIT" if abs(z.iloc[-1]) < exit_z and abs(z.iloc[-2]) > exit_z
                     else "WAIT",
            "target": round(mean.iloc[-1], 5),
            "distance_to_mean_pct": round((close.iloc[-1] / mean.iloc[-1] - 1) * 100, 2),
        }

    @staticmethod
    def scan_all(df: pd.DataFrame, symbol: str = "") -> dict:
        return {
            "symbol": symbol,
            "bollinger": MeanReversionEngine.bollinger_bounce(df),
            "rsi_fade": MeanReversionEngine.rsi_extreme_fade(df),
            "zscore": MeanReversionEngine.zscore_reversion(df),
            "WARNING": "Mean reversion ONLY works in ranging markets. Check regime first.",
        }
```

---

## Related Skills

- [Technical Indicators](../technical-analysis.md)
- [Price Action](../price-action.md)
- [Chart Vision](../chart-vision.md)
- [Ict Smart Money](../ict-smart-money.md)
- [Liquidity Analysis](../liquidity-analysis.md)


---

## Market Profile & Auction Market Theory

### Core Concept
Markets are two-sided auctions. Price seeks areas of value. When price is in the value area, it ranges. When outside, it trends back toward value or seeks a new value area.

### Key Terms
- **TPO (Time Price Opportunity):** Each letter = 30-min period at a specific price. Height of letters = time spent there.
- **POC (Point of Control):** Price with the most TPOs — strongest S/R, price magnet.
- **Value Area (VA):** Range containing 70% of day's TPOs. VAH = upper bound, VAL = lower bound.
- **Initial Balance (IB):** Price range in the first hour of trading. Determines day type.
- **Single Prints:** Areas where price passed through quickly — price tends to return to fill them.
- **Excess:** Long tail at high/low showing strong rejection — "fair" high/low.

### Day Types
| Type | IB Width | Character | Trade Approach |
|------|----------|-----------|---------------|
| Normal | Wide (>2× avg) | Range-bound | Fade extremes, mean revert to POC |
| Normal Variation | Moderate | Extends one side | Follow extension direction |
| Trend Day | Very narrow | Strong single direction | Follow trend, trail stops |
| Double Distribution | Moderate | Two value areas form | Gap between distributions = key level |
| Neutral | Moderate | Extends both sides | No clear direction, range trade |

### 80% Value Area Rule
If price opens outside VA and spends 2 TPOs outside → 80% chance of testing opposite VA boundary.

### Opening Types
1. **Open-Drive (OD):** Immediately moves away from open → follow direction
2. **Open-Test-Drive (OTD):** Tests extreme, then drives opposite → follow drive
3. **Open-Rejection-Reverse (ORR):** Drives one way, gets rejected, reverses → fade
4. **Open-Auction (OA):** Rotates around open → range trade or avoid

### Using Value Area for Targets
- VAH = resistance, VAL = support
- Breakout above VAH → target prior day's POC, then prior VAH
- Breakdown below VAL → target prior day's POC, then prior VAL
- POC = "fair price" magnet for mean reversion

### Key Level Hierarchy
1. Monthly VAH/VAL/POC (strongest)
2. Weekly VAH/VAL/POC
3. Prior day VAH/VAL/POC
4. Current day developing VA boundaries
5. Hourly/session POC (weakest)
