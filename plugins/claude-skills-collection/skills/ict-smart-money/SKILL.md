---
name: ict-smart-money
description: >
  ICT (Inner Circle Trader) Smart Money Concepts — full methodology reference by Michael J.
  Huddleston. Covers market structure (BOS/CHoCH/MSS), order blocks, smart money traps,
  supply/demand zones, Wyckoff method, institutional behavior, order flow delta analysis,
  power of 3, AMD accumulation manipulation distribution, PD arrays, killzones, silver bullet,
  judas swing, optimal trade entry OTE, liquidity BSL SSL, fair value gap FVG, inverse FVG IFVG,
  CISD change in state of delivery, breaker blocks, IPDA, NWOG new week opening gap, SMT
  divergence, market maker model MMBM MMSM, unicorn model, ICT 2022 model, multi-timeframe
  analysis, London killzone, New York killzone, confluence scoring, premium discount zones,
  institutional footprint, MQL5 indicator development, AdvanceSMC, ICT_OB_BB_Detector, SMC_FVG.
  USE FOR: ICT, smart money, SMC, order block, BOS, CHoCH, change of character, break of
  structure, market structure shift, MSS, fair value gap, FVG, liquidity sweep, stop hunt,
  buy-side liquidity, sell-side liquidity, breaker block, supply demand zones, Wyckoff
  accumulation distribution, institutional order flow, order flow delta, cumulative delta,
  footprint chart, absorption, composite man, Wyckoff schematic, power of 3, AMD, killzones,
  silver bullet, judas swing, OTE, PD arrays, IPDA, NWOG, SMT divergence, market maker model,
  unicorn model, ICT 2022 model, confluence scoring, risk management, pre-trade checklist,
  MQL5 indicators, prop firm model.
related_skills:
  - session-scalping
  - technical-analysis
  - liquidity-analysis
  - price-action
  - market-regime-classifier
  - strategy-selection
tags:
  - trading
  - strategy
  - ict
  - smc
  - liquidity
  - orderflow
  - fvg
  - orderblock
skill_level: advanced
kind: reference
category: trading/strategies
status: active
aliases: [ict-smc]
---
> **Skill:** Ict Smart Money  |  **Domain:** trading  |  **Category:** strategy  |  **Level:** advanced
> **Tags:** `trading`, `strategy`, `ict`, `smc`, `liquidity`, `orderflow`, `fvg`, `orderblock`


## Market Structure Bos Choch

# Market Structure — BOS & CHoCH

```python
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
from functools import lru_cache
from typing import Optional
from dataclasses import dataclass, field

# ── Validation helpers ──────────────────────────────────────────────────────

def _validate_ohlcv(df: pd.DataFrame, min_bars: int = 20) -> None:
    """Raise ValueError if df is missing required OHLCV columns or too short."""
    required = {"open", "high", "low", "close"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"DataFrame missing columns: {missing}")
    if len(df) < min_bars:
        raise ValueError(f"Need at least {min_bars} bars, got {len(df)}")
    if (df["high"] < df["low"]).any():
        raise ValueError("Data integrity error: high < low detected")

def _atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """True-range ATR — fully vectorized, NaN-safe."""
    hl  = df["high"] - df["low"]
    hcp = (df["high"] - df["close"].shift(1)).abs()
    lcp = (df["low"]  - df["close"].shift(1)).abs()
    tr  = pd.concat([hl, hcp, lcp], axis=1).max(axis=1)
    return tr.rolling(period, min_periods=1).mean()


# ── Market Structure ────────────────────────────────────────────────────────

class MarketStructure:
    """
    Detects Break of Structure (BOS) and Change of Character (CHoCH)
    using scipy argrelextrema for swing point identification.

    Example
    -------
    >>> result = MarketStructure.analyze(df, order=5)
    >>> print(result["current_structure"])
    'BULLISH (HH+HL)'
    """

    @staticmethod
    def analyze(df: pd.DataFrame, order: int = 5) -> dict:
        """
        Parameters
        ----------
        df    : OHLCV DataFrame with DatetimeIndex
        order : window size for swing-point detection (default 5)

        Returns
        -------
        dict with keys: current_structure, swing_highs, swing_lows,
                        recent_events, latest_event, bias_score (-1..+1)
        """
        _validate_ohlcv(df, min_bars=order * 4)

        high_vals = df["high"].values
        low_vals  = df["low"].values

        highs_idx = argrelextrema(high_vals, np.greater_equal, order=order)[0]
        lows_idx  = argrelextrema(low_vals,  np.less_equal,    order=order)[0]

        # Deduplicate consecutive equal extrema
        highs_idx = highs_idx[np.diff(highs_idx, prepend=-999) > 1]
        lows_idx  = lows_idx [np.diff(lows_idx,  prepend=-999) > 1]

        swing_highs = [(int(i), float(high_vals[i])) for i in highs_idx]
        swing_lows  = [(int(i), float(low_vals[i]))  for i in lows_idx]
        events: list[dict] = []

        # ── BOS detection (vectorised comparison) ──
        for i in range(1, len(swing_highs)):
            if swing_highs[i][1] > swing_highs[i - 1][1]:
                events.append({
                    "type":    "BOS_BULLISH",
                    "idx":     swing_highs[i][0],
                    "price":   round(swing_highs[i][1], 5),
                    "meaning": "Break of Structure UP — bullish continuation",
                })

        for i in range(1, len(swing_lows)):
            if swing_lows[i][1] < swing_lows[i - 1][1]:
                events.append({
                    "type":    "BOS_BEARISH",
                    "idx":     swing_lows[i][0],
                    "price":   round(swing_lows[i][1], 5),
                    "meaning": "Break of Structure DOWN — bearish continuation",
                })

        # ── CHoCH detection ──
        for i in range(1, min(len(swing_highs), len(swing_lows))):
            prev_trend_up  = (i >= 2 and swing_highs[i - 1][1] > swing_highs[i - 2][1]) or i < 2
            curr_break_dn  = swing_lows[i][1] < swing_lows[i - 1][1]
            prev_trend_dn  = (i >= 2 and swing_lows[i - 1][1] < swing_lows[i - 2][1]) or i < 2
            curr_break_up  = swing_highs[i][1] > swing_highs[i - 1][1]

            if prev_trend_up and curr_break_dn:
                events.append({
                    "type":    "CHoCH_BEARISH",
                    "idx":     swing_lows[i][0],
                    "price":   round(swing_lows[i][1], 5),
                    "meaning": "Change of Character — trend shifting bearish",
                })
            if prev_trend_dn and curr_break_up:
                events.append({
                    "type":    "CHoCH_BULLISH",
                    "idx":     swing_highs[i][0],
                    "price":   round(swing_highs[i][1], 5),
                    "meaning": "Change of Character — trend shifting bullish",
                })

        # ── Current structure ──
        if len(swing_highs) >= 2 and len(swing_lows) >= 2:
            hh = swing_highs[-1][1] > swing_highs[-2][1]
            hl = swing_lows[-1][1]  > swing_lows[-2][1]
            lh = swing_highs[-1][1] < swing_highs[-2][1]
            ll = swing_lows[-1][1]  < swing_lows[-2][1]
            structure = ("BULLISH (HH+HL)"  if hh and hl  else
                         "BEARISH (LH+LL)"  if lh and ll  else
                         "TRANSITIONING")
        else:
            structure = "INSUFFICIENT DATA"

        # Bias score: fraction of recent BOS events that are bullish
        recent = sorted(events, key=lambda e: e["idx"])[-10:]
        bull_n = sum(1 for e in recent if "BULLISH" in e["type"])
        bear_n = sum(1 for e in recent if "BEARISH" in e["type"])
        bias_score = round((bull_n - bear_n) / max(bull_n + bear_n, 1), 3)

        return {
            "current_structure": structure,
            "swing_highs":       swing_highs[-5:],
            "swing_lows":        swing_lows[-5:],
            "recent_events":     sorted(events, key=lambda e: e["idx"])[-5:],
            "latest_event":      events[-1] if events else None,
            "bias_score":        bias_score,   # +1 = fully bullish, -1 = fully bearish
        }
```


---

## Multi Tf Order Block Mapper

# Multi-TF Order Block Mapper

```python
import pandas as pd
import numpy as np
from typing import Optional

class MultiTFOrderBlockMapper:
    """
    Detects ICT order blocks across multiple timeframes and identifies
    price-level confluences where OBs from different TFs overlap.

    Example
    -------
    >>> result = MultiTFOrderBlockMapper.map_obs_across_tfs(
    ...     {"H1": df_h1, "H4": df_h4}, atr_mult=1.5
    ... )
    >>> print(result["n_confluences"])
    3
    """

    # TF weight for strength scoring (higher = more significant)
    TF_WEIGHTS: dict[str, float] = {
        "M5": 0.3, "M15": 0.4, "M30": 0.5,
        "H1": 0.7, "H4": 0.9, "D1": 1.0, "W1": 1.2,
    }

    @staticmethod
    def _detect_obs_single_tf(
        df: pd.DataFrame,
        tf: str,
        atr_mult: float = 1.5,
        lookback: int = 5,
    ) -> list[dict]:
        """
        Detect order blocks on a single timeframe DataFrame.

        An order block is the last opposing candle before a strong impulsive move.
        - Bullish OB  : bearish candle immediately before a strong bullish move
        - Bearish OB  : bullish candle immediately before a strong bearish move
        """
        if df.empty or len(df) < 20:
            return []

        # Vectorised ATR
        hl    = df["high"] - df["low"]
        hcp   = (df["high"] - df["close"].shift(1)).abs()
        lcp   = (df["low"]  - df["close"].shift(1)).abs()
        atr   = pd.concat([hl, hcp, lcp], axis=1).max(axis=1).rolling(14, min_periods=1).mean()

        opens  = df["open"].values
        closes = df["close"].values
        highs  = df["high"].values
        lows   = df["low"].values
        atr_v  = atr.values
        times  = df.index

        obs: list[dict] = []
        n = len(df)

        for i in range(2, n - 1):
            move      = df.iloc[i + 1] if i + 1 < n else df.iloc[i]
            move_size = abs(move["close"] - move["open"])
            threshold = atr_mult * atr_v[i]

            if move_size <= threshold:
                continue

            ob_top    = max(opens[i], closes[i])
            ob_bottom = min(opens[i], closes[i])
            ob_mid    = (ob_top + ob_bottom) / 2

            # Bullish OB: bearish candle → strong bullish move
            if closes[i] < opens[i] and move["close"] > move["open"]:
                obs.append({
                    "type":       "bullish",
                    "top":        round(ob_top, 5),
                    "bottom":     round(ob_bottom, 5),
                    "midpoint":   round(ob_mid, 5),
                    "tf":         tf,
                    "time":       times[i],
                    "atr_ratio":  round(move_size / max(atr_v[i], 1e-10), 2),
                    "valid":      True,   # becomes False when price trades through OB
                })
            # Bearish OB: bullish candle → strong bearish move
            elif closes[i] > opens[i] and move["close"] < move["open"]:
                obs.append({
                    "type":       "bearish",
                    "top":        round(ob_top, 5),
                    "bottom":     round(ob_bottom, 5),
                    "midpoint":   round(ob_mid, 5),
                    "tf":         tf,
                    "time":       times[i],
                    "atr_ratio":  round(move_size / max(atr_v[i], 1e-10), 2),
                    "valid":      True,
                })

        # Mark OBs as invalidated if price has traded through them since formation
        current_price = float(closes[-1])
        for ob in obs:
            if ob["type"] == "bullish" and current_price < ob["bottom"]:
                ob["valid"] = False
            elif ob["type"] == "bearish" and current_price > ob["top"]:
                ob["valid"] = False

        # Return only valid OBs, most recent first
        valid_obs = [ob for ob in obs if ob["valid"]]
        return valid_obs[-lookback:]

    @staticmethod
    def map_obs_across_tfs(
        data_by_tf: dict[str, pd.DataFrame],
        atr_mult: float = 1.5,
        lookback: int = 5,
        detect_fn: Optional[object] = None,    # kept for backward-compatibility
    ) -> dict:
        """
        Map order blocks from each TF and find multi-TF price confluences.

        Parameters
        ----------
        data_by_tf : {"H1": df, "H4": df, ...}
        atr_mult   : impulse move must exceed ATR × this multiplier
        lookback   : OBs to keep per timeframe

        Returns
        -------
        {obs_by_tf, confluences, n_confluences, strongest_confluence}
        """
        all_obs: dict[str, list] = {}

        for tf, df in data_by_tf.items():
            try:
                _validate_ohlcv(df, min_bars=20)
                obs = MultiTFOrderBlockMapper._detect_obs_single_tf(df, tf, atr_mult, lookback)
            except (ValueError, KeyError):
                obs = []
            all_obs[tf] = obs

        # ── Find price-level confluences ──────────────────────────────────────
        confluences: list[dict] = []
        flat_obs = [(tf, ob) for tf, obs_list in all_obs.items() for ob in obs_list]
        tf_weight = MultiTFOrderBlockMapper.TF_WEIGHTS

        for i, (tf_a, ob_a) in enumerate(flat_obs):
            for tf_b, ob_b in flat_obs[i + 1:]:
                if tf_a == tf_b or ob_a["type"] != ob_b["type"]:
                    continue
                overlap = (min(ob_a["top"], ob_b["top"])
                           - max(ob_a["bottom"], ob_b["bottom"]))
                if overlap > 0:
                    w_a = tf_weight.get(tf_a, 0.5)
                    w_b = tf_weight.get(tf_b, 0.5)
                    strength_score = round((w_a + w_b) / 2 * (1 + overlap), 3)
                    confluences.append({
                        "tf_pair":      f"{tf_a}+{tf_b}",
                        "type":         ob_a["type"],
                        "zone_top":     round(min(ob_a["top"], ob_b["top"]), 5),
                        "zone_bottom":  round(max(ob_a["bottom"], ob_b["bottom"]), 5),
                        "overlap":      round(overlap, 5),
                        "strength_score": strength_score,
                        "grade":        ("A+" if strength_score > 1.2 else
                                         "A"  if strength_score > 0.8 else "B"),
                    })

        confluences.sort(key=lambda c: c["strength_score"], reverse=True)

        return {
            "obs_by_tf":           all_obs,
            "confluences":         confluences,
            "n_confluences":       len(confluences),
            "strongest_confluence": confluences[0] if confluences else None,
        }
```


