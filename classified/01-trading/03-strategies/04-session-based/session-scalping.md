---
name: session-scalping
description: >
  Session-based and short-term strategies: Asian session scalping, session breakouts, scalping
  frameworks, breakout strategies, gap trading, grid trading, end-of-day, and swing trading.
  Opening Range Break & Retest (ORB) — NY session M5/M1/M15 first candle strategy.
  USE FOR: Asian session, London session, New York session, Tokyo session, scalping, scalp trade,
  M1 strategy, session breakout, London breakout, Asian range breakout, NY reversal, gap trading,
  opening gap, gap fill, gap and go, Sunday gap, weekend gap, grid trading, grid bot, DCA grid,
  end of day trading, D1 strategy, swing trade, multi-day hold, H4 setup, pullback entry,
  session overlap, killzone, best time to trade, when is the market most active,
  opening range break, ORB, ORC, first candle strategy, 9:30 AM scalp, opening range retest,
  opening range breakout trap, displacement break, FVG confirmation, NY open scalping.
related_skills:
  - ict-smart-money
  - technical-analysis
  - strategy-selection
  - liquidity-analysis
  - session-scalping
tags:
  - trading
  - strategy
  - scalping
  - orb
  - session
  - ny-open
skill_level: intermediate
kind: reference
category: trading/strategies
status: active
---
> **Skill:** Session Scalping  |  **Domain:** trading  |  **Category:** strategy  |  **Level:** intermediate
> **Tags:** `trading`, `strategy`, `scalping`, `orb`, `session`, `ny-open`


## Asian Session Scalper

# Asian Session Scalper

```python
import pandas as pd, numpy as np

class AsianSessionScalper:
    @staticmethod
    def range_fade(df: pd.DataFrame) -> dict:
        """Fade the range during Tokyo session — buy lows, sell highs of the range."""
        df = df.copy()
        df["hour"] = df.index.hour
        asian = df[(df["hour"] >= 0) & (df["hour"] < 7)]
        if len(asian) < 10: return {"error": "Insufficient Asian data"}
        range_high = asian["high"].rolling(20).max().iloc[-1]
        range_low = asian["low"].rolling(20).min().iloc[-1]
        mid = (range_high + range_low) / 2
        current = df.iloc[-1]["close"]
        atr = (asian["high"] - asian["low"]).mean()
        return {
            "strategy": "asian_range_fade",
            "range_high": round(range_high, 5), "range_low": round(range_low, 5),
            "midpoint": round(mid, 5),
            "signal": "BUY (near range low)" if current < range_low + atr * 0.3 else
                     "SELL (near range high)" if current > range_high - atr * 0.3 else "WAIT (mid-range)",
            "stop_pips": round(atr * 10000 * 1.5, 1),
            "target_pips": round(atr * 10000 * 1.0, 1),
            "best_pairs": ["USDJPY", "EURJPY", "AUDJPY", "AUDNZD"],
            "avoid": ["GBPUSD", "EURUSD (low liquidity in Asia)"],
        }
```


---

## Session Breakout Strategies

# Session Breakout Strategies

```python
import pandas as pd, numpy as np
from datetime import time

class SessionBreakoutStrategies:

    @staticmethod
    def asian_range_breakout(df: pd.DataFrame) -> dict:
        """Trade the breakout of the Asian session range during London open."""
        df = df.copy()
        df["hour"] = df.index.hour
        asian = df[(df["hour"] >= 0) & (df["hour"] < 7)]
        if asian.empty: return {"error": "No Asian session data"}
        asian_high = asian["high"].max()
        asian_low = asian["low"].min()
        asian_range = asian_high - asian_low
        current = df.iloc[-1]
        return {
            "strategy": "asian_range_breakout",
            "asian_high": round(asian_high, 5), "asian_low": round(asian_low, 5),
            "range_pips": round(asian_range * 10000, 1),
            "buy_trigger": round(asian_high, 5), "sell_trigger": round(asian_low, 5),
            "buy_sl": round(asian_low, 5), "sell_sl": round(asian_high, 5),
            "buy_tp": round(asian_high + asian_range, 5), "sell_tp": round(asian_low - asian_range, 5),
            "broken_up": current["close"] > asian_high,
            "broken_down": current["close"] < asian_low,
            "timing": "Place pending orders at 07:00 UTC (London open)",
            "cancel_by": "12:00 UTC if not triggered",
            "best_pairs": ["GBPUSD", "EURUSD", "EURGBP"],
        }

    @staticmethod
    def london_breakout(df: pd.DataFrame) -> dict:
        """Trade first directional move of London session."""
        df = df.copy()
        df["hour"] = df.index.hour
        first_hour = df[(df["hour"] >= 7) & (df["hour"] < 8)]
        if first_hour.empty: return {"error": "No London first hour data"}
        fh_high = first_hour["high"].max()
        fh_low = first_hour["low"].min()
        fh_range = fh_high - fh_low
        current = df.iloc[-1]
        return {
            "strategy": "london_breakout",
            "first_hour_high": round(fh_high, 5), "first_hour_low": round(fh_low, 5),
            "buy_trigger": round(fh_high, 5), "sell_trigger": round(fh_low, 5),
            "target": round(fh_range * 1.5, 5),
            "stop": round(fh_range * 0.75, 5),
            "broken_up": current["close"] > fh_high,
            "broken_down": current["close"] < fh_low,
            "timing": "08:00-10:00 UTC",
            "best_days": "Tuesday, Wednesday, Thursday",
        }

    @staticmethod
    def ny_session_reversal(df: pd.DataFrame) -> dict:
        """NY session often reverses the London move. Fade London direction after NY open."""
        df = df.copy()
        df["hour"] = df.index.hour
        london = df[(df["hour"] >= 7) & (df["hour"] < 13)]
        if london.empty: return {"error": "No London data"}
        london_direction = "UP" if london["close"].iloc[-1] > london["open"].iloc[0] else "DOWN"
        london_move = abs(london["close"].iloc[-1] - london["open"].iloc[0])
        atr = (df["high"] - df["low"]).rolling(14).mean().iloc[-1]
        extended = london_move > 1.5 * atr
        return {
            "strategy": "ny_reversal",
            "london_direction": london_direction,
            "london_move_pips": round(london_move * 10000, 1),
            "extended": extended,
            "signal": f"FADE {london_direction} — sell if London went UP, buy if DOWN" if extended else "WAIT — London move not extended enough",
            "timing": "13:30-15:00 UTC (after NY data releases)",
            "confirmation": "Wait for rejection candle at London extreme before fading",
        }
```


