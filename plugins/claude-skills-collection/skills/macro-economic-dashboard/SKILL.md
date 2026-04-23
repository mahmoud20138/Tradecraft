---
name: macro-economic-dashboard
description: >
  Macro economic inter-market analysis dashboard — DXY, VIX, yield curves, bond spreads,
  commodity flows, and cross-asset correlations. Use this skill whenever the user asks about
  "DXY", "dollar index", "VIX", "volatility index", "yield curve", "bond yields", "10-year",
  "2-10 spread", "yield inversion", "risk on risk off", "inter-market", "commodity flows",
  "gold vs dollar", "oil vs CAD", "equities vs forex", "macro overview", "big picture",
  "cross-asset", "safe havens", or any macro-level inter-market relationship analysis.
  This is the macro context layer that sits above pair-level analysis.
kind: reference
category: trading/market-context
status: active
tags: [correlation, dashboard, economic, forex, ict, macro, market-context, risk-and-portfolio]
related_skills: [institutional-timeline, market-breadth-analyzer, market-regime-classifier]
---

# Macro Economic Dashboard

## Overview
Maps the macro landscape across asset classes — currencies, bonds, equities, commodities.
Identifies risk-on/risk-off conditions, yield curve signals, and cross-asset divergences
that drive currency trends.

---

## 1. Key Macro Instruments

```python
MACRO_INSTRUMENTS = {
    "dollar": {
        "DXY": {"description": "US Dollar Index", "impact": "USD strength gauge"},
    },
    "volatility": {
        "VIX": {"description": "CBOE Volatility Index", "impact": "Fear gauge — high VIX = risk-off"},
    },
    "bonds": {
        "US10Y": {"description": "US 10-Year Treasury Yield"},
        "US02Y": {"description": "US 2-Year Treasury Yield"},
        "US30Y": {"description": "US 30-Year Treasury Yield"},
        "DE10Y": {"description": "German 10-Year Bund Yield"},
        "JP10Y": {"description": "Japan 10-Year JGB Yield"},
        "UK10Y": {"description": "UK 10-Year Gilt Yield"},
    },
    "commodities": {
        "XAUUSD": {"description": "Gold", "impact": "Safe haven, inverse USD"},
        "XAGUSD": {"description": "Silver", "impact": "Industrial + precious"},
        "WTI": {"description": "Crude Oil", "impact": "CAD, NOK, RUB driver"},
        "BRENT": {"description": "Brent Crude", "impact": "Global energy benchmark"},
    },
    "equity_indices": {
        "SPX": {"description": "S&P 500", "impact": "US risk appetite"},
        "NDX": {"description": "Nasdaq 100", "impact": "Tech/growth sentiment"},
        "DAX": {"description": "German DAX", "impact": "EU risk appetite"},
        "NI225": {"description": "Nikkei 225", "impact": "JPY flows"},
    },
}
```

---

## 2. Inter-Market Relationship Engine

