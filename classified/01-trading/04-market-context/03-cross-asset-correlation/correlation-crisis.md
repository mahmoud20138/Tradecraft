---
id: correlation-crisis
name: correlation-crisis
description: "Correlation breakdown during crises, tail risk measurement (VaR, CVaR, fat tails), regime-dependent correlation matrices, hedging strategies by volatility regime, and stress testing protocols. Use for correlation crisis, tail risk, VaR, CVaR, hedging strategy, stress test, or any correlation/tail-risk analysis."
title: "Correlation Crisis & Tail Risk"
domain: trading/risk-and-portfolio
level: advanced
version: 1
depends_on: [portfolio-optimization, cross-asset-relationships]
unlocks: [real-time-risk-monitor]
tags: [correlation, tail-risk, hedging, crisis, regime, diversification]
status: active
created: "2025-01-15"
updated: "2025-01-15"
context_cost: medium
load_priority: 0.60
kind: reference
category: trading/market-context
---
> **Skill:** Correlation Crisis & Tail Risk  |  **Domain:** trading/risk-and-portfolio  |  **Category:** risk  |  **Level:** advanced
> **Tags:** `correlation`, `tail-risk`, `hedging`, `crisis`, `regime`, `diversification`

# Correlation Crisis & Tail Risk

## 1. The Correlation Problem

### Normal Times vs Crisis
```
NORMAL REGIME (VIX < 20):
  Correlations are moderate and stable
  Diversification works as expected
  Asset A: +1%  Asset B: -0.3%  Asset C: +0.5%
  Portfolio: smoothed returns ✓

CRISIS REGIME (VIX > 30):
  Correlations spike toward 1.0
  "All correlations go to 1 in a crash"
  Asset A: -5%  Asset B: -4%  Asset C: -6%
  Portfolio: concentrated loss ✗

  Exception: USD, Treasuries, Gold often decouple
  (but not always — March 2020 everything sold)
```

### Correlation Is Not Constant
```python
def rolling_correlation(asset_a: pd.Series, asset_b: pd.Series,
                        window: int = 60) -> pd.Series:
    """60-day rolling correlation reveals regime shifts."""
    return asset_a.rolling(window).corr(asset_b)

# Key insight: when rolling correlation breaks out of its
# historical range, regime change is likely in progress
```

## 2. Measuring Tail Risk

### Beyond Standard Deviation
```
Standard deviation assumes normal distribution.
Markets have fat tails. Use:

1. Value at Risk (VaR)
   - 95% VaR: "I expect to lose no more than X on 95% of days"
   - Limitation: says nothing about the worst 5%

2. Conditional VaR (CVaR / Expected Shortfall)
   - "When I DO exceed VaR, what's my expected loss?"
   - Average of losses beyond VaR threshold
   - This is the metric that matters for tail risk

3. Maximum Drawdown
   - Empirical worst case (so far)
   - Rule of thumb: future MDD ≈ 1.5-2× historical MDD

4. Tail Ratio
   - 95th percentile gain / abs(5th percentile loss)
   - >1.0 = positive skew (good)
   - <1.0 = negative skew (hidden risk)
```

### Fat Tail Detection
```python
from scipy.stats import kurtosis, jarque_bera

def tail_risk_report(returns: pd.Series) -> dict:
    kurt = kurtosis(returns)  # >0 means fat tails
    jb_stat, jb_pval = jarque_bera(returns)

    var_95 = returns.quantile(0.05)
    cvar_95 = returns[returns <= var_95].mean()

    tail_ratio = returns.quantile(0.95) / abs(returns.quantile(0.05))

    return {
        'kurtosis': kurt,           # Normal = 0, fat tails > 3
        'is_normal': jb_pval > 0.05,  # Almost always False for markets
        'var_95': var_95,
        'cvar_95': cvar_95,
        'tail_ratio': tail_ratio,
        'worst_day': returns.min(),
        'best_day': returns.max(),
    }
```

## 3. Regime-Dependent Correlation Matrix

### Building Conditional Correlation
```python
def regime_correlations(returns: pd.DataFrame,
                        vix: pd.Series) -> dict:
    """Compute separate correlation matrices per regime."""

    regimes = {
        'low_vol':  vix < vix.quantile(0.33),
        'mid_vol':  (vix >= vix.quantile(0.33)) & (vix < vix.quantile(0.66)),
        'high_vol': vix >= vix.quantile(0.66),
        'crisis':   vix > vix.quantile(0.95),
    }

    matrices = {}
    for name, mask in regimes.items():
        regime_returns = returns[mask]
        matrices[name] = regime_returns.corr()

    return matrices

# USE THIS for portfolio construction:
# - Size positions using CRISIS correlations
# - Don't trust calm-period diversification benefits
```