---

## Scalping Framework

# Scalping Framework

## CRITICAL: Only scalp during HIGH LIQUIDITY sessions (London/NY overlap). Spread must be < 1.5 pips.

```python
import pandas as pd
import numpy as np

class ScalpingFramework:

    @staticmethod
    def spread_check(current_spread_pips: float, avg_spread: float) -> dict:
        """Pre-scalp spread validation — never scalp with wide spreads."""
        ratio = current_spread_pips / max(avg_spread, 0.1)
        return {
            "current_spread": current_spread_pips,
            "avg_spread": avg_spread,
            "spread_ratio": round(ratio, 2),
            "can_scalp": current_spread_pips < 1.5 and ratio < 1.5,
            "warning": "SPREAD TOO WIDE — do not scalp" if current_spread_pips > 2.0 else None,
        }

    @staticmethod
    def momentum_burst(df: pd.DataFrame, lookback: int = 5, threshold_mult: float = 2.0) -> dict:
        """Detect sudden momentum bursts for scalp entries."""
        close = df["close"]
        returns = close.pct_change()
        avg_move = returns.rolling(50).std()
        burst = returns.abs() > threshold_mult * avg_move
        direction = np.where(returns > 0, "long", "short")

        current_burst = burst.iloc[-1]
        return {
            "strategy": "momentum_burst_scalp",
            "burst_detected": bool(current_burst),
            "direction": direction[-1] if current_burst else "none",
            "magnitude": round(abs(returns.iloc[-1]) / avg_move.iloc[-1], 1) if avg_move.iloc[-1] > 0 else 0,
            "entry": round(close.iloc[-1], 5),
            "target_pips": round(avg_move.iloc[-1] * 10000 * 1.5, 1),
            "stop_pips": round(avg_move.iloc[-1] * 10000 * 1.0, 1),
            "max_hold_bars": 10,
        }

    @staticmethod
    def ema_cross_scalp(df: pd.DataFrame, fast: int = 5, slow: int = 13) -> dict:
        """Ultra-fast EMA crossover for M1/M5 scalping."""
        close = df["close"]
        ema_fast = close.ewm(span=fast).mean()
        ema_slow = close.ewm(span=slow).mean()
        cross_up = (ema_fast.iloc[-1] > ema_slow.iloc[-1]) and (ema_fast.iloc[-2] <= ema_slow.iloc[-2])
        cross_down = (ema_fast.iloc[-1] < ema_slow.iloc[-1]) and (ema_fast.iloc[-2] >= ema_slow.iloc[-2])

        return {
            "strategy": "ema_cross_scalp",
            "fast_ema": round(ema_fast.iloc[-1], 5),
            "slow_ema": round(ema_slow.iloc[-1], 5),
            "cross_up": cross_up,
            "cross_down": cross_down,
            "signal": "LONG" if cross_up else "SHORT" if cross_down else "WAIT",
            "hold_max_bars": 15,
        }

    @staticmethod
    def scalp_rules() -> dict:
        return {
            "max_hold_time": "15-30 minutes (M1) or 1-2 hours (M5)",
            "max_risk_per_scalp": "0.5% of account (half normal risk)",
            "min_rr": "1:1 minimum (1:1.5 preferred)",
            "session": "London/NY overlap ONLY (13:00-16:00 UTC)",
            "spread_max": "1.5 pips (ideally < 1.0)",
            "pairs": "EURUSD, GBPUSD, USDJPY only (tightest spreads)",
            "stop_after": "3 consecutive losses — take a break",
        }
```


---

## Breakout Strategy Engine

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

## Gap Trading Strategy

# Gap Trading Strategy

```python
import pandas as pd, numpy as np

class GapTradingStrategy:

    @staticmethod
    def detect_gaps(df: pd.DataFrame, min_gap_atr: float = 0.5) -> list[dict]:
        atr = (df["high"] - df["low"]).rolling(14).mean()
        gaps = []
        for i in range(1, len(df)):
            gap = df.iloc[i]["open"] - df.iloc[i-1]["close"]
            if abs(gap) > min_gap_atr * atr.iloc[i]:
                filled = False
                if gap > 0:  # Gap up
                    filled = (df.iloc[i:min(i+20, len(df))]["low"].min() <= df.iloc[i-1]["close"])
                else:  # Gap down
                    filled = (df.iloc[i:min(i+20, len(df))]["high"].max() >= df.iloc[i-1]["close"])
                gaps.append({
                    "time": df.index[i], "gap_pips": round(gap * 10000, 1),
                    "direction": "up" if gap > 0 else "down",
                    "gap_atr": round(abs(gap) / atr.iloc[i], 2),
                    "filled_within_20_bars": filled,
                })
        return gaps

    @staticmethod
    def gap_fill_statistics(df: pd.DataFrame) -> dict:
        gaps = GapTradingStrategy.detect_gaps(df)
        if not gaps: return {"n_gaps": 0}
        fill_rate = sum(1 for g in gaps if g["filled_within_20_bars"]) / len(gaps)
        up_gaps = [g for g in gaps if g["direction"] == "up"]
        down_gaps = [g for g in gaps if g["direction"] == "down"]
        return {
            "n_gaps": len(gaps),
            "fill_rate_pct": round(fill_rate * 100, 1),
            "up_gap_fill_rate": round(sum(1 for g in up_gaps if g["filled_within_20_bars"]) / max(len(up_gaps), 1) * 100, 1),
            "down_gap_fill_rate": round(sum(1 for g in down_gaps if g["filled_within_20_bars"]) / max(len(down_gaps), 1) * 100, 1),
            "avg_gap_size_pips": round(np.mean([abs(g["gap_pips"]) for g in gaps]), 1),
            "strategy": "FADE THE GAP" if fill_rate > 0.65 else "GAP AND GO" if fill_rate < 0.40 else "MIXED — use confirmation",
            "note": f"Gaps fill {fill_rate*100:.0f}% of the time within 20 bars on this pair",
        }

    @staticmethod
    def sunday_gap_trade(friday_close: float, sunday_open: float, atr: float) -> dict:
        gap = sunday_open - friday_close
        return {
            "strategy": "sunday_gap_fade",
            "gap_pips": round(gap * 10000, 1),
            "direction": "SELL (fade gap up)" if gap > 0 else "BUY (fade gap down)",
            "entry": round(sunday_open, 5),
            "target": round(friday_close, 5),
            "stop": round(sunday_open + (gap * 0.5 if gap > 0 else gap * 0.5), 5),
            "note": "Sunday gaps fill ~70% of the time. Use small size due to wide spreads.",
        }
```


