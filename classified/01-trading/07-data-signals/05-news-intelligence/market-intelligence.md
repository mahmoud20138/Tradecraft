---
name: market-intelligence
description: >
  Complete market intelligence layer — macro analysis, regime classification, news impact, sentiment,
  institutional behavior, event timelines, pair correlations, and trading fundamentals.
  Includes NLP sentiment scoring, news straddle strategies, COT positioning, seasonality analysis,
  contrarian sentiment composites, economic indicator tracking, and event timeline linking.

  MACRO & INTERMARKET: "DXY", "dollar index", "VIX", "volatility index", "yield curve",
  "bond yields", "10-year", "2-10 spread", "yield inversion", "risk on risk off", "inter-market",
  "commodity flows", "gold vs dollar", "oil vs CAD", "equities vs forex", "macro overview",
  "big picture", "cross-asset", "safe havens", "intermarket divergence", "gold dollar divergence",
  "oil CAD divergence", "bond equity divergence", "cross-market divergence", "asset class divergence".

  REGIME CLASSIFICATION: "is the market trending", "what regime are we in", "ranging or trending",
  "market conditions", "volatility regime", "classify market state", "adapt strategy",
  "regime change", "market phase", "consolidation or breakout", "trending market detection".

  NEWS & EVENTS: "what news is moving the market", "why did EURUSD drop", "upcoming events",
  "news impact on gold", "Fed decision impact", "ECB hawkish dovish", "central bank decision",
  "NFP", "CPI", "GDP", "economic calendar", "geopolitical risk", "market sentiment",
  "news blackout", "event impact", "surprise reading", "above below expectations".

  SENTIMENT & POSITIONING: "market sentiment", "what are traders saying", "retail positioning",
  "Fear and Greed Index", "crowd sentiment", "contrarian signal", "Twitter sentiment",
  "Reddit WallStreetBets", "social media trading", "TradingView ideas", "bullish bearish crowd",
  "retail long short ratio", "IG client sentiment", "Myfxbook sentiment", "COT strategy",
  "commitment of traders", "speculative positioning", "commercial hedgers", "COT signal",
  "contrarian trade", "fade the crowd", "retail is wrong", "extreme sentiment".

  INSTITUTIONAL BEHAVIOR: "what are banks doing", "institutional positioning", "central bank policy",
  "Fed hawkish dovish", "ECB stance", "bank forecasts", "smart money", "institutional flows",
  "Goldman Sachs view", "JPMorgan forecast", "hedge fund positioning", "bank intervention",
  "reserve changes", "monetary policy impact", "dealer positioning", "rate decision impact",
  "policy divergence", "intervention detection".

  EVENT TIMELINE: "what happened when", "why did the market move", "connect the dots",
  "timeline of events", "what caused this price move", "link news to price action",
  "temporal analysis", "event chain", "cause and effect", "reconstruct what happened on date",
  "what will happen next based on history", "correlate events".

  PAIR CORRELATIONS: "correlate EURUSD and GBPUSD", "which pairs move together",
  "find divergences", "correlation matrix", "historical vs current correlation",
  "correlation breakdown", "hedging pairs", "pair clustering", "correlation regime change",
  "adaptive strategy switching", "when correlations break", "correlation spike", "decorrelation",
  "dynamic strategy switching", "auto-switch strategy", "transition detector".

  TRADING FUNDAMENTALS: "explain market structure", "what is a market order", "types of orders",
  "limit order vs stop order", "iceberg order", "TWAP VWAP orders", "asset classes",
  "scalping vs day trading vs swing trading", "trading timeframes", "market participants",
  "market microstructure", "tick size", "lot size", "price discovery", "OTC market".

  ALTERNATIVE DATA: "alternative data", "Google Trends trading", "search trends",
  "web traffic signals", "nowcasting", "satellite data trading", "shipping index",
  "Baltic Dry", "unusual data sources", "non-traditional indicators",
  "big data trading signals", incorporate non-standard data into trading decisions.

  SEASONALITY: "seasonality", "monthly patterns", "best month to trade",
  "day of week edge", "hour of day analysis", "seasonal tendencies", "January effect",
  "sell in May", "summer doldrums", "end of quarter", "seasonal patterns forex",
  "when does EURUSD perform best", calendar-based statistical analysis.

  DO NOT USE FOR: ICT-specific analysis (use ict-smart-money), specific strategy entry/exit
  (use trading-strategies), risk position sizing (use risk-and-portfolio), chart patterns
  (use technical-analysis).
related_skills:
  - fundamental-analysis
  - social-sentiment-scraper
  - news-intelligence
  - economic-calendar
tags:
  - trading
  - research
  - macro
  - news
  - regime
  - intelligence
skill_level: intermediate
kind: reference
category: trading/data
status: active
---
> **Skill:** Market Intelligence  |  **Domain:** trading  |  **Category:** research  |  **Level:** intermediate
> **Tags:** `trading`, `research`, `macro`, `news`, `regime`, `intelligence`


# Market Intelligence — Complete Analysis Layer

> The informational foundation of all trading decisions.
> Macro context → regime → news → sentiment → institutional → correlation → execute.

## Sections

1. **Macro Dashboard** — DXY, VIX, yield curves, commodity-FX links, intermarket divergence
2. **Regime Classifier** — trending/ranging/volatile/quiet + strategy mapping
3. **News & Events** — economic calendar, impact scoring, event-price matching, sentiment
4. **Sentiment & Positioning** — retail positioning, COT, Fear/Greed, contrarian signals
5. **Institutional Monitor** — central banks, investment banks, COT analysis, intervention detection
6. **Event Timeline** — event linking, causal chains, narrative building, prediction
7. **Pair Correlations** — rolling correlation, divergence detection, clustering, regime switching
8. **Trading Fundamentals** — market structure, order types, asset classes, timeframes
9. **Alternative Data** — Google Trends signals, economic nowcasting, shipping/supply chain, search sentiment
10. **Seasonality** — monthly/day-of-week/hourly statistical edges with significance testing

---

## Reference Files

- **[references/macro-regime.md](references/macro-regime.md)** — Macro dashboard (DXY/VIX/yield curves/commodities) + regime classifier (ADX/BB-width/MA-alignment + strategy map)
- **[references/news-sentiment.md](references/news-sentiment.md)** — Economic calendar, news impact scoring, event-price matching, retail sentiment, COT, Fear/Greed, contrarian composite
- **[references/institutional-timeline.md](references/institutional-timeline.md)** — Central bank tracker, policy divergence, investment bank monitor, COT analyzer, intervention detector + full event timeline linker
- **[references/correlation-fundamentals.md](references/correlation-fundamentals.md)** — Pair correlation engine (rolling/historical/divergence/clustering/lead-lag) + correlation regime switcher + trading fundamentals reference
- **[references/alternative-data.md](references/alternative-data.md)** — AlternativeDataSources class: Google Trends signal, economic nowcast (Baltic Dry/copper-gold/credit spreads), search volume sentiment mapping
- **[references/seasonality.md](references/seasonality.md)** — SeasonalityAnalyzer class: monthly/day-of-week/hourly return statistics with t-tests, p-values, win rates, and significance flags