---

## Smart Money Trap Detector

# Smart Money Trap Detector

```python
import pandas as pd
import numpy as np

class TrapDetector:
    """
    Detects bull and bear smart-money traps using wick-size and
    range-breakout logic. Includes historical calibration helper.

    Example
    -------
    >>> traps = TrapDetector.detect_traps(df, lookback=20)
    >>> prob  = TrapDetector.trap_probability(df)
    """

    @staticmethod
    def detect_traps(df: pd.DataFrame, lookback: int = 20) -> list[dict]:
        """
        Scan for liquidity sweeps (smart-money traps).

        Parameters
        ----------
        df       : OHLCV DataFrame
        lookback : rolling window for resistance/support levels

        Returns
        -------
        List of trap dicts, capped at the 10 most recent.
        """
        _validate_ohlcv(df, min_bars=lookback + 2)

        atr     = _atr(df)
        high_n  = df["high"].rolling(lookback).max().shift(1)   # previous high
        low_n   = df["low"].rolling(lookback).min().shift(1)    # previous low

        highs   = df["high"].values
        lows    = df["low"].values
        opens   = df["open"].values
        closes  = df["close"].values
        atr_v   = atr.values
        hi_n_v  = high_n.values
        lo_n_v  = low_n.values
        times   = df.index

        traps: list[dict] = []

        for i in range(lookback + 1, len(df)):
            atr_i = atr_v[i]
            if np.isnan(atr_i) or atr_i == 0:
                continue

            # ── Bull trap: spike above resistance, close back below ──
            if highs[i] > hi_n_v[i] and closes[i] < hi_n_v[i]:
                wick = highs[i] - max(opens[i], closes[i])
                if wick > atr_i:
                    traps.append({
                        "type":       "bull_trap",
                        "time":       times[i],
                        "level":      round(float(hi_n_v[i]), 5),
                        "wick_pips":  round(wick * 10_000, 1),
                        "wick_atr":   round(wick / atr_i, 2),
                        "signal":     "SELL — false breakout above resistance",
                        "confidence": round(min(wick / atr_i / 3, 0.95), 3),
                    })

            # ── Bear trap: spike below support, close back above ──
            if lows[i] < lo_n_v[i] and closes[i] > lo_n_v[i]:
                wick = min(opens[i], closes[i]) - lows[i]
                if wick > atr_i:
                    traps.append({
                        "type":       "bear_trap",
                        "time":       times[i],
                        "level":      round(float(lo_n_v[i]), 5),
                        "wick_pips":  round(wick * 10_000, 1),
                        "wick_atr":   round(wick / atr_i, 2),
                        "signal":     "BUY — false breakout below support",
                        "confidence": round(min(wick / atr_i / 3, 0.95), 3),
                    })

        return traps[-10:]

    @staticmethod
    def trap_probability(df: pd.DataFrame, lookback: int = 20) -> dict:
        """
        Historical trap frequency — calibrate breakout vs trap expectations.

        Returns
        -------
        dict with trap rates per direction and actionable recommendation.
        """
        _validate_ohlcv(df, min_bars=lookback + 10)
        traps = TrapDetector.detect_traps(df, lookback)

        # Vectorised breakout counts
        high_breaks = int((df["high"] > df["high"].rolling(lookback).max().shift(1)).sum())
        low_breaks  = int((df["low"]  < df["low"].rolling(lookback).min().shift(1)).sum())

        bull_traps  = sum(1 for t in traps if t["type"] == "bull_trap")
        bear_traps  = sum(1 for t in traps if t["type"] == "bear_trap")

        total_breaks = high_breaks + low_breaks
        trap_rate    = (bull_traps + bear_traps) / max(total_breaks, 1)

        return {
            "total_breakouts_up":   high_breaks,
            "bull_trap_pct":        round(bull_traps / max(high_breaks, 1) * 100, 1),
            "total_breakouts_down": low_breaks,
            "bear_trap_pct":        round(bear_traps / max(low_breaks, 1) * 100, 1),
            "overall_trap_rate":    round(trap_rate * 100, 1),
            "recommendation": (
                "High trap rate — wait for retest confirmation before entering breakouts"
                if trap_rate > 0.4 else
                "Low trap rate — breakouts tend to follow through, enter on confirmation"
            ),
        }
```


---

## Supply Demand Zone Strategy

# Supply & Demand Zone Strategy

```python
import pandas as pd, numpy as np

class SupplyDemandZones:
    """
    Detect, grade, and score supply & demand zones from OHLCV data.

    Zones are identified by a strong impulse move away from a base candle.
    Each zone is graded A+/A/B/C based on freshness and impulse strength.
    Invalidated zones (price closed through them) are automatically excluded.

    Example
    -------
    >>> result = SupplyDemandZones.detect_zones(df, min_move_atr=2.0)
    >>> print(result["nearest_demand"])
    {'time': ..., 'top': 1.0850, 'bottom': 1.0820, 'strength': 3.1, 'grade': 'A+', 'valid': True}
    """

    @staticmethod
    def detect_zones(df: pd.DataFrame, min_move_atr: float = 2.0, top_n: int = 5) -> dict:
        """
        Detect supply and demand zones — fully vectorised, no Python bar-loops.

        Parameters
        ----------
        df           : OHLCV DataFrame with DatetimeIndex
        min_move_atr : minimum move after base candle (in ATR units) to qualify
        top_n        : maximum zones returned per side

        Returns
        -------
        dict with demand_zones, supply_zones, nearest_demand, nearest_supply,
             and summary statistics.
        """
        _validate_ohlcv(df, min_bars=20)
        atr = _atr(df, 14)

        opens  = df["open"].values
        closes = df["close"].values
        highs  = df["high"].values
        lows   = df["low"].values
        atr_v  = atr.values

        n = len(df)
        zones: dict[str, list] = {"demand": [], "supply": []}

        # Vectorised body and move-after arrays (exclude last bar — no move_after)
        bodies    = np.abs(closes - opens)           # (n,)
        # move_after[i] = |close[i+1] - close[i]|
        move_after = np.abs(np.diff(closes, append=closes[-1]))   # shift-safe

        bull_mask  = closes > opens
        bear_mask  = closes < opens
        strong_mask = move_after > min_move_atr * atr_v

        demand_idx = np.where(bull_mask & strong_mask)[0]
        supply_idx = np.where(bear_mask & strong_mask)[0]

        current_price = float(closes[-1])

        for idx_arr, zone_type in [(demand_idx, "demand"), (supply_idx, "supply")]:
            for i in idx_arr:
                if i >= n - 1:
                    continue                        # Skip last bar (no move_after)
                top    = float(max(opens[i], closes[i]))
                bottom = float(min(opens[i], closes[i]))

                # Count touches (subsequent bars that enter the zone)
                sub_highs = highs[i + 1:]
                sub_lows  = lows[i + 1:]
                sub_close = closes[i + 1:]

                if zone_type == "demand":
                    touch_mask = (sub_lows <= top) & (sub_lows >= bottom)
                    # Invalidated: close below zone bottom
                    invalid_mask = sub_close < bottom
                else:
                    touch_mask = (sub_highs >= bottom) & (sub_highs <= top)
                    # Invalidated: close above zone top
                    invalid_mask = sub_close > top

                touches  = int(touch_mask.sum())
                is_valid = not invalid_mask.any()   # Zone survived (not traded through)

                strength = round(float(move_after[i] / max(atr_v[i], 1e-10)), 2)
                fresh    = touches <= 1 and is_valid

                grade = (
                    "A+" if fresh and strength > 3 else
                    "A"  if fresh and strength > 2 else
                    "B"  if touches <= 2 and is_valid else
                    "C"  if is_valid else
                    "INVALID"
                )

                if not is_valid:
                    continue    # Don't include zones price has already passed through

                zones[zone_type].append({
                    "time":     df.index[i],
                    "top":      round(top, 5),
                    "bottom":   round(bottom, 5),
                    "strength": strength,
                    "touches":  touches,
                    "fresh":    fresh,
                    "grade":    grade,
                    "valid":    is_valid,
                    "atr_ratio": round(float(bodies[i] / max(atr_v[i], 1e-10)), 2),
                })

        # Sort by strength descending, keep top_n
        dem = sorted(zones["demand"], key=lambda z: z["strength"], reverse=True)[:top_n]
        sup = sorted(zones["supply"], key=lambda z: z["strength"], reverse=True)[:top_n]

        nearest_demand = (
            min(dem, key=lambda z: abs(z["top"] - current_price)) if dem else None
        )
        nearest_supply = (
            min(sup, key=lambda z: abs(z["bottom"] - current_price)) if sup else None
        )

        return {
            "demand_zones":   dem,
            "supply_zones":   sup,
            "nearest_demand": nearest_demand,
            "nearest_supply": nearest_supply,
            "n_demand":       len(dem),
            "n_supply":       len(sup),
            "current_price":  round(current_price, 5),
        }
```


---

## Wyckoff Method Engine

