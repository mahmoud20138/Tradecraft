---
name: fibonacci-harmonic-wave
description: "Fibonacci retracement/extension levels, harmonic pattern detection (Gartley, Butterfly, Bat, Crab, Cypher, Shark), and Elliott Wave counting with Python engines. Use for Fibonacci levels, harmonic pattern, Elliott Wave, wave count, XABCD pattern, or any combined Fibonacci/harmonic/wave analysis."
kind: reference
category: trading/analysis
status: active
tags: [analysis, elliott-wave, fibonacci, harmonic, harmonics, python, trading, wave]
related_skills: [elliott-wave-engine, harmonic-pattern-engine]
---

# Fibonacci, Harmonic Patterns & Elliott Wave Engine

---

## Section 1: Fibonacci Analysis

### Core Fibonacci Levels Reference

```
RETRACEMENT LEVELS:
  23.6% → Minor support/resistance (weak)
  38.2% → Moderate pullback level
  50.0% → Psychological midpoint (widely watched, not true Fibonacci)
  61.8% → "Golden Ratio" — MOST IMPORTANT level
  78.6% → Deep retracement (= √0.618)
  88.6% → Very deep (= √0.786); used in harmonic patterns

EXTENSION LEVELS (profit targets):
  127.2% = 1st extension (= √1.272)
  138.2%
  161.8% = Most common major target
  200.0% = Double the prior move
  261.8% = Strong extension target

Entry Strategy:
  Conservative: Wait for price to react at level + candle confirmation
  Aggressive: Enter directly at level with tight stop

Stop Loss: Just beyond next Fibonacci level (e.g., short at 61.8%, stop above 78.6%)

Extensions — How to Draw:
  Uptrend: From swing low (A) to swing high (B) to retracement low (C)
  Target = C + (A to B distance × extension %)
```

### Fibonacci Time Zones
```
After swing high or low, count forward:
Bars 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
→ Significant reactions likely at these time intervals
```

---

### Fibonacci Strategy Engine (Code)

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

FIB_LEVELS = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
FIB_EXTENSIONS = [1.0, 1.272, 1.414, 1.618, 2.0, 2.618]

class FibonacciEngine:

    @staticmethod
    def retracement(swing_high: float, swing_low: float, direction: str = "up") -> dict:
        diff = swing_high - swing_low
        levels = {}
        for fib in FIB_LEVELS:
            if direction == "up":
                levels[f"{fib:.3f}"] = round(swing_high - fib * diff, 5)
            else:
                levels[f"{fib:.3f}"] = round(swing_low + fib * diff, 5)
        return {
            "direction": direction, "swing_high": swing_high, "swing_low": swing_low,
            "levels": levels,
            "golden_zone": f"{levels['0.618']} — {levels['0.786']}",
            "strategy": "Buy at 0.618-0.786 in uptrend, sell at 0.618-0.786 in downtrend",
        }

    @staticmethod
    def extension(point_a: float, point_b: float, point_c: float) -> dict:
        diff = abs(point_b - point_a)
        direction = 1 if point_b > point_a else -1
        levels = {}
        for ext in FIB_EXTENSIONS:
            levels[f"{ext:.3f}"] = round(point_c + direction * diff * ext, 5)
        return {"extensions": levels, "primary_target": levels["1.618"]}

    @staticmethod
    def auto_fib(df: pd.DataFrame, order: int = 10) -> dict:
        """Automatically detect last major swing and compute fibs."""
        highs = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows = argrelextrema(df["low"].values, np.less, order=order)[0]
        if len(highs) == 0 or len(lows) == 0:
            return {"error": "No swings found"}
        last_high = df["high"].iloc[highs[-1]]
        last_low = df["low"].iloc[lows[-1]]
        direction = "up" if lows[-1] < highs[-1] else "down"
        return FibonacciEngine.retracement(last_high, last_low, direction)

    @staticmethod
    def cluster_zones(fibs_list: list, tolerance: float = 0.0005) -> list:
        """Find confluence zones where multiple fib levels cluster together."""
        all_levels = []
        for fib_set in fibs_list:
            for level_name, price in fib_set.get("levels", {}).items():
                all_levels.append(price)
        all_levels.sort()
        clusters = []
        i = 0
        while i < len(all_levels):
            cluster = [all_levels[i]]
            while i + 1 < len(all_levels) and all_levels[i + 1] - all_levels[i] < tolerance:
                i += 1
                cluster.append(all_levels[i])
            if len(cluster) >= 2:
                clusters.append({
                    "zone_center": round(np.mean(cluster), 5),
                    "zone_width": round(max(cluster) - min(cluster), 5),
                    "n_fibs_confluent": len(cluster),
                    "strength": "STRONG" if len(cluster) >= 3 else "MODERATE",
                })
            i += 1
        return sorted(clusters, key=lambda c: c["n_fibs_confluent"], reverse=True)