## Quick Decision Guide

| Task | Load |
|------|------|
| Is market risk-on or risk-off? | `references/macro-regime.md` |
| What does the yield curve signal? | `references/macro-regime.md` |
| Gold/Oil divergence from DXY? | `references/macro-regime.md` |
| What regime is EURUSD in? | `references/macro-regime.md` |
| Which strategy type fits now? | `references/macro-regime.md` |
| What events are this week? | `references/news-sentiment.md` |
| Is crowd long or short? | `references/news-sentiment.md` |
| COT extreme positioning? | `references/news-sentiment.md` |
| What is the Fed/ECB doing? | `references/institutional-timeline.md` |
| Rate decision impact model | `references/institutional-timeline.md` |
| Policy divergence between banks | `references/institutional-timeline.md` |
| Why did price move on [date]? | `references/institutional-timeline.md` |
| Which pairs are correlated? | `references/correlation-fundamentals.md` |
| Correlation regime shift? | `references/correlation-fundamentals.md` |
| What strategy works now (regime)? | `references/correlation-fundamentals.md` |
| What is a limit order / TWAP? | `references/correlation-fundamentals.md` |
| Google Trends signal / nowcast? | `references/alternative-data.md` |
| Baltic Dry / shipping index signal? | `references/alternative-data.md` |
| Search volume sentiment (fear/greed)? | `references/alternative-data.md` |
| Best month / day / hour to trade? | `references/seasonality.md` |
| January effect / sell in May? | `references/seasonality.md` |
| Seasonal edge with significance test? | `references/seasonality.md` |

## Core Macro Intelligence Quick Card

```
RISK-ON:   VIX < 15, SPX rising → AUD, NZD up | JPY, CHF, Gold down
RISK-OFF:  VIX > 25, SPX falling → JPY, CHF, Gold up | AUD, NZD, EM down
DXY UP:    EUR, GBP, Gold down | USDJPY, USDCAD up
DXY DOWN:  EUR, GBP, Gold up | USDJPY, USDCAD down
YIELD ↑:   USD strengthens, Gold weakens
YIELD INVERSION (2-10 < 0): Recession warning, risk-off ahead
OIL ↑:     CAD, NOK strengthen
TREND REGIME:  ADX > 25, MAs aligned → use trend following
RANGE REGIME:  ADX < 20, BB narrow → use mean reversion
VOLATILE:  ADX < 20, BB wide → reduce size, wait for clarity
```

---

## Implementations (Merged from sentiment-macro)

---

## News Sentiment NLP Engine

```python
import re, numpy as np
SENTIMENT_LEXICON = {
    "hawkish": 0.8, "dovish": -0.8, "rate hike": 0.7, "rate cut": -0.7,
    "inflation rises": 0.5, "inflation falls": -0.3, "recession": -0.8,
    "strong jobs": 0.6, "weak jobs": -0.6, "stimulus": 0.5, "tightening": 0.4,
    "crisis": -0.9, "default": -0.9, "war": -0.7, "peace": 0.3,
    "surge": 0.6, "plunge": -0.7, "rally": 0.5, "crash": -0.8,
    "beat expectations": 0.6, "miss expectations": -0.6, "surprise": 0.3,
    "upgrade": 0.5, "downgrade": -0.5, "bullish": 0.5, "bearish": -0.5,
}
class NewsSentimentNLP:
    @staticmethod
    def score_headline(headline: str) -> dict:
        h = headline.lower()
        matched = [(kw, score) for kw, score in SENTIMENT_LEXICON.items() if kw in h]
        avg = np.mean([s for _, s in matched]) if matched else 0
        entities = re.findall(r"\b(Fed|ECB|BOE|BOJ|NFP|CPI|GDP|FOMC|IMF)\b", headline, re.IGNORECASE)
        return {
            "headline": headline,
            "sentiment_score": round(avg, 3),
            "label": "BULLISH" if avg > 0.2 else "BEARISH" if avg < -0.2 else "NEUTRAL",
            "matched_keywords": [kw for kw, _ in matched],
            "entities": entities,
            "confidence": min(len(matched) / 3, 1.0),
        }
    @staticmethod
    def batch_score(headlines: list) -> dict:
        scores = [NewsSentimentNLP.score_headline(h) for h in headlines]
        avg = np.mean([s["sentiment_score"] for s in scores])
        return {"overall": round(avg, 3), "n_headlines": len(headlines),
                "bullish": sum(1 for s in scores if s["label"] == "BULLISH"),
                "bearish": sum(1 for s in scores if s["label"] == "BEARISH")}
```

---

## Market News Impact

### Overview
Monitors and analyzes major economic news, central bank decisions, geopolitical events,
and market-moving developments. Matches news events to price reactions across instruments.
Provides forward-looking event calendars with expected impact ratings.

### Architecture

```
┌───────────────────────────────────────────────────────────┐
│                Market News Impact Engine                   │
├──────────────┬───────────────┬───────────────┬────────────┤
│ News Fetcher │ Event Calendar│ Impact Matcher│ Sentiment  │
│ & Classifier │ & Scheduler   │ & Scorer      │ Analyzer   │
└──────────────┴───────────────┴───────────────┴────────────┘
```

### 1. News Source Architecture

#### Source Priority (highest quality first)
```python
NEWS_SOURCES = {
    "central_banks": {
        "fed":  {"url": "https://www.federalreserve.gov/newsevents.htm", "priority": 1},
        "ecb":  {"url": "https://www.ecb.europa.eu/press/html/index.en.html", "priority": 1},
        "boj":  {"url": "https://www.boj.or.jp/en/", "priority": 1},
        "boe":  {"url": "https://www.bankofengland.co.uk/news", "priority": 1},
        "rba":  {"url": "https://www.rba.gov.au/media-releases/", "priority": 1},
        "snb":  {"url": "https://www.snb.ch/en/", "priority": 1},
        "boc":  {"url": "https://www.bankofcanada.ca/press/", "priority": 1},
        "rbnz": {"url": "https://www.rbnz.govt.nz/news", "priority": 1},
    },
    "economic_data": {
        "forexfactory":  {"url": "https://www.forexfactory.com/calendar", "priority": 1},
        "investing_com":  {"url": "https://www.investing.com/economic-calendar/", "priority": 2},
        "tradingeconomics": {"url": "https://tradingeconomics.com/calendar", "priority": 2},
    },
    "financial_news": {
        "reuters":    {"url": "https://www.reuters.com/markets/", "priority": 1},
        "bloomberg":  {"url": "https://www.bloomberg.com/markets", "priority": 1},
        "wsj":        {"url": "https://www.wsj.com/news/markets", "priority": 2},
        "ft":         {"url": "https://www.ft.com/markets", "priority": 2},
        "cnbc":       {"url": "https://www.cnbc.com/world-markets/", "priority": 3},
    },
    "geopolitical": {
        "reuters_world": {"url": "https://www.reuters.com/world/", "priority": 1},
        "bbc_world":     {"url": "https://www.bbc.com/news/world", "priority": 2},
    },
}
```

