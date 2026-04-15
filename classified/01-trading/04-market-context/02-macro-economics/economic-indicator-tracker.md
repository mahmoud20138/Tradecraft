---
name: economic-indicator-tracker
description: >
  Track leading, lagging, and coincident economic indicators systematically. Use for "economic
  indicators", "leading indicator", "lagging indicator", "PMI tracker", "GDP tracker", "jobs data",
  "inflation tracker", "economic cycle", "recession indicator", "expansion indicator", "economic
  health", or any systematic macro indicator tracking. Works with macro-economic-dashboard.
kind: tool
category: trading/data
status: active
tags: [economic, indicator, market-context, tracker, trading]
related_skills: [economic-calendar, market-data-ingestion, alternative-data-integrator, macro-economic-dashboard, market-intelligence]
---

# Economic Indicator Tracker

```python
INDICATORS = {
    "leading": [
        {"name": "PMI Manufacturing", "frequency": "monthly", "impact": "HIGH", "pairs": ["USD", "EUR", "GBP"]},
        {"name": "Building Permits", "frequency": "monthly", "impact": "MEDIUM", "pairs": ["USD"]},
        {"name": "Consumer Confidence", "frequency": "monthly", "impact": "MEDIUM", "pairs": ["USD", "EUR"]},
        {"name": "Yield Curve 2-10", "frequency": "daily", "impact": "HIGH", "pairs": ["USD"]},
        {"name": "New Orders Index", "frequency": "monthly", "impact": "MEDIUM", "pairs": ["USD"]},
        {"name": "Stock Market (SPX)", "frequency": "daily", "impact": "HIGH", "pairs": ["ALL"]},
        {"name": "Initial Jobless Claims", "frequency": "weekly", "impact": "MEDIUM", "pairs": ["USD"]}],
    "coincident": [
        {"name": "Non-Farm Payrolls", "frequency": "monthly", "impact": "HIGH", "pairs": ["USD"]},
        {"name": "Industrial Production", "frequency": "monthly", "impact": "MEDIUM", "pairs": ["USD", "EUR"]},
        {"name": "Retail Sales", "frequency": "monthly", "impact": "HIGH", "pairs": ["USD", "GBP"]},
        {"name": "GDP", "frequency": "quarterly", "impact": "HIGH", "pairs": ["ALL"]}],
    "lagging": [
        {"name": "CPI / Inflation", "frequency": "monthly", "impact": "HIGH", "pairs": ["ALL"]},
        {"name": "Unemployment Rate", "frequency": "monthly", "impact": "HIGH", "pairs": ["USD"]},
        {"name": "Core PCE", "frequency": "monthly", "impact": "HIGH", "pairs": ["USD"]},
        {"name": "Average Hourly Earnings", "frequency": "monthly", "impact": "MEDIUM", "pairs": ["USD"]}],
}

class EconomicIndicatorTracker:
    @staticmethod
    def cycle_position(leading_trend: str, coincident_trend: str, lagging_trend: str) -> dict:
        if leading_trend == "improving" and coincident_trend == "improving":
            phase = "EXPANSION — risk-on currencies favored (AUD, NZD, CAD)"
        elif leading_trend == "deteriorating" and coincident_trend == "improving":
            phase = "LATE CYCLE — be cautious, peak may be near"
        elif leading_trend == "deteriorating" and coincident_trend == "deteriorating":
            phase = "CONTRACTION — safe havens favored (JPY, CHF, USD, Gold)"
        elif leading_trend == "improving" and coincident_trend == "deteriorating":
            phase = "EARLY RECOVERY — selective risk-on, high-beta currencies"
        else:
            phase = "TRANSITION — mixed signals"
        return {"phase": phase, "leading": leading_trend, "coincident": coincident_trend, "lagging": lagging_trend}

    @staticmethod
    def surprise_index(actual: float, forecast: float, previous: float) -> dict:
        surprise = actual - forecast
        beat = actual > forecast
        return {
            "surprise": round(surprise, 3),
            "beat_expectations": beat,
            "vs_previous": "improving" if actual > previous else "deteriorating",
            "market_impact": "Positive surprise — currency should strengthen" if beat else "Negative surprise — currency weakens",
        }
```
