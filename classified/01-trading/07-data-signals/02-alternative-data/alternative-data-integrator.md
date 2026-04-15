---
name: alternative-data-integrator
description: >
  Alternative data sources for trading signals — Google Trends, web traffic, search volume,
  shipping/supply chain data, satellite imagery proxies, and economic nowcasting. Use this skill
  whenever the user asks about "alternative data", "Google Trends trading", "search trends",
  "web traffic signals", "nowcasting", "satellite data trading", "shipping index", "Baltic Dry",
  "unusual data sources", "non-traditional indicators", "big data trading signals", or any
  request to incorporate non-standard data into trading decisions. Works with trading-data-science
  for feature engineering and trading-brain for signal integration.
kind: reference
category: trading/data
status: active
tags: [alternative, data, integrator, trading]
related_skills: [economic-calendar, market-data-ingestion, economic-indicator-tracker, market-intelligence, news-intelligence]
---

# Alternative Data Integrator

```python
import pandas as pd
import numpy as np
from datetime import datetime

class AlternativeDataSources:
    """
    Framework for integrating alternative data. In Claude context, use web_search
    to fetch data, then process through these analytical pipelines.
    """

    # Web search queries for alt data
    SEARCH_QUERIES = {
        "google_trends": "Google Trends {keyword} interest over time",
        "baltic_dry": "Baltic Dry Index today shipping",
        "economic_surprise": "Citigroup Economic Surprise Index",
        "credit_spreads": "US high yield credit spread OAS today",
        "copper_gold_ratio": "copper gold ratio economic indicator",
        "shipping_rates": "container shipping rates index",
        "job_postings": "Indeed job postings trend {country}",
        "restaurant_bookings": "OpenTable restaurant bookings trend",
        "electricity_consumption": "electricity consumption {country} trend",
    }

    @staticmethod
    def google_trends_signal(trend_data: pd.Series, asset: str) -> dict:
        """Process Google Trends data into trading signal.
        Rising search interest often leads price moves by 1-4 weeks."""
        if len(trend_data) < 10:
            return {"error": "Need at least 10 data points"}
        momentum = trend_data.pct_change(4).iloc[-1]  # 4-week momentum
        z_score = (trend_data.iloc[-1] - trend_data.rolling(52).mean().iloc[-1]) / (trend_data.rolling(52).std().iloc[-1] or 1)
        return {
            "asset": asset,
            "current_interest": int(trend_data.iloc[-1]),
            "4w_momentum": round(momentum * 100, 1),
            "z_score": round(z_score, 2),
            "signal": "ELEVATED ATTENTION — potential move incoming" if abs(z_score) > 2 else "NORMAL",
            "note": "Google Trends leads retail flows by 1-4 weeks. Contrarian at extremes.",
        }

    @staticmethod
    def economic_nowcast(indicators: dict) -> dict:
        """Combine real-time indicators for economic activity nowcast."""
        scores = {
            "baltic_dry_change": indicators.get("baltic_dry_mom", 0) * 0.15,
            "credit_spread_change": -indicators.get("credit_spread_change", 0) * 0.20,
            "copper_gold_ratio_change": indicators.get("copper_gold_mom", 0) * 0.20,
            "job_postings_change": indicators.get("job_postings_mom", 0) * 0.15,
            "electricity_change": indicators.get("electricity_mom", 0) * 0.10,
            "shipping_rates_change": indicators.get("shipping_mom", 0) * 0.10,
            "consumer_traffic_change": indicators.get("consumer_traffic_mom", 0) * 0.10,
        }
        composite = sum(scores.values())
        return {
            "nowcast_score": round(composite, 4),
            "components": scores,
            "regime": "EXPANSION" if composite > 0.02 else "CONTRACTION" if composite < -0.02 else "STABLE",
            "fx_implication": "Risk-on currencies favored (AUD, NZD, CAD)" if composite > 0.02
                            else "Risk-off currencies favored (JPY, CHF, USD)" if composite < -0.02
                            else "Mixed — trade pair-specific fundamentals",
        }

    @staticmethod
    def sentiment_from_search_volume(keywords: dict) -> dict:
        """Map search volume patterns to market sentiment."""
        fear_keywords = ["recession", "market crash", "financial crisis", "bank run"]
        greed_keywords = ["bull market", "stock tips", "get rich", "crypto moon"]
        fear_score = sum(keywords.get(k, 0) for k in fear_keywords)
        greed_score = sum(keywords.get(k, 0) for k in greed_keywords)
        net = greed_score - fear_score
        return {
            "fear_index": fear_score,
            "greed_index": greed_score,
            "net_sentiment": round(net, 2),
            "interpretation": "FEAR dominant — contrarian buy signal" if net < -50
                            else "GREED dominant — contrarian sell signal" if net > 50
                            else "BALANCED",
        }
```