#### News Fetching Framework
```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from typing import Optional
import json

class NewsFetcher:
    """
    Fetch and classify market-moving news from multiple sources.
    In Claude context: use web_search tool as the primary fetcher.
    """

    # Impact classification keywords
    HIGH_IMPACT_KEYWORDS = [
        "rate decision", "interest rate", "nfp", "non-farm", "cpi", "inflation",
        "gdp", "fomc", "fed chair", "ecb president", "quantitative",
        "emergency", "war", "sanctions", "default", "recession", "crisis",
        "tariff", "trade war", "stimulus", "bailout"]
    MEDIUM_IMPACT_KEYWORDS = [
        "pmi", "employment", "retail sales", "housing", "trade balance",
        "industrial production", "consumer confidence", "jobless claims",
        "manufacturing", "services", "earnings", "ism"]

    @staticmethod
    def classify_impact(headline: str) -> str:
        """Classify a headline into impact level."""
        h = headline.lower()
        if any(kw in h for kw in NewsFetcher.HIGH_IMPACT_KEYWORDS):
            return "HIGH"
        if any(kw in h for kw in NewsFetcher.MEDIUM_IMPACT_KEYWORDS):
            return "MEDIUM"
        return "LOW"

    @staticmethod
    def extract_affected_currencies(headline: str) -> list[str]:
        """Extract which currencies are likely affected by a headline."""
        currency_map = {
            "fed": ["USD"], "fomc": ["USD"], "nfp": ["USD"], "us ": ["USD"],
            "ecb": ["EUR"], "euro": ["EUR"], "eurozone": ["EUR"],
            "boe": ["GBP"], "uk ": ["GBP"], "britain": ["GBP"], "sterling": ["GBP"],
            "boj": ["JPY"], "japan": ["JPY"], "yen": ["JPY"],
            "rba": ["AUD"], "australia": ["AUD"],
            "boc": ["CAD"], "canada": ["CAD"],
            "snb": ["CHF"], "swiss": ["CHF"],
            "rbnz": ["NZD"], "zealand": ["NZD"],
            "china": ["CNH", "AUD", "NZD"], "oil": ["CAD", "NOK"],
            "gold": ["XAU", "AUD"], "bitcoin": ["BTC"], "crypto": ["BTC", "ETH"],
        }
        h = headline.lower()
        affected = set()
        for trigger, currencies in currency_map.items():
            if trigger in h:
                affected.update(currencies)
        return list(affected) if affected else ["BROAD"]

    @staticmethod
    def map_to_pairs(currencies: list[str]) -> list[str]:
        """Map affected currencies to specific tradeable pairs."""
        major_pairs = {
            "USD": ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"],
            "EUR": ["EURUSD", "EURJPY", "EURGBP", "EURAUD", "EURCHF"],
            "GBP": ["GBPUSD", "EURGBP", "GBPJPY", "GBPAUD"],
            "JPY": ["USDJPY", "EURJPY", "GBPJPY", "AUDJPY"],
            "AUD": ["AUDUSD", "EURAUD", "GBPAUD", "AUDJPY", "AUDNZD"],
            "CAD": ["USDCAD", "CADCHF", "CADJPY"],
            "CHF": ["USDCHF", "EURCHF", "GBPCHF"],
            "NZD": ["NZDUSD", "AUDNZD", "NZDJPY"],
            "XAU": ["XAUUSD"],
            "BTC": ["BTCUSD"],
        }
        pairs = set()
        for c in currencies:
            pairs.update(major_pairs.get(c, []))
        return list(pairs)
```

### 2. Economic Calendar Engine

```python
# Standard economic calendar event structure
EVENT_IMPACT_MAP = {
    # USD events
    "Non-Farm Payrolls":         {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 3.0},
    "FOMC Rate Decision":        {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 4.0},
    "FOMC Press Conference":     {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 3.5},
    "CPI m/m":                   {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 2.5},
    "CPI y/y":                   {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 2.5},
    "Core CPI":                  {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 2.5},
    "GDP q/q":                   {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 2.0},
    "Unemployment Rate":         {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 2.0},
    "ISM Manufacturing PMI":     {"impact": "MEDIUM", "currencies": ["USD"], "volatility_multiplier": 1.5},
    "ISM Services PMI":          {"impact": "MEDIUM", "currencies": ["USD"], "volatility_multiplier": 1.5},
    "Retail Sales":              {"impact": "MEDIUM", "currencies": ["USD"], "volatility_multiplier": 1.5},
    "Initial Jobless Claims":    {"impact": "MEDIUM", "currencies": ["USD"], "volatility_multiplier": 1.2},
    "Fed Chair Speech":          {"impact": "HIGH", "currencies": ["USD"], "volatility_multiplier": 3.0},
    # EUR events
    "ECB Rate Decision":         {"impact": "HIGH", "currencies": ["EUR"], "volatility_multiplier": 4.0},
    "ECB Press Conference":      {"impact": "HIGH", "currencies": ["EUR"], "volatility_multiplier": 3.5},
    "Eurozone CPI":              {"impact": "HIGH", "currencies": ["EUR"], "volatility_multiplier": 2.0},
    "German Manufacturing PMI":  {"impact": "MEDIUM", "currencies": ["EUR"], "volatility_multiplier": 1.3},
    # GBP events
    "BOE Rate Decision":         {"impact": "HIGH", "currencies": ["GBP"], "volatility_multiplier": 4.0},
    "UK CPI":                    {"impact": "HIGH", "currencies": ["GBP"], "volatility_multiplier": 2.0},
    # JPY events
    "BOJ Rate Decision":         {"impact": "HIGH", "currencies": ["JPY"], "volatility_multiplier": 4.0},
    "Japan CPI":                 {"impact": "MEDIUM", "currencies": ["JPY"], "volatility_multiplier": 1.5},
}

class EconomicCalendar:
    """Structured economic calendar with impact ratings and pair mapping."""

    def __init__(self):
        self.events = []

    def add_event(self, name: str, dt: datetime, actual: Optional[float] = None,
                  forecast: Optional[float] = None, previous: Optional[float] = None) -> dict:
        meta = EVENT_IMPACT_MAP.get(name, {"impact": "LOW", "currencies": ["BROAD"], "volatility_multiplier": 1.0})
        event = {
            "name": name,
            "datetime": dt.isoformat(),
            "actual": actual,
            "forecast": forecast,
            "previous": previous,
            "surprise": (actual - forecast) if actual is not None and forecast is not None else None,
            "impact": meta["impact"],
            "currencies": meta["currencies"],
            "affected_pairs": NewsFetcher.map_to_pairs(meta["currencies"]),
            "volatility_multiplier": meta["volatility_multiplier"],
        }
        self.events.append(event)
        return event

    def get_upcoming(self, hours: int = 24, impact_filter: Optional[str] = None) -> list[dict]:
        """Get events in the next N hours, optionally filtered by impact."""
        cutoff = datetime.utcnow() + timedelta(hours=hours)
        upcoming = [e for e in self.events if datetime.fromisoformat(e["datetime"]) <= cutoff]
        if impact_filter:
            upcoming = [e for e in upcoming if e["impact"] == impact_filter.upper()]
        return sorted(upcoming, key=lambda x: x["datetime"])

    def get_events_for_pair(self, pair: str) -> list[dict]:
        """All events affecting a specific pair."""
        return [e for e in self.events if pair.upper() in e["affected_pairs"]]
```

