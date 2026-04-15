---
name: trading-fundamentals
description: >
  Core trading knowledge covering market structure, order types, asset classes, timeframes,
  risk management, position sizing, trading psychology, and journaling. USE FOR: explain market
  structure, what is a market order, types of orders, limit order vs stop order, iceberg order,
  TWAP VWAP orders, asset classes, scalping vs day trading vs swing trading vs position trading,
  risk management rules, position sizing, Kelly criterion, ATR position sizing, fixed percent risk,
  risk reward ratio, drawdown management, trading psychology, trade-psychology-coach biases in trading,
  emotional management, trading journal template, how to manage risk, 1% rule trading,
  fear and greed in trading, overtrading, revenge trading.
user-invocable: false
related_skills:
  - strategy-selection
  - risk-and-portfolio
  - smc-beginner-pro-guide

tags:
  - trading
  - fundamentals
  - psychology
  - development
  - dual-tf
  - risk
skill_level: beginner
kind: reference
category: trading/core
status: active
---
# Trading Fundamentals

> **Skill:** Trading Fundamentals  |  **Domain:** trading  |  **Category:** fundamentals  |  **Level:** beginner
> **Tags:** `trading`, `fundamentals`, `psychology`, `development`, `dual-tf`, `risk`

## 1. Market Structure

### Market Types

| Market Type | Description | Examples |
|-------------|-------------|---------|
| **Exchange-Traded** | Centralized, regulated, standardized | NYSE, NASDAQ, CME, CBOE |
| **OTC (Over-the-Counter)** | Decentralized, bilateral, flexible | Forex spot, bonds, derivatives |
| **Dark Pools** | Private exchanges, minimal pre-trade transparency | Liquidnet, IEX |
| **ECN/ATS** | Electronic, direct order matching | ARCA, BATS, IEX |

### Market Participants

| Participant | Role | Typical Behavior |
| ----------- | ---- | --------------- |
| **Market Makers** | Provide liquidity, quote bid/ask | Mean-reverting, earn spread |
| **Institutional Investors** | Large funds, pension funds | Slow accumulation, trend-following |
| **Hedge Funds** | Diverse strategies, leverage | Short-term tactical, event-driven |
| **Retail Traders** | Individual accounts | Often contrarian signal (sentiment) |
| **High-Frequency Traders** | Algorithms, co-location | Latency arbitrage, market making |
| **Central Banks** | Currency intervention | Large directional moves |
| **Arbitrageurs** | Exploit price discrepancies | Keep markets efficient |

### Market Microstructure

- **Bid-Ask Spread**: Cost of immediacy; tighter = more liquid
- **Order Book Depth**: Volume at each price level; thin books = slippage
- **Price Discovery**: Process of finding fair value through supply/demand
- **Market Impact**: Price moves against your order as size increases
- **Slippage**: Difference between expected and executed price
- **Tick Size**: Minimum price increment (e.g., $0.01 stocks, 0.25 pts ES futures)
- **Lot Size**: Standard trading unit (100 shares stocks, 100,000 units forex standard lot)

---

## 2. Order Types

### Basic Orders

| Order Type | Description | When to Use | Risk |
|------------|-------------|-------------|------|
| **Market Order** | Execute immediately at best price | Need instant fill | Slippage in thin markets |
| **Limit Order** | Execute only at specified price or better | Price-sensitive entry/exit | May not fill |
| **Stop Order** | Becomes market when price reached | Stop-loss, breakout entry | Slippage at trigger |
| **Stop-Limit** | Becomes limit when stop triggered | Breakout with price control | May not fill past gap |
| **Trailing Stop** | Stop adjusts with price movement | Lock in profits on trends | Whipsaws in volatile markets |
| **MIT (Market if Touched)** | Market order when price touched | Reversal entries | Slippage |
| **GTC (Good Till Cancelled)** | Order stays until filled or cancelled | Swing trade entries | Forgotten orders |
| **FOK (Fill or Kill)** | Fill entire order or cancel | Large block trades | Frequent cancellations |
| **IOC (Immediate or Cancel)** | Fill what's available, cancel rest | Partial fills acceptable | Partial execution |

### Advanced/Algorithmic Orders

