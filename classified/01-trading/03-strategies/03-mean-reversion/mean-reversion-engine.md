---
name: mean-reversion-engine
description: >
  Mean reversion strategy templates — Bollinger bounce, RSI extreme fade, Z-score reversion
  with regime guard. Use this skill for "mean reversion", "fade the move", "RSI overbought
  oversold", "Bollinger bounce", "reversion to mean", "Z-score trade", "oversold bounce",
  "overbought fade", "rubber band strategy", "range trading strategy", or any reversion setup.
  Works with market-regime-classifier (ONLY use in ranging regimes) and risk-and-portfolio.
kind: engine
category: trading/strategies
status: active
tags: [engine, mean, mean-reversion, regime, reversion, risk-and-portfolio, strategies, trading]
related_skills: [market-regime-classifier]
---

# Mean Reversion Engine

## CRITICAL: Only use in RANGING regimes. Mean reversion in trends = catching knives.

```python
import pandas as pd
import numpy as np

class MeanReversionEngine:

    @staticmethod
    def bollinger_bounce(df: pd.DataFrame, period: int = 20, std_mult: float = 2.0) -> dict:
        """Buy at lower band, sell at upper band. Classic range strategy."""
        close = df["close"]
        mid = close.rolling(period).mean()
        std = close.rolling(period).std()
        upper = mid + std_mult * std
        lower = mid - std_mult * std
        pct_b = (close - lower) / (upper - lower)

        current = df.iloc[-1]
        return {
            "strategy": "bollinger_bounce",
            "upper": round(upper.iloc[-1], 5),
            "middle": round(mid.iloc[-1], 5),
            "lower": round(lower.iloc[-1], 5),
            "pct_b": round(pct_b.iloc[-1], 3),
            "signal": "BUY (at lower band)" if pct_b.iloc[-1] < 0.05 else
                     "SELL (at upper band)" if pct_b.iloc[-1] > 0.95 else "WAIT",
            "target": round(mid.iloc[-1], 5),
            "stop": round(lower.iloc[-1] - (upper.iloc[-1] - lower.iloc[-1]) * 0.25, 5) if pct_b.iloc[-1] < 0.05
                   else round(upper.iloc[-1] + (upper.iloc[-1] - lower.iloc[-1]) * 0.25, 5),
        }

    @staticmethod
    def rsi_extreme_fade(df: pd.DataFrame, period: int = 14,
                         oversold: float = 25, overbought: float = 75) -> dict:
        """Fade RSI extremes with divergence confirmation."""
        close = df["close"]
        delta = close.diff()
        gain = delta.where(delta > 0, 0).rolling(period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
        rsi = 100 - (100 / (1 + gain / loss.replace(0, np.nan)))

        # Divergence: price makes new low but RSI makes higher low (bullish)
        price_lower = close.iloc[-1] < close.rolling(20).min().iloc[-5]
        rsi_higher = rsi.iloc[-1] > rsi.rolling(20).min().iloc[-5]
        bull_divergence = price_lower and rsi_higher and rsi.iloc[-1] < 40

        price_higher = close.iloc[-1] > close.rolling(20).max().iloc[-5]
        rsi_lower = rsi.iloc[-1] < rsi.rolling(20).max().iloc[-5]
        bear_divergence = price_higher and rsi_lower and rsi.iloc[-1] > 60

        return {
            "strategy": "rsi_extreme_fade",
            "rsi": round(rsi.iloc[-1], 1),
            "oversold": rsi.iloc[-1] < oversold,
            "overbought": rsi.iloc[-1] > overbought,
            "bullish_divergence": bull_divergence,
            "bearish_divergence": bear_divergence,
            "signal": "BUY (oversold + divergence)" if rsi.iloc[-1] < oversold and bull_divergence
                     else "BUY (oversold)" if rsi.iloc[-1] < oversold
                     else "SELL (overbought + divergence)" if rsi.iloc[-1] > overbought and bear_divergence
                     else "SELL (overbought)" if rsi.iloc[-1] > overbought
                     else "WAIT",
            "quality": "A+" if bull_divergence or bear_divergence else "B",
        }

    @staticmethod
    def zscore_reversion(df: pd.DataFrame, lookback: int = 60,
                         entry_z: float = 2.0, exit_z: float = 0.5) -> dict:
        """Z-score based reversion with configurable thresholds."""
        close = df["close"]
        mean = close.rolling(lookback).mean()
        std = close.rolling(lookback).std()
        z = (close - mean) / std.replace(0, np.nan)

        return {
            "strategy": "zscore_reversion",
            "z_score": round(z.iloc[-1], 3),
            "mean": round(mean.iloc[-1], 5),
            "signal": "BUY (z < -2)" if z.iloc[-1] < -entry_z
                     else "SELL (z > 2)" if z.iloc[-1] > entry_z
                     else "EXIT" if abs(z.iloc[-1]) < exit_z and abs(z.iloc[-2]) > exit_z
                     else "WAIT",
            "target": round(mean.iloc[-1], 5),
            "distance_to_mean_pct": round((close.iloc[-1] / mean.iloc[-1] - 1) * 100, 2),
        }

    @staticmethod
    def scan_all(df: pd.DataFrame, symbol: str = "") -> dict:
        return {
            "symbol": symbol,
            "bollinger": MeanReversionEngine.bollinger_bounce(df),
            "rsi_fade": MeanReversionEngine.rsi_extreme_fade(df),
            "zscore": MeanReversionEngine.zscore_reversion(df),
            "WARNING": "Mean reversion ONLY works in ranging markets. Check regime first.",
        }
```

## Practical Mean-Reversion Scalping: EMA + Bollinger Band (CodeTrading)

> Source: "Trading with Python: Simple Scalping Strategy" by CodeTrading (Jan 2024)

A practical M5 scalping implementation of mean-reversion with trend filter:
- **Entry:** Price touches lower BB (long) or upper BB (short) while dual EMA confirms trend direction
- **Logic:** Mean-reversion (BB bounce to center) filtered by trend-following (EMA 30/50 alignment for 6+ candles)
- **Results:** 25% return in 3 months on EURUSD M5, 1,671 trades, 44% win rate
- **Key insight:** Combining trend-following with mean-reversion produces steadily increasing equity — the trend filter prevents trading BB bounces against the trend
- SL = ATR * 1.1, TP = SL * 1.5

For full implementation details and Python code, see `scalping-framework` skill.
