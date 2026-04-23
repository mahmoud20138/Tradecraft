---
name: breakout-strategy-engine
description: >
  Pre-built breakout strategy templates — volatility squeeze detection, range breakout, momentum
  breakout with confirmation filters. Use this skill whenever the user asks about "breakout
  strategy", "Bollinger squeeze", "range breakout", "momentum breakout", "volatility expansion",
  "ATR breakout", "Donchian breakout", "breakout confirmation", "false breakout filter",
  "squeeze momentum", "compression breakout", or any breakout-based trade setup.
  Works with market-regime-classifier, mt5-chart-browser, and risk-and-portfolio.
kind: engine
category: trading/strategies
status: active
tags: [breakout, engine, mt5, regime, risk-and-portfolio, strategies, strategy, trading]
related_skills: [market-regime-classifier, mt5-chart-browser]
---

# Breakout Strategy Engine

## Pre-Built Breakout Strategies with Confirmation Filters

```python
import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class BreakoutSignal:
    symbol: str
    direction: str  # "long" or "short"
    entry: float
    stop_loss: float
    target: float
    strategy: str
    confirmation: list[str]
    strength: float  # 0-1

class BreakoutEngine:

    # ═══════════════════════════════════════
    # 1. BOLLINGER SQUEEZE BREAKOUT
    # ═══════════════════════════════════════
    @staticmethod
    def bollinger_squeeze(df: pd.DataFrame, bb_period: int = 20, kc_period: int = 20,
                          kc_mult: float = 1.5) -> dict:
        """Bollinger inside Keltner Channel = squeeze. Breakout when squeeze releases."""
        close = df["close"]
        bb_mid = close.rolling(bb_period).mean()
        bb_std = close.rolling(bb_period).std()
        bb_upper = bb_mid + 2 * bb_std
        bb_lower = bb_mid - 2 * bb_std

        atr = ((df["high"] - df["low"]).rolling(kc_period).mean())
        kc_upper = bb_mid + kc_mult * atr
        kc_lower = bb_mid - kc_mult * atr

        squeeze_on = (bb_lower > kc_lower) & (bb_upper < kc_upper)
        squeeze_off = ~squeeze_on
        # Squeeze just released
        squeeze_fire = squeeze_off & squeeze_on.shift(1)

        # Direction from momentum
        momentum = close - close.rolling(bb_period).mean()
        direction = np.where(momentum > 0, "long", "short")

        df_out = df.copy()
        df_out["squeeze_on"] = squeeze_on
        df_out["squeeze_fire"] = squeeze_fire
        df_out["direction"] = direction
        df_out["bb_width"] = (bb_upper - bb_lower) / bb_mid * 100

        current = df_out.iloc[-1]
        return {
            "strategy": "bollinger_squeeze",
            "squeeze_active": bool(current["squeeze_on"]),
            "squeeze_firing": bool(current["squeeze_fire"]),
            "direction": current["direction"],
            "bb_width": round(current["bb_width"], 3),
            "bars_in_squeeze": int(squeeze_on.iloc[-20:].sum()),
            "signal": "BREAKOUT FIRING" if current["squeeze_fire"] else
                     "SQUEEZE BUILDING" if current["squeeze_on"] else "NO SQUEEZE",
        }

    # ═══════════════════════════════════════
    # 2. RANGE BREAKOUT (Donchian)
    # ═══════════════════════════════════════
    @staticmethod
    def donchian_breakout(df: pd.DataFrame, period: int = 20, atr_mult: float = 1.5) -> dict:
        """Break above/below N-period high/low with ATR confirmation."""
        high_n = df["high"].rolling(period).max().shift(1)
        low_n = df["low"].rolling(period).min().shift(1)
        atr_val = ((df["high"] - df["low"]).rolling(14).mean())
        close = df["close"]

        long_break = close > high_n
        short_break = close < low_n
        # Volume confirmation
        vol_confirm = df["volume"] > df["volume"].rolling(20).mean() * 1.5

        current = df.iloc[-1]
        return {
            "strategy": "donchian_breakout",
            "upper_channel": round(high_n.iloc[-1], 5),
            "lower_channel": round(low_n.iloc[-1], 5),
            "current_price": round(current["close"], 5),
            "long_breakout": bool(long_break.iloc[-1]),
            "short_breakout": bool(short_break.iloc[-1]),
            "volume_confirmed": bool(vol_confirm.iloc[-1]),
            "atr": round(atr_val.iloc[-1], 5),
            "stop_long": round(high_n.iloc[-1] - atr_mult * atr_val.iloc[-1], 5),
            "stop_short": round(low_n.iloc[-1] + atr_mult * atr_val.iloc[-1], 5),
        }

    # ═══════════════════════════════════════
    # 3. MOMENTUM BREAKOUT
    # ═══════════════════════════════════════
    @staticmethod
    def momentum_breakout(df: pd.DataFrame) -> dict:
        """Multi-filter momentum breakout: ADX + volume + close above/below structure."""
        close = df["close"]
        atr = (df["high"] - df["low"]).rolling(14).mean()
        # ADX proxy
        plus_dm = df["high"].diff().clip(lower=0).rolling(14).mean()
        minus_dm = (-df["low"].diff()).clip(lower=0).rolling(14).mean()
        dx = abs(plus_dm - minus_dm) / (plus_dm + minus_dm + 1e-10) * 100
        adx = dx.rolling(14).mean()
        # Momentum
        mom_10 = close.pct_change(10)
        vol_ratio = df["volume"] / df["volume"].rolling(20).mean()
        # Structure break
        high_20 = df["high"].rolling(20).max()
        low_20 = df["low"].rolling(20).min()

        current = df.iloc[-1]
        filters = []
        if adx.iloc[-1] > 25: filters.append("ADX>25 (trending)")
        if vol_ratio.iloc[-1] > 1.5: filters.append("Volume 1.5x avg")
        if current["close"] > high_20.iloc[-2]: filters.append("New 20-bar high")
        if current["close"] < low_20.iloc[-2]: filters.append("New 20-bar low")
        if abs(mom_10.iloc[-1]) > 0.01: filters.append("Strong 10-bar momentum")

        direction = "long" if mom_10.iloc[-1] > 0 else "short"
        return {
            "strategy": "momentum_breakout",
            "direction": direction,
            "adx": round(adx.iloc[-1], 1),
            "momentum_10": round(mom_10.iloc[-1] * 100, 2),
            "volume_ratio": round(vol_ratio.iloc[-1], 2),
            "confirmations": filters,
            "n_confirmations": len(filters),
            "signal_quality": "A+" if len(filters) >= 4 else "A" if len(filters) >= 3 else "B" if len(filters) >= 2 else "C",
            "atr_stop": round(atr.iloc[-1] * 2, 5),
        }

    # ═══════════════════════════════════════
    # FALSE BREAKOUT FILTER
    # ═══════════════════════════════════════
    @staticmethod
    def false_breakout_probability(df: pd.DataFrame, lookback: int = 100) -> dict:
        """Historical false breakout rate for current pair to calibrate expectations."""
        high_n = df["high"].rolling(20).max().shift(1)
        low_n = df["low"].rolling(20).min().shift(1)
        breakouts = (df["close"] > high_n) | (df["close"] < low_n)
        # A breakout is false if price returns inside range within 5 bars
        false_count = 0
        total = 0
        for i in range(20, len(df) - 5):
            if breakouts.iloc[i]:
                total += 1
                future = df.iloc[i+1:i+6]
                mid = (high_n.iloc[i] + low_n.iloc[i]) / 2
                if (future["close"] < high_n.iloc[i]).any() and (future["close"] > low_n.iloc[i]).any():
                    false_count += 1
        rate = false_count / max(total, 1)
        return {
            "false_breakout_rate": round(rate * 100, 1),
            "total_breakouts": total,
            "recommendation": "Wait for retest" if rate > 0.5 else "Trade breakout with confirmation",
        }

    @staticmethod
    def scan_all(df: pd.DataFrame, symbol: str = "") -> dict:
        return {
            "symbol": symbol,
            "squeeze": BreakoutEngine.bollinger_squeeze(df),
            "donchian": BreakoutEngine.donchian_breakout(df),
            "momentum": BreakoutEngine.momentum_breakout(df),
            "false_breakout_rate": BreakoutEngine.false_breakout_probability(df),
        }
```