---

## Grid Trading Engine

# Grid Trading Engine

```python
import numpy as np

class GridTradingEngine:

    @staticmethod
    def build_grid(center_price: float, range_pct: float = 2.0, n_levels: int = 10,
                   lot_per_level: float = 0.01, grid_type: str = "symmetric") -> dict:
        upper = center_price * (1 + range_pct / 100)
        lower = center_price * (1 - range_pct / 100)
        step = (upper - lower) / (n_levels - 1)
        buy_levels = [{"price": round(lower + i * step, 5), "lots": lot_per_level, "side": "buy"}
                      for i in range(n_levels // 2)]
        sell_levels = [{"price": round(center_price + (i + 1) * step, 5), "lots": lot_per_level, "side": "sell"}
                       for i in range(n_levels // 2)]
        return {
            "strategy": f"grid_{grid_type}",
            "center": round(center_price, 5),
            "range": f"{round(lower, 5)} — {round(upper, 5)}",
            "step_size": round(step, 5),
            "buy_orders": buy_levels,
            "sell_orders": sell_levels,
            "total_lots": round(lot_per_level * n_levels, 2),
            "max_risk": f"All {n_levels // 2} buy levels filled = {round(lot_per_level * n_levels // 2, 2)} lots long",
            "WARNING": "Grid trading has UNLIMITED risk if price trends beyond grid. Always use a master stop-loss.",
        }

    @staticmethod
    def profit_calculator(step_pips: float, lot_per_level: float, pip_value: float = 10.0,
                          fill_rate: float = 0.7) -> dict:
        profit_per_cycle = step_pips * pip_value * lot_per_level
        return {
            "profit_per_grid_cycle": round(profit_per_cycle, 2),
            "estimated_daily_cycles": round(fill_rate * 3, 1),
            "estimated_daily_profit": round(profit_per_cycle * fill_rate * 3, 2),
            "note": "Profits depend on price oscillating within the grid. Trending = losses.",
        }
```


---

## End Of Day Strategy

# End of Day Strategy — Trade Once, Set & Forget

```python
import pandas as pd, numpy as np

class EndOfDayStrategy:
    @staticmethod
    def daily_close_signal(df: pd.DataFrame) -> dict:
        """Complete D1 close analysis — all signals from one daily candle."""
        close = df["close"]
        # Trend filter
        ema50 = close.ewm(span=50).mean()
        ema200 = close.ewm(span=200).mean()
        trend = "UP" if ema50.iloc[-1] > ema200.iloc[-1] else "DOWN"
        # RSI
        delta = close.diff()
        rsi = 100 - 100 / (1 + delta.where(delta > 0, 0).rolling(14).mean() / (-delta.where(delta < 0, 0)).rolling(14).mean().replace(0, np.nan))
        # Pin bar detection
        last = df.iloc[-1]
        body = abs(last["close"] - last["open"])
        total = last["high"] - last["low"]
        upper_wick = last["high"] - max(last["open"], last["close"])
        lower_wick = min(last["open"], last["close"]) - last["low"]
        pin_bull = lower_wick > body * 2 and upper_wick < body * 0.5
        pin_bear = upper_wick > body * 2 and lower_wick < body * 0.5
        # Engulfing
        prev = df.iloc[-2]
        bull_engulf = last["close"] > last["open"] and prev["close"] < prev["open"] and last["close"] > prev["open"] and last["open"] < prev["close"]
        bear_engulf = last["close"] < last["open"] and prev["close"] > prev["open"] and last["open"] > prev["close"] and last["close"] < prev["open"]
        # ATR for stop/target
        atr = (df["high"] - df["low"]).rolling(14).mean().iloc[-1]
        # Signal
        signals = []
        if trend == "UP" and (pin_bull or bull_engulf) and rsi.iloc[-1] < 50:
            signals.append("BUY — trend up + bullish candle + RSI not overbought")
        if trend == "DOWN" and (pin_bear or bear_engulf) and rsi.iloc[-1] > 50:
            signals.append("SELL — trend down + bearish candle + RSI not oversold")
        return {
            "strategy": "end_of_day_d1",
            "trend": trend,
            "rsi": round(rsi.iloc[-1], 1),
            "pin_bar_bullish": pin_bull, "pin_bar_bearish": pin_bear,
            "bullish_engulfing": bull_engulf, "bearish_engulfing": bear_engulf,
            "signals": signals if signals else ["NO SIGNAL — wait for next daily close"],
            "atr_stop": round(atr * 1.5, 5),
            "atr_target": round(atr * 2.5, 5),
            "timing": "Analyze at 22:00 UTC (NY close). Place orders. Walk away.",
            "review": "Check once at next day's close. No intraday monitoring needed.",
        }
```


---

## Swing Trading Framework

