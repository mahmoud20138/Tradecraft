---
name: price-action
description: "Pure price action analysis: candlestick patterns & statistics, chart pattern recognition, harmonic patterns, Elliott Wave theory, and trendline/S&R detection. USE FOR: price action trading, candlestick pattern identification, candle pattern analysis, chart pattern recognition, harmonic patterns ABCD Gartley Butterfly Bat Crab, Elliott Wave count, trendline drawing, support resistance levels, head and shoulders, double top double bottom, engulfing candle, pin bar, doji, hammer, shooting star, inside bar, key level reaction, naked chart analysis, no-indicator trading."
related_skills:
  - technical-analysis
  - price-action
  - ict-smart-money
  - chart-vision
tags:
  - trading
  - analysis
  - price-action
  - harmonics
  - elliott-wave
  - technical-analysis
skill_level: intermediate
kind: reference
category: trading/strategies
status: active
---
> **Skill:** Price Action  |  **Domain:** trading  |  **Category:** analysis  |  **Level:** intermediate
> **Tags:** `trading`, `analysis`, `price-action`, `harmonics`, `elliott-wave`, `technical-analysis`



---

## Price Action Pure Engine

# Price Action Pure Engine — No Indicators

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class PriceActionEngine:

    @staticmethod
    def key_level_reaction(df: pd.DataFrame, levels: list[float], tolerance_atr_mult: float = 0.3) -> list[dict]:
        """Detect price reactions at key levels — the core of PA trading."""
        atr = (df["high"] - df["low"]).rolling(14).mean()
        reactions = []
        for level in levels:
            recent = df.tail(20)
            for i, (idx, bar) in enumerate(recent.iterrows()):
                tol = atr.loc[idx] * tolerance_atr_mult
                touching = bar["low"] <= level + tol and bar["high"] >= level - tol
                if touching:
                    body = abs(bar["close"] - bar["open"])
                    lower_wick = min(bar["open"], bar["close"]) - bar["low"]
                    upper_wick = bar["high"] - max(bar["open"], bar["close"])
                    if lower_wick > body * 2 and bar["close"] > bar["open"]:
                        reactions.append({"level": level, "time": idx, "type": "bullish_rejection",
                                         "signal": "BUY — rejection pin bar at key level"})
                    elif upper_wick > body * 2 and bar["close"] < bar["open"]:
                        reactions.append({"level": level, "time": idx, "type": "bearish_rejection",
                                         "signal": "SELL — rejection pin bar at key level"})
                    elif bar["close"] > level + tol and bar["open"] < level:
                        reactions.append({"level": level, "time": idx, "type": "bullish_engulf_level",
                                         "signal": "BUY — bullish engulfing through key level"})
        return reactions

    @staticmethod
    def inside_bar_breakout(df: pd.DataFrame) -> list[dict]:
        """Inside bar = compression before expansion. Trade the breakout."""
        signals = []
        for i in range(1, min(20, len(df))):
            idx = len(df) - i
            mother = df.iloc[idx - 1]
            inside = df.iloc[idx]
            if inside["high"] < mother["high"] and inside["low"] > mother["low"]:
                if idx + 1 < len(df):
                    breakout = df.iloc[idx + 1]
                    if breakout["close"] > mother["high"]:
                        signals.append({"type": "inside_bar_bullish_breakout", "idx": idx,
                                       "entry": round(mother["high"], 5), "stop": round(mother["low"], 5)})
                    elif breakout["close"] < mother["low"]:
                        signals.append({"type": "inside_bar_bearish_breakout", "idx": idx,
                                       "entry": round(mother["low"], 5), "stop": round(mother["high"], 5)})
                else:
                    signals.append({"type": "inside_bar_forming", "idx": idx,
                                   "buy_trigger": round(mother["high"], 5),
                                   "sell_trigger": round(mother["low"], 5)})
        return signals

    @staticmethod
    def engulfing_at_structure(df: pd.DataFrame, order: int = 10) -> list[dict]:
        """Engulfing candles at swing highs/lows — highest probability PA setup."""
        highs = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows = argrelextrema(df["low"].values, np.less, order=order)[0]
        signals = []
        for i in range(1, min(10, len(df))):
            idx = len(df) - i
            curr = df.iloc[idx]
            prev = df.iloc[idx - 1]
            # Bullish engulfing near swing low
            near_low = any(abs(df["low"].iloc[l] - curr["low"]) < (df["high"] - df["low"]).rolling(14).mean().iloc[idx] for l in lows if abs(l - idx) < 20)
            if curr["close"] > curr["open"] and prev["close"] < prev["open"] and curr["close"] > prev["open"] and curr["open"] < prev["close"] and near_low:
                signals.append({"type": "bullish_engulfing_at_structure", "idx": idx, "signal": "A+ BUY"})
            # Bearish engulfing near swing high
            near_high = any(abs(df["high"].iloc[h] - curr["high"]) < (df["high"] - df["low"]).rolling(14).mean().iloc[idx] for h in highs if abs(h - idx) < 20)
            if curr["close"] < curr["open"] and prev["close"] > prev["open"] and curr["open"] > prev["close"] and curr["close"] < prev["open"] and near_high:
                signals.append({"type": "bearish_engulfing_at_structure", "idx": idx, "signal": "A+ SELL"})
        return signals

    @staticmethod
    def full_pa_scan(df: pd.DataFrame, key_levels: list[float] = None) -> dict:
        levels = key_levels or []
        return {
            "level_reactions": PriceActionEngine.key_level_reaction(df, levels) if levels else [],
            "inside_bars": PriceActionEngine.inside_bar_breakout(df),
            "engulfing_at_structure": PriceActionEngine.engulfing_at_structure(df),
            "principle": "Trade what you SEE, not what you think. PA at key levels = highest probability.",
        }
```


---

## Candlestick Pattern Vision

# Candlestick Pattern Vision

## Overview
Pure computer vision approach to candlestick pattern detection. Extracts individual candle
geometries from chart images via contour detection, then classifies patterns using geometric
ratios. Works on any chart screenshot — TradingView, MT5, phone captures.

## Stack
- **OpenCV 4.13** — contour detection, morphological analysis, connected components
- **scikit-image 0.26** — region properties, label analysis
- **numpy 2.4** — geometric computations

---

## 1. Candle Geometry Extractor

```python
import cv2
import numpy as np
from skimage import measure, morphology as sk_morphology
from dataclasses import dataclass
from typing import Optional

