---
name: portfolio-optimization
description: "Modern portfolio construction: Markowitz MVO, Risk Parity, Black-Litterman, Hierarchical Risk Parity (HRP), Kelly Criterion, VaR/CVaR tail risk, and portfolio analytics. USE FOR: portfolio optimization, Markowitz, efficient frontier, risk parity, Black-Litterman, HRP, Kelly criterion, VaR, CVaR, max Sharpe, minimum variance, covariance, portfolio weights, asset allocation, tail risk, diversification."
related_skills:
  - risk-and-portfolio
  - portfolio-optimization
  - cross-asset-relationships
  - statistics-timeseries
tags:
  - trading
  - risk
  - portfolio
  - markowitz
  - hrp
  - risk-parity
  - optimization
skill_level: advanced
kind: reference
category: trading/risk
status: active
related_to: [portfolio-optimizer]
---
> **Skill:** Portfolio Optimization  |  **Domain:** trading  |  **Category:** risk  |  **Level:** advanced
> **Tags:** `trading`, `risk`, `portfolio`, `markowitz`, `hrp`, `risk-parity`, `optimization`


---

## Portfolio Optimization Skill

### Overview
Complete modern portfolio construction toolkit. Implements five major allocation frameworks —
Markowitz MVO, Equal Risk Contribution, Black-Litterman, Hierarchical Risk Parity, and Kelly
Criterion — plus robust covariance estimation, tail risk measurement, and performance attribution.

### Python Module
`xtrading/skills/portfolio_optimization.py`

### Stack
- **scipy.optimize.minimize** — SLSQP constrained optimisation for MVO and ERC
- **scipy.cluster.hierarchy** — Ward linkage clustering for HRP
- **scipy.spatial.distance** — Condensed distance matrix for HRP
- **numpy** — Matrix algebra, eigenvalue decomposition
- **pandas** — Returns DataFrames, weight Series

---

## 1. Covariance Estimator — Robust Matrix Estimation

```python
import pandas as pd
from xtrading.skills.portfolio_optimization import CovarianceEstimator

# returns: DataFrame of daily returns (T × N)
returns = pd.DataFrame(...)  # columns = asset names

# Standard sample covariance (noisy for small T)
cov_sample = CovarianceEstimator.sample(returns)

# Ledoit-Wolf analytical shrinkage (recommended for N > 10 or T < 3N)
cov_lw = CovarianceEstimator.ledoit_wolf(returns)

# Exponentially weighted (upweights recent data, halflife = 60 days)
cov_ewm = CovarianceEstimator.exponential(returns, halflife=60)

# Constant correlation shrinkage target
cov_cc = CovarianceEstimator.constant_correlation(returns)

# Guarantee positive definiteness (clip negative eigenvalues)
cov_pd = CovarianceEstimator.ensure_positive_definite(cov_lw, epsilon=1e-8)
```

### When to Use Which Estimator

| Method | Best For | Limitation |
|--------|----------|------------|
| `sample` | Large T (T >> 5N) | Noisy; singular if T < N |
| `ledoit_wolf` | General use, N ≤ 50 | Shrinks toward identity |
| `exponential` | Regime-aware, recent data | Requires tuning halflife |
| `constant_correlation` | Stable correlation structure | Assumes constant ρ |

---

## 2. MeanVarianceOptimiser — Markowitz Efficient Frontier

```python
from xtrading.skills.portfolio_optimization import MeanVarianceOptimiser

opt = MeanVarianceOptimiser(
    returns=returns,               # daily returns DataFrame
    cov_method="ledoit_wolf",      # covariance estimator
    risk_free_rate=0.05,           # annualised risk-free rate
    allow_short=False,             # long-only (set True for long/short)
)

# Maximum Sharpe Ratio (tangency) portfolio
max_s = opt.max_sharpe()
# max_s.method           → "Max Sharpe"
# max_s.weights          → {"EURUSD": 0.32, "XAUUSD": 0.28, ...}
# max_s.expected_return  → 0.1842  (18.4% annualised)
# max_s.expected_volatility → 0.0921
# max_s.sharpe_ratio     → 1.457
# max_s.diversification_ratio → 1.23
# max_s.effective_n      → 3.8   (1 / HHI)

# Global Minimum Variance portfolio
min_v = opt.min_variance()

# Target a specific annual return (min variance for that return)
port_10 = opt.target_return(target=0.10)   # 10% annualised return

# Maximum Diversification portfolio
max_d = opt.max_diversification()

# Full efficient frontier
frontier = opt.efficient_frontier(n_points=50)
# DataFrame: columns = ["return", "volatility", "sharpe"]

# Rebalancing trades from current allocation
current_w = {"EURUSD": 0.50, "XAUUSD": 0.30, "GBPUSD": 0.20}
trades_df = max_s.rebalance_trades(current_w, portfolio_value=100_000)
# asset    current_weight  target_weight  delta_weight  trade_value  action
# EURUSD   0.50            0.32           -0.18         -18000.0     sell
# XAUUSD   0.30            0.28           -0.02          -2000.0     sell
# GBPUSD   0.20            0.40           +0.20         +20000.0     buy
```