# Swing Trading Framework

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class SwingTradingFramework:

    @staticmethod
    def pullback_to_ema(df: pd.DataFrame, trend_ema: int = 50, entry_ema: int = 20) -> dict:
        """Buy pullbacks to EMA in uptrend, sell rallies to EMA in downtrend."""
        close = df["close"]
        ema_trend = close.ewm(span=trend_ema).mean()
        ema_entry = close.ewm(span=entry_ema).mean()
        atr = (df["high"] - df["low"]).rolling(14).mean()
        uptrend = close.iloc[-1] > ema_trend.iloc[-1]
        at_ema = abs(close.iloc[-1] - ema_entry.iloc[-1]) < atr.iloc[-1] * 0.5
        bouncing = close.iloc[-1] > close.iloc[-2] if uptrend else close.iloc[-1] < close.iloc[-2]
        return {
            "strategy": "pullback_to_ema",
            "trend": "UP" if uptrend else "DOWN",
            "at_entry_zone": at_ema,
            "bouncing": bouncing,
            "signal": "BUY PULLBACK" if uptrend and at_ema and bouncing else
                     "SELL RALLY" if not uptrend and at_ema and bouncing else "WAIT",
            "entry": round(ema_entry.iloc[-1], 5),
            "stop": round(ema_entry.iloc[-1] - 2 * atr.iloc[-1], 5) if uptrend else round(ema_entry.iloc[-1] + 2 * atr.iloc[-1], 5),
            "target": round(close.iloc[-1] + 3 * atr.iloc[-1], 5) if uptrend else round(close.iloc[-1] - 3 * atr.iloc[-1], 5),
            "hold_days": "3-10 days typical",
        }

    @staticmethod
    def swing_structure(df: pd.DataFrame, order: int = 5) -> dict:
        """Trade swing highs and lows with structure-based entries."""
        highs = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows = argrelextrema(df["low"].values, np.less, order=order)[0]
        if len(highs) < 2 or len(lows) < 2:
            return {"signal": "INSUFFICIENT SWINGS"}
        hh = df["high"].iloc[highs[-1]] > df["high"].iloc[highs[-2]]
        hl = df["low"].iloc[lows[-1]] > df["low"].iloc[lows[-2]]
        ll = df["low"].iloc[lows[-1]] < df["low"].iloc[lows[-2]]
        lh = df["high"].iloc[highs[-1]] < df["high"].iloc[highs[-2]]
        structure = "UPTREND (HH+HL)" if hh and hl else "DOWNTREND (LH+LL)" if lh and ll else "RANGE"
        return {
            "strategy": "swing_structure",
            "structure": structure,
            "last_swing_high": round(df["high"].iloc[highs[-1]], 5),
            "last_swing_low": round(df["low"].iloc[lows[-1]], 5),
            "signal": "BUY at next HL" if "UP" in structure else "SELL at next LH" if "DOWN" in structure else "RANGE — fade extremes",
        }

    @staticmethod
    def weekly_bias_daily_entry(df_w1: pd.DataFrame, df_d1: pd.DataFrame) -> dict:
        """Set bias from weekly, enter on daily. Classic top-down swing approach."""
        w_close = df_w1["close"]
        w_ema20 = w_close.ewm(span=20).mean()
        weekly_bias = "BULLISH" if w_close.iloc[-1] > w_ema20.iloc[-1] else "BEARISH"
        d_close = df_d1["close"]
        d_rsi = 100 - 100 / (1 + d_close.diff().clip(lower=0).rolling(14).mean() / (-d_close.diff().clip(upper=0)).rolling(14).mean().replace(0, np.nan))
        daily_pullback = (weekly_bias == "BULLISH" and d_rsi.iloc[-1] < 40) or (weekly_bias == "BEARISH" and d_rsi.iloc[-1] > 60)
        return {
            "strategy": "weekly_bias_daily_entry",
            "weekly_bias": weekly_bias,
            "daily_rsi": round(d_rsi.iloc[-1], 1),
            "pullback_zone": daily_pullback,
            "signal": f"BUY — weekly {weekly_bias}, daily RSI oversold" if weekly_bias == "BULLISH" and daily_pullback
                     else f"SELL — weekly {weekly_bias}, daily RSI overbought" if weekly_bias == "BEARISH" and daily_pullback
                     else f"WAIT — bias {weekly_bias} but no pullback",
        }