@dataclass
class CandleGeometry:
    """Geometric properties of a single candlestick extracted from image."""
    x_center: int           # horizontal position (pixel)
    y_top: int              # highest point (wick top)
    y_bottom: int           # lowest point (wick bottom)
    body_top: int           # body top (max of open/close)
    body_bottom: int        # body bottom (min of open/close)
    width: int              # body width
    is_bullish: bool        # green/white = bullish
    confidence: float       # detection confidence

    @property
    def total_height(self) -> int:
        return self.y_bottom - self.y_top

    @property
    def body_height(self) -> int:
        return self.body_bottom - self.body_top

    @property
    def upper_wick(self) -> int:
        return self.body_top - self.y_top

    @property
    def lower_wick(self) -> int:
        return self.y_bottom - self.body_bottom

    @property
    def body_ratio(self) -> float:
        """Body size relative to total candle."""
        return self.body_height / max(self.total_height, 1)

    @property
    def upper_wick_ratio(self) -> float:
        return self.upper_wick / max(self.total_height, 1)

    @property
    def lower_wick_ratio(self) -> float:
        return self.lower_wick / max(self.total_height, 1)


class CandleExtractor:
    """Extract individual candlestick geometries from a preprocessed chart image."""

    @staticmethod
    def extract_candles(img: np.ndarray, color_info: dict = None) -> list[CandleGeometry]:
        """
        Extract all candlesticks from a chart image.
        Uses color segmentation + contour analysis + connected components.
        """
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, w = img.shape[:2]

        # Separate bullish (green) and bearish (red) candles
        green_mask = cv2.inRange(hsv, (35, 30, 30), (85, 255, 255))
        red_mask1 = cv2.inRange(hsv, (0, 30, 30), (15, 255, 255))
        red_mask2 = cv2.inRange(hsv, (165, 30, 30), (180, 255, 255))
        red_mask = cv2.bitwise_or(red_mask1, red_mask2)

        candles = []

        for mask, is_bull in [(green_mask, True), (red_mask, False)]:
            # Morphological cleanup
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

            # Connected components (scikit-image 0.26)
            labels = measure.label(mask, connectivity=2)
            regions = measure.regionprops(labels)

            for region in regions:
                # Filter by size — candles have specific aspect ratios
                bbox = region.bbox  # (min_row, min_col, max_row, max_col)
                region_h = bbox[2] - bbox[0]
                region_w = bbox[3] - bbox[1]

                if region_h < 5 or region_w < 2:  # Too small
                    continue
                if region_w > w * 0.1:  # Too wide (probably not a candle)
                    continue
                if region.area < 20:  # Too few pixels
                    continue

                # Determine body vs wick
                # Body is the thickest part; wick is thin
                col_slice = mask[bbox[0]:bbox[2], bbox[1]:bbox[3]]
                row_widths = np.sum(col_slice > 0, axis=1)

                # Body rows: where width is > 50% of max width
                max_width = row_widths.max()
                body_rows = np.where(row_widths > max_width * 0.5)[0]

                if len(body_rows) > 0:
                    body_top_local = body_rows[0]
                    body_bottom_local = body_rows[-1]
                else:
                    body_top_local = 0
                    body_bottom_local = region_h

                candles.append(CandleGeometry(
                    x_center=int(region.centroid[1]),
                    y_top=bbox[0],
                    y_bottom=bbox[2],
                    body_top=bbox[0] + body_top_local,
                    body_bottom=bbox[0] + body_bottom_local,
                    width=region_w,
                    is_bullish=is_bull,
                    confidence=min(region.area / 100, 1.0),
                ))

        # Sort by x position (left to right = chronological)
        candles.sort(key=lambda c: c.x_center)
        return candles
```

---

## 2. Single Candle Pattern Classifier

```python
class SingleCandleClassifier:
    """Classify individual candlestick patterns from geometry."""

    @staticmethod
    def classify(candle: CandleGeometry) -> dict:
        br = candle.body_ratio
        uwr = candle.upper_wick_ratio
        lwr = candle.lower_wick_ratio

        patterns = []

        # Doji: very small body
        if br < 0.1:
            if uwr > 0.3 and lwr > 0.3:
                patterns.append({"pattern": "long_legged_doji", "bias": "reversal", "strength": 0.7})
            elif uwr > 0.4:
                patterns.append({"pattern": "gravestone_doji", "bias": "bearish_reversal", "strength": 0.75})
            elif lwr > 0.4:
                patterns.append({"pattern": "dragonfly_doji", "bias": "bullish_reversal", "strength": 0.75})
            else:
                patterns.append({"pattern": "doji", "bias": "indecision", "strength": 0.5})

        # Hammer / Hanging Man: small body at top, long lower wick
        elif br < 0.35 and lwr > 0.55 and uwr < 0.1:
            if candle.is_bullish:
                patterns.append({"pattern": "hammer", "bias": "bullish_reversal", "strength": 0.8})
            else:
                patterns.append({"pattern": "hanging_man", "bias": "bearish_reversal", "strength": 0.7})

        # Inverted Hammer / Shooting Star: small body at bottom, long upper wick
        elif br < 0.35 and uwr > 0.55 and lwr < 0.1:
            if candle.is_bullish:
                patterns.append({"pattern": "inverted_hammer", "bias": "bullish_reversal", "strength": 0.65})
            else:
                patterns.append({"pattern": "shooting_star", "bias": "bearish_reversal", "strength": 0.8})

        # Marubozu: full body, no wicks
        elif br > 0.85 and uwr < 0.05 and lwr < 0.05:
            bias = "strong_bullish" if candle.is_bullish else "strong_bearish"
            patterns.append({"pattern": "marubozu", "bias": bias, "strength": 0.85})

        # Pin bar: small body, one very long wick
        elif br < 0.25 and (uwr > 0.6 or lwr > 0.6):
            direction = "bullish" if lwr > uwr else "bearish"
            patterns.append({"pattern": "pin_bar", "bias": f"{direction}_reversal", "strength": 0.8})

        # Spinning top: small body, both wicks present
        elif br < 0.3 and uwr > 0.2 and lwr > 0.2:
            patterns.append({"pattern": "spinning_top", "bias": "indecision", "strength": 0.4})

        if not patterns:
            patterns.append({"pattern": "regular", "bias": "bullish" if candle.is_bullish else "bearish", "strength": 0.3})

        return {"candle": patterns[0], "all_matches": patterns,
                "geometry": {"body_ratio": round(br, 3), "upper_wick_ratio": round(uwr, 3), "lower_wick_ratio": round(lwr, 3)}}
