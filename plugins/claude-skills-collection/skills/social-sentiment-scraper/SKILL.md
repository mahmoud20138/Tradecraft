---
name: social-sentiment-scraper
description: >
  Scrapes and analyzes social media sentiment from Twitter/X, Reddit, TradingView, and market
  sentiment indicators like Fear & Greed Index and retail positioning. Use this skill whenever
  the user asks about "market sentiment", "what are traders saying", "Twitter sentiment",
  "Reddit WallStreetBets", "retail positioning", "Fear and Greed Index", "crowd sentiment",
  "contrarian signal", "social media trading", "TradingView ideas", "bullish or bearish crowd",
  "retail long/short ratio", "IG client sentiment", "Myfxbook sentiment", or any question about
  what the trading crowd thinks. Retail crowd is often a contrarian indicator.
  Works with market-news-impact and trading-brain.
kind: reference
category: trading/data
status: active
tags: [data, news, scraper, sentiment, social, trading]
related_skills: [economic-calendar, market-data-ingestion, alternative-data-integrator, analyze, economic-indicator-tracker]
---

# Social Sentiment Scraper

## Overview
Aggregates sentiment from social platforms and retail positioning data. The primary value is
as a **contrarian indicator** — when retail is overwhelmingly long, consider selling, and vice versa.

---

## 1. Sentiment Sources & Priority

```python
SENTIMENT_SOURCES = {
    # Quantitative (most reliable)
    "retail_positioning": {
        "ig_client_sentiment": {"url": "https://www.ig.com/en/trading-sentiment", "reliability": 0.8},
        "myfxbook_outlook": {"url": "https://www.myfxbook.com/community/outlook", "reliability": 0.7},
        "oanda_positions": {"url": "https://www.oanda.com/forex-trading/analysis/open-position-ratios", "reliability": 0.7},
    },
    # Index-based
    "fear_greed": {
        "cnn_fear_greed": {"url": "https://edition.cnn.com/markets/fear-and-greed", "reliability": 0.6},
        "crypto_fear_greed": {"url": "https://alternative.me/crypto/fear-and-greed-index/", "reliability": 0.5},
    },
    # Social (noisy but informative at extremes)
    "social_media": {
        "twitter_fintwit": {"query": "$EURUSD OR #forex OR #trading", "reliability": 0.4},
        "reddit_forex": {"url": "https://www.reddit.com/r/Forex/", "reliability": 0.3},
        "tradingview_ideas": {"url": "https://www.tradingview.com/ideas/", "reliability": 0.5},
    },
}
```

---

## 2. Retail Positioning Analysis

```python
from dataclasses import dataclass
import numpy as np

@dataclass
class RetailPositioning:
    symbol: str
    long_pct: float
    short_pct: float
    source: str

    @property
    def ratio(self) -> float:
        return self.long_pct / max(self.short_pct, 1)

    @property
    def contrarian_signal(self) -> dict:
        """
        Retail is wrong at extremes. >70% one way = contrarian signal.
        This is one of the most reliable sentiment indicators.
        """
        if self.long_pct > 75:
            return {"signal": "CONTRARIAN SELL", "strength": "strong",
                    "reason": f"{self.long_pct:.0f}% retail is long — crowd usually wrong at extremes"}
        if self.short_pct > 75:
            return {"signal": "CONTRARIAN BUY", "strength": "strong",
                    "reason": f"{self.short_pct:.0f}% retail is short — crowd usually wrong at extremes"}
        if self.long_pct > 65:
            return {"signal": "MILD CONTRARIAN SELL", "strength": "moderate",
                    "reason": f"{self.long_pct:.0f}% retail long — leaning contrarian"}
        if self.short_pct > 65:
            return {"signal": "MILD CONTRARIAN BUY", "strength": "moderate",
                    "reason": f"{self.short_pct:.0f}% retail short — leaning contrarian"}
        return {"signal": "NEUTRAL", "strength": "none",
                "reason": "No extreme positioning — no contrarian signal"}

class SentimentAggregator:
    """Combine multiple sentiment sources into actionable score."""

    def __init__(self):
        self.data_points = []

    def add_retail_positioning(self, pos: RetailPositioning):
        signal = pos.contrarian_signal
        score = -1 if "SELL" in signal["signal"] else 1 if "BUY" in signal["signal"] else 0
        self.data_points.append({
            "source": f"retail_{pos.source}",
            "symbol": pos.symbol,
            "score": score * (0.8 if signal["strength"] == "strong" else 0.4),
            "raw": {"long": pos.long_pct, "short": pos.short_pct},
            "signal": signal["signal"],
        })

    def add_fear_greed(self, index_value: int, index_name: str = "CNN"):
        """Fear & Greed: 0 = extreme fear, 100 = extreme greed."""
        if index_value < 20:
            score, label = 0.7, "EXTREME FEAR — contrarian buy"
        elif index_value < 35:
            score, label = 0.3, "FEAR — mild buy signal"
        elif index_value > 80:
            score, label = -0.7, "EXTREME GREED — contrarian sell"
        elif index_value > 65:
            score, label = -0.3, "GREED — mild sell signal"
        else:
            score, label = 0, "NEUTRAL"
        self.data_points.append({"source": f"fear_greed_{index_name}", "score": score, "label": label, "value": index_value})

    def add_social_sentiment(self, bullish_pct: float, bearish_pct: float, platform: str, sample_size: int):
        """Process social media sentiment. Weight by sample size."""
        if sample_size < 50:
            return  # Too small to be meaningful
        net = (bullish_pct - bearish_pct) / 100
        # Social sentiment as contrarian (inverted)
        contrarian = -net * min(sample_size / 500, 1.0) * 0.3
        self.data_points.append({
            "source": f"social_{platform}", "score": round(contrarian, 3),
            "raw_bullish": bullish_pct, "raw_bearish": bearish_pct, "sample_size": sample_size,
        })

    def aggregate(self) -> dict:
        if not self.data_points:
            return {"overall_score": 0, "signal": "NO DATA", "data_points": []}
        scores = [dp["score"] for dp in self.data_points]
        overall = np.mean(scores)
        return {
            "overall_score": round(overall, 3),
            "signal": "CONTRARIAN BUY" if overall > 0.3 else "CONTRARIAN SELL" if overall < -0.3 else "NEUTRAL",
            "confidence": round(min(abs(overall) * 1.5, 0.9), 2),
            "data_points": self.data_points,
            "n_sources": len(self.data_points),
            "WARNING": "Sentiment is a SECONDARY indicator — never trade on sentiment alone",
        }
```

---

## 3. Web Search Queries
```
# Retail positioning
web_search("IG client sentiment EURUSD")
web_search("Myfxbook forex outlook community")
web_search("OANDA open position ratios forex")

# Fear & Greed
web_search("CNN Fear Greed Index today")
web_search("crypto fear greed index")

# Social
web_search("Twitter forex sentiment EURUSD today")
web_search("Reddit r/forex daily discussion")
web_search("TradingView EURUSD ideas bullish bearish")
```

## Key Principle: Retail crowd is reliably wrong at extremes (>70% one direction). Use as contrarian confirmation, never as primary signal.
