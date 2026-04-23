---
name: gap-trading-strategy
description: >
  Gap trading — opening gaps, gap fill probability, gap-and-go, fade the gap. Use for "gap
  trading", "opening gap", "gap fill", "gap and go", "fade the gap", "Sunday gap", "weekend gap",
  "gap statistics", "gap probability", or any gap-based trading. Works with session-profiler.
kind: strategy
category: trading/strategies
status: active
tags: [gap, strategies, strategy, trading]
related_skills: [jdub-price-action-strategy, session-scalping, asian-session-scalper, grid-trading-engine, session-profiler]
---

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
