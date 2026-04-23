---
name: trading-gym-rl-env
description: TradingGym — OpenAI Gym-style RL trading environment toolkit for tick and OHLC data. Supports training, backtesting, and (planned) live trading via IB API. 3-action discrete space (hold/buy/sell), configurable observation window, fee-adjusted rewards
kind: strategy
category: trading/quant
status: active
tags: [backtesting, env, gym, quant, trading]
related_skills: [backtesting-sim, backtest-report-generator, hurst-exponent-dynamics-crisis-prediction, ml-trading, quant-ml-trading]
---

# trading-gym-rl-env

USE FOR:
  - "gym-style trading environment for RL"
  - "tick-level RL trading simulation"
  - "backtesting RL agent on OHLC data"
  - "custom RL trading environment setup"
  - "discrete action space trading (hold/buy/sell)"
tags: [RL, gym, trading-environment, tick-data, OHLC, backtesting, reinforcement-learning]
kind: framework
category: quant-ml-trading

---

## What Is TradingGym?

OpenAI Gym-inspired RL trading environment toolkit.
- Repo: https://github.com/Yvictor/TradingGym
- Focus: **Tick-level data** (also OHLC)
- Use cases: RL training, backtesting, future live trading (IB API)

---

## Environment Design

### Action Space
```
0 → Hold (do nothing)
1 → Buy one unit
2 → Sell one unit
```

### Observation Space
```
State = selected features over window of N steps
Features: price, volume, bid/ask, custom columns
Window size: configurable (default: 30 ticks)
```

### Reward
```
Reward = price_delta × position - transaction_fee
```

---

## Installation & Setup

```python
import trading_gym
import pandas as pd

# Load your market data (any asset, any timeframe)
data = pd.read_hdf("market_data.h5")

# Create environment
env = trading_gym.TradingEnv(
    data=data,
    obs_len=30,           # Observation window
    step_len=1,           # Steps per action
    fee=0.001,            # Transaction fee (0.1%)
    deal_col_name="close",# Column for P&L calculation
)
```

---

## Usage Patterns

### Random Agent (Baseline)
```python
obs = env.reset()
done = False
while not done:
    action = env.action_space.sample()  # Random: 0, 1, or 2
    obs, reward, done, info = env.step(action)
```

### Custom RL Agent
```python
class MyAgent:
    def predict(self, obs):
        # Your RL policy here (DQN, PPO, etc.)
        return action  # 0, 1, or 2

agent = MyAgent()
obs = env.reset()
done = False
while not done:
    action = agent.predict(obs)
    obs, reward, done, info = env.step(action)
```

### Rule-Based Strategy (MA Crossover)
```python
class MACrossoverAgent:
    def predict(self, obs):
        fast_ma = obs[-5:, price_col].mean()
        slow_ma = obs[-20:, price_col].mean()
        if fast_ma > slow_ma:
            return 1  # Buy
        elif fast_ma < slow_ma:
            return 2  # Sell
        return 0      # Hold
```

---

## Comparison: TradingGym vs TensorTrade

| Feature | TradingGym | TensorTrade |
|---------|-----------|-------------|
| Data focus | Tick-level primary | OHLCV + feeds |
| Action space | Simple discrete (3) | Configurable |
| Reward | Price delta - fee | Multiple schemes |
| RL integration | Any gym-compatible | Ray RLlib built-in |
| Portfolio management | Basic | Full wallets/positions |
| Complexity | Lightweight | Full framework |
| Best for | Quick RL experiments | Production RL systems |


---
