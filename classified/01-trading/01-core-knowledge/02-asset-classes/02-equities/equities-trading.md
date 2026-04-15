---
name: equities-trading
description: >
  Equities and stock CFD trading: NYSE/NASDAQ sessions, stock-specific mechanics,
  earnings impact, sector rotation, index correlation, gap trading, opening range.
  USE FOR: stocks, equities, stock CFD, NYSE, NASDAQ, earnings, sector rotation,
  index correlation, opening range breakout, ORB, gap and go, pre-market, after-hours,
  stock screener, TSLAm, AAPLm, MSFTm, NVDAm, AMZNm, GOOGm, METAm, JPMm, BAm.
related_skills:
  - session-scalping
  - technical-analysis
  - fundamental-analysis
  - risk-and-portfolio
tags:
  - trading
  - asset-class
  - equities
  - stocks
  - cfds
  - earnings
  - sectors
skill_level: beginner
kind: reference
category: trading/asset-classes
status: active
---
> **Skill:** Equities Trading  |  **Domain:** trading  |  **Category:** asset-class  |  **Level:** beginner
> **Tags:** `trading`, `asset-class`, `equities`, `stocks`, `cfds`, `earnings`, `sectors`


# Equities & Stock CFD Trading

## Trading Hours (Critical for CFDs)
| Market | UTC | EST | Notes |
|--------|-----|-----|-------|
| Pre-market | 09:00–13:30 | 04:00–08:30 | Low liquidity, wide spreads |
| **NYSE/NASDAQ Open** | **13:30–20:00** | **09:30–16:00** | **Primary window** |
| After-hours | 20:00–01:00 | 16:00–20:00 | Low liquidity |

> **CFD Rule**: Stock CFDs (TSLAm, AAPLm, etc.) only trade during NY session 13:30–20:00 UTC

## Opening Range Breakout (ORB)
```python
def opening_range_breakout(candles_930_to_1000: list) -> dict:
    """First 30 minutes of NYSE session sets the range for ORB strategy."""
    highs = [c["high"] for c in candles_930_to_1000]
    lows  = [c["low"]  for c in candles_930_to_1000]
    orb_high = max(highs)
    orb_low  = min(lows)
    orb_range = orb_high - orb_low
    return {
        "orb_high": orb_high, "orb_low": orb_low,
        "orb_range": round(orb_range, 2),
        "long_trigger": orb_high,
        "short_trigger": orb_low,
        "long_target": round(orb_high + orb_range, 2),
        "short_target": round(orb_low - orb_range, 2),
        "long_stop": round(orb_low, 2),
        "short_stop": round(orb_high, 2),
        "timing": "Trade breakouts between 10:00–11:30 AM EST only",
    }
```

## Earnings Impact Framework
- **Beat + guidance raise** → gap up, momentum long first hour
- **Beat + guidance cut** → sell the news — fade the gap within 30 min
- **Miss** → gap down, short any bounce to VWAP
- **In-line** → range trade, fade opening extremes
- **Rule**: Never hold stock CFD positions through earnings — gap risk is unlimited

## Sector Rotation Model
| Cycle Phase | Leading Sectors | Lagging Sectors |
|-------------|----------------|-----------------|
| Early expansion | Tech, Consumer Disc | Utilities, Staples |
| Mid expansion | Industrials, Materials | Healthcare |
| Late expansion | Energy, Materials | Tech |
| Recession | Utilities, Healthcare, Staples | Energy, Tech |

## Your Stock CFD Watchlist (Exness MT5)
```python
STOCK_CFDS = ["TSLAm", "AAPLm", "MSFTm", "NVDAm", "AMZNm", "GOOGm", "METAm", "JPMm", "BAm"]
INDICES    = ["US500m", "USTECm", "US30m"]
PIP_SIZE   = 0.01  # All stock CFDs
```

## Index Correlation (useful for bias)
- **USTECm** drives NVDAm, AAPLm, MSFTm, GOOGm, METAm
- **US30m** drives JPMm, BAm
- **US500m** = broad market — use as overall risk-on/off filter
- If indices sell off → avoid long stock CFDs regardless of individual setup

---

## Related Skills

- [Session Scalping](../session-scalping.md)
- [Technical Analysis](../technical-analysis.md)
- [Fundamental Analysis](../fundamental-analysis.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
