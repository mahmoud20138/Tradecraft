---
name: volume-analysis
description: "Volume Profile (POC, VAH, VAL, HVN, LVN), Order Flow & Delta analysis, and Wyckoff accumulation/distribution detection with Python engines. Use for volume profile, order flow, delta divergence, Wyckoff, POC level, or any volume-based trading analysis."
kind: analyzer
category: trading/strategies
status: active
tags: [analysis, python, trading, volume]
related_skills: [price-action, xtrading-analyze, capitulation-mean-reversion, mtf-confluence-scorer, poc-bounce-strategy]
---

# Volume Analysis — Profile, Order Flow & Wyckoff

Three complementary methodologies for complete volume-based analysis:
1. **Volume Profile** — Price-level volume distribution (POC, VAH, VAL, HVN, LVN)
2. **Order Flow & Delta** — Cumulative delta, absorption detection, delta divergence
3. **Wyckoff Method** — Accumulation/distribution schematics, spring/upthrust, phase detection

These form a complete picture: _where_ volume transacted (profile), _direction_ of aggressive orders (delta), and _institutional intent_ (Wyckoff).

---

## Section 1: Volume Profile

```python
import pandas as pd
import numpy as np

class VolumeProfile:

    @staticmethod
    def compute(df: pd.DataFrame, n_bins: int = 50) -> dict:
        """Build volume profile: volume distributed across price levels."""
        price_range = df["high"].max() - df["low"].min()
        bin_size = price_range / n_bins
        bins = np.arange(df["low"].min(), df["high"].max() + bin_size, bin_size)
        profile = pd.Series(0.0, index=bins[:-1])

        for _, row in df.iterrows():
            bar_bins = bins[(bins >= row["low"]) & (bins < row["high"])]
            vol_per_bin = row["volume"] / max(len(bar_bins), 1)
            for b in bar_bins:
                if b in profile.index:
                    profile[b] += vol_per_bin

        poc = profile.idxmax()
        total_vol = profile.sum()

        # Value Area: 70% of total volume around POC
        sorted_profile = profile.sort_values(ascending=False)
        va_vol, va_levels = 0, []
        for level, vol in sorted_profile.items():
            va_levels.append(level)
            va_vol += vol
            if va_vol >= total_vol * 0.70:
                break
        vah = max(va_levels)
        val = min(va_levels)

        threshold_high = profile.quantile(0.8)
        threshold_low = profile.quantile(0.2)
        hvn = profile[profile > threshold_high].index.tolist()
        lvn = profile[profile < threshold_low].index.tolist()

        current = df.iloc[-1]["close"]
        return {
            "poc": round(poc, 5),
            "value_area_high": round(vah, 5),
            "value_area_low": round(val, 5),
            "current_vs_va": ("ABOVE VA" if current > vah else "BELOW VA" if current < val else "INSIDE VA"),
            "high_volume_nodes": [round(h, 5) for h in hvn[:5]],
            "low_volume_nodes": [round(l, 5) for l in lvn[:5]],
            "strategy": "Buy at VAL, sell at VAH when inside VA. Breakout trade when outside VA.",
            "poc_acts_as": "Magnet — price tends to return to POC",
            "lvn_acts_as": "Price moves quickly through LVN — fast moves expected",
        }
```

### Volume Profile Key Concepts

| Level | Meaning | Trading Implication |
|-------|---------|-------------------|
| **POC** (Point of Control) | Price with highest traded volume | Strong magnet — price gravitates here |
| **VAH** (Value Area High) | Top of 70% volume zone | Resistance inside VA; breakout target if above |
| **VAL** (Value Area Low) | Bottom of 70% volume zone | Support inside VA; breakout target if below |
| **HVN** (High Volume Node) | Heavy trading concentration | Strong S/R, price slows down here |
| **LVN** (Low Volume Node) | Thin trading, price gap | Price moves rapidly through — fast move zones |

**Strategies:**
- **Inside VA:** Mean reversion — buy VAL, sell VAH, target POC
- **Outside VA:** Breakout — price above VAH targets prior VAH; below VAL targets prior VAL
- **POC retest:** High-probability entry — POC acts as magnet after breakouts

---

## Section 2: Order Flow & Delta Analysis