# Wyckoff Method Engine

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class WyckoffEngine:
    """
    Detect Wyckoff accumulation/distribution phases from price + volume.

    Uses fully vectorised numpy operations for climax and extreme-volume detection.
    Spring/upthrust detection uses scipy extrema for range boundary identification.

    Example
    -------
    >>> result = WyckoffEngine.detect_phases(df, order=7)
    >>> print(result["current_phase"])
    'PHASE_C_ACCUMULATION — spring detected, look for SOS'
    """

    @staticmethod
    def detect_phases(df: pd.DataFrame, order: int = 7,
                      climax_atr_mult: float = 2.5,
                      climax_vol_mult: float = 2.5) -> dict:
        """
        Detect Wyckoff phases from price + volume — vectorised implementation.

        Parameters
        ----------
        df              : OHLCV DataFrame (must include 'volume' column)
        order           : window for swing high/low detection
        climax_atr_mult : bar range must exceed ATR × this for a climax
        climax_vol_mult : volume must exceed 20-bar avg × this for a climax

        Returns
        -------
        dict with events list, current_phase, volume_declining_in_range,
             interpretation, volume_trend (early vs late range), and
             phase_confidence (0–1).
        """
        required = {"open", "high", "low", "close", "volume"}
        missing  = required - set(df.columns)
        if missing:
            raise ValueError(f"WyckoffEngine requires columns: {missing}")
        _validate_ohlcv(df, min_bars=40)

        close = df["close"].values
        highs = df["high"].values
        lows  = df["low"].values
        vol   = df["volume"].values
        n     = len(df)

        atr_s    = _atr(df, 14).values
        vol_ma20 = pd.Series(vol).rolling(20, min_periods=1).mean().values
        bar_range = highs - lows

        # ── Vectorised climax detection masks ──────────────────────────────
        bearish_bar  = close < np.roll(close, 1)
        bullish_bar  = close > np.roll(close, 1)
        wide_bar     = bar_range > climax_atr_mult * atr_s
        high_vol     = vol > climax_vol_mult * vol_ma20

        sc_candidates = np.where(bearish_bar & wide_bar & high_vol)[0]
        bc_candidates = np.where(bullish_bar & wide_bar & high_vol)[0]
        sc_candidates = sc_candidates[sc_candidates >= 20]
        bc_candidates = bc_candidates[bc_candidates >= 20]

        events: list[dict] = []

        # Selling Climax: bounce ≥ 50% of bar range within next 3 bars
        for i in sc_candidates:
            if i + 3 >= n:
                continue
            recovery = close[i + 1: i + 4].max() - close[i]
            if recovery > bar_range[i] * 0.5:
                events.append({
                    "type":         "selling_climax",
                    "idx":          int(i),
                    "time":         df.index[i],
                    "price":        round(float(close[i]), 5),
                    "volume_ratio": round(float(vol[i] / max(vol_ma20[i], 1e-10)), 2),
                    "bar_range_atr": round(float(bar_range[i] / max(atr_s[i], 1e-10)), 2),
                })

        # Buying Climax: pullback ≥ 50% of bar range within next 3 bars
        for i in bc_candidates:
            if i + 3 >= n:
                continue
            pullback = close[i] - close[i + 1: i + 4].min()
            if pullback > bar_range[i] * 0.5:
                events.append({
                    "type":         "buying_climax",
                    "idx":          int(i),
                    "time":         df.index[i],
                    "price":        round(float(close[i]), 5),
                    "volume_ratio": round(float(vol[i] / max(vol_ma20[i], 1e-10)), 2),
                    "bar_range_atr": round(float(bar_range[i] / max(atr_s[i], 1e-10)), 2),
                })

        # Spring / Upthrust — scipy swing extrema for range boundaries
        swing_highs_idx = argrelextrema(df["high"].values, np.greater, order=order)[0]
        swing_lows_idx  = argrelextrema(df["low"].values,  np.less,    order=order)[0]

        if len(swing_lows_idx) >= 2:
            range_low = float(min(lows[swing_lows_idx[-2]], lows[swing_lows_idx[-1]]))
            # Check last 20 bars for spring
            tail_start = max(n - 20, 0)
            for i in range(tail_start, n):
                if lows[i] < range_low and close[i] > range_low:
                    events.append({
                        "type":    "spring",
                        "time":    df.index[i],
                        "price":   round(float(lows[i]), 5),
                        "close":   round(float(close[i]), 5),
                        "signal":  "BULLISH — spring below support with recovery",
                        "range_low": round(range_low, 5),
                    })

        if len(swing_highs_idx) >= 2:
            range_high = float(max(highs[swing_highs_idx[-2]], highs[swing_highs_idx[-1]]))
            tail_start = max(n - 20, 0)
            for i in range(tail_start, n):
                if highs[i] > range_high and close[i] < range_high:
                    events.append({
                        "type":    "upthrust",
                        "time":    df.index[i],
                        "price":   round(float(highs[i]), 5),
                        "close":   round(float(close[i]), 5),
                        "signal":  "BEARISH — upthrust above resistance with failure",
                        "range_high": round(range_high, 5),
                    })

        # Volume trend within range (last 40 bars)
        vol_declining = False
        vol_early_mean = vol_late_mean = 0.0
        if n > 40:
            vol_early_mean = float(vol[-40:-20].mean())
            vol_late_mean  = float(vol[-20:].mean())
            vol_declining  = vol_late_mean < vol_early_mean * 0.7

        # Phase classification and confidence
        phase = WyckoffEngine._classify_phase(events, df)
        n_events = len(events)
        phase_confidence = min(0.3 + n_events * 0.1, 0.95) if n_events else 0.1

        return {
            "events":                    events[-10:],
            "n_events":                  len(events),
            "current_phase":             phase,
            "phase_confidence":          round(phase_confidence, 2),
            "volume_declining_in_range": vol_declining,
            "volume_early_mean":         round(vol_early_mean, 1),
            "volume_late_mean":          round(vol_late_mean, 1),
            "interpretation":            WyckoffEngine._interpret(phase),
        }

    @staticmethod
    def _classify_phase(events: list, df: pd.DataFrame) -> str:
        if not events:
            return "NO CLEAR WYCKOFF STRUCTURE"
        # Walk events in reverse to find the most recent meaningful event
        for ev in reversed(events):
            t = ev["type"]
            if t == "spring":         return "PHASE_C_ACCUMULATION — spring detected, look for SOS"
            if t == "upthrust":       return "PHASE_C_DISTRIBUTION — upthrust detected, look for SOW"
            if t == "selling_climax": return "PHASE_A_ACCUMULATION — selling climax occurred"
            if t == "buying_climax":  return "PHASE_A_DISTRIBUTION — buying climax occurred"
        return "PHASE_B — building cause (range trading)"

    @staticmethod
    def _interpret(phase: str) -> str:
        if "ACCUMULATION" in phase and "PHASE_C" in phase:
            return "HIGH PROBABILITY BUY — spring is the highest conviction Wyckoff entry"
        if "DISTRIBUTION" in phase and "PHASE_C" in phase:
            return "HIGH PROBABILITY SELL — upthrust signals distribution complete"
        if "PHASE_A" in phase:
            return "WAIT — initial stopping action, range will develop"
        return "RANGE — wait for spring/upthrust test before entry"
```


---

## Institutional Behavior Monitor

# Institutional Behavior Monitor Skill

## Overview
Tracks and analyzes the behavior, positioning, and policy decisions of major central banks,
investment banks, hedge funds, and sovereign wealth funds. Extracts actionable signals from
institutional activity and maps them to market impact.

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│              Institutional Behavior Monitor                     │
├──────────────┬──────────────┬──────────────┬──────────────────┤
│ Central Bank │ Investment   │ COT/Position │ Impact           │
│ Tracker      │ Bank Monitor │ Analyzer     │ Scorer           │
└──────────────┴──────────────┴──────────────┴──────────────────┘
```

---

## 1. Central Bank Monitor

### Central Bank Registry
```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Literal
import pandas as pd
import numpy as np

@dataclass
class CentralBankProfile:
    """Profile of a central bank and its current policy stance."""
    name: str
    code: str
    currency: str
    current_rate: float
    last_decision: str          # "hike", "cut", "hold"
    last_decision_date: str
    next_meeting: str
    bias: str                   # "hawkish", "dovish", "neutral"
    qe_status: str              # "tightening", "stable", "expanding"
    key_officials: list[str]
    affected_pairs: list[str]

CENTRAL_BANKS = {
    "FED": CentralBankProfile(
        name="Federal Reserve", code="FED", currency="USD",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="neutral", qe_status="tightening",
        key_officials=["Chair", "Vice Chair", "NY Fed President"],
        affected_pairs=["EURUSD", "USDJPY", "GBPUSD", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD", "XAUUSD"],
    ),
    "ECB": CentralBankProfile(
        name="European Central Bank", code="ECB", currency="EUR",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="neutral", qe_status="stable",
        key_officials=["President", "Vice President", "Chief Economist"],
        affected_pairs=["EURUSD", "EURJPY", "EURGBP", "EURAUD", "EURCHF"],
    ),
    "BOE": CentralBankProfile(
        name="Bank of England", code="BOE", currency="GBP",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="neutral", qe_status="stable",
        key_officials=["Governor", "Deputy Governor"],
        affected_pairs=["GBPUSD", "EURGBP", "GBPJPY"],
    ),
    "BOJ": CentralBankProfile(
        name="Bank of Japan", code="BOJ", currency="JPY",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="dovish", qe_status="expanding",
        key_officials=["Governor", "Deputy Governor"],
        affected_pairs=["USDJPY", "EURJPY", "GBPJPY", "AUDJPY"],
    ),
    "RBA": CentralBankProfile(
        name="Reserve Bank of Australia", code="RBA", currency="AUD",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="neutral", qe_status="stable",
        key_officials=["Governor", "Deputy Governor"],
        affected_pairs=["AUDUSD", "AUDNZD", "EURAUD", "AUDJPY"],
    ),
    "BOC": CentralBankProfile(
        name="Bank of Canada", code="BOC", currency="CAD",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="neutral", qe_status="stable",
        key_officials=["Governor", "Senior Deputy Governor"],
        affected_pairs=["USDCAD", "CADJPY"],
    ),
    "SNB": CentralBankProfile(
        name="Swiss National Bank", code="SNB", currency="CHF",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="neutral", qe_status="stable",
        key_officials=["Chairman", "Vice Chairman"],
        affected_pairs=["USDCHF", "EURCHF"],
    ),
    "RBNZ": CentralBankProfile(
        name="Reserve Bank of New Zealand", code="RBNZ", currency="NZD",
        current_rate=0.0, last_decision="hold", last_decision_date="",
        next_meeting="", bias="neutral", qe_status="stable",
        key_officials=["Governor", "Deputy Governor"],
        affected_pairs=["NZDUSD", "AUDNZD"],
    ),
}

class CentralBankTracker:
    """Track and analyze central bank behavior and policy shifts."""

    def __init__(self):
        self.banks = CENTRAL_BANKS
        self.policy_history = []

    def update_bank(self, code: str, **kwargs):
        """Update a central bank's profile with new data."""
        if code in self.banks:
            for k, v in kwargs.items():
                if hasattr(self.banks[code], k):
                    setattr(self.banks[code], k, v)

    def get_policy_divergence(self) -> pd.DataFrame:
        """
        Map policy divergence between central banks.
        Divergence drives currency pair trends.
        """
        data = []
        banks = list(self.banks.values())
        for i, bank_a in enumerate(banks):
            for bank_b in banks[i + 1:]:
                rate_diff = bank_a.current_rate - bank_b.current_rate
                bias_map = {"hawkish": 1, "neutral": 0, "dovish": -1}
                bias_diff = bias_map.get(bank_a.bias, 0) - bias_map.get(bank_b.bias, 0)
                data.append({
                    "pair": f"{bank_a.currency}/{bank_b.currency}",
                    "rate_differential": round(rate_diff, 2),
                    "bias_differential": bias_diff,
                    "divergence_signal": self._interpret_divergence(rate_diff, bias_diff),
                    f"{bank_a.code}_rate": bank_a.current_rate,
                    f"{bank_b.code}_rate": bank_b.current_rate,
                    f"{bank_a.code}_bias": bank_a.bias,
                    f"{bank_b.code}_bias": bank_b.bias,
                })
        return pd.DataFrame(data)

    @staticmethod
    def _interpret_divergence(rate_diff: float, bias_diff: int) -> str:
        if rate_diff > 0.5 and bias_diff > 0:
            return "STRONG BUY base currency — widening rate advantage + hawkish bias"
        if rate_diff < -0.5 and bias_diff < 0:
            return "STRONG SELL base currency — widening rate disadvantage + dovish bias"
        if abs(rate_diff) < 0.25 and bias_diff == 0:
            return "NEUTRAL — no clear policy divergence"
        if bias_diff > 0:
            return "MILD BUY base — bias divergence favors base currency"
        if bias_diff < 0:
            return "MILD SELL base — bias divergence favors quote currency"
        return "MIXED — rates and bias sending conflicting signals"

    def rate_decision_impact_model(self, code: str, decision: str, expected: str) -> dict:
        """Model the expected market impact of a rate decision vs expectations."""
        bank = self.banks.get(code)
        if not bank:
            return {"error": f"Unknown bank: {code}"}

        surprise_map = {
            ("hike", "hold"): {"direction": "bullish", "magnitude": "large", "confidence": 0.85},
            ("hike", "hike"): {"direction": "neutral_to_bullish", "magnitude": "small", "confidence": 0.5},
            ("cut", "hold"): {"direction": "bearish", "magnitude": "large", "confidence": 0.85},
            ("cut", "cut"): {"direction": "neutral_to_bearish", "magnitude": "small", "confidence": 0.5},
            ("hold", "hike"): {"direction": "bearish", "magnitude": "medium", "confidence": 0.7},
            ("hold", "cut"): {"direction": "bullish", "magnitude": "medium", "confidence": 0.7},
            ("hold", "hold"): {"direction": "neutral", "magnitude": "minimal", "confidence": 0.3},
        }
        key = (decision.lower(), expected.lower())
        impact = surprise_map.get(key, {"direction": "unknown", "magnitude": "unknown", "confidence": 0})

        return {
            "bank": bank.name,
            "currency": bank.currency,
            "decision": decision,
            "expected": expected,
            "is_surprise": decision != expected,
            "impact": impact,
            "affected_pairs": bank.affected_pairs,
            "recommendation": f"{'Strong' if impact['magnitude'] == 'large' else 'Moderate'} "
                             f"{impact['direction']} signal on {bank.currency} pairs" if impact["confidence"] > 0.5
                             else "Wait for price action confirmation",
        }
```

---

## 2. Investment Bank & Hedge Fund Monitor

```python
MAJOR_INSTITUTIONS = {
    "investment_banks": [
        "Goldman Sachs", "JPMorgan", "Morgan Stanley", "Citigroup",
        "Bank of America", "Deutsche Bank", "UBS", "Credit Suisse",
        "Barclays", "HSBC", "BNP Paribas", "Nomura"],
    "hedge_funds": [
        "Bridgewater", "Citadel", "Two Sigma", "Renaissance Technologies",
        "Point72", "Millennium", "DE Shaw", "Man Group"],
    "sovereign_wealth": [
        "Norway Government Pension Fund", "Abu Dhabi Investment Authority",
        "China Investment Corporation", "GIC Singapore", "Kuwait Investment Authority"],
}

@dataclass
class InstitutionalAction:
    """Represents a tracked institutional action."""
    institution: str
    institution_type: Literal["investment_bank", "hedge_fund", "sovereign_wealth", "central_bank"]
    action_type: str          # "forecast_change", "position_shift", "intervention", "report"
    datetime: str
    title: str
    description: str
    affected_currencies: list[str]
    affected_pairs: list[str]
    direction: str            # "bullish", "bearish", "neutral"
    impact: str               # "HIGH", "MEDIUM", "LOW"
    source_url: str = ""

class InstitutionalMonitor:
    """
    Track and analyze institutional behavior.
    In Claude context: use web_search to fetch latest institutional data.
    """

    def __init__(self):
        self.tracked_actions: list[InstitutionalAction] = []

    def add_action(self, action: InstitutionalAction):
        self.tracked_actions.append(action)

    def get_consensus(self, currency: str) -> dict:
        """Aggregate institutional sentiment for a currency."""
        relevant = [a for a in self.tracked_actions if currency in a.affected_currencies]
        if not relevant:
            return {"currency": currency, "consensus": "NO_DATA", "n_actions": 0}

        bullish = sum(1 for a in relevant if a.direction == "bullish")
        bearish = sum(1 for a in relevant if a.direction == "bearish")
        neutral = sum(1 for a in relevant if a.direction == "neutral")
        total = len(relevant)

        return {
            "currency": currency,
            "bullish_pct": round(bullish / total * 100, 1),
            "bearish_pct": round(bearish / total * 100, 1),
            "neutral_pct": round(neutral / total * 100, 1),
            "consensus": "BULLISH" if bullish > bearish + neutral else "BEARISH" if bearish > bullish + neutral else "MIXED",
            "n_actions": total,
            "key_actions": [{"institution": a.institution, "title": a.title, "direction": a.direction}
                           for a in sorted(relevant, key=lambda x: x.datetime, reverse=True)[:5]],
        }
```

