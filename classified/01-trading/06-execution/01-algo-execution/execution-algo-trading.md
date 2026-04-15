---
name: execution-algo-trading
description: "Institutional execution algorithms: TWAP, VWAP, Implementation Shortfall, POV, Iceberg orders, slippage analysis, market impact, and TCA. USE FOR: execution, TWAP, VWAP, implementation shortfall, slippage, market impact, TCA, iceberg order, POV, algo execution, transaction cost."
related_skills:
  - market-making-hft
  - liquidity-analysis
  - trading-autopilot
tags:
  - trading
  - execution
  - twap
  - vwap
  - iceberg
  - algo
skill_level: advanced
kind: reference
category: trading/execution
status: active
---
> **Skill:** Execution Algo Trading  |  **Domain:** trading  |  **Category:** execution  |  **Level:** advanced
> **Tags:** `trading`, `execution`, `twap`, `vwap`, `iceberg`, `algo`


---

## Execution Algorithm Trading Skill

### Overview
Implements institutional-grade execution algorithms used by buy-side desks to minimise
market impact and transaction costs when executing large orders.

### Python Module
`xtrading/skills/execution_algo.py`

### Stack
- **numpy** — Numerical computations, binomial tree, random generation
- **pandas** — VWAP calculation, fill data management
- **scipy** — Statistical computations

---

## 1. TWAP Executor

```python
from datetime import datetime, timedelta
from xtrading.skills.execution_algo import TWAPExecutor

now = datetime.now()
twap = TWAPExecutor(
    symbol="EURUSD",
    total_qty=100_000,
    side="buy",
    start_time=now,
    end_time=now + timedelta(hours=4),
    n_slices=20,
    randomise_size=True,    # add ±15% size variation
    randomise_time=True,    # add ±10% timing jitter
)

schedule = twap.build_schedule()
# schedule.n_slices = 20
# schedule.estimated_cost_bps ≈ 3.0
# schedule.slices[i].target_time, .quantity, .order_type

# Simulate against historical prices
import pandas as pd
prices = pd.Series(...)  # mid prices with DatetimeIndex
result = twap.simulate_execution(prices, spread_bps=2.0)
# {"avg_fill_price": 1.1005, "twap_benchmark": 1.1003,
#  "vs_benchmark_bps": 1.8, "total_cost_bps": 3.8}
```

---

## 2. VWAP Executor

```python
from xtrading.skills.execution_algo import VWAPExecutor
import numpy as np

# Custom intraday volume profile
profile = np.array([0.10, 0.08, 0.06, 0.05, 0.04, 0.04,
                    0.04, 0.04, 0.05, 0.06, 0.07, 0.08,
                    0.09, 0.10, 0.10, 0.10])

vwap = VWAPExecutor(
    symbol="XAUUSD",
    total_qty=50_000,
    side="sell",
    start_time=now,
    end_time=now + timedelta(hours=8),
    volume_profile=profile,
    participation_cap=0.15,   # max 15% of any interval
)

schedule = vwap.build_schedule(avg_interval_volume=10_000)
# schedule.participation_rate ≈ 0.031 (3.1% of daily volume)

# Calculate realised VWAP
import pandas as pd
vwap_price = vwap.calculate_volume_weighted_price(prices, volumes)
```

---

## 3. Implementation Shortfall (Almgren-Chriss)

```python
from xtrading.skills.execution_algo import ISOptimiser

opt = ISOptimiser(
    total_qty=100_000,
    T_hours=4.0,             # execute over 4 hours
    sigma=0.02,              # daily vol
    eta=2.5e-6,              # temporary impact coefficient
    gamma=1e-7,              # permanent impact coefficient
    risk_aversion=1e-6,      # λ: 0 = minimise IS only
)

result = opt.optimal_trajectory(n_intervals=10)
# {
#   "urgency_factor_kappa": 0.000123,
#   "expected_shortfall_bps": 4.2,
#   "schedule": [
#     {"interval": 1, "qty_to_trade": 8234, "remaining_inventory": 91766, "completion_pct": 8.2},
#     ...
#   ]
# }

# Efficient frontier (trade-off: urgency vs cost)
frontier = opt.efficient_frontier()  # DataFrame
```

---

## 4. POV (Percentage of Volume)