Cumulative delta measures aggressive buying vs. selling pressure. Delta divergence with price reveals absorption and exhaustion.

```python
import pandas as pd
import numpy as np

class OrderFlowDelta:

    @staticmethod
    def compute_delta(df: pd.DataFrame) -> pd.DataFrame:
        """Approximate delta from OHLCV (true delta requires tick data)."""
        df = df.copy()
        df["bar_delta"] = np.where(
            df["close"] > df["open"],
            df["volume"] * ((df["close"] - df["low"]) / (df["high"] - df["low"] + 1e-10)),
            -df["volume"] * ((df["high"] - df["close"]) / (df["high"] - df["low"] + 1e-10)),
        )
        df["cumulative_delta"] = df["bar_delta"].cumsum()
        return df

    @staticmethod
    def delta_divergence(df: pd.DataFrame) -> dict:
        """
        Price new high + delta NOT new high = distribution (bearish).
        Price new low + delta NOT new low = accumulation (bullish).
        """
        df = OrderFlowDelta.compute_delta(df)
        price_new_high = df["high"].iloc[-1] >= df["high"].tail(20).max()
        delta_new_high = df["cumulative_delta"].iloc[-1] >= df["cumulative_delta"].tail(20).max()
        price_new_low = df["low"].iloc[-1] <= df["low"].tail(20).min()
        delta_new_low = df["cumulative_delta"].iloc[-1] <= df["cumulative_delta"].tail(20).min()

        if price_new_high and not delta_new_high:
            return {"divergence": "BEARISH — price high but delta weak (distribution)", "signal": "SELL",
                    "interpretation": "Aggressive sellers overwhelming price push — expect reversal"}
        if price_new_low and not delta_new_low:
            return {"divergence": "BULLISH — price low but delta strong (accumulation)", "signal": "BUY",
                    "interpretation": "Aggressive buyers absorbing price decline — expect reversal"}
        return {"divergence": "NONE", "signal": "NO DIVERGENCE",
                "delta_trend": "bullish" if df["bar_delta"].tail(10).mean() > 0 else "bearish"}

    @staticmethod
    def absorption_detection(df: pd.DataFrame) -> dict:
        """High volume + small range = absorption. Large player absorbing — precedes reversal."""
        df = df.copy()
        df["range"] = df["high"] - df["low"]
        df["vol_range_ratio"] = df["volume"] / (df["range"].replace(0, np.nan) * 10000)
        last = df.iloc[-1]
        avg_ratio = df["vol_range_ratio"].tail(50).mean()
        absorbing = last["vol_range_ratio"] > 2 * avg_ratio
        return {
            "absorption_detected": absorbing,
            "vol_range_ratio": round(last["vol_range_ratio"], 1),
            "avg_ratio": round(avg_ratio, 1),
            "interpretation": ("LARGE PLAYER ABSORBING — expect reversal or breakout" if absorbing else "Normal flow"),
        }

    @staticmethod
    def full_order_flow_analysis(df: pd.DataFrame) -> dict:
        df_delta = OrderFlowDelta.compute_delta(df)
        divergence = OrderFlowDelta.delta_divergence(df)
        absorption = OrderFlowDelta.absorption_detection(df)
        last_delta = df_delta["bar_delta"].tail(5).mean()
        cum_delta = df_delta["cumulative_delta"].iloc[-1]
        return {
            "current_bar_delta": round(df_delta["bar_delta"].iloc[-1], 0),
            "cumulative_delta": round(cum_delta, 0),
            "recent_delta_trend": "BULLISH" if last_delta > 0 else "BEARISH",
            "divergence_signal": divergence,
            "absorption_signal": absorption,
            "overall_signal": (divergence["signal"] if divergence["signal"] != "NO DIVERGENCE"
                               else ("BUY" if last_delta > 0 else "SELL")),
        }
```

### Delta Interpretation Guide

| Condition | Signal | Meaning |
|-----------|--------|---------|
| Price new high + Delta new high | Bullish continuation | Genuine buying pressure |
| Price new high + Delta NOT new high | **Bearish divergence** | Distribution — sellers absorbing |
| Price new low + Delta new low | Bearish continuation | Genuine selling pressure |
| Price new low + Delta NOT new low | **Bullish divergence** | Accumulation — buyers absorbing |
| High volume + tiny range | **Absorption** | Large player absorbing — imminent move |
| Cumulative delta rising + price flat | Bullish — breakout imminent | Buying absorbed, ready to rip |

