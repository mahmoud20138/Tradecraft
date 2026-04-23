---
name: multi-strategy-orchestration
description: >
  Pipeline for running multiple trading strategies simultaneously. Signal arbitration,
  conflict resolution, capital allocation per strategy, risk aggregation, and regime
  switchover logic. The brain that coordinates all strategy agents.
  USE FOR: multi-strategy, strategy orchestration, signal conflict, strategy pipeline,
  run multiple strategies, strategy coordination, risk aggregation, portfolio heat,
  regime switchover, strategy agent, trading pipeline, strategy conflict resolution,
  how to combine strategies, which strategy wins, signal weighting.
related_skills:
  - portfolio-optimization
  - strategy-selection
  - market-regime-classifier
  - risk-and-portfolio
  - trading-brain
tags:
  - trading
  - orchestration
  - strategy
  - pipeline
  - risk
  - meta
skill_level: expert
kind: orchestrator
category: trading/portfolio
status: active
---
> **Skill:** Multi Strategy Orchestration  |  **Domain:** trading  |  **Category:** meta-intelligence  |  **Level:** expert
> **Tags:** `trading`, `orchestration`, `strategy`, `pipeline`, `risk`, `meta`


# Multi-Strategy Orchestration

> The command layer: regime detection → strategy selection → allocation → **this file** → execution
> For strategy weights → see `portfolio-optimization.md`
> For execution mechanics → see `trading-brain.md`

## Orchestration Pipeline

```
┌─────────────────────────────────────────────────────────┐
│                   ORCHESTRATION PIPELINE                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. REGIME DETECTION                                    │
│     market-regime-classifier.md                          │
│     → Output: TRENDING | RANGING | TRANSITIONING | VOL  │
│                                                         │
│  2. STRATEGY SELECTION                                  │
│     strategy-selection.md                               │
│     → Output: Active strategy set for current regime    │
│                                                         │
│  3. PORTFOLIO ALLOCATION                                │
│     portfolio-optimization.md                    │
│     → Output: Weight per strategy, max positions        │
│                                                         │
│  4. SIGNAL GENERATION (parallel)                        │
│     Each active strategy scans independently:           │
│     ├── ICT MSS+FVG scanner                            │
│     ├── ORB detector                                    │
│     ├── S&D zone fade scanner                          │
│     └── Liquidity trap scanner                         │
│     → Output: Raw signals with confluence scores        │
│                                                         │
│  5. SIGNAL ARBITRATION ← THIS FILE                      │
│     Resolve conflicts, rank, filter                     │
│     → Output: Approved trade list                       │
│                                                         │
│  6. RISK CHECK                                          │
│     risk-and-portfolio.md                               │
│     → Output: Position sizes, heat check                │
│                                                         │
│  7. EXECUTION                                           │
│     execute_trades.py                                   │
│     → Output: Open positions                            │
│                                                         │
│  8. MONITORING & REBALANCE (loop)                       │
│     → Regime change? → Back to step 1                   │
│     → Drawdown threshold? → Scale down                  │
│     → Session change? → Adjust weights                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Signal Arbitration

### When Strategies Agree (Confluence)

```
Multiple strategies signal SAME direction on SAME instrument:
  → STRONGEST setup — increase conviction

Scoring:
  1 strategy agrees:  Base signal (normal size)
  2 strategies agree: +25% confidence (can increase to 1.25% risk)
  3+ strategies agree: +50% confidence (can increase to 1.5% risk)

Example:
  ICT MSS+FVG signals LONG XAUUSDm  (confluence: 7/10)
  ORB signals LONG XAUUSDm           (confluence: 5/10)
  S&D zone supports LONG XAUUSDm     (zone tested)
  → 3 strategies agree → 1.5% risk, highest priority entry
```

### When Strategies Conflict (Opposing Signals)

```
Two strategies signal OPPOSITE direction on SAME instrument:

Resolution rules (in priority order):

1. HTF WINS: Strategy aligned with daily/4H trend takes priority
   → If daily bullish + ICT signals long + ORB signals short
   → Take the ICT long, ignore ORB short

2. HIGHER CONFLUENCE WINS: Compare confluence scores
   → If S&D fade: 8/10 vs ICT trend: 5/10
   → Take S&D fade (but at half size due to conflict)

