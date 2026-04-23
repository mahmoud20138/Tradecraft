---
name: harmonic-pattern-engine
description: >
  Harmonic pattern detection — Gartley, Butterfly, Bat, Crab, Cypher, Shark with Fibonacci
  ratio validation. Use for "harmonic pattern", "Gartley", "Butterfly pattern", "Bat pattern",
  "Crab pattern", "Cypher", "XABCD", "harmonic trading", "Scott Carney", or any harmonic analysis.
  Works with fibonacci-strategy-engine and chart-pattern-scanner.
kind: engine
category: trading/analysis
status: active
tags: [analysis, engine, fibonacci, harmonic, harmonics, pattern, trading]
related_skills: [elliott-wave-engine, fibonacci-harmonic-wave]
---

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