---

## Section 3: Wyckoff Method

Detect accumulation/distribution phases, spring/upthrust events, and composite man footprints.

```python
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

class WyckoffEngine:

    @staticmethod
    def detect_phases(df: pd.DataFrame, order: int = 7) -> dict:
        close = df["close"]
        vol = df["volume"]
        atr = (df["high"] - df["low"]).rolling(14).mean()
        highs = argrelextrema(df["high"].values, np.greater, order=order)[0]
        lows = argrelextrema(df["low"].values, np.less, order=order)[0]
        events = []

        # Selling Climax (SC): sharp drop on very high volume, then bounce
        for i in range(20, len(df)):
            bar_range = df.iloc[i]["high"] - df.iloc[i]["low"]
            if (close.iloc[i] < close.iloc[i-1] and
                    bar_range > 2.5 * atr.iloc[i] and
                    vol.iloc[i] > vol.rolling(20).mean().iloc[i] * 2.5):
                if i + 3 < len(df):
                    recovery = close.iloc[i+1:i+4].max() - close.iloc[i]
                    if recovery > bar_range * 0.5:
                        events.append({"type": "selling_climax", "idx": i, "time": df.index[i],
                                       "price": round(close.iloc[i], 5),
                                       "volume_ratio": round(vol.iloc[i] / vol.rolling(20).mean().iloc[i], 1)})

        # Buying Climax (BC): sharp rally on very high volume, then pullback
        for i in range(20, len(df)):
            bar_range = df.iloc[i]["high"] - df.iloc[i]["low"]
            if (close.iloc[i] > close.iloc[i-1] and
                    bar_range > 2.5 * atr.iloc[i] and
                    vol.iloc[i] > vol.rolling(20).mean().iloc[i] * 2.5):
                if i + 3 < len(df):
                    pullback = close.iloc[i] - close.iloc[i+1:i+4].min()
                    if pullback > bar_range * 0.5:
                        events.append({"type": "buying_climax", "idx": i, "time": df.index[i],
                                       "price": round(close.iloc[i], 5)})

        # Spring: price dips below support then quickly recovers (bullish)
        if len(lows) >= 2:
            range_low = min(df["low"].iloc[lows[-2]], df["low"].iloc[lows[-1]])
            recent = df.tail(20)
            spring_bars = recent[recent["low"] < range_low]
            if not spring_bars.empty:
                for idx in spring_bars.index:
                    bar = df.loc[idx]
                    if bar["close"] > range_low:
                        events.append({"type": "spring", "time": idx, "price": round(bar["low"], 5),
                                       "signal": "BULLISH — spring below support with recovery"})

        # Upthrust: price spikes above resistance then fails (bearish)
        if len(highs) >= 2:
            range_high = max(df["high"].iloc[highs[-2]], df["high"].iloc[highs[-1]])
            recent = df.tail(20)
            upthrust_bars = recent[recent["high"] > range_high]
            if not upthrust_bars.empty:
                for idx in upthrust_bars.index:
                    bar = df.loc[idx]
                    if bar["close"] < range_high:
                        events.append({"type": "upthrust", "time": idx, "price": round(bar["high"], 5),
                                       "signal": "BEARISH — upthrust above resistance with failure"})

        vol_declining = False
        if len(df) > 40:
            vol_early = vol.iloc[-40:-20].mean()
            vol_late = vol.iloc[-20:].mean()
            vol_declining = vol_late < vol_early * 0.7

        phase = WyckoffEngine._classify_phase(events, df)
        return {
            "events": events[-10:], "current_phase": phase,
            "volume_declining_in_range": vol_declining,
            "interpretation": WyckoffEngine._interpret(phase),
        }

    @staticmethod
    def _classify_phase(events: list, df: pd.DataFrame) -> str:
        if not events: return "NO CLEAR WYCKOFF STRUCTURE"
        last = events[-1]["type"]
        if last == "selling_climax": return "PHASE_A_ACCUMULATION — selling climax occurred"
        if last == "spring":         return "PHASE_C_ACCUMULATION — spring detected, look for SOS"
        if last == "buying_climax":  return "PHASE_A_DISTRIBUTION — buying climax occurred"
        if last == "upthrust":       return "PHASE_C_DISTRIBUTION — upthrust detected, look for SOW"
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

### Wyckoff Schematics Reference

#### Accumulation Schematic
```
Phase A: Selling Climax (SC) → Automatic Rally (AR) → Secondary Test (ST)
Phase B: Range development — building cause (BC), volume declining
Phase C: Spring — shakeout below support, then recovery above
Phase D: Sign of Strength (SOS) — strong breakout above trading range
Phase E: Markup — sustained uptrend begins
```

#### Distribution Schematic
```
Phase A: Buying Climax (BC) → Automatic Reaction (AR) → Secondary Test (ST)
Phase B: Range development — distribution to retail, volume declining
Phase C: Upthrust After Distribution (UTAD) — fake breakout above resistance
Phase D: Sign of Weakness (SOW) — breaks below range
Phase E: Markdown — sustained downtrend begins
```

### Wyckoff Event Glossary

| Event | Abbrev | Phase | Signal |
|-------|--------|-------|--------|
| Selling Climax | SC | A (Acc) | Panic selling ends — start of range |
| Automatic Rally | AR | A (Acc) | Bounce off SC — sets range top |
| Secondary Test | ST | A/B | Retest of SC on lower volume |
| Spring | SPR | C (Acc) | Shakeout below range low — ENTRY |
| Sign of Strength | SOS | D (Acc) | Breakout above range — confirm |
| Buying Climax | BC | A (Dist) | Euphoria top — start of distribution |
| Automatic Reaction | AR | A (Dist) | Drop off BC — sets range bottom |
| Upthrust | UT | C (Dist) | Fake breakout above range — SHORT |
| Sign of Weakness | SOW | D (Dist) | Break below range — confirm |

---

## Combined Volume Analysis

```python
def full_volume_analysis(df: pd.DataFrame) -> dict:
    """Run all three volume analysis methods and synthesize a unified signal."""
    profile = VolumeProfile.compute(df)
    order_flow = OrderFlowDelta.full_order_flow_analysis(df)
    wyckoff = WyckoffEngine.detect_phases(df)

    signals = []
    if order_flow["divergence_signal"]["signal"] != "NO DIVERGENCE":
        signals.append(order_flow["divergence_signal"]["signal"])
    if order_flow["absorption_signal"]["absorption_detected"]:
        signals.append("WATCH")
    if "SPRING" in wyckoff["current_phase"].upper():
        signals.append("BUY")
    if "UPTHRUST" in wyckoff["current_phase"].upper():
        signals.append("SELL")

    buy_count = signals.count("BUY")
    sell_count = signals.count("SELL")
    net_signal = "BUY" if buy_count > sell_count else "SELL" if sell_count > buy_count else "NEUTRAL"

    return {
        "volume_profile": profile, "order_flow": order_flow, "wyckoff": wyckoff,
        "synthesized_signal": {
            "direction": net_signal, "buy_factors": buy_count, "sell_factors": sell_count,
            "key_level": profile["poc"],
            "value_area": f"{profile['value_area_low']} – {profile['value_area_high']}",
            "phase": wyckoff["current_phase"],
        },
    }
```

## Usage Decision Guide

| Question | Tool |
|----------|------|
| Where is the most traded price level? | `VolumeProfile.compute()` → POC |
| Is price inside or outside fair value? | `VolumeProfile.compute()` → current_vs_va |
| Where will price stall vs. fly? | HVN (stall) vs. LVN (fast move) |
| Are buyers or sellers more aggressive? | `OrderFlowDelta.compute_delta()` |
| Is price moving on genuine pressure? | `OrderFlowDelta.delta_divergence()` |
| Is a large player absorbing orders? | `OrderFlowDelta.absorption_detection()` |
| Are we in accumulation or distribution? | `WyckoffEngine.detect_phases()` |
| Is this a spring (high conviction buy)? | Events → spring type |
| Is this an upthrust (high conviction sell)? | Events → upthrust type |
| Full picture — all three combined | `full_volume_analysis()` |
