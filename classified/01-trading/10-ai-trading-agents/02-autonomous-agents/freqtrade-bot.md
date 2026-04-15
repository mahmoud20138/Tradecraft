---
name: freqtrade-bot
description: Freqtrade — open-source Python crypto trading bot. Backtesting, hyperopt (ML parameter optimization), FreqAI (self-training adaptive strategies), Telegram + WebUI control. Supports Binance, Kraken, Bybit, OKX, Gate.io (spot + futures). SQLite trade h
kind: agent
category: trading/ai-agents
status: active
tags: [ai-agents, backtesting, bot, crypto, freqtrade, python, telegram, trading]
related_skills: [ai-trading-crew, autohedge-swarm, openalice-trading-agent, polymarket-prediction-agents, ritmex-crypto-agent]
---

# freqtrade-bot

USE FOR:
  - "crypto trading bot Python"
  - "freqtrade strategy development"
  - "backtesting crypto strategy"
  - "hyperopt parameter optimization"
  - "FreqAI machine learning trading"
  - "Binance/Bybit/Kraken automated bot"
  - "Telegram trading bot"
tags: [freqtrade, crypto, trading-bot, backtesting, hyperopt, FreqAI, Binance, Bybit, Python, Telegram, ML]
kind: framework
category: crypto-defi-trading

---

## What Is Freqtrade?

Free open-source Python crypto trading bot with full backtesting and ML optimization.
- Repo: https://github.com/freqtrade/freqtrade
- Python: 3.11+
- Requirements: 2GB RAM, 1GB disk, 2vCPU
- Control: Telegram · WebUI · CLI

---

## Supported Exchanges

| Type | Exchanges |
|------|-----------|
| **Spot** | Binance · Kraken · Gate.io · OKX · Bybit · Kucoin · Bitvavo |
| **Futures** | Binance · Bitget · Gate.io · OKX · Bybit |

---

## Installation

```bash
# Docker (recommended)
docker compose up -d

# pip install
pip install freqtrade
freqtrade install-ui   # optional WebUI

# From source
git clone https://github.com/freqtrade/freqtrade
cd freqtrade
./setup.sh -i
```

---

## CLI Commands

```bash
# Create new strategy template
freqtrade new-strategy --strategy MyStrategy

# Run backtesting
freqtrade backtesting --strategy MyStrategy --timerange 20240101-20241231

# Hyperopt (ML parameter search)
freqtrade hyperopt --strategy MyStrategy --hyperopt-loss SharpeHyperOptLoss --epochs 500

# Paper trading (dry run)
freqtrade trade --strategy MyStrategy --dry-run

# Live trading
freqtrade trade --strategy MyStrategy

# Plot strategy signals
freqtrade plot-dataframe --strategy MyStrategy
```

---

## Strategy Structure

```python
from freqtrade.strategy import IStrategy, DecimalParameter, IntParameter
import pandas as pd
from pandas import DataFrame
import talib.abstract as ta

class MyStrategy(IStrategy):
    # Required settings
    minimal_roi = {"0": 0.10, "30": 0.05, "60": 0.01}
    stoploss = -0.05
    timeframe = "1h"

    # Hyperopt parameters (searchable)
    rsi_period = IntParameter(10, 30, default=14, space="buy")
    rsi_buy    = IntParameter(20, 40, default=30, space="buy")
    rsi_sell   = IntParameter(60, 80, default=70, space="sell")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["rsi"]  = ta.RSI(dataframe, timeperiod=self.rsi_period.value)
        dataframe["macd"], dataframe["macdsignal"], _ = ta.MACD(dataframe)
        dataframe["ema20"] = ta.EMA(dataframe, timeperiod=20)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe["rsi"] < self.rsi_buy.value) &
            (dataframe["close"] > dataframe["ema20"]),
            "enter_long"
        ] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            dataframe["rsi"] > self.rsi_sell.value,
            "exit_long"
        ] = 1
        return dataframe
```

---

## Hyperopt (ML Parameter Search)

```bash
# Optimize entry/exit parameters
freqtrade hyperopt \
  --strategy MyStrategy \
  --hyperopt-loss SharpeHyperOptLoss \
  --spaces buy sell \
  --epochs 300

# Loss functions available:
# SharpeHyperOptLoss    → maximize Sharpe ratio
# SortinoHyperOptLoss   → maximize Sortino ratio
# CalmarHyperOptLoss    → maximize Calmar ratio
# MaxDrawDownHyperOptLoss → minimize drawdown
```

---

## FreqAI (Adaptive ML Strategies)

