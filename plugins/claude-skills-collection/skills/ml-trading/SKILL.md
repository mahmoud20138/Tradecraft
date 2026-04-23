---
name: ml-trading
description: "Machine learning for trading — supervised classification/regression (XGBoost, LSTM), feature engineering, unsupervised regime detection (K-Means, HMM), reinforcement learning (PPO), NLP sentiment, and time-series cross-validation. Use for ML trading, machine learning, feature engineering, XGBoost, LSTM, or any ML-based trading model development."
kind: reference
category: trading/quant
status: active
tags: [ml, quant, regime, rl, sentiment, trading]
related_skills: [backtesting-sim, backtest-report-generator, hurst-exponent-dynamics-crisis-prediction, quant-ml-trading, statistics-timeseries]
---

# Machine Learning in Trading

## Table of Contents
1. [Supervised Learning — Classification](#1-supervised-learning--classification)
2. [Supervised Learning — Regression](#2-supervised-learning--regression)
3. [Feature Engineering for Trading](#3-feature-engineering-for-trading)
4. [Unsupervised Learning & Regime Detection](#4-unsupervised-learning--regime-detection)
5. [Reinforcement Learning](#5-reinforcement-learning)
6. [NLP & Sentiment Analysis](#6-nlp--social-sentiment-scraper)
7. [Model Validation for Trading](#7-model-validation-for-trading)

---

## 1. Supervised Learning — Classification

**Goal:** Predict direction (long / short / flat) or probability of an outcome.

### Algorithm Comparison

| Algorithm | Strengths | Weaknesses | Best Use |
|---|---|---|---|
| **Logistic Regression** | Interpretable, fast, baseline | Linear boundaries, no interactions | Baseline, factor scoring |
| **Random Forest** | Handles nonlinearity, robust, OOB error | Slower, memory | General purpose, stable |
| **XGBoost / LightGBM** | Top accuracy, handles missing data | More hyperparams, can overfit | Main workhorse for tabular data |
| **SVM** | Good for small datasets, margin-based | Slow on large data, kernel choice | Small feature sets |
| **LSTM** | Learns sequences, temporal patterns | Needs large data, slow training | Raw OHLCV sequences |
| **GRU** | Faster than LSTM, similar performance | Less interpretable | Sequence modeling |
| **Transformer** | Attention over long sequences | Very data-hungry | High-freq, NLP |
| **1D CNN** | Local pattern detection in time | Fixed receptive field | Chart pattern detection |

### Ensemble Methods

**Voting Ensemble (Soft):**
```python
from sklearn.ensemble import VotingClassifier
ensemble = VotingClassifier(
    estimators=[('rf', rf_model), ('xgb', xgb_model), ('lgb', lgb_model)],
    voting='soft'  # use predicted probabilities
)
```

**Stacking:**
```
Level 1: RF + XGBoost + LSTM → out-of-fold predictions
Level 2: Meta-learner (LogReg or XGBoost) on Level 1 outputs
```

**Blending (simpler stacking):**
```python
blend = 0.4 * model1_proba + 0.35 * model2_proba + 0.25 * model3_proba
```

### XGBoost Configuration for Trading
```python
import xgboost as xgb

model = xgb.XGBClassifier(
    n_estimators=500,
    max_depth=4,           # shallow = less overfit
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    min_child_weight=5,    # minimum samples per leaf
    reg_alpha=0.1,         # L1 regularization
    reg_lambda=1.0,        # L2 regularization
    scale_pos_weight=neg_count/pos_count,  # handle class imbalance
    eval_metric='auc',
    early_stopping_rounds=50
)
model.fit(X_train, y_train, eval_set=[(X_val, y_val)])
```

### LSTM for Price Sequences
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, BatchNormalization

def build_lstm(sequence_length, n_features, n_classes=3):
    model = Sequential([
        LSTM(64, return_sequences=True, input_shape=(sequence_length, n_features)),
        Dropout(0.2),
        LSTM(32, return_sequences=False),
        Dropout(0.2),
        BatchNormalization(),
        Dense(16, activation='relu'),
        Dense(n_classes, activation='softmax')  # Long / Short / Flat
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Input shape: (samples, lookback_days, features)
X = np.array([features[i:i+lookback] for i in range(len(features)-lookback)])
```

---

## 2. Supervised Learning — Regression

**Goal:** Predict magnitude of returns (continuous output).

| Algorithm | Notes |
|---|---|
| **Linear Regression** | Baseline; assumes linear relationships |
| **Ridge (L2)** | Penalizes large coefficients; use when features correlate |
| **Lasso (L1)** | Drives coefficients to zero; automatic feature selection |
| **ElasticNet** | Combines L1 + L2; best of both |
| **Random Forest Regressor** | Non-linear, robust, handles interactions |
| **XGBoost Regressor** | Top performer on tabular data |
| **Neural Network Regressor** | Captures complex non-linearities |

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Pipeline with scaling (critical for Ridge/Lasso)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', Ridge(alpha=1.0))
])

# Cross-validate alpha
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)  # use time-series split, NOT random!
```

**Target Engineering for Regression:**
```python
# Predict forward returns
y_1d  = returns.shift(-1)   # next 1-day return
y_5d  = returns.shift(-5).rolling(5).mean()  # average next 5-day return
y_20d = returns.rolling(20).mean().shift(-20)

# Rank-normalize (reduces impact of extreme returns)
y_ranked = y_1d.rank(pct=True)  # maps to [0,1]
```

---

## 3. Feature Engineering for Trading

### Price-Based Features
```python
# Multi-period returns
for period in [1, 5, 10, 20, 60]:
    df[f'ret_{period}d'] = df['close'].pct_change(period)

# Rolling volatility
for window in [10, 21, 63]:
    df[f'vol_{window}d'] = df['close'].pct_change().rolling(window).std() * np.sqrt(252)

# MA ratios (trend strength)
for ma in [20, 50, 200]:
    df[f'price_ma{ma}_ratio'] = df['close'] / df['close'].rolling(ma).mean()

# Technical indicator values (NOT signals)
df['rsi_14'] = talib.RSI(df['close'], timeperiod=14)
df['macd'], df['macd_signal'], df['macd_hist'] = talib.MACD(df['close'])
df['stoch_k'], df['stoch_d'] = talib.STOCH(df['high'], df['low'], df['close'])

# Bollinger Band position
upper, mid, lower = talib.BBANDS(df['close'], timeperiod=20)
df['bb_pct_b'] = (df['close'] - lower) / (upper - lower)  # 0=at lower, 1=at upper

# ATR normalized
df['atr_pct'] = talib.ATR(df['high'], df['low'], df['close'], 14) / df['close']
```

### Volume-Based Features
```python
# Volume ratio vs. average
df['vol_ratio_20d'] = df['volume'] / df['volume'].rolling(20).mean()

# On-Balance Volume momentum
df['obv'] = talib.OBV(df['close'], df['volume'])
df['obv_slope'] = df['obv'].pct_change(5)

# Volume momentum
df['vol_momentum'] = df['volume'].pct_change(5)

# Dollar volume (liquidity)
df['dollar_vol'] = df['close'] * df['volume']
df['dollar_vol_20d_avg'] = df['dollar_vol'].rolling(20).mean()
```

### Market Structure Features
```python
# Distance from 52-week high/low
df['dist_52wk_high'] = df['close'] / df['high'].rolling(252).max() - 1
df['dist_52wk_low']  = df['close'] / df['low'].rolling(252).min() - 1

# Days since n-period high/low
df['days_since_20d_high'] = df['high'].rolling(20).apply(
    lambda x: (len(x) - 1 - np.argmax(x))
)

# ADX (trend strength, 0-100)
df['adx'] = talib.ADX(df['high'], df['low'], df['close'], timeperiod=14)
df['plus_di'] = talib.PLUS_DI(df['high'], df['low'], df['close'], 14)
df['minus_di'] = talib.MINUS_DI(df['high'], df['low'], df['close'], 14)
```

### Cross-Asset Features
```python
# Sector relative performance
df['sector_rel_perf'] = df['stock_ret_20d'] - df['sector_etf_ret_20d']

# VIX level and change
df['vix_level']  = vix_data['close']
df['vix_change'] = vix_data['close'].pct_change(5)

# Bond yield curve (10yr - 2yr spread)
df['yield_spread'] = tnx - twoyr  # inverted = recession signal

# USD index strength
df['dxy_5d'] = dxy['close'].pct_change(5)

# Risk-on/off regime
df['spy_vix_ratio'] = spy['close'] / vix_data['close']
```

### Time-Based Features
```python
# Calendar features
df['day_of_week'] = df.index.dayofweek       # 0=Mon, 4=Fri
df['month']       = df.index.month
df['quarter']     = df.index.quarter
df['week_of_year'] = df.index.isocalendar().week

# Event proximity (requires earnings calendar)
df['days_to_earnings'] = (next_earnings_date - df.index).days
df['is_options_expiry_week'] = (df.index.weekday == 4) & (df.index.day >= 15) & (df.index.day <= 21)

# Monthly seasonality patterns
# January effect, sell in May, etc.
df['is_january'] = (df.index.month == 1).astype(int)
```

### Feature Selection & Importance
```python
# SHAP values for model interpretability
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)

# Mutual Information for feature screening
from sklearn.feature_selection import mutual_info_classif
mi_scores = mutual_info_classif(X, y, discrete_features=False)
feature_importance = pd.Series(mi_scores, index=feature_names).sort_values(ascending=False)
```

---

## 4. Unsupervised Learning & Regime Detection

### K-Means Regime Detection (4 Regimes)
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Features for regime clustering
regime_features = pd.DataFrame({
    'return_20d': returns.rolling(20).mean(),
    'volatility_20d': returns.rolling(20).std(),
    'trend_strength': adx_values,
    'vix': vix_data
}).dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(regime_features)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
regimes = kmeans.fit_predict(X_scaled)

# Typical 4 regimes:
# 0: Bull Quiet    (positive return, low vol)
# 1: Bear Volatile (negative return, high vol)
# 2: Bear Quiet    (negative return, low vol)
# 3: Bull Volatile (positive return, high vol)
```

### DBSCAN (Density-Based — discovers arbitrary shapes)
```python
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.5, min_samples=5)
labels = db.fit_predict(X_scaled)
# labels == -1 → outliers/anomalies (useful for detecting unusual market days)
```

### Gaussian Mixture Models
```python
from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=3, covariance_type='full', random_state=42)
gmm.fit(regime_features)
# Soft assignment: probability of each regime
regime_proba = gmm.predict_proba(regime_features)  # shape: (n_days, 3)
```

### PCA (Dimensionality Reduction)
```python
from sklearn.decomposition import PCA

# Factor analysis on stock returns (find hidden drivers)
pca = PCA(n_components=10)
pca.fit(returns_matrix)  # rows=dates, cols=stocks

print(pca.explained_variance_ratio_)  # PC1 often = market factor
# PC1 ≈ market, PC2 ≈ growth vs. value, PC3 ≈ interest rate sensitivity

# Use PC scores as features or for decorrelated portfolios
factor_returns = pca.transform(returns_matrix)
```

### Hidden Markov Models
```python
from hmmlearn.hmm import GaussianHMM

# Fit 2-state HMM (bull / bear) on returns + volatility
features = np.column_stack([returns, returns_sq])  # returns and vol proxy
hmm = GaussianHMM(n_components=2, covariance_type='full', n_iter=100)
hmm.fit(features)

# Current regime
current_state = hmm.predict(features)[-1]

# Transition probabilities (persistence of regimes)
# transmat_[i,j] = P(go from regime i to regime j)
print(hmm.transmat_)
```

---

## 5. Reinforcement Learning

### Core Components
| Component | Trading Context | Example |
|---|---|---|
| **State (S)** | Market observation | [prices, features, portfolio, P&L] |
| **Action (A)** | Trading decision | {-1: short, 0: flat, 1: long} or position size |
| **Reward (R)** | Objective signal | Risk-adjusted return, Sharpe increment |
| **Policy (π)** | Strategy | Maps state → action |
| **Environment** | Market simulator | Historical replay or stochastic simulator |

### Reward Function Design
```python
# Simple return reward
reward = portfolio_value_t / portfolio_value_{t-1} - 1

# Sharpe-based reward (encourages consistency)
reward = returns_window.mean() / (returns_window.std() + 1e-8)

# Differential Sharpe (online estimation)
delta_return = current_return - mean_return
reward = delta_return / std_return - 0.5 * (delta_return**2) / std_return**3

# Penalize transaction costs and excessive trading
reward = raw_return - cost_penalty * abs(position_change)
```

### Algorithm Selection
| Algorithm | Type | Best For |
|---|---|---|
| **DQN** | Value-based | Discrete actions (long/short/flat) |
| **REINFORCE** | Policy Gradient | Simple continuous control |
| **A2C / A3C** | Actor-Critic | Parallel training, decent baseline |
| **PPO** | Policy Gradient | Stable training, most widely used |
| **DDPG** | Deterministic PG | Continuous position sizing |
| **SAC** | Soft Actor-Critic | Best continuous control + entropy bonus |

### PPO Implementation (using Stable-Baselines3)
```python
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

# Custom Gym environment
class TradingEnv(gym.Env):
    def __init__(self, df, window=50):
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(window, n_features))
        self.action_space = gym.spaces.Discrete(3)  # 0=sell, 1=hold, 2=buy

model = PPO("MlpPolicy", env, verbose=1,
            learning_rate=3e-4, n_steps=2048,
            batch_size=64, n_epochs=10)
model.learn(total_timesteps=1_000_000)
```

### RL Challenges in Trading
| Challenge | Description | Mitigation |
|---|---|---|
| **Non-stationarity** | Market regime shifts invalidate learned policy | Periodic retraining, meta-learning |
| **Delayed reward** | Position profits/losses accrue over time | Reward shaping, discount factor tuning |
| **Overfitting** | Policy memorizes historical noise | Regularization, dropout, multiple seeds |
| **Regime changes** | Policy fails in unseen market conditions | Train across diverse market periods |
| **Sample inefficiency** | Need millions of samples | Replay buffers, transfer learning |
| **Reward hacking** | Policy exploits sim imperfections | Adversarial testing, realistic costs |

### RL Best Practices
1. **Realistic simulation**: Include bid-ask spreads, partial fills, market impact
2. **Walk-forward testing**: Deploy on rolling out-of-sample windows
3. **Multiple seeds**: Run 5-10 seeds; report mean ± std
4. **Regularization**: L2, dropout, action entropy bonus (encourages exploration)
5. **Normalize observations**: StandardScaler on features
6. **Clip rewards**: Prevents gradient explosion from extreme returns

---

## 6. NLP & Sentiment Analysis

### Data Sources
| Source | Signal Type | Latency | Notes |
|---|---|---|---|
| **Financial News** (Bloomberg, Reuters) | Event-driven | Minutes | Highest quality, paid |
| **Social Media** (Twitter/X, Reddit) | Crowd sentiment | Real-time | Noisy, manipulation risk |
| **Earnings Calls** (transcripts) | Management tone | Same day | Tone change = leading indicator |
| **SEC Filings** (10-K, 10-Q, 8-K) | Risk disclosure changes | Days | Systematic risk signal |
| **Analyst Reports** | Expert opinion | Days | Revision direction matters |

### Analysis Methods

**1. Dictionary-Based (Loughran-McDonald Finance Lexicon)**
```python
import pandas as pd

# Load Loughran-McDonald word lists
lm_positive = set(pd.read_csv('LM_positive.csv')['Word'])
lm_negative = set(pd.read_csv('LM_negative.csv')['Word'])

def lm_sentiment(text):
    words = text.lower().split()
    pos = sum(1 for w in words if w in lm_positive)
    neg = sum(1 for w in words if w in lm_negative)
    score = (pos - neg) / (pos + neg + 1e-8)
    return score
```

**2. ML Classifier (Fine-tuned)**
```python
from transformers import pipeline

# FinBERT — pre-trained on financial text
finbert = pipeline("text-classification",
                   model="ProsusAI/finbert",
                   tokenizer="ProsusAI/finbert")

result = finbert("Company reports record earnings beating expectations")
# → {'label': 'positive', 'score': 0.94}
```

**3. GPT-based Analysis**
```python
import openai

def analyze_earnings_call(transcript_excerpt):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "Analyze earnings call tone. Return JSON: {sentiment: positive/neutral/negative, confidence: 0-1, key_topics: [], management_tone_change: up/flat/down}"
        }, {
            "role": "user",
            "content": transcript_excerpt
        }]
    )
    return response.choices[0].message.content
```

### Engineered Sentiment Features
```python
# Per-asset sentiment score (rolling)
df['sentiment_score']   = sentiment_series.rolling(5).mean()

# Sentiment delta (change in sentiment)
df['sentiment_delta']   = sentiment_series.diff(5)

# Mention volume (buzz / attention)
df['mention_volume']    = mention_count_series
df['mention_vol_ratio'] = mention_count_series / mention_count_series.rolling(20).mean()

# Sentiment dispersion (disagreement signal)
df['sentiment_dispersion'] = sentiment_series.rolling(5).std()
```

### Trading Signals from Sentiment
| Signal Type | Interpretation | Direction |
|---|---|---|
| **Extreme Positive Sentiment** | Euphoria → contrarian sell signal | Counter-trend (short) |
| **Extreme Negative Sentiment** | Capitulation → contrarian buy signal | Counter-trend (long) |
| **Sentiment + Price Divergence** | Bearish sentiment + rising price = weak rally | Short |
| **Unusual Spike in Volume** | Major news event → directional follow-through | With-trend |
| **Earnings Call Tone Change** | Suddenly more cautious vs. last quarter | Sell if neg delta |
| **Accumulation on Bad News** | Price holds despite negative sentiment | Buy |

---

## 7. Model Validation for Trading

### Time-Series Cross-Validation (Critical!)
```python
from sklearn.model_selection import TimeSeriesSplit

# NEVER use random K-fold — introduces look-ahead bias!
tscv = TimeSeriesSplit(n_splits=5, gap=21)  # gap prevents leakage

scores = []
for train_idx, test_idx in tscv.split(X):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    scores.append(score)

print(f"Mean: {np.mean(scores):.3f} ± {np.std(scores):.3f}")
```

### Preventing Data Leakage
```python
# WRONG — uses future data in rolling calculation
df['vol_20d'] = df['close'].pct_change().rolling(20).std()

# CORRECT — use only data available at signal time
df['vol_20d'] = df['close'].pct_change().rolling(20).std().shift(1)

# Feature matrix construction: ensure all features are shifted
feature_cols = ['ret_1d', 'vol_20d', 'rsi_14', ...]
X = df[feature_cols].shift(1)  # all features from previous day
y = df['ret_5d_forward']       # target: next 5-day return
```

### Feature Importance & Model Monitoring
```python
# Track feature importance drift over time (regime shift detector)
monthly_importance = {}
for month in months:
    monthly_model = xgb.fit(X[month], y[month])
    monthly_importance[month] = monthly_model.feature_importances_

importance_df = pd.DataFrame(monthly_importance).T
# Large shifts in importance → regime change → retrain model
```