### PortfolioWeights Fields

| Field | Type | Description |
|-------|------|-------------|
| `method` | `str` | Optimisation method name |
| `weights` | `dict[str, float]` | Asset → weight (sums to 1.0) |
| `expected_return` | `float` | Annualised expected return |
| `expected_volatility` | `float` | Annualised volatility |
| `sharpe_ratio` | `float` | (Return − rf) / Volatility |
| `diversification_ratio` | `float` | Weighted avg vol / portfolio vol |
| `effective_n` | `float` | 1 / HHI (effective number of bets) |
| `metadata` | `dict` | Method-specific extra data |

---

## 3. RiskParityOptimiser — Equal Risk Contribution

```python
from xtrading.skills.portfolio_optimization import RiskParityOptimiser
import numpy as np

# Equal risk contribution (each asset = same % of portfolio variance)
erc = RiskParityOptimiser(
    returns=returns,
    cov_method="ledoit_wolf",
)
port = erc.optimise()
# port.method → "Equal Risk Contribution (Risk Parity)"
# port.metadata["risk_contributions"] → {"EURUSD": 0.25, "XAUUSD": 0.25, ...}
# port.metadata["erc_convergence"]    → True

# Custom risk budgets (e.g. 60/40 risk allocation)
budgets = np.array([0.60, 0.40])
erc_custom = RiskParityOptimiser(returns[["SPY", "TLT"]], risk_budgets=budgets)
port_custom = erc_custom.optimise()
```

**Key Property**: Risk parity does NOT require return estimates. It only uses the
covariance matrix, making it robust to estimation error in expected returns.

---

## 4. BlackLittermanModel — Bayesian Return Integration

```python
import numpy as np
import pandas as pd
from xtrading.skills.portfolio_optimization import BlackLittermanModel

# Market-cap weights (or any prior/benchmark weights)
market_caps = pd.Series({
    "EURUSD": 1_000_000,
    "XAUUSD": 500_000,
    "GBPUSD": 750_000,
    "USDJPY": 250_000,
})

bl = BlackLittermanModel(
    market_caps=market_caps,
    returns=returns,
    risk_free=0.05,
    tau=0.05,                   # prior uncertainty (0.025–0.10)
    cov_method="ledoit_wolf",
)

# Add investor views
# View 1 (absolute): EURUSD will return 12% next year
# View 2 (relative): XAUUSD will outperform GBPUSD by 5%

P = np.array([
    [1, 0, 0, 0],   # View 1: long EURUSD
    [0, 1, -1, 0],  # View 2: long XAUUSD, short GBPUSD
])
Q = np.array([0.12, 0.05])      # 12% and 5% view returns

result = bl.add_views(P=P, Q=Q)
# {
#   "prior_returns":     {"EURUSD": 0.0821, "XAUUSD": 0.0654, ...},
#   "posterior_returns": {"EURUSD": 0.0965, "XAUUSD": 0.0721, ...},
#   "bl_weights":        {"EURUSD": 0.3410, "XAUUSD": 0.2850, ...},
#   "return_change":     {"EURUSD": +0.0144, "XAUUSD": +0.0067, ...},
#   "n_views": 2
# }
```

**Black-Litterman Formula**:
```
π           = δ · Σ · w_mkt          (equilibrium returns)
Ω           = τ · P · Σ · P'         (view uncertainty, diagonal)
posterior μ = [(τΣ)⁻¹ + P'Ω⁻¹P]⁻¹ · [(τΣ)⁻¹π + P'Ω⁻¹Q]
```

---

## 5. HRPOptimiser — Hierarchical Risk Parity

```python
from xtrading.skills.portfolio_optimization import HRPOptimiser

hrp = HRPOptimiser(returns=returns)
port = hrp.optimise()
# port.method  → "Hierarchical Risk Parity (HRP)"
# port.weights → {"EURUSD": 0.2841, "XAUUSD": 0.3102, ...}
# port.metadata["cluster_order"] → ["XAUUSD", "EURUSD", "USDJPY", "GBPUSD"]
```

### HRP Algorithm Steps

