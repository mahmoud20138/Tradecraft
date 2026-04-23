---
name: stocksight-sentiment
description: StockSight — open-source stock sentiment analysis using Twitter + news headlines. Elasticsearch storage, Kibana dashboards, NLTK/TextBlob/VADER NLP. Correlates social/news sentiment with price movements. Docker or local install. Asset-agnostic: works
kind: reference
category: trading/data
status: active
tags: [data, news, sentiment, stocksight, trading]
related_skills: [economic-calendar, market-data-ingestion, alternative-data-integrator, economic-indicator-tracker, market-intelligence]
---

# stocksight-sentiment

USE FOR:
  - "Twitter sentiment analysis for stocks"
  - "news headline sentiment pipeline"
  - "Elasticsearch + Kibana sentiment dashboard"
  - "VADER / TextBlob sentiment scoring for trading"
  - "social media signal for trading"
  - "correlate sentiment with price"
tags: [sentiment, Twitter, news, NLP, Elasticsearch, Kibana, VADER, TextBlob, NLTK, social-media, stocks]
kind: tool
category: market-intelligence

---

## What Is StockSight?

Open-source sentiment analysis platform correlating Twitter + news sentiment with stock price.
- Repo: https://github.com/shirosaidev/stocksight
- Stack: Python 3 + Elasticsearch 5 + Kibana 5
- NLP: NLTK, TextBlob, VADER
- Asset-agnostic: designed for stocks, works for crypto too

---

## Architecture

```
Twitter API       →  tweepy collector  ─┐
Financial News    →  newspaper3k/BS4  ──┤→ Sentiment Scoring → Elasticsearch → Kibana
Web pages (links) →  optional deep     ─┘   (NLTK/TextBlob/VADER)             Dashboards
                                                   ↕
                                           stockprice.py
                                        (price correlation)
```

---

## Installation

### Docker (Recommended)
```bash
git clone https://github.com/shirosaidev/stocksight
cd stocksight
docker-compose up -d    # Spins up ES + Kibana + stocksight
```

### Local
```bash
pip install tweepy beautifulsoup4 newspaper3k nltk textblob elasticsearch
# Also requires: Elasticsearch 5.x + Kibana 5.x running locally
```

---

## Configuration

```yaml
# config/stocksight.cfg
[twitter]
keywords = TSLA, Tesla, Elon Musk
whitelist = buy, bullish, moon, long
blacklist = spam, follow, RT

[stocks]
symbol = TSLA
```

---

## Usage

```bash
# Collect Twitter sentiment for TSLA
python stocksight.py -s TSLA -t "Tesla, TSLA" -l

# Track a specific Twitter user's feed
python stocksight.py -s TSLA -u elonmusk

# Collect with deep web page analysis
python stocksight.py -s TSLA -t "Tesla" --web

# Add price data
python stockprice.py -s TSLA
```

---

## NLP Sentiment Pipeline

```python
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# TextBlob polarity
blob = TextBlob(tweet_text)
polarity = blob.sentiment.polarity  # -1.0 to +1.0

# VADER compound score (better for social media)
vader = SentimentIntensityAnalyzer()
scores = vader.polarity_scores(tweet_text)
compound = scores["compound"]  # -1.0 to +1.0

# Classification
if compound >= 0.05:
    sentiment = "POSITIVE"
elif compound <= -0.05:
    sentiment = "NEGATIVE"
else:
    sentiment = "NEUTRAL"
```

---

## Kibana Dashboard

After data collection, Kibana (localhost:5601) shows:
- Sentiment trend over time (line chart)
- Tweet volume by sentiment class
- Sentiment vs. price overlay
- Top keywords driving positive/negative sentiment
- Hourly/daily sentiment distribution

---

## Extending to Crypto / Other Assets

```python
# Works for any keyword-based asset
python stocksight.py -s BTC -t "Bitcoin, BTC, crypto" -l
python stocksight.py -s ETH -t "Ethereum, ETH, DeFi" -l
```

---

## Sentiment → Trading Signal Pattern

