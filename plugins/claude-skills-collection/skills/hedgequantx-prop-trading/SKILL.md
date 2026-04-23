---
name: hedgequantx-prop-trading
description: HedgeQuantX — CLI tool connecting to 37+ prop trading firms for automated futures trading. Supports ProjectX (19 firms), Rithmic (16 firms), Tradovate (3 firms). Two modes: proprietary HQX strategy or copy trading (lead→followers). AES-256-GCM local 
kind: strategy
category: trading/execution
status: active
tags: [execution, hedgequantx, prop, trading]
related_skills: [execution-algo-trading, market-making-hft, tick-data-storage, market-impact-model, spread-slippage-cost-analyzer]
---

# hedgequantx-prop-trading

USE FOR:
  - "prop firm trading automation"
  - "TopStep / Apex / Bulenox automated trading"
  - "futures copy trading"
  - "ProjectX / Rithmic API trading"
  - "multi-account prop firm bot"
  - "automated futures trading CLI"
tags: [prop-trading, futures, copy-trading, TopStep, Apex, Rithmic, ProjectX, Tradovate, CLI, multi-account]
kind: tool
category: execution-algo-trading

---

## What Is HedgeQuantX?

CLI tool for automated futures trading across 37+ proprietary trading firms.

- Repo: https://github.com/HedgeQuantX/HedgeQuantX
- Install: `npm i -g hedgequantx`
- Architecture: Local-only, no external server, AES-256-GCM encrypted sessions

---

## Installation & Launch

```bash
npm i -g hedgequantx
hqx          # or: hedgequantx
```

---

## Supported Platforms & Firms

### ProjectX (19 firms)
TopStep · TickTickTrader · TradeDay · Goat Futures · + 15 more

### Rithmic (16 firms)
Apex Trader Funding · MES Capital · Bulenox · + 13 more

### Tradovate (3 firms)
Apex · TakeProfitTrader · MyFundedFutures

---

## Operating Modes

### Mode 1: One Account (HQX Strategy)
```
Single account → runs proprietary HQX systematic strategy
```

### Mode 2: Copy Trading
```
Lead account → executes primary trades
    ↓ mirrors to
Follower accounts (multiple) → same trades replicated
```

---

## Key Features

| Feature | Detail |
|---------|--------|
| Multi-account | Manage multiple prop accounts simultaneously |
| Real-time monitoring | Live balance, P&L, positions, orders |
| Market hours validation | Auto-validates trading hours per instrument |
| Session encryption | AES-256-GCM, machine-bound keys |
| Local execution | Direct API, no server middleman |
| Credential security | Never stored in plaintext, 0600 file permissions |

---

## Use Case: Pass Prop Firm Challenge

```bash
# 1. Install and launch
npm i -g hedgequantx && hqx

# 2. Connect to TopStep (via ProjectX API)
# 3. Select "One Account Mode" → HQX strategy
# 4. Monitor P&L in real-time dashboard
# 5. Meet daily/max drawdown limits automatically
```


---
# ── KNOWLEDGE INJECTION: All of Statistics in 1 Hour (JensenMath) ──
# Source: https://www.youtube.com/watch?v=_Pyi12dn4Kw
# Channel: JensenMath (MDM4U Grade 12 Data Management)
# Routed to: trading.md → statistics-timeseries
# Date: 2026-03-17

## Statistics Complete Reference (JensenMath MDM4U)

A comprehensive statistics study guide covering all foundational concepts
relevant to trading, quant research, and data science.

---

### 1. Data Types & Graphical Displays

**Variable types:**
- **Qualitative** (categorical): bar graphs, pie charts
- **Quantitative** (numeric): histograms, box plots, scatter plots

**Distribution shapes:**
- Symmetric (normal) · Left-skewed · Right-skewed · Bimodal · Uniform

**Scatter plots & correlation:**
- Positive / negative / no correlation
- Strong vs weak (spread around line of best fit)
- Outliers and leverage points

**Misleading graphs — red flags:**
- Truncated y-axis (starts non-zero)
- Unequal intervals on axis
- 3D effects distorting area/volume
- Cherry-picked time ranges

---

### 2. Data Collection & Bias

**Sampling methods:**
| Method | Description |
|--------|-------------|
| Simple random | Every member equally likely |
| Systematic | Every Nth member |
| Stratified | Proportional subgroups |
| Cluster | Random groups (not individuals) |
| Convenience | Easiest to reach (biased) |

**Sources of bias:**
- **Sampling bias**: non-representative sample
- **Response bias**: wording influences answers
- **Non-response bias**: certain groups don't respond
- **Voluntary response bias**: self-selected strong opinions

---

### 3. Descriptive Statistics

**Measures of central tendency:**
```
Mean   = Σx / n
Median = middle value (or avg of two middle)
Mode   = most frequent value
```

**Measures of spread:**
```
Range      = max − min
Variance   = Σ(x − x̄)² / (n−1)        [sample]
Std Dev    = √Variance
IQR        = Q3 − Q1                    [robust to outliers]
```

**Choosing the right measure:**
```
Symmetric distribution  → use mean + std dev
Skewed / outliers       → use median + IQR
```

**Z-score (standardization):**
```
z = (x − μ) / σ

Interpretation:
z = +1.5 → value is 1.5 standard deviations ABOVE mean
z = −2.0 → value is 2.0 standard deviations BELOW mean
```

---

### 4. Normal Distribution

**Properties:**
- Bell-shaped, symmetric about μ
- Mean = Median = Mode
- Total area under curve = 1
- Defined by μ (mean) and σ (std dev)