```python
# config.json — enable FreqAI
{
  "freqai": {
    "enabled": true,
    "purge_old_models": 2,
    "train_period_days": 30,
    "backtest_period_days": 7,
    "feature_parameters": {
      "include_timeframes": ["5m", "15m", "1h"],
      "include_corr_pairlist": ["BTC/USDT", "ETH/USDT"],
      "label_period_candles": 24,
      "include_shifted_candles": 2
    },
    "identifier": "my_model",
    "model_training_parameters": {
      "n_estimators": 200,
      "learning_rate": 0.05
    }
  }
}
```

```python
# In strategy: use FreqAI predictions
class FreqAIStrategy(IStrategy):
    def populate_indicators(self, df, metadata):
        df = self.freqai.start(df, metadata, self)  # runs ML model
        return df

    def populate_entry_trend(self, df, metadata):
        df.loc[df["&-s_close"] > 0.02, "enter_long"] = 1  # predict +2% close
        return df
```

---

## Backtesting Results

```bash
# Key metrics in backtesting output:
# Total profit % · Win rate · Avg profit per trade
# Max drawdown · Sharpe ratio · Sortino ratio
# Calmar ratio · Profit factor · Avg duration

freqtrade backtesting --strategy MyStrategy \
  --timerange 20240101-20241231 \
  --export trades \
  --export-filename results.json
```

---

## Telegram Commands

```
/start      → start trading
/stop       → stop trading
/status     → show open trades
/profit     → show P&L summary
/balance    → show portfolio
/performance → strategy performance
/forceenter BTC/USDT → force buy
/forceexit 1 → force close trade #1
```



---
# KNOWLEDGE INJECTION: pysystemtrade (Rob Carver)
# Source: https://github.com/pst-group/pysystemtrade
# Routed to: trading.md - risk-and-portfolio / backtesting-sim
# Date: 2026-03-17

# SKILL: pysystemtrade
name: pysystemtrade
description: >
  pysystemtrade - Rob Carvers open-source futures trading system implementing
  Systematic Trading book framework. Backtesting + live trading via Interactive
  Brokers (IB insync). Production system traded 20h/day by the author.
  Risk management, position sizing, futures data management, Python 3.
USE FOR:
  - systematic futures trading Python
  - Rob Carver pysystemtrade
  - backtesting futures with position sizing
  - live futures trading Interactive Brokers
  - Systematic Trading book implementation
tags: [pysystemtrade, futures, systematic-trading, Rob-Carver, IB, backtesting, position-sizing, risk]
kind: framework
category: backtesting-sim

---

## What Is pysystemtrade?

Rob Carvers open-source implementation of the Systematic Trading framework.
- Repo: https://github.com/pst-group/pysystemtrade
- Live trading: Interactive Brokers (IB insync)
- Author trades it live 20h/day - production-grade
- Books: Systematic Trading, Leveraged Trader, Advanced Futures Trading

### Installation
git clone https://github.com/pst-group/pysystemtrade
cd pysystemtrade
pip install -r requirements.txt
python setup.py install

### Core Concepts (Rob Carver Framework)
Instrument selection - futures with sufficient liquidity and diversification
Rule signals - trend-following, carry, mean-reversion signals
Forecast scaling - normalize signals to +/-20 range
Forecast combination - blend multiple signals with weights
Position sizing - use volatility targeting (% annual risk per instrument)
Portfolio construction - diversification multiplier across instruments

### Volatility Targeting (Key Concept)
target_vol = 0.25  # 25% annual portfolio volatility
instrument_vol = price * daily_vol * sqrt(256)  # annualized
notional_exposure = (capital * target_vol) / instrument_vol
contracts = notional_exposure / point_value
# Result: size positions by risk, not by price

### Trend Following Signal
import pysystemtrade as pst
from sysquant.estimators.ewm import ewmac

# EWMAC crossover (Exponentially Weighted Moving Average Crossover)
raw_signal = ewmac(price, Lfast=16, Lslow=64)
scaled_forecast = raw_signal.clip(-20, 20) * forecast_scalar

# Combine multiple EWMAC speeds
forecasts = {
  ewmac_2_8: weight_0.15,
  ewmac_4_16: weight_0.15,
  ewmac_8_32: weight_0.15,
  ewmac_16_64: weight_0.30,
  ewmac_32_128: weight_0.25
}
combined_forecast = sum(f * w for f, w in forecasts.items())

### Risk Management Rules
1. Never risk more than 2% of capital per instrument per year (volatility target)
2. Diversification multiplier caps total portfolio leverage
3. IDM (instrument diversification multiplier) scales up when correlation is low
4. Position limits: never exceed 1/3 of daily volume
5. Buffering: avoid trading if new position within N% of current

