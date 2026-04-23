---
name: options-trading
description: "Full options trading: Black-Scholes pricing, Greeks, IV surface, multi-leg strategies, and option screening. USE FOR: options, black-scholes, greeks, delta, gamma, theta, vega, implied volatility, iron condor, straddle, strangle, call, put, option chain."
related_skills:
  - technical-analysis
  - risk-and-portfolio
  - statistics-timeseries
  - portfolio-optimization
tags:
  - trading
  - asset-class
  - options
  - greeks
  - iv
  - multi-leg
  - volatility
skill_level: advanced
kind: reference
category: trading/asset-classes
status: active
---
> **Skill:** Options Trading  |  **Domain:** trading  |  **Category:** asset-class  |  **Level:** advanced
> **Tags:** `trading`, `asset-class`, `options`, `greeks`, `iv`, `multi-leg`, `volatility`


---

## Options Trading Skill

### Overview
Complete options pricing and strategy analysis toolkit. Implements Black-Scholes (1973) pricing,
all five first-order Greeks plus second-order (charm, vanna, volga), implied volatility extraction,
multi-leg strategy payoff analysis, IV surface construction, and option chain screening.

### Python Module
`xtrading/skills/options.py`

### Stack
- **scipy.stats.norm** — Black-Scholes d1/d2 cumulative normal
- **scipy.optimize.brentq** — Implied volatility root finding
- **numpy** — Vectorised payoff calculations and Monte Carlo
- **pandas** — Option chain and surface management

---

## 1. Options Pricing — Black-Scholes

```python
from xtrading.skills.options import OptionsPricing

# European call price
price = OptionsPricing.black_scholes(S=100, K=100, T=0.25, r=0.05, sigma=0.20, option_type="call")
# → ~5.07

# Put-call parity holds:
# call - put = S - K * exp(-rT)

# Implied volatility (Brent solver)
iv = OptionsPricing.implied_volatility(
    market_price=5.0, S=100, K=100, T=0.25, r=0.05, option_type="call"
)
# → 0.1963 (≈20% IV)

# Binomial tree (American options)
am_put = OptionsPricing.binomial_price(
    S=100, K=100, T=0.25, r=0.05, sigma=0.20, option_type="put", american=True
)

# Monte Carlo with confidence interval
mc = OptionsPricing.monte_carlo_price(S=100, K=100, T=0.25, r=0.05, sigma=0.20, n_paths=100_000)
# → {"price": 5.07, "std_error": 0.02, "ci_95_lower": 5.03, "ci_95_upper": 5.11}
```

---

## 2. Greeks Calculator

```python
from xtrading.skills.options import GreeksCalculator

# All Greeks in one call
greeks = GreeksCalculator.all_greeks(S=100, K=100, T=0.25, r=0.05, sigma=0.20, option_type="call")
# {
#   "price": 5.07, "delta": 0.5377, "gamma": 0.0394,
#   "theta": -0.0451, "vega": 0.1974, "rho": 0.1220,
#   "charm": -0.00015, "vanna": 0.0789, "volga": 0.3948,
#   "moneyness": "ATM", "intrinsic": 0.0, "time_value": 5.07
# }

# Individual Greeks
delta = GreeksCalculator.delta(S=105, K=100, T=0.25, r=0.05, sigma=0.20, option_type="call")
# → 0.726 (ITM call, delta > 0.5)

gamma = GreeksCalculator.gamma(S=100, K=100, T=0.25, r=0.05, sigma=0.20)
# → 0.0394 (always positive)

theta = GreeksCalculator.theta(S=100, K=100, T=0.25, r=0.05, sigma=0.20, option_type="call")
# → -0.0451 per day (time decay)
```

---

## 3. Strategy Builder — Multi-Leg Analysis

