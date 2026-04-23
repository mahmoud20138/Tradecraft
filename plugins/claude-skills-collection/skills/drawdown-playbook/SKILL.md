---
id: drawdown-playbook
name: drawdown-playbook
description: "Drawdown taxonomy, tiered response protocols (caution to emergency), equity curve health analysis, recovery mathematics, and pre-drawdown preparation. Use for drawdown, equity curve, max drawdown, recovery protocol, drawdown management, or any drawdown-related analysis."
title: "Drawdown Playbook"
domain: trading/risk-and-portfolio
level: advanced
version: 1
depends_on: [risk-of-ruin]
unlocks: [real-time-risk-monitor, risk-of-ruin]
tags: [drawdown, recovery, equity-curve, max-dd, protocols]
status: active
created: "2025-01-15"
updated: "2025-01-15"
context_cost: medium
load_priority: 0.80
kind: reference
category: trading/risk
---
> **Skill:** Drawdown Playbook  |  **Domain:** trading/risk-and-portfolio  |  **Category:** risk  |  **Level:** advanced
> **Tags:** `drawdown`, `recovery`, `equity-curve`, `max-dd`, `protocols`

# Drawdown Playbook

## 1. Drawdown Taxonomy

### Types
| Type | Definition | Typical Cause |
|------|-----------|---------------|
| **Strategy DD** | Expected drawdown within strategy parameters | Normal variance |
| **Behavioral DD** | Drawdown from rule violations | Revenge trading, FOMO |
| **Regime DD** | Drawdown from regime change | Strategy-regime mismatch |
| **Black Swan DD** | Drawdown from extreme events | Flash crash, gap, liquidity vacuum |

### Measurement
```
Max Drawdown (MDD):
  MDD = (Peak - Trough) / Peak × 100

Average Drawdown:
  Avg of all drawdown periods in lookback window

Drawdown Duration:
  Time from peak to recovery (not just to trough)

Ulcer Index:
  UI = sqrt(mean(DD²)) — penalizes deep AND long drawdowns
```

## 2. Drawdown Thresholds & Responses

### Tiered Response Protocol
```
LEVEL 1: CAUTION (DD = 3-5% of account)
├── Review: Check if within strategy expected DD
├── Action: Reduce position size by 25%
├── Monitor: Tighten review frequency to per-trade
└── Journal: Document what's happening in market

LEVEL 2: WARNING (DD = 5-10% of account)
├── Review: Full strategy audit — is this regime change?
├── Action: Reduce position size by 50%
├── Restrict: No new strategy experiments
├── Require: Every trade needs written thesis before entry
└── Timeline: If no recovery in 10 sessions, escalate

LEVEL 3: CRITICAL (DD = 10-15% of account)
├── Action: Reduce to 1 instrument, 1 strategy, minimum size
├── Pause: No trading for 24-48 hours minimum
├── Audit: Full performance review with data
│   ├── Win rate vs historical
│   ├── Average R vs historical
│   ├── Are losses from stops or blowups?
│   └── Regime classification check
├── Require: Paper trade for 5 sessions before resuming
└── Consider: Is the strategy broken or am I broken?

LEVEL 4: EMERGENCY (DD > 15% of account)
├── Action: STOP TRADING. Full stop.
├── Close: All open positions at market
├── Duration: Minimum 1 week away from screens
├── Requirement: Complete written post-mortem before resuming
├── Review: Account sizing — is total capital at risk appropriate?
└── Return: Restart at LEVEL 1 position sizes for 20+ trades
```

## 3. Equity Curve Analysis

### Health Indicators
```
HEALTHY EQUITY CURVE:
✓ Drawdowns are shallow relative to advances
✓ Recovery time < 2× drawdown duration
✓ New equity highs every 20-40 trades
✓ Ulcer Index < 5%
✓ Consistent slope (not spike-dependent)

DETERIORATING EQUITY CURVE:
✗ Drawdowns deepening over time
✗ Time between new highs increasing
✗ Equity curve flattening (winners shrinking)
✗ Large gap between gross and net P&L (overtrading)
```