---

## 3. COT (Commitment of Traders) Analysis

```python
class COTAnalyzer:
    """
    Analyze CFTC Commitment of Traders data for positioning signals.
    Data source: https://www.cftc.gov/dea/futures/financial_lf.htm
    """

    CURRENCY_CONTRACTS = {
        "EUR": "EURO FX", "GBP": "BRITISH POUND", "JPY": "JAPANESE YEN",
        "AUD": "AUSTRALIAN DOLLAR", "CAD": "CANADIAN DOLLAR", "CHF": "SWISS FRANC",
        "NZD": "NEW ZEALAND DOLLAR", "MXN": "MEXICAN PESO",
        "XAU": "GOLD", "XAG": "SILVER", "WTI": "CRUDE OIL",
    }

    @staticmethod
    def analyze_positioning(cot_data: pd.DataFrame, currency: str) -> dict:
        """
        Analyze COT positioning for a currency.
        cot_data columns: [date, long_noncommercial, short_noncommercial, long_commercial,
                          short_commercial, long_nonreportable, short_nonreportable]
        """
        latest = cot_data.iloc[-1]
        prev = cot_data.iloc[-2] if len(cot_data) > 1 else latest

        net_spec = latest["long_noncommercial"] - latest["short_noncommercial"]
        prev_net_spec = prev["long_noncommercial"] - prev["short_noncommercial"]
        net_change = net_spec - prev_net_spec

        # Historical percentile
        historical_net = cot_data["long_noncommercial"] - cot_data["short_noncommercial"]
        percentile = (historical_net < net_spec).mean() * 100

        return {
            "currency": currency,
            "net_speculative": int(net_spec),
            "weekly_change": int(net_change),
            "direction": "LONG" if net_spec > 0 else "SHORT",
            "change_direction": "adding_longs" if net_change > 0 else "adding_shorts",
            "historical_percentile": round(percentile, 1),
            "extreme_positioning": percentile > 90 or percentile < 10,
            "signal": COTAnalyzer._cot_signal(net_spec, net_change, percentile),
        }

    @staticmethod
    def _cot_signal(net: int, change: int, percentile: float) -> str:
        if percentile > 90 and change < 0:
            return "EXTREME LONG + UNWINDING → potential reversal (bearish for currency)"
        if percentile < 10 and change > 0:
            return "EXTREME SHORT + COVERING → potential reversal (bullish for currency)"
        if percentile > 80 and change > 0:
            return "STRONG LONG + BUILDING → trend continuation but watch for crowding"
        if percentile < 20 and change < 0:
            return "STRONG SHORT + BUILDING → trend continuation but watch for squeeze"
        return "MODERATE positioning — no extreme signal"
```

---

## 4. Intervention Detection

```python
class InterventionDetector:
    """
    Detect potential central bank interventions from price action — vectorised.

    Intervention signatures: abnormally wide bar + very high volume + trend reversal.

    Example
    -------
    >>> events = InterventionDetector.detect_fx_intervention(df, "USDJPY")
    >>> for e in events:
    ...     print(e["timestamp"], e["intervention_probability"])
    """

    @staticmethod
    def detect_fx_intervention(
        df: pd.DataFrame,
        symbol: str,
        atr_multiplier: float = 5.0,
        volume_multiplier: float = 3.0,
        trend_window: int = 10,
    ) -> list[dict]:
        """
        Detect abnormal price moves that may indicate central bank intervention.

        Parameters
        ----------
        df                : OHLCV DataFrame (with 'volume' column)
        symbol            : instrument name (label only)
        atr_multiplier    : bar range must exceed ATR × this value
        volume_multiplier : volume must exceed 20-bar avg × this value
        trend_window      : lookback bars for prior-trend direction

        Returns
        -------
        list of detection dicts sorted chronologically, each with probability score.
        """
        required = {"open", "high", "low", "close", "volume"}
        missing  = required - set(df.columns)
        if missing:
            raise ValueError(f"InterventionDetector requires columns: {missing}")
        if len(df) < 25:
            return []

        # Fully vectorised anomaly masks
        atr_v   = _atr(df, 14).values
        vol_v   = df["volume"].values
        high_v  = df["high"].values
        low_v   = df["low"].values
        close_v = df["close"].values
        open_v  = df["open"].values
        n       = len(df)

        bar_range = high_v - low_v
        vol_ma20  = pd.Series(vol_v).rolling(20, min_periods=1).mean().values

        wide_mask   = bar_range > atr_multiplier * atr_v
        hiVol_mask  = vol_v > volume_multiplier * vol_ma20
        candidate_idx = np.where(wide_mask & hiVol_mask)[0]
        candidate_idx = candidate_idx[candidate_idx >= trend_window]

        detections: list[dict] = []

        # Rolling prior-trend: mean pct change over trend_window bars
        # Vectorised: pct change array and rolling mean
        pct_chg = pd.Series(close_v).pct_change().values
        # prior_trend[i] = mean(pct_chg[i-trend_window : i])
        prior_trend = pd.Series(pct_chg).rolling(trend_window, min_periods=1).mean().values

        for i in candidate_idx:
            bar_dir     = 1 if close_v[i] > open_v[i] else -1
            is_reversal = (prior_trend[i] > 0 and bar_dir < 0) or (prior_trend[i] < 0 and bar_dir > 0)

            range_atr   = float(bar_range[i] / max(atr_v[i], 1e-10))
            vol_ratio   = float(vol_v[i] / max(vol_ma20[i], 1e-10))
            prob        = min(0.3 + range_atr * 0.05 + vol_ratio * 0.03 + (0.2 if is_reversal else 0), 0.95)

            detections.append({
                "timestamp":              df.index[i].isoformat(),
                "symbol":                 symbol,
                "bar_range_atr":          round(range_atr, 2),
                "volume_ratio":           round(vol_ratio, 2),
                "direction":              "bullish" if bar_dir > 0 else "bearish",
                "prior_trend":            round(float(prior_trend[i]) * 100, 4),  # % per bar
                "is_trend_reversal":      is_reversal,
                "intervention_probability": round(prob, 3),
                "note": (
                    "HIGH: Possible central bank intervention (reversal + extreme range + volume)"
                    if is_reversal and prob > 0.7 else
                    "MODERATE: Large institutional flow detected"
                    if not is_reversal else
                    "LOW-MODERATE: Trend reversal on wide bar but moderate volume"
                ),
            })

        return detections
```

---

## 5. Web Search Integration

When this skill is active, use web_search for real-time institutional data:

```
# Central bank current rates and policy
web_search("Federal Reserve interest rate 2025 current")
web_search("ECB monetary policy latest decision")

# Investment bank forecasts
web_search("Goldman Sachs EURUSD forecast 2025")
web_search("JPMorgan FX outlook currencies")

# COT data
web_search("CFTC COT report latest forex positioning")

# Institutional flows
web_search("institutional forex positioning this week")
web_search("hedge fund currency exposure")
```

## Integration Points

| Skill | Data Exchanged |
|---|---|
| `mt5-chart-browser` | Price data for intervention detection |
| `market-news-impact` | Central bank decisions and statements |
| `event-timeline-linker` | Institutional actions as timeline events |
| `pair-correlation-engine` | Policy divergence maps to correlation analysis |
| `trading-brain` | Institutional intelligence for decisions |


---

## Order Flow Masterclass — Reading Institutional Activity
> Source: "How He Made $40,000+ Trading using OrderFlow (Full Masterclass)" — Carmine Rosato on Chart Fanatics (229K views, 3h42m, 7-figure verified)

### Fundamental Mechanics
```
Every transaction = ONE buyer + ONE seller (not "more buyers than sellers")
Requires pairing: LIMIT ORDER (passive) + MARKET ORDER (aggressive)

Passive Orders (Limit): Add liquidity, wait at price → CAN be faked (pulled before fill)
Aggressive Orders (Market): Take liquidity, immediate → CANNOT be faked (creates transaction)

Key Insight: Only aggressive orders show REAL intention. This is what order flow reads.
```

### Support & Resistance in Order Flow
```
Resistance = Many PASSIVE SELLERS at price level + not enough AGGRESSIVE BUYERS to absorb
Support = Many PASSIVE BUYERS at price level + not enough AGGRESSIVE SELLERS to absorb

Breakout = When aggressive volume ABSORBS all passive orders at a level
Rejection = When passive orders OUTLAST aggressive volume → price reverses
```

### Delta — The Core Order Flow Metric
```
Delta = Aggressive Buys (at ASK) − Aggressive Sells (at BID)

Positive delta → aggressive buyers dominating → bullish pressure
Negative delta → aggressive sellers dominating → bearish pressure
Delta near zero → balanced, no clear aggressor

Cumulative Delta: Running total over time
  Rising + price rising → healthy trend (confirmed)
  Rising + price FALLING → absorption (bullish divergence — institutions buying the dip)
  Falling + price rising → distribution (bearish divergence — institutions selling into rally)
```

### Absorption — The Highest-Probability Signal
```
Absorption = Price STOPS moving despite heavy aggressive volume

Bullish Absorption: Heavy aggressive SELLING but price WON'T go down
  → Passive buyers absorbing all sell pressure → reversal UP imminent

Bearish Absorption: Heavy aggressive BUYING but price WON'T go up
  → Passive sellers absorbing all buy pressure → reversal DOWN imminent

How to spot: High delta + no price movement = absorption happening
This is the STRONGEST order flow signal — institutions are stepping in.
```

### Low Volume Node (LVN) — Price Acceptance/Rejection
```
LVN = Price level where very little trading occurred (thin area on VP)
When price reaches LVN: Either BLASTS through (no resistance) or REJECTS hard

LVN as confirmation: If your ICT/SMC setup aligns with an LVN → higher probability
LVN between heavy zones: Price tends to "jump" through LVNs quickly
```

### Order Flow + ICT/SMC Integration
```
FVG + Positive Delta at level = institutional buying confirmation → strong long
OB + Absorption at level = institutions defending the block → high-probability entry
Liquidity sweep + Delta divergence = smart money accumulated during the sweep
BOS + Heavy aggressive volume = genuine breakout (not a fakeout)
BOS + LOW aggressive volume = likely fakeout → fade it

"No matter what strategy you trade — ICT, SMC, Fibonacci, supply/demand —
orderflow will make your trading better. Better RR, better confirmations."
— Carmine Rosato
```

### Practical Order Flow Checklist
```
□ Identify your ICT/SMC setup first (structure, level, direction)
□ Check delta at the key level: who is aggressive?
□ Look for absorption: is price stopping despite heavy aggression?
□ Check cumulative delta trend: does it confirm or diverge from price?
□ If divergence → expect reversal soon
□ Enter with confidence when order flow confirms your setup
□ If order flow contradicts → skip the trade
```

### Carmine's 3-Confirmation Entry Framework
> Source: Same masterclass — applied to every live trade
```
1. CONTEXT — Does price action fit your thesis?
   (At supply/demand level? Prior rejection? Trend line break?)
2. LOCATION — Is entry at optimal price?
   (Key level, good RR, not mid-range)
3. CONFIRMATION — What does order flow show RIGHT NOW?
   (P-shape at high? Absorption? Volume tail? Delta divergence?)

All three required. Missing any one = skip.
```

### Key OF Patterns for Entries
```
P-Shape (Trapped Buyers):
  High volume at top of move → selling off
  = Buyers got in at high, now trapped → short setup
  When P-shape at supply level = strongest short signal

Volume Tail (True Reversal):
  Valid high/low forms when there's LACK of volume
  High volume at level = NOT a final H/L (will be retested)
  Low volume at level = likely VALID reversal point
  After sweep: lack of volume on pullback = true low placed

Zero Prints (Fair Value Gaps in OF):
  Price levels where NO volume traded
  Market is "magnetic" to zero prints — likes to revisit them
  Use as targets (Carmine: "I love zero prints... gravitating forces")

Spoofing Tell:
  Completed transactions (delta/VP) CANNOT be spoofed
  Limit orders CAN be spoofed (pulled before filling)
  Large orders appear → disappear without filling → artificial
  Market often reverses after spoofing occurs
```

### Shorting Pops (Best RR Setup)
```
When large passive sellers visible at supply level:
  1. Let market rally into them
  2. Watch aggressive buyers hit the offer
  3. If market can't break through → short on the pop
  Gives: entry further from target (wider reward) + closer to SL (tighter stop)
  Example: 357 contracts hitting offer, market reverses = short entry
```

---

## Fabio Valentini's Order Flow Scalping — World Cup Champion
> Source: "Trading LIVE with the #1 Scalper in the WORLD" — Chart Fanatics (3h34m, 218% annual returns, Robbins Cup top 3)

### Core Philosophy
```
0% prediction ability vs 100% reading ability
Read the market, don't predict it
Probability-based execution driven by real-time data (order flow, volume delta)
Not opinions — data shows who is really buying/selling
```