```

---

## Section 2: Harmonic Patterns

### Harmonic Pattern Reference Table

| Pattern | XB Ratio | AC Ratio | BD Ratio | XD Ratio (PRZ) | Reliability |
|---------|----------|----------|----------|-----------------|-------------|
| **Gartley** | 0.618 | 0.382–0.886 | 1.272–1.618 | **0.786** | 65–70% |
| **Butterfly** | 0.786 | 0.382–0.886 | 1.618–2.618 | **1.272–1.618** | 70–75% |
| **Bat** | 0.382–0.500 | 0.382–0.886 | 1.618–2.618 | **0.886** | 72–78% |
| **Crab** | 0.382–0.618 | 0.382–0.886 | 2.240–3.618 | **1.618** | 65–70% |
| **Cypher** | 0.382–0.618 | 1.130–1.414 | 1.272–2.000 | **0.786** | 70–75% |
| **Shark** | any | 1.130 ext | 0.886 | **0.886 of 0X** | 60–65% |

### ABCD Pattern
```
AB = CD (time and price symmetry)
BC: 61.8% or 78.6% of AB
CD: 127.2% or 161.8% of BC

Bullish ABCD: Buy at D | Bearish ABCD: Sell at D
Stop: Beyond D by structure | Target: B level (38.2% and 61.8% of AD)
```

### Gartley
```
XA: Initial move | AB: 61.8% retrace of XA
BC: 38.2–88.6% retrace of AB | CD: 78.6% retrace of XA (PRZ)
Bullish: Buy at D (78.6% of XA) | Stop: Below X
Target 1: 61.8% of CD | Target 2: 127.2% of CD
```

### Butterfly
```
AB: 78.6% retrace of XA
CD: 127.2% OR 161.8% extension of XA (beyond X — D extends past X)
PRZ: 127.2–161.8% of XA | Reliability: 70–75%
```

### Bat
```
AB: 38.2–50% retrace of XA (key differentiator from Gartley)
CD: 88.6% retrace of XA (PRZ) | Reliability: 72–78% | Tighter stops
```

### Crab
```
AB: 38.2–61.8% retrace of XA
CD: 161.8% extension of XA (deepest extension) | PRZ: 161.8% of XA
Reliability: 65–70% | Use tight stops
```

### Cypher
```
AB: 38.2–61.8% retrace of XA
BC: 127.2–141.4% extension of XA
CD: 78.6% retrace of XC (PRZ) | Reliability: 70–75%
```

### Harmonic Pattern Trading Rules
```
Entry: At PRZ (Potential Reversal Zone)
Confirmation: Wait for reversal candle at PRZ
Stop: Beyond the extreme of pattern (D or X)
Target 1: 38.2% retrace of CD
Target 2: 61.8% retrace of CD
Target 3: Full retracement to AB or beyond
Risk: 1–1.5% per harmonic trade | Best timeframes: 1H, 4H, Daily
```

---

### Harmonic Pattern Engine (Code)

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

HARMONIC_RATIOS = {
    "gartley":   {"XB": (0.618, 0.618), "AC": (0.382, 0.886), "BD": (1.272, 1.618), "XD": (0.786, 0.786)},
    "butterfly": {"XB": (0.786, 0.786), "AC": (0.382, 0.886), "BD": (1.618, 2.618), "XD": (1.272, 1.618)},
    "bat":       {"XB": (0.382, 0.500), "AC": (0.382, 0.886), "BD": (1.618, 2.618), "XD": (0.886, 0.886)},
    "crab":      {"XB": (0.382, 0.618), "AC": (0.382, 0.886), "BD": (2.240, 3.618), "XD": (1.618, 1.618)},
    "cypher":    {"XB": (0.382, 0.618), "AC": (1.130, 1.414), "BD": (1.272, 2.000), "XD": (0.786, 0.786)},
}

class HarmonicEngine:

    @staticmethod
    def detect_xabcd(df: pd.DataFrame, tolerance: float = 0.05) -> list:
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
            XD_ratio = abs(D - X) / XA

            for name, ratios in HARMONIC_RATIOS.items():
                xb_min, xb_max = ratios["XB"][0] - tolerance, ratios["XB"][1] + tolerance
                xd_min, xd_max = ratios["XD"][0] - tolerance, ratios["XD"][1] + tolerance
                if xb_min <= XB_ratio <= xb_max and xd_min <= XD_ratio <= xd_max:
                    bullish = D < X if swings[i]["type"] == "L" else D > X
                    patterns.append({
                        "pattern": name, "bullish": bullish,
                        "X": round(X, 5), "A": round(A, 5), "B": round(B, 5),
                        "C": round(C, 5), "D": round(D, 5),
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

## Section 3: Elliott Wave Theory

### Elliott Wave Rules (MUST be satisfied)
```
5-wave Impulse:
  Rule 1: Wave 2 NEVER retraces more than 100% of Wave 1
  Rule 2: Wave 3 is NEVER the shortest impulse wave
  Rule 3: Wave 4 NEVER overlaps into Wave 1 price territory
           (Exception: Diagonal triangles in Wave 1 or 5)
