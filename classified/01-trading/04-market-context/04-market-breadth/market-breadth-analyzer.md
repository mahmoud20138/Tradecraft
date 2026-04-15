---
name: market-breadth-analyzer
description: >
  Market breadth — how many pairs trending vs ranging, overall market health, breadth divergence. Use for "market breadth, breadth scan, market health, how many trending, broad market, pairs trending", or any related query.
  Works with trading-brain and relevant analysis/strategy skills.
kind: analyzer
category: trading/market-context
status: active
tags: [analyzer, breadth, market, market-context, trading]
related_skills: [institutional-timeline, macro-economic-dashboard, market-regime-classifier, trading-brain]
---

# Market Breadth Analyzer

```python
import pandas as pd, numpy as np

class MarketBreadthAnalyzer:
    @staticmethod
    def scan_breadth(pairs_data: dict, trend_threshold: float = 25) -> dict:
        trending_up = []; trending_down = []; ranging = []
        for sym, df in pairs_data.items():
            if df.empty or len(df) < 50: continue
            close = df["close"]
            ema50 = close.ewm(span=50).mean().iloc[-1]
            plus_dm = df["high"].diff().clip(lower=0).rolling(14).mean()
            minus_dm = (-df["low"].diff()).clip(lower=0).rolling(14).mean()
            atr = (df["high"] - df["low"]).rolling(14).mean()
            dx = abs(plus_dm - minus_dm) / (plus_dm + minus_dm + 1e-10) * 100
            adx = dx.rolling(14).mean().iloc[-1]
            if adx > trend_threshold and close.iloc[-1] > ema50: trending_up.append(sym)
            elif adx > trend_threshold and close.iloc[-1] < ema50: trending_down.append(sym)
            else: ranging.append(sym)
        total = len(trending_up) + len(trending_down) + len(ranging)
        return {
            "trending_up": trending_up, "trending_down": trending_down, "ranging": ranging,
            "breadth_score": round((len(trending_up) - len(trending_down)) / max(total, 1) * 100, 1),
            "pct_trending": round((len(trending_up) + len(trending_down)) / max(total, 1) * 100, 1),
            "market_mode": "TRENDING" if len(trending_up) + len(trending_down) > len(ranging) else "RANGE-BOUND",
            "bias": "RISK-ON" if len(trending_up) > len(trending_down) * 1.5 else "RISK-OFF" if len(trending_down) > len(trending_up) * 1.5 else "MIXED",
        }

    @staticmethod
    def breadth_divergence(breadth_history: list[dict], index_prices: list[float]) -> dict:
        """Detect divergence between breadth and price index."""
        if len(breadth_history) < 5 or len(index_prices) < 5:
            return {"divergence": "INSUFFICIENT_DATA"}
        recent_breadth = [b["breadth_score"] for b in breadth_history[-5:]]
        breadth_trend = recent_breadth[-1] - recent_breadth[0]
        price_trend = index_prices[-1] - index_prices[0]
        if price_trend > 0 and breadth_trend < -10:
            return {"divergence": "BEARISH", "signal": "Price rising but fewer pairs trending up — rally weakening"}
        elif price_trend < 0 and breadth_trend > 10:
            return {"divergence": "BULLISH", "signal": "Price falling but more pairs turning up — selloff exhausting"}
        return {"divergence": "NONE", "signal": "Breadth confirms price action"}
```

## Interpretation Guide

| Breadth Score | Market Mode | Strategy Implication |
| --- | --- | --- |
| > +60 | Strong risk-on | Trend-following, momentum strategies |
| +20 to +60 | Moderate bullish | Selective breakouts, reduced position size |
| -20 to +20 | Mixed/neutral | Mean reversion, range strategies |
| -60 to -20 | Moderate bearish | Short setups, defensive positioning |
| < -60 | Strong risk-off | Counter-trend caution, hedge existing longs |

## Usage

```python
breadth = MarketBreadthAnalyzer.scan_breadth(pairs_data)
print(f"Market: {breadth['market_mode']} | Bias: {breadth['bias']} | {breadth['pct_trending']}% trending")

div = MarketBreadthAnalyzer.breadth_divergence(breadth_history, dxy_prices)
if div["divergence"] != "NONE":
    print(f"WARNING: {div['divergence']} divergence — {div['signal']}")
```