### Rolling Performance Windows
```python
def equity_health_check(trades: list[Trade], window: int = 50) -> dict:
    """Run on last N trades to detect deterioration early."""
    recent = trades[-window:]

    metrics = {
        'win_rate': len([t for t in recent if t.pnl > 0]) / len(recent),
        'avg_r': mean([t.r_multiple for t in recent]),
        'max_dd_pct': max_drawdown(recent),
        'profit_factor': sum(wins) / abs(sum(losses)),
        'expectancy': win_rate * avg_win - (1 - win_rate) * avg_loss,
        'sqn': (avg_r / std_r) * sqrt(len(recent)),  # System Quality Number
    }

    # Compare to full history
    baseline = compute_metrics(trades)

    alerts = []
    if metrics['win_rate'] < baseline['win_rate'] * 0.85:
        alerts.append('WIN_RATE_DEGRADATION')
    if metrics['avg_r'] < baseline['avg_r'] * 0.75:
        alerts.append('R_MULTIPLE_COMPRESSION')
    if metrics['max_dd_pct'] > baseline['max_dd_pct'] * 1.5:
        alerts.append('DRAWDOWN_EXPANSION')
    if metrics['sqn'] < 1.6:
        alerts.append('SYSTEM_QUALITY_LOW')

    return {'metrics': metrics, 'alerts': alerts}
```

## 4. Recovery Protocols

### Mathematical Reality of Recovery
```
Loss    Required Gain to Recover
─────   ────────────────────────
  5%    →   5.3%
 10%    →  11.1%
 15%    →  17.6%
 20%    →  25.0%
 25%    →  33.3%
 30%    →  42.9%
 50%    →  100%    ← Point of no practical return
```

### Recovery Rules
```
1. Never try to recover fast. Increasing size during drawdown accelerates ruin.
2. Recovery position size = Normal size × (1 - DD%/MaxAllowableDD%)
3. Track recovery separately. When equity returns to 95% of peak, you're "recovered."
4. Time-based recovery. After emergency stop, require N profitable paper trades before live.
```

## 5. Pre-Drawdown Preparation

### Account Structure
```
Total Capital: $X
├── Trading Account: 60-70% of X
│   ├── Active margin: ≤50% of trading account
│   └── Reserve: ≥50% as buffer
├── Opportunity Reserve: 20-30% of X
│   └── Deploy only in high-conviction setups after drawdown recovery
└── Emergency Fund: 10% of X (NEVER trade this)
```

### Pre-Commitment Device
```
Write this BEFORE you start trading, sign it, review monthly:

My maximum account drawdown is ____%
At ____% DD I reduce size by ____%
At ____% DD I stop trading for ____ days
I will not increase size during drawdown
I will not add funds to cover drawdown (throwing good money after bad)
```

## 6. Drawdown Journaling Template

```markdown
## Drawdown Event: [DATE]

**Current DD:** ___% | **Level:** 1/2/3/4
**Duration:** ___ trading days since peak
**Peak Equity:** $___  |  **Current Equity:** $___

### What happened?
- [] Normal strategy variance
- [] Regime change
- [] Rule violation
- [] Unexpected event
- [] Overtrading
- [] Position sizing error

### My mental state:
- [] Calm, following protocol
- [] Frustrated but controlled
- [] Anxious, wanting to make it back
- [] Tilted / revenge trading impulse

### Actions taken:
1. ___
2. ___
3. ___

### Review date: [DATE + 3 days]
```

---

## Related Skills

- [Risk And Portfolio](risk-and-portfolio.md)
- [Correlation Crisis](correlation-crisis.md)
- [Risk Of Ruin](risk-of-ruin.md)
- [Real-Time Risk Monitor](real-time-risk-monitor.md)