### Live Trading (IB Integration)
from sysbrokers.IB.ib_connection import ibConnection
from sysbrokers.IB.ib_futures_contracts_data import ibFuturesContractData

connection = ibConnection()
# System runs daily: checks positions, generates orders, submits to IB


---
# KNOWLEDGE INJECTION: FinRL-Trading v2.0
# Source: https://github.com/AI4Finance-Foundation/FinRL-Trading
# Routed to: trading.md - ml-trading / quant-ml-trading
# Date: 2026-03-17

# SKILL: finrl-trading
name: finrl-trading
description: >
  FinRL-Trading v2.0 - modular quant trading platform with ML strategies,
  professional backtesting, live trading via Alpaca. Strategies: Equal Weight,
  Market Cap Weighted, Random Forest stock selection, Sector Neutral ML.
  Data: Yahoo Finance, FMP, WRDS. Python 3.11+.
USE FOR:
  - FinRL reinforcement learning trading
  - ML stock selection strategy
  - Alpaca paper/live trading Python
  - modular quant trading platform
  - Random Forest stock selection
tags: [FinRL, RL, ML, trading, Alpaca, Random-Forest, backtesting, quant, Python]
kind: framework
category: ml-trading

---

## What Is FinRL-Trading?

Modular quant trading platform by AI4Finance Foundation.
- Repo: https://github.com/AI4Finance-Foundation/FinRL-Trading
- Version: v2.0
- Broker: Alpaca (paper + live)
- Python: 3.11+

### Implemented Strategies
Equal Weight - buy all S&P500 stocks equally weighted
Market Cap Weighted - weight by market capitalization
Random Forest ML - ML-based stock selection (scikit-learn)
Sector Neutral ML - ML selection with sector exposure control
Deep RL (roadmap) - PPO/DQN agents (planned)

### Installation
git clone https://github.com/AI4Finance-Foundation/FinRL-Trading
pip install -r requirements.txt
cp .env.example .env
# Add Alpaca keys + optional FMP key

### Quick Start
jupyter notebook examples/FinRL_Full_Workflow.ipynb

### Data Sources
Yahoo Finance - free default (yfinance)
Financial Modeling Prep (FMP) - paid, higher quality
WRDS - academic dataset (requires credentials)

### ML Stock Selection Pattern
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit

# Feature engineering
features = [return_1m, return_3m, return_6m, volume_ratio, pe_ratio, pb_ratio]

# Train RF on historical data
model = RandomForestClassifier(n_estimators=200, random_state=42)
tscv = TimeSeriesSplit(n_splits=5)

for train_idx, val_idx in tscv.split(X):
    model.fit(X[train_idx], y[train_idx])

# Score stocks and select top N
scores = model.predict_proba(X_current)[:, 1]
top_50 = pd.Series(scores, index=tickers).nlargest(50).index

### Alpaca Live Trading
import alpaca_trade_api as tradeapi

api = tradeapi.REST(ALPACA_KEY, ALPACA_SECRET, base_url="https://paper-api.alpaca.markets")

for ticker, weight in portfolio.items():
    equity = float(api.get_account().equity)
    target_value = equity * weight
    current_price = api.get_last_trade(ticker).price
    qty = int(target_value / current_price)
    api.submit_order(symbol=ticker, qty=qty, side="buy", type="market", time_in_force="day")


---
# KNOWLEDGE INJECTION: Algorithmic Trading Python (Nick McCullum / FreeCodeCamp)
# Source: https://github.com/nickmccullum/algorithmic-trading-python
# Routed to: trading.md - backtesting-sim / ml-trading
# Date: 2026-03-17

## Algorithmic Trading Python - Strategy Reference

Three production-quality strategies using IEX Cloud API:

### Strategy 1: Equal-Weight S&P 500 Index Fund
Allocate equal capital to all 500 S&P 500 components.

import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math

# Get S&P 500 tickers
stocks = pd.read_csv("sp_500_stocks.csv")

# For each stock: fetch price + market cap via IEX Cloud
IEX_CLOUD_API_TOKEN = "YOUR_TOKEN"
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# Batch API calls (100 stocks per call)
symbol_groups = list(chunks(stocks["Ticker"], 100))
for group in symbol_groups:
    batch_url = f"https://sandbox.iexapis.com/stable/stock/market/batch/?types=quote&symbols={','.join(group)}&token={IEX_CLOUD_API_TOKEN}"
    data = requests.get(batch_url).json()

# Calculate position sizes
portfolio_size = 10_000_000  # 0M
position_size = portfolio_size / len(stocks)
num_shares = math.floor(position_size / price)


