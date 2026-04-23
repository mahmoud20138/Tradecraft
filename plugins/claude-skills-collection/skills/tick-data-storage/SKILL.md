---
name: tick-data-storage
description: >
  Tick data collection and storage: real-time tick capture from MT5, efficient storage
  formats (Parquet, HDF5), tick aggregation to OHLCV, bid/ask spread tracking.
  USE FOR: tick data, real-time data, live data feed, data storage, Parquet, HDF5,
  tick aggregation, bid ask spread, L1 data, time and sales, trade tape,
  high frequency data, MT5 ticks, save data, data archive, historical ticks.
related_skills:
  - market-data-ingestion
  - market-data-ingestion
  - backtesting-sim
tags:
  - trading
  - data
  - tick
  - parquet
  - hdf5
  - storage
skill_level: advanced
kind: reference
category: trading/execution
status: active
---
> **Skill:** Tick Data Storage  |  **Domain:** trading  |  **Category:** data  |  **Level:** advanced
> **Tags:** `trading`, `data`, `tick`, `parquet`, `hdf5`, `storage`


# Tick Data Storage

## MT5 Real-Time Tick Capture
```python
import MetaTrader5 as mt5
import pandas as pd
import time
from pathlib import Path

def capture_ticks(symbol: str, duration_sec: int = 3600,
                  save_path: str = "data/ticks/") -> pd.DataFrame:
    """Capture live ticks from MT5 for specified duration."""
    mt5.initialize()
    Path(save_path).mkdir(parents=True, exist_ok=True)
    ticks = []
    start = time.time()
    last_tick = None

    while time.time() - start < duration_sec:
        tick = mt5.symbol_info_tick(symbol)
        if tick and tick != last_tick:
            ticks.append({
                "time": pd.Timestamp(tick.time, unit="s"),
                "bid": tick.bid, "ask": tick.ask,
                "last": tick.last, "volume": tick.volume,
                "spread": round((tick.ask - tick.bid) * 10000, 1),
            })
            last_tick = tick
        time.sleep(0.05)  # 20Hz polling

    mt5.shutdown()
    df = pd.DataFrame(ticks).set_index("time")
    # Save as Parquet (efficient columnar storage)
    fname = f"{save_path}{symbol}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.parquet"
    df.to_parquet(fname, compression="snappy")
    return df
```

## Tick → OHLCV Aggregation
```python
def ticks_to_ohlcv(ticks: pd.DataFrame, freq: str = "5min") -> pd.DataFrame:
    """Aggregate tick data into OHLCV bars at any frequency."""
    mid = (ticks["bid"] + ticks["ask"]) / 2
    ohlcv = mid.resample(freq).agg(
        open="first", high="max", low="min", close="last"
    )
    ohlcv["volume"] = ticks["volume"].resample(freq).sum()
    ohlcv["avg_spread"] = ticks["spread"].resample(freq).mean()
    return ohlcv.dropna()
```

## Efficient Storage Formats
| Format | Size | Speed | Use Case |
|--------|------|-------|----------|
| CSV | Large | Slow | Human-readable, small datasets |
| Parquet | Small (10×) | Fast | Production — columnar, compressed |
| HDF5 | Medium | Very fast | ML pipelines — random access |
| Feather | Small | Fastest | In-memory → disk → in-memory cycles |

```python
# Recommended: Parquet for persistence, Feather for ML pipelines
import pyarrow.parquet as pq

def load_ticks(symbol: str, date: str, path: str = "data/ticks/") -> pd.DataFrame:
    pattern = f"{path}{symbol}_{date}*.parquet"
    import glob
    files = glob.glob(pattern)
    return pd.concat([pd.read_parquet(f) for f in files]).sort_index()
```

## Spread Analytics
```python
def spread_analysis(ticks: pd.DataFrame) -> dict:
    """Analyze bid/ask spread patterns throughout the day."""
    ticks["hour"] = ticks.index.hour
    hourly = ticks.groupby("hour")["spread"].agg(["mean", "max", "min"])
    widest = hourly["mean"].idxmax()
    tightest = hourly["mean"].idxmin()
    return {
        "avg_spread_pips": round(ticks["spread"].mean(), 2),
        "widest_hour_utc": widest,
        "tightest_hour_utc": tightest,
        "scalp_recommended_hours": hourly[hourly["mean"] < 1.0].index.tolist(),
        "avoid_hours": hourly[hourly["mean"] > 2.0].index.tolist(),
    }
```

---

## Related Skills

- [Market Data Ingestion](../market-data-ingestion.md)
- [Data Pipelines](../market-data-ingestion.md)
- [Market Microstructure](../market-microstructure.md)
- [Backtesting Sim](../backtesting-sim.md)



---



---

