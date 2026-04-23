---
id: risk-of-ruin
name: risk-of-ruin
description: "Risk of Ruin formula, Kelly Criterion (full and fractional), Monte Carlo survival simulation, and position sizing models (fixed fractional, volatility-adjusted, fixed ratio). Use for risk of ruin, Kelly criterion, Monte Carlo, position sizing, bankroll management, or any ruin/sizing calculation."
title: "Risk of Ruin & Bankroll Mathematics"
domain: trading/risk-and-portfolio
level: advanced
version: 1
depends_on: [risk-of-ruin, drawdown-playbook]
unlocks: [portfolio-optimization]
tags: [ruin, kelly, monte-carlo, bankroll, survival, sizing]
status: active
created: "2025-01-15"
updated: "2025-01-15"
context_cost: medium
load_priority: 0.70
kind: reference
category: trading/risk
---
> **Skill:** Risk of Ruin & Bankroll Mathematics  |  **Domain:** trading/risk-and-portfolio  |  **Category:** risk  |  **Level:** advanced
> **Tags:** `ruin`, `kelly`, `monte-carlo`, `bankroll`, `survival`, `sizing`

# Risk of Ruin & Bankroll Mathematics

## 1. Risk of Ruin Formula

### Classical Formula
```
For a system with:

Win rate: W
Loss rate: L = 1 - W
Win/Loss ratio: R = avg_win / avg_loss
Risk per trade: f (fraction of bankroll)

Risk of Ruin = ((1 - Edge) / (1 + Edge))^(Capital_Units)

Where:
  Edge = W × R - L = W × R - (1 - W)
  Capital_Units = Account / Risk_Per_Trade
```

### Practical Table
```
Win Rate: 55% | Win/Loss Ratio: 1.5:1 | Edge = 0.55×1.5 - 0.45 = 0.375

Risk/Trade  Risk of Ruin  Account Units
──────────  ────────────  ─────────────
    1%        0.001%       100 units
    2%        0.1%          50 units
    3%        1.2%          33 units
    5%       12.4%          20 units
   10%       52.1%          10 units
   20%       89.3%           5 units

Win Rate: 45% | Win/Loss Ratio: 2.0:1 | Edge = 0.45×2.0 - 0.55 = 0.35

Risk/Trade  Risk of Ruin
──────────  ────────────
    1%        0.01%
    2%        0.3%
    5%       18.7%
   10%       61.2%
```

**Key insight:** Even with a positive edge, risking >5% per trade gives unacceptable ruin probability.

## 2. Kelly Criterion

### Full Kelly
```
f* = (W × R - L) / R = Edge / R

Where:
  f* = optimal fraction of bankroll to risk
  W = win probability
  R = win/loss ratio
  L = 1 - W

Example:
  W = 55%, R = 1.5
  f* = (0.55 × 1.5 - 0.45) / 1.5
  f* = 0.375 / 1.5
  f* = 25% ← Full Kelly
```

### Why Full Kelly Is Dangerous
```
Full Kelly:
  ✓ Maximizes long-term growth rate
  ✗ Produces stomach-churning drawdowns (50-85% is normal)
  ✗ Assumes known exact edge (you don't know this)
  ✗ Assumes infinite time horizon
  ✗ One estimation error can be fatal

RULE: Use fractional Kelly

Half Kelly (f*/2):
  75% of the growth rate of full Kelly
  Dramatically lower drawdowns
  Much more robust to edge estimation errors

Quarter Kelly (f*/4):
  50% of growth rate
  Very smooth equity curve
  Recommended for uncertain edge
```

### Practical Kelly Sizing
```python
def kelly_size(win_rate: float, avg_win: float, avg_loss: float,
               kelly_fraction: float = 0.25) -> float:
    """
    Quarter Kelly by default. Never go above half Kelly.

    Returns: fraction of account to risk per trade
    """
    R = avg_win / abs(avg_loss)
    edge = win_rate * R - (1 - win_rate)

    if edge <= 0:
        return 0.0  # No edge = no trade

    full_kelly = edge / R
    return full_kelly * kelly_fraction

# Example:
# kelly_size(0.55, 150, 100, kelly_fraction=0.25)
# → Full Kelly = 25%, Quarter Kelly = 6.25%
# → Risk 6.25% of account per trade
#
# But cap at 2% maximum regardless of Kelly output
```

## 3. Monte Carlo Survival Analysis

