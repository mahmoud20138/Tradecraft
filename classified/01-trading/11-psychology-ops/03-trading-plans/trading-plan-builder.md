---
name: trading-plan-builder
description: >
  Structured pre-market routine, watchlist generation, daily preparation checklist, and trading
  plan templates. Use this skill for "trading plan", "pre-market routine", "daily prep",
  "watchlist", "what should I focus on today", "morning routine", "prepare for trading",
  "daily checklist", "plan my trading day", "what pairs to watch", or any trading preparation.
  Works with all analysis skills to auto-generate the daily plan.
kind: workflow
category: trading/strategies
status: active
tags: [builder, plan, psychology, trading]
related_skills: [price-action, xtrading-analyze, capitulation-mean-reversion, mtf-confluence-scorer, poc-bounce-strategy]
---

# Trading Plan Builder

```python
from datetime import datetime, timedelta
from dataclasses import dataclass, field

@dataclass
class DailyTradingPlan:
    date: str
    session_focus: str
    watchlist: list[dict] = field(default_factory=list)
    macro_context: str = ""
    key_events: list[str] = field(default_factory=list)
    bias: dict = field(default_factory=dict)
    risk_budget: dict = field(default_factory=dict)
    rules_today: list[str] = field(default_factory=list)
    checklist: dict = field(default_factory=dict)

class TradingPlanBuilder:

    @staticmethod
    def pre_market_checklist() -> dict:
        return {
            "1_macro_scan": {
                "task": "Check DXY, VIX, yield curves, equity futures",
                "tools": ["macro-economic-dashboard"],
                "time": "5 min",
            },
            "2_news_check": {
                "task": "Review upcoming economic events and overnight news",
                "tools": ["market-news-impact", "risk-calendar-trade-filter"],
                "time": "5 min",
            },
            "3_htf_analysis": {
                "task": "D1 and H4 analysis on watchlist pairs — set daily bias",
                "tools": ["mt5-chart-browser", "mtf-confluence-scorer"],
                "time": "10 min",
            },
            "4_key_levels": {
                "task": "Mark S/R, order blocks, FVGs on H1 charts",
                "tools": ["trendline-sr-vision", "liquidity-order-flow-mapper"],
                "time": "10 min",
            },
            "5_risk_budget": {
                "task": "Set max risk for the day, check portfolio heat",
                "tools": ["risk-and-portfolio"],
                "time": "2 min",
            },
            "6_session_check": {
                "task": "Verify current session quality and killzones",
                "tools": ["session-profiler", "risk-calendar-trade-filter"],
                "time": "2 min",
            },
            "total_time": "~35 minutes",
        }

    @staticmethod
    def generate_watchlist(pairs: list[str], confluence_scores: dict) -> list[dict]:
        """Rank pairs by confluence and generate focused watchlist."""
        watchlist = []
        for pair in pairs:
            score = confluence_scores.get(pair, {})
            watchlist.append({
                "pair": pair,
                "mtf_score": score.get("overall_score", 0),
                "bias": score.get("direction", "NEUTRAL"),
                "confluence_pct": score.get("confluence_pct", 0),
                "priority": "A" if score.get("confluence_pct", 0) >= 75 else
                           "B" if score.get("confluence_pct", 0) >= 50 else "C",
            })
        return sorted(watchlist, key=lambda w: w.get("confluence_pct", 0), reverse=True)[:6]

    @staticmethod
    def end_of_day_review() -> dict:
        return {
            "1_log_trades": "Journal all trades with setup type, entry/exit reasoning, and R-multiple",
            "2_review_execution": "Did you follow the plan? Rate 1-10.",
            "3_what_worked": "List setups that worked and why",
            "4_what_failed": "List setups that failed and why",
            "5_lessons": "One key lesson for tomorrow",
            "6_emotional_state": "Rate emotional discipline 1-10",
            "7_plan_adjustments": "Any changes for tomorrow's plan?",
        }

    @staticmethod
    def build_plan(now: datetime = None) -> DailyTradingPlan:
        now = now or datetime.utcnow()
        session = "london" if 7 <= now.hour < 13 else "new_york" if 13 <= now.hour < 22 else "tokyo"
        return DailyTradingPlan(
            date=now.strftime("%Y-%m-%d"),
            session_focus=session,
            risk_budget={"max_risk_today": "4%", "max_trades": 3, "max_loss_per_trade": "2%"},
            rules_today=[
                "Follow the plan. Do not deviate.",
                "Only A and B grade setups.",
                "No revenge trades after a loss.",
                "Stop after 3 trades (win or lose).",
                "No trading in last hour before high-impact news."],
            checklist=TradingPlanBuilder.pre_market_checklist(),
        )
```
