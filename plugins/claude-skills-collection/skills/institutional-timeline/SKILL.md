---
name: institutional-timeline
description: "Central bank policy tracking, COT positioning analysis, FX intervention detection, and event timeline linking with causal chain analysis. Use for central bank, COT report, institutional flow, FX intervention, policy divergence, event timeline, or any institutional behavior monitoring."
kind: reference
category: trading/market-context
status: active
tags: [institutional, market-context, timeline, trading]
related_skills: [macro-economic-dashboard, market-breadth-analyzer, market-regime-classifier]
---

# Institutional Behavior Monitor & Event Timeline Linker

## Part 1: Central Bank Tracker

```python
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional, Literal
import pandas as pd
import numpy as np

@dataclass
class CentralBankProfile:
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
    "FED":  CentralBankProfile("Federal Reserve",       "FED",  "USD", 0.0, "hold", "", "", "neutral",  "tightening", ["Chair","Vice Chair"], ["EURUSD","USDJPY","GBPUSD","USDCHF","AUDUSD","USDCAD","NZDUSD","XAUUSD"]),
    "ECB":  CentralBankProfile("European Central Bank", "ECB",  "EUR", 0.0, "hold", "", "", "neutral",  "stable",     ["President","Chief Economist"], ["EURUSD","EURJPY","EURGBP","EURAUD","EURCHF"]),
    "BOE":  CentralBankProfile("Bank of England",       "BOE",  "GBP", 0.0, "hold", "", "", "neutral",  "stable",     ["Governor","Deputy Governor"], ["GBPUSD","EURGBP","GBPJPY"]),
    "BOJ":  CentralBankProfile("Bank of Japan",         "BOJ",  "JPY", 0.0, "hold", "", "", "dovish",   "expanding",  ["Governor","Deputy Governor"], ["USDJPY","EURJPY","GBPJPY","AUDJPY"]),
    "RBA":  CentralBankProfile("Reserve Bank of Aus",   "RBA",  "AUD", 0.0, "hold", "", "", "neutral",  "stable",     ["Governor","Deputy Governor"], ["AUDUSD","AUDNZD","EURAUD","AUDJPY"]),
    "BOC":  CentralBankProfile("Bank of Canada",        "BOC",  "CAD", 0.0, "hold", "", "", "neutral",  "stable",     ["Governor","Senior Deputy"], ["USDCAD","CADJPY"]),
    "SNB":  CentralBankProfile("Swiss National Bank",   "SNB",  "CHF", 0.0, "hold", "", "", "neutral",  "stable",     ["Chairman","Vice Chairman"], ["USDCHF","EURCHF"]),
    "RBNZ": CentralBankProfile("Reserve Bank of NZ",    "RBNZ", "NZD", 0.0, "hold", "", "", "neutral",  "stable",     ["Governor","Deputy Governor"], ["NZDUSD","AUDNZD"]),
}

class CentralBankTracker:

    def get_policy_divergence(self) -> pd.DataFrame:
        """Map policy divergence — divergence drives currency pair trends."""
        data   = []
        banks  = list(CENTRAL_BANKS.values())
        bias_map = {"hawkish": 1, "neutral": 0, "dovish": -1}

        for i, bank_a in enumerate(banks):
            for bank_b in banks[i + 1:]:
                rate_diff  = bank_a.current_rate - bank_b.current_rate
                bias_diff  = bias_map.get(bank_a.bias, 0) - bias_map.get(bank_b.bias, 0)
                data.append({
                    "pair":            f"{bank_a.currency}/{bank_b.currency}",
                    "rate_differential": round(rate_diff, 2),
                    "bias_differential": bias_diff,
                    "divergence_signal": self._interpret_divergence(rate_diff, bias_diff),
                })
        return pd.DataFrame(data)

    @staticmethod
    def _interpret_divergence(rate_diff: float, bias_diff: int) -> str:
        if rate_diff > 0.5 and bias_diff > 0:  return "STRONG BUY base — widening rate + hawkish bias"
        if rate_diff < -0.5 and bias_diff < 0: return "STRONG SELL base — widening rate disadvantage"
        if abs(rate_diff) < 0.25 and bias_diff == 0: return "NEUTRAL — no clear divergence"
        if bias_diff > 0: return "MILD BUY base — bias divergence"
        if bias_diff < 0: return "MILD SELL base — quote currency favored"
        return "MIXED — conflicting signals"

    @staticmethod
    def rate_decision_impact_model(code: str, decision: str, expected: str) -> dict:
        """Model market impact of rate decision vs expectations."""
        bank = CENTRAL_BANKS.get(code)
        if not bank:
            return {"error": f"Unknown bank: {code}"}

        SURPRISE_MAP = {
            ("hike", "hold"): {"direction": "bullish",          "magnitude": "large",    "confidence": 0.85},
            ("hike", "hike"): {"direction": "neutral_to_bullish","magnitude": "small",   "confidence": 0.50},
            ("cut",  "hold"): {"direction": "bearish",          "magnitude": "large",    "confidence": 0.85},
            ("cut",  "cut"):  {"direction": "neutral_to_bearish","magnitude": "small",   "confidence": 0.50},
            ("hold", "hike"): {"direction": "bearish",          "magnitude": "medium",   "confidence": 0.70},
            ("hold", "cut"):  {"direction": "bullish",          "magnitude": "medium",   "confidence": 0.70},
            ("hold", "hold"): {"direction": "neutral",          "magnitude": "minimal",  "confidence": 0.30},
        }
        impact = SURPRISE_MAP.get((decision.lower(), expected.lower()),
                                   {"direction": "unknown", "magnitude": "unknown", "confidence": 0})
        return {
            "bank":          bank.name,
            "currency":      bank.currency,
            "decision":      decision,
            "expected":      expected,
            "is_surprise":   decision != expected,
            "impact":        impact,
            "affected_pairs": bank.affected_pairs,
            "recommendation": f"{'Strong' if impact['magnitude'] == 'large' else 'Moderate'} "
                              f"{impact['direction']} signal on {bank.currency} pairs"
                              if impact["confidence"] > 0.5 else "Wait for price action confirmation",
        }
```