| Order Type | Description | Formula/Logic |
|------------|-------------|--------------|
| **TWAP** | Time-Weighted Average Price | Executes equal portions each time interval |
| **VWAP** | Volume-Weighted Average Price | Executes proportional to volume distribution |
| **Iceberg** | Shows only portion of total size | Total size hidden; refreshes displayed qty |
| **POV (% of Volume)** | Participate at set % of market volume | Slices = Volume × Target% |
| **Implementation Shortfall** | Minimize cost vs. arrival price | Optimizes between urgency and market impact |
| **Pegged Orders** | Price pegs to bid/ask/midpoint | Dynamic pricing with spread |

### Iceberg Order Example

Total Order: 100,000 shares
Display Quantity: 1,000 shares
→ Market sees only 1,000 at a time
→ After each fill, 1,000 more displayed
→ Used to hide large institutional interest

```

---

## 3. Asset Classes

| Asset Class | Sub-Types | Key Characteristics | Typical Instruments |
|-------------|-----------|--------------------|--------------------|
| **Equities** | Stocks, ETFs, ADRs | Ownership stake, dividends, earnings driven | AAPL, SPY, QQQ |
| **Fixed Income** | Gov bonds, Corp bonds, Munis | Interest payments, duration risk | TLT, AGG, UST |
| **Commodities** | Energy, Metals, Agri | Inflation hedge, cyclical | Gold, Oil, Corn |
| **Forex** | Major, Minor, Exotic pairs | 24/5 market, leverage, macro driven | EUR/USD, USD/JPY |
| **Derivatives** | Options, Futures, Swaps | Leverage, hedging, expiration | SPX options, ES futures |
| **Cryptocurrencies** | Layer-1, DeFi, Stablecoins | 24/7, high volatility, on-chain data | BTC, ETH, SOL |
| **Real Assets** | REITs, Infrastructure | Tangible, inflation protection | VNQ, MLP |
| **Alternative** | Hedge funds, PE, Commodities | Low correlation, illiquid | SPACs, art, wine |

### Asset Class Correlations (Typical)

- **Stocks ↔ Bonds**: Negative correlation in risk-off; breaks down in stagflation
- **USD ↑ → Gold ↓**: Usually negative (priced in USD)
- **Oil ↑ → CAD ↑**: Canada major oil exporter
- **Risk-off**: Buy USD, JPY, Gold, Treasuries; Sell EM, commodities
- **Risk-on**: Buy stocks, commodities, EM; Sell USD, bonds

---

## 4. Trading Timeframes

| Style | Holding Period | Chart TF | Trades/Day | Typical R:R | Capital Required |
|-------|---------------|----------|-----------|-------------|-----------------|
| **Scalping** | Seconds–minutes | 1s–5m | 20–100+ | 1:1–1.5:1 | High (commissions) |
| **Day Trading** | Minutes–hours | 5m–1h | 2–10 | 2:1–3:1 | $25k+ (PDT rule) |
| **Swing Trading** | Days–weeks | 4h–Daily | 3–15/month | 3:1–5:1 | $5k–$25k |
| **Position Trading** | Weeks–months | Daily–Weekly | 1–5/month | 5:1–10:1 | $10k+ |
| **Investing** | Months–years | Weekly–Monthly | Annual | N/A | Any amount |

### Multi-Timeframe Hierarchy

```

Higher TF → Determines Trend Direction (Primary Bias)
Middle TF → Confirms Setup / Pattern
Lower TF  → Precise Entry/Exit Timing

Example (Day Trader):
  HTF: Daily chart → Uptrend (above 200 EMA)
  MTF: 1h chart → Pullback to key support
  LTF: 15m chart → Bullish reversal candle for entry

```

---

## 5. Core Principles: Risk Management (10 Rules)

### Rule 1: Never Risk More Than 1-2% Per Trade

```

Account: $50,000
Max Risk/Trade: 1% = $500
If stop = 50 points at $10/point → Max 1 contract

```

### Rule 2: Define Risk BEFORE Entry

- Place stop loss before entering
- Know exact dollar risk before sizing position
- Never move stops to avoid a loss (move only to lock in profit)

### Rule 3: Use Position Sizing, Not Gut Feel

- Size = Risk Amount ÷ (Entry Price − Stop Price)
- Always calculate; never guess

### Rule 4: Maintain Positive Expected Value

```