```

### Elliott Wave Guidelines
```
Wave 1: Often muted; not widely recognized
Wave 2: Typically 50–61.8% retracement of Wave 1
Wave 3: Longest and strongest; 161.8% of Wave 1 common
Wave 4: Typically 38.2% retracement of Wave 3
Wave 5: Often equals Wave 1 in length; or 61.8% of W1+W3

Corrective Waves (A-B-C):
  Zigzag: Sharp correction (5-3-5)
  Flat: Sideways correction (3-3-5)
  Triangle: Converging correction (3-3-3-3-3)
```

### Fibonacci Relationships in Elliott

| Wave | Typical Fibonacci Relationship |
|------|-------------------------------|
| Wave 2 | 50%, 61.8% retrace of Wave 1 |
| Wave 3 | 161.8%, 261.8% of Wave 1 |
| Wave 4 | 38.2% retrace of Wave 3 |
| Wave 5 | 61.8% or 100% of Wave 1 |
| Wave A | 100% of Wave 5 often |
| Wave B | 50–78.6% retrace of Wave A |
| Wave C | 100%, 161.8% of Wave A |

### Wave Degrees
```
Grand Supercycle → Supercycle → Cycle → Primary → Intermediate
→ Minor → Minute → Minuette → Sub-Minuette

Each degree contains 5-wave impulse + 3-wave correction nested fractally.
Trade in direction of at least 2 higher-degree waves for highest probability.
```

---

### Elliott Wave Engine (Code)

```python
import pandas as pd, numpy as np
from scipy.signal import argrelextrema

class ElliottWaveEngine:

    @staticmethod
    def find_waves(df: pd.DataFrame, order: int = 10) -> dict:
        highs_idx = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows_idx = argrelextrema(df["low"].values, np.less, order=order)[0]
        swings = []
        for i in highs_idx:
            swings.append({"idx": int(i), "price": df["high"].iloc[i], "type": "high", "time": df.index[i]})
        for i in lows_idx:
            swings.append({"idx": int(i), "price": df["low"].iloc[i], "type": "low", "time": df.index[i]})
        swings.sort(key=lambda s: s["idx"])
        waves = ElliottWaveEngine._classify_impulse(swings)
        return {
            "swings_found": len(swings), "waves": waves,
            "current_wave": waves[-1] if waves else None,
            "note": "Elliott Waves are subjective. Use as confluence, not primary signal.",
        }

    @staticmethod
    def _classify_impulse(swings: list) -> list:
        waves = []
        if len(swings) < 5:
            return [{"wave": "insufficient_data", "swings": len(swings)}]
        for i in range(0, len(swings) - 4, 2):
            s = swings[i:i+5]
            if len(s) < 5: break
            is_bullish = s[0]["type"] == "low" and s[2]["price"] > s[0]["price"]
            if is_bullish:
                w2_above_w1_start = s[1]["price"] > s[0]["price"]
                waves.append({
                    "type": "impulse_bullish",
                    "wave_1": {"start": round(s[0]["price"], 5), "end": round(s[1]["price"], 5)},
                    "wave_2": {"start": round(s[1]["price"], 5), "end": round(s[2]["price"], 5) if len(s) > 2 else 0},
                    "w2_valid": w2_above_w1_start, "position": i,
                })
        return waves if waves else [{"wave": "no_clear_impulse"}]

    @staticmethod
    def fibonacci_targets(wave_1_start: float, wave_1_end: float, wave_2_end: float) -> dict:
        w1_range = abs(wave_1_end - wave_1_start)
        direction = 1 if wave_1_end > wave_1_start else -1
        return {
            "wave_3_targets": {
                "1.000": round(wave_2_end + direction * w1_range * 1.0, 5),
                "1.618": round(wave_2_end + direction * w1_range * 1.618, 5),
                "2.618": round(wave_2_end + direction * w1_range * 2.618, 5),
            },
            "invalidation": round(wave_1_start, 5),
        }
```

---

## Section 4: Combined Workflow

### How to Use All Three Together
```
Step 1 — FIBONACCI: Run auto_fib() to identify key retracement/extension levels
Step 2 — HARMONICS: Run detect_xabcd() to find XABCD patterns forming at fib levels
Step 3 — ELLIOTT: Run find_waves() to confirm wave position and project next wave target
Step 4 — CONFLUENCE: Use cluster_zones() to find where all three methods agree

High-probability setup:
  → Price at Fibonacci golden zone (61.8–78.6%)
  → Harmonic PRZ at same level
  → Elliott Wave 2 or Wave 4 retracement landing there
  → Confirmed by reversal candle
```

### Confluence Scoring

| Signal | Score |
|--------|-------|
| Fibonacci 61.8% level | +1 |
| Fibonacci 78.6% level | +1 |
| Fib cluster (3+ levels converging) | +2 |
| Harmonic PRZ match | +2 |
| Elliott Wave retrace landing zone | +1 |
| Multiple pattern type agreement | +2 |
| Reversal candle at zone | +1 |
| **Total ≥ 6 → High-confidence entry** | |