```
Step 1: Distance matrix    d_ij = √(0.5 × (1 − ρ_ij))
Step 2: Ward clustering    Hierarchical linkage on correlation distance
Step 3: Quasi-diagonalise  Order assets so similar assets are adjacent
Step 4: Recursive bisection
         Allocate weight proportionally to inverse variance:
         α = 1 − Var(left_cluster) / [Var(left) + Var(right)]
         left_weights  *= α
         right_weights *= (1 − α)
```

**HRP Advantages over MVO**:
- No matrix inversion → stable for large N
- Respects correlation structure → less concentrated
- No return estimates needed
- Out-of-sample outperforms MVO (Lopez de Prado 2016)

---

## 6. KellyCriterion — Optimal Position Sizing

```python
from xtrading.skills.portfolio_optimization import KellyCriterion

# Discrete Kelly (binary bet / single trade)
k = KellyCriterion.discrete(
    win_probability=0.60,
    win_payoff=1.5,          # 1.5R on win
    loss_payoff=1.0,         # 1.0R on loss
)
# {
#   "full_kelly": 0.2667,
#   "half_kelly": 0.1333,
#   "quarter_kelly": 0.0667,
#   "kelly_pct": 26.67,
#   "edge": 0.4000,
#   "recommendation": "MODERATE BET"
# }

# Continuous Kelly (Gaussian strategy returns)
k2 = KellyCriterion.continuous(
    mu=0.20,       # 20% annualised expected return
    sigma=0.15,    # 15% annualised volatility
    risk_free=0.05,
)
# {
#   "full_kelly": 6.667,      # leverage ratio (use fractional!)
#   "half_kelly": 3.333,
#   "growth_rate_full": 0.450,
#   "growth_rate_half": 0.431,
#   "sharpe_ratio": 1.00,
#   "recommendation": "AGGRESSIVE"
# }

# Multi-asset Kelly (full Kelly portfolio)
import pandas as pd, numpy as np
mu = pd.Series({"A": 0.12, "B": 0.08, "C": 0.15})
cov = pd.DataFrame([[0.04, 0.01, 0.02],
                    [0.01, 0.02, 0.01],
                    [0.02, 0.01, 0.06]],
                   index=mu.index, columns=mu.index)
k3 = KellyCriterion.multi_asset(mu, cov, risk_free=0.05)
# {
#   "full_kelly_weights":      {"A": 3.2, "B": 1.4, "C": 2.8},   # leveraged
#   "normalised_kelly_weights":{"A": 0.43, "B": 0.19, "C": 0.38}, # long-only
#   "leverage_ratio": 7.4
# }
```

### Kelly Sizing Rules

| Full Kelly | Half Kelly | Recommended Use |
|------------|------------|-----------------|
| < 0.02 | < 0.01 | No edge — skip trade |
| 0.02–0.10 | 0.01–0.05 | Small bet (conservative) |
| 0.10–0.20 | 0.05–0.10 | Moderate bet |
| > 0.20 | > 0.10 | Strong edge — still use half-Kelly |

**Rule**: Always trade **half-Kelly or less** in practice. Full Kelly maximises
long-run growth but has high variance and frequent large drawdowns.

---

## 7. TailRiskEstimator — VaR and CVaR

```python
import pandas as pd
from xtrading.skills.portfolio_optimization import TailRiskEstimator

# Historical simulation VaR (most conservative, data-driven)
hist = TailRiskEstimator.historical_var(
    returns=portfolio_returns,    # pd.Series of daily returns
    confidence=0.95,
    horizon_days=1,
)
# {
#   "method": "historical",   "confidence": 0.95,
#   "var": 0.0182,            "var_pct": 1.82,
#   "cvar": 0.0251,           "cvar_pct": 2.51,
#   "worst_return": -0.0487,  "n_observations": 252
# }

# Parametric (Gaussian) VaR — fast, assumes normality
para = TailRiskEstimator.parametric_var(
    mu=0.0004,        # daily mean return
    sigma=0.012,      # daily volatility
    confidence=0.99,
    horizon_days=10,  # 10-day regulatory horizon
)

# Monte Carlo VaR (GBM paths, most flexible)
mc = TailRiskEstimator.monte_carlo_var(
    mu=0.0004, sigma=0.012,
    confidence=0.95,
    horizon_days=1,
    n_paths=100_000,
    seed=42,
)

# Cornish-Fisher VaR (adjusted for fat tails)
cf = TailRiskEstimator.cornish_fisher_var(
    returns=portfolio_returns,
    confidence=0.95,
)
# {
#   "method": "cornish_fisher",
#   "var": 0.0209,          "var_pct": 2.09,
#   "skewness": -0.42,      "excess_kurtosis": 1.85,
#   "z_standard": -1.6449,  "z_adjusted": -1.9213,
# }
```