# ── KNOWLEDGE INJECTION: Markov Chains (from Veritasium) ──
> Source: "The Strange Math That Predicts (Almost) Anything" — Veritasium (2025)
> Added: 2026-03-17 · Relevant skills: statistics-timeseries, quant-ml-trading, ml-trading

## Markov Chains — Complete Reference

### Origin Story (1905 Russian Math Feud)
- **Pavel Nekrasov** ("Tsar of Probability"): claimed statistical independence proved free will
- **Andrey Markov** ("The Furious"): proved him wrong using Pushkin's *Eugene Onegin*
  - Counted vowel/consonant sequences → next letter depends on current letter
  - Dependent events STILL follow the Law of Large Numbers → predictable patterns emerge

### Core Definition
> **"The next state depends ONLY on the current state — not the entire past."**

Three components:
1. **States** — all possible conditions the system can be in
2. **Transition probabilities** — P(next state | current state)
3. **Markov property** — memoryless; past history is irrelevant

### Key Mathematical Properties
| Property | Definition | Trading Use |
|----------|-----------|-------------|
| **Transition Matrix (P)** | P[i][j] = prob of moving from state i → j | Regime switching probabilities |
| **Stationary Distribution (π)** | Long-run % time spent in each state | Expected time in trending vs ranging |
| **Mixing Time** | Steps until process forgets initial state | Regime persistence measure |
| **Ergodicity** | Every state reachable from every other | Ensures stationary dist. exists |

### Transition Matrix Example (Market Regimes)
```
           Trending  Ranging  Volatile
Trending  [  0.70     0.20     0.10  ]
Ranging   [  0.25     0.60     0.15  ]
Volatile  [  0.30     0.30     0.40  ]
```
→ Stationary distribution gives long-run % time in each regime

### Python Implementation
```python
import numpy as np

# Transition matrix
P = np.array([
    [0.70, 0.20, 0.10],  # from Trending
    [0.25, 0.60, 0.15],  # from Ranging
    [0.30, 0.30, 0.40],  # from Volatile
])

# Stationary distribution (solve π = πP)
eigenvalues, eigenvectors = np.linalg.eig(P.T)
stationary = eigenvectors[:, np.isclose(eigenvalues, 1)].real.flatten()
stationary /= stationary.sum()
print(stationary)  # [0.47, 0.35, 0.18] → 47% trending, 35% ranging, 18% volatile

# Simulate Markov chain
def simulate(P, start_state, n_steps):
    states = [start_state]
    for _ in range(n_steps):
        states.append(np.random.choice(len(P), p=P[states[-1]]))
    return states
```

### Real-World Applications

**1. Monte Carlo Method (Manhattan Project, 1940s)**
- Ulam + von Neumann: simulated nuclear chain reactions using Markov processes
- Now used for: strategy stress testing, option pricing, risk simulation
```python
# Monte Carlo equity curve simulation
def monte_carlo(returns, n_sims=1000, n_days=252):
    results = []
    for _ in range(n_sims):
        simulated = np.random.choice(returns, n_days, replace=True)
        results.append(np.cumprod(1 + simulated))
    return np.array(results)
```

**2. Google PageRank**
- Web pages = states, links = transitions
- Random surfer model → stationary distribution = page importance
- Trading equivalent: asset importance by capital flow network

**3. Card Shuffling (Mixing Time)**
- Bayer & Diaconis: exactly **7 riffle shuffles** randomize a 52-card deck
- Trading equivalent: how many bars until regime signal is reliable

**4. Hidden Markov Models (HMM) for Regime Detection**
```python
from hmmlearn import hmm

model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=100)
returns = np.array(daily_returns).reshape(-1, 1)
model.fit(returns)
hidden_states = model.predict(returns)
# 0=low vol, 1=trending, 2=high vol/crisis
```

**5. Markov Decision Processes (MDP) — Reinforcement Learning**
- State: market conditions
- Action: buy/sell/hold
- Reward: P&L
- Policy: optimal action per state
- Used in: AlphaGo, self-driving cars, RL trading agents

### Markov Chains vs LLMs
| | Markov Chain | LLM (Claude/GPT) |
|--|-------------|-----------------|
| Memory | Memoryless (current state only) | Long-range context window |
| Prediction | P(next | current) | P(next | all prior tokens) |
| Complexity | O(states²) | O(sequence²) |
| Interpretable | Yes | No |

### Trading Applications Summary
| Application | How |
|-------------|-----|
| **Regime detection** | HMM on returns → hidden states |
| **Regime persistence** | Transition matrix diagonal |
| **Strategy switching** | Trigger on regime change |
| **Monte Carlo backtests** | Simulate paths from historical returns |
| **Position sizing** | Weight by stationary distribution |
| **Risk modeling** | Tail state probabilities |


---