### 3. Price Impact Matching

```python
def measure_event_impact(
    df: pd.DataFrame,
    event_time: datetime,
    pre_window_bars: int = 5,
    post_window_bars: int = 20,
) -> dict:
    """
    Measure price reaction around a specific event.
    Returns: pre-event range, immediate reaction, sustained move, retracement.
    """
    # Find nearest bar to event time
    idx = df.index.searchsorted(event_time)
    if idx < pre_window_bars or idx + post_window_bars > len(df):
        return {"error": "Insufficient data around event"}

    pre = df.iloc[idx - pre_window_bars:idx]
    post = df.iloc[idx:idx + post_window_bars]
    event_bar = df.iloc[idx]

    pre_range = pre["high"].max() - pre["low"].min()
    immediate_move = event_bar["close"] - pre.iloc[-1]["close"]
    max_post_move = post["high"].max() - pre.iloc[-1]["close"]
    min_post_move = post["low"].min() - pre.iloc[-1]["close"]
    sustained_move = post.iloc[-1]["close"] - pre.iloc[-1]["close"]

    return {
        "event_time": event_time.isoformat(),
        "pre_event_range": round(pre_range, 5),
        "immediate_move_pips": round(immediate_move / df.attrs.get("point", 0.0001), 1),
        "max_favorable": round(max_post_move / df.attrs.get("point", 0.0001), 1),
        "max_adverse": round(min_post_move / df.attrs.get("point", 0.0001), 1),
        "sustained_move_pips": round(sustained_move / df.attrs.get("point", 0.0001), 1),
        "retracement_pct": round(1 - abs(sustained_move) / max(abs(max_post_move), abs(min_post_move), 1e-10), 3),
        "direction": "bullish" if sustained_move > 0 else "bearish",
        "volatility_expansion": round(post["high"].max() - post["low"].min(), 5) / max(pre_range, 1e-10),
    }

def historical_event_impact_study(
    df: pd.DataFrame,
    events: list[dict],
    post_window: int = 20,
) -> pd.DataFrame:
    """
    Analyze price reaction across multiple historical occurrences of an event.
    Builds a statistical profile of how a pair reacts to a specific event type.
    """
    results = []
    for event in events:
        try:
            impact = measure_event_impact(df, datetime.fromisoformat(event["datetime"]), post_window_bars=post_window)
            impact["event_name"] = event["name"]
            impact["surprise"] = event.get("surprise")
            results.append(impact)
        except Exception:
            continue
    return pd.DataFrame(results)
```

### 4. Sentiment Analysis Framework

```python
SENTIMENT_KEYWORDS = {
    "hawkish": +1.0, "tightening": +0.8, "rate hike": +0.9, "inflation concerns": +0.5,
    "strong employment": +0.5, "above expectations": +0.6,
    "dovish": -1.0, "easing": -0.8, "rate cut": -0.9, "slowdown": -0.5,
    "recession fears": -0.7, "below expectations": -0.6, "miss": -0.5,
    "risk on": +0.3, "rally": +0.4, "bullish": +0.5, "upgrade": +0.4,
    "risk off": -0.3, "sell-off": -0.5, "bearish": -0.5, "downgrade": -0.4,
    "uncertainty": -0.2, "volatile": -0.1, "crisis": -0.8, "default": -0.9,
    "stimulus": +0.6, "infrastructure": +0.3, "trade deal": +0.4,
    "sanctions": -0.4, "tariff": -0.3, "war": -0.8,
}

def score_sentiment(text: str) -> dict:
    """Quick keyword-based sentiment score for a news headline or summary."""
    text_lower = text.lower()
    scores = []
    matched = []
    for keyword, score in SENTIMENT_KEYWORDS.items():
        if keyword in text_lower:
            scores.append(score)
            matched.append(keyword)
    avg = np.mean(scores) if scores else 0.0
    return {
        "sentiment_score": round(avg, 3),
        "label": "BULLISH" if avg > 0.2 else "BEARISH" if avg < -0.2 else "NEUTRAL",
        "matched_keywords": matched,
        "confidence": min(len(matched) / 3, 1.0),
    }

def aggregate_sentiment(headlines: list[str]) -> dict:
    """Aggregate sentiment across multiple headlines."""
    scores = [score_sentiment(h) for h in headlines]
    avg_score = np.mean([s["sentiment_score"] for s in scores])
    return {
        "overall_score": round(avg_score, 3),
        "overall_label": "BULLISH" if avg_score > 0.15 else "BEARISH" if avg_score < -0.15 else "NEUTRAL",
        "n_headlines": len(headlines),
        "bullish_count": sum(1 for s in scores if s["label"] == "BULLISH"),
        "bearish_count": sum(1 for s in scores if s["label"] == "BEARISH"),
        "neutral_count": sum(1 for s in scores if s["label"] == "NEUTRAL"),
    }
```

### 5. Usage with Claude's Web Search

When this skill is active in Claude, the primary data acquisition method is **web_search**:

```
# Fetch current market news
web_search("forex market news today major events")
web_search("FOMC rate decision 2025")
web_search("forex factory economic calendar this week")
web_search("Reuters forex market analysis")

# Fetch specific event impact
web_search("NFP non-farm payrolls result today")
web_search("ECB interest rate decision impact EURUSD")

# Geopolitical
web_search("geopolitical risk forex markets today")
web_search("US China trade tensions impact currencies")
```

