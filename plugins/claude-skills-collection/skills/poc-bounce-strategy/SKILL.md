---
name: poc-bounce-strategy
description: >
  Complete Volume Profile POC (Point of Control) bounce trading strategy with level detection,
  confluence scoring, multi-timeframe analysis, and trade management. Use whenever the user asks
  about "POC bounce", "point of control", "volume profile strategy", "volume profile levels",
  "POC trading", "naked POC", "virgin POC", "value area bounce", "VAH VAL", "HVN LVN",
  "volume nodes", "session POC", "profile shape", "80% rule", "value area fill",
  "where did institutions trade", "fair value volume", "volume-based support resistance",
  "POC as support", "POC magnet", "developing POC", "POC cluster", "mini-POC",
  "volume profile XAUUSD", "volume profile gold", "volume profile forex",
  "volume profile futures", "session volume profile", "fixed range volume profile",
  or any request involving volume profile analysis, POC-based entries, or institutional
  volume level detection. Also trigger when user asks "where should I enter based on volume",
  "what levels matter today", "where are institutions positioned", or wants to identify
  high-probability bounce levels from volume data. Works with multi-tf-order-block-mapper,
  currency-strength-meter, cross-timeframe-divergence-scanner, candlestick-statistics-engine,
  automated-strategy-builder, correlation-heatmap-visualizer, and mq5-mq4-how-to-work-with.
kind: strategy
category: trading/strategies
status: active
tags: [bounce, correlation, forex, poc, strategies, strategy, trading]
related_skills: [price-action, xtrading-analyze, capitulation-mean-reversion, mtf-confluence-scorer, smc-python-library]
---

# POC Bounce Strategy

Complete institutional-grade volume profile trading system. Trades bounces off recent session
POC levels where institutions accumulated positions. Applicable to any instrument/timeframe,
optimized for XAUUSD H1/H4 and intraday futures M5–M30.

## When This Skill Triggers

- "POC bounce" / "trade the POC" / "volume profile strategy"
- "Where are the volume levels?" / "Key levels from volume"
- "Naked POC" / "Virgin POC" / "untested POC"
- "Value area strategy" / "VAH VAL bounce" / "80% rule"
- "Where did institutions trade?" / "Fair value zone"
- "Volume profile on gold/forex/ES/NQ"
- "What levels should I watch today?"
- Any request for volume-based support/resistance identification
- Any request to analyze, detect, or trade POC levels

## Quick Reference — For detailed rules, read `references/full-strategy-rules.md`

## Architecture

```
User Query
    │
    ├─[1] DETECT LEVELS → POCDetector
    │     ├── Session POCs (daily/weekly/monthly)
    │     ├── Naked POC filter
    │     ├── POC Cluster detection
    │     └── Value Area boundaries (VAH/VAL)
    │
    ├─[2] CLASSIFY REGIME → RegimeClassifier
    │     ├── Balanced (D-shape) → Optimal for bounces
    │     ├── Trending (P/b-shape) → Trend-direction only
    │     └── Breakout/Discovery → Skip bounces
    │
    ├─[3] SCORE SETUP → ConfluenceScorer
    │     └── 10-point scoring system (min 5 to trade)
    │
    ├─[4] CONFIRM ENTRY → BounceConfirmation
    │     ├── Rejection candle (wick/body ≥ 1.5)
    │     ├── RSI confirmation
    │     ├── Volume spike check
    │     └── Trend alignment
    │
    ├─[5] EXECUTE TRADE → TradeManager
    │     ├── ATR-based SL/TP/sizing
    │     ├── Trailing stop behind developing POC
    │     └── Partial exit at primary target
    │
    └─[6] ROUTE TO SKILLS → SkillRouter
          └── Recommend linked skills for deeper analysis
```

## Core Engine