---

## Part 2: COT Analyzer (Full Institutional)

```python
class COTAnalyzer:

    CURRENCY_CONTRACTS = {
        "EUR": "EURO FX", "GBP": "BRITISH POUND", "JPY": "JAPANESE YEN",
        "AUD": "AUSTRALIAN DOLLAR", "CAD": "CANADIAN DOLLAR", "CHF": "SWISS FRANC",
        "NZD": "NEW ZEALAND DOLLAR", "XAU": "GOLD", "WTI": "CRUDE OIL",
    }

    @staticmethod
    def analyze_positioning(cot_data: pd.DataFrame, currency: str) -> dict:
        """
        cot_data columns: [date, long_noncommercial, short_noncommercial, ...]
        """
        latest = cot_data.iloc[-1]
        prev   = cot_data.iloc[-2] if len(cot_data) > 1 else latest

        net_spec       = latest["long_noncommercial"] - latest["short_noncommercial"]
        prev_net_spec  = prev["long_noncommercial"]   - prev["short_noncommercial"]
        net_change     = net_spec - prev_net_spec

        historical_net = cot_data["long_noncommercial"] - cot_data["short_noncommercial"]
        percentile     = (historical_net < net_spec).mean() * 100

        signal = (
            "EXTREME LONG + UNWINDING → potential reversal (bearish)"  if percentile > 90 and net_change < 0
            else "EXTREME SHORT + COVERING → potential reversal (bullish)" if percentile < 10 and net_change > 0
            else "STRONG LONG + BUILDING → continuation but watch crowding" if percentile > 80
            else "MODERATE positioning — no extreme signal"
        )

        return {
            "currency":            currency,
            "net_speculative":     int(net_spec),
            "weekly_change":       int(net_change),
            "direction":           "LONG" if net_spec > 0 else "SHORT",
            "historical_percentile": round(percentile, 1),
            "extreme_positioning": percentile > 90 or percentile < 10,
            "signal":              signal,
        }
```

---

## Part 3: Intervention Detector

```python
class InterventionDetector:

    @staticmethod
    def detect_fx_intervention(df: pd.DataFrame, symbol: str,
                                atr_multiplier: float = 5.0,
                                volume_multiplier: float = 3.0) -> list[dict]:
        """Detect abnormal price moves indicating possible central bank intervention."""
        atr_val  = (df["high"] - df["low"]).rolling(14).mean()
        vol_avg  = df["volume"].rolling(20).mean()
        detections = []

        for i in range(20, len(df)):
            bar_range = df.iloc[i]["high"] - df.iloc[i]["low"]
            bar_vol   = df.iloc[i]["volume"]
            if bar_range > atr_multiplier * atr_val.iloc[i] and bar_vol > volume_multiplier * vol_avg.iloc[i]:
                prior_trend   = df["close"].iloc[i-10:i].pct_change().mean()
                bar_direction = 1 if df.iloc[i]["close"] > df.iloc[i]["open"] else -1
                is_reversal   = (prior_trend > 0 and bar_direction < 0) or (prior_trend < 0 and bar_direction > 0)
                detections.append({
                    "timestamp":        df.index[i].isoformat(),
                    "symbol":           symbol,
                    "bar_range_atr":    round(bar_range / atr_val.iloc[i], 2),
                    "volume_ratio":     round(bar_vol / vol_avg.iloc[i], 2),
                    "is_trend_reversal": is_reversal,
                    "intervention_probability": round(
                        min(0.3 + (bar_range / atr_val.iloc[i]) * 0.1 + (0.2 if is_reversal else 0), 0.95), 3),
                    "note": "Possible central bank intervention" if is_reversal else "Large institutional flow",
                })
        return detections

    @staticmethod
    def web_search_queries():
        return [
            'web_search("Federal Reserve interest rate 2025 current")',
            'web_search("ECB monetary policy latest decision")',
            'web_search("Goldman Sachs EURUSD forecast")',
            'web_search("JPMorgan FX outlook currencies")',
            'web_search("CFTC COT report latest forex positioning")']
```