3. HIGHER TIMEFRAME STRATEGY WINS: 4H signal > 1H signal > M5 signal
   → If 4H OB signals long + M5 ORB signals short
   → Take 4H OB long

4. IF TRULY EQUAL: NO TRADE on that instrument
   → Conflicting signals = market indecision
   → Move to next instrument with clearer signal

NEVER take both sides of a conflict simultaneously.
```

### Signal Priority Ranking

```
When multiple valid signals across different instruments:

Priority 1: Multi-strategy confluence (3+ strategies agree)
Priority 2: HTF-aligned + high confluence (7+/10)
Priority 3: Killzone-aligned signals (correct session)
Priority 4: Single strategy, high confluence (7+/10)
Priority 5: Single strategy, moderate confluence (4-6/10)

Execute in priority order until:
  - Max position count reached (from allocation table)
  - Portfolio heat limit reached (from risk rules)
  - No more valid signals above confluence threshold
```

## Capital Allocation Per Strategy

### Equity Bucketing Model

```
Total trading equity: 100%
├── Strategy A (ICT trend):    40% of equity → max 2 positions × 1%
├── Strategy B (ORB):          20% of equity → max 1 position × 1%
├── Strategy C (S&D fade):     20% of equity → max 2 positions × 0.5%
├── Strategy D (liquidity trap):20% of equity → max 1 position × 0.5%
└── Reserve:                    0% (fully allocated when regime clear)

Per-strategy equity is a SOFT LIMIT:
  - Strategy can exceed allocation by 25% if confluence > 8/10
  - Strategy must reduce to 0% if regime changes away from it
  - Reserve builds to 20-40% during VOLATILE regime (cash is a position)
```

### Kelly-Adjusted Strategy Sizing

```
For each strategy, calculate optimal fraction:

Kelly % = (Win Rate × Avg Win) - (Loss Rate × Avg Loss)
          ───────────────────────────────────────────────
                         Avg Win

Half-Kelly (conservative):
  Strategy       | WR   | Avg W | Avg L | Kelly | Half-K | Max Risk
  ────────────────┼──────┼───────┼───────┼───────┼────────┼─────────
  ICT MSS+FVG    | 55%  | 2.5R  | 1.0R  | 19.5% | 9.75%  | 1.0%
  ORB Break/Rest | 60%  | 2.0R  | 1.0R  | 20.0% | 10.0%  | 1.0%
  S&D Zone Fade  | 65%  | 1.5R  | 1.0R  | 21.7% | 10.8%  | 0.75%
  Liquidity Trap | 50%  | 3.0R  | 1.0R  | 16.7% | 8.3%   | 0.75%

Cap at 1% regardless of Kelly — protect against overfitting.
```

## Risk Aggregation

### Portfolio Heat Dashboard

```
┌─────────────────────────────────────────────────┐
│              PORTFOLIO HEAT CHECK                │
├─────────────────────────────────────────────────┤
│ Strategy        │ Positions │ Risk Each │ Heat   │
│─────────────────┼───────────┼───────────┼────────│
│ ICT MSS+FVG     │    2      │   1.0%    │  2.0%  │
│ ORB NY           │    1      │   1.0%    │  1.0%  │
│ S&D Fade         │    1      │   0.5%    │  0.5%  │
│ Liquidity Trap   │    0      │    —      │  0.0%  │
├─────────────────┼───────────┼───────────┼────────│
│ TOTAL           │    4      │           │  3.5%  │
├─────────────────────────────────────────────────┤
│ Max heat: 6% (trending) │ Status: ✅ UNDER LIMIT │
│ Correlated heat: 2.0% (2 gold positions)        │
│ Corr limit: 3% │ Status: ✅ UNDER LIMIT          │
└─────────────────────────────────────────────────┘
```

### Heat Limits by Regime

```
Regime         | Max Total Heat | Max Per Strategy | Max Correlated
───────────────┼────────────────┼──────────────────┼───────────────
TRENDING       |      6%        |       3%         |      3%
RANGING        |      4%        |       2%         |      2%
TRANSITIONING  |      3%        |       1.5%       |      1.5%
VOLATILE       |      1%        |       1%         |      1%
```

## Regime Switchover Logic

### Detection → Action Timeline

```
Regime change detected (e.g., TRENDING → RANGING):