```python
import pandas as pd, numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Tuple
from enum import Enum

# ============================================================
# DATA STRUCTURES
# ============================================================
class Regime(Enum):
    BALANCED = "balanced"      # D-shape, optimal for bounces
    TRENDING_UP = "trending_up"  # P-shape, long bounces only
    TRENDING_DN = "trending_dn"  # b-shape, short bounces only
    BREAKOUT = "breakout"      # Skip all bounce setups

class BounceDirection(Enum):
    LONG = "long"
    SHORT = "short"

@dataclass
class POCLevel:
    price: float
    zone_high: float          # POC + 0.3×ATR
    zone_low: float           # POC - 0.3×ATR
    volume: float             # Total volume at POC bin
    timeframe: str            # "D1", "W1", "MN1", "session"
    session_date: str         # When this POC was created
    is_naked: bool = True     # Never retested = True
    is_cluster: bool = False  # Part of multi-POC cluster
    cluster_strength: int = 1 # Number of POCs in cluster
    tested_count: int = 0     # 0 = virgin, 1 = tested once

@dataclass
class ValueArea:
    vah: float                # Value Area High (70% boundary)
    val: float                # Value Area Low (70% boundary)
    poc: float                # Point of Control
    total_volume: float
    timeframe: str
    session_date: str

@dataclass
class TradeSetup:
    direction: BounceDirection
    poc_level: POCLevel
    entry_price: float
    stop_loss: float
    take_profit_1: float      # Primary: next HVN/POC
    take_profit_2: float      # Secondary: opposite VA boundary
    lot_size: float
    confluence_score: int
    grade: str                # "A" (≥7), "B" (5-6), "SKIP" (<5)
    regime: Regime
    confirmations: List[str]  # Which factors confirmed


# ============================================================
# 1. POC DETECTOR — Level Detection Engine
# ============================================================
class POCDetector:
    """Builds volume profile from OHLCV data and extracts POC, VA, HVN, LVN."""

    @staticmethod
    def build_volume_profile(df: pd.DataFrame, n_bins: int = 100) -> Dict:
        """
        Build volume profile from OHLCV dataframe.
        df must have columns: open, high, low, close, volume (tick or real).
        Returns dict with bins, poc, vah, val, hvn_list, lvn_list.
        """
        price_high = df["high"].max()
        price_low = df["low"].min()
        bin_size = (price_high - price_low) / n_bins
        if bin_size <= 0:
            return {"error": "Invalid price range"}

        bins = np.zeros(n_bins)
        bin_prices = [price_low + (i + 0.5) * bin_size for i in range(n_bins)]

        for _, row in df.iterrows():
            vol = row.get("volume", row.get("tick_volume", 1))
            low_bin = max(0, min(int((row["low"] - price_low) / bin_size), n_bins - 1))
            high_bin = max(0, min(int((row["high"] - price_low) / bin_size), n_bins - 1))
            close_bin = max(0, min(int((row["close"] - price_low) / bin_size), n_bins - 1))
            span = high_bin - low_bin + 1
            for b in range(low_bin, high_bin + 1):
                weight = 1.0 / (abs(b - close_bin) + 1)
                bins[b] += vol * weight / span

        # POC = bin with max volume
        poc_idx = int(np.argmax(bins))
        poc_price = round(bin_prices[poc_idx], 5)

        # Value Area = 70% of total volume centered on POC
        total_vol = bins.sum()
        target_vol = total_vol * 0.70
        va_vol = bins[poc_idx]
        lo, hi = poc_idx, poc_idx
        while va_vol < target_vol and (lo > 0 or hi < n_bins - 1):
            up_vol = bins[hi + 1] if hi + 1 < n_bins else 0
            dn_vol = bins[lo - 1] if lo - 1 >= 0 else 0
            if up_vol >= dn_vol and hi + 1 < n_bins:
                hi += 1; va_vol += bins[hi]
            elif lo - 1 >= 0:
                lo -= 1; va_vol += bins[lo]
            else:
                hi = min(hi + 1, n_bins - 1); va_vol += bins[hi]

        vah = round(bin_prices[hi], 5)
        val = round(bin_prices[lo], 5)

        # HVN/LVN detection
        mean_vol = bins.mean()
        std_vol = bins.std()
        hvn = [round(bin_prices[i], 5) for i in range(n_bins) if bins[i] > mean_vol + 0.5 * std_vol]
        lvn = [round(bin_prices[i], 5) for i in range(n_bins) if bins[i] < mean_vol - 0.5 * std_vol and bins[i] > 0]

        return {
            "poc": poc_price, "vah": vah, "val": val,
            "hvn_list": hvn, "lvn_list": lvn,
            "total_volume": round(total_vol, 2),
            "bin_prices": bin_prices, "bin_volumes": bins.tolist(),
        }

    @staticmethod
    def detect_session_pocs(data_by_session: Dict[str, pd.DataFrame],
                            atr: float, n_bins: int = 100) -> List[POCLevel]:
        """Detect POC for each session and mark naked/cluster status."""
        pocs = []
        for session_id, df in data_by_session.items():
            if df.empty or len(df) < 10:
                continue
            profile = POCDetector.build_volume_profile(df, n_bins)
            if "error" in profile:
                continue
            zone_width = atr * 0.3
            pocs.append(POCLevel(
                price=profile["poc"],
                zone_high=round(profile["poc"] + zone_width, 5),
                zone_low=round(profile["poc"] - zone_width, 5),
                volume=profile["total_volume"],
                timeframe="session",
                session_date=session_id,
            ))

        # Mark naked POCs (not yet retested by current price)
        # Caller should update is_naked based on current price history

        # Detect clusters (POCs within 0.5×ATR of each other)
        merge_threshold = atr * 0.5
        for i in range(len(pocs)):
            for j in range(i + 1, len(pocs)):
                if abs(pocs[i].price - pocs[j].price) < merge_threshold:
                    pocs[i].is_cluster = True
                    pocs[j].is_cluster = True
                    pocs[i].cluster_strength += 1
                    pocs[j].cluster_strength += 1

        return pocs

    @staticmethod
    def update_naked_status(pocs: List[POCLevel], price_history: pd.Series) -> List[POCLevel]:
        """Mark POCs as tested if price has visited their zone."""
        for poc in pocs:
            touches = ((price_history >= poc.zone_low) & (price_history <= poc.zone_high)).sum()
            if touches > 1:  # >1 because the original session counts as 1
                poc.is_naked = False
                poc.tested_count = int(touches) - 1
        return pocs


# ============================================================
# 2. REGIME CLASSIFIER
# ============================================================
class RegimeClassifier:
    """Classifies market regime from profile shape and price action."""

    @staticmethod
    def classify(profile: Dict, df: pd.DataFrame, atr: float) -> Regime:
        """
        Classify regime based on:
        - Profile shape (distribution of volume)
        - Price position relative to VA
        - Recent price action (HH/HL vs LH/LL)
        """
        poc = profile["poc"]
        vah = profile["vah"]
        val = profile["val"]
        va_range = vah - val
        current = df["close"].iloc[-1]

        # Check if price is outside all known value areas (breakout)
        if current > vah + atr or current < val - atr:
            return Regime.BREAKOUT

        # Check trend from recent swing structure
        highs = df["high"].rolling(20).max()
        lows = df["low"].rolling(20).min()
        recent_highs = df["high"].tail(40)
        recent_lows = df["low"].tail(40)

        # Simple HH/HL check
        mid = len(recent_highs) // 2
        first_half_high = recent_highs.iloc[:mid].max()
        second_half_high = recent_highs.iloc[mid:].max()
        first_half_low = recent_lows.iloc[:mid].min()
        second_half_low = recent_lows.iloc[mid:].min()

        if second_half_high > first_half_high and second_half_low > first_half_low:
            return Regime.TRENDING_UP
        elif second_half_high < first_half_high and second_half_low < first_half_low:
            return Regime.TRENDING_DN

        return Regime.BALANCED

    @staticmethod
    def is_bounce_allowed(regime: Regime, direction: BounceDirection) -> bool:
        """Check if bounce direction is compatible with regime."""
        if regime == Regime.BREAKOUT:
            return False
        if regime == Regime.TRENDING_UP and direction == BounceDirection.SHORT:
            return False
        if regime == Regime.TRENDING_DN and direction == BounceDirection.LONG:
            return False
        return True


# ============================================================
# 3. CONFLUENCE SCORER — 10-Point System
# ============================================================
CONFLUENCE_FACTORS = {
    "naked_poc":          {"points": 3, "desc": "Naked (Virgin) POC — first test ever"},
    "htf_poc_alignment":  {"points": 2, "desc": "POC aligns with weekly/monthly POC"},
    "va_boundary":        {"points": 2, "desc": "POC at/near VAH or VAL boundary"},
    "poc_cluster":        {"points": 2, "desc": "POC cluster (2+ sessions within 0.5×ATR)"},
    "fib_alignment":      {"points": 1, "desc": "Fibonacci 0.5/0.618 retracement alignment"},
    "rsi_divergence":     {"points": 1, "desc": "RSI divergence at POC level"},
    "order_block_fvg":    {"points": 1, "desc": "Order block or FVG alignment"},
    "strong_rejection":   {"points": 1, "desc": "Rejection candle wick/body ≥ 2.0"},
    "trend_aligned":      {"points": 1, "desc": "Bounce in direction of HTF trend"},
    "volume_spike":       {"points": 1, "desc": "Volume spike on bounce candle (>1.5× avg)"},
    # PENALTIES
    "second_test":        {"points": -2, "desc": "PENALTY: POC already tested once"},
    "counter_trend":      {"points": -2, "desc": "PENALTY: Bounce against dominant trend"},
}

class ConfluenceScorer:
    @staticmethod
    def score(factors_present: List[str]) -> Dict:
        """Score a setup based on which confluence factors are present."""
        total = 0
        details = []
        for f in factors_present:
            if f in CONFLUENCE_FACTORS:
                pts = CONFLUENCE_FACTORS[f]["points"]
                total += pts
                details.append({"factor": f, "points": pts,
                               "desc": CONFLUENCE_FACTORS[f]["desc"]})

        grade = "A" if total >= 7 else "B" if total >= 5 else "SKIP"
        risk_mult = 1.0 if grade == "A" else 0.5 if grade == "B" else 0.0

        return {
            "score": total, "grade": grade,
            "risk_multiplier": risk_mult,
            "details": details,
            "tradeable": total >= 5,
            "action": f"{'FULL SIZE' if grade == 'A' else 'HALF SIZE' if grade == 'B' else 'NO TRADE'}"
        }


# ============================================================
# 4. BOUNCE CONFIRMATION
# ============================================================
class BounceConfirmation:
    @staticmethod
    def check_rejection_candle(open_p, high, low, close, min_ratio=1.5) -> Dict:
        """Check for rejection candle at POC level."""
        body = abs(close - open_p)
        if body == 0: body = 0.0001
        upper_wick = high - max(close, open_p)
        lower_wick = min(close, open_p) - low

        is_bullish_rejection = (lower_wick / body >= min_ratio) and close > open_p
        is_bearish_rejection = (upper_wick / body >= min_ratio) and close < open_p
        strong = max(lower_wick, upper_wick) / body >= 2.0

        return {
            "bullish_rejection": is_bullish_rejection,
            "bearish_rejection": is_bearish_rejection,
            "wick_body_ratio": round(max(lower_wick, upper_wick) / body, 2),
            "strong_rejection": strong,
            "direction": "long" if is_bullish_rejection else "short" if is_bearish_rejection else "none",
        }

    @staticmethod
    def check_rsi(rsi_value: float) -> Dict:
        """RSI confirmation for bounce direction."""
        return {
            "value": rsi_value,
            "long_confirm": rsi_value < 50,
            "short_confirm": rsi_value > 50,
            "oversold": rsi_value < 35,
            "overbought": rsi_value > 65,
        }

    @staticmethod
    def check_volume_spike(current_vol, avg_vol, threshold=1.5) -> bool:
        """Check if current bar volume is a spike above average."""
        return current_vol > avg_vol * threshold if avg_vol > 0 else False

    @staticmethod
    def full_confirmation(candle, rsi_val, volume, avg_volume, poc: POCLevel) -> Dict:
        """Run all confirmation checks and return combined result."""
        rejection = BounceConfirmation.check_rejection_candle(
            candle["open"], candle["high"], candle["low"], candle["close"])
        rsi = BounceConfirmation.check_rsi(rsi_val)
        vol_spike = BounceConfirmation.check_volume_spike(volume, avg_volume)

        # Determine direction
        direction = None
        confirmations = []

        if rejection["bullish_rejection"] and candle["low"] <= poc.zone_high:
            direction = BounceDirection.LONG
            confirmations.append("bullish_rejection_candle")
            if rsi["long_confirm"]: confirmations.append("rsi_below_50")
            if rsi["oversold"]: confirmations.append("rsi_oversold")
            if vol_spike: confirmations.append("volume_spike")
            if rejection["strong_rejection"]: confirmations.append("strong_rejection")

        elif rejection["bearish_rejection"] and candle["high"] >= poc.zone_low:
            direction = BounceDirection.SHORT
            confirmations.append("bearish_rejection_candle")
            if rsi["short_confirm"]: confirmations.append("rsi_above_50")
            if rsi["overbought"]: confirmations.append("rsi_overbought")
            if vol_spike: confirmations.append("volume_spike")
            if rejection["strong_rejection"]: confirmations.append("strong_rejection")

        return {
            "confirmed": direction is not None and len(confirmations) >= 2,
            "direction": direction,
            "confirmations": confirmations,
            "n_confirmations": len(confirmations),
            "rejection": rejection,
            "rsi": rsi,
            "volume_spike": vol_spike,
        }


# ============================================================
# 5. TRADE MANAGER — SL/TP/Sizing
# ============================================================
class TradeManager:
    @staticmethod
    def calculate_trade(direction: BounceDirection, entry: float, atr: float,
                        poc: POCLevel, next_hvn: Optional[float],
                        opposite_va: Optional[float],
                        balance: float, risk_pct: float = 1.0,
                        tick_value: float = 1.0, tick_size: float = 0.01,
                        sl_atr_mult: float = 1.5, tp_atr_mult: float = 2.5) -> Dict:
        """Calculate complete trade parameters."""
        sl_dist = atr * sl_atr_mult
        tp_dist = atr * tp_atr_mult

        if direction == BounceDirection.LONG:
            sl = round(entry - sl_dist, 5)
            tp1 = round(next_hvn if next_hvn else entry + tp_dist, 5)
            tp2 = round(opposite_va if opposite_va else entry + tp_dist * 1.5, 5)
        else:
            sl = round(entry + sl_dist, 5)
            tp1 = round(next_hvn if next_hvn else entry - tp_dist, 5)
            tp2 = round(opposite_va if opposite_va else entry - tp_dist * 1.5, 5)

        # Position sizing
        risk_amount = balance * risk_pct / 100
        sl_ticks = sl_dist / tick_size if tick_size > 0 else 1
        lot_size = risk_amount / (sl_ticks * tick_value) if (sl_ticks * tick_value) > 0 else 0.01
        lot_size = round(max(0.01, lot_size), 2)

        # R:R calculation
        reward = abs(tp1 - entry)
        risk = abs(entry - sl)
        rr = round(reward / risk, 2) if risk > 0 else 0

        return {
            "entry": entry, "stop_loss": sl,
            "take_profit_1": tp1, "take_profit_2": tp2,
            "lot_size": lot_size, "risk_reward": rr,
            "risk_amount": round(risk_amount, 2),
            "sl_distance": round(sl_dist, 5),
            "tradeable": rr >= 1.0,
            "management": {
                "move_sl_to_be_after": f"{atr:.2f} (1×ATR) in profit",
                "trail_stop": f"Behind developing POC or {atr:.2f} (1×ATR)",
                "partial_exit": "Close 50% at TP1, trail rest to TP2",
            }
        }


# ============================================================
# 6. THE 80% RULE (Value Area Fill)
# ============================================================
class EightyPercentRule:
    """
    If price opens outside previous session's VA, re-enters, and stays
    inside for 2 consecutive 30-min periods → 80% probability of filling
    the entire Value Area (VAH to VAL or vice versa).
    """
    @staticmethod
    def check(open_price: float, current_price: float,
              prev_va: ValueArea, bars_inside_va: int) -> Dict:
        opened_above = open_price > prev_va.vah
        opened_below = open_price < prev_va.val
        opened_outside = opened_above or opened_below
        now_inside = prev_va.val <= current_price <= prev_va.vah
        confirmed = opened_outside and now_inside and bars_inside_va >= 2

        direction = None
        target = None
        if confirmed:
            if opened_above:
                direction = "short"
                target = prev_va.val
            elif opened_below:
                direction = "long"
                target = prev_va.vah

        return {
            "rule_active": confirmed,
            "opened_outside": opened_outside,
            "re_entered": now_inside,
            "bars_inside": bars_inside_va,
            "direction": direction,
            "target": target,
            "stop": prev_va.vah + 0.002 if direction == "short" else prev_va.val - 0.002 if direction == "long" else None,
            "probability": "~80%" if confirmed else "N/A",
            "note": "Works best in balanced/mean-reverting conditions. Avoid on trend days.",
        }


# ============================================================
# 7. SKILL ROUTER — Link to Other Skills
# ============================================================
class SkillRouter:
    ROUTES = {
        "poc_near_order_block": {
            "skill": "multi-tf-order-block-mapper",
            "action": "Check if POC aligns with HTF order block for extra confluence",
        },
        "currency_strength_filter": {
            "skill": "currency-strength-meter",
            "action": "Check relative strength before taking forex POC bounce",
        },
        "divergence_at_poc": {
            "skill": "cross-timeframe-divergence-scanner",
            "action": "Scan for RSI/MACD divergence across timeframes at POC level",
        },
        "candle_pattern_at_poc": {
            "skill": "candlestick-statistics-engine",
            "action": "Look up win rate of rejection candle pattern at the POC",
        },
        "build_ea": {
            "skill": "mq5-mq4-how-to-work-with",
            "action": "Convert this setup to an MQL5 Expert Advisor for backtesting",
        },
        "auto_strategy": {
            "skill": "automated-strategy-builder",
            "action": "Generate structured strategy code from the POC bounce rules",
        },
        "correlation_check": {
            "skill": "correlation-heatmap-visualizer",
            "action": "Check if correlated pairs confirm the POC bounce direction",
        },
    }

    @staticmethod
    def suggest(setup_context: Dict) -> List[Dict]:
        """Suggest linked skills based on the current setup context."""
        suggestions = []
        if setup_context.get("has_order_block"):
            suggestions.append(SkillRouter.ROUTES["poc_near_order_block"])
        if setup_context.get("instrument_type") == "forex":
            suggestions.append(SkillRouter.ROUTES["currency_strength_filter"])
        if setup_context.get("has_divergence"):
            suggestions.append(SkillRouter.ROUTES["divergence_at_poc"])
        suggestions.append(SkillRouter.ROUTES["candle_pattern_at_poc"])
        if setup_context.get("wants_ea"):
            suggestions.append(SkillRouter.ROUTES["build_ea"])
        return suggestions
```

