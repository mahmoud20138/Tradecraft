---
name: correlation-regime-switcher
description: >
  Automatically switches strategy sets when correlation regimes change. Use this skill whenever
  the user asks about "correlation regime change", "adaptive strategy switching", "when correlations
  break", "regime-based strategy selection", "correlation breakdown trading", "dynamic strategy
  switching", "auto-switch strategy", or any question about adapting to changing inter-market
  relationships. Works with pair-correlation-engine and market-regime-classifier.
kind: reference
category: trading/market-context
status: active
tags: [correlation, market-context, regime, switcher, trading]
related_skills: [cross-asset-relationships, correlation-crisis, market-regime-classifier, multi-pair-basket-trader, pair-scanner-screener]
---

# Correlation Regime Switcher

```python
import pandas as pd
import numpy as np

class CorrelationRegimeSwitcher:

    REGIME_STRATEGIES = {
        "normal_correlation": {
            "description": "Correlations at historical norms",
            "strategies": ["trend_following", "carry_trade", "mean_reversion_pairs"],
            "risk_level": "NORMAL",
        },
        "correlation_breakdown": {
            "description": "Historical correlations breaking down",
            "strategies": ["single_pair_momentum", "volatility_selling"],
            "risk_level": "ELEVATED — reduce correlated positions",
        },
        "correlation_spike": {
            "description": "All assets moving together (crisis mode)",
            "strategies": ["safe_haven_only", "volatility_buying", "cash"],
            "risk_level": "HIGH — correlation=1 means no diversification benefit",
        },
        "decorrelation": {
            "description": "Assets becoming uncorrelated — dispersion rising",
            "strategies": ["pairs_trading", "relative_value", "basket_trades"],
            "risk_level": "OPPORTUNITY — dispersion creates relative value trades",
        },
    }

    @staticmethod
    def detect_regime(correlation_matrix: pd.DataFrame, historical_avg_corr: float) -> dict:
        """Classify current correlation regime."""
        upper_tri = correlation_matrix.values[np.triu_indices_from(correlation_matrix.values, k=1)]
        current_avg = np.mean(np.abs(upper_tri))
        deviation = current_avg - abs(historical_avg_corr)

        if current_avg > 0.8:
            regime = "correlation_spike"
        elif deviation > 0.15:
            regime = "correlation_spike"
        elif deviation < -0.15:
            regime = "decorrelation"
        elif abs(deviation) < 0.05:
            regime = "normal_correlation"
        else:
            regime = "correlation_breakdown"

        strategies = CorrelationRegimeSwitcher.REGIME_STRATEGIES[regime]
        return {
            "regime": regime,
            "current_avg_correlation": round(current_avg, 4),
            "historical_avg": round(abs(historical_avg_corr), 4),
            "deviation": round(deviation, 4),
            **strategies,
        }

    @staticmethod
    def transition_detector(rolling_corr: pd.Series, window: int = 20) -> dict:
        """Detect regime transitions from rolling correlation data."""
        recent = rolling_corr.tail(window)
        prior = rolling_corr.iloc[-(window*2):-window]
        change = recent.mean() - prior.mean()
        return {
            "transition_detected": abs(change) > 0.2,
            "direction": "CONVERGING" if change > 0.2 else "DIVERGING" if change < -0.2 else "STABLE",
            "magnitude": round(abs(change), 4),
            "action": "Switch strategy set — correlation regime changing" if abs(change) > 0.2 else "Hold current strategies",
        }
```