T+0 min:  DETECT — VP shape changed, ATR dropped below threshold
T+0 min:  FREEZE — No new entries from old regime strategies
T+5 min:  ASSESS — Are existing positions still valid?
            ├── Position WITH new regime → KEEP (adjust SL/TP)
            └── Position AGAINST new regime → CLOSE or TIGHTEN
T+10 min: SWITCH — New strategy allocation active
T+15 min: SCAN — New regime strategies begin scanning for signals
T+30 min: EXECUTE — First entries under new regime allocation

Total switchover time: ~30 minutes
During switchover: maximum 2% portfolio heat (protective)
```

### Regime Confidence Scoring

```
Don't switch on weak signals. Require confirmation:

Confidence Score (0-10):
  +2  VP shape confirms new regime
  +2  ATR confirms (above/below 20-day avg)
  +2  Price structure confirms (HH/HL or LH/LL established)
  +2  Cumulative delta confirms
  +1  Session timing supports (London open often triggers transitions)
  +1  News catalyst present (fundamental driver for regime change)

Score 7+ → CONFIRMED regime change → full switchover
Score 4-6 → POSSIBLE change → reduce allocation 50%, wait for confirmation
Score <4 → NOISE → maintain current regime allocation
```

## Conflict Resolution Matrix

```
Scenario                          | Resolution
──────────────────────────────────┼───────────────────────────────────
Same signal, same instrument      | Combine → highest confluence entry
Opposing signals, same instrument | HTF wins, or skip if truly equal
Same signal, correlated pairs     | Take strongest setup only
Opposing signals, correlated pairs| Take neither — market unclear
Strategy says trade, regime says no| Regime overrides strategy always
Multiple instruments, limited heat| Rank by priority, fill top-down
News event approaching            | Freeze all signals until T+30 min
Drawdown >4% active               | Half all allocations immediately
```

## Monitoring Loop

```python
# Conceptual orchestration loop (runs every 5 min during session)

def orchestration_loop():
    # 1. Check regime
    regime = detect_regime()  # TRENDING | RANGING | TRANSITIONING | VOLATILE

    # 2. Get active strategies for regime
    strategies = select_strategies(regime)

    # 3. Get allocation weights
    weights = get_allocation(regime, current_session(), current_drawdown())

    # 4. Generate signals (parallel)
    signals = []
    for strategy in strategies:
        sigs = strategy.scan(watched_symbols)
        signals.extend(sigs)

    # 5. Arbitrate conflicts
    approved = arbitrate_signals(signals, weights)

    # 6. Risk check
    approved = risk_filter(approved, current_positions(), heat_limits[regime])

    # 7. Execute approved signals
    for signal in approved:
        execute_trade(signal)

    # 8. Monitor existing positions
    for position in current_positions():
        if not valid_for_regime(position, regime):
            tighten_or_close(position)
```

## Strategy Performance Tracking

```
Track per-strategy metrics to adjust future allocation:

Weekly Review:
  Strategy       | Trades | WR    | Avg R  | Total R | Sharpe
  ────────────────┼────────┼───────┼────────┼─────────┼───────
  ICT MSS+FVG    |   8    | 62%   | +1.8R  | +6.4R   | 2.1
  ORB             |   5    | 60%   | +1.5R  | +3.0R   | 1.8
  S&D Fade        |   6    | 67%   | +1.2R  | +2.4R   | 1.6
  Liquidity Trap  |   3    | 33%   | +2.5R  | -0.5R   | 0.3

Action: If strategy Sharpe < 1.0 for 2 consecutive weeks:
  → Reduce allocation by 50%
  → Review: is the strategy broken, or is regime wrong for it?
  → If regime-appropriate but still underperforming → bench for 1 week
```

---

## Related Skills

- [Portfolio Strategy Allocation](../portfolio-optimization.md)
- [Strategy Selection](../strategy-selection.md)
- [Market Regime Detection](../market-regime-classifier.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
- [Trading Brain Orchestrator](../trading-brain.md)