```

---

## OrderBookImbalance & TapeReading (Enhancement)

Ctrl click to launch VS Code Native REPL

---

## NY Open — Opening Range Break & Retest (ORB)

> Sources: Jdub Trades — 8 videos covering the Opening Range Break strategy in depth.
> Consolidated from: "My Secret 9:30 AM 1 Minute Scalping Strategy", "The Best 9:30 AM 5 Minute Scalping Strategy",
> "My Incredible Easy 1 Minute Scalping Strategy", "The Dark Side Of The First Candle Scalping Strategy",
> "My Simple 5 Minute Scalping Strategy", "Master The Opening Range Break Trading Strategy (5 Minute ORB)",
> "This 1 Minute Scalping Strategy Works Everyday", "My Simple 1 Minute Scalping Strategy To Make $10,000/Month"

### Core Concept

The Opening Range Break & Retest (ORB) is a mechanical scalping strategy based on the first candle of the NY session (9:30 AM EST). It:
- Requires NO daily bias
- Sets up every single day
- Works on stocks, futures, forex, options, crypto
- Targets within first 90 minutes of market open
- Is a break-and-RETEST strategy (NOT a breakout strategy — never chase the break)

### Why the First Candle Matters

- The first candle at 9:30 AM EST has the **highest volume** of the day
- The NY session has the most volatility and liquidity of all sessions
- The opening range establishes the key levels for the morning session
- It tells you the overall direction within the first 90 minutes

### Three-Step Checklist

```
Step 1: MARK the opening range — high + low of the first candle at 9:30 AM EST
Step 2: WAIT for a break with displacement above/below the range
Step 3: ENTER on the retest with confirmation — target 1:2 RR minimum
```

### Choosing the Right Timeframe

| Market Condition | Opening Range TF | Break Confirmation | Entry TF |
|-----------------|-------------------|-------------------|----------|
| Very volatile | M1 | M1 close | M1 |
| Normal | M5 | M1 close | M1 |
| Low volatility / consolidating | M15 | M5 close | M1 |

**M15 Three-TF Model (highest probability for beginners):**
```
M15 → Mark opening range high + low
M5  → Wait for M5 candle close above/below M15 range
M1  → Find entries for continuation (breakout, retest, or reversal)
```

**M5 Two-TF Model (most popular):**
```
M5  → Mark opening range high + low
M1  → Wait for M1 candle close above/below M5 range → retest → enter
```

### The Break — Displacement is MANDATORY

**What counts as displacement:**
- Strong impulsive candle close above/below the range (60%+ body)
- Fair Value Gap / Bullish or Bearish Gap (three-candle sequence with gap between C1 high and C3 low)
- Clear momentum — not a wick poke or slow drift

**What is NOT displacement:**
- Weak candle close with big wicks → likely fake out
- Slow grind above/below with no impulsive move
- Upper/lower wicks testing the range without closing beyond it

### The Retest — Wait for Confirmation

After the displacement break, wait for price to pull back and retest the broken level:

**For longs (broke above range high):**
- Price pulls back to range high area
- Look for: hammerstick candles, lower wicks, buyers stepping in
- Confirmation candle closes bullish above the range high
- Enter long | Stop: below range low (or below confirmation candle for tighter stop)

**For shorts (broke below range low):**
- Price pulls back to range low area
- Look for: upper wicks, sellers stepping in, weak candle closures
- Confirmation candle closes bearish below the range low
- Enter short | Stop: above range high (or above confirmation candle)

### Three Entry Models

**1. Breakout Entry (aggressive)**
- Used when displacement creates a FVG/bullish gap
- Enter on the candle that forms the gap, stop below C2 of the gap
- Best when: very strong trend, HTF draw on target, price unlikely to come back for retest
- Risk: getting caught in a fake out

**2. Break & Retest Entry (preferred)**
- Wait for break → wait for pullback → wait for confirmation at level → enter
- Lowest risk, highest probability
- Stop: just beyond the opposite side of the range
- Target: 1:2 fixed RR, or key levels (LOD/HOD, PDH/PDL, pre-market H/L)

**3. Reversal / Mean Reversion Entry (when ORC fails)**
- If price breaks one direction but fails (no follow-through)
- Look for a break back through the range in the opposite direction
- Wait for CHoCH (change of character) on M1 + displacement
- Enter on retest of the M1 order block/FVG after the reversal
- Common on ranging/choppy days, especially on indices

### Why Most ORB Trades FAIL (Trap Avoidance)

**Three main reasons for failure:**
1. **Chasing the breakout** — buying/selling as soon as price breaks the range without waiting for the retest
2. **No displacement** — entering on weak candle closes without impulsive movement
3. **No confirmation** — entering blindly at the retest level without waiting for price action reaction

**Weak break vs. Strong break (side-by-side):**
```
LOSING TRADE:                    WINNING TRADE:
- Weak candle close at range     - Strong impulsive candle close
- No displacement / no FVG       - Clear FVG / displacement
- Buy immediately                - Wait for retest + confirmation
- Get faked out                   - Enter with tight stop
- Loss                            - Win with 1:2+ RR
```

**Rule: If there's no displacement and no confirmation → NO TRADE.**

### HTF Context Filter (Advanced)

Using the M15 or H1 trend direction dramatically increases win rate:

```
1. Check M15/H1 trend: HH/HL = bullish, LH/LL = bearish
2. If HTF is bullish → only take ORC breaks to the UPSIDE
3. If HTF is bearish → only take ORC breaks to the DOWNSIDE
4. If trend is unclear → trade is still valid but lower conviction
```

**Context avoids the biggest traps:**
- Counter-trend ORC setups have much higher failure rate
- Even a perfect ORC break & retest will fail if the HTF is against you
- Trading with HTF trend = higher probability + ability to hold through pullbacks

### Trade Management

| Action | Level |
|--------|-------|
| Entry | After confirmation candle at retest |
| Stop Loss | Just beyond opposite side of opening range |
| Tight Stop | Below/above the confirmation candle or BOS |
| Partial TP (50%) | LOD/HOD or next swing extreme |
| Final TP | 1:2 fixed RR, or PDH/PDL, or pre-market H/L |
| Time Stop | Close if no movement within 60-90 min of entry |
| BE Stop | Move to breakeven after 1:1 or after partial TP |

**Profit-taking at key levels:** Don't always force a fixed 1:2. Scale at pre-market H/L, PDH/PDL, or other visible levels. Leave runners for 1:2+ if room exists.

### Backtest Results

**SPY (1 week, M5 ORB):** 3W / 1NT / 1 near-loss = 6R total. 50%+ win rate with 2:1 RR.
**TSLA (1 week, M1 ORC):** 3W / 1L / 1NT = +$538 on 100 shares. 75% win rate.
**NQ/MNQ (1 week, M1 ORB → PDH/PDL targets):** ~8W / 3L = +14R total. 73% win rate, avg +1.27R/trade.
**General:** Strategy has ~50-75% win rate with consistent 1:2+ RR = highly profitable over time.

### M1 ORB → PDH/PDL Targeting Variant

> Source: Jdub Trades — "My Simple 1 Minute Scalping Strategy To Make $10,000/Month"

A simplified variant that uses **Previous Day High/Low as the only targets**:

```
Step 1: Daily TF → Mark yesterday's high (PDH) and low (PDL)
         These are liquidity pools — stops and limits cluster at PDH/PDL
Step 2: M1 chart → Mark the FIRST 1-minute candle at 9:30 AM (Opening Range)
Step 3: Wait for displacement break above ORC high → retest → long → target PDH
         OR displacement break below ORC low → retest → short → target PDL
```

**Key differences from standard ORB:**
- **Target is always PDH or PDL** (not fixed RR or nearest swing)
- **No bias required** — trade whichever direction breaks first with displacement
- **Stop = opposite side of the full opening range** (wider but more valid)
- **First trade is highest probability** — second trades have lower win rate
- **Session window: first 2 hours only** (9:30-11:30 AM ET)

**Why PDH/PDL as targets:**
- Institutional liquidity rests above PDH and below PDL (stops from prior day's traders)
- Price is drawn to these levels to fill orders — high-probability magnets
- Provides 2-4R potential on most setups (distance from ORC to PDH/PDL is typically large)

### Implementation

```python
import pandas as pd
import numpy as np
from datetime import time