```
Compound Score  │  Signal
────────────────┼──────────────
> +0.3          │  Strong BUY signal
+0.05 to +0.3   │  Weak BUY
-0.05 to +0.05  │  NEUTRAL / hold
-0.05 to -0.3   │  Weak SELL
< -0.3          │  Strong SELL signal

Volume spike + strong sentiment → high-conviction signal
```


---
# ── KNOWLEDGE INJECTION: Stock Prediction (alisonmitchell) ──
# Source: https://github.com/alisonmitchell/Stock-Prediction
# Routed to: trading.md → ml-trading / statistics-timeseries
# Date: 2026-03-17

# ── KNOWLEDGE INJECTION: ML Stock Prediction Reference ──

## ML Model Reference for Stock Price Prediction

Research project on FTSE 100 top-6 stocks combining:
- Time series forecasting
- Deep learning sequence models
- Classical ML classifiers
- NLP sentiment features

### Model Taxonomy

#### Time Series / Statistical
| Model | Use Case | Notes |
|-------|----------|-------|
| ARIMA | Short-horizon price forecast | Needs stationarity (differencing) |
| SARIMA | ARIMA + seasonal component | Good for weekly/monthly patterns |
| Facebook Prophet | Trend + seasonality decomposition | Handles holidays, robust to missing data |
| Moving Averages | Baseline trend | SMA, EMA — simple but interpretable |

#### Deep Learning Sequence Models
| Model | Use Case | Notes |
|-------|----------|-------|
| LSTM | Long-term temporal dependencies | Standard for price sequences |
| GRU | LSTM-lite, faster training | Similar performance, fewer params |
| Simple RNN | Baseline seq model | Vanishing gradient limits depth |

#### Classical ML (Classification / Regression)
| Model | Use Case | Notes |
|-------|----------|-------|
| Gradient Boosting | Direction prediction | XGBoost/LightGBM variants preferred |
| Gaussian Naive Bayes | Fast baseline classifier | Good with sentiment features |

#### NLP Sentiment Tools
| Tool | Approach | Best For |
|------|----------|----------|
| VADER | Rule-based lexicon | Social media, short texts |
| TextBlob | Pattern-based | Quick polarity scoring |
| BERT | Contextual embeddings | Financial news (FinBERT variant) |
| SpaCy | NER + entity linking | Extract company/ticker mentions |
| Gensim | Topic modeling (LDA) | News theme extraction |

### Feature Engineering Reference

```python
import pandas as pd
import talib  # or pandas-ta

# Core price features
df["returns"] = df["Adj Close"].pct_change()
df["log_returns"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))

# Technical indicators
df["MACD"], df["MACD_signal"], _ = talib.MACD(df["Adj Close"])
df["RSI"] = talib.RSI(df["Adj Close"], timeperiod=14)
df["BB_upper"], df["BB_mid"], df["BB_lower"] = talib.BBANDS(df["Adj Close"])
df["STOCH_k"], df["STOCH_d"] = talib.STOCH(df["High"], df["Low"], df["Close"])
df["MFI"] = talib.MFI(df["High"], df["Low"], df["Close"], df["Volume"])
df["ROC"] = talib.ROC(df["Adj Close"], timeperiod=10)
df["OBV"] = talib.OBV(df["Close"], df["Volume"])
```

### Critical ML Anti-Pattern: Data Leakage

```python
# WRONG — random split causes look-ahead bias
from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)  # ❌

# CORRECT — time-based split
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)
for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X[train_idx], X[test_idx]  # ✓

# BEST — walk-forward validation
# Each fold: train on past, predict next N days, advance window
```

### Framing: Regression vs Classification

```python
# Regression: predict price or return magnitude
y = df["Adj Close"].shift(-1)               # Next day price
y = df["returns"].shift(-1)                  # Next day return

# Classification: predict direction
y = (df["returns"].shift(-1) > 0).astype(int)  # 1=up, 0=down
# or 3-class: 1=up, 0=flat, -1=down
y = np.where(df["returns"].shift(-1) > threshold, 1,
    np.where(df["returns"].shift(-1) < -threshold, -1, 0))
```


---
