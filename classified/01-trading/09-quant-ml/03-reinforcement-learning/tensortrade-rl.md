---
name: tensortrade-rl
description: TensorTrade — composable RL framework for building and training reinforcement learning trading agents. Modular TradingEnv with Observer, ActionScheme, RewardScheme, Portfolio, Exchange components. Integrates Ray RLlib for distributed training. Python
kind: reference
category: trading/quant
status: active
tags: [portfolio, python, quant, rl, tensortrade, trading]
related_skills: [backtesting-sim, backtest-report-generator, hurst-exponent-dynamics-crisis-prediction, ml-trading, quant-ml-trading]
---

# tensortrade-rl

USE FOR:
  - "train RL agent to trade"
  - "reinforcement learning for algorithmic trading"
  - "PPO / DQN / A3C trading agent"
  - "custom trading environment (gym-style)"
  - "backtesting with RL agent"
  - "distributed RL training with Ray"
  - "position-based reward function trading"
tags: [RL, reinforcement-learning, trading, PPO, DQN, Ray, RLlib, backtesting, gym, TensorTrade, algorithmic]
kind: framework
category: quant-ml-trading

---

## What Is TensorTrade?

Open-source Python RL trading framework. Builds composable `TradingEnv` environments
to train and evaluate RL agents against market data.

- Repo: https://github.com/tensortrade-org/tensortrade
- Docs: tensortrade.org
- License: Apache 2.0
- Python: 3.12+

> Research finding: PPO on BTC/USD achieves directional prediction at zero commission,
> but trading frequency → commissions exceed profits in live conditions.

---

## Core Architecture

```
┌─────────────── TradingEnv ────────────────────┐
│                                               │
│  Observer      → feature engineering          │
│  ↓                                            │
│  Agent         → RL policy (PPO/DQN/etc.)     │
│  ↓                                            │
│  ActionScheme  → BUY / SELL / HOLD orders     │
│  ↓                                            │
│  Exchange      → simulated execution + fees   │
│  ↓                                            │
│  Portfolio     → wallet + position tracking   │
│  ↓                                            │
│  RewardScheme  → position-based returns       │
└───────────────────────────────────────────────┘
```

---

## Installation

```bash
python3.12 -m venv tensortrade-env
source tensortrade-env/bin/activate
pip install -e .
pip install -r examples/requirements.txt
```

---

## Basic Usage

```python
import tensortrade.env.default as default
from tensortrade.feed.core import Stream, DataFeed
from tensortrade.oms.exchanges import Exchange
from tensortrade.oms.services.execution.simulated import execute_order
from tensortrade.oms.wallets import Wallet, Portfolio

# Define exchange and portfolio
coinbase = Exchange("coinbase", service=execute_order)(
    Stream.source(price_data, dtype="float").rename("USD-BTC")
)
portfolio = Portfolio(USD, [Wallet(coinbase, 10000 * USD), Wallet(coinbase, 0 * BTC)])

# Build environment
env = default.create(
    portfolio=portfolio,
    action_scheme="managed-risk",     # BUY/SELL/HOLD with risk sizing
    reward_scheme="risk-adjusted",    # Sharpe-ratio based reward
    feed=DataFeed([price_stream, volume_stream, rsi_stream]),
    window_size=20,
)
```

---

## Training with Ray RLlib

```python
from ray import tune
from ray.rllib.algorithms.ppo import PPOConfig

config = (
    PPOConfig()
    .environment(env_class, env_config={"window_size": 20})
    .training(lr=1e-4, gamma=0.99, train_batch_size=4000)
    .rollouts(num_rollout_workers=4)
)

tune.run("PPO", config=config.to_dict(), stop={"episodes_total": 500})
```

---

## Hyperparameter Optimization (Optuna)

```python
# examples/training/train_optuna.py
# Searches: lr, gamma, clip_param, window_size, reward_scheme
```

---

## Action Schemes

| Scheme | Description |
|--------|-------------|
| `simple` | BUY / SELL / HOLD discrete actions |
| `managed-risk` | Position sizing + stop-loss built-in |
| `bsh` | Binary: BUY or SELL only |

## Reward Schemes

| Scheme | Description |
|--------|-------------|
| `simple` | Raw P&L per step |
| `risk-adjusted` | Sharpe ratio-based |
| `position-based` | Return based on current position |

---

## Key Research Insights

| Finding | Detail |
|---------|--------|
| Directional accuracy | PPO learns BTC direction at 0 commission |
| Commission sensitivity | Even small fees (0.1%) significantly hurt returns |
| Training regime | Needs 200+ episodes to converge on noisy data |
| Overfitting risk | Walk-forward validation critical |

---

## Pre-built Examples

```bash
# Simple training run
python examples/training/train_simple.py

# Distributed training (Ray)
python examples/training/train_ray.py

# Hyperparameter search
python examples/training/train_optuna.py

# Use pre-tuned config
python examples/training/train_best.py
```


---