def detect_opening_range(df_m1: pd.DataFrame, range_tf_minutes: int = 5,
                          session_start: str = "09:30") -> dict:
    """Detect the opening range from M1 data.

    Args:
        df_m1: M1 OHLCV DataFrame with datetime index (EST timezone)
        range_tf_minutes: 1, 5, or 15 — determines the opening range candle size
        session_start: NY session open time

    Returns:
        Dict with range_high, range_low, and candle data
    """
    today = df_m1.index[-1].date()
    open_time = pd.Timestamp(f"{today} {session_start}")
    end_time = open_time + pd.Timedelta(minutes=range_tf_minutes)

    range_candles = df_m1.loc[(df_m1.index >= open_time) & (df_m1.index < end_time)]
    if range_candles.empty:
        return {"error": "No candles found at session open"}

    return {
        "range_high": range_candles["high"].max(),
        "range_low": range_candles["low"].min(),
        "range_size": range_candles["high"].max() - range_candles["low"].min(),
        "open_time": open_time,
        "range_tf": f"M{range_tf_minutes}",
    }


def detect_orb_signal(df_m1: pd.DataFrame, range_high: float, range_low: float,
                       min_displacement_ratio: float = 0.6) -> dict:
    """Detect ORB break, retest, and confirmation signal.

    Args:
        df_m1: M1 candles AFTER the opening range
        range_high: Opening range high
        range_low: Opening range low
        min_displacement_ratio: Body-to-range ratio for displacement (0.6 = 60%)

    Returns:
        Signal dict with direction, entry, stop, and status
    """
    range_size = range_high - range_low
    broke_above = False
    broke_below = False
    break_candle_idx = None
    has_fvg = False

    # Phase 1: Look for displacement break
    for i, (idx, row) in enumerate(df_m1.iterrows()):
        body = abs(row["close"] - row["open"])
        candle_range = row["high"] - row["low"]
        is_displacement = body > candle_range * min_displacement_ratio

        if row["close"] > range_high and is_displacement and not broke_above:
            broke_above = True
            break_candle_idx = i
            # Check for FVG (gap between candle i-1 high and candle i+1 low)
            if i >= 1 and i + 1 < len(df_m1):
                prev_high = df_m1.iloc[i - 1]["high"]
                next_low = df_m1.iloc[i + 1]["low"]
                has_fvg = next_low > prev_high
            break

        if row["close"] < range_low and is_displacement and not broke_below:
            broke_below = True
            break_candle_idx = i
            if i >= 1 and i + 1 < len(df_m1):
                prev_low = df_m1.iloc[i - 1]["low"]
                next_high = df_m1.iloc[i + 1]["high"]
                has_fvg = next_high < prev_low
            break

    if not broke_above and not broke_below:
        return {"signal": "NO_SETUP", "reason": "No displacement break"}

    # Phase 2: Look for retest and confirmation
    post_break = df_m1.iloc[break_candle_idx + 1:]
    if len(post_break) < 2:
        return {"signal": "WAIT", "reason": "Waiting for retest"}

    atr = (df_m1["high"] - df_m1["low"]).mean()
    tol = atr * 0.3

    if broke_above:
        for i, (idx, row) in enumerate(post_break.iterrows()):
            if row["low"] <= range_high + tol:
                # Found retest — check for confirmation
                if i + 1 < len(post_break):
                    confirm = post_break.iloc[i + 1]
                    buyers_in = confirm["close"] > range_high and confirm["close"] > confirm["open"]
                    has_wick = (confirm["close"] - confirm["low"]) > (confirm["high"] - confirm["close"])
                    if buyers_in or has_wick:
                        return {
                            "signal": "BUY",
                            "entry": round(confirm["close"], 5),
                            "stop": round(range_low - atr * 0.1, 5),
                            "tight_stop": round(min(row["low"], confirm["low"]) - atr * 0.1, 5),
                            "tp_1to2": round(confirm["close"] + 2 * (confirm["close"] - range_low), 5),
                            "has_fvg": has_fvg,
                            "displacement": "STRONG" if has_fvg else "MODERATE",
                        }
                return {"signal": "WAIT", "reason": "Retest found, no confirmation yet"}

    if broke_below:
        for i, (idx, row) in enumerate(post_break.iterrows()):
            if row["high"] >= range_low - tol:
                if i + 1 < len(post_break):
                    confirm = post_break.iloc[i + 1]
                    sellers_in = confirm["close"] < range_low and confirm["close"] < confirm["open"]
                    has_wick = (confirm["high"] - confirm["close"]) > (confirm["close"] - confirm["low"])
                    if sellers_in or has_wick:
                        return {
                            "signal": "SELL",
                            "entry": round(confirm["close"], 5),
                            "stop": round(range_high + atr * 0.1, 5),
                            "tight_stop": round(max(row["high"], confirm["high"]) + atr * 0.1, 5),
                            "tp_1to2": round(confirm["close"] - 2 * (range_high - confirm["close"]), 5),
                            "has_fvg": has_fvg,
                            "displacement": "STRONG" if has_fvg else "MODERATE",
                        }
                return {"signal": "WAIT", "reason": "Retest found, no confirmation yet"}

    return {"signal": "NO_SETUP", "reason": "No retest found"}


def choose_orb_timeframe(recent_atr: float, avg_atr_20: float) -> str:
    """Suggest which ORB timeframe based on current volatility.

    Returns: 'M1', 'M5', or 'M15'
    """
    ratio = recent_atr / avg_atr_20 if avg_atr_20 > 0 else 1.0
    if ratio > 1.3:
        return "M1"   # High volatility → tighter range
    elif ratio < 0.7:
        return "M15"  # Low volatility → wider range
    else:
        return "M5"   # Normal → standard
