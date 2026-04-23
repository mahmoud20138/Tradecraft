---
name: statistics-timeseries
description: >
  Statistical analysis and time series modeling for trading: regime detection, probability modeling,
  edge validation, correlation modeling, distribution analysis, hypothesis testing, ARIMA models,
  stationarity testing, autocorrelation analysis.
  USE FOR: regime detection, edge validation, win rate analysis, expectancy,
  probability of profit, distribution analysis, normal distribution, fat tails,
  Sharpe ratio calculation, statistical significance, hypothesis testing, Monte Carlo simulation,
  correlation, R-squared, beta, alpha, time series, ARIMA, ADF test, cointegration,
  descriptive statistics, return distributions, stationarity.
related_skills:
  - backtesting-sim
  - quant-ml-trading
  - risk-and-portfolio
  - market-regime-classifier
tags:
  - trading
  - quant
  - statistics
  - timeseries
  - edge-validation
kind: reference
category: trading/quant
status: active
---

# Statistical Foundations & Time Series Analysis

## Table of Contents
1. [Descriptive Statistics](#1-descriptive-statistics)
2. [Financial Return Distributions](#2-financial-return-distributions)
3. [Time Series Stationarity](#3-time-series-stationarity)
4. [Autocorrelation Analysis](#4-autocorrelation-analysis)
5. [ARIMA Models](#5-arima-models)
6. [GARCH Volatility Models](#6-garch-volatility-models)
7. [Regression Analysis](#7-regression-analysis)
8. [Factor Models](#8-factor-models)

---

## 1. Descriptive Statistics

### Central Tendency
| Measure | Formula | Trading Use |
|---|---|---|
| **Mean (μ)** | `Σx / n` | Average return |
| **Median** | Middle value | Robust to outliers; preferred for skewed returns |
| **Mode** | Most frequent | Price clustering levels |

### Dispersion
| Measure | Formula | Trading Use |
|---|---|---|
| **Variance (σ²)** | `Σ(x - μ)² / (n-1)` | Risk measure |
| **Std Dev (σ)** | `√Variance` | Annualized: `σ_daily × √252` |
| **Range** | `Max - Min` | Volatility proxy |
| **IQR** | `Q3 - Q1` | Robust dispersion |

### Shape Statistics

**Skewness** — asymmetry of distribution:
- **Positive skew (right tail)**: Long tail to right; mean > median; less common in equity returns
- **Negative skew (left tail)**: Long tail to left; mean < median; **typical for equity returns** (crash risk)
- Formula: `Σ((x - μ)³/σ³) / n`
- Rule of thumb: |skew| > 0.5 is significant for trading

**Kurtosis** — tail heaviness vs. normal distribution:
- **Leptokurtic** (excess kurtosis > 0): **Fat tails** — more extreme events than normal; typical for financial returns
- **Mesokurtic** (excess kurtosis = 0): Normal distribution (kurtosis = 3)
- **Platykurtic** (excess kurtosis < 0): Thin tails — fewer extremes than normal
- Formula: `Σ((x - μ)⁴/σ⁴) / n` (excess = this - 3)

---

## 2. Financial Return Distributions

### How Financial Returns Differ from Normal

Financial returns are **NOT normally distributed**. Key violations:

| Property | Normal Assumption | Reality |
|---|---|---|
| **Tails** | Thin, 3σ events rare | **Fat tails** — 5σ+ events happen regularly |
| **Skewness** | Symmetric (0) | **Negative skew** — crashes are larger than rallies |
| **Clustering** | Constant variance | **Volatility clustering** — calm periods follow calm |
| **Autocorrelation** | None | Returns: near zero; Volatility: high persistence |

### Return Calculation Methods
```python
# Simple returns
R_t = (P_t - P_{t-1}) / P_{t-1}

# Log returns (preferred for compounding, stationarity)
r_t = ln(P_t / P_{t-1}) = ln(P_t) - ln(P_{t-1})

# Annualization
Annual_Return = (1 + Daily_Return)^252 - 1  # simple
Annual_Return = Daily_Return × 252           # log returns
```

### Why This Matters
- **VaR underestimates risk** if based on normality assumption
- **Black-Scholes misprices** options at far strikes due to fat tails
- **Position sizing** must account for fat tails (use CVaR/Expected Shortfall)
- Use **t-distribution** (ν ≈ 3–5 df) or empirical distributions for risk modeling

---

## 3. Time Series Stationarity

### Definition
A **stationary** time series has constant statistical properties over time:
- Constant mean: `E[X_t] = μ` for all t
- Constant variance: `Var(X_t) = σ²` for all t
- Autocovariance depends only on lag, not time: `Cov(X_t, X_{t+k}) = f(k)`

**Why it matters:** Most statistical models (ARIMA, regression) assume stationarity. Non-stationary series produce spurious correlations.

### Types of Non-Stationarity
| Type | Example | Fix |
|---|---|---|
| **Trend** | Stock price level | First-difference or detrend |
| **Unit Root** | Random walk | First-difference |
| **Seasonality** | Monthly patterns | Seasonal differencing |
| **Structural Break** | Regime change | Dummy variables or subsample |

### Stationarity Tests

#### Augmented Dickey-Fuller (ADF)
- **H₀**: Unit root present (non-stationary)
- **H₁**: No unit root (stationary)
- **Reject H₀** (p < 0.05) → series is stationary
```python
from statsmodels.tsa.stattools import adfuller
result = adfuller(series, autolag='AIC')
# result[1] is the p-value
```

#### KPSS Test (Kwiatkowski-Phillips-Schmidt-Shin)
- **H₀**: Series is stationary (opposite of ADF!)
- **H₁**: Unit root (non-stationary)
- **Reject H₀** (p < 0.05) → series is non-stationary
- Use alongside ADF; conflicting results suggest trend-stationarity

#### Phillips-Perron (PP)
- Similar to ADF but uses non-parametric correction for serial correlation
- More robust to heteroskedasticity

#### Interpretation Matrix
| ADF result | KPSS result | Conclusion |
|---|---|---|
| Reject H₀ | Don't reject H₀ | **Stationary** ✓ |
| Don't reject H₀ | Reject H₀ | **Non-stationary** (unit root) |
| Reject H₀ | Reject H₀ | **Trend-stationary** |
| Don't reject H₀ | Don't reject H₀ | **Ambiguous** |

### Making Series Stationary
```python
# First differencing (removes random walk / linear trend)
d1_series = series.diff().dropna()

# Log transformation (stabilizes variance)
log_series = np.log(series)

# Log-differencing (returns series — most common for prices)
returns = np.log(series).diff().dropna()

# Seasonal differencing
seasonal_diff = series.diff(12)  # monthly with annual seasonality
```

---

## 4. Autocorrelation Analysis

### ACF (Autocorrelation Function)
Measures correlation between series and its own lagged values:
```
ACF(k) = Cov(X_t, X_{t-k}) / Var(X_t)
```
- **Significance band**: ±1.96/√n (95% confidence)
- ACF values outside band → statistically significant autocorrelation at that lag

### PACF (Partial Autocorrelation Function)
Correlation at lag k after removing effects of all shorter lags.

### Patterns and Model Identification
| Pattern | ACF | PACF | Suggests |
|---|---|---|---|
| AR(p) | Decays gradually | Cuts off at lag p | AR model of order p |
| MA(q) | Cuts off at lag q | Decays gradually | MA model of order q |
| ARMA(p,q) | Decays gradually | Decays gradually | ARMA model |
| No pattern | Within bounds | Within bounds | White noise (no signal) |

### Ljung-Box Test
Tests whether group of autocorrelations ≠ 0:
- **H₀**: Data is independently distributed (white noise)
- **Reject H₀** (p < 0.05) → significant autocorrelation present

---

## 5. ARIMA Models

### Components
- **AR(p)** — Autoregressive: current value depends on past p values
  - `X_t = c + φ₁X_{t-1} + φ₂X_{t-2} + ... + φₚX_{t-p} + ε_t`
- **I(d)** — Integrated: number of differences needed for stationarity
- **MA(q)** — Moving Average: current value depends on past q error terms
  - `X_t = μ + ε_t + θ₁ε_{t-1} + θ₂ε_{t-2} + ... + θ_qε_{t-q}`

**Full ARIMA(p,d,q):**
```
ARIMA(1,1,1): ΔX_t = c + φ₁ΔX_{t-1} + θ₁ε_{t-1} + ε_t
```

### ARIMA Modeling Process (Step-by-Step)

**Step 1 — Check stationarity:**
```python
from statsmodels.tsa.stattools import adfuller
p_value = adfuller(series)[1]
# If p_value > 0.05, series is non-stationary → difference
```

**Step 2 — Difference if needed (determine d):**
```python
d = 0
while adfuller(series.diff(d if d > 0 else 1).dropna())[1] > 0.05:
    d += 1
stationary_series = series.diff(d).dropna() if d > 0 else series
```

**Step 3 — Plot ACF and PACF to identify p, q:**
```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(stationary_series, lags=40)
plot_pacf(stationary_series, lags=40)
```

**Step 4 — Fit ARIMA (or use auto_arima):**
```python
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

# Manual fit
model = ARIMA(series, order=(p, d, q)).fit()

# Auto-select order
auto_model = auto_arima(series, seasonal=False, stepwise=True, information_criterion='aic')
```

**Step 5 — Validate residuals (should be white noise):**
```python
from statsmodels.stats.diagnostic import acorr_ljungbox
lb_test = acorr_ljungbox(model.resid, lags=[10], return_df=True)
# p_value > 0.05 → residuals are white noise ✓
```

**Step 6 — Forecast:**
```python
forecast = model.forecast(steps=5)
conf_int = model.get_forecast(steps=5).conf_int()
```

### Model Selection Criteria
- **AIC** (Akaike): `2k - 2ln(L)` — penalizes complexity; prefer lower
- **BIC** (Bayesian): `k·ln(n) - 2ln(L)` — stronger penalty; prefer lower
- **AIC vs BIC**: AIC for prediction; BIC for model identification

### ARIMA in Trading Context
- Returns series are usually near-white-noise (weak ARIMA signal)
- Better for: volatility, spreads, alternative data with predictable patterns
- ARIMA forecasts are baselines; combine with ML for stronger signals

---

## 6. GARCH Volatility Models

### Why GARCH?
Standard ARIMA assumes constant variance (homoskedasticity). Financial returns show **volatility clustering** — calm periods followed by turbulent ones. GARCH models this explicitly.

### GARCH(1,1) Formula
```
Return equation:  r_t = μ + ε_t,   where ε_t = σ_t · z_t,  z_t ~ N(0,1)

Variance equation: σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}

Constraints:
  ω > 0  (long-run variance weight)
  α ≥ 0  (ARCH effect — yesterday's shock)
  β ≥ 0  (GARCH effect — yesterday's variance)
  α + β < 1  (stationarity; sum close to 1 = high persistence)
```

**Unconditional (long-run) variance:** `σ²_LR = ω / (1 - α - β)`

### GARCH Variants

| Model | Key Feature | Use Case |
|---|---|---|
| **GARCH(1,1)** | Symmetric, baseline | General volatility modeling |
| **EGARCH** | Asymmetric, log-variance | Leverage effect (bad news > good news) |
| **GJR-GARCH** | Asymmetric with indicator | Separate up/down volatility |
| **TGARCH** (TARCH) | Threshold-based asymmetry | Regime-specific vol estimation |
| **GARCH-M** | Vol in mean equation | Risk-return premium |
| **DCC-GARCH** | Dynamic correlation | Portfolio correlation modeling |

**GJR-GARCH(1,1):**
```
σ²_t = ω + (α + γ·I_{t-1})·ε²_{t-1} + β·σ²_{t-1}
where I_{t-1} = 1 if ε_{t-1} < 0 (leverage effect indicator)
```

### Python Implementation
```python
from arch import arch_model

# GARCH(1,1)
am = arch_model(returns * 100, vol='Garch', p=1, q=1)
res = am.fit(disp='off')

# Get conditional volatility forecast
vol_forecast = res.forecast(horizon=5)
next_day_vol = vol_forecast.variance.values[-1][0] ** 0.5 / 100

# EGARCH
am_eg = arch_model(returns * 100, vol='EGARCH', p=1, q=1)
```

### Trading Applications
- **Options pricing**: Use GARCH vol instead of historical vol for better pricing
- **Risk management**: Dynamic VaR based on conditional volatility
- **Position sizing**: Scale positions inversely with GARCH forecast volatility
- **Regime detection**: High σ_t → reduce exposure; Low σ_t → increase
- **Vol surface**: Calibrate term structure of implied vs. GARCH realized vol

---

## 7. Regression Analysis

### Simple Linear Regression
```
Y = α + β·X + ε
```
- **α (alpha/intercept)**: Y value when X = 0; in finance, excess return vs. benchmark
- **β (beta/slope)**: Change in Y per unit change in X; market exposure/sensitivity
- **ε (residual)**: Unexplained variation; should be white noise
- **R²**: Fraction of variance explained; `R² = 1 - SS_res/SS_tot`

```python
import statsmodels.api as sm
X = sm.add_constant(X_data)
model = sm.OLS(y_data, X).fit()
print(model.summary())  # alpha, beta, t-stats, R², F-stat
```

### OLS Assumptions (BLUE)
1. Linearity
2. No perfect multicollinearity
3. Zero mean errors
4. Homoskedasticity (constant variance) — test: Breusch-Pagan
5. No autocorrelation in errors — test: Durbin-Watson
6. Normality of errors (for inference)

### Interpreting Alpha (Jensen's Alpha)
```
R_p - R_f = α + β·(R_m - R_f)
```
- α > 0: Portfolio outperforms risk-adjusted benchmark (true skill)
- α = 0: Performance explained entirely by market exposure
- α < 0: Underperformance after risk adjustment
- **Statistical significance**: t-stat > 2, p-value < 0.05

---

## 8. Factor Models

### Fama-French 3-Factor Model
```
R_i - R_f = α + β₁·(R_m - R_f) + β₂·SMB + β₃·HML + ε
```
| Factor | Definition | Economic Rationale |
|---|---|---|
| **Rm - Rf** | Market excess return | Market risk premium |
| **SMB** (Small Minus Big) | Small-cap minus large-cap returns | Size premium (~2-3%/yr) |
| **HML** (High Minus Low) | High B/M minus low B/M returns | Value premium (~3-5%/yr) |

### Fama-French 5-Factor Model (adds profitability + investment)
```
R_i - R_f = α + β₁·MKT + β₂·SMB + β₃·HML + β₄·RMW + β₅·CMA + ε
```
| Factor | Definition |
|---|---|
| **RMW** (Robust Minus Weak) | High profitability minus low profitability |
| **CMA** (Conservative Minus Aggressive) | Low investment minus high investment |

### Carhart 4-Factor Model (adds momentum to FF3)
```
R_i - R_f = α + β₁·MKT + β₂·SMB + β₃·HML + β₄·MOM + ε
```
- **MOM**: Winners (past 12-1 month return) minus losers

### Factor Data Sources
- **Fama-French data**: [mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
- Python: `pandas_datareader` → `famafrench` data source

### Rolling Factor Regression
```python
# 252-day rolling beta estimation
rolling_betas = {}
for i in range(252, len(returns)):
    window = slice(i-252, i)
    X = sm.add_constant(factors[window])
    betas = sm.OLS(returns[window], X).fit().params
    rolling_betas[returns.index[i]] = betas
```

### Cointegration (Statistical Arbitrage)
When two non-stationary series share a common stochastic trend:
```python
from statsmodels.tsa.stattools import coint
score, p_value, critical_values = coint(series_A, series_B)
# p < 0.05 → cointegrated (tradeable spread)

# Spread Z-score for entry/exit
spread = series_A - hedge_ratio * series_B
z_score = (spread - spread.rolling(window).mean()) / spread.rolling(window).std()
# Entry: |z| > 2.0  |  Exit: |z| < 0.5  |  Stop: |z| > 3.5
```
