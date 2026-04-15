---
name: futures-trading
description: >
  Futures markets: contract specs, margin, rollover dates, commodity futures,
  index futures, interest rate futures, contango/backwardation, basis risk.
  USE FOR: futures contract, futures margin, rollover, expiry, contango,
  backwardation, commodity futures, crude oil futures, gold futures, ES futures,
  NQ futures, S&P futures, Nasdaq futures, treasury futures, basis risk,
  futures spread, USOILm, XAUUSDm futures.
related_skills:
  - execution-algo-trading
  - cross-asset-relationships
tags:
  - trading
  - asset-class
  - futures
  - contracts
  - rollover
  - contango
skill_level: intermediate
kind: reference
category: trading/asset-classes
status: active
---
> **Skill:** Futures Trading  |  **Domain:** trading  |  **Category:** asset-class  |  **Level:** intermediate
> **Tags:** `trading`, `asset-class`, `futures`, `contracts`, `rollover`, `contango`


# Futures Trading — Asset Class Reference

## Contract Mechanics
- **Expiry**: Futures expire on a fixed date (quarterly for index/rates, monthly for commodities)
- **Rollover**: Roll to next contract before expiry (typically 5–10 days before)
- **Basis**: Difference between futures price and spot price
- **Contango**: Futures > Spot (normal for commodities with storage costs)
- **Backwardation**: Futures < Spot (supply squeeze signal for commodities)

## Key Futures Instruments
| Contract | Exchange | Tick Size | Session (UTC) |
|----------|----------|-----------|---------------|
| ES (S&P 500) | CME | $12.50 | 23:00–22:00 |
| NQ (Nasdaq) | CME | $5.00 | 23:00–22:00 |
| CL (Crude Oil) | NYMEX | $10.00 | 00:00–23:00 |
| GC (Gold) | COMEX | $10.00 | 23:00–22:00 |
| ZN (10Y Note) | CBOT | $15.625 | 00:00–22:00 |

## Contango/Backwardation Signal
```python
def term_structure_signal(spot: float, front_month: float, next_month: float) -> dict:
    basis_1 = front_month - spot
    basis_2 = next_month - front_month
    structure = ("CONTANGO" if basis_1 > 0 and basis_2 > 0 else
                 "BACKWARDATION" if basis_1 < 0 and basis_2 < 0 else "MIXED")
    return {
        "structure": structure,
        "basis_front": round(basis_1, 2),
        "basis_next": round(basis_2, 2),
        "signal": {
            "CONTANGO": "Normal — no supply shock. Bearish medium-term for commodities.",
            "BACKWARDATION": "Supply squeeze or high demand. Bullish near-term.",
            "MIXED": "Transitioning — watch for structure shift.",
        }.get(structure),
    }
```

## Oil & Gold (Your Instruments)
```python
# Exness CFD equivalents of futures
OIL_CFD  = "USOILm"   # Tracks WTI crude front-month
GOLD_CFD = "XAUUSDm"  # Tracks COMEX gold spot/front-month

# Key oil fundamentals
OIL_DRIVERS = ["EIA inventory (Wed 14:30 UTC)", "OPEC decisions",
                "USD strength (inverse)", "geopolitical risk premium"]
GOLD_DRIVERS = ["Real yields (inverse)", "USD index (inverse)",
                "Risk sentiment", "Central bank buying"]
```

## Futures Rollover Impact
- Price gaps at rollover — check if your broker adjusts or creates gap
- Exness CFDs typically adjust continuously — no hard rollover gap
- Watch COT reports for large spec positioning at rollover dates

---

## Related Skills

- [Execution Algo Trading](../execution-algo-trading.md)
- [Market Microstructure](../market-microstructure.md)
- [Cross Asset Relationships](../cross-asset-relationships.md)