EV = (Win Rate × Avg Win) − (Loss Rate × Avg Loss)
EV must be > 0 for long-term profitability
Example: 40% WR, $300 avg win, 60% LR, $150 avg loss
EV = (0.40 × $300) − (0.60 × $150) = $120 − $90 = +$30 per trade ✓

```

### Rule 5: Risk-Reward Minimum 2:1

- Never take a trade with R:R < 1.5:1
- Optimal: 2:1 to 3:1 for most strategies
- Allows profitability at 40% win rate: (0.40 × 2) − (0.60 × 1) = +0.20R

### Rule 6: Correlation Risk Management

- Don't hold multiple correlated positions at full size
- If 3 long tech stocks: effective risk = 3× single position risk
- Limit correlated sector exposure to 5–6% of capital

### Rule 7: Drawdown Limits

- Daily loss limit: 3% of account → Stop trading for the day
- Weekly loss limit: 6% → Reduce size by 50% next week
- Monthly loss limit: 10% → Full review before continuing
- Account drawdown: >20% → Stop, assess, fix before continuing

### Rule 8: Scale In, Scale Out

- Enter in 2–3 tranches to average better price
- Exit in 2–3 tranches to lock profits while running winners
- Never add to a losing position ("averaging down" = dangerous)

### Rule 9: Keep a Trading Journal

- Record every trade with: entry/exit, rationale, emotion, result
- Review weekly for patterns and improvement areas

### Rule 10: Protect Capital First, Make Profits Second

- Goal #1: Survive to trade another day
- Goal #2: Consistent small gains compound to large gains

---

## 6. Position Sizing Formulas

### Method 1: Fixed Percentage Risk (Most Common)

```

Position Size = (Account × Risk%) ÷ |Entry − Stop|

Example:
  Account = $100,000
  Risk% = 1% → $1,000 risk
  Entry = $50.00, Stop = $48.00 → $2.00 risk/share
  Position Size = $1,000 ÷ $2.00 = 500 shares
  Position Value = 500 × $50 = $25,000 (25% of account)

```

### Method 2: Kelly Criterion

```

f* = (bp − q) ÷ b

Where:
  b = average win / average loss ratio
  p = probability of win (win rate)
  q = 1 − p (probability of loss)

Example:
  Win Rate = 55%, Avg Win = $300, Avg Loss = $150
  b = 300/150 = 2.0
  f* = (2.0 × 0.55 − 0.45) ÷ 2.0 = (1.10 − 0.45) ÷ 2.0 = 0.325 = 32.5%

⚠️ Full Kelly is too aggressive! Use Half-Kelly (16.25%) or Quarter-Kelly (8.1%)

```

### Method 3: ATR-Based Position Sizing

```

Position Size = (Account × Risk%) ÷ (ATR × Multiplier)

Example:
  Account = $100,000, Risk% = 1%
  ATR(14) = $3.50 on a $75 stock
  Multiplier = 2× ATR for stop distance
  Stop Distance = 2 × $3.50 = $7.00
  Position Size = $1,000 ÷ $7.00 = 142 shares

```

### Method 4: Volatility-Adjusted (Equal Volatility)

```

Position Size = Target Volatility / (Price × Daily Vol %)
Target each position to contribute equal volatility to portfolio
Used in risk parity and institutional portfolios

```

### Risk-Reward Analysis Table

| Win Rate | Min R:R Required for Breakeven |
|----------|-------------------------------|
| 30% | 2.33:1 |
| 40% | 1.50:1 |
| 50% | 1.00:1 |
| 60% | 0.67:1 |
| 70% | 0.43:1 |

---

## 7. Drawdown Management

### Drawdown Calculations

```

Max Drawdown = (Peak Value − Trough Value) ÷ Peak Value × 100

Recovery Required from Drawdown:
  10% loss → Need 11.1% gain to recover
  20% loss → Need 25.0% gain to recover
  30% loss → Need 42.9% gain to recover
  40% loss → Need 66.7% gain to recover
  50% loss → Need 100.0% gain to recover