### VaR Method Comparison

| Method | Assumption | Best For |
|--------|-----------|----------|
| Historical | None (empirical) | Stable regimes, ≥ 250 obs |
| Parametric | Gaussian returns | Quick estimate, symmetric |
| Monte Carlo | GBM dynamics | Custom paths, derivatives |
| Cornish-Fisher | Non-Gaussian (skew+kurtosis) | Fat-tailed, skewed returns |

**CVaR (Conditional VaR)** = Expected loss *given* that loss exceeds VaR.
Always use CVaR alongside VaR — it captures tail severity, not just threshold.

---

## 8. PortfolioAnalytics — Performance Attribution

```python
import pandas as pd
from xtrading.skills.portfolio_optimization import PortfolioAnalytics

analytics = PortfolioAnalytics(
    portfolio_returns=my_daily_returns,    # pd.Series
    benchmark_returns=spy_daily_returns,   # pd.Series
    risk_free_rate=0.05,
)

# Individual statistics
ret  = analytics.annualised_return()     # 0.1842 → 18.4%
vol  = analytics.annualised_volatility() # 0.0921 → 9.2%
sr   = analytics.sharpe_ratio()          # 1.457
so   = analytics.sortino_ratio()         # 2.103
ir   = analytics.information_ratio()     # 0.823 (vs benchmark)
dd   = analytics.max_drawdown()          # -0.082 → -8.2%
beta = analytics.beta()                  # 0.65
alp  = analytics.alpha()                 # 0.042 → +4.2% annualised Jensen's α

# Full report in one call
report = analytics.full_report()
# {
#   "annualised_return": 0.1842,
#   "annualised_volatility": 0.0921,
#   "sharpe_ratio": 1.457,
#   "sortino_ratio": 2.103,
#   "information_ratio": 0.823,
#   "calmar_ratio": 2.247,
#   "max_drawdown": -0.082,
#   "max_drawdown_pct": -8.20,
#   "beta": 0.65,
#   "alpha_annualised": 0.042,
#   "var_95_1d": 0.0182,
#   "cvar_95_1d": 0.0251,
#   "n_days": 252,
# }

# Rolling Sharpe (252-day window)
rolling_sr = analytics.rolling_sharpe(window=252)
# pd.Series indexed by date: "rolling_sharpe"
```

---

## Full Workflow — Multi-Model Comparison

```python
import pandas as pd
import numpy as np
from xtrading.skills.portfolio_optimization import (
    MeanVarianceOptimiser, RiskParityOptimiser,
    HRPOptimiser, KellyCriterion, TailRiskEstimator, PortfolioAnalytics,
)

# 1. Load returns data
returns = pd.read_csv("returns.csv", index_col=0, parse_dates=True)

# 2. Build four portfolios
mvo  = MeanVarianceOptimiser(returns, cov_method="ledoit_wolf", risk_free_rate=0.05)
ms   = mvo.max_sharpe()
mv   = mvo.min_variance()

erc  = RiskParityOptimiser(returns).optimise()
hrp  = HRPOptimiser(returns).optimise()

print(f"Max Sharpe:    Sharpe={ms.sharpe_ratio:.3f}, Vol={ms.expected_volatility:.1%}")
print(f"Min Variance:  Sharpe={mv.sharpe_ratio:.3f}, Vol={mv.expected_volatility:.1%}")
print(f"Risk Parity:   EffN={erc.effective_n:.1f}")
print(f"HRP:           EffN={hrp.effective_n:.1f}")

# 3. Kelly sizing for a strategy
k = KellyCriterion.discrete(win_probability=0.60, win_payoff=2.0)
print(f"Half-Kelly: {k['half_kelly']:.1%} per trade")

# 4. Tail risk assessment
port_returns = (returns * ms.to_series()).sum(axis=1)
var_hist = TailRiskEstimator.historical_var(port_returns, 0.95)
var_cf   = TailRiskEstimator.cornish_fisher_var(port_returns, 0.95)
print(f"VaR 95%: {var_hist['var_pct']:.2f}%  (CF: {var_cf['var_pct']:.2f}%)")

# 5. Rebalancing trades
current = {"A": 0.33, "B": 0.33, "C": 0.34}
rebalance = ms.rebalance_trades(current, portfolio_value=1_000_000)
print(rebalance)
```

---

## Algorithm Selection Guide