```python
from xtrading.skills.execution_algo import POVExecutor

pov = POVExecutor(
    symbol="GBPUSD",
    total_qty=200_000,
    side="buy",
    target_pov=0.10,          # 10% of market volume
    min_slice_qty=1_000,
    max_slice_qty=20_000,
)

# Called on each new market volume observation
slice_order = pov.on_market_volume(
    interval_volume=50_000,
    mid_price=1.2650,
    spread_bps=1.5,
)

# Summary after execution
summary = pov.execution_summary()
# {"n_fills": 15, "avg_fill_price": 1.2652, "vs_vwap_bps": 1.2, "completion_pct": 85.3}
```

---

## 5. Iceberg Order

```python
from xtrading.skills.execution_algo import IcebergOrder

ice = IcebergOrder(
    symbol="XAUUSD",
    total_qty=10_000,
    display_qty=500,           # only 500 oz visible at a time
    side="buy",
    limit_price=2000.0,
    randomise_display=True,    # vary display size ±10%
)

# Process fills
status = ice.on_fill(fill_qty=500, fill_price=2000.5)
# {"filled": 500, "total_filled": 500, "remaining": 9500,
#  "visible": 487, "reserve": 9013, "refreshed": True, "complete": False}

print(ice.summary)
```

---

## 6. Slippage & Market Impact Analysis

```python
from xtrading.skills.execution_algo import SlippageAnalyser, MarketImpactModel

# Post-trade slippage decomposition
decomp = SlippageAnalyser.decompose(
    arrival_price=1.1000,
    avg_fill_price=1.1012,
    vwap_benchmark=1.1008,
    twap_benchmark=1.1005,
    side="buy",
    spread_bps=2.0,
)
# {"implementation_shortfall_bps": 10.9, "market_impact_bps": 8.9,
#  "spread_cost_bps": 2.0, "grade": "B  (Acceptable)"}

# Pre-trade impact estimate
impact = SlippageAnalyser.estimate_market_impact(
    qty=50_000, adv=2_000_000, price=1.1000,
    volatility_daily=0.008, side="buy", model="sqrt"
)
# {"impact_bps": 5.3, "participation_rate": 0.025}

# Full cost model (Almgren-Chriss components)
model = MarketImpactModel(sigma=0.01, adv=1_000_000,
                           bid_ask_spread=0.0002, price=1.1000)
cost = model.total_cost(qty=100_000, execution_time_hours=2.0)
# {"permanent_impact_bps": 2.8, "transient_impact_bps": 1.9,
#  "spread_cost_bps": 0.9, "total_cost_bps": 5.6}
```

---

## 7. TCA Report

```python
from xtrading.skills.execution_algo import TCAReport
import pandas as pd

fills = pd.DataFrame({
    "timestamp": [...],
    "qty": [1000] * 20,
    "fill_price": [...],
    "mid_price": [...],
})

report = TCAReport(
    symbol="EURUSD", side="buy", fills=fills,
    arrival_price=1.1000, vwap=1.1005, twap=1.1003,
    algorithm="VWAP", benchmark="vwap"
)
d = report.to_dict()
# {
#   "total_cost_bps": 4.2,
#   "quality_score": 91.6,
#   "grade": "A  (Good)",
#   "implementation_shortfall_bps": 2.3,
# }
```

---

## Decision Framework

| Order Size (% ADV) | Recommended Algorithm | Typical Cost (bps) |
|--------------------|-----------------------|-------------------|
| < 1%               | Market / Limit        | 1–2               |
| 1–5%               | TWAP (1–2h)           | 2–4               |
| 5–15%              | VWAP (full day)       | 4–8               |
| 15–30%             | IS + POV              | 8–15              |
| > 30%              | Iceberg + multi-day   | 15–30             |

## Usage Conventions

1. **qty** — shares, lots, or contracts (consistent units throughout)
2. **adv** — average daily volume in the same units as qty
3. **sigma** — daily volatility as decimal (0.01 = 1%)
4. **spread_bps** — round-trip spread cost, not half-spread
5. **TCA benchmark** — use VWAP for passive strategies, arrival for aggressive

---

## Related Skills

- [Market Making Hft](../market-making-hft.md)
- [Market Microstructure](../market-microstructure.md)
- [Liquidity Analysis](../liquidity-analysis.md)
- [Trading Automation](../trading-autopilot.md)
