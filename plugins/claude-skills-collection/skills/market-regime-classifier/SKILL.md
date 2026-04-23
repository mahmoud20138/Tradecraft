---
name: market-regime-classifier
description: >
  ML-powered market regime classification — trending, ranging, volatile, quiet. Automatically
  adapts strategy selection based on detected regime. Use this skill whenever the user asks
  "is the market trending", "what regime are we in", "ranging or trending", "market conditions",
  "volatility regime", "classify market state", "adapt strategy", "regime change", "market phase",
  "consolidation or breakout", "trending market detection", or any question about current market
  conditions and which strategy type to use. Works with trading-brain for strategy
  selection and mt5-chart-browser for data.
kind: analyzer
category: trading/market-context
status: active
tags: [breakout, classifier, market, market-context, mt5, regime, trading, volatility]
related_skills: [institutional-timeline, macro-economic-dashboard, market-breadth-analyzer, mt5-chart-browser, trading-brain]
---

# Market Regime Classifier

## Overview
Classifies current market state into regimes (trending-up, trending-down, ranging, volatile,
quiet) using multiple features. Maps each regime to optimal strategy types and risk parameters.

---

## 1. Regime Detection Engine

```python
import pandas as pd
import numpy as np
from typing import Literal

RegimeType = Literal["trending_up", "trending_down", "ranging", "volatile", "quiet"]

class RegimeClassifier:
    """Multi-feature regime classification."""

    @staticmethod
    def classify(df: pd.DataFrame, lookback: int = 50) -> dict:
        """
        Classify current market regime using:
        - ADX for trend strength
        - Bollinger bandwidth for volatility
        - Directional bias from MA alignment
        - Range ratio (ATR / price range)
        """
        recent = df.tail(lookback)
        close = recent["close"]
        returns = close.pct_change().dropna()

        # Trend strength via ADX proxy
        plus_dm = recent["high"].diff().clip(lower=0)
        minus_dm = (-recent["low"].diff()).clip(lower=0)
        atr = (recent["high"] - recent["low"]).rolling(14).mean()
        plus_di = plus_dm.rolling(14).mean() / atr.replace(0, np.nan) * 100
        minus_di = minus_dm.rolling(14).mean() / atr.replace(0, np.nan) * 100
        dx = abs(plus_di - minus_di) / (plus_di + minus_di).replace(0, np.nan) * 100
        adx = dx.rolling(14).mean().iloc[-1]

        # Volatility via Bollinger bandwidth
        sma20 = close.rolling(20).mean()
        std20 = close.rolling(20).std()
        bb_width = ((std20 * 2) / sma20).iloc[-1] * 100

        # MA alignment
        sma_10 = close.rolling(10).mean().iloc[-1]
        sma_20 = sma20.iloc[-1]
        sma_50 = close.rolling(50).mean().iloc[-1] if len(close) >= 50 else sma_20
        ma_aligned_up = sma_10 > sma_20 > sma_50
        ma_aligned_down = sma_10 < sma_20 < sma_50

        # Efficiency ratio: net move / total path
        net_move = abs(close.iloc[-1] - close.iloc[0])
        total_path = returns.abs().sum() * close.mean()
        efficiency = net_move / max(total_path, 1e-10)

        # Classify
        regime = RegimeClassifier._determine_regime(adx, bb_width, ma_aligned_up, ma_aligned_down, efficiency)
        strategy = RegimeClassifier._map_strategy(regime)

        return {
            "regime": regime,
            "confidence": RegimeClassifier._regime_confidence(adx, bb_width, efficiency),
            "metrics": {
                "adx": round(adx, 2) if not np.isnan(adx) else 0,
                "bb_width": round(bb_width, 4),
                "efficiency_ratio": round(efficiency, 4),
                "ma_aligned_up": ma_aligned_up,
                "ma_aligned_down": ma_aligned_down,
            },
            "recommended_strategy": strategy,
            "risk_adjustment": RegimeClassifier._risk_adjustment(regime),
        }

    @staticmethod
    def _determine_regime(adx, bb_width, ma_up, ma_down, efficiency) -> RegimeType:
        if adx > 25 and ma_up and efficiency > 0.3:
            return "trending_up"
        if adx > 25 and ma_down and efficiency > 0.3:
            return "trending_down"
        if bb_width > 3.0 and adx < 20:
            return "volatile"
        if bb_width < 1.0 and adx < 15:
            return "quiet"
        return "ranging"

    @staticmethod
    def _map_strategy(regime: RegimeType) -> dict:
        strategies = {
            "trending_up": {
                "primary": "Trend following — buy pullbacks to support/MAs",
                "avoid": "Selling, mean reversion, counter-trend",
                "indicators": "MA crossovers, ADX, trailing stops",
                "entry_style": "Buy dips to EMA20, add on breakouts",
            },
            "trending_down": {
                "primary": "Trend following — sell rallies to resistance/MAs",
                "avoid": "Buying, catching falling knives",
                "indicators": "MA crossovers, ADX, trailing stops",
                "entry_style": "Sell rallies to EMA20, add on breakdowns",
            },
            "ranging": {
                "primary": "Mean reversion — buy support, sell resistance",
                "avoid": "Breakout trades (most will be false)",
                "indicators": "RSI, Stochastic, Bollinger Bands, S/R levels",
                "entry_style": "Fade extremes, tight stops beyond range",
            },
            "volatile": {
                "primary": "Reduce size or stay flat — wait for regime clarity",
                "avoid": "Large positions, tight stops (will get stopped out)",
                "indicators": "ATR for wide stops, wait for structure",
                "entry_style": "Only high-probability setups with wide stops",
            },
            "quiet": {
                "primary": "Breakout preparation — range compression precedes expansion",
                "avoid": "Intraday trading (no movement to capture)",
                "indicators": "Bollinger squeeze, ATR contraction, volume dry-up",
                "entry_style": "Set breakout orders above/below range",
            },
        }
        return strategies.get(regime, strategies["ranging"])

    @staticmethod
    def _risk_adjustment(regime: RegimeType) -> dict:
        adjustments = {
            "trending_up": {"position_size_mult": 1.0, "stop_width_mult": 1.0, "hold_longer": True},
            "trending_down": {"position_size_mult": 1.0, "stop_width_mult": 1.0, "hold_longer": True},
            "ranging": {"position_size_mult": 0.8, "stop_width_mult": 0.8, "hold_longer": False},
            "volatile": {"position_size_mult": 0.5, "stop_width_mult": 1.5, "hold_longer": False},
            "quiet": {"position_size_mult": 0.5, "stop_width_mult": 0.5, "hold_longer": False},
        }
        return adjustments.get(regime, adjustments["ranging"])

    @staticmethod
    def _regime_confidence(adx, bb_width, efficiency) -> float:
        score = 0
        if adx > 30: score += 0.3
        elif adx < 15: score += 0.2
        if bb_width > 3 or bb_width < 1: score += 0.2
        if efficiency > 0.4 or efficiency < 0.1: score += 0.2
        return round(min(score + 0.3, 0.95), 2)

    @staticmethod
    def regime_history(df: pd.DataFrame, window: int = 50, step: int = 10) -> pd.DataFrame:
        """Rolling regime classification to detect regime transitions."""
        results = []
        for i in range(window, len(df), step):
            chunk = df.iloc[i - window:i]
            r = RegimeClassifier.classify(chunk, window)
            results.append({"time": df.index[i], "regime": r["regime"], "confidence": r["confidence"],
                           "adx": r["metrics"]["adx"]})
        return pd.DataFrame(results).set_index("time")
```

---

## Usage: Always check regime before deciding strategy type. A trend-following setup in a ranging market will fail.
