---
name: mtf-confluence-scorer
description: >
  Scores multi-timeframe alignment and outputs confluence heat maps. Use this skill whenever
  the user asks about "multi-timeframe analysis", "MTF confluence", "timeframe alignment",
  "higher timeframe bias", "are timeframes aligned", "confluence score", "top-down analysis",
  "HTF/LTF alignment", "which timeframes agree", "heat map", or any question about whether
  multiple timeframes support the same directional bias. Works with mt5-chart-browser for data
  and trading-brain for trade decisions.
kind: reference
category: trading/strategies
status: active
tags: [analysis, confluence, mt5, mtf, scorer, trading]
related_skills: [price-action, xtrading-analyze, capitulation-mean-reversion, mt5-chart-browser, poc-bounce-strategy]
---

# Multi-Timeframe Confluence Scorer

## Overview
Systematic top-down analysis across multiple timeframes. Scores directional agreement
between timeframes and produces a confluence heat map. Higher confluence = higher probability.

---

## 1. Single Timeframe Bias Calculator

```python
import pandas as pd
import numpy as np

def timeframe_bias(df: pd.DataFrame) -> dict:
    """
    Calculate directional bias for a single timeframe.
    Uses: MA alignment, RSI, MACD, price position relative to structure.
    Returns score from -1 (strong bearish) to +1 (strong bullish).
    """
    close = df["close"]
    scores = []

    # MA alignment
    sma20 = close.rolling(20).mean().iloc[-1]
    sma50 = close.rolling(50).mean().iloc[-1] if len(close) >= 50 else sma20
    ema10 = close.ewm(span=10).mean().iloc[-1]
    current = close.iloc[-1]

    if current > sma20 > sma50: scores.append(1.0)
    elif current < sma20 < sma50: scores.append(-1.0)
    elif current > sma20: scores.append(0.3)
    elif current < sma20: scores.append(-0.3)
    else: scores.append(0)

    # RSI
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rs = gain / loss.replace(0, np.nan)
    rsi = (100 - (100 / (1 + rs))).iloc[-1]
    if rsi > 60: scores.append(0.5)
    elif rsi < 40: scores.append(-0.5)
    else: scores.append(0)

    # MACD
    fast = close.ewm(span=12).mean()
    slow = close.ewm(span=26).mean()
    macd_line = (fast - slow).iloc[-1]
    signal = (fast - slow).ewm(span=9).mean().iloc[-1]
    if macd_line > signal and macd_line > 0: scores.append(0.7)
    elif macd_line < signal and macd_line < 0: scores.append(-0.7)
    elif macd_line > signal: scores.append(0.3)
    elif macd_line < signal: scores.append(-0.3)
    else: scores.append(0)

    # Price position in recent range
    high_20 = df["high"].tail(20).max()
    low_20 = df["low"].tail(20).min()
    position = (current - low_20) / (high_20 - low_20) if high_20 != low_20 else 0.5
    scores.append(position - 0.5)  # center at 0

    bias_score = np.mean(scores)
    return {
        "score": round(bias_score, 3),
        "direction": "BULLISH" if bias_score > 0.2 else "BEARISH" if bias_score < -0.2 else "NEUTRAL",
        "strength": "strong" if abs(bias_score) > 0.5 else "moderate" if abs(bias_score) > 0.2 else "weak",
        "rsi": round(rsi, 1),
        "macd_signal": "bullish" if macd_line > signal else "bearish",
        "price_vs_sma20": "above" if current > sma20 else "below",
    }
```

---

## 2. Multi-Timeframe Confluence Engine

```python
# TF weights: higher timeframes carry more weight
TF_WEIGHTS = {
    "MN1": 1.5, "W1": 1.3, "D1": 1.2, "H4": 1.0,
    "H1": 0.8, "M30": 0.6, "M15": 0.5, "M5": 0.4, "M1": 0.2,
}

def confluence_score(
    data_by_tf: dict,  # {"H1": df_h1, "H4": df_h4, "D1": df_d1, ...}
    symbol: str = ""
) -> dict:
    """
    Score multi-timeframe confluence.
    Higher score = more timeframes agree on direction.
    """
    tf_results = {}
    weighted_sum = 0
    total_weight = 0

    for tf, df in data_by_tf.items():
        if df.empty or len(df) < 50:
            continue
        bias = timeframe_bias(df)
        weight = TF_WEIGHTS.get(tf, 0.5)
        tf_results[tf] = {**bias, "weight": weight}
        weighted_sum += bias["score"] * weight
        total_weight += weight

    overall_score = weighted_sum / max(total_weight, 1e-10)

    # Count agreements
    bullish_tfs = [tf for tf, r in tf_results.items() if r["direction"] == "BULLISH"]
    bearish_tfs = [tf for tf, r in tf_results.items() if r["direction"] == "BEARISH"]
    neutral_tfs = [tf for tf, r in tf_results.items() if r["direction"] == "NEUTRAL"]
    agreement_pct = max(len(bullish_tfs), len(bearish_tfs)) / max(len(tf_results), 1) * 100

    return {
        "symbol": symbol,
        "overall_score": round(overall_score, 3),
        "direction": "BULLISH" if overall_score > 0.15 else "BEARISH" if overall_score < -0.15 else "NEUTRAL",
        "confluence_pct": round(agreement_pct, 1),
        "strength": "STRONG" if agreement_pct >= 75 else "MODERATE" if agreement_pct >= 50 else "WEAK",
        "bullish_timeframes": bullish_tfs,
        "bearish_timeframes": bearish_tfs,
        "neutral_timeframes": neutral_tfs,
        "timeframe_details": tf_results,
        "trade_recommendation": _trade_recommendation(overall_score, agreement_pct),
    }

def _trade_recommendation(score: float, agreement: float) -> str:
    if agreement >= 75 and abs(score) > 0.3:
        return f"STRONG {'BUY' if score > 0 else 'SELL'} — {agreement:.0f}% TF agreement, full position"
    if agreement >= 60 and abs(score) > 0.2:
        return f"MODERATE {'BUY' if score > 0 else 'SELL'} — {agreement:.0f}% agreement, reduced size"
    if agreement < 50:
        return "NO TRADE — timeframes disagree, wait for alignment"
    return "WEAK signal — consider only with additional confirmation"

def multi_pair_confluence_scan(
    pairs_data: dict,  # {"EURUSD": {"H1": df, "H4": df, "D1": df}, "GBPUSD": ...}
) -> pd.DataFrame:
    """Scan multiple pairs for best confluence opportunities."""
    results = []
    for symbol, tf_data in pairs_data.items():
        score = confluence_score(tf_data, symbol)
        results.append({
            "symbol": symbol,
            "score": score["overall_score"],
            "direction": score["direction"],
            "confluence_pct": score["confluence_pct"],
            "strength": score["strength"],
            "recommendation": score["trade_recommendation"],
        })
    return pd.DataFrame(results).sort_values("confluence_pct", ascending=False)
```

---

## 3. Confluence Heat Map Data

```python
def generate_heatmap_data(pairs_data: dict) -> dict:
    """Generate data for visual heat map rendering."""
    matrix = {}
    for symbol, tf_data in pairs_data.items():
        matrix[symbol] = {}
        for tf, df in tf_data.items():
            if not df.empty and len(df) >= 20:
                bias = timeframe_bias(df)
                matrix[symbol][tf] = bias["score"]
    return {
        "matrix": matrix,
        "color_scale": "green (+1) → white (0) → red (-1)",
        "timeframes": list(TF_WEIGHTS.keys()),
        "symbols": list(pairs_data.keys()),
    }
```


---