```python
from xtrading.skills.options import StrategyBuilder

# Bull Call Spread
builder = StrategyBuilder.bull_call_spread(
    symbol="SPY", S=100, K_long=100, K_short=110,
    T=0.25, r=0.05, sigma=0.20
)
result = builder.analyse()
# result.strategy_name = "Bull Call Spread"
# result.net_premium   = -1.23  (debit: negative)
# result.max_profit    = 8.77
# result.max_loss      = -1.23
# result.breakeven_prices = [101.23]
# result.risk_reward   = 7.13
# result.probability_of_profit = 0.41

# Iron Condor
ic = StrategyBuilder.iron_condor(
    symbol="SPX", S=4000,
    K_put_long=3800, K_put_short=3900,
    K_call_short=4100, K_call_long=4200,
    T=0.25, r=0.05, sigma=0.18
)
result = ic.analyse()
# result.net_premium = +3.45  (credit)
# result.max_profit  = 3.45
# result.max_loss    = -96.55

# Long Straddle
straddle = StrategyBuilder.long_straddle(
    symbol="AAPL", S=150, K=150, T=0.25, r=0.05, sigma=0.35
)
result = straddle.analyse()
# Two breakeven prices: [139.xx, 160.xx]
```

---

## 4. Volatility Surface

```python
import pandas as pd
from xtrading.skills.options import VolatilitySurface

# Build from option chain data
surface_data = pd.DataFrame({
    "strike": [90, 95, 100, 105, 110, 90, 95, 100, 105, 110],
    "expiry_days": [30]*5 + [60]*5,
    "iv": [0.25, 0.22, 0.20, 0.21, 0.23, 0.27, 0.24, 0.22, 0.23, 0.25],
})
vs = VolatilitySurface(surface_data)

# Smile at 30-day expiry
smile = vs.smile_at_expiry(expiry_days=30, atm_strike=100)
# {"atm_iv": 0.20, "skew_25d": -0.02, "butterfly_25d": 0.015, "bias": "put_skew"}

# Term structure
ts = vs.term_structure(atm_strike=100)
# DataFrame: expiry_days → atm_iv, vix_equiv, annualised_cost_pct

# IV Rank
import numpy as np
hist = pd.Series(np.linspace(0.10, 0.40, 252))
rank = vs.iv_rank(current_iv=0.30, historical_ivs=hist)
# {"iv_rank": 66.7, "regime": "NORMAL_IV", "strategy_bias": "NEUTRAL"}

# Arbitrage check
arb = vs.validate_no_arbitrage()
# {"arbitrage_free": True, "violations": [], "n_violations": 0}
```

---

## 5. Option Screener

```python
from xtrading.skills.options import OptionScreener

screener = OptionScreener(chain_df, underlying_price=100.0, r=0.05)

# Screen for short-premium setups (30-60 DTE, 0.20-0.45 delta)
candidates = screener.screen(
    min_pop=0.60, min_dte=30, max_dte=60,
    min_delta=0.20, max_delta=0.45,
    option_type="put",
)

# Expected move calculation
em = screener.expected_move(expiry_days=30)
# {"expected_move_pts": 5.07, "expected_move_pct": 5.07,
#  "upper_bound": 105.07, "lower_bound": 94.93}
```

---

## Usage Conventions

1. **All prices** — same currency units as S and K
2. **T** — always in years (30 days = 30/365 = 0.082)
3. **sigma** — annualised decimal (20% = 0.20)
4. **r** — annualised risk-free rate decimal
5. **Theta** — returned as per-day (divide annual by 365 internally)
6. **Vega** — returned per 1% IV move (divide annual by 100 internally)
7. **Put-call parity** — always verified for European options

## Key Formulas

```
Black-Scholes Call: S*N(d1) - K*exp(-rT)*N(d2)
Black-Scholes Put:  K*exp(-rT)*N(-d2) - S*N(-d1)
d1 = [ln(S/K) + (r + σ²/2)*T] / (σ*√T)
d2 = d1 - σ*√T

Delta (call) = N(d1)
Delta (put)  = N(d1) - 1
Gamma        = N'(d1) / (S*σ*√T)
Theta (call) = [-S*N'(d1)*σ/(2√T) - r*K*exp(-rT)*N(d2)] / 365
Vega         = S*√T*N'(d1) / 100
```

---

## Related Skills

- [Technical Analysis](../technical-analysis.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
- [Statistical Analysis](../statistics-timeseries.md)
- [Portfolio Optimization](../portfolio-optimization.md)