### Simulation Framework
```python
import numpy as np

def monte_carlo_survival(
    win_rate: float,
    avg_win_r: float,      # in R-multiples
    avg_loss_r: float,     # typically -1R
    risk_per_trade: float, # fraction of current bankroll
    num_trades: int = 500,
    num_sims: int = 10000,
    ruin_threshold: float = 0.5,  # 50% drawdown = ruin
) -> dict:
    """
    Simulate N trading paths and measure survival.
    """
    ruin_count = 0
    max_dds = []
    final_balances = []

    for _ in range(num_sims):
        balance = 1.0  # normalized
        peak = 1.0
        max_dd = 0.0
        ruined = False

        for _ in range(num_trades):
            if np.random.random() < win_rate:
                pnl = balance * risk_per_trade * avg_win_r
            else:
                pnl = balance * risk_per_trade * avg_loss_r

            balance += pnl
            peak = max(peak, balance)
            dd = (peak - balance) / peak
            max_dd = max(max_dd, dd)

            if balance <= (1.0 - ruin_threshold):
                ruined = True
                ruin_count += 1
                break

        max_dds.append(max_dd)
        final_balances.append(balance)

    return {
        'ruin_probability': ruin_count / num_sims,
        'median_max_dd': np.median(max_dds),
        'p95_max_dd': np.percentile(max_dds, 95),
        'median_final_balance': np.median(final_balances),
        'p5_final_balance': np.percentile(final_balances, 5),
        'p95_final_balance': np.percentile(final_balances, 95),
    }

# Run with YOUR actual stats:
# result = monte_carlo_survival(
#     win_rate=0.52, avg_win_r=1.8, avg_loss_r=-1.0,
#     risk_per_trade=0.02, num_trades=500
# )
```

### Interpreting Results
```
ACCEPTABLE:
  Ruin probability: < 1%
  P95 max drawdown: < 30%
  P5 final balance: > starting balance
  Median final balance: significantly above starting

WARNING:
  Ruin probability: 1-5%
  P95 max drawdown: 30-50%
  → Reduce risk_per_trade

UNACCEPTABLE:
  Ruin probability: > 5%
  → System is not viable at this risk level
  → Either improve edge or reduce risk until ruin < 1%
```

## 4. Position Sizing Models

### Fixed Fractional
```
Risk per trade = Account × Fixed_Percent

Pro: Simple, anti-martingale (bet less after losses)
Con: Can be slow to grow small accounts
Best for: Most traders, most of the time
Typical: 1-2% per trade
```

### Volatility-Adjusted (ATR-Based)
```
Position Size = (Account × Risk%) / (ATR × ATR_Multiple)

Pro: Automatically adjusts for market volatility
Con: Requires reliable ATR calculation
Best for: Multi-instrument portfolios

Example:
  Account: $100,000
  Risk: 1% = $1,000
  EURUSD ATR(14): 80 pips
  ATR Multiple: 2 (stop at 2× ATR = 160 pips)
  Position: $1,000 / 160 pips = 6.25 per pip ≈ 0.6 lots
```

### Fixed Ratio (Ryan Jones)
```
Next level increase when: Profits ≥ Delta × Current_Units

Delta = chosen profit threshold per unit increase
Lower delta = more aggressive scaling
Higher delta = more conservative scaling

Pro: Geometric growth potential
Con: Complex, requires tracking
Best for: Scaling up proven strategies
```

## 5. Survival Rules

```
1. NEVER risk more than 2% per trade. Period.

2. NEVER have more than 6% total open risk.
   (3 positions × 2% each, or 6 × 1%)

3. DAILY loss limit: 4% of account.
   Hit it → done for the day. No exceptions.

4. WEEKLY loss limit: 8% of account.
   Hit it → paper trade rest of week.

5. MONTHLY loss limit: 12% of account.
   Hit it → full stop, review everything.

6. NEVER add to a losing position.
   Average down = accelerate ruin.

7. Know your edge BEFORE you size.
   If you can't state your win rate and average R,
   you're gambling, not trading.

8. Run Monte Carlo quarterly.
   Your actual stats change. Your sizing should adapt.
```

---

## Related Skills

- [Risk And Portfolio](risk-and-portfolio.md)
- [Drawdown Playbook](drawdown-playbook.md)
- [Portfolio Optimization](portfolio-optimization.md)
- [Real-Time Risk Monitor](real-time-risk-monitor.md)