Then pipe fetched content through `classify_impact()`, `extract_affected_currencies()`, and
`score_sentiment()` to produce structured, actionable output.

### Integration Points

| Skill | Data Exchanged |
|---|---|
| `mt5-chart-browser` | Price data around events for impact measurement |
| `event-timeline-linker` | Timestamped events for temporal correlation |
| `institutional-behavior-monitor` | Central bank decisions and positioning |
| `trading-brain` | News alerts and sentiment reports |

---

## News Straddle Strategy

```python
import pandas as pd, numpy as np

class NewsStraddleStrategy:

    @staticmethod
    def pre_news_straddle(current_price: float, atr: float, spread_pips: float) -> dict:
        """Place pending orders both sides before high-impact news."""
        buffer = atr * 0.5
        return {
            "strategy": "pre_news_straddle",
            "buy_stop": round(current_price + buffer, 5),
            "sell_stop": round(current_price - buffer, 5),
            "buy_sl": round(current_price, 5),
            "sell_sl": round(current_price, 5),
            "buy_tp": round(current_price + buffer + atr * 2, 5),
            "sell_tp": round(current_price - buffer - atr * 2, 5),
            "timing": "Place 2-5 minutes before news release",
            "cancel_unfilled": "Remove unfilled order immediately after news hits",
            "WARNING": "Spread widens massively during news. Slippage is real. Use limit orders where possible.",
            "risk": "HIGH — only use with 0.5% risk max",
        }

    @staticmethod
    def spike_fade(spike_direction: str, spike_high: float, spike_low: float, atr: float) -> dict:
        """Fade the initial news spike after it overextends."""
        if spike_direction == "up":
            entry = round(spike_high - atr * 0.3, 5)
            sl = round(spike_high + atr * 0.5, 5)
            tp = round(spike_high - atr * 1.5, 5)
        else:
            entry = round(spike_low + atr * 0.3, 5)
            sl = round(spike_low - atr * 0.5, 5)
            tp = round(spike_low + atr * 1.5, 5)
        return {
            "strategy": "spike_fade",
            "entry": entry, "sl": sl, "tp": tp,
            "direction": "SELL" if spike_direction == "up" else "BUY",
            "timing": "Wait 5-15 minutes after spike for momentum to exhaust",
            "confirmation": "Look for rejection candle (pin bar, engulfing) at spike extreme",
            "win_rate": "~55-60% historically — initial spikes retrace 50-70% of the move",
        }

    @staticmethod
    def news_momentum(data_surprise: float, direction: str, atr: float, entry_price: float) -> dict:
        """Ride the momentum when data significantly beats/misses expectations."""
        if abs(data_surprise) < 0.5:
            return {"signal": "NO TRADE — data in line with expectations, no directional edge"}
        strength = "STRONG" if abs(data_surprise) > 2 else "MODERATE"
        return {
            "strategy": "news_momentum",
            "surprise_magnitude": round(data_surprise, 2),
            "direction": direction,
            "strength": strength,
            "entry": round(entry_price, 5),
            "sl": round(entry_price - atr * 1.5, 5) if direction == "BUY" else round(entry_price + atr * 1.5, 5),
            "tp": round(entry_price + atr * 3, 5) if direction == "BUY" else round(entry_price - atr * 3, 5),
            "hold": "30 min to 4 hours depending on follow-through",
        }
```

---

## Sentiment Extreme Contrarian

```python
class SentimentContrarian:
    @staticmethod
    def composite_contrarian_signal(retail_long_pct: float, fear_greed: int, cot_percentile: float,
                                      social_bullish_pct: float) -> dict:
        scores = []
        if retail_long_pct > 75: scores.append(-0.8)
        elif retail_long_pct < 25: scores.append(0.8)
        else: scores.append(0)

        if fear_greed > 80: scores.append(-0.6)
        elif fear_greed < 20: scores.append(0.6)
        else: scores.append(0)

        if cot_percentile > 90: scores.append(-0.7)
        elif cot_percentile < 10: scores.append(0.7)
        else: scores.append(0)

        if social_bullish_pct > 80: scores.append(-0.5)
        elif social_bullish_pct < 20: scores.append(0.5)
        else: scores.append(0)

        import numpy as np
        avg = np.mean(scores)
        extreme_count = sum(1 for s in scores if abs(s) > 0.4)
        return {
            "composite_score": round(avg, 3),
            "direction": "CONTRARIAN BUY" if avg > 0.3 else "CONTRARIAN SELL" if avg < -0.3 else "NO EXTREME",
            "extreme_indicators": extreme_count,
            "conviction": "HIGH" if extreme_count >= 3 else "MODERATE" if extreme_count >= 2 else "LOW",
            "note": "Best when 3+ indicators at extremes simultaneously. Single indicator extremes are noisy.",
        }
```

---

## Economic Indicator Tracker

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

---

## COT Positioning Strategy

```python
import pandas as pd, numpy as np

class COTStrategy:
    @staticmethod
    def weekly_change_signal(net_spec: int, prev_net_spec: int, percentile: float) -> dict:
        change = net_spec - prev_net_spec
        return {
            "strategy": "cot_positioning",
            "net_speculative": net_spec, "weekly_change": change,
            "percentile": round(percentile, 1),
            "signal": "CONTRARIAN SELL" if percentile > 90 and change < 0 else
                     "CONTRARIAN BUY" if percentile < 10 and change > 0 else
                     "TREND BUY" if change > 0 and 30 < percentile < 70 else
                     "TREND SELL" if change < 0 and 30 < percentile < 70 else "WAIT",
            "logic": "Extremes = fade the crowd. Mid-range = follow the smart money flow.",
            "timing": "Hold 2-8 weeks. COT is a slow signal — not for day trading.",
        }
```

---

## Seasonality Analyzer