---

## Automated Breakout Detection with Liquidity Sweep (CodeTrading Python)

> Source: "Automated Break Out Detection in Python" by CodeTrading (Nov 2025)

### Why Simple Breakouts Fail
A candle closing above a recent high is NOT enough — price often reverts back (fake breakout). A stronger breakout pattern is preceded by a **liquidity sweep**.

### The Liquidity-Confirmed Breakout Pattern

**Bullish breakout with sweep:**
1. Identify pivot highs and pivot lows within a lookback window (e.g., 40 candles)
2. Find the most recent pivot high (resistance level)
3. Check if a pivot low formed AFTER that high AND is **lower than all previous pivot lows** in the window = liquidity sweep
4. Current candle closes above the pivot high AND previous candle was below it = **breakout confirmed**
5. Filter: only take bullish breakouts when last 15 candles are ALL above EMA (trend confirmation)

**Bearish breakout with sweep:** Mirror logic — pivot low → higher high sweep → breakdown below pivot low

### Python Implementation Details

**Pivot Detection (no look-ahead bias):**
```python
def mark_pivots(df, window=7, high_col='high', low_col='low'):
    # Compare candle high to W neighbors left AND right
    # Pivot high: higher than all W neighbors
    # Pivot low: lower than all W neighbors
    # CRITICAL: stop at current_candle - window + 1 to avoid future data
```