```

---

## 3. Multi-Candle Pattern Classifier

```python
class MultiCandleClassifier:
    """Detect patterns spanning 2-3 candles."""

    @staticmethod
    def classify_sequence(candles: list[CandleGeometry]) -> list[dict]:
        patterns = []
        if len(candles) < 2:
            return patterns

        for i in range(len(candles) - 1):
            c1, c2 = candles[i], candles[i + 1]

            # Bullish Engulfing
            if not c1.is_bullish and c2.is_bullish and c2.body_height > c1.body_height * 1.2:
                patterns.append({"pattern": "bullish_engulfing", "position": i, "bias": "bullish", "strength": 0.82})

            # Bearish Engulfing
            if c1.is_bullish and not c2.is_bullish and c2.body_height > c1.body_height * 1.2:
                patterns.append({"pattern": "bearish_engulfing", "position": i, "bias": "bearish", "strength": 0.82})

            # Tweezer Top/Bottom
            if abs(c1.y_top - c2.y_top) < 3:  # Equal highs
                patterns.append({"pattern": "tweezer_top", "position": i, "bias": "bearish", "strength": 0.65})
            if abs(c1.y_bottom - c2.y_bottom) < 3:  # Equal lows
                patterns.append({"pattern": "tweezer_bottom", "position": i, "bias": "bullish", "strength": 0.65})

        # 3-candle patterns
        for i in range(len(candles) - 2):
            c1, c2, c3 = candles[i], candles[i + 1], candles[i + 2]

            # Morning Star
            if not c1.is_bullish and c2.body_ratio < 0.2 and c3.is_bullish and c3.body_height > c1.body_height * 0.5:
                patterns.append({"pattern": "morning_star", "position": i, "bias": "bullish_reversal", "strength": 0.85})

            # Evening Star
            if c1.is_bullish and c2.body_ratio < 0.2 and not c3.is_bullish and c3.body_height > c1.body_height * 0.5:
                patterns.append({"pattern": "evening_star", "position": i, "bias": "bearish_reversal", "strength": 0.85})

            # Three White Soldiers
            if all(c.is_bullish for c in [c1, c2, c3]) and c2.body_bottom < c1.body_bottom and c3.body_bottom < c2.body_bottom:
                patterns.append({"pattern": "three_white_soldiers", "position": i, "bias": "strong_bullish", "strength": 0.8})

            # Three Black Crows
            if all(not c.is_bullish for c in [c1, c2, c3]) and c2.body_top > c1.body_top and c3.body_top > c2.body_top:
                patterns.append({"pattern": "three_black_crows", "position": i, "bias": "strong_bearish", "strength": 0.8})

        return patterns

    @staticmethod
    def full_scan(img: np.ndarray) -> dict:
        """Complete candlestick pattern scan from image."""
        candles = CandleExtractor.extract_candles(img)
        single_patterns = [SingleCandleClassifier.classify(c) for c in candles[-10:]]  # Last 10
        multi_patterns = MultiCandleClassifier.classify_sequence(candles[-10:])
        return {
            "candles_detected": len(candles),
            "last_candle": single_patterns[-1] if single_patterns else None,
            "recent_single_patterns": [p["candle"] for p in single_patterns if p["candle"]["pattern"] != "regular"],
            "multi_candle_patterns": multi_patterns,
            "overall_bias": MultiCandleClassifier._aggregate_bias(single_patterns, multi_patterns),
        }

    @staticmethod
    def _aggregate_bias(singles: list, multis: list) -> dict:
        scores = []
        for p in singles:
            bias = p["candle"]["bias"]
            strength = p["candle"]["strength"]
            if "bullish" in bias: scores.append(strength)
            elif "bearish" in bias: scores.append(-strength)
        for p in multis:
            if "bullish" in p["bias"]: scores.append(p["strength"])
            elif "bearish" in p["bias"]: scores.append(-p["strength"])
        avg = np.mean(scores) if scores else 0
        return {"score": round(avg, 3), "direction": "BULLISH" if avg > 0.2 else "BEARISH" if avg < -0.2 else "NEUTRAL"}
```


---

## Candlestick Statistics Engine

# Candlestick Statistics Engine

```python
CANDLE_STATS = {
    "hammer":            {"bullish_pct": 60, "avg_follow_through": 1.5, "sample_note": "Based on studies of 10+ years of FX data"},
    "shooting_star":     {"bearish_pct": 59, "avg_follow_through": 1.4},
    "bullish_engulfing":  {"bullish_pct": 63, "avg_follow_through": 1.8, "best_at": "support levels"},
    "bearish_engulfing":  {"bearish_pct": 62, "avg_follow_through": 1.7, "best_at": "resistance levels"},
    "morning_star":      {"bullish_pct": 68, "avg_follow_through": 2.2, "note": "High reliability when volume confirms"},
    "evening_star":      {"bearish_pct": 67, "avg_follow_through": 2.1},
    "doji":              {"reversal_pct": 51, "note": "Doji alone is weak — needs context (at key level + trend exhaustion)"},
    "pin_bar":           {"reversal_pct": 65, "avg_follow_through": 1.6, "best_at": "key levels with long wick into liquidity"},
    "three_white_soldiers": {"bullish_pct": 72, "avg_follow_through": 2.5, "note": "Strongest multi-candle bullish pattern"},
    "three_black_crows":    {"bearish_pct": 71, "avg_follow_through": 2.4},
    "marubozu":          {"continuation_pct": 56, "note": "Shows conviction but often follows through only partially"},
    "inside_bar":        {"breakout_follow_pct": 62, "note": "Trade the breakout direction, not the inside bar itself"},
}
class CandleStatsEngine:
    @staticmethod
    def lookup(pattern: str) -> dict:
        return CANDLE_STATS.get(pattern, {"error": f"No stats for {pattern}"})
    @staticmethod
    def all_stats() -> dict:
        return CANDLE_STATS
