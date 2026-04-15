---
name: news-straddle-strategy
description: >
  News trading strategies — pre-news straddle, spike fade, news momentum riding, and event
  volatility strategies. Use for "news trading", "straddle NFP", "trade the news", "news spike",
  "fade the spike", "news momentum", "event trading", "FOMC trade", "NFP strategy", "high impact
  news trade", or any news-event-based trading strategy.
  Works with market-news-impact and risk-calendar-trade-filter.
kind: strategy
category: trading/data
status: active
tags: [news, risk-and-portfolio, straddle, strategies, strategy, trading, volatility]
related_skills: [economic-calendar, market-data-ingestion, alternative-data-integrator, economic-indicator-tracker, market-intelligence]
---

# News Straddle & Event Trading Strategy

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