```

### Drawdown Response Protocol

| Drawdown Level | Action |
|---------------|--------|
| 5% | Review recent trades, check for pattern errors |
| 10% | Reduce position size by 25%, increase selectivity |
| 15% | Reduce size by 50%, review strategy validity |
| 20% | Stop trading, full strategy audit, paper trade |
| 25%+ | Complete reset: new strategy or long break |

---

## 8. Trading Psychology: 12 Cognitive Biases

### Bias 1: Confirmation Bias

- **What**: Seek information that confirms existing view
- **Example**: Only reading bullish articles on a stock you own
- **Counter**: Actively seek bearish arguments; read the bear thesis

### Bias 2: Recency Bias

- **What**: Overweight recent events, underweight long-term data
- **Example**: After 3 winning trades, expect #4 to win too
- **Counter**: Review at least 100+ trade sample; use statistics

### Bias 3: Loss Aversion

- **What**: Pain of losing 2× stronger than joy of equal gain
- **Example**: Hold losers too long, cut winners too early
- **Counter**: Pre-define exits; use trailing stops; separate emotions from trades

### Bias 4: Overconfidence Bias

- **What**: Overestimate skill, underestimate luck
- **Example**: Attribute wins to skill, losses to bad luck
- **Counter**: Track edge-adjusted returns; keep win/loss attribution log

### Bias 5: Anchoring Bias

- **What**: Over-rely on first piece of information seen
- **Example**: "Stock was at $100, now $60, must be cheap"
- **Counter**: Value from fundamentals/technicals, not reference prices

### Bias 6: Gambler's Fallacy

- **What**: Believe past events affect independent future events
- **Example**: After 5 losses, feel "due for a win"
- **Counter**: Each trade is independent; law of large numbers applies, not sequences

### Bias 7: Herding Bias

- **What**: Follow the crowd, seek social validation
- **Example**: Buying because "everyone on Twitter is bullish"
- **Counter**: Trade your own plan; use contrary indicators for positioning

### Bias 8: Status Quo Bias

- **What**: Prefer current state, resist change
- **Example**: Hold losing position hoping it "comes back"
- **Counter**: Ask "would I enter this trade fresh today?" If no → exit

### Bias 9: Disposition Effect

- **What**: Sell winners too early, hold losers too long (tax + psychology)
- **Example**: Sell at 10% profit but hold 30% losers
- **Counter**: Use trailing stops; evaluate positions on forward-looking merit only

### Bias 10: Narrative Fallacy

- **What**: Create coherent stories for random events
- **Example**: "Oil rose because traders worried about Middle East"
- **Counter**: Focus on price action and data; be skeptical of explanations

### Bias 11: Sunk Cost Fallacy

- **What**: Continue because of past investment, not future value
- **Example**: "I'm already down $5,000, I'll hold to get back to even"
- **Counter**: Sunk costs are irrelevant; decide based on future expected value

### Bias 12: FOMO (Fear of Missing Out)

- **What**: Chase trades already in motion due to fear of missing profits
- **Example**: Buying breakout 5% above your planned entry
- **Counter**: There's always another trade; define entry rules strictly

---

## 9. Emotional Management Framework

### The STOP Technique (In-Trade)

```

S → Stop: Pause before acting impulsively
T → Think: What does my system say to do?
O → Observe: Am I emotional or rational right now?
P → Proceed: Only act according to pre-defined rules

```

### Pre-Trade Checklist (Mental State)

- [] Am I well-rested? (Sleep < 6h → reduce size or don't trade)
- [] Am I emotionally neutral? (Not angry, depressed, or euphoric)
- [] Did I review my plan? (Know entry, stop, target before touching keyboard)
- [] Am I trading my system? (Not revenge trading or FOMO)
- [] Is account within normal drawdown? (Not tilting)

### States That Degrade Performance

| State | Risk | Action |
|-------|------|--------|
| Euphoric (after big win) | Oversize next trade | Reduce size 50% |
| Angry (after loss) | Revenge trade | Stop for the day |
| Tired | Slow reactions, poor judgment | Don't trade |
| Anxious | Exit too early | Reduce position size |
| Bored | Force trades | Find another activity |

---

## 10. Trading Journal Template

### Trade Entry Fields

```yaml
Trade #: [Sequential number]
Date/Time: [Entry timestamp]
Instrument: [Symbol/Asset]
Direction: [Long/Short]
Setup Name: [e.g., "Bullish Engulfing at Support"]
Timeframe: [Primary chart TF]