```


---

## Chart Pattern Recognition Vision

# Chart Pattern Recognition Vision

## Overview
Identifies classical chart patterns from images using price contour extraction, peak/trough
detection on the extracted price curve, and geometric validation of pattern structures.

## Stack
- **OpenCV 4.13** — contour analysis, convex hull, template matching
- **scikit-image 0.26** — ridge detection, peak finding on contours
- **scipy 1.17** — peak finding, curve fitting, geometric analysis

---

## 1. Price Curve Extraction from Image

```python
import cv2
import numpy as np
from scipy.signal import find_peaks, savgol_filter
from scipy.ndimage import gaussian_filter1d

class PriceCurveExtractor:
    """Extract the price curve as a 1D signal from a chart image."""

    @staticmethod
    def extract_price_curve(img: np.ndarray) -> np.ndarray:
        """
        Extract price line from candlestick chart image.
        Uses candle body midpoints as the price curve.
        Returns: 1D array of y-positions (inverted: lower y = higher price).
        """
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, w = img.shape[:2]

        # Combine bullish + bearish candle masks
        green = cv2.inRange(hsv, (35, 30, 30), (85, 255, 255))
        red1 = cv2.inRange(hsv, (0, 30, 30), (15, 255, 255))
        red2 = cv2.inRange(hsv, (165, 30, 30), (180, 255, 255))
        candle_mask = cv2.bitwise_or(green, cv2.bitwise_or(red1, red2))

        # Morphological cleanup
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 5))
        candle_mask = cv2.morphologyEx(candle_mask, cv2.MORPH_CLOSE, kernel, iterations=2)

        # For each column, find the center of candle pixels
        price_curve = np.full(w, np.nan)
        for col in range(w):
            col_pixels = np.where(candle_mask[:, col] > 0)[0]
            if len(col_pixels) > 2:
                price_curve[col] = np.mean(col_pixels)

        # Interpolate NaN gaps
        valid = ~np.isnan(price_curve)
        if np.sum(valid) < 20:
            return np.array([])

        from numpy import interp
        x_valid = np.where(valid)[0]
        price_curve = interp(np.arange(w), x_valid, price_curve[valid])

        # Smooth
        price_curve = savgol_filter(price_curve, window_length=min(21, len(price_curve) // 5 * 2 + 1),
                                     polyorder=3)

        return price_curve

    @staticmethod
    def find_swings(curve: np.ndarray, order: int = 15) -> dict:
        """Find swing highs and lows from the extracted price curve."""
        # Invert because lower y = higher price in image coordinates
        inv_curve = -curve

        peaks, peak_props = find_peaks(inv_curve, distance=order, prominence=np.std(curve) * 0.3)
        troughs, trough_props = find_peaks(curve, distance=order, prominence=np.std(curve) * 0.3)

        return {
            "highs": [{"x": int(p), "y": int(curve[p])} for p in peaks],
            "lows": [{"x": int(t), "y": int(curve[t])} for t in troughs],
            "n_highs": len(peaks),
            "n_lows": len(troughs),
        }
```

---

## 2. Pattern Detectors (Image-Based)

```python
class VisualPatternDetector:
    """Detect chart patterns from extracted price curve and swing points."""

    @staticmethod
    def detect_head_and_shoulders(swings: dict, curve: np.ndarray, img_height: int) -> list[dict]:
        """H&S from image: three swing highs where middle is highest."""
        patterns = []
        highs = swings["highs"]
        if len(highs) < 3:
            return patterns

        for i in range(len(highs) - 2):
            ls, head, rs = highs[i], highs[i+1], highs[i+2]
            # Head must be highest (lowest y value = highest price)
            if head["y"] < ls["y"] and head["y"] < rs["y"]:
                shoulder_diff = abs(ls["y"] - rs["y"]) / img_height
                if shoulder_diff < 0.05:  # Shoulders at similar level
                    neckline_y = max(ls["y"], rs["y"])  # Higher y = lower price
                    height = neckline_y - head["y"]
                    patterns.append({
                        "pattern": "head_and_shoulders",
                        "head": head, "left_shoulder": ls, "right_shoulder": rs,
                        "neckline_y": neckline_y,
                        "height_px": height,
                        "target_y": neckline_y + height,
                        "bias": "BEARISH",
                        "reliability": 0.83,
                        "confidence": round(1 - shoulder_diff / 0.05, 2),
                    })

        # Inverse H&S (from lows)
        lows = swings["lows"]
        if len(lows) >= 3:
            for i in range(len(lows) - 2):
                ls, head, rs = lows[i], lows[i+1], lows[i+2]
                if head["y"] > ls["y"] and head["y"] > rs["y"]:
                    shoulder_diff = abs(ls["y"] - rs["y"]) / img_height
                    if shoulder_diff < 0.05:
                        neckline_y = min(ls["y"], rs["y"])
                        height = head["y"] - neckline_y
                        patterns.append({
                            "pattern": "inverse_head_and_shoulders",
                            "head": head, "left_shoulder": ls, "right_shoulder": rs,
                            "neckline_y": neckline_y,
                            "height_px": height,
                            "bias": "BULLISH",
                            "reliability": 0.83,
                        })
        return patterns

    @staticmethod
    def detect_double_top_bottom(swings: dict, img_height: int, tolerance: float = 0.02) -> list[dict]:
        patterns = []
        highs = swings["highs"]
        lows = swings["lows"]

        for i in range(len(highs) - 1):
            h1, h2 = highs[i], highs[i+1]
            diff = abs(h1["y"] - h2["y"]) / img_height
            if diff < tolerance:
                patterns.append({"pattern": "double_top", "peak1": h1, "peak2": h2,
                                "bias": "BEARISH", "reliability": 0.72})

        for i in range(len(lows) - 1):
            l1, l2 = lows[i], lows[i+1]
            diff = abs(l1["y"] - l2["y"]) / img_height
            if diff < tolerance:
                patterns.append({"pattern": "double_bottom", "trough1": l1, "trough2": l2,
                                "bias": "BULLISH", "reliability": 0.72})
        return patterns

    @staticmethod
    def detect_triangles(swings: dict, curve: np.ndarray) -> list[dict]:
        """Detect converging trendlines forming triangles."""
        patterns = []
        highs = swings["highs"]
        lows = swings["lows"]

        if len(highs) >= 2 and len(lows) >= 2:
            h_slope = (highs[-1]["y"] - highs[0]["y"]) / max(highs[-1]["x"] - highs[0]["x"], 1)
            l_slope = (lows[-1]["y"] - lows[0]["y"]) / max(lows[-1]["x"] - lows[0]["x"], 1)
            # Remember: positive slope in image = price declining

            if abs(h_slope) < 0.05 and l_slope < -0.05:
                patterns.append({"pattern": "ascending_triangle", "bias": "BULLISH", "reliability": 0.73,
                                "h_slope": round(h_slope, 4), "l_slope": round(l_slope, 4)})
            elif abs(l_slope) < 0.05 and h_slope > 0.05:
                patterns.append({"pattern": "descending_triangle", "bias": "BEARISH", "reliability": 0.72,
                                "h_slope": round(h_slope, 4), "l_slope": round(l_slope, 4)})
            elif h_slope > 0.02 and l_slope < -0.02:
                patterns.append({"pattern": "symmetrical_triangle", "bias": "NEUTRAL", "reliability": 0.60})
            elif h_slope < -0.02 and l_slope < -0.02:
                patterns.append({"pattern": "falling_wedge", "bias": "BULLISH", "reliability": 0.68})
            elif h_slope > 0.02 and l_slope > 0.02:
                patterns.append({"pattern": "rising_wedge", "bias": "BEARISH", "reliability": 0.68})
        return patterns

    @staticmethod
    def full_pattern_scan(img: np.ndarray) -> dict:
        """Complete visual pattern recognition pipeline."""
        curve = PriceCurveExtractor.extract_price_curve(img)
        if len(curve) == 0:
            return {"error": "Could not extract price curve from image"}

        h, w = img.shape[:2]
        swings = PriceCurveExtractor.find_swings(curve)

        hs_patterns = VisualPatternDetector.detect_head_and_shoulders(swings, curve, h)
        dt_patterns = VisualPatternDetector.detect_double_top_bottom(swings, h)
        tri_patterns = VisualPatternDetector.detect_triangles(swings, curve)

        all_patterns = hs_patterns + dt_patterns + tri_patterns

        return {
            "swings": swings,
            "patterns_found": len(all_patterns),
            "patterns": sorted(all_patterns, key=lambda p: p.get("reliability", 0), reverse=True),
            "dominant_pattern": all_patterns[0] if all_patterns else None,
            "overall_bias": VisualPatternDetector._aggregate_pattern_bias(all_patterns),
        }

    @staticmethod
    def _aggregate_pattern_bias(patterns: list) -> str:
        if not patterns: return "NO PATTERNS"
        bullish = sum(1 for p in patterns if "BULLISH" in p.get("bias", ""))
        bearish = sum(1 for p in patterns if "BEARISH" in p.get("bias", ""))
        if bullish > bearish: return "BULLISH"
        if bearish > bullish: return "BEARISH"
        return "NEUTRAL"
```


---

## Harmonic Pattern Engine

# Harmonic Pattern Engine

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

HARMONIC_RATIOS = {
    "gartley":    {"XB": (0.618, 0.618), "AC": (0.382, 0.886), "BD": (1.272, 1.618), "XD": (0.786, 0.786)},
    "butterfly":  {"XB": (0.786, 0.786), "AC": (0.382, 0.886), "BD": (1.618, 2.618), "XD": (1.272, 1.618)},
    "bat":        {"XB": (0.382, 0.500), "AC": (0.382, 0.886), "BD": (1.618, 2.618), "XD": (0.886, 0.886)},
    "crab":       {"XB": (0.382, 0.618), "AC": (0.382, 0.886), "BD": (2.240, 3.618), "XD": (1.618, 1.618)},
    "cypher":     {"XB": (0.382, 0.618), "AC": (1.130, 1.414), "BD": (1.272, 2.000), "XD": (0.786, 0.786)},
}

class HarmonicEngine:

    @staticmethod
    def detect_xabcd(df: pd.DataFrame, tolerance: float = 0.05) -> list[dict]:
        """Detect XABCD harmonic patterns from swing points."""
        highs = argrelextrema(df["high"].values, np.greater, order=5)[0]
        lows = argrelextrema(df["low"].values, np.less, order=5)[0]
        swings = []
        for i in highs: swings.append({"idx": i, "price": df["high"].iloc[i], "type": "H"})
        for i in lows: swings.append({"idx": i, "price": df["low"].iloc[i], "type": "L"})
        swings.sort(key=lambda s: s["idx"])

        patterns = []
        for i in range(len(swings) - 4):
            X, A, B, C, D = [swings[j]["price"] for j in range(i, i + 5)]
            XA = abs(A - X)
            if XA == 0: continue
            AB = abs(B - A)
            BC = abs(C - B)
            CD = abs(D - C)
            XB_ratio = AB / XA
            AC_ratio = BC / AB if AB > 0 else 0
            BD_ratio = CD / BC if BC > 0 else 0
            XD_ratio = abs(D - X) / XA

            for name, ratios in HARMONIC_RATIOS.items():
                xb_min, xb_max = ratios["XB"][0] - tolerance, ratios["XB"][1] + tolerance
                xd_min, xd_max = ratios["XD"][0] - tolerance, ratios["XD"][1] + tolerance
                if xb_min <= XB_ratio <= xb_max and xd_min <= XD_ratio <= xd_max:
                    bullish = D < X if swings[i]["type"] == "L" else D > X
                    patterns.append({
                        "pattern": name,
                        "bullish": bullish,
                        "X": round(X, 5), "A": round(A, 5), "B": round(B, 5), "C": round(C, 5), "D": round(D, 5),
                        "XB": round(XB_ratio, 3), "XD": round(XD_ratio, 3),
                        "prz": round(D, 5),
                        "signal": f"{'BUY' if bullish else 'SELL'} at PRZ {round(D, 5)}",
                        "stop": round(X, 5),
                        "tp1": round(D + (A - D) * 0.382, 5) if bullish else round(D - (D - A) * 0.382, 5),
                        "tp2": round(D + (A - D) * 0.618, 5) if bullish else round(D - (D - A) * 0.618, 5),
                    })
        return patterns
```


---

## Elliott Wave Engine

# Elliott Wave Engine

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class ElliottWaveEngine:

    @staticmethod
    def find_waves(df: pd.DataFrame, order: int = 10) -> dict:
        """Attempt to identify Elliott Wave structure from swing points."""
        highs_idx = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows_idx = argrelextrema(df["low"].values, np.less, order=order)[0]
        swings = []
        for i in highs_idx:
            swings.append({"idx": int(i), "price": df["high"].iloc[i], "type": "high", "time": df.index[i]})
        for i in lows_idx:
            swings.append({"idx": int(i), "price": df["low"].iloc[i], "type": "low", "time": df.index[i]})
        swings.sort(key=lambda s: s["idx"])

        # Validate impulse wave rules
        waves = ElliottWaveEngine._classify_impulse(swings)
        return {
            "swings_found": len(swings),
            "waves": waves,
            "current_wave": waves[-1] if waves else None,
            "note": "Elliott Waves are subjective. Multiple valid counts often exist. Use as confluence, not primary signal.",
        }

    @staticmethod
    def _classify_impulse(swings: list) -> list:
        """Check if swing sequence follows 5-wave impulse rules."""
        waves = []
        if len(swings) < 5:
            return [{"wave": "insufficient_data", "swings": len(swings)}]
        for i in range(0, len(swings) - 4, 2):
            s = swings[i:i+5]
            if len(s) < 5: break
            # Basic impulse: up-down-up-down-up (bullish) or reverse
            is_bullish = s[0]["type"] == "low" and s[2]["price"] > s[0]["price"]
            if is_bullish:
                w3_longest = (s[2]["price"] - s[1]["price"]) > (s[0]["price"] if s[0]["type"]=="high" else 0)
                w2_above_w1_start = s[1]["price"] > s[0]["price"]
                waves.append({
                    "type": "impulse_bullish",
                    "wave_1": {"start": round(s[0]["price"], 5), "end": round(s[1]["price"], 5)},
                    "wave_2": {"start": round(s[1]["price"], 5), "end": round(s[2]["price"], 5) if len(s) > 2 else 0},
                    "w2_valid": w2_above_w1_start,
                    "position": i,
                })
        return waves if waves else [{"wave": "no_clear_impulse"}]

    @staticmethod
    def fibonacci_targets(wave_1_start: float, wave_1_end: float, wave_2_end: float) -> dict:
        """Project wave 3 and wave 5 targets using Fibonacci extensions."""
        w1_range = abs(wave_1_end - wave_1_start)
        direction = 1 if wave_1_end > wave_1_start else -1
        return {
            "wave_3_targets": {
                "1.000": round(wave_2_end + direction * w1_range * 1.0, 5),
                "1.618": round(wave_2_end + direction * w1_range * 1.618, 5),
                "2.618": round(wave_2_end + direction * w1_range * 2.618, 5),
            },
            "wave_5_note": "Project from wave 4 end using wave 1 range",
            "invalidation": round(wave_1_start, 5),
        }
```


---

## Trendline Sr Vision

# Trendline & Support/Resistance Vision

## Overview
Computer vision algorithms for detecting trendlines and S/R levels directly from chart images.
Uses Hough line transforms, Line Segment Detector (LSD), horizontal density projection, and
price level clustering. No price data needed — pure image analysis.

## Stack
- **OpenCV 4.13** — HoughLinesP, LSD (ximgproc), edge detection
- **scikit-image 0.26** — probabilistic Hough, peak detection
- **scipy 1.17** — signal peak finding, clustering

---

## 1. Support/Resistance Level Detection

```python
import cv2
import numpy as np
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
from scipy.cluster.hierarchy import fcluster, linkage
from skimage.transform import probabilistic_hough_line
from skimage import feature

class SRDetector:
    """Detect support and resistance levels from chart images."""

    @staticmethod
    def horizontal_projection_sr(img: np.ndarray, n_levels: int = 8) -> list[dict]:
        """
        Project pixel intensity horizontally to find price levels where
        price action clusters (many candle bodies/wicks at same level).
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape

        # Invert if dark theme (candles are bright on dark background)
        if np.mean(gray) < 128:
            gray = 255 - gray

        # Horizontal projection: sum intensity per row
        projection = np.sum(gray.astype(float), axis=1)

        # Smooth to reduce noise
        projection = gaussian_filter1d(projection, sigma=h * 0.01)

        # Find peaks (rows with high pixel density = S/R levels)
        peaks, properties = find_peaks(
            projection,
            height=np.percentile(projection, 75),
            distance=h // (n_levels * 2),
            prominence=np.std(projection) * 0.5,
        )

        # Cluster nearby peaks
        if len(peaks) > n_levels:
            peaks = peaks[np.argsort(properties["peak_heights"])[-n_levels:]]

        levels = []
        for peak in sorted(peaks):
            y_pct = 1 - peak / h  # Invert: top of image = high price
            strength = projection[peak] / projection.max()
            levels.append({
                "y_pixel": int(peak),
                "price_pct": round(y_pct, 4),  # 0=bottom, 1=top of chart
                "strength": round(strength, 3),
                "type": "resistance" if y_pct > 0.5 else "support",
            })

        return sorted(levels, key=lambda l: l["strength"], reverse=True)

    @staticmethod
    def candle_body_clustering_sr(candles: list, n_clusters: int = 6) -> list[dict]:
        """
        Cluster candle body edges (open/close levels) to find natural S/R zones.
        Uses hierarchical clustering on candle geometry from CandleExtractor.
        """
        if not candles or len(candles) < 5:
            return []

        # Collect all body edges (top and bottom of each candle body)
        edges = []
        for c in candles:
            edges.extend([c.body_top, c.body_bottom, c.y_top, c.y_bottom])

        edges = np.array(edges).reshape(-1, 1)

        # Hierarchical clustering
        Z = linkage(edges, method="ward")
        labels = fcluster(Z, t=n_clusters, criterion="maxclust")

        # Compute cluster centers and sizes
        levels = []
        for cluster_id in range(1, n_clusters + 1):
            cluster_edges = edges[labels == cluster_id]
            if len(cluster_edges) < 3:
                continue
            center = np.mean(cluster_edges)
            spread = np.std(cluster_edges)
            levels.append({
                "y_pixel": int(center),
                "zone_width_px": int(spread * 2),
                "touch_count": len(cluster_edges),
                "strength": round(len(cluster_edges) / len(edges), 3),
            })

        return sorted(levels, key=lambda l: l["strength"], reverse=True)
```

---

## 2. Trendline Detection

```python
class TrendlineDetector:
    """Detect trendlines from chart images using line detection algorithms."""

    @staticmethod
    def hough_trendlines(img: np.ndarray, min_length: int = 100, max_gap: int = 10) -> list[dict]:
        """
        Probabilistic Hough Line Transform for trendline detection.
        OpenCV 4.13 HoughLinesP.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)

        # Dilate edges slightly to connect fragmented lines
        edges = cv2.dilate(edges, np.ones((2, 2), np.uint8), iterations=1)

        lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=80,
                                 minLineLength=min_length, maxLineGap=max_gap)
        if lines is None:
            return []

        trendlines = []
        h, w = gray.shape
        for line in lines:
            x1, y1, x2, y2 = line[0]
            angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Filter: trendlines should be roughly diagonal (10-80 degrees)
            # or horizontal (S/R lines, 0-10 degrees)
            abs_angle = abs(angle)
            if abs_angle > 85:  # Vertical lines = not trendlines
                continue

            line_type = TrendlineDetector._classify_line(angle, y1, y2, h)

            trendlines.append({
                "start": (x1, y1), "end": (x2, y2),
                "angle": round(angle, 1),
                "length": round(length, 1),
                "type": line_type,
                "slope": round((y2 - y1) / max(x2 - x1, 1), 4),
            })

        # Merge nearby parallel lines
        trendlines = TrendlineDetector._merge_nearby(trendlines)

        return sorted(trendlines, key=lambda l: l["length"], reverse=True)[:15]

    @staticmethod
    def lsd_trendlines(img: np.ndarray) -> list[dict]:
        """
        Line Segment Detector (LSD) from OpenCV 4.13 ximgproc.
        More accurate than Hough for detecting clean line segments.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Create LSD detector
        lsd = cv2.createLineSegmentDetector(cv2.LSD_REFINE_STD)
        lines, widths, _, _ = lsd.detect(gray)

        if lines is None:
            return []

        trendlines = []
        h, w = gray.shape
        for line, width in zip(lines, widths):
            x1, y1, x2, y2 = line[0]
            angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if length < 50 or abs(angle) > 85:
                continue

            trendlines.append({
                "start": (int(x1), int(y1)), "end": (int(x2), int(y2)),
                "angle": round(angle, 1),
                "length": round(length, 1),
                "width": round(float(width[0]), 1),
                "type": TrendlineDetector._classify_line(angle, y1, y2, h),
            })

        return sorted(trendlines, key=lambda l: l["length"], reverse=True)[:15]

    @staticmethod
    def detect_channels(trendlines: list[dict], tolerance_deg: float = 5) -> list[dict]:
        """Detect parallel trendline pairs forming channels."""
        channels = []
        for i, line_a in enumerate(trendlines):
            for line_b in trendlines[i + 1:]:
                angle_diff = abs(line_a["angle"] - line_b["angle"])
                if angle_diff < tolerance_deg:
                    # Parallel lines — potential channel
                    y_diff = abs(line_a["start"][1] - line_b["start"][1])
                    channels.append({
                        "upper": line_a if line_a["start"][1] < line_b["start"][1] else line_b,
                        "lower": line_b if line_a["start"][1] < line_b["start"][1] else line_a,
                        "width_px": y_diff,
                        "angle": round((line_a["angle"] + line_b["angle"]) / 2, 1),
                        "type": "ascending" if line_a["angle"] < -2 else "descending" if line_a["angle"] > 2 else "horizontal",
                    })
        return channels

    @staticmethod
    def _classify_line(angle: float, y1: int, y2: int, img_height: int) -> str:
        abs_angle = abs(angle)
        if abs_angle < 5:
            return "horizontal_sr"
        elif angle < -5:
            return "uptrend_support" if (y1 + y2) / 2 > img_height * 0.5 else "uptrend_resistance"
        elif angle > 5:
            return "downtrend_resistance" if (y1 + y2) / 2 < img_height * 0.5 else "downtrend_support"
        return "unknown"

    @staticmethod
    def _merge_nearby(lines: list[dict], pixel_threshold: int = 15) -> list[dict]:
        """Merge lines that are very close and parallel."""
        if len(lines) < 2:
            return lines
        merged = [lines[0]]
        for line in lines[1:]:
            is_duplicate = False
            for existing in merged:
                if (abs(line["angle"] - existing["angle"]) < 3 and
                    abs(line["start"][1] - existing["start"][1]) < pixel_threshold):
                    if line["length"] > existing["length"]:
                        merged.remove(existing)
                        merged.append(line)
                    is_duplicate = True
                    break
            if not is_duplicate:
                merged.append(line)
        return merged

    @staticmethod
    def full_analysis(img: np.ndarray) -> dict:
        """Complete trendline and S/R analysis from image."""
        sr_levels = SRDetector.horizontal_projection_sr(img)
        hough_lines = TrendlineDetector.hough_trendlines(img)
        lsd_lines = TrendlineDetector.lsd_trendlines(img)
        channels = TrendlineDetector.detect_channels(hough_lines + lsd_lines)
        return {
            "sr_levels": sr_levels,
            "hough_trendlines": hough_lines,
            "lsd_trendlines": lsd_lines,
            "channels": channels,
            "n_sr_levels": len(sr_levels),
            "n_trendlines": len(hough_lines) + len(lsd_lines),
        }
```

---

## PatternReliability (Enhancement)

Ctrl click to launch VS Code Native REPL

## Candlestick Patterns with SMC Confluence (Smart Risk)
*Source: video_034 — Best Candlestick Signals That Work Every Time*
- **Pin bar + SSL sweep at OB = A+:** Pin bar wick sweeps SSL at OB level then closes above → institutional stop hunt confirmed; enter long; stop below wick tip
- **Bullish engulfing at FVG:** Engulfing candle forms at H1 FVG → confirms zone defended → enter at 50% of engulfing body; stop below engulfing low
- **Inside bar at BOS level:** Inside bar (mother bar range contained) at prior BOS level (now support) → enter on bullish breakout of inside bar; stop below inside bar low
- **Confluence stacking priority:** structural level (OB/FVG/S&D) + Fibonacci 0.618–0.786 + candlestick signal + killzone timing + liquidity sweep = A+ entry; each added layer improves probability
- **Rejection block:** 2-3 candles with wicks in same direction at a level, bodies not closing beyond → institutional defense confirmed → enter after pattern completion
- **Entry discipline:** always wait for candle CLOSE before entering (never anticipate mid-candle); exception: limit order pre-placed at defined zone level

## Chart Patterns with SMC Integration (Smart Risk)
*Source: video_056 — Best Chart Patterns in Price Action Trading*
- **Rising/falling wedge + SMC:** BSL sweep at wedge top (bearish) or SSL sweep at wedge bottom (bullish) = PO3 manipulation phase; break + CHoCH = distribution; measured move = wedge height applied from breakout
- **Double top/bottom = Turtle Soup:** Second high sweeps first high (BSL sweep) → close back below both highs → enter short; second low sweeps first low (SSL sweep) → close back above both lows → enter long; stop beyond sweep wick
- **Triangles = liquidity compression:** Longer compression → larger sweep when breaks; sweep of triangle extreme + CHoCH = entry; measured move (triangle height) applied in breakout direction
- **SMC filter requirement:** Never trade patterns without SMC context (sweep + CHoCH); pattern alone ~50% probability; with SMC filter significantly higher
- **Ascending triangle trap:** False breakdown below ascending trendline → SSL swept → enters long; descending triangle: false breakout above → BSL swept → enter short

## Naked Price Action Signals (Smart Risk)
*Source: video_075 — Top Naked Price Action Signals*
- **Shrinking candles (momentum exhaustion):** 3+ consecutive candles with decreasing body size at a key level (OB/FVG) = institutional absorption; enter after the third shrinking candle closes in the zone direction
- **Momentum candlestick quality rule:** Large-body candle (>70% of total range = body) in one direction = institutional commitment; BOS or FVG created by a momentum candle carries more weight; if a momentum candle closes THROUGH your FVG → expect IFVG formation
- **Inside bar at SMC level:** Inside bar forming AT an OB or FVG = zone being defended; enter on directional breakout of mother bar; stop opposite side of mother bar
- **Fakeout (SMC equivalent of Turtle Soup):** Price breaks obvious level (round number, prior H/L) → reversal candle closes back inside → enter in reversal direction; the more obvious the level, the more likely it's a fakeout
- **Signal stacking rule:** 1 signal ~55%; 2 signals ~65-70%; 3 signals ~75-80%; 4+ = A+ setup; never trade single signals at major structure

---

## Related Skills

- [Technical Analysis](../technical-analysis.md)
- [Price Action Strategies](../price-action.md)
- [Ict Smart Money](../ict-smart-money.md)
- [Chart Vision](../chart-vision.md)


---

## Three-Bar Confirmation Pattern (DLE Framework)

### Direction → Location → Execute

The systematic 3-step entry model for high-probability PA setups:

1. **Direction** — confirm trend on higher timeframe (HH/HL = up, LH/LL = down)
2. **Location** — price must be at a Key Point of Interest (PDH, PDL, swing high/low, OB/FVG)
3. **Execute** — wait for 3-bar confirmation (Lead → Reaction → Confirm)

**Pattern structure:**
- Lead candle: pushes toward the level
- Reaction candle: initial response, weak close (indecision)
- Confirmation candle: closes strongly in reversal direction, breaking reaction candle's high/low

```python
import pandas as pd
import numpy as np

def detect_three_bar_confirmation(df: pd.DataFrame, levels: list[float],
                                   tolerance_atr_mult: float = 0.5) -> list[dict]:
    atr = (df["high"] - df["low"]).rolling(14).mean()
    signals = []
    for level in levels:
        for i in range(2, min(20, len(df))):
            idx = len(df) - i
            if idx < 2: continue
            lead = df.iloc[idx - 2]
            reaction = df.iloc[idx - 1]
            confirm = df.iloc[idx]
            tol = atr.iloc[idx] * tolerance_atr_mult
            if (lead["low"] <= level + tol and lead["close"] < lead["open"]
                and reaction["close"] > level
                and confirm["close"] > reaction["high"] and confirm["close"] > confirm["open"]):
                strength = "STRONG" if confirm["close"] > lead["high"] else "MODERATE"
                signals.append({"type": "bullish_three_bar", "level": level, "idx": idx,
                    "entry": round(confirm["close"], 5),
                    "stop": round(min(lead["low"], reaction["low"]) - atr.iloc[idx] * 0.1, 5),
                    "strength": strength, "signal": f"BUY - three-bar at {level} ({strength})"})
            if (lead["high"] >= level - tol and lead["close"] > lead["open"]
                and reaction["close"] < level
                and confirm["close"] < reaction["low"] and confirm["close"] < confirm["open"]):
                strength = "STRONG" if confirm["close"] < lead["low"] else "MODERATE"
                signals.append({"type": "bearish_three_bar", "level": level, "idx": idx,
                    "entry": round(confirm["close"], 5),
                    "stop": round(max(lead["high"], reaction["high"]) + atr.iloc[idx] * 0.1, 5),
                    "strength": strength, "signal": f"SELL - three-bar at {level} ({strength})"})
    return signals


def get_daily_pois(df_daily: pd.DataFrame) -> dict:
    """Extract PDH, PDL, prev close, swing highs/lows as Points of Interest."""
    if len(df_daily) < 2: return {}
    prev = df_daily.iloc[-2]
    pois = {"pdh": prev["high"], "pdl": prev["low"], "prev_close": prev["close"]}
    from scipy.signal import argrelextrema
    recent = df_daily.tail(20)
    swing_highs = argrelextrema(recent["high"].values, np.greater, order=3)[0]
    swing_lows = argrelextrema(recent["low"].values, np.less, order=3)[0]
    pois["old_highs"] = [round(recent["high"].iloc[h], 5) for h in swing_highs]
    pois["old_lows"] = [round(recent["low"].iloc[l], 5) for l in swing_lows]
    return pois


def gap_fill_bias(open_930: float, prev_close: float, atr_daily: float) -> dict:
    gap = open_930 - prev_close
    gap_pct_atr = abs(gap) / atr_daily
    return {"gap_present": gap_pct_atr > 0.1, "gap_direction": "UP" if gap > 0 else "DOWN",
            "fill_target": prev_close,
            "bias": "Expect price to fill toward prev_close FIRST before trending",
            "note": "Only trade WITH trend after gap fill completes"}
```

## 9:30 AM NY Open Scalp (M5 Only, 9:30–11:00 AM EST)

Mark **before** the open: PDH, PDL, prev_close, pre-market H/L, H1 trend.
Opening Print = first M5 candle closing at 9:35 AM — mark its high/low as primary POI.
Apply 3-bar confirmation at opening print level or PDH/PDL.
Close all positions by 11:00 AM EST regardless.
