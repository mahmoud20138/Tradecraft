---
name: elliott-wave-engine
description: >
  Elliott Wave counting and forecasting — impulse waves, corrective patterns, wave degree.
  Use for "Elliott Wave", "wave count", "impulse wave", "corrective wave", "wave 3", "wave 5",
  "ABC correction", "wave analysis", "Fibonacci wave", "wave degree", or any Elliott Wave analysis.
  Works with fibonacci-strategy-engine for price targets and chart-pattern-scanner.
kind: engine
category: trading/analysis
status: active
tags: [analysis, elliott, elliott-wave, engine, fibonacci, trading, wave]
related_skills: [fibonacci-harmonic-wave, harmonic-pattern-engine]
---

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