**Breakout Detection Function:**
```python
def detect_breakout(candle_idx, back_candles=40, window=5):
    # 1. Find pivots in [candle_idx - back_candles : candle_idx - window + 1]
    # 2. Find last pivot high value
    # 3. Check if close[candle_idx] > pivot_high AND close[candle_idx-1] < pivot_high
    # 4. Find pivot low between last_pivot_high and breakout candle
    # 5. Confirm pivot_low < min(all previous pivot lows) = SWEEP
    # Return: 2 = bullish breakout, 1 = bearish breakout, 0 = no signal
```

**Trend Filter (EMA-based):**
- Check if last N candles (e.g., 15) are ALL above EMA → uptrend → only bullish breakouts
- ALL below EMA → downtrend → only bearish breakouts
- Adjustable selectivity: 10, 15, 20, 25 candles

### Backtest Results (EURUSD, 20 years hourly data, 2003-2023)

**Optimization surface (TP/SL ratio vs ATR multiplier):**
- Best zone: TP/SL ratio 4-5x, ATR multiplier 4+
- Returns: 5-52% depending on parameters (no leverage, no commission)
- Drawdown minimized at ATR mult ~1, TP/SL ~1 (but returns limited to 5-8%)

### Key Parameters
```python
back_candles = 40     # Lookback window for pattern detection
pivot_window = 5-7    # Neighbors for pivot detection
ema_candles = 15      # Candles for trend confirmation
atr_mult = 1-5        # Stop loss = ATR * multiplier
tp_sl_ratio = 1-5     # Take profit / stop loss ratio
```

### Usage Recommendation
- Best as an **alert indicator** — bot detects pattern, human manages trade
- Run simultaneously on multiple assets to multiply signal count without losing precision
- Trade management (TP/SL optimization) is asset-specific — needs tuning per instrument

See also: `smart-money-trap-detector` (fake breakout detection), `liquidity-order-flow-mapper`, `chart-pattern-scanner`