### Strategy 2: Quantitative Momentum Strategy
Select top 50 momentum stocks from S&P 500.

Metrics used:
  1-month return (25% weight)
  3-month return (25% weight)
  6-month return (25% weight)
  12-month return (25% weight)

# Composite momentum score (HQM = High Quality Momentum)
hqm_columns = [
    "One-Year Price Return",
    "Six-Month Price Return",
    "Three-Month Price Return",
    "One-Month Price Return"
]

for row in hqm_dataframe.index:
    momentum_percentiles = []
    for time_period in hqm_columns:
        hqm_dataframe.loc[row, f"{time_period} Percentile"] = stats.percentileofscore(
            hqm_dataframe[time_period], hqm_dataframe.loc[row, time_period]
        ) / 100

    hqm_dataframe.loc[row, "HQM Score"] = mean(momentum_percentiles)

# Select top 50 by HQM Score
hqm_dataframe.sort_values("HQM Score", ascending=False, inplace=True)
hqm_dataframe = hqm_dataframe[:50]


### Strategy 3: Quantitative Value Strategy
Select top 50 value stocks using composite value score (RV Score).

Metrics used (each 20% weight):
  Price-to-Earnings (P/E) ratio
  Price-to-Book (P/B) ratio
  Price-to-Sales (P/S) ratio
  Enterprise Value / EBITDA
  Enterprise Value / Gross Profit

# RV = Robust Value Score (percentile average across all 5 metrics)
rv_columns = ["Price-to-Earnings Ratio", "Price-to-Book Ratio",
              "Price-to-Sales Ratio", "EV/EBITDA", "EV/GP"]

for row in rv_dataframe.index:
    value_percentiles = []
    for metric in rv_columns:
        rv_dataframe.loc[row, f"{metric} Percentile"] = stats.percentileofscore(
            rv_dataframe[metric], rv_dataframe.loc[row, metric]
        ) / 100
        value_percentiles.append(rv_dataframe.loc[row, f"{metric} Percentile"])
    rv_dataframe.loc[row, "RV Score"] = mean(value_percentiles)

rv_dataframe.sort_values("RV Score", ascending=False, inplace=True)
rv_dataframe = rv_dataframe[:50]


### Key Libraries
requests  - API calls to IEX Cloud
pandas    - data manipulation
numpy     - math operations
scipy.stats.percentileofscore - percentile ranking
xlsxwriter - export results to Excel with formatting
math.floor - position sizing calculations


---
# KNOWLEDGE INJECTION: Awesome Crypto Trading Bots (Reference List)
# Source: https://github.com/botcrypto-io/awesome-crypto-trading-bots
# Routed to: trading.md - crypto-defi-trading
# Date: 2026-03-18

## Crypto Trading Bot Ecosystem Reference

### Open-Source Trading Bots
| Bot | Language | Key Feature |
|-----|----------|-------------|
| Freqtrade | Python | Backtesting + hyperopt + FreqAI (in skills) |
| Hummingbot | Python | CEX + DEX market making, 50+ exchanges |
| Superalgos | Node.js | Visual designer + data mining (in skills) |
| OpenTrader | Python | Self-hosted, 100+ exchanges via CCXT |
| Jesse | Python | Crypto strategy framework with backtesting |
| Gekko | Node.js | Simple rule-based bot (legacy) |
| Catalyst | Python | Zipline fork for crypto |
| Krypto-trading-bot | TypeScript | Multi-exchange auto-trader |

### Technical Analysis Libraries
| Library | Language | Indicators |
|---------|----------|-----------|
| pandas-ta | Python | 120+ indicators + utility functions |
| ta-lib | C/Python | 150+ functions (industry standard) |
| technicalindicators | JavaScript | 50+ indicators + candlestick patterns |
| finta | Python | 80+ technical indicators |
| ta | Python | Wrapper around pandas-ta |

### Market Data & Exchange APIs
| Tool | Description |
|------|-------------|
| CCXT | 120+ exchanges, Python/JS/PHP |
| python-binance | Binance API wrapper |
| CoinGecko API | Free historical + current prices |
| CryptoCompare | OHLCV, news, social data |
| Alpaca | US equities + crypto, paper trading |

### Charting / Visualization
| Tool | Description |
|------|-------------|
| TradingView Lightweight Charts | Customizable JS price charts |
| TradingVue.js | Vue.js trading chart component |
| mplfinance | Python candlestick charts |
| plotly | Interactive charts |

### Community Resources
- Freqtrade Discord: discord.gg/freqtrade
- Hummingbot Discord: discord.hummingbot.io
- Awesome list: github.com/botcrypto-io/awesome-crypto-trading-bots

