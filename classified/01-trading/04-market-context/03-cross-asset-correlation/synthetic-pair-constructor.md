---
name: synthetic-pair-constructor
description: >
  Build custom synthetic instruments from weighted pair combinations. Use this skill whenever
  the user asks about "synthetic pair", "basket construction", "custom index", "weighted
  basket", "create a currency basket", "DXY replica", "synthetic instrument", "pair basket",
  "composite instrument", "trade a basket", or any request to construct custom tradeable
  instruments from multiple pairs. Works with pair-correlation-engine and portfolio-optimizer.
kind: reference
category: trading/market-context
status: active
tags: [constructor, correlation, market-context, pair, portfolio, synthetic, trading]
related_skills: [cross-asset-relationships, correlation-crisis, correlation-regime-switcher, multi-pair-basket-trader, pair-scanner-screener]
---

# Synthetic Pair & Basket Constructor

```python
import pandas as pd
import numpy as np

class SyntheticPairBuilder:

    @staticmethod
    def build_basket(prices: pd.DataFrame, weights: dict, name: str = "BASKET") -> pd.Series:
        """Construct a synthetic instrument from weighted price series."""
        normalized = prices / prices.iloc[0]  # Normalize to 1.0
        basket = sum(normalized[sym] * w for sym, w in weights.items() if sym in normalized.columns)
        basket.name = name
        return basket

    @staticmethod
    def dxy_replica(prices: pd.DataFrame) -> pd.Series:
        """Replicate the US Dollar Index from FX pairs."""
        weights = {"EURUSD": -0.576, "USDJPY": 0.136, "GBPUSD": -0.119,
                   "USDCAD": 0.091, "USDSEK": 0.042, "USDCHF": 0.036}
        # Invert pairs where USD is quote currency
        adjusted = prices.copy()
        for pair in ["EURUSD", "GBPUSD"]:
            if pair in adjusted.columns:
                adjusted[pair] = 1 / adjusted[pair]
        return SyntheticPairBuilder.build_basket(adjusted, {k: abs(v) for k, v in weights.items()}, "DXY_SYNTHETIC")

    @staticmethod
    def risk_on_off_basket(prices: pd.DataFrame) -> dict:
        """Build risk-on and risk-off baskets for sentiment measurement."""
        risk_on = {"AUDUSD": 0.33, "NZDUSD": 0.33, "USDCAD": -0.34}  # long AUD/NZD, short USD/CAD
        risk_off = {"USDJPY": -0.5, "USDCHF": -0.5}  # long JPY, CHF
        return {
            "risk_on_basket": SyntheticPairBuilder.build_basket(prices, risk_on, "RISK_ON"),
            "risk_off_basket": SyntheticPairBuilder.build_basket(prices, risk_off, "RISK_OFF"),
        }

    @staticmethod
    def optimal_basket_weights(prices: pd.DataFrame, target: pd.Series,
                                method: str = "ols") -> dict:
        """Find optimal weights to replicate a target series."""
        from sklearn.linear_model import LinearRegression
        normalized_prices = prices / prices.iloc[0]
        normalized_target = target / target.iloc[0]
        aligned = pd.concat([normalized_prices, normalized_target.rename("target")], axis=1).dropna()
        X = aligned.drop("target", axis=1)
        y = aligned["target"]
        model = LinearRegression(fit_intercept=False).fit(X, y)
        weights = dict(zip(X.columns, np.round(model.coef_, 4)))
        r_squared = round(model.score(X, y), 4)
        return {"weights": weights, "r_squared": r_squared,
                "tracking_error": round((y - model.predict(X)).std(), 6)}
```