---

## Part 4: Event Timeline Linker

```python
from dataclasses import dataclass, field, asdict

@dataclass
class TimelineEvent:
    """Universal event structure for cross-source linking."""
    timestamp: datetime
    source: Literal["price", "news", "economic", "institutional", "correlation", "technical", "geopolitical"]
    event_type: str
    title: str
    description: str
    impact: Literal["HIGH", "MEDIUM", "LOW"]
    affected_instruments: list[str] = field(default_factory=list)
    data: dict = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)

class TemporalAligner:

    @staticmethod
    def find_concurrent_events(events: list[TimelineEvent], target_time: datetime,
                                window: timedelta = timedelta(hours=4)) -> list[TimelineEvent]:
        return [e for e in events
                if abs((e.timestamp - target_time).total_seconds()) <= window.total_seconds()]

    @staticmethod
    def cluster_by_time(events: list[TimelineEvent],
                         max_gap: timedelta = timedelta(hours=2)) -> list[list[TimelineEvent]]:
        if not events:
            return []
        sorted_events = sorted(events, key=lambda e: e.timestamp)
        clusters = [[sorted_events[0]]]
        for event in sorted_events[1:]:
            if event.timestamp - clusters[-1][-1].timestamp <= max_gap:
                clusters[-1].append(event)
            else:
                clusters.append([event])
        return clusters

class CausalChainBuilder:
    """Build cause-effect chains from temporally aligned events."""

    CAUSAL_PATTERNS = {
        ("economic", "price"):     {"mechanism": "Economic data release triggered market repricing", "base_confidence": 0.7},
        ("news", "price"):         {"mechanism": "News headline drove sentiment shift and price reaction", "base_confidence": 0.5},
        ("institutional", "price"):{"mechanism": "Institutional flow caused directional pressure",         "base_confidence": 0.6},
        ("geopolitical", "price"): {"mechanism": "Geopolitical event triggered risk repricing",            "base_confidence": 0.6},
    }

    @staticmethod
    def build_narrative(cluster: list[TimelineEvent]) -> dict:
        """Build WHAT → WHY → HOW → RESULT → PREDICTION narrative."""
        cluster.sort(key=lambda e: e.timestamp)
        causes  = [e for e in cluster if e.source in ("economic", "news", "institutional", "geopolitical")]
        effects = [e for e in cluster if e.source in ("price", "correlation", "technical")]

        PREDICTIONS = {
            "economic":    "Watch for follow-through in direction of surprise. Elevated vol for 2-4h post-release.",
            "news":        "Sentiment moves often retrace 50-70%. Watch for confirmation at key S/R.",
            "institutional":"Institutional flows tend to persist. Watch continuation over 1-3 sessions.",
            "geopolitical":"Risk-off flows initially. JPY, CHF, Gold strengthen. Duration depends on escalation.",
        }

        primary_source = causes[0].source if causes else "unknown"
        return {
            "time_range": f"{cluster[0].timestamp.isoformat()} → {cluster[-1].timestamp.isoformat()}",
            "what":       " → ".join([e.title for e in cluster]),
            "why":        causes[0].description if causes else "Cause unclear — further analysis needed",
            "how":        "; ".join([f"{e.source}: {e.title}" for e in causes]) if causes else "No clear trigger",
            "result":     "; ".join([e.title for e in effects]) if effects else "Price impact not yet measured",
            "prediction": PREDICTIONS.get(primary_source, "Monitor for follow-through or reversal signals."),
            "n_events":   len(cluster),
            "sources":    list(set(e.source for e in cluster)),
        }
```

### Timeline Usage Rules
1. **Always collect from multiple sources** — single-source narratives are unreliable
2. **4h window for intraday events**, 24h for daily, 1 week for macro
3. **Confidence < 0.5** = hypothesis only, not conclusion
4. **Predictions are probabilistic** — never present as certainties