### The 3-Step Non-Discretionary Model
```
① STATE (Condition): Is market BALANCED or UNBALANCED?
   Balanced = range-bound, mean-reversion environment
   Unbalanced = one-directional, trend-following environment

② LOCATION: WHERE to enter (profile-based S/R)
   Draw daily volume profile → identify low-volume nodes
   Place ALERT (not limit order) at the node
   Only engage when price reaches your pre-identified level

③ EXECUTION: Wait for AGGRESSION to trigger entry
   Large volume spikes at your level = confirmation
   No aggression = no entry (even if at perfect location)
```

### Trending Model (NY Session)
```
Session: New York ONLY (highest volatility)
Market State: Unbalanced (out-of-balance seeking new equilibrium)

Entry:
  1. Draw daily profile → identify low-volume nodes
  2. Place alert below the node
  3. Enter on first aggressive candle showing directional momentum
  4. SL: 1-2 pips BELOW spike high (not AT spike high — avoid acceleration slippage)
  5. TP: Previous Point of Control (POC/balance level)
     → 70% probability of reversal at POC

Exit: Full position close at target (don't split — high reversal probability at POC)
```

### Mean Reversion Model (London Session)
```
Session: London OR summer consolidation periods
Market State: Balanced/consolidated (range-bound)

Entry:
  1. Identify consolidation range from daily profile
  2. Locate low-volume node within range
  3. Wait for FIRST breakout → DON'T take it
  4. Take 2ND push (retest on correction) — NOT the 1st
  5. Enter on aggressive orders at LVN on retracement

SL: Above aggressive seller/buyer level
TP: Return to balance level within consolidation range
```

### Filter Settings
```
30 contract minimum for NY session (ignore retail noise)
20 contract minimum for London session
These filters ensure you only see institutional activity
```

### Seasonal Adjustments
```
Months to avoid: May-June (volatile consolidation, summer pressure)
Best times: NY session mornings post-gap + after macro news
Volatility regimes: Adjust stop placement and entry timing based on ATR
High-pressure periods: Mean-reversion model works better, trending model takes losses
```

### Risk Model
```
Risk per trade: 0.25% - 0.5% of account
Quality > Quantity: 1 good 20-point trade beats 10 mediocre trades
Win rate: 30-33% is fine with 4:1-5:1 RR (validated over 2,400+ trades/year)
Full-time commitment: Must watch entire session (not set-and-forget)
```

---

## Order Flow Delta Strategy

# Order Flow Delta Strategy

```python
import pandas as pd
import numpy as np

class OrderFlowDelta:
    """
    Approximates order-flow delta from OHLCV data (tick delta requires L2).

    The bar delta formula uses price position within the bar as a proxy for
    buy vs sell pressure — a common approximation when tick data is unavailable.

    Example
    -------
    >>> df_with_delta = OrderFlowDelta.compute_delta(df)
    >>> div = OrderFlowDelta.delta_divergence(df)
    >>> abs_ = OrderFlowDelta.absorption_detection(df)
    """

    @staticmethod
    def compute_delta(df: pd.DataFrame) -> pd.DataFrame:
        """
        Approximate delta from OHLCV — fully vectorised, NaN-safe.

        Returns the input DataFrame augmented with:
          - bar_delta        : signed volume proxy per bar
          - cumulative_delta : running cumulative delta
          - delta_ema        : 14-bar EMA of bar_delta for smoothing
        """
        _validate_ohlcv(df, min_bars=5)
        out = df.copy()

        hl_range  = (df["high"] - df["low"]).replace(0, np.nan)
        buy_frac  = (df["close"] - df["low"])  / hl_range
        sell_frac = (df["high"] - df["close"]) / hl_range

        # Bullish bars: volume proportional to buy pressure
        # Bearish bars: volume proportional to sell pressure (negative)
        is_bull = df["close"] >= df["open"]
        out["bar_delta"] = np.where(
            is_bull,
             df["volume"] * buy_frac.fillna(0.5),
            -df["volume"] * sell_frac.fillna(0.5),
        )
        out["cumulative_delta"] = out["bar_delta"].cumsum()
        out["delta_ema"]        = out["bar_delta"].ewm(span=14, adjust=False).mean()
        return out

    @staticmethod
    def delta_divergence(df: pd.DataFrame, window: int = 20) -> dict:
        """
        Detect price/delta divergences — the footprint of institutional distribution
        (price new high + delta diverging down) or accumulation (vice versa).

        Returns
        -------
        dict with divergence label, signal, confidence, and delta trend.
        """
        _validate_ohlcv(df, min_bars=window + 5)
        df_d = OrderFlowDelta.compute_delta(df)

        tail_price = df_d["high"].tail(window)
        tail_delta = df_d["cumulative_delta"].tail(window)

        price_new_high = df_d["high"].iloc[-1] >= tail_price.max()
        delta_new_high = df_d["cumulative_delta"].iloc[-1] >= tail_delta.max()
        price_new_low  = df_d["low"].iloc[-1]  <= df_d["low"].tail(window).min()
        delta_new_low  = df_d["cumulative_delta"].iloc[-1] <= tail_delta.min()

        # Delta trend (recent 10 bars)
        delta_trend = ("bullish" if df_d["bar_delta"].tail(10).mean() > 0 else "bearish")

        # Delta slope (linear regression over last 20 bars)
        y = df_d["cumulative_delta"].tail(window).values
        x = np.arange(len(y))
        if len(y) > 1:
            slope = float(np.polyfit(x, y, 1)[0])
        else:
            slope = 0.0

        if price_new_high and not delta_new_high:
            return {
                "divergence":  "BEARISH — price new high but delta not confirming (distribution)",
                "signal":      "SELL",
                "confidence":  0.70,
                "delta_trend": delta_trend,
                "delta_slope": round(slope, 4),
            }
        if price_new_low and not delta_new_low:
            return {
                "divergence":  "BULLISH — price new low but delta not confirming (accumulation)",
                "signal":      "BUY",
                "confidence":  0.70,
                "delta_trend": delta_trend,
                "delta_slope": round(slope, 4),
            }
        return {
            "divergence":  "NONE",
            "signal":      "NO DIVERGENCE",
            "delta_trend": delta_trend,
            "delta_slope": round(slope, 4),
        }

    @staticmethod
    def absorption_detection(df: pd.DataFrame, multiplier: float = 2.0, window: int = 50) -> dict:
        """
        Detect volume absorption: high volume on small bar range signals a large
        player absorbing orders — often precedes a reversal or explosive breakout.

        Parameters
        ----------
        multiplier : vol/range ratio must be > this × average to flag absorption
        window     : lookback for average vol/range ratio

        Returns
        -------
        dict with absorption flag, ratios, z-score, and interpretation.
        """
        _validate_ohlcv(df, min_bars=window + 5)
        out = df.copy()

        # Volume-per-pip as proxy for absorption
        out["range"]          = (df["high"] - df["low"]).replace(0, np.nan)
        out["vol_range_ratio"] = df["volume"] / (out["range"] * 10_000)

        last      = out.iloc[-1]
        rolling   = out["vol_range_ratio"].tail(window)
        avg_ratio = rolling.mean()
        std_ratio = rolling.std()

        current_ratio = last["vol_range_ratio"]
        z_score       = (current_ratio - avg_ratio) / max(std_ratio, 1e-10)
        absorbing     = current_ratio > multiplier * avg_ratio

        return {
            "absorption_detected": bool(absorbing),
            "vol_range_ratio":     round(float(current_ratio), 1),
            "avg_ratio":           round(float(avg_ratio), 1),
            "z_score":             round(float(z_score), 2),
            "interpretation": (
                "LARGE PLAYER ABSORBING — expect reversal or explosive breakout"
                if absorbing else "Normal order flow — no absorption signal"
            ),
        }
```

---

## Liquidity Trap Strategy — Direction, Entry & Scaling
> Source: "STEAL This EASY Liquidity TRAP Trading Strategy" — Marco Trades on Chart Fanatics (724K views, $500K+ payouts)

**Core principle:** Liquidity = everything. Retail concepts (BOS, FVG, SMC) exist to BUILD liquidity at obvious levels. Don't trade them — identify WHERE they'll trap traders, then fade the trap.

### Liquidity Identification — The Single Rule
```
High RESPECTED → price moves AWAY = Liquidity resting ABOVE that high
Low RESPECTED → price moves AWAY = Liquidity resting BELOW that low

"Respected" = price approaches, bounces off without breaking, reverses sharply
"Move Away" = price accelerates opposite direction after respecting the level
```

### Direction Bias — High → Low → High Pattern
```
1. Identify previous high that was RESPECTED
2. Did price pull back to a LOW?
3. Did price MOVE AWAY from that low?
If YES to all → market biased to continue in that direction
                → liquidity exists below that low (for buys) or above that high (for sells)
```

### Entry Rules (Strict)
```
Rule 1: BUY only BELOW previous lows. SELL only ABOVE previous highs.
  → This is where trapped traders' stops get liquidated = your edge

Rule 2: Wait for Liquidity Sweep + False Reaction
  → Market breaks above/below level (retail enters thinking breakout)
  → Market pulls back (false reaction = trap induction)
  → Retail enters thinking they're catching momentum
  → Market reverses sharply INTO them
  → YOUR ENTRY: when price moves AWAY from false reaction, confirming trap

Rule 3: Fractal Confirmation Required
  → Same pattern must appear on HTF AND LTF
  → HTF (4H/Daily) = direction bias
  → MTF (1H) = setup confirmation
  → LTF (15M/5M) = exact entry execution
  → No trade without alignment across all three

Rule 4: Execute Immediately After Trigger
  → Once high/low is taken (confirming false reaction trap)
  → Entry is DIRECT from that level — no hesitation
```

### Stop Loss & Targets
```
SL: Directly above (sells) / below (buys) the structure level that triggered entry
  → Tight as possible. Risk 1-2% per trade.

Targets: IDENTIFIED LIQUIDITY POINTS (not arbitrary R:R)
  → Internal liquidity: highs/lows within consolidation → scale 20-30%
  → External liquidity: range extremes, major swing H/L → hold 70-80%
  → Ask: "Why am I closing here? What liquidity is at this level?"

Trail: Once +1R profit → trail SL to breakeven or better
```

### Common Mistakes
```
× Trading H/L without respect + move away pattern
× Entering DURING false reaction (you ARE the trapped trader)
× Random SL placement instead of structure-based
× Partials at arbitrary R:R instead of identified liquidity
× No fractal alignment (LTF entry without HTF confirmation)
× Trading outside high-liquidity hours (stock open + 2hrs best)
```

---

## CISD — Change in State of Delivery

**Definition:** When a breakout candle through a FVG simultaneously creates a *new* FVG that overlaps the IFVG zone. Two signals merge into one candle.

**Why it matters:** CISD is the highest-probability reversal signal in the SMC framework. It shows:
1. The prior FVG expectation completely failed (IFVG formed)
2. The breakout candle itself left a new imbalance in the opposite direction
3. Both zones overlap — creating a double-confluence reaction area

**Conditions:**
- Occurs at the **end of a trend** (after liquidity sweep or at HTF key level) — strongest signal
- Can occur at any timeframe; LTF CISD inside HTF key zone = maximum confluence
- The overlapping area of the original IFVG + new FVG = the entry zone

**Trading the CISD:**
- Enter short (bearish CISD) or long (bullish CISD) at the overlapping zone
- SL: beyond the most recent swing (above for shorts, below for longs)
- No additional confirmation needed — the pattern itself is the confirmation
- Relates to: IFVG (the failed FVG component), Displacement candles (the breakout component), MSS (the structural component)

---

## One Setup For Life — 5-Step ICT Execution Model
> Source: "My One Setup For Life! (ICT Concepts)" — Stef Trades (93K views, 3:1 RR consistently)

**A complete, repeatable ICT entry model that occurs daily in the AM session.**

### The 5 Steps
```
Step 1: 15-Minute Sweep of Liquidity (REQUIRED)
  → A significant swing high or low gets swept on the 15M chart
  → Must be a clear, obvious liquidity level (not minor wicks)

Step 2: 15-Minute Imbalance Alignment (OPTIONAL — adds confluence)
  → If sweeping BSL: bearish FVG resting above the swept high
  → If sweeping SSL: bullish FVG resting below the swept low
  → The sweep + imbalance happening together = stronger signal

Step 3: Dealing Range — Premium / Discount
  → Mark the dealing range: from the high that swept to the low that swept
  → Optimal LONGS: anywhere BELOW the 0.5 (midpoint) = discount zone
  → Optimal SHORTS: anywhere ABOVE the 0.5 (midpoint) = premium zone
  → If Steps 1-3 are met → go to LTF

Step 4: Lower Timeframe Reversal + Break of Structure
  → On 1M/5M: look for price to REVERSE and BREAK a minor swing H/L
  → A wick breaking the swing is enough to confirm BOS
  → If you also get a Change in State of Delivery (CISD) → even better confluence
  → CISD may give a slightly later entry but with higher probability

Step 5: PDA Entry — Back Past Liquidity Swept (REQUIRED)
  → Find an FVG or breaker block on the LTF after the BOS
  → CRITICAL: The entry MUST be BACK PAST the liquidity that was swept
  → If SSL was swept at price X → entry must form ABOVE X (came back past it)
  → If BSL was swept at price X → entry must form BELOW X
  → Enter at retest of the FVG/gap → SL below the low → TP at opposing liquidity
```

