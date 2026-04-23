---
name: trade-psychology-coach
description: >
  Trading psychology monitoring — tilt detection, emotional state tracking, trade-psychology-coach bias alerts,
  discipline scoring, and behavioral pattern recognition. Use for "trading psychology", "am I
  tilted", "revenge trading", "emotional trading", "discipline check", "trading mindset",
  "fear of missing out", "FOMO", "trading emotions", "overtrading detection", "psychology check",
  or any trading psychology question. Works with trade-journal-performance and drawdown-playbook.
kind: reference
category: trading/psychology
status: active
tags: [alerts, coach, drawdown, psychology, trade, trading]
related_skills: [trade-journal-analytics]
---

# Trade Psychology Coach

```python
import pandas as pd, numpy as np
from datetime import datetime, timedelta

class TradePsychologyCoach:

    @staticmethod
    def tilt_detector(trades: pd.DataFrame) -> dict:
        """Detect revenge trading and tilt from trade patterns."""
        if trades.empty or len(trades) < 5: return {"tilt_level": "INSUFFICIENT DATA"}
        recent = trades.tail(10)
        # Signs of tilt
        signals = []
        consecutive_losses = 0
        for _, t in recent.iterrows():
            if t.get("pnl_pips", 0) < 0: consecutive_losses += 1
            else: consecutive_losses = 0
        if consecutive_losses >= 3: signals.append(f"3+ consecutive losses ({consecutive_losses})")
        # Increasing position sizes after losses
        if len(recent) >= 4:
            last_lots = recent["lot_size"].tail(3).values
            if all(last_lots[i] > last_lots[i-1] for i in range(1, len(last_lots))):
                signals.append("DANGER: Increasing size after losses (revenge pattern)")
        # Rapid-fire trading
        if "entry_time" in recent.columns and len(recent) >= 3:
            times = pd.to_datetime(recent["entry_time"])
            gaps = times.diff().dt.total_seconds() / 60
            if gaps.tail(3).mean() < 15:
                signals.append("Rapid-fire entries (<15 min apart) — possible overtrading")
        # Wider stops (desperation)
        if "stop_loss" in recent.columns and "entry_price" in recent.columns:
            sl_distances = abs(recent["entry_price"] - recent["stop_loss"])
            if sl_distances.tail(3).mean() > sl_distances.mean() * 1.5:
                signals.append("Stop losses widening — possible hope trading")

        tilt_level = "HIGH" if len(signals) >= 3 else "MODERATE" if len(signals) >= 2 else "ELEVATED" if signals else "CALM"
        return {
            "tilt_level": tilt_level,
            "signals": signals,
            "consecutive_losses": consecutive_losses,
            "action": {
                "HIGH": "STOP TRADING IMMEDIATELY. Walk away for minimum 4 hours. Review journal.",
                "MODERATE": "Take a 30-minute break. Reduce position size by 50%.",
                "ELEVATED": "Be extra cautious. Only take A+ setups.",
                "CALM": "Emotional state appears normal. Continue with plan.",
            }[tilt_level],
        }

    @staticmethod
    def trade-psychology-coach_bias_check(trade_context: dict) -> list[dict]:
        """Flag common trade-psychology-coach biases that may be affecting decision-making."""
        biases = []
        if trade_context.get("adding_to_loser"):
            biases.append({"bias": "Sunk Cost Fallacy", "fix": "Your average price is irrelevant. Would you enter this trade fresh at current price?"})
        if trade_context.get("moved_stop_loss_further"):
            biases.append({"bias": "Loss Aversion", "fix": "A stop loss is a contract with yourself. Moving it breaks trust with your system."})
        if trade_context.get("closed_winner_early"):
            biases.append({"bias": "Disposition Effect", "fix": "You cut winners short and let losers run. Reverse this: trail winners, cut losers fast."})
        if trade_context.get("entered_because_others_said"):
            biases.append({"bias": "Herding", "fix": "Other people's analysis is noise unless you independently verified it."})
        if trade_context.get("big_win_then_bigger_risk"):
            biases.append({"bias": "House Money Effect", "fix": "Profits are real money, not 'house money'. Maintain standard risk."})
        if trade_context.get("missed_trade_then_chased"):
            biases.append({"bias": "FOMO", "fix": "There will always be another setup. Chasing fills at bad prices is -EV."})
        return biases

    @staticmethod
    def discipline_score(journal: pd.DataFrame) -> dict:
        """Score trading discipline from journal data."""
        if journal.empty: return {"score": 0, "error": "No journal data"}
        scores = []
        if "followed_plan" in journal.columns:
            scores.append(journal["followed_plan"].mean() * 100)
        if "setup_type" in journal.columns:
            has_setup = (journal["setup_type"] != "").mean() * 100
            scores.append(has_setup)
        if "lot_size" in journal.columns and "pnl_pips" in journal.columns:
            losers = journal[journal["pnl_pips"] < 0]
            if len(losers) > 0:
                size_after_loss = journal["lot_size"].shift(-1).loc[losers.index]
                increased = (size_after_loss > losers["lot_size"]).mean()
                scores.append((1 - increased) * 100)
        avg = np.mean(scores) if scores else 0
        return {
            "discipline_score": round(avg, 1),
            "grade": "A" if avg >= 85 else "B" if avg >= 70 else "C" if avg >= 55 else "D" if avg >= 40 else "F",
            "components": scores,
        }

    @staticmethod
    def pre_trade_checklist() -> dict:
        return {
            "questions": [
                "Am I following my trading plan?",
                "Is this setup in my playbook (not a random idea)?",
                "Am I trading because the setup is there, or because I WANT to trade?",
                "Would I take this trade if I'd just had 3 losses in a row?",
                "Is my position size within my rules?",
                "Have I defined my exit BEFORE entering?",
                "Am I emotionally neutral right now?"],
            "rule": "If ANY answer is NO or uncertain — do NOT take the trade.",
        }
```