Entry Price: $___
Stop Loss: $___     Stop Distance: $___ (___%)
Target 1: $___      R:R to T1: ___:1
Target 2: $___      R:R to T2: ___:1
Position Size: ___ shares/contracts
Dollar Risk: $___   % Account Risk: ___%

Pre-Trade Reasoning:
  Trend: [Higher TF trend direction]
  Pattern: [Technical setup identified]
  Confluence: [Supporting factors]
  Trigger: [Exact entry trigger]
  
Emotional State (1-10): ___
Conviction Level (1-10): ___
```

### Trade Exit Fields

```yaml
Exit Price: $___
Exit Date/Time: [Exit timestamp]
Hold Duration: ___
P&L: $___  (___R)

Exit Reason: [Stop/Target/Manual/Time]
Exit Rating (1-10): ___

Post-Trade Review:
  What worked: ___
  What failed: ___
  Emotional grade: ___
  Would I take this trade again? [Yes/No]
  Lesson learned: ___
```

### Weekly Review Template

```
Week of: ___
Total Trades: ___
Winners: ___ (___%)  Losers: ___ (___%)

Gross P&L: $___
Avg Win: $___   Avg Loss: $___
Profit Factor: ___  (Gross Wins ÷ Gross Losses; target > 1.5)
Max Win: $___   Max Loss: $___
Max Drawdown: $___

Best Trade: ___ (Why it worked)
Worst Trade: ___ (What to change)
Main Lesson: ___
Next Week Focus: ___
```

---

## 11. Trader Development Framework — 5 Stages
>
> Source: Umar Ashraf — $55M+ career earnings, TradeZella founder, 12 years experience

### Pre-Journey Truths (Accept Before Starting)

```
1. Trading is not easy — accepting difficulty prevents surprise/frustration
2. Money is NOT the goal — chase process, money is byproduct
3. Control only what you can control — risk, trade selection, emotions, rules
4. No permanent "aha moment" — consistent process, forever adjusted
5. Psychology is overrated in early stages — if emotions are a problem at
   stage 1-2, your SIZE is too large, not your psychology