### Execution Summary
```
Long Setup:
  1. 15M SSL sweep ✓
  2. 15M bullish FVG at the sweep level (optional) ✓
  3. In discount of dealing range (below 0.5) ✓
  4. LTF: reversal + BOS above minor swing high ✓
  5. FVG entry back past the swept SSL → SL below low → TP at BSL (opposing liquidity)

Short Setup:
  1. 15M BSL sweep ✓
  2. 15M bearish FVG at the sweep level (optional) ✓
  3. In premium of dealing range (above 0.5) ✓
  4. LTF: reversal + BOS below minor swing low ✓
  5. FVG entry back past the swept BSL → SL above high → TP at SSL (opposing liquidity)

Partials: Take at equal highs/lows, dealing range midpoint, then let rest ride to TP
Typical RR: 3:1+
Frequency: Occurs every single day in the AM session
```

---

## Candle Range Theory (CRT) — Liquidity Sweep Model
> Source: "Candle Range Theory (CRT) Trading Model" — Smart Risk (755K views)

**Core concept:** Each candle's high/low = the most important liquidity levels. Break any candle down to LTF and its H/L act as turning points. CRT uses a 3-candle sequence to trade these sweeps.

### Three-Candle Structure
```
Candle 1: RANGE — defines liquidity levels (CRH = Candle Range High, CRL = Candle Range Low)
Candle 2: SWEEP — attacks one side's liquidity, then closes BACK INSIDE the range
Candle 3: ENTRY — move toward opposite liquidity level

INVALID if: Candle 2 CLOSES beyond the range (continuation, not reversal)
```

### CRT with Trend (Preferred Setup)
```
Bullish Trend CRT:
  1. Market clearly trending up (HH/HL structure)
  2. Wait for correction inside latest impulse range
  3. Apply CRT to BEARISH candles only (counter-correction)
  4. Mark each bearish candle's H/L
  5. If next candle breaks below CRL but CLOSES back inside → valid CRT
  6. Zoom to LTF (5M/15M) → find bullish FVG after the sweep → enter at FVG
  7. SL: below the FVG
  8. TP1: 1:1 RR (close half, move to BE) → TP2: let run to next HTF level

Bearish Trend CRT:
  1. Market clearly trending down (LH/LL structure)
  2. Wait for correction into premium zone
  3. Apply CRT to BULLISH candles only
  4. If next candle sweeps above CRH but closes back inside → valid CRT
  5. Zoom to LTF → find bearish FVG after sweep → sell at FVG
  6. SL: above the FVG
  7. TP1: 1:1 (half position, BE stop) → TP2: next major support/liquidity zone
```

### NY Session CRT (Counter-Trend Variant)
```
Focus: 1H candle just before NY open (9:30 EST)
Why: NY session typically sweeps London session liquidity then reverses
Setup: If price sweeps beyond that candle's range → returns inside → trade the reversal
Caution: This is counter-trend. Use only with strong HTF context.
```

### CRT Common Mistakes
```
× Trading CRT in choppy/ranging markets → needs clear trend
× Entering before sweep candle CLOSES → it can continue beyond range
× Ignoring HTF context → CRT near major news/HTF levels can fail
× Applying to all candles → only apply to counter-trend candles during corrections
```

### CRT + Premium/Discount Confluence
```
In uptrend: wait for correction into DISCOUNT zone → CRT on bearish candles
In downtrend: wait for correction into PREMIUM zone → CRT on bullish candles
Combines: trend direction + manipulation (sweep) + discount/premium entry = highest probability
```

---

## ICT Full Methodology Reference

> Merged from `ict-smart-money.md` — the complete ICT Smart Money Concepts strategy framework by Michael J. Huddleston. Use this section for strategy selection, execution rules, risk management, confluence scoring, killzone timing, and MQL5 indicator reference.

---

### Core Methodology

ICT Smart Money Concepts by Michael J. Huddleston. Markets are driven by institutional order flow through three phases: **Accumulation, Manipulation, Distribution (AMD / Power of 3)**.

#### The Five Pillars

1. **Market Structure** -- Where is the trend? (HH/HL = bullish, LH/LL = bearish)
2. **Liquidity** -- Where are the stops? (BSL above, SSL below)
3. **PD Arrays** -- Where do institutions enter? (FVG, OB, Breaker)
4. **Time** -- When does it happen? (Killzones only)
5. **Confluence** -- How many factors align? (Score >= 5 to trade)

#### Price Delivery Algorithm

```
ERL (sweep liquidity) --> IRL (retrace to FVG/OB) --> ERL (target opposite liquidity)
```

---

### Market Structure

- **BOS (Break of Structure)**: Trend continuation -- price breaks prior swing in trend direction
- **CHoCH (Change of Character)**: Trend reversal warning -- breaks opposing swing
- **MSS (Market Structure Shift)**: CHoCH + displacement = confirmed reversal
- **MSS Validation**: Swing violation + displacement candle (large body, small wicks) + FVG created + occurs after liquidity sweep
- **Rule**: Never trade against TWO timeframes above your entry TF

#### Multi-TF Hierarchy

```
Weekly --> Daily --> 4H --> 1H --> 15M/5M --> 1M
(bias)   (swing)  (intermediate) (entry) (execution) (precision)
```

---

### Liquidity

- **BSL (Buy-Side)**: Above swing highs, EQH, PDH, PWH, session highs
- **SSL (Sell-Side)**: Below swing lows, EQL, PDL, PWL, session lows
- **Sweep != Breakout**: Wick through + body closes back = sweep (high-prob reversal)
- **Equal highs/lows** are the strongest engineered liquidity pools

---

### PD Arrays (Entry Zones)

#### Fair Value Gaps (FVG)
- 3-candle formation where C1 and C3 wicks don't overlap
- Best entry: upper 25% (bullish) or lower 25% (bearish) of the gap
- First touch (untouched) FVGs are strongest
- 50%+ filled = mitigated
- **FVG role: continuation, not reversal** — FVGs are best used to add to a running winning position or for trend continuation setups, NOT as the first reversal entry signal
- **One-time use rule**: once price reacts to a FVG and continues, the zone is consumed. A subsequent break through a consumed FVG does NOT create an IFVG.
- **Midpoint (50%) = decision line**: price respecting the midpoint → FVG holds → trade normally. Price closing through the midpoint → IFVG is forming → flip the zone.

#### IFVG (Inversion / Inverse Fair Value Gap)
- A FVG that price completely ignores on **first contact** — closes straight through it
- Polarity flip: bullish FVG violated → becomes bearish IFVG (resistance). Bearish FVG violated → becomes bullish IFVG (support)
- **Two valid conditions (BOTH required — standalone IFVGs are noise):**
  1. **After a liquidity grab**: market sweeps BSL/SSL, stops triggered, price returns inside range → IFVG forms confirming reversal momentum
  2. **At a HTF key level**: IFVG forms inside a daily/4H OB, FVG, or major supply/demand zone → institutional confirmation
- **CISD (Change in State of Delivery)**: when the breakout candle through a FVG simultaneously creates a new FVG that overlaps the IFVG → **highest probability reversal signal**. Marks a sudden shift in momentum; strongest at end of trend.
- Entry options: immediate (right as IFVG forms) or limit at highest/lowest point of IFVG zone. SL below/above most recent swing.

#### Order Blocks (OB)
- Last opposing candle before displacement
- **3-Part Validation**: Displacement + FVG creation + BOS/MSS (ALL required)
- Best entry: 50% of OB body (mean threshold)
- Price closing through entire OB body = invalidated

#### OB Drawing — The One-Candle Rule
> Source: "The ONE CANDLE Trading Strategy" — Jdub Trades

**Core principle:** In an uptrend, down-close candles support price higher. In a downtrend, up-close candles support price lower.

**Bullish OB (down-close candle in uptrend):** Mark from wick high to body high.
**Bearish OB (up-close candle in downtrend):** Mark from wick low to body low.

**OB Probability Ranking:**

| Rank | Candle Shape | Draw Zone | Notes |
|------|-------------|-----------|-------|
| Highest | Candle with wick | Wick to body edge | Tightest reaction zone → strong momentum |
| Medium | Small wick | Full wick to far body edge | Give more room — slightly wider zone |
| Lowest | Full-body (no wick) | Body top to body bottom | Can bounce anywhere → wide, less precise |

**OB quality checklist:**
- Trending market required — OBs won't hold in chop/range
- Best at key levels (PDH/PDL + opening range + HTF level = A+ confluence)
- Unmitigated liquidity objective must exist (clear target for continuation)
- Wick-to-body hold = strong momentum; price falling to OB bottom = valid but slower move

#### OB Variants
- **Breaker Block**: Failed OB, now acts as S/R in opposite direction
- **Mitigation Block**: Partially filled OB, trade on second test
- **Reclaimed OB**: Swept but held -- strongest type
- **BB + FVG Confluence**: Breaker Blocks often sit slightly above/below a FVG. Price reacts from the BB *first*, not the FVG. When a BB **overlaps** with a FVG → significantly higher probability entry zone.

#### Premium / Discount & OTE
```
100% -- Swing High ---- PREMIUM (sell entries)
 79% -- OTE Top
70.5% - OTE Sweet Spot (primary entry)
 62% -- OTE Bottom
 50% -- EQUILIBRIUM (skip -- no edge)
  0% -- Swing Low ----- DISCOUNT (buy entries)
```

#### Fibonacci Levels (ICT Custom)
- Entry: 0.62, 0.705, 0.79 (OTE zone)
- Targets: -0.27, -0.62, -1.0, -1.5, -2.0, -2.5

---

### Time Theory -- Sessions & Killzones (EST)

| Session | Time (EST) | Action |
|---------|-----------|--------|
| Asian | 7 PM - 12 AM | Mark range (AH/AL) -- NO trading |
| **London KZ** | **2-5 AM** | **PRIMARY EXECUTION** |
| **NY Open KZ** | **8:30-11 AM** | **PRIMARY EXECUTION** |
| NY Lunch | 11 AM - 1 PM | **NO TRADING** |
| NY Afternoon | 1-3 PM | Secondary setups only |

#### Silver Bullet Windows
- SB1: 2:00-3:00 AM (London Open)
- SB2: 3:00-4:00 AM (London Continuation)
- **SB3: 9:30-10:30 AM (NY Open -- PRIMARY)**

#### News Rule
- No entries within 30 min before/after red-folder news
- FOMC/NFP/CPI days: consider sitting out or post-event only

---

### The 3-Element Entry Framework

Every valid ICT entry must satisfy all three elements in order:

```
① HTF Area of Interest (AOI) — where is price? (HTF FVG, OB, supply/demand, or after liquidity sweep)
② Confirmation             — what happened? (MSS / CHoCH on LTF)
③ Entry Model              — how to enter? (Breaker Block / FVG / Mitigation Block / IFVG / Order Block)
```

- Entries "in the middle of nowhere" without a qualifying AOI are invalid regardless of how clean the model looks
- This framework applies universally to all 5 precision entry models

### FVG-in-FVG Two-Timeframe Execution Plan

A systematic continuation setup using FVGs across two timeframes:

**Timeframe pairing rule**: entry TF must be **2 levels lower** than the analysis TF.

| Analysis TF | Entry TF |
|-------------|----------|
| Daily | 1H |
| 4H | 15M |
| 1H | 5M |

**Phase 1 — HTF Analysis:**
1. Identify market direction via BOS / liquidity sweeps / CHoCH+
2. Mark HTF FVG in correct zone (discount for buys, premium for sells — apply 50% Fib filter)
3. Wait for price to enter the HTF FVG zone

**Phase 2 — LTF Execution:**
1. Identify reversal on LTF: liquidity sweep above swing high (aggressive entry) or CHoCH (conservative)
2. After confirmation: find new **LTF FVG** in the direction of the trade
3. Entry: limit at the **start of the LTF FVG zone** | SL: above/below the LTF FVG
4. TP1: 1:1 → close 50% of position, move SL to breakeven
5. TP2: next key HTF level

> The HTF gap defines *where* to be — the LTF gap defines *when* to enter. They don't need to overlap exactly.

**Edge-case SL handling:**
- Small LTF FVG → use a larger surrounding zone as SL to survive noise
- Large LTF FVG → enter at 50% midpoint of the zone to reduce SL size

---

## FVG Selection — 4 Rules for High-Probability FVGs
> Source: "Fair Value Gap Secrets I Wish I Knew as a Beginner" — Justin Bennett (64K views, trading since 2007)

### Imbalance vs Inefficiency — Cause and Effect
```
Imbalance = cause (supply/demand mismatch at a level)
Inefficiency = effect (the gap/zone that forms on the chart)
They are NOT interchangeable terms — one creates the other.
FVG, OB, or any gap = the inefficiency. The sudden supply/demand shift = the imbalance.
```

### Why Markets Revisit FVGs
```
Market makers must facilitate large orders → need liquidity
Fast moves away from zones = unfilled pending orders left behind
Market returns to those pockets to fill resting orders
FVGs fill because of LIQUIDITY — market makers drive price back to unfilled zones
Markets are "liquidity-seeking machines" — always moving toward deepest liquidity pools
```

