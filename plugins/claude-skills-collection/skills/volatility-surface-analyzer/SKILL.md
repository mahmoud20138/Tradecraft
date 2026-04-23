---
name: volatility-surface-analyzer
description: >
  Implied volatility, vol smile, term structure, and vol arbitrage signal analysis. Use this skill
  whenever the user asks about "implied volatility", "vol smile", "volatility surface", "term
  structure", "vol skew", "IV rank", "IV percentile", "volatility arbitrage", "realized vs implied",
  "volatility cone", "variance risk premium", "vol crush", "straddle pricing", or any options/
  volatility-related analysis. Works with macro-economic-dashboard for VIX context.
kind: analyzer
category: trading/market-context
status: active
aliases: [volatility-surface]
tags: [analyzer, market-context, risk-and-portfolio, surface, trading, volatility]
related_skills: [options-trading, macro-economic-dashboard]
---

# Volatility Surface Analyzer

## Overview
Analyzes realized vs implied volatility, constructs vol surfaces, detects mispricing,
and generates vol-based trading signals. Essential for options-aware FX trading.

---

## 1. Realized Volatility Engine

```python
import pandas as pd
import numpy as np
from scipy import stats

class VolatilityAnalyzer:
    """Complete volatility analysis toolkit."""

    @staticmethod
    def realized_vol(returns: pd.Series, windows: list[int] = [5, 10, 20, 60, 252]) -> pd.DataFrame:
        """Multi-window realized volatility (annualized)."""
        result = pd.DataFrame(index=returns.index)
        for w in windows:
            result[f"rv_{w}d"] = returns.rolling(w).std() * np.sqrt(252) * 100
        return result

    @staticmethod
    def volatility_cone(returns: pd.Series, windows: list[int] = [5, 10, 20, 60]) -> dict:
        """Vol cone: distribution of RV at each window — shows where current vol sits historically."""
        cone = {}
        for w in windows:
            rv = returns.rolling(w).std() * np.sqrt(252) * 100
            rv = rv.dropna()
            current = rv.iloc[-1]
            percentile = (rv < current).mean() * 100
            cone[f"{w}d"] = {
                "current": round(current, 2),
                "percentile": round(percentile, 1),
                "min": round(rv.min(), 2), "p25": round(rv.quantile(0.25), 2),
                "median": round(rv.median(), 2), "p75": round(rv.quantile(0.75), 2),
                "max": round(rv.max(), 2),
                "regime": "HIGH" if percentile > 75 else "LOW" if percentile < 25 else "NORMAL",
            }
        return cone

    @staticmethod
    def iv_rank(current_iv: float, iv_high_52w: float, iv_low_52w: float) -> dict:
        """IV Rank: where current IV sits in 52-week range (0-100)."""
        iv_range = iv_high_52w - iv_low_52w
        rank = ((current_iv - iv_low_52w) / iv_range * 100) if iv_range > 0 else 50
        return {
            "iv_rank": round(rank, 1),
            "current_iv": current_iv,
            "52w_high": iv_high_52w, "52w_low": iv_low_52w,
            "signal": "SELL VOL (premium rich)" if rank > 80 else "BUY VOL (premium cheap)" if rank < 20 else "NEUTRAL",
        }

    @staticmethod
    def variance_risk_premium(realized_vol: float, implied_vol: float) -> dict:
        """VRP = IV - RV. Positive = vol sellers earn premium."""
        vrp = implied_vol - realized_vol
        return {
            "vrp": round(vrp, 2),
            "implied_vol": round(implied_vol, 2),
            "realized_vol": round(realized_vol, 2),
            "signal": "SELL VOL — IV overpricing risk" if vrp > 3 else "BUY VOL — IV underpricing risk" if vrp < -2 else "FAIR",
            "note": "Positive VRP is normal (insurance premium). Extreme readings are actionable.",
        }

    @staticmethod
    def vol_term_structure(ivs_by_expiry: dict) -> dict:
        """Analyze IV term structure shape: contango (normal) vs backwardation (fear)."""
        expiries = sorted(ivs_by_expiry.keys())
        ivs = [ivs_by_expiry[e] for e in expiries]
        if len(ivs) < 2:
            return {"shape": "insufficient data"}
        slope = (ivs[-1] - ivs[0]) / len(ivs)
        shape = "CONTANGO (normal)" if slope > 0.5 else "BACKWARDATION (fear/event)" if slope < -0.5 else "FLAT"
        return {
            "shape": shape, "slope": round(slope, 3),
            "front_iv": round(ivs[0], 2), "back_iv": round(ivs[-1], 2),
            "signal": "Risk-off positioning" if "BACKWARDATION" in shape else "Normal conditions",
            "term_structure": {e: round(v, 2) for e, v in zip(expiries, ivs)},
        }

    @staticmethod
    def vol_regime_signal(returns: pd.Series) -> dict:
        """Generate trading signals from vol regime analysis."""
        cone = VolatilityAnalyzer.volatility_cone(returns)
        rv_20 = cone.get("20d", {})
        regime = rv_20.get("regime", "NORMAL")
        return {
            "regime": regime,
            "rv_20d": rv_20.get("current", 0),
            "percentile": rv_20.get("percentile", 50),
            "strategy_advice": {
                "HIGH": "Widen stops, reduce size. Vol expansion phase — breakout strategies work.",
                "LOW": "Tighten stops, normal size. Vol compression — expect breakout soon. Set range orders.",
                "NORMAL": "Standard parameters. Follow directional signals.",
            }.get(regime, ""),
        }
```
