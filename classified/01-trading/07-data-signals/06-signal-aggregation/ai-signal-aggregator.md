---
name: ai-signal-aggregator
description: >
  ML-powered signal aggregation across ALL strategy skills — combines signals from every strategy
  using weighted voting, random forest meta-learner, and confidence calibration. THE MASTER
  SIGNAL COMBINER. Use for "combine all signals", "aggregate strategies", "meta strategy",
  "AI signal", "ensemble signal", "which signal to follow", "best signal now", "combine everything",
  "master signal", "AI recommendation", or any request to synthesize signals from multiple skills.
  This is the intelligence layer ABOVE trading-brain.
kind: engine
category: trading/data
status: active
aliases: [ai-signal-aggregator]
tags: [aggregator, data, signal, trading]
related_skills: [trading-brain]
---

# AI Signal Aggregator — Meta-Strategy Signal Combiner

```python
import pandas as pd, numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.calibration import CalibratedClassifierCV

class AISignalAggregator:

    @staticmethod
    def weighted_vote(signals: dict, weights: dict = None) -> dict:
        """Combine signals from multiple strategies using weighted voting."""
        default_weights = {
            "trend_following": 1.2, "mean_reversion": 0.8, "breakout": 1.0,
            "price_action": 1.3, "divergence": 0.9, "momentum": 0.8,
            "institutional": 1.5, "news": 0.7, "sentiment_contrarian": 0.6,
            "fibonacci": 0.7, "harmonic": 0.6, "elliott_wave": 0.5,
            "wyckoff": 1.2, "supply_demand": 1.1, "volume_profile": 1.0,
            "market_structure": 1.3, "session_breakout": 0.9, "mtf_confluence": 1.4,
        }
        weights = weights or default_weights
        total_score = 0
        total_weight = 0
        details = []

        for strategy, signal in signals.items():
            w = weights.get(strategy, 1.0)
            # Normalize signal to -1 (sell) to +1 (buy)
            if isinstance(signal, str):
                s = signal.upper()
                score = 1.0 if "BUY" in s or "BULL" in s or "LONG" in s else -1.0 if "SELL" in s or "BEAR" in s or "SHORT" in s else 0
            elif isinstance(signal, (int, float)):
                score = np.clip(signal, -1, 1)
            elif isinstance(signal, dict):
                score = signal.get("score", signal.get("signal_score", 0))
            else:
                continue

            total_score += score * w
            total_weight += abs(w)
            details.append({"strategy": strategy, "signal_score": round(score, 2), "weight": w, "contribution": round(score * w, 3)})

        normalized = total_score / max(total_weight, 1e-10)
        agreement = sum(1 for d in details if np.sign(d["signal_score"]) == np.sign(normalized)) / max(len(details), 1)

        return {
            "composite_score": round(normalized, 4),
            "direction": "STRONG BUY" if normalized > 0.5 else "BUY" if normalized > 0.2 else "STRONG SELL" if normalized < -0.5 else "SELL" if normalized < -0.2 else "NEUTRAL",
            "confidence": round(min(abs(normalized) * agreement * 1.5, 0.95), 3),
            "agreement_pct": round(agreement * 100, 1),
            "n_strategies": len(details),
            "bullish_count": sum(1 for d in details if d["signal_score"] > 0),
            "bearish_count": sum(1 for d in details if d["signal_score"] < 0),
            "neutral_count": sum(1 for d in details if d["signal_score"] == 0),
            "top_contributors": sorted(details, key=lambda d: abs(d["contribution"]), reverse=True)[:5],
            "conflicts": [d["strategy"] for d in details if np.sign(d["signal_score"]) != np.sign(normalized) and d["signal_score"] != 0],
            "trade_decision": AISignalAggregator._make_decision(normalized, agreement, len(details)),
        }

    @staticmethod
    def _make_decision(score: float, agreement: float, n_strategies: int) -> str:
        if n_strategies < 3:
            return "INSUFFICIENT DATA — need at least 3 strategy signals"
        if abs(score) > 0.4 and agreement > 0.7:
            return f"HIGH CONVICTION {'BUY' if score > 0 else 'SELL'} — full position size"
        if abs(score) > 0.25 and agreement > 0.5:
            return f"MODERATE {'BUY' if score > 0 else 'SELL'} — reduced position size"
        if abs(score) > 0.15:
            return f"LOW CONVICTION {'BUY' if score > 0 else 'SELL'} — test position only"
        return "NO TRADE — insufficient consensus across strategies"

    @staticmethod
    def train_meta_model(historical_signals: pd.DataFrame, outcomes: pd.Series) -> dict:
        """Train an ML meta-model to learn optimal signal weights from history."""
        X = historical_signals.dropna()
        y = (outcomes.reindex(X.index) > 0).astype(int)
        common = X.index.intersection(y.index)
        X, y = X.loc[common], y.loc[common]

        # Time-series split
        split = int(len(X) * 0.7)
        X_train, X_test = X.iloc[:split], X.iloc[split:]
        y_train, y_test = y.iloc[:split], y.iloc[split:]

        model = CalibratedClassifierCV(GradientBoostingClassifier(n_estimators=100, max_depth=3), cv=3)
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)

        # Extract learned weights (feature importance)
        base_model = model.calibrated_classifiers_[0].estimator
        importances = dict(zip(X.columns, base_model.feature_importances_))
        top = sorted(importances.items(), key=lambda x: x[1], reverse=True)

        return {
            "oos_accuracy": round(accuracy, 4),
            "learned_weights": {k: round(v, 4) for k, v in top[:10]},
            "most_predictive": top[0][0],
            "least_predictive": top[-1][0],
            "WARNING": "Meta-model overfits easily. Re-train monthly with walk-forward.",
        }
```