### The 4 Rules (ALL must be satisfied)
```
Rule 1: Must be WITH the trend (or after a confirmed CHoCH establishing new trend)
  → Never trade counter-trend FVGs
  → CHoCH identification: find last BOS → highest high within that leg = CHoCH level
  → Once price closes above/below CHoCH level → new trend confirmed → only trade that direction

Rule 2: Must trigger a BOS or CHoCH
  → The FVG must be associated with a structural break — not an internal move
  → Internal FVGs (within a range, no structural break) = AVOID
  → The BOS doesn't need to happen ON the FVG candle, but within the same leg

Rule 3: Must be in discount (buys) or premium (sells)
  → Draw Fib from external low to external high (buys) or high to low (sells)
  → Only trade FVGs BELOW the 50% line (buys) or ABOVE the 50% line (sells)
  → FVGs in premium during uptrend or discount during downtrend = SKIP
  → Fib tip: remove all levels except 0%, 50%, 100% → shade premium/discount zones

Rule 4: One-time use only
  → Once a FVG is tested/mitigated, it is consumed — do NOT trade it again
  → Reason: the resting orders that caused the retrace are now filled
  → A second test has no guaranteed liquidity
```

### FVGs as Targets (Not Just Entries)
```
FVGs work as profit targets, not only entry zones:
  → In uptrend, unfilled bearish FVGs above = resistance targets
  → In downtrend, unfilled bullish FVGs below = support targets
  → Combine with HTF structure for target selection
```

### Area of Interest (AOI) Narrowing Process
```
Step 1: Identify trend direction via BOS/CHoCH on 1H+
Step 2: Mark external high and external low of current leg
Step 3: Draw 50% Fib → identify discount/premium zone
Step 4: Mark all FVGs within the valid zone (1H + 15M)
Step 5: Overlap the discount/premium box with the FVG zones → narrowed AOI

Target AOI width: 10-15 pips on 1H setups
If AOI > 20 pips → too broad, need LTF FVG refinement
```

### Multi-TF FVG Refinement for Entry
```
1H FVG (direction) → 15M FVGs within zone (refinement) → 5M/1M CHoCH (entry trigger)

Common mistake: Starting on 1M/5M without 1H context
→ Always top-down: define HTF AOI first, THEN drop to LTF for execution
→ 15M CHoCH > 5M CHoCH (fewer but higher-quality entries)
→ If 5M gives CHoCH but 15M does not → skip the trade
```

---

## SMC Precision Entry Techniques — 3 Models
> Source: "BEST SMC Entry Strategies for Low-Risk Trades" — The Trading Geek / Brad (190K views, $1M+ yearly)

Core philosophy: Losses are inevitable. The edge comes from minimizing loss SIZE via tight SL entries, not from win rate. Aim for 3:1+ RR minimum.

### Entry Model 1: Displacement Trap Entry (Highest Probability)
```
Catches the FINAL liquidity sweep, not early ones.

Step 1: Identify the impulse candle that led to a BOS
  → Map the entire impulse move
  → Identify the last internal lower high (bearish) or higher low (bullish)
  → When price breaks that level = short-term market shift (pullback phase begins)

Step 2: Wait for FINAL liquidation (not just any sweep)
  → Price pulls back, retail enters early (FOMO entries at first reaction)
  → Early entries get stopped out → this is the DISPLACEMENT TRAP
  → Wait for price to CLOSE PAST the imbalance from Step 1 (not just wick)
  → The leg that closes through the imbalance = final sweep confirmation

Step 3: Confirmation — internal structure shift
  → Map internal lower highs (bearish pullback) or higher lows (bullish pullback)
  → Wait for price to break the LAST internal swing point
  → This confirms internal structure aligned with HTF direction
  → NO entry without structural confirmation

SL: Below the final liquidity sweep low (buys) / above sweep high (sells)
  → This level is "protected" — liquidity already swept
TP: Fixed 3:1 RR OR next opposing supply/demand zone
```

### Why Early Entries Fail (The Displacement Trap Mechanism)
```
Sequence of traps:
  1. Strong impulse → retail FOMO entries on first pullback
  2. Retail stops below pullback → liquidity pool forms
  3. Price sweeps those stops (Trap #1) → some re-enter
  4. Price sweeps DEEPER past original imbalance (Trap #2 — displacement)
  5. Only AFTER displacement trap clears → real institutional flow begins
  6. YOUR entry: after displacement trap + structural confirmation

Visual clues of final sweep:
  → Candles losing momentum (getting smaller)
  → Lower wicks getting longer (buying pressure building)
  → Volume declining on the downmove
```

### Entry Model 2: Refined Order Block Entry (Aggressive)
```
Higher frequency, more aggressive — limit orders, no confirmation.

OB Identification Acronym: BASIL
  B = Break of Structure (OB must precede a BOS)
  A = Alignment with trend (OB direction matches HTF bias)
  S = Sweep of liquidity (OB formed after sweeping highs/lows)
  I = Imbalance (OB led to large displacement candle / FVG)
  L = Last candle (the OB is the LAST candle before the displacement)

More BASIL criteria checked = stronger OB = higher probability

Refinement Process:
  1. Mark OB on 1H (typically 15-25 pips wide — too wide for day trading)
  2. Drop to 15M or 5M within the 1H OB zone
  3. Identify the LAST candle before displacement on LTF = refined OB
  4. Refined OB typically 5-10 pips wide → sniper SL

Also identify "extreme zone" — outermost supply/demand within the OB
  → Two zones: refined OB (first target) + extreme zone (second opportunity)

Execution:
  → LIMIT order at edge of refined OB zone
  → SL above/below the refined OB
  → TP: 3:1 RR fixed OR next swing H/L
  → ~60-70% hit rate, losses are small (tight SL)
  → If stopped out → OB becomes breaker block → Entry Model 3
```

### Entry Model 3: Breaker Block Entry (Adaptive)
```
Turns Model 2 losses into wins. Failed OBs become breaker blocks.

When an OB fails (price closes through it):
  1. The OB is now a breaker block (polarity flip)
  2. All liquidity at that level has been absorbed
  3. Next time price returns → opposite direction support/resistance
  4. Entry: buy at failed bearish OB (now bullish breaker) or vice versa

Execution:
  → Wait for price to return to the failed OB / breaker zone
  → Enter on mitigation of the breaker block
  → SL: below/above the breaker block
  → TP: 3:1 RR

Combined Model 2 + 3 math:
  → Trade 1 (Model 2): stopped out at -1R
  → Trade 2 (Model 3 on same zone): win at +3R
  → Net: +2R from two trades on same zone
```

### Session Timing Filter for Entries (Q-Zones)
```
Best Trading Windows (EST):
  Asian Q-Zone:   7:00 PM - 12:00 AM → JPY, AUD, NZD pairs
  London Q-Zone:  2:00 AM -  5:00 AM → EUR, GBP pairs (20-50 pip moves)
  NY Q-Zone:      8:30 AM - 11:00 AM → USD pairs, indices, gold
  London Close:  10:00 AM - 12:00 PM → GBP continuation/reversal setups

Rules:
  → Only trade currency pairs during THEIR session Q-zone
  → Entry during Q-zone = immediate volatility → fast move to TP
  → Entry outside Q-zone → SKIP IT
```

### 1M Order Block Warning
```
1-minute order blocks are extremely unpredictable and unreliable
  → Too much noise on 1M → OBs get blown through frequently
  → Minimum reliable OB timeframe: 5M (scalping) or 15M (day trading)
```

---

## Order Block Quality Criteria — Backtested Filters
> Source: "How to Identify Best Order Blocks to Trade?" — Smart Risk (2.4M views)

### 5 Filters to Increase OB Win Rate
```
Filter 1: Primary Rules (standard OB definition)
  → Baseline win rate: ~50% without additional filters

Filter 2: Market Structure Alignment
  → Bullish OBs only in bullish structure (HH/HL)
  → Bearish OBs only in bearish structure (LH/LL)
  → This single filter increases win rate by 10-15%

Filter 3: Market Volatility & Spread
  → Avoid OBs during low-volatility periods (wide spreads)
  → Trade OBs during killzone hours when spreads are tightest

Filter 4: Recency
  → More recent OBs > older ones
  → OB from 200 bars ago < OB from 20 bars ago
  → Trade the MOST RECENT unmitigated OB in trend direction

Filter 5: LTF Confirmation at OB
  → Don't blindly limit order at OB — wait for LTF reaction
  → CHoCH or BOS on LTF at the OB level
  → Conservative but maximizes win rate at cost of some RR
```

---

### Trading Strategies

#### Strategy A: MSS + FVG (Primary)
1. Establish HTF bias (Daily)
2. Mark key levels (PDH/PDL, AH/AL, EQH/EQL)
3. Wait for liquidity sweep (1H/15M)
4. Confirm MSS with displacement (15M/5M)
5. Enter at FVG in correct premium/discount zone
6. SL: beyond sweep point + 5-10 pip buffer
7. TP: nearest opposing liquidity | Min RR: 1:2

#### Strategy B: Silver Bullet (Time-Based)
1. Pre-determine daily bias before window
2. Observe first 15 min of window (no entry)
3. Wait for displacement + FVG within the window
4. Entry before window closes | Min RR: 1:3

#### Strategy C: Judas Swing (Reversal)
- False move at session open against daily bias
- Sweeps known liquidity, then reverses with displacement
- London: sweeps Asian range | NY: sweeps London extreme
- Enter from FVG after MSS confirmation | Min RR: 1:2

#### Strategy D: Market Maker Models
- **MMBM (Buy)**: Consolidation > engineering SSL > reversal at HTF PD Array > targets BSL
- **MMSM (Sell)**: Consolidation > sweep BSL > displacement down > targets SSL
- Enter FVG/OB after MSS + SMT divergence | Min RR: 1:3

#### Strategy D2: MMM + OTE Prop Firm Model (Omor / NBB Trader)
**Source:** Chart Fanatics Ep. w/ Omor — $1M+ payouts, $30M+ funded students

**Framework (not an entry — a structural template):**
1. **Pre-determined daily bias required** — without bias you can't tell manipulation from distribution
2. **Only trade at key levels**: PDH/PDL, PWH/PWL, 4H+ PD arrays (FVG, Breaker, OB, Mitigation)
3. **Wait for price to open near key level** — if open isn't near a key level, sit out
4. **Identify AMD on 15m**: Asia accumulates → London manipulates (sweeps opposite side) → NY distributes

**Execution stack:** Daily (bias) → 4H (framework/retracement) → 15m (breaker + OTE) → 5m (only for FVG inside 15m displacement)

**Entry rules:**
- Wait for **breaker block with displacement** (body close, not wick) on 15m = Smart Money Reversal
- If **wicky close** or **opposing 15m PD array** blocks path → skip 1st leg, wait for **2nd leg** ("Silver Bullet" retracement)
- Apply OTE: 62% entry + **90% SL** (not swing high) = **2.2R fixed** | 70.5% + 90% SL = **~3R**
- R:R is fixed regardless of range size because entries are percentage-based

**90% SL Optimization:**
- Price reaching 90% of range and NOT hitting 100% happens <5% of the time (1 in 15 trades)
- Shaving 10% off SL dramatically improves R:R with minimal increase in stop-outs

**Trade management — the 0.2 rule:**
1. When price reaches 0.2 level (20% toward TP) with **body close** → move SL to breakeven
2. At BE: remove TP entirely → original TP becomes new SL → trail from there
3. "Coin flip" decision: if account can afford to miss TP, remove it and go for runner
4. Scale in: at BE add same risk again (e.g., another 1%). Worst case = 1% loss. Best case = doubled leverage

**Prop firm math:**
- 1.5% risk + 62% OTE + 90% SL = 2.2R = ~3.3% gain per win
- **3 filtered wins = 10% target passed**
- Within 10 trades with filtered OTE setups, challenge should be passed

**London-to-NY OTE:**
- If positioned during London manipulation, hold through entire NY session
- Check ADR: if <50% of average daily range used by NY open, continuation entries valid
- London Close (10 AM–12 PM NY) can provide 2nd distribution leg if ADR permits

#### Strategy E: Unicorn Model
- Breaker Block + FVG overlap = high-conviction entry zone
- OB fails > becomes Breaker > displacement creates FVG > overlap is the entry
- Min RR: 1:3

#### Strategy F: ICT 2022 Entry Model
1. Daily bias + key levels + NY midnight range marked
2. Wait for liquidity sweep of midnight/Asian range
3. Confirm MSS on LTF (5M/3M/1M)
4. Enter at PD Array in correct zone | Min RR: 1:3

---

### Risk Management (Non-Negotiable Rules)

| Rule | Value |
|------|-------|
| Max risk per trade | 1% (0.5% first month live) |
| Max concurrent trades | 2 (same direction only) |
| Max daily loss | 3% (then STOP) |
| Max weekly loss | 5% (then STOP) |
| Consecutive losses | 2 = stop that session |
| Correlated pairs | Count as 1 trade at 1% combined |
| Max trades per day | 3 |

#### Position Sizing
```
Position Size = (Account Balance x Risk%) / (SL Pips x Pip Value)
```

#### Drawdown Protocol
- 3% daily: stop for day
- 5% weekly: stop for week + review journal
- 10% monthly: reduce to 0.5%, 1 week demo
- 15% from peak: stop live, backtest 50 more trades
- 20% from peak: full review, 1 month demo

---

### Trade Management