```

### ORB Checklist (Pre-Trade)

```
[] 9:30 AM EST — first candle formed?
[] Opening range H/L marked on chosen TF (M1/M5/M15)?
[] Break occurred with displacement (strong candle close + FVG)?
[] Retest of range level in progress or complete?
[] Confirmation candle (buyers/sellers defending level)?
[] Stop placed beyond opposite side of range?
[] Target ≥ 1:2 RR (or key level: LOD/HOD, PDH/PDL)?
[] HTF context checked? (optional but highly recommended)
[] Time < 11:00 AM EST?
→ ALL YES → ENTER | ANY NO → WAIT or SKIP
```

---

## Previous-Session Liquidity Sweep Model (5-Min)
> Source: "This 5 Minute Scalping Indicator Made Me $27,535" — Nico Trades (80%+ WR claimed)

Uses the PREVIOUS session's high/low as liquidity targets for the CURRENT session. Not ORB — trades the sweep of prior session extremes.

### Core Concept
- Prior session's H/L = liquidity pools (stop-loss clusters)
- After session open, wait for price to sweep ONE side of prior session range
- Trade toward opposite side using FVG disrespect as entry trigger
- Best: NY session sweeping London H/L | Also: London sweeping Asia H/L

### Indicator Setup
- TradingView: **"ICT Kill Zones + Pivots"** by TradeForOP
- For NY: enable London session box only (marks London H/L)
- For London: enable Asia session box only (marks Asia H/L)
- Timeframe: 5-minute chart

### Step-by-Step Execution
```
Step 1: Open 5M chart at session open (9:30 AM EST for NY)
Step 2: Wait for price to sweep ONE side (wick above high or below low)
        Do NOT enter on the sweep itself
Step 3: Find the LAST FVG created during the move toward swept level
Step 4: Wait for candle CLOSE through the FVG (disrespect/inversion)
        - Shorts after high sweep: candle must CLOSE BELOW the bullish FVG
        - Longs after low sweep: candle must CLOSE ABOVE the bearish FVG
        - Mere wick into FVG is NOT sufficient — need body close through it
Step 5: Enter at the close of the candle that disrespected the FVG
Step 6: SL above the FVG (shorts) / below the FVG (longs)
Step 7: TP: the opposite session level (the unswept side)
```

### Key Rules
- High swept → SHORT only (target the low) | Low swept → LONG only (target the high)
- If a NEW FVG forms after the sweep (closer to swept level), use the newest FVG
- No FVG disrespect → NO TRADE
- Both sides swept before entry → invalidated (range-bound day)
- Typical trade duration: ~30 minutes | Typical RR: 3:1

---

## Flip + Sweep Entry Model (1-Min / 5-Min)
> Source: "My 1 Minute Scalping Strategy To Make $16,570/Month" — The Trading Geek

Precision entry combining flip zones with liquidity sweeps. Requires zone FLIP + liquidity sweep before entry.

### Higher Timeframe Narrative (15M) — 3 Questions
```
1. Is price BULLISH or BEARISH? (HH/HL = bullish, LH/LL = bearish)
2. Is price in CONTINUATION or PULLBACK phase?
   - Just created breakout → anticipate pullback
   - Pulling back into zone → anticipate continuation
3. Where is the AVAILABLE LIQUIDITY?
   - Swing lows in uptrend = buy-side liquidity (stops below)
   - Swing highs in downtrend = sell-side liquidity (stops above)
   - This liquidity will be swept BEFORE the real move (inducement)
```

### The Flip + Sweep Entry (5M execution, refine on 1M)
```
Step 1: IDENTIFY FLIP ZONE
  - A supply zone that gets broken becomes demand (flip)
  - OR a demand zone that gets broken becomes supply (flip)

Step 2: WAIT FOR LIQUIDITY SWEEP
  - After flip zone forms, a new swing H/L is created nearby
  - Wait for price to sweep liquidity BEYOND the flip zone

Step 3: CONFIRM MARKET SHIFT
  - After sweep, look for MSS/CHoCH
  - Price must break last internal swing point in opposite direction

Step 4: ENTER AT FLIP + SWEEP ZONE
  - After market shift, wait for retracement to the Flip + Sweep zone
  - Enter on tap | SL: beyond the zone | TP: fixed 3R

Step 5: REFINE ON 1M (advanced)
  - On 1M, refine to just the extreme OB within the zone
  - Tighter stop → 5-7R possible (experienced traders only)
```

### Critical Principle: Inducement
```
Before any real move, price FIRST sweeps obvious liquidity to trap retail
  → Minor pullback swing lows in uptrend = inducement targets
  → Price sweeps these stops, THEN makes the real move
  → "If you cannot identify liquidity, then YOU ARE the liquidity"
  → Always wait for the liquidity sweep before entering
```

---

## One Candle Setup (5-Min ORB Variant with FVG Confirmation)
> Source: "The One Candle Setup" — Cryptic Hustle

Simplified ORB variant with specific differences from the main ORB section above.

### Differences from Main ORB
1. Fixed **2R target** (mechanical, no discretion)
2. FVG sequence must print **OUTSIDE the range** as confirmation
3. No need for retest — enter on the FVG sequence after range break
4. Can hit target in as fast as 4 minutes

### Execution
```
Step 1: Mark H/L of FIRST 5-minute candle at 9:30 AM EST
Step 2: Switch to 1-minute chart
Step 3: Wait for 1M candles to CLOSE outside the 5M range
Step 4: Look for FVG SEQUENCE outside the range:
  - 3-candle pattern where C1 and C3 wicks don't overlap
  - FVG must be PRINTED OUTSIDE the opening range
Step 5: Enter after third candle of FVG sequence closes
  - SL: opposite side of opening range
  - TP: exactly 2R (mechanical)
```

### Key Insight
- Even a very small FVG is valid as long as C1 and C3 wicks don't overlap
- Don't dismiss setups because the gap looks tiny — any FVG confirms displacement

---

## Session Liquidity Cascade Rules (Cross-Video Consensus)

| Trading Session | Liquidity Source | What to Sweep |
|----------------|-----------------|---------------|
| London open | Asia session H/L | Asia high or low |
| NY open (9:30 EST) | London session H/L | London high or low |
| NY afternoon | NY morning H/L | AM session high or low |

**Universal rule**: ALWAYS trade the sweep of the PRIOR session, targeting the opposite side. The session that just ended provides the liquidity pools. The new session's volatility provides the engine.

---

## FVG Disrespect vs FVG Retest (Key Distinction)
> Source: Nico Trades + Cryptic Hustle, cross-referenced

```
FVG RESPECT (continuation):
  - Price taps into FVG, holds, continues in original direction
  - FVG acts as support/resistance → trade WITH the FVG direction