| Objective | Recommended Model | Key Parameter |
|-----------|------------------|---------------|
| Best risk-adjusted return | `MVO.max_sharpe()` | `cov_method` |
| Lowest volatility | `MVO.min_variance()` | `allow_short` |
| Equal risk contribution | `RiskParityOptimiser` | `risk_budgets` |
| Incorporate analyst views | `BlackLittermanModel` | `tau`, `P`, `Q` |
| Correlation-robust allocation | `HRPOptimiser` | none |
| Optimal bet sizing | `KellyCriterion.discrete()` | fraction of full Kelly |
| Tail risk measurement | `TailRiskEstimator` | `confidence`, `horizon_days` |

## Usage Conventions

1. **Returns format** — daily decimal returns (not percent): `0.01 = 1%`
2. **Annualisation** — all outputs are annualised using `× 252` (trading days)
3. **Covariance** — input `returns` is daily; annualised internally by `× 252`
4. **Kelly fractions** — always use half-Kelly or less in live trading
5. **VaR sign** — returned as a positive loss (0.018 = 1.8% potential loss)
6. **CVaR** — always ≥ VaR; represents expected loss in the tail beyond VaR
7. **HRP** — no return estimates needed; pure covariance-based allocation
8. **Black-Litterman tau** — typical range 0.025–0.10; lower = more weight on prior

---

## Sharpe-First Portfolio Construction (Wall Street Quants)

> Source: "The Sharpe Ratio Explained (by a quant trader)" by Wall Street Quants (Aug 2024)

**Key quant insight:** Maximize Sharpe first, then use leverage to target desired return level.

- Two negatively correlated SR=2.0 strategies combined 50/50 → SR=5.0 portfolio
- Leverage preserves Sharpe: 2x leverage = 2x returns, 2x vol, same SR
- The tangency portfolio (highest SR portfolio) is mathematically optimal per mean-variance theory
- Benchmark: S&P 500 SR ~0.45, Buffett ~0.75, good hedge funds 2.0+
- Goal: SR 2.0+ consistently = better than 99% of investors

For full Sharpe ratio deep-dive, see `risk-and-portfolio` skill.

---

---

## Strategy Allocation by Market Regime (merged from portfolio-optimization)

> Pipeline: `market-regime-classifier` → `strategy-selection` → **this section** → `multi-strategy-orchestration`

### Regime → Strategy Allocation Matrix

**TRENDING Regime**
```
Strategy                    | Allocation | Max Concurrent
ICT MSS + FVG              |    40%     |       2
Displacement Trap Entry     |    25%     |       2
ORB (with-trend only)       |    20%     |       1
Silver Bullet / ICT 2022   |    15%     |       1
Total portfolio heat: up to 4%
```

**RANGING Regime**
```
Strategy                    | Allocation | Max Concurrent
S&D Zone Fades             |    35%     |       2
VWAP Mean Reversion        |    30%     |       2
Asian Range Fade           |    20%     |       1
ORB Mean Reversion (fade)  |    15%     |       1
Total portfolio heat: up to 3% (half-size — false breakouts common)
```

**TRANSITIONING Regime**
```
Strategy                    | Allocation | Max Concurrent
Liquidity Trap / CRT       |    40%     |       2
Breaker Block Entry        |    30%     |       1
Counter-trend ICT models   |    30%     |       1
Total portfolio heat: up to 2% (highest uncertainty — smallest allocation)
```

**VOLATILE / NEWS Regime**
```
No new entries | Capital preservation | Post-news fade (30m wait) only
Total portfolio heat: reduce to 1% max
```

### Session-Based Allocation Overlay
```
Asia 00-07 UTC   | Asian Range: 1.0x | All others: 0.25x
London 07-12     | Breakout/Sweep: 1.0x | Mean Rev: 0.5x
NY Open 13:30-15 | ORB: 1.0x | ICT: 1.0x | All valid
Overlap 13:30-16 | ALL strategies: 1.0x (peak liquidity)
Rule: Strategy allocation × session modifier = effective allocation
```

### Drawdown-Based Allocation Scaling
```
0-2%  → 1.0x (full) | 2-4% → 0.75x | 4-6% → 0.50x
6-8%  → 0.25x (one position max) | >10% → STOP — full review
Recovery: Only step UP one level per profitable day
```

### Rebalancing Priority
- Reduce: (1) Against HTF trend → (2) Wrong regime strategy → (3) Worst R-multiple → (4) Newest → (5) Illiquid
- Increase: (1) Highest win rate for regime → (2) Best liquidity for session → (3) Highest confluence score → (4) Uncorrelated

---

## Related Skills

- [Risk And Portfolio](../risk-and-portfolio.md)
- [Cross Asset Relationships](../cross-asset-relationships.md)
- [Statistical Analysis](../statistics-timeseries.md)