### Correlation Breakout Alert
```python
def correlation_alert(rolling_corr: pd.Series,
                      lookback: int = 252) -> str:
    current = rolling_corr.iloc[-1]
    mean = rolling_corr.iloc[-lookback:].mean()
    std = rolling_corr.iloc[-lookback:].std()
    z_score = (current - mean) / std

    if z_score > 2.0:
        return "ALERT: Correlation spike — diversification degrading"
    elif z_score < -2.0:
        return "NOTE: Correlation breakdown — unusual divergence"
    return "NORMAL"
```

## 4. Hedging Strategies

### Portfolio Hedges by Regime
```
LOW VOLATILITY (VIX 10-15):
  ├── Hedges are cheap → buy tail protection
  ├── OTM puts on portfolio (1-3% of portfolio value quarterly)
  ├── Long VIX calls (3-6 month expiry)
  └── Cost: drag on returns during calm periods

RISING VOLATILITY (VIX 15-25):
  ├── Hedges getting expensive → be selective
  ├── Reduce gross exposure by 10-20%
  ├── Shift to shorter holding periods
  ├── Tighten stops
  └── Increase cash allocation

HIGH VOLATILITY (VIX 25-40):
  ├── Hedges are expensive → use position sizing instead
  ├── Reduce position sizes by 40-60%
  ├── Only A+ setups
  ├── Consider inverse correlation trades
  └── No overnight exposure in uncertain direction

CRISIS (VIX > 40):
  ├── Capital preservation mode
  ├── Flatten all non-core positions
  ├── Cash is a position
  ├── Look for dislocation opportunities (small size)
  └── This is when fortunes are made AND lost
```

### Cross-Asset Hedges
```
If long equities:
  ├── Long treasuries (TLT) — works most of the time
  ├── Long gold (GLD) — works in inflation + crisis
  ├── Long USD (DXY) — works in global risk-off
  ├── Long VIX futures — works fast but decay kills you
  └── CAUTION: March 2020 showed all can fail simultaneously

If long forex carry:
  ├── Long JPY, CHF — classic safe havens
  ├── Short AUD, NZD — risk-sensitive commodity currencies
  └── Position size is the best hedge

If long crypto:
  ├── Stablecoin allocation (capital preservation)
  ├── Short perpetuals on portion of holdings
  ├── Options if liquid (BTC/ETH only practically)
  └── Crypto correlations to equities are regime-dependent
```

## 5. Stress Testing Protocol

```python
def stress_test_portfolio(positions: list[Position],
                          scenarios: dict) -> pd.DataFrame:
    """
    scenarios = {
        '2008_GFC': {'SPY': -0.55, 'TLT': +0.20, 'GLD': +0.25, 'VIX': +300%},
        '2020_COVID': {'SPY': -0.34, 'TLT': +0.15, 'GLD': -0.05, 'BTC': -0.50},
        'Flash_Crash': {'SPY': -0.10, 'all_corr': 0.95, 'liquidity': -80%},
        'Rate_Shock': {'TLT': -0.25, 'SPY': -0.15, 'USDJPY': +10%},
        'Custom': {...}
    }
    """
    results = []
    for name, shocks in scenarios.items():
        portfolio_pnl = sum(
            pos.value * shocks.get(pos.symbol, shocks.get('default', -0.10))
            for pos in positions
        )
        results.append({
            'scenario': name,
            'portfolio_pnl': portfolio_pnl,
            'pct_loss': portfolio_pnl / total_portfolio_value,
            'survives': abs(portfolio_pnl / total_portfolio_value) < max_allowed_dd,
        })
    return pd.DataFrame(results)
```

## 6. Rules

1. **Size for the crisis, not the calm.** Use crisis-regime correlations for position sizing.
2. **When hedges are cheap, buy them.** Low VIX = cheap insurance.
3. **Diversification is a regime-dependent feature.** It works until you need it most.
4. **Cash is a position.** 20-30% cash in uncertain regimes is not "missing out."
5. **Stress test monthly.** Run portfolio through historical crises. If you can't survive 2008 on paper, you can't survive the next one live.

---

## Related Skills

- [Portfolio Optimization](portfolio-optimization.md)
- [Cross-Asset Relationships](../market-foundations/cross-asset-relationships.md)
- [Risk And Portfolio](risk-and-portfolio.md)
- [Real-Time Risk Monitor](real-time-risk-monitor.md)
- [Drawdown Playbook](drawdown-playbook.md)