6. Trading is a marathon — rushing = boom-bust cycle
```

### Stage 1: Novice (2-4 weeks)

```
Goal: Build foundation, establish process
- Pick ONE market, ONE session, ONE style (don't diversify yet)
- Paper trade first if new, then real money with minimal capital ($1-3K)
- Risk: <1% per account (0.5% better). Risk $10 on $1K account.
- Max 3 trades/day
- End trading by 11-12am ET max
- Be at desk 1 hour before market open

Process framework:
  1. Pre-market game plan (events, levels, bias, inflection points)
  2. Live trading notes (15-minute check-ins, write thoughts while trading)
  3. Post-market analysis (compare plan vs actual execution)

Education balance: Videos/books start high, screen time medium;
  over time video goes down, screen time goes up
```

### Stage 2: Developing (2-3 months)

```
Goal: Build playbooks with conceptual WHY
- Build playbooks — understand WHY patterns work, not just shapes
- Example "Morning Top" playbook:
  → Gap down from previous close
  → First 5min to 1h window
  → Upside move with NO follow-through (low volume, weak tape)
  → Activity slows / selling pressure appears
  → Short at key level rejection

- Back-test extensively: 3 years, 50+ instances, document each
- Track everything in R-multiple (not dollars): Lost 1R, made 2R, etc.
- Track: stop effectiveness, drawdown speed, entry/exit timing,
  best/worst trade times, rule compliance rate
- Weekly reviews mandatory
- Goals are skill-based: "Improve R-multiple" not "make $X"
```

### Stage 3: Intermediate / Optimization (2-6 months)

```
Goal: Identify and fix problems systematically
- By now: data proves your biggest problems
- Problem-solving cycle:
  Identify → Understand deeply → Create solution → Track → Fixed
- Common problems: bias blocking flexibility, cutting profits early,
  oversizing, rushing second trade after win
- Correlating factors matter: bad sleep → emotional decisions → oversizing
- Playbooks should be established and back-tested by now
- Still NOT focused on money — money starts appearing as byproduct
```

### Stage 4: Advanced / Sizing Up (6 months - 2+ years)

```
Goal: Dynamic risk management, emotions at scale
THIS is where emotions actually matter (not stages 1-3)

Dynamic risk rules:
  → Size up 20-30% increments only (not 10x jumps)
  → 1-2 max increased-risk trades per MONTH (special card)
  → Stay at new risk level 2 months before next increase
  → If in drawdown: DO NOT size up
  → After a big win: size DOWN on second trade
  → Volatile/uncertain market = conservative sizing

Confidence trap:
  After wins → confidence rises → every trade looks good →
  take bad trades → lose. Reset: walk away, journal, take time off.
```

### Stage 5: Pro / Expert

```
NOT permanent — oscillate between 4 and 5 while sizing up
- Max risk defined, average risk defined (e.g., max 10K, avg 5K)
- 3-5 proven setups mastered
- Repeatable process that survives market regime changes
- Key feeling: "I can do this again" — process confidence, not aha moment
- Even at stage 5, revisit stage 1 basics when market shifts
- Took Umar ~8 years to reach stage 5
```

### R-Multiple Tracking System

```
All P&L tracked in R (risk units), not dollars:
  Won 2R = made 2x your risk | Lost 1R = lost your risk amount

Metrics to track:
  - Win rate per playbook
  - R-multiple distribution (are you losing > -1R?)
  - Stop loss effectiveness (hit stop then reverse?)
  - Entry timing (early/late/on time)
  - Exit timing (early/late/on target)
  - Drawdown speed and recovery speed
  - Best/worst trade hours
  - Rule compliance rate
  - Playbook-specific performance

Review cadence: Daily recaps + Weekly reviews + Monthly reviews
```

---

## 12. Dual Time-Frame Auction Retest System
>
> Source: Rajan Dhall — DND Capital founder, CFTE/STA qualified, taught at London School of Economics

### Framework

```
Anchor chart: Daily (determines bias)
Execution chart: 5-minute (takes trades)
NO intermediate timeframes — intentionally skips everything between
  Daily and 5M to avoid conflicting signals and preserve gap info
```

### Moving Average Alignment Rule

```
Daily: 50 MA (macro trend) or 21 MA (day trading)
5-minute: 21 MA (intraday)

ONLY trade when BOTH timeframes show price on same side of MA:
  Above both MAs = LONGS only
  Below both MAs = SHORTS only
Both charts must show similar 45° angle structure ("look like each other")
```

### Auction Area Concept

```
Derived from Market Profile theory (price discovery / value areas)
Auction area = zone of congestion where price spent most time
Yesterday's candle body provides auction context for today
Gap levels and opening price create key S/R zones
```

### Entry Rules

```
1. Wait for price to retest the auction area (congestion zone) from the right side
2. Look for 2-candle break pattern at the auction retest:
   - Down candle breaks low of up candle = short signal (and vice versa)
3. Minimum 2:1 risk-to-reward on every trade
4. SL: above/below the candle structure high/low at the auction area
```

### Trade Management

```
- 1 trade per day (data shows 3+ per day underperforms)
- Trade duration: 4-9 minutes average
- First hour of session only (highest volatility + best execution)
- Static risk every day (not dynamic) — compound by increasing base
  after building 20 trades of "casino money" profit
- Moving SL to breakeven at 1.75:1 is viable for candle-breaker entries
  but NOT for gap trades during high-volatility environments
```

### The "Marta Method" Variation

```
Same entry as above but drops to 1-minute chart for exit:
  - Holds until 1M reversal candle pattern appears
  - Achieves 5-6:1 R:R vs standard 2:1
  - Requires more composure / micromanagement skill
```

### Market Selection Insight

```
Best: Individual stocks (TSLA, AAPL, GOOG, NVDA) — $3-10 daily ranges
Good: DAX futures (50c stop, €1 target)
Avoid: FX (too efficient, two-way flow = 4 variables vs 2, spread costs kill edge)
Key: Stocks have no negative economic consequence from going up (unlike currencies)

Fractal: Same logic applies on Monthly+Daily (swing) or Weekly+Daily instead of Daily+5M
```

---

## Related Skills

- [Strategy Selection](../strategy-selection.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
- [Smc Beginner Pro Guide](../smc-beginner-pro-guide.md)
- [Market Microstructure](../market-microstructure.md)