**Empirical Rule (68-95-99.7):**
```
μ ± 1σ → 68.27% of data
μ ± 2σ → 95.45% of data
μ ± 3σ → 99.73% of data
```

**Using z-tables / standard normal:**
```python
from scipy import stats

# P(X < 75) where μ=70, σ=5
z = (75 - 70) / 5          # z = 1.0
p = stats.norm.cdf(z)      # p ≈ 0.8413 → 84.13%

# P(65 < X < 75)
p = stats.norm.cdf(1.0) - stats.norm.cdf(-1.0)  # ≈ 68.27%

# Find value at 90th percentile
x = stats.norm.ppf(0.90, loc=70, scale=5)        # x ≈ 76.4
```

**Confidence intervals:**
```
CI = x̄ ± z* · (σ / √n)

Common z* values:
  90% CI → z* = 1.645
  95% CI → z* = 1.960
  99% CI → z* = 2.576
```

---

### 5. Probability

**Fundamental rules:**
```
P(A) = favourable outcomes / total outcomes     [theoretical]
P(A) = successes / trials                       [experimental]

0 ≤ P(A) ≤ 1
P(A) + P(A') = 1                               [complement rule]
```

**Addition rule:**
```
P(A ∪ B) = P(A) + P(B) − P(A ∩ B)            [general]
P(A ∪ B) = P(A) + P(B)                         [mutually exclusive]
```

**Multiplication rule:**
```
P(A ∩ B) = P(A) · P(B|A)                       [general / dependent]
P(A ∩ B) = P(A) · P(B)                         [independent events]
```

**Conditional probability:**
```
P(B|A) = P(A ∩ B) / P(A)

"Probability of B GIVEN A has occurred"
```

**Set notation:**
```
A ∪ B  → A OR B  (union)
A ∩ B  → A AND B (intersection)
A'     → NOT A   (complement)
```

---

### 6. Counting Methods

**Fundamental counting principle:**
```
m choices for event 1 × n choices for event 2 = m × n total
```

**Permutations (ORDER matters):**
```
nPr = n! / (n−r)!

All arrangements of n items:  n!
Arrangements with repeats:    n! / (a! · b! · ...)
```

**Combinations (ORDER doesn't matter):**
```
nCr = n! / (r! · (n−r)!)     also written C(n,r) or (n choose r)

Key identity: nCr = nC(n−r)
```

```python
from math import factorial, comb, perm

# Permutations: arrange 3 from 5
perm(5, 3)       # = 60

# Combinations: choose 3 from 5
comb(5, 3)       # = 10
```

---

### 7. Probability Distributions

**Discrete probability distribution requirements:**
```
1. 0 ≤ P(x) ≤ 1 for all x
2. ΣP(x) = 1
```

**Expected value and variance:**
```
E(X) = μ = Σ[x · P(x)]
Var(X) = σ² = Σ[(x−μ)² · P(x)]
```

#### Binomial Distribution B(n, p)
```
Conditions: fixed n trials, constant p, independent, binary outcome

P(X = k) = C(n,k) · pᵏ · (1−p)^(n−k)

μ = np
σ² = np(1−p)
σ = √(np(1−p))
```

```python
from scipy.stats import binom
# 10 flips, p=0.5, P(exactly 6 heads)
binom.pmf(6, n=10, p=0.5)    # ≈ 0.2051

# P(X ≤ 6)
binom.cdf(6, n=10, p=0.5)    # ≈ 0.8281
```

#### Geometric Distribution
```
Conditions: repeated trials until FIRST success

P(X = k) = (1−p)^(k−1) · p    [k = trial of first success]

μ = 1/p
σ² = (1−p) / p²
```

#### Hypergeometric Distribution
```
Conditions: sampling WITHOUT replacement from finite population

Population N, K successes in population, draw n items:
P(X = k) = C(K,k) · C(N−K, n−k) / C(N,n)

μ = nK/N
σ² = nK(N−K)(N−n) / [N²(N−1)]
```

---

### 8. Linear Regression

**Least squares regression line:**
```
ŷ = a + bx

b = r · (Sy / Sx)           [slope]
a = ȳ − b·x̄                [intercept]

where r = correlation coefficient (−1 ≤ r ≤ 1)
```

**Correlation coefficient r:**
```
|r| = 1.0       perfect linear relationship
|r| > 0.8       strong
0.5 < |r| < 0.8 moderate
|r| < 0.5       weak
r = 0           no linear relationship
```

**Coefficient of determination r²:**
```
r² = proportion of variance in y explained by x
r² = 0.81 → x explains 81% of variation in y
```

```python
import numpy as np
from scipy import stats

slope, intercept, r, p_value, std_err = stats.linregress(x, y)
print(f"r = {r:.3f}, r² = {r**2:.3f}")
print(f"ŷ = {intercept:.2f} + {slope:.2f}x")
```

---

### Trading Applications of Each Topic

| Statistics Topic | Trading Use Case |
|-----------------|-----------------|
| Normal distribution | Return distribution, VaR, z-score signals |
| Confidence intervals | Entry zones, expected price ranges |
| Correlation (r) | Pair trading, hedge ratios, sector correlation |
| Regression | Price prediction, beta calculation, factor models |
| Binomial dist. | Win rate modeling, position sizing (Kelly) |
| Conditional probability | Bayesian signal updating |
| Hypergeometric | Sampling from finite order book |
| Z-score | Mean reversion entries (Bollinger Bands logic) |
| Standard deviation | Volatility measurement, ATR normalization |
| Combinations nCr | Portfolio combinations, basket construction |


---