1. **Entry to TP1**: No SL movement, no adding to position
2. **At TP1**: Close 50-75%, move SL to breakeven
3. **After TP1**: Trail SL using LTF swing points
4. **Close triggers**: TP2 hit, opposing MSS on 15M, red-folder news, 3 PM EST (day trades), Friday 2 PM EST

---

### Confluence Scoring (Score Before Every Entry)

| Factor | Points |
|--------|--------|
| HTF Bias alignment | +2 |
| Killzone timing | +2 |
| Liquidity sweep confirmed | +2 |
| MSS/CHoCH confirmed | +2 |
| FVG entry | +1 |
| Order Block entry | +1 |
| OTE zone (62-79%) | +1 |
| Premium/Discount correct | +1 |
| SMT Divergence | +1 |
| NWOG alignment | +1 |
| BB + FVG overlap (confluence) | +1 |
| IFVG after liquidity grab | +1 |
| CISD (IFVG + new FVG overlap) | +1 |

- **8-12**: Full risk (1%) | **5-7**: Half risk (0.5%) | **< 5**: NO TRADE
- **Hard requirements** (must have all 4): HTF bias + Killzone + Sweep + MSS = base 8

---

### IPDA & Weekly Profiles

#### IPDA Look-Back Windows
- 20-day: short-term targets | 40-day: medium-term | 60-day: long-term

#### NWOG (New Week Opening Gap)
- Friday close to Sunday open gap -- strong weekly magnet
- Track last 4 NWOGs + current

#### Weekly Day Tendencies
- **Monday**: Range establishment, one weekly extreme often forms
- **Tuesday**: Most common for weekly low (bullish) or high (bearish)
- **Wednesday**: Pivot/reversal point
- **Thursday**: Expansion day -- strong conviction moves
- **Friday**: Profit-taking, close before weekend

---

### MQL5 Indicator Arsenal (Key Indicators)

#### Market Structure & SMC
- `AdvanceSMC.mq5` -- Advanced SMC structure detection
- `Smart_Money_Algo_Pro_E5.mq5` -- CHOCH, OB, demand/supply
- `ICT_OB_BB_Detector_v3.mq5` -- Order Blocks & Breaker Blocks
- `SwingHL_Pro_v8_5.mq5` -- Professional swing high/low detection

#### FVG Detection
- `SMC_FVG_Validator_v24b.mq5` -- FVG validation & filtering
- `SMC_FVG_ML_Optimized_v22.mq5` -- ML-optimized FVG detection
- `FVG_Trade_Analyzer_V3.mq5` -- FVG trade simulation with SL/TP

#### Session & Killzone
- `ICT_SilverBullet_PRO.mq5` -- Silver Bullet pattern detection
- `London_Hunter_v21.20.mq5` -- London session breakout analysis
- `ICT_Unicorn_Model.mq5` -- Unicorn pattern identification

#### Order Flow & Volume
- `MM_Ultimate_Pro_Analyzer.mq5` -- Volume delta, CVD, BOS/CHoCH, FVG, OB
- `OrderFlowAnalysis.mq5` -- Order flow analysis

#### Multi-Symbol Scanning
- `MS_Breakout_Monitor_v94.mq5` -- 32+ symbol breakout monitoring
- `MS_London_Hunter_v21b.mq5` -- Multi-symbol London session scan
- `MS_NY_Breakout_Monitor_v1a.mq5` -- Multi-symbol NY breakout scan

#### Recommended Setups per Strategy
- **A (MSS+FVG)**: AdvanceSMC + SMC_FVG_Validator_v24b + ICT_OB_BB_Detector_v3 + EnhancedRangeBox_Pro_v3
- **B (Silver Bullet)**: ICT_SilverBullet_PRO + SMC_FVG_Finder_v1a + London_Hunter_v21.20
- **C (Judas Swing)**: Smart_Money_Algo_Pro_E5 + SMC_FVG_Validator_v24b + EnhancedRangeBox_Pro_v3
- **D (Market Maker)**: MM_Ultimate_Pro_Analyzer + ICT_OB_BB_Detector_v3 + BreakerBlocks_v2
- **E (Unicorn)**: ICT_Unicorn_Model + BreakerBlocks_v2 + SMC_FVG_Validator_v24b

---

### Markets & Pairs

| Market | Instruments | Best Sessions |
|--------|------------|---------------|
| Forex | EUR/USD, GBP/USD, EUR/GBP, USD/CHF, USD/CAD | London, NY |
| Commodities | XAU/USD, XAG/USD | NY |
| Indices | NAS100, US30, SPX500 | NY |
| Crypto | BTC/USD, ETH/USD | All sessions |

#### SMT Divergence Pairs
- EUR/USD <-> GBP/USD (positive) | ES/SPX <-> NAS100 (positive)
- XAU/USD <-> XAG/USD (positive) | DXY <-> EUR/USD (inverse)

---

### Key Abbreviations

| Abbr | Meaning |
|------|---------|
| PDH/PDL | Previous Day High/Low |
| PWH/PWL | Previous Week High/Low |
| AH/AL | Asian Range High/Low |
| EQH/EQL | Equal Highs/Lows |
| BSL/SSL | Buy-Side/Sell-Side Liquidity |
| FVG | Fair Value Gap |
| OB | Order Block |
| BB | Breaker Block |
| MSS | Market Structure Shift |
| BOS | Break of Structure |
| CHoCH | Change of Character |
| OTE | Optimal Trade Entry (62-79% Fib) |
| NWOG | New Week Opening Gap |
| AMD/PO3 | Accumulation-Manipulation-Distribution / Power of 3 |
| IPDA | Interbank Price Delivery Algorithm |
| IRL/ERL | Internal/External Range Liquidity |
| MMBM/MMSM | Market Maker Buy/Sell Model |
| SMT | Smart Money Technique (Divergence) |
| IFVG | Inverse Fair Value Gap |

---

### Pre-Trade Checklist (Every Trade)

```
[] 1. Daily bias: BULLISH / BEARISH (neutral = NO TRADE)
[] 2. Killzone active: London (2-5 AM) / NY (8:30-11 AM)
[] 3. No red-folder news within 30 min
[] 4. ① AOI: price at HTF FVG / OB / supply/demand OR after liquidity sweep
[] 5. ② Confirmation: MSS / CHoCH confirmed (displacement + FVG)
[] 6. ③ Entry model: valid Breaker / FVG / Mitigation / IFVG / OB identified
[] 7. If IFVG: preceded by liquidity grab OR at HTF key level (no standalone IFVGs)
[] 8. Correct zone (discount for buys, premium for sells)
[] 9. RR >= minimum for strategy
[] 10. Risk <= 1% of account
[] 11. Confluence score >= 5
[] 12. Daily loss < 3%
[] 13. Consecutive losses < 2 this session

ALL CHECKED = EXECUTE | ANY FAIL = STAND ASIDE
```

---

### Daily Execution Routine

1. **Pre-Market (40 min before KZ)**: Check calendar, Weekly/Daily context, determine bias, mark levels (PDH/PDL/AH/AL/EQH/EQL), plan 3 scenarios (bullish/bearish/no-trade), set alerts
2. **During Killzone**: Alert triggers > 15M/5M charts > observe sweep > wait for MSS+FVG > check confluence > execute if score >= 5
3. **Post-Trade**: Journal every trade, review entry quality, update levels for tomorrow, close charts

---

### Backtesting & Progression

#### Backtesting Targets (100 trades minimum per strategy)
- Win Rate > 45% | Avg RR > 1:2 | Expectancy > 0 | Profit Factor > 1.5 | Max DD < 15%

#### Progression Path
1. **Weeks 1-2**: Education (study, identify concepts on charts, no trades)
2. **Weeks 3-6**: Backtest Strategy A on EUR/USD (100 trades)
3. **Weeks 7-10**: Demo trading (3 consecutive profitable weeks to proceed)
4. **Months 3-5**: Live at 0.5% risk (execution quality focus)
5. **Month 6+**: Scale to 1% after 3 profitable months
6. **Month 12+**: All 6 strategies, multi-symbol, 3-5% monthly target

---

### Source Files

| File | Description |
|------|-------------|
| `P1/ICT_MASTER_STRATEGY_PLAN.md` | Complete master reference |
| `P1/01_ict_core_concepts.md` | Core SMC concepts |
| `P1/02_ict_detailed_strategies.md` | Strategy summaries |
| `P1/03_ict_daily_routine.md` | Daily execution process |
| `P1/04_ict_risk_psychology.md` | Risk & psychology framework |
| `P1/subs/` | Deep-dive guides per topic |

---

---

## Advanced ICT Entry Models (merged from ict-smart-money)

### 3-Element Entry Model

ICT entries require three confluences to align before taking a trade:

```
Element 1: CONTEXT (HTF bias)
  └── Daily/4H direction — bullish or bearish dealing range?

Element 2: CATALYST (trigger event)
  └── Liquidity sweep, FVG test, CISD, structure shift

Element 3: ENTRY (LTF confirmation)
  └── M1/M5 displacement + FVG or OB on entry timeframe
```

All 3 must align. Missing any element = skip the trade.

### CISD (Change in State of Delivery)
- Candle closes opposite to current order flow direction
- Signals smart money has shifted intent
- Most powerful at liquidity levels (old highs/lows, FVG extremes)

### FVG-in-FVG Plan
1. Identify daily FVG (primary target zone)
2. Within daily FVG, find 4H FVG (entry refinement)
3. Within 4H FVG, find M15/M5 FVG (precise entry)
4. Enter at M5 FVG with stop beyond 4H FVG extreme

### Cameron's Model — Three-Layer ICT Entry (Smart Risk)
- **Sequence:** (1) Price sweeps SSL/BSL near an existing FVG → (2) FVG is violated (closed through) → becomes IFVG → (3) Price returns to IFVG (retest from opposite side) + LTF CHoCH inside IFVG → entry
- **Entry:** Limit at IFVG zone on retest; stop beyond IFVG; target next BSL/SSL
- **Logic:** Sweep + FVG violated (IFVG) + IFVG retest + CHoCH = four-layer institutional confirmation
- **Best context:** IFVG formed at HTF POI (OB, S&D zone) for additional confluence

### Turtle Soup — Fade the Stop Run (Smart Risk)
- **Bearish Turtle Soup:** Sweep above swing high or equal highs → reversal candle closes BACK BELOW the high → enter short; stop above sweep wick; target next SSL
- **Bullish Turtle Soup:** Sweep below swing low or equal lows → reversal candle closes BACK ABOVE the low → enter long; stop below sweep wick; target next BSL
- **Best context:** At HTF premium zones (bearish) or discount zones (bullish); always confirm with LTF CHoCH
- **Win rate:** High at HTF confluence zones; identical mechanism to Liquidity Raid Entries but with explicit candle confirmation requirement

### Silver Bullet — Mechanical Rules & Backtested Parameters (Smart Risk)
- **Three time windows (NY local time):** 2:00–3:00 AM, 10:00–11:00 AM, 2:00–3:00 PM
- **Mechanical entry:** liquidity sweep during window → MSS (body close CHoCH on M1/M5) → FVG formed by MSS impulse → enter at FVG 50%; stop at sweep wick extreme; target opposite BSL/SSL
- **Non-negotiable rules:** sweep MUST precede MSS; enter ONLY first FVG retest; max 1 trade per window
- **Best window:** 10:00–11:00 AM NY has highest win rate (backtested EURUSD)
- **Daily bias alignment:** counter-trend Silver Bullets have ~60% lower win rate; only trade WITH D1 bias
- **Time exit:** if trade doesn't reach target within 2 hours after window close, exit at market

### NBB Trader (Omor) — Simple Retracement ICT Entry

**Why 90% of SMC traders fail:** They apply OB/FVG like retail patterns without understanding the algorithmic delivery sequence. Correct concept, wrong timing = stopped out.

**The simple retracement model (Omor's core entry):**
```
1. Identify D1/W1 liquidity target (WHERE price is going — BSL or SSL)
2. Wait for liquidity sweep at a key level (equal H/L, prior swing extreme)
3. Wait for CHoCH after the sweep (confirms institutional direction change)
4. Enter at first pullback to: OB left by displacement candle, OR FVG in displacement
5. Stop: beyond the sweep wick extreme
6. Target: the original D1/W1 liquidity pool
```
Fewer steps = fewer mistakes. One sweep + one CHoCH + one zone = complete setup.

**Central bank macro alignment:**
- CB hawkish (rate hiking) → dollar strengthens → gold/risk assets weaker
- CB dovish (rate cutting) → dollar weakens → gold/risk assets stronger
- SMC setups WITH CB direction: 3/5 confluence sufficient
- SMC setups AGAINST CB direction: require 5/5 confluence or skip

**Economic calendar tiers (Omor's rules):**
| Tier | Events | Rule |
|------|--------|------|
| 1 | NFP, CPI, FOMC | No trading 30 min before or after |
| 2 | ISM, Retail Sales, PPI | Note it; reduce size; expect deviation |
| 3 | Minor data | Aware, trade normally |
Post-news: first clean OB/FVG formed AFTER release = highest-probability zone of the session.

---

## Related Skills

- [Session Scalping](../session-scalping.md)
- [Technical Analysis](../technical-analysis.md)
- [Liquidity Analysis](../liquidity-analysis.md)
- [Price Action](../price-action.md)
- [Market Regime Detection](../market-regime-classifier.md)
- [Strategy Selection](../strategy-selection.md)
