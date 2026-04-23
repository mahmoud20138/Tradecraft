---
name: pair-scanner-screener
description: >
  Scan all available pairs for specific technical conditions — overbought, oversold, breakout,
  squeeze, divergence, pattern match. Use for "scan all pairs", "screener", "find setups",
  "which pairs have RSI oversold", "scan for breakouts", "find squeeze setups", "market scan",
  "pair filter", "setup scanner", "opportunity finder", or any multi-pair screening.
  Works with mt5-chart-browser for data and all strategy/indicator skills for conditions.
kind: reference
category: trading/market-context
status: active
tags: [breakout, market-context, mt5, pair, scanner, screener, trading]
related_skills: [cross-asset-relationships, correlation-crisis, correlation-regime-switcher, mt5-chart-browser, multi-pair-basket-trader]
---

# Pair Scanner & Screener

```python
import pandas as pd, numpy as np
from typing import Callable

class PairScanner:

    @staticmethod
    def scan(pairs_data: dict, conditions: list[dict]) -> list[dict]:
        """
        Scan all pairs against a list of conditions.
        pairs_data: {"EURUSD": df, "GBPUSD": df, ...}
        conditions: [{"name": "RSI_oversold", "fn": lambda df: rsi(df) < 30}, ...]
        """
        results = []
        for symbol, df in pairs_data.items():
            if df.empty or len(df) < 50: continue
            matches = []
            for cond in conditions:
                try:
                    if cond["fn"](df):
                        matches.append(cond["name"])
                except: continue
            if matches:
                results.append({
                    "symbol": symbol,
                    "conditions_met": matches,
                    "n_conditions": len(matches),
                    "score": len(matches) / len(conditions),
                })
        return sorted(results, key=lambda r: r["n_conditions"], reverse=True)

    @staticmethod
    def preset_scans() -> dict:
        """Pre-built scan conditions for common setups."""
        def _rsi(df, period=14):
            d = df["close"].diff()
            g = d.where(d > 0, 0).rolling(period).mean()
            l = (-d.where(d < 0, 0)).rolling(period).mean()
            return (100 - 100 / (1 + g / l.replace(0, np.nan))).iloc[-1]

        return {
            "oversold_bounce": [
                {"name": "RSI<30", "fn": lambda df: _rsi(df) < 30},
                {"name": "above_SMA200", "fn": lambda df: df["close"].iloc[-1] > df["close"].rolling(200).mean().iloc[-1]},
                {"name": "bullish_candle", "fn": lambda df: df["close"].iloc[-1] > df["open"].iloc[-1]}],
            "overbought_fade": [
                {"name": "RSI>70", "fn": lambda df: _rsi(df) > 70},
                {"name": "below_SMA200", "fn": lambda df: df["close"].iloc[-1] < df["close"].rolling(200).mean().iloc[-1]},
                {"name": "bearish_candle", "fn": lambda df: df["close"].iloc[-1] < df["open"].iloc[-1]}],
            "breakout_candidate": [
                {"name": "BB_squeeze", "fn": lambda df: (df["close"].rolling(20).std().iloc[-1] / df["close"].rolling(20).mean().iloc[-1]) < 0.005},
                {"name": "volume_rising", "fn": lambda df: df["volume"].iloc[-1] > df["volume"].rolling(20).mean().iloc[-1] * 1.3},
                {"name": "near_20bar_high", "fn": lambda df: df["close"].iloc[-1] > df["high"].rolling(20).max().iloc[-2] * 0.998}],
            "trend_pullback": [
                {"name": "above_EMA50", "fn": lambda df: df["close"].iloc[-1] > df["close"].ewm(span=50).mean().iloc[-1]},
                {"name": "touching_EMA20", "fn": lambda df: abs(df["close"].iloc[-1] - df["close"].ewm(span=20).mean().iloc[-1]) < (df["high"] - df["low"]).rolling(14).mean().iloc[-1] * 0.5},
                {"name": "RSI_40_60", "fn": lambda df: 40 < _rsi(df) < 60}],
        }

    @staticmethod
    def quick_scan(pairs_data: dict, scan_name: str = "oversold_bounce") -> list[dict]:
        presets = PairScanner.preset_scans()
        conditions = presets.get(scan_name, presets["oversold_bounce"])
        return PairScanner.scan(pairs_data, conditions)
```


---