```python
import pandas as pd
import numpy as np

INTER_MARKET_RULES = [
    {"condition": "DXY rising", "effect": "EURUSD falls, GBPUSD falls, Gold falls", "reliability": 0.85},
    {"condition": "DXY falling", "effect": "EURUSD rises, GBPUSD rises, Gold rises", "reliability": 0.85},
    {"condition": "VIX > 25", "effect": "Risk-off: JPY, CHF, Gold rise; AUD, NZD fall", "reliability": 0.80},
    {"condition": "VIX < 15", "effect": "Risk-on: AUD, NZD rise; JPY, CHF fall", "reliability": 0.75},
    {"condition": "US10Y rising", "effect": "USD tends to strengthen, Gold weakens", "reliability": 0.70},
    {"condition": "US10Y falling", "effect": "USD may weaken, Gold strengthens", "reliability": 0.65},
    {"condition": "2-10 spread inverting", "effect": "Recession signal — risk-off ahead", "reliability": 0.60},
    {"condition": "Oil rising sharply", "effect": "CAD strengthens, inflation fears, JPY weakens", "reliability": 0.70},
    {"condition": "Oil falling sharply", "effect": "CAD weakens, deflation signal", "reliability": 0.70},
    {"condition": "SPX + Gold both rising", "effect": "Liquidity expansion — everything bid", "reliability": 0.55},
    {"condition": "SPX falling + Gold rising", "effect": "Classic risk-off rotation", "reliability": 0.80},
    {"condition": "SPX falling + Gold falling", "effect": "Liquidity crisis — cash is king", "reliability": 0.75}]

class MacroDashboard:
    """Analyze macro conditions and their FX implications."""

    @staticmethod
    def risk_regime(vix: float, spx_change: float, gold_change: float, dxy_change: float) -> dict:
        """Classify current risk environment."""
        if vix > 30 and spx_change < -0.5:
            regime = "RISK-OFF EXTREME"
            fx_impact = "JPY, CHF surge. AUD, NZD, EM currencies under pressure."
        elif vix > 20 and spx_change < 0:
            regime = "RISK-OFF"
            fx_impact = "JPY, CHF firm. AUD, NZD soft. USD mixed (safe haven but rates)."
        elif vix < 15 and spx_change > 0:
            regime = "RISK-ON"
            fx_impact = "AUD, NZD, EM strong. JPY, CHF weak. Carry trades favored."
        elif vix < 12:
            regime = "COMPLACENT"
            fx_impact = "Low vol environment. Carry works. Watch for vol spike reversal."
        else:
            regime = "NEUTRAL"
            fx_impact = "Mixed signals. Trade on pair-specific fundamentals."

        return {
            "regime": regime,
            "vix": vix,
            "fx_impact": fx_impact,
            "safe_haven_flow": vix > 20,
            "carry_environment": vix < 18 and spx_change > 0,
        }

    @staticmethod
    def yield_curve_analysis(us2y: float, us10y: float, us30y: float) -> dict:
        """Analyze US yield curve for economic signals."""
        spread_2_10 = us10y - us2y
        spread_10_30 = us30y - us10y

        if spread_2_10 < 0:
            curve_state = "INVERTED"
            signal = "Recession warning — historically leads recession by 6-18 months"
        elif spread_2_10 < 0.25:
            curve_state = "FLAT"
            signal = "Slowdown signal — economy losing momentum"
        elif spread_2_10 > 1.5:
            curve_state = "STEEP"
            signal = "Growth signal — economy expanding, rates expected to rise"
        else:
            curve_state = "NORMAL"
            signal = "Healthy curve — no extreme signal"

        return {
            "curve_state": curve_state,
            "spread_2_10": round(spread_2_10, 3),
            "spread_10_30": round(spread_10_30, 3),
            "signal": signal,
            "us2y": us2y, "us10y": us10y, "us30y": us30y,
            "fx_implications": {
                "INVERTED": "USD may weaken medium-term. Safe havens favored.",
                "STEEP": "USD may strengthen on growth. Risk-on currencies favored.",
                "FLAT": "Uncertainty. Range-bound FX likely.",
                "NORMAL": "Fundamentals-driven. Follow rate differentials.",
            }.get(curve_state, ""),
        }

    @staticmethod
    def dollar_regime(dxy_current: float, dxy_sma50: float, dxy_sma200: float) -> dict:
        """Classify USD regime from DXY."""
        if dxy_current > dxy_sma50 > dxy_sma200:
            return {"regime": "STRONG DOLLAR", "bias": "USD bullish — sell EURUSD, GBPUSD. Buy USDJPY.",
                    "trend": "uptrend", "dxy": dxy_current}
        elif dxy_current < dxy_sma50 < dxy_sma200:
            return {"regime": "WEAK DOLLAR", "bias": "USD bearish — buy EURUSD, GBPUSD. Sell USDJPY.",
                    "trend": "downtrend", "dxy": dxy_current}
        return {"regime": "MIXED DOLLAR", "bias": "No clear USD trend. Trade cross-pairs.",
                "trend": "sideways", "dxy": dxy_current}

    @staticmethod
    def commodity_fx_links(oil_change: float, gold_change: float) -> dict:
        """Map commodity moves to currency implications."""
        links = []
        if abs(oil_change) > 1:
            direction = "rising" if oil_change > 0 else "falling"
            links.append({
                "commodity": "Oil",
                "move": f"{direction} ({oil_change:+.1f}%)",
                "fx_impact": f"CAD {'strengthens' if oil_change > 0 else 'weakens'} — "
                            f"{'buy' if oil_change > 0 else 'sell'} USDCAD",
            })
        if abs(gold_change) > 0.5:
            direction = "rising" if gold_change > 0 else "falling"
            links.append({
                "commodity": "Gold",
                "move": f"{direction} ({gold_change:+.1f}%)",
                "fx_impact": f"Safe haven {'bid' if gold_change > 0 else 'offered'} — "
                            f"AUD {'supported' if gold_change > 0 else 'pressured'} (gold exporter)",
            })
        return {"links": links, "rules_checked": len(INTER_MARKET_RULES)}
```

---

## Web Search Queries for Real-Time Data
```
web_search("DXY dollar index today")
web_search("VIX index current level")
web_search("US 10 year treasury yield today")
web_search("US 2-10 yield curve spread")
web_search("oil price WTI today")
web_search("S&P 500 today risk sentiment")
```