```python
import pandas as pd
import numpy as np
from scipy import stats

class SeasonalityAnalyzer:

    @staticmethod
    def monthly_seasonality(df: pd.DataFrame) -> pd.DataFrame:
        """Monthly return statistics with significance testing."""
        df = df.copy()
        df["return"] = df["close"].pct_change()
        df["month"] = df.index.month
        monthly = df.groupby("month")["return"].agg(["mean", "std", "count"])
        monthly["annualized"] = monthly["mean"] * 21 * 12 * 100
        monthly["t_stat"] = monthly["mean"] / (monthly["std"] / np.sqrt(monthly["count"]))
        monthly["p_value"] = monthly["t_stat"].apply(lambda t: 2 * (1 - stats.t.cdf(abs(t), df=max(monthly["count"].min()-1, 1))))
        monthly["significant"] = monthly["p_value"] < 0.05
        monthly["win_rate"] = df.groupby("month")["return"].apply(lambda x: (x > 0).mean()) * 100
        monthly.index = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        return monthly.round(4)

    @staticmethod
    def day_of_week_seasonality(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["return"] = df["close"].pct_change()
        df["dow"] = df.index.dayofweek
        daily = df.groupby("dow")["return"].agg(["mean", "std", "count"])
        daily["annualized"] = daily["mean"] * 252 * 100
        daily["t_stat"] = daily["mean"] / (daily["std"] / np.sqrt(daily["count"]))
        daily["p_value"] = daily["t_stat"].apply(lambda t: 2 * (1 - stats.t.cdf(abs(t), df=max(daily["count"].min()-1, 1))))
        daily["significant"] = daily["p_value"] < 0.05
        daily.index = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        return daily.round(4)

    @staticmethod
    def hourly_seasonality(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["return"] = df["close"].pct_change()
        df["hour"] = df.index.hour
        hourly = df.groupby("hour")["return"].agg(["mean", "std", "count"])
        hourly["annualized"] = hourly["mean"] * 252 * 24 * 100
        hourly["range_pips"] = df.groupby(df.index.hour).apply(lambda x: (x["high"] - x["low"]).mean()) * 10000
        return hourly.round(4)

    @staticmethod
    def full_report(df: pd.DataFrame, symbol: str = "") -> dict:
        return {
            "symbol": symbol,
            "monthly": SeasonalityAnalyzer.monthly_seasonality(df).to_dict(),
            "daily": SeasonalityAnalyzer.day_of_week_seasonality(df).to_dict(),
            "hourly": SeasonalityAnalyzer.hourly_seasonality(df).to_dict(),
            "WARNING": "Seasonality = historical tendency, not guarantee. Always combine with other analysis.",
        }
```

---

## Event Timeline Linker

### Overview
Links data points across time from multiple sources (price, news, institutional flows,
economic data, correlation shifts) to reconstruct event chains and build predictive narratives.
Answers: **What happened? Why? How? What was the result? What will likely happen next?**

### Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Event Timeline Linker                            │
├────────────┬────────────┬──────────────┬───────────┬───────────────┤
│ Event      │ Temporal   │ Causal Chain │ Pattern   │ Prediction    │
│ Collector  │ Aligner    │ Builder      │ Matcher   │ Engine        │
└────────────┴────────────┴──────────────┴───────────┴───────────────┘
         ↑            ↑             ↑            ↑
    [mt5-chart]  [news-impact]  [correlation]  [institutional]
```

### 1. Event Data Model

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional, Literal
from dataclasses import dataclass, field, asdict
import json

@dataclass
class TimelineEvent:
    """Universal event structure for cross-source linking."""
    timestamp: datetime
    source: Literal["price", "news", "economic", "institutional", "correlation", "technical", "geopolitical"]
    event_type: str          # e.g., "rate_decision", "breakout", "correlation_shift"
    title: str               # human-readable title
    description: str         # detailed description
    impact: Literal["HIGH", "MEDIUM", "LOW"]
    affected_instruments: list[str] = field(default_factory=list)
    data: dict = field(default_factory=dict)  # source-specific payload
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["timestamp"] = self.timestamp.isoformat()
        return d

@dataclass
class CausalLink:
    """Represents a cause -> effect relationship between events."""
    cause: TimelineEvent
    effect: TimelineEvent
    confidence: float        # 0-1 confidence in the causal relationship
    lag_seconds: int         # time between cause and effect
    mechanism: str           # how the cause led to the effect
    evidence: list[str] = field(default_factory=list)
```

### 2. Event Collector — Gather from All Sources

```python
class EventCollector:
    """
    Collect and normalize events from all trading skill sources into
    a unified timeline. Each source adapter converts raw data into TimelineEvent.
    """

    @staticmethod
    def from_price_data(df: pd.DataFrame, symbol: str) -> list[TimelineEvent]:
        """Extract significant price events: breakouts, reversals, gaps, spikes."""
        events = []
        returns = df["close"].pct_change()
        atr_val = ((df["high"] - df["low"]).rolling(14).mean())

        for i in range(20, len(df)):
            row = df.iloc[i]
            ret = returns.iloc[i]

            # Large move detection (>2 ATR)
            move = abs(row["close"] - row["open"])
            if move > 2 * atr_val.iloc[i]:
                events.append(TimelineEvent(
                    timestamp=df.index[i],
                    source="price",
                    event_type="large_move",
                    title=f"{symbol} {'bullish' if ret > 0 else 'bearish'} spike",
                    description=f"{symbol} moved {abs(ret)*100:.2f}% in one bar ({move:.5f} > 2x ATR)",
                    impact="HIGH" if abs(ret) > 0.01 else "MEDIUM",
                    affected_instruments=[symbol],
                    data={"return": round(ret, 6), "atr": round(atr_val.iloc[i], 6)},
                    tags=["spike", "volatility"],
                ))

            # Gap detection
            if i > 0:
                gap = abs(row["open"] - df.iloc[i - 1]["close"])
                if gap > 1.5 * atr_val.iloc[i]:
                    events.append(TimelineEvent(
                        timestamp=df.index[i],
                        source="price",
                        event_type="gap",
                        title=f"{symbol} gap {'up' if row['open'] > df.iloc[i-1]['close'] else 'down'}",
                        description=f"Gap of {gap:.5f} detected at open",
                        impact="MEDIUM",
                        affected_instruments=[symbol],
                        data={"gap_size": round(gap, 6)},
                        tags=["gap"],
                    ))

            # New high/low detection (20-bar)
            if row["high"] == df["high"].iloc[max(0, i-20):i+1].max():
                events.append(TimelineEvent(
                    timestamp=df.index[i],
                    source="price",
                    event_type="new_high",
                    title=f"{symbol} 20-bar high",
                    description=f"New 20-bar high at {row['high']:.5f}",
                    impact="LOW",
                    affected_instruments=[symbol],
                    data={"price": round(row["high"], 6)},
                    tags=["breakout", "high"],
                ))

        return events

    @staticmethod
    def from_news(news_items: list[dict]) -> list[TimelineEvent]:
        """Convert news items into timeline events."""
        events = []
        for item in news_items:
            events.append(TimelineEvent(
                timestamp=datetime.fromisoformat(item.get("datetime", datetime.utcnow().isoformat())),
                source="news" if "rate" not in item.get("name", "").lower() else "economic",
                event_type=item.get("type", "news_release"),
                title=item.get("name", item.get("headline", "Unknown")),
                description=item.get("description", ""),
                impact=item.get("impact", "MEDIUM"),
                affected_instruments=item.get("affected_pairs", []),
                data=item,
                tags=item.get("tags", ["news"]),
            ))
        return events

    @staticmethod
    def from_correlation_shift(shifts: list[dict]) -> list[TimelineEvent]:
        """Convert correlation regime shifts into timeline events."""
        events = []
        for shift in shifts:
            events.append(TimelineEvent(
                timestamp=datetime.utcnow(),
                source="correlation",
                event_type="correlation_regime_shift",
                title=f"Correlation shift: {shift['pair']}",
                description=f"Deviation: {shift['deviation']:.4f} — {shift['signal']}",
                impact="HIGH" if abs(shift["deviation"]) > 0.4 else "MEDIUM",
                affected_instruments=shift["pair"].split("/"),
                data=shift,
                tags=["correlation", "regime_shift"],
            ))
        return events

    @staticmethod
    def from_institutional(actions: list[dict]) -> list[TimelineEvent]:
        """Convert institutional actions into timeline events."""
        events = []
        for action in actions:
            events.append(TimelineEvent(
                timestamp=datetime.fromisoformat(action.get("datetime", datetime.utcnow().isoformat())),
                source="institutional",
                event_type=action.get("type", "institutional_action"),
                title=action.get("title", "Institutional Activity"),
                description=action.get("description", ""),
                impact=action.get("impact", "HIGH"),
                affected_instruments=action.get("affected_pairs", []),
                data=action,
                tags=["institutional", action.get("institution", "unknown")],
            ))
        return events
```

