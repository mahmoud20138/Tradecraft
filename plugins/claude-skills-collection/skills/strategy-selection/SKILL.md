---
name: strategy-selection
description: >
  Meta-skill for selecting the optimal trading strategy based on current market conditions,
  session timing, volatility regime, and asset class. Routes to the correct strategy skill.
  USE FOR: which strategy to use, what setup for this market, strategy for current conditions,
  best approach right now, market regime detection, should I scalp or swing, trending or ranging.
related_skills:
  - ict-smart-money
  - session-scalping
  - technical-analysis
  - price-action
  - trading-fundamentals
tags:
  - trading
  - strategy
  - meta
  - regime
  - session
skill_level: intermediate
kind: orchestrator
category: trading/core
status: active
---
> **Skill:** Strategy Selection  |  **Domain:** trading  |  **Category:** meta-intelligence  |  **Level:** intermediate
> **Tags:** `trading`, `strategy`, `meta`, `regime`, `session`


# Strategy Selection Framework

## Step 1: Identify Market Regime

```
TRENDING (Unbalanced):
  → Price making HH/HL (bull) or LH/LL (bear)
  → ADR > 80% of 20-day average
  → Clear displacement candles visible on 1H+
  → Volume profile: THIN shape (strong directional flow)
  → Best strategies: ICT MSS+FVG, Market Maker Models, Displacement Trap Entry

RANGING (Balanced):
  → Price oscillating between defined H/L
  → ADR < 60% of 20-day average
  → Volume profile: D-SHAPE (heavy middle, light edges)
  → Best strategies: Mean Reversion, S&D Zone Fades, Asian Range Fade

TRANSITIONING:
  → After extended trend, first signs of exhaustion
  → Volume profile: P-SHAPE (top-heavy) or B-SHAPE (bottom-heavy)
  → Best strategies: Liquidity Trap, Breaker Block entries, counter-trend CRT
```

## Step 2: Match Session to Strategy

| Session | Best Strategies | Skill File |
|---------|----------------|------------|
| Asia (00:00-07:00 UTC) | Asian Range Fade, range identification | session-scalping.md |
| London (07:00-12:00 UTC) | Judas Swing, London breakout, ORB | session-scalping.md |
| NY (13:30-17:00 UTC) | Silver Bullet, ICT 2022, Flip+Sweep | ict-smart-money.md |
| NY afternoon (17:00-20:00 UTC) | Mean Reversion, Session Sweep | session-scalping.md |
| Overlap (13:30-16:00 UTC) | Highest volatility — all trend strategies valid | ict-smart-money.md |

## Step 3: Match Asset to Approach

| Asset Class | Primary Strategy | Notes |
|-------------|-----------------|-------|
| Forex majors | ICT/SMC, dual-TF auction | Best during their session killzone |
| Gold (XAUUSDm) | Order Flow + ICT, Silver Bullet | NY session only, high volatility |
| Indices (US30/NAS/SPX) | ORB, Session Sweep, VWAP | NY open, first hour |
| Crypto (BTC/ETH) | All sessions, trend-following | 24/7 but best during NY overlap |
| Stock CFDs | Dual-TF auction, S&D zones | NY session 13:30-20:00 UTC only |

## Step 4: Confluence Check

```
Before entering ANY trade, verify:
□ Market regime identified (trending/ranging/transitioning)
□ Correct session for this strategy
□ Asset matches approach
□ HTF bias established
□ At least 2 confluences present (FVG + OB, S&D + VP, etc.)
□ Risk ≤ 1% | RR ≥ 2:1

Score < 4 confluences → SKIP
Score 4-6 → half size
Score 7+ → full size
```

## Decision Tree

```
Is market TRENDING?
├── YES → Is it YOUR session killzone?
│   ├── YES → Use ICT/SMC trend strategies (MSS+FVG, Silver Bullet, Displacement Trap)
│   └── NO → Wait for your killzone or use session-transition strategies
└── NO → Is market RANGING?
    ├── YES → Use mean-reversion strategies (S&D fade, Asian range, VWAP reversion)
    └── TRANSITIONING → Use reversal strategies (Liquidity Trap, CRT, Breaker Block)
```

---

## Related Skills

- [Ict Smart Money](../ict-smart-money.md)
- [Session Scalping](../session-scalping.md)
- [Technical Analysis](../technical-analysis.md)
- [Price Action Strategies](../price-action.md)
- [Trading Fundamentals](../trading-fundamentals.md)


---

## Universal Trading Rules (All Strategies)

1. Never risk more than 1–2% of account per trade
2. Always define stop loss BEFORE entry
3. Trade with the higher-timeframe trend when possible
4. Volume confirms breakouts — low-volume moves are suspect
5. Avoid trading into major news events unless that IS the strategy
6. Journal every trade — strategy, entry reason, result, lesson
7. Cut losses quickly; let winners run — do not move stops against position
8. Review strategy performance monthly — edge can decay
9. Check market regime first — wrong strategy in wrong regime = losses

## Strategy Evaluation Criteria
- **Expectancy** = (Win Rate × Avg Win) − (Loss Rate × Avg Loss) — must be positive
- **Sharpe Ratio** > 1.0 acceptable; > 2.0 excellent
- **Max Drawdown** < 20% for most retail strategies
- **Sample Size** minimum 100 trades for statistical significance
- **Robustness** — test on out-of-sample data (walk-forward or holdout)
- **Correlation** — avoid strategies that fail at the same time

## Quick Strategy Match by Condition
| Market Condition | Best Strategy | Avoid |
|---|---|---|
| Strong uptrend, ADX > 25 | Trend Following, Momentum | Mean Reversion |
| Downtrend, ADX > 25 | Trend Following (short) | Mean Reversion |
| Ranging, ADX < 20 | Mean Reversion, Grid | Trend Following |
| Volatility compression | Breakout (anticipate expansion) | Momentum |
| High volatility expansion | Momentum, Breakout continuation | Counter-trend |
| End of trend / divergence | PA Reversal, Mean Reversion | Trend Following |
| News catalyst | Event-Driven, Gap | Range mean reversion |
