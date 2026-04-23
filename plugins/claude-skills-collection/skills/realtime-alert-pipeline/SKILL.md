---
name: realtime-alert-pipeline
description: >
  Condition monitoring, multi-trigger alerts, and notification pipeline for trading signals.
  Use this skill whenever the user asks about "set an alert", "price alert", "notify me when",
  "trigger alert", "condition monitoring", "signal pipeline", "push notification trading",
  "alert system", "watchlist alerts", "multi-condition trigger", "composite alert",
  or any request to set up automated monitoring and alerting. Works with mt5-chart-browser
  for data and all analysis skills for condition generation.
kind: tool
category: trading/infrastructure
status: active
aliases: [alert-pipeline]
tags: [alert, alerts, infrastructure, mt5, pipeline, realtime, trading]
related_skills: [discord-webhook, mt5-chart-browser, notion-sync, telegram-bot, trade-copier-signal-broadcaster]
---

# Real-Time Alert & Signal Pipeline

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Callable, Optional
import json

@dataclass
class AlertCondition:
    name: str
    check_fn: Callable  # returns True/False
    priority: str = "MEDIUM"  # HIGH, MEDIUM, LOW
    cooldown_minutes: int = 60
    last_triggered: Optional[datetime] = None

@dataclass
class AlertRule:
    id: str
    name: str
    conditions: list[AlertCondition]
    logic: str = "ALL"  # ALL (AND) or ANY (OR)
    channels: list[str] = field(default_factory=lambda: ["console"])
    message_template: str = ""

class AlertPipeline:

    def __init__(self):
        self.rules: list[AlertRule] = []
        self.triggered_alerts: list[dict] = []

    def add_rule(self, rule: AlertRule):
        self.rules.append(rule)

    def check_all(self, context: dict) -> list[dict]:
        """Check all rules against current market context."""
        triggered = []
        now = datetime.utcnow()
        for rule in self.rules:
            results = []
            for cond in rule.conditions:
                if cond.last_triggered and (now - cond.last_triggered).seconds < cond.cooldown_minutes * 60:
                    results.append(False)
                    continue
                try:
                    results.append(cond.check_fn(context))
                except:
                    results.append(False)

            fire = all(results) if rule.logic == "ALL" else any(results)
            if fire:
                alert = {
                    "rule_id": rule.id, "name": rule.name, "time": now.isoformat(),
                    "priority": max((c.priority for c in rule.conditions), key=lambda p: {"HIGH": 3, "MEDIUM": 2, "LOW": 1}[p]),
                    "channels": rule.channels,
                    "message": rule.message_template.format(**context) if rule.message_template else rule.name,
                }
                triggered.append(alert)
                for cond in rule.conditions:
                    cond.last_triggered = now
        self.triggered_alerts.extend(triggered)
        return triggered

    def format_for_telegram(self, alert: dict) -> str:
        return f"🚨 *{alert['priority']}* — {alert['name']}\n{alert['message']}\n⏰ {alert['time']}"

    def format_for_mt5(self, alert: dict) -> str:
        return f"Alert(\"{alert['name']}\", \"{alert['message']}\");"

# Preset alert conditions
def price_above(symbol: str, level: float):
    return AlertCondition(f"{symbol} > {level}", lambda ctx: ctx.get(f"{symbol}_price", 0) > level, "HIGH")

def rsi_extreme(symbol: str, overbought: float = 70, oversold: float = 30):
    return AlertCondition(f"{symbol} RSI extreme",
        lambda ctx: ctx.get(f"{symbol}_rsi", 50) > overbought or ctx.get(f"{symbol}_rsi", 50) < oversold, "MEDIUM")

def correlation_shift(pair: str, threshold: float = 0.3):
    return AlertCondition(f"{pair} corr shift",
        lambda ctx: abs(ctx.get(f"{pair}_corr_deviation", 0)) > threshold, "HIGH")
```