### 3. Temporal Aligner — Synchronize Events Across Sources

```python
class TemporalAligner:
    """Align events from different sources by time proximity."""

    @staticmethod
    def build_timeline(events: list[TimelineEvent], sort: bool = True) -> list[TimelineEvent]:
        """Merge all events into a single chronological timeline."""
        if sort:
            events.sort(key=lambda e: e.timestamp)
        return events

    @staticmethod
    def find_concurrent_events(
        events: list[TimelineEvent],
        target_time: datetime,
        window: timedelta = timedelta(hours=4)
    ) -> list[TimelineEvent]:
        """Find all events within a time window of a target event."""
        return [
            e for e in events
            if abs((e.timestamp - target_time).total_seconds()) <= window.total_seconds()
        ]

    @staticmethod
    def cluster_by_time(
        events: list[TimelineEvent],
        max_gap: timedelta = timedelta(hours=2)
    ) -> list[list[TimelineEvent]]:
        """Group events into temporal clusters (events happening together)."""
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

    @staticmethod
    def event_density(events: list[TimelineEvent], bin_size: str = "1H") -> pd.Series:
        """Count events per time bin — high density = significant period."""
        timestamps = pd.Series([e.timestamp for e in events])
        return timestamps.dt.floor(bin_size).value_counts().sort_index()
```

### 4. Causal Chain Builder — What -> Why -> How -> Result

```python
class CausalChainBuilder:
    """
    Build cause-effect chains from temporally aligned events.
    Produces structured narratives: WHAT happened -> WHY -> HOW -> RESULT -> PREDICTION.
    """

    # Causal relationship templates
    CAUSAL_PATTERNS = {
        ("economic", "price"): {
            "mechanism": "Economic data release triggered market repricing",
            "base_confidence": 0.7,
        },
        ("news", "price"): {
            "mechanism": "News headline drove sentiment shift and price reaction",
            "base_confidence": 0.5,
        },
        ("institutional", "price"): {
            "mechanism": "Institutional positioning/flow caused directional pressure",
            "base_confidence": 0.6,
        },
        ("correlation", "price"): {
            "mechanism": "Correlation regime shift indicates structural market change",
            "base_confidence": 0.4,
        },
        ("economic", "correlation"): {
            "mechanism": "Macro data release shifted inter-market relationships",
            "base_confidence": 0.5,
        },
        ("geopolitical", "price"): {
            "mechanism": "Geopolitical event triggered risk repricing across markets",
            "base_confidence": 0.6,
        },
    }

    @staticmethod
    def find_causal_links(
        events: list[TimelineEvent],
        max_lag: timedelta = timedelta(hours=6)
    ) -> list[CausalLink]:
        """Identify potential causal relationships between events."""
        links = []
        sorted_events = sorted(events, key=lambda e: e.timestamp)

        for i, potential_cause in enumerate(sorted_events):
            for potential_effect in sorted_events[i + 1:]:
                lag = (potential_effect.timestamp - potential_cause.timestamp).total_seconds()
                if lag > max_lag.total_seconds():
                    break
                if lag < 0:
                    continue

                pattern_key = (potential_cause.source, potential_effect.source)
                pattern = CausalChainBuilder.CAUSAL_PATTERNS.get(pattern_key)
                if not pattern:
                    continue

                # Check instrument overlap
                overlap = set(potential_cause.affected_instruments) & set(potential_effect.affected_instruments)
                if not overlap and "BROAD" not in potential_cause.affected_instruments:
                    continue

                # Compute confidence
                confidence = pattern["base_confidence"]
                if potential_cause.impact == "HIGH":
                    confidence += 0.15
                if lag < 3600:  # Within 1 hour
                    confidence += 0.1
                confidence = min(confidence, 0.95)

                links.append(CausalLink(
                    cause=potential_cause,
                    effect=potential_effect,
                    confidence=round(confidence, 3),
                    lag_seconds=int(lag),
                    mechanism=pattern["mechanism"],
                    evidence=[f"Time lag: {lag/3600:.1f}h", f"Instrument overlap: {overlap}"],
                ))

        return sorted(links, key=lambda l: l.confidence, reverse=True)

    @staticmethod
    def build_narrative(
        cluster: list[TimelineEvent],
        causal_links: list[CausalLink]
    ) -> dict:
        """
        Build a structured narrative from an event cluster.
        Returns: {what, why, how, result, prediction}
        """
        # Sort by time
        cluster.sort(key=lambda e: e.timestamp)

        # Identify initiating events (causes) vs resulting events (effects)
        causes = [e for e in cluster if e.source in ("economic", "news", "institutional", "geopolitical")]
        effects = [e for e in cluster if e.source in ("price", "correlation", "technical")]

        # Build narrative
        what = " -> ".join([e.title for e in cluster])
        why = "; ".join([link.mechanism for link in causal_links[:3]]) if causal_links else "Cause unclear — further analysis needed"
        how = "; ".join([
            f"{e.source}: {e.title} ({e.impact})" for e in causes
        ]) if causes else "No clear trigger identified"
        result = "; ".join([
            f"{e.title}: {e.data.get('return', 'N/A')}" for e in effects
        ]) if effects else "Price impact not yet measured"

        # Prediction based on historical pattern matching
        prediction = CausalChainBuilder._predict_next(cluster, causal_links)

        return {
            "time_range": f"{cluster[0].timestamp.isoformat()} -> {cluster[-1].timestamp.isoformat()}",
            "what": what,
            "why": why,
            "how": how,
            "result": result,
            "prediction": prediction,
            "confidence": round(np.mean([l.confidence for l in causal_links]), 3) if causal_links else 0,
            "n_events": len(cluster),
            "sources_involved": list(set(e.source for e in cluster)),
        }

    @staticmethod
    def _predict_next(cluster: list[TimelineEvent], links: list[CausalLink]) -> str:
        """Generate prediction based on event pattern and causal chain."""
        if not links:
            return "Insufficient causal data for prediction"

        high_impact = [e for e in cluster if e.impact == "HIGH"]
        if not high_impact:
            return "Low-impact event cluster — expect mean-reversion or consolidation"

        causes = [l.cause for l in links]
        primary_source = max(set(c.source for c in causes), key=lambda s: sum(1 for c in causes if c.source == s))

        predictions = {
            "economic": "Watch for follow-through move in the direction of data surprise. Expect elevated volatility for 2-4 hours post-release.",
            "news": "Sentiment-driven moves often retrace 50-70%. Watch for confirmation or reversal at key S/R levels.",
            "institutional": "Institutional flows tend to persist. Watch for continuation in the direction of the initial move over 1-3 sessions.",
            "geopolitical": "Geopolitical events create risk-off flows initially. JPY, CHF, Gold tend to strengthen. Effect duration depends on escalation.",
            "correlation": "Correlation regime shifts signal structural changes. Previous mean-reversion strategies may fail. Re-evaluate pair relationships.",
        }
        return predictions.get(primary_source, "Monitor closely for follow-through or reversal signals.")
```

