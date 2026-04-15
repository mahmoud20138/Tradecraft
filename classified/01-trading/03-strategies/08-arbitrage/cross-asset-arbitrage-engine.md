---
name: cross-asset-arbitrage-engine
description: >
  Statistical arbitrage, triangular arbitrage, basis trades, and convergence detection across
  instruments. Use this skill whenever the user asks about "arbitrage", "stat arb", "pairs
  trading", "triangular arbitrage", "convergence trade", "mean reversion pair", "cointegration",
  "basis trade", "spread trading", "relative value", "mispricing detection", or any cross-asset
  relative value strategy. Works with pair-correlation-engine and mt5-chart-browser.
kind: engine
category: trading/strategies
status: active
aliases: [arbitrage-engine]
tags: [arbitrage, asset, correlation, cross, engine, mean-reversion, mt5, strategies]
related_skills: [mt5-chart-browser]
---

# Cross-Asset Arbitrage Engine

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint, adfuller

class ArbitrageEngine:

    @staticmethod
    def cointegration_test(series_a: pd.Series, series_b: pd.Series) -> dict:
        """Test if two series are cointegrated (mean-reverting spread)."""
        score, pvalue, _ = coint(series_a.dropna(), series_b.dropna())
        return {
            "cointegrated": pvalue < 0.05,
            "p_value": round(pvalue, 4),
            "test_stat": round(score, 4),
            "signal": "COINTEGRATED — pairs trade viable" if pvalue < 0.05 else "NOT cointegrated — avoid pairs trade",
        }

    @staticmethod
    def hedge_ratio(series_a: pd.Series, series_b: pd.Series) -> dict:
        """OLS hedge ratio for pairs trade construction."""
        from numpy.polynomial.polynomial import polyfit
        b, a = np.polyfit(series_b, series_a, 1)
        spread = series_a - b * series_b
        adf_stat, adf_p, *_ = adfuller(spread.dropna())
        return {
            "hedge_ratio": round(b, 6),
            "intercept": round(a, 6),
            "spread_stationary": adf_p < 0.05,
            "spread_adf_p": round(adf_p, 4),
            "entry_rule": f"Buy A, sell {abs(b):.4f} B when z-score < -2. Reverse when z-score > 2.",
        }

    @staticmethod
    def triangular_arb_check(rates: dict) -> dict:
        """
        Check for triangular arbitrage opportunity.
        rates: {"EURUSD": 1.0850, "GBPUSD": 1.2650, "EURGBP": 0.8570}
        """
        try:
            eurusd = rates["EURUSD"]
            gbpusd = rates["GBPUSD"]
            eurgbp = rates["EURGBP"]
            # Path 1: USD → EUR → GBP → USD
            implied_eurgbp = eurusd / gbpusd
            arb_1 = (implied_eurgbp / eurgbp - 1) * 10000  # in pips
            # Path 2: USD → GBP → EUR → USD
            implied_eurusd = eurgbp * gbpusd
            arb_2 = (implied_eurusd / eurusd - 1) * 10000
            return {
                "implied_eurgbp": round(implied_eurgbp, 5),
                "actual_eurgbp": eurgbp,
                "arb_pips": round(arb_1, 1),
                "opportunity": abs(arb_1) > 2,
                "direction": "Buy EURGBP" if arb_1 < -2 else "Sell EURGBP" if arb_1 > 2 else "No arb",
                "note": "Account for spread + execution latency. Sub-2pip arbs rarely executable.",
            }
        except KeyError:
            return {"error": "Need EURUSD, GBPUSD, EURGBP rates"}

    @staticmethod
    def spread_z_score_signals(spread: pd.Series, window: int = 60,
                                entry_z: float = 2.0, exit_z: float = 0.5) -> pd.DataFrame:
        """Generate entry/exit signals from spread z-score."""
        mean = spread.rolling(window).mean()
        std = spread.rolling(window).std()
        z = (spread - mean) / std.replace(0, np.nan)
        signals = pd.DataFrame(index=spread.index)
        signals["z_score"] = z
        signals["signal"] = 0
        signals.loc[z < -entry_z, "signal"] = 1   # Buy spread
        signals.loc[z > entry_z, "signal"] = -1    # Sell spread
        signals.loc[z.abs() < exit_z, "signal"] = 0  # Exit
        return signals

    @staticmethod
    def scan_cointegrated_pairs(prices: pd.DataFrame, max_pvalue: float = 0.05) -> list[dict]:
        """Scan all pair combinations for cointegration."""
        symbols = prices.columns.tolist()
        results = []
        for i, a in enumerate(symbols):
            for b in symbols[i+1:]:
                try:
                    test = ArbitrageEngine.cointegration_test(prices[a], prices[b])
                    if test["cointegrated"]:
                        hr = ArbitrageEngine.hedge_ratio(prices[a], prices[b])
                        results.append({"pair": f"{a}/{b}", **test, **hr})
                except: continue
        return sorted(results, key=lambda x: x["p_value"])
```


---