## Session Timing (XAUUSD)

| Session | Hours (GMT) | POC Strategy |
|---------|------------|--------------|
| Asian | 00:00–07:00 | AVOID. Low vol, builds liquidity for London sweep |
| London | 07:00–12:00 | PRIME. Sweeps into POC levels, best bounce session |
| NY Overlap | 12:00–16:00 | EXCELLENT. Continuation or news reversal at POC |
| Late NY | 16:00–21:00 | 80% Rule setups. Fading extreme moves back to POC |

## XAUUSD-Specific Settings

- **Bin size**: 0.10 on M5–M30; 1.00 on H1–D1
- **POC zone width**: 0.3 × ATR(14) ≈ $5–$10
- **SL**: 1.5 × ATR; **TP1**: next HVN/POC; **TP2**: opposite VA boundary
- **Volume**: Tick volume works as proxy (correlates with real volume)
- **Sessions**: London + NY overlap only for live entries
- **Risk**: 1% per trade, max 3% daily drawdown

## Pre-Trade Checklist (ALL mandatory items must pass)

1. ☐ Market regime is NOT pure breakout/discovery — **MANDATORY**
2. ☐ Rejection candle formed (wick/body ≥ 1.5) — **MANDATORY**
3. ☐ Confluence score ≥ 5 — **MANDATORY**
4. ☐ No major news in next 30 min — **MANDATORY**
5. ☐ Risk ≤ 1% of balance, position sized — **MANDATORY**
6. ☐ R:R ratio ≥ 1:1 — **MANDATORY**
7. ☐ Naked POC (first test) — Preferred
8. ☐ Bounce in HTF trend direction — Preferred
9. ☐ Within optimal session (London/NY) — Preferred
10. ☐ RSI confirms direction — Preferred

## Skill File Locations

```
poc-bounce-strategy/
├── SKILL.md                              ← You are here
├── references/
│   └── full-strategy-rules.md            ← Deep strategy: profile shapes, 80% rule,
│                                            liquidity sweeps, daily routine, all tables
└── scripts/
    └── poc_engine.py                     ← Standalone Python engine (copy of above classes)
```

**For detailed strategy rules, profile shape analysis, trade examples, and the daily
trading routine, read `references/full-strategy-rules.md`.**