### 5. Full Timeline Report

```python
def generate_timeline_report(
    events: list[TimelineEvent],
    focus_time: Optional[datetime] = None,
    window: timedelta = timedelta(hours=24)
) -> dict:
    """
    Complete timeline analysis report.
    If focus_time provided, narrows to events within the window.
    """
    if focus_time:
        events = TemporalAligner.find_concurrent_events(events, focus_time, window)

    timeline = TemporalAligner.build_timeline(events)
    clusters = TemporalAligner.cluster_by_time(events)
    all_links = CausalChainBuilder.find_causal_links(events)

    narratives = []
    for cluster in clusters:
        cluster_links = [l for l in all_links if l.cause in cluster or l.effect in cluster]
        narratives.append(CausalChainBuilder.build_narrative(cluster, cluster_links))

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "total_events": len(events),
        "event_clusters": len(clusters),
        "causal_links_found": len(all_links),
        "narratives": narratives,
        "density": TemporalAligner.event_density(events).to_dict(),
        "high_confidence_chains": [
            {"cause": l.cause.title, "effect": l.effect.title,
             "confidence": l.confidence, "mechanism": l.mechanism}
            for l in all_links if l.confidence > 0.6
        ],
    }
```

### Usage Conventions

1. **Always collect from multiple sources** — single-source narratives are unreliable
2. **Time windows matter** — use 4h for intraday events, 24h for daily, 1 week for macro
3. **Confidence < 0.5** — treat as hypothesis, not conclusion
4. **Predictions are probabilistic** — never present as certainties
5. **Store all reports** — via `trading-data-science` persistent storage for future pattern matching

---

## News Trading Entry Framework
*Source: "The ONLY Newstrading-Video you'll EVER need" — World Class Edge (Trading World Champion)*

### Core Principle: Trade the Deviation, Not the Number

```
Market move = Actual − Consensus expectation
Positive deviation = bullish for base currency / asset
Negative deviation = bearish
Small deviation (±0.1%) → fade the spike
Large deviation (±1%+) → trade the continuation
```

Always check prior period revisions — a downward revision offsets a beat in the current period.

### Tier 1 News Events (highest impact)

| Event | Time (UTC) | Frequency | Instrument impact |
|-------|-----------|-----------|------------------|
| NFP (Non-Farm Payrolls) | 13:30 | 1st Friday/month | USD pairs, Gold, indices |
| FOMC Rate Decision | 19:00 | 8× per year | All USD pairs, indices |
| FOMC Press Conference | 19:30 | Same day | Often reverses the 19:00 move |
| CPI | 13:30 | Monthly | USD, Gold, bonds |
| GDP (advance) | 13:30 | Quarterly | USD, indices |

**FOMC two-trade rule:** Trade the 19:00 rate decision, then reassess at 19:30 press conference — the press conference frequently reverses the initial reaction.

### 3 Entry Models

**Model A — Post-News Retracement (primary, safest):**
```
1. News releases → DO NOT trade the spike
2. Wait 15–30 minutes for direction to establish
3. Find first OB or FVG created by the news displacement candle
4. Enter at OB/FVG in direction of fundamental surprise
5. Stop: beyond OB/FVG distal line
6. Target: major HTF level (weekly H/L, monthly open)
```

**Model B — Pre-News Straddle (advanced):**
```
1. Place BUY STOP above prior swing high
2. Place SELL STOP below prior swing low
3. Cancel whichever doesn't trigger within 5 min of release
4. Win side profits from initial momentum
Risk: whipsaw = two small losses
Best for: NFP, FOMC, CPI (known high-directional events)
```

**Model C — Fade the Fakeout:**
```
1. Initial spike fires in direction of surprise
2. Within 5 candles: M5 CHoCH forms (reversal signal)
3. Enter opposite direction of spike
4. Stop: beyond spike wick extreme
Best for: data "already priced in" situations
```

### News Risk Rules

- **Reduce position to 25–50% of normal size** during news events
- **Never enter in the first candle** — spreads 3–10× normal; slippage severe
- **Wait for spread normalization** — 2–5 min post-release before entering
- **No pending orders too close to price** — can gap through stops unfilled
- **The 30-minute rule** — after 30 min, news effect absorbed; sustained move is fundamentally driven

### Spread Impact During News

| Instrument | Normal | News spike |
|-----------|--------|-----------|
| EURUSD | 0.1–0.5 pips | 3–20 pips |
| XAUUSDm | 0.15–0.30 pts | 2–10 pts |
| US500m | 0.4–1 pt | 3–15 pts |
| USDJPYm | 0.2–0.5 pips | 2–8 pips |

---

## Related Skills

- [Fundamental Analysis](../fundamental-analysis.md)
- [Sentiment Analysis](../social-sentiment-scraper.md)
- [News Data Stream](../news-intelligence.md)
- [Economic Calendar](../economic-calendar.md)