FVG DISRESPECT / INVERSION (reversal signal):
  - Price CLOSES THROUGH the FVG entirely (body close, not just wick)
  - The FVG that was bullish is now bearish (inverted)
  - This is a REVERSAL entry signal — trade AGAINST original FVG direction
  - SL above/below the disrespected FVG
  - Primary entry trigger in the Previous-Session Liquidity Sweep Model
```

**Key rule:** A wick into the FVG without close through = FVG is still respected = no inversion signal.

---

## Scalping Risk Management Rules (Consolidated)
```
- Max 1% risk per scalp trade (funded accounts)
- Fixed RR targets: 2R (One Candle) or 3R (Flip+Sweep, Session Sweep)
- Time stop: If trade hasn't moved within 30-60 minutes → close at market
- One trade per session: these models target ONE high-quality setup, not multiple
- No trade without confirmation: sweeps without FVG disrespect or market shift = SKIP
```

---

## Related Skills

- [Ict Smart Money](../ict-smart-money.md)
- [Technical Analysis](../technical-analysis.md)
- [Strategy Selection](../strategy-selection.md)
- [Liquidity Analysis](../liquidity-analysis.md)
- [Session Strategies](../session-scalping.md)


---

## Swing Trading Framework

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class SwingTradingFramework:

    @staticmethod
    def pullback_to_ema(df: pd.DataFrame, trend_ema: int = 50, entry_ema: int = 20) -> dict:
        """Buy pullbacks to EMA in uptrend, sell rallies to EMA in downtrend."""
        close = df["close"]
        ema_trend = close.ewm(span=trend_ema).mean()
        ema_entry = close.ewm(span=entry_ema).mean()
        atr = (df["high"] - df["low"]).rolling(14).mean()
        uptrend = close.iloc[-1] > ema_trend.iloc[-1]
        at_ema = abs(close.iloc[-1] - ema_entry.iloc[-1]) < atr.iloc[-1] * 0.5
        bouncing = close.iloc[-1] > close.iloc[-2] if uptrend else close.iloc[-1] < close.iloc[-2]
        return {
            "strategy": "pullback_to_ema", "trend": "UP" if uptrend else "DOWN",
            "at_entry_zone": at_ema, "bouncing": bouncing,
            "signal": "BUY PULLBACK" if uptrend and at_ema and bouncing else
                     "SELL RALLY" if not uptrend and at_ema and bouncing else "WAIT",
            "entry": round(ema_entry.iloc[-1], 5),
            "stop": round(ema_entry.iloc[-1] - 2*atr.iloc[-1], 5) if uptrend else round(ema_entry.iloc[-1] + 2*atr.iloc[-1], 5),
            "target": round(close.iloc[-1] + 3*atr.iloc[-1], 5) if uptrend else round(close.iloc[-1] - 3*atr.iloc[-1], 5),
            "hold_days": "3-10 days typical",
        }

    @staticmethod
    def weekly_bias_daily_entry(df_w1: pd.DataFrame, df_d1: pd.DataFrame) -> dict:
        """Set weekly bias, enter on daily pullback. Classic top-down swing approach."""
        w_close = df_w1["close"]
        weekly_bias = "BULLISH" if w_close.iloc[-1] > w_close.ewm(span=20).mean().iloc[-1] else "BEARISH"
        d_close = df_d1["close"]
        d_rsi = 100 - 100 / (1 + d_close.diff().clip(lower=0).rolling(14).mean() /
                             (-d_close.diff().clip(upper=0)).rolling(14).mean().replace(0, np.nan))
        daily_pullback = (weekly_bias == "BULLISH" and d_rsi.iloc[-1] < 40) or (weekly_bias == "BEARISH" and d_rsi.iloc[-1] > 60)
        return {"weekly_bias": weekly_bias, "daily_rsi": round(d_rsi.iloc[-1], 1),
                "pullback_zone": daily_pullback,
                "signal": f"{'BUY' if weekly_bias == 'BULLISH' else 'SELL'} — weekly bias + daily {'oversold' if weekly_bias == 'BULLISH' else 'overbought'}" if daily_pullback else f"WAIT — bias {weekly_bias}, no pullback yet"}
```

## End-of-Day Strategy (D1 Close — Set and Forget)

Analyze at 22:00 UTC (NY close). Place pending orders. Walk away.

```python
class EndOfDayStrategy:

    @staticmethod
    def daily_close_signal(df: pd.DataFrame) -> dict:
        close = df["close"]
        ema50 = close.ewm(span=50).mean(); ema200 = close.ewm(span=200).mean()
        trend = "UP" if ema50.iloc[-1] > ema200.iloc[-1] else "DOWN"
        delta = close.diff()
        rsi = 100 - 100 / (1 + delta.where(delta > 0, 0).rolling(14).mean() /
                           (-delta.where(delta < 0, 0)).rolling(14).mean().replace(0, np.nan))
        last = df.iloc[-1]; prev = df.iloc[-2]
        body = abs(last["close"] - last["open"])
        lower_wick = min(last["open"], last["close"]) - last["low"]
        upper_wick = last["high"] - max(last["open"], last["close"])
        pin_bull = lower_wick > body * 2 and upper_wick < body * 0.5
        pin_bear = upper_wick > body * 2 and lower_wick < body * 0.5
        bull_engulf = last["close"] > last["open"] and prev["close"] < prev["open"] and last["close"] > prev["open"] and last["open"] < prev["close"]
        bear_engulf = last["close"] < last["open"] and prev["close"] > prev["open"] and last["open"] > prev["close"] and last["close"] < prev["open"]
        atr = (df["high"] - df["low"]).rolling(14).mean().iloc[-1]
        signals = []
        if trend == "UP" and (pin_bull or bull_engulf) and rsi.iloc[-1] < 50:
            signals.append("BUY — trend up + bullish candle + RSI not overbought")
        if trend == "DOWN" and (pin_bear or bear_engulf) and rsi.iloc[-1] > 50:
            signals.append("SELL — trend down + bearish candle + RSI not oversold")
        return {"strategy": "end_of_day_d1", "trend": trend, "rsi": round(rsi.iloc[-1], 1),
                "signals": signals or ["NO SIGNAL — wait for next daily close"],
                "atr_stop": round(atr * 1.5, 5), "atr_target": round(atr * 2.5, 5)}
```
