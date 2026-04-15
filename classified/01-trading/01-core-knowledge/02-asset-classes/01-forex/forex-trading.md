---
name: forex-trading
description: >
  Forex market specifics: major/minor/exotic pairs, currency pair mechanics, pip values,
  lot sizes, swap/rollover, session overlaps, carry trades, central bank impact.
  USE FOR: forex pairs, currency pairs, pip value, lot size, major pairs, minor pairs,
  exotic pairs, forex session, carry trade, swap rates, rollover, central bank,
  forex spread, forex leverage, currency risk, forex broker, forex liquidity.
related_skills:
  - session-scalping
  - ict-smart-money
  - cross-asset-relationships
  - liquidity-analysis
tags:
  - trading
  - asset-class
  - forex
  - pairs
  - pips
  - session-hours
skill_level: beginner
kind: reference
category: trading/asset-classes
status: active
---
> **Skill:** Forex Trading  |  **Domain:** trading  |  **Category:** asset-class  |  **Level:** beginner
> **Tags:** `trading`, `asset-class`, `forex`, `pairs`, `pips`, `session-hours`


# Forex Trading — Asset Class Reference

## Major Pairs & Characteristics
| Pair | Nickname | Spread (avg) | Best Session | Volatility |
|------|----------|--------------|--------------|------------|
| EURUSD | Fiber | 0.1–0.6 pips | London/NY overlap | Medium |
| GBPUSD | Cable | 0.3–1.0 pips | London open | High |
| USDJPY | Ninja | 0.2–0.7 pips | Tokyo/London | Medium |
| AUDUSD | Aussie | 0.2–0.8 pips | Sydney/London | Medium |
| USDCAD | Loonie | 0.3–1.0 pips | NY session | Medium |
| USDCHF | Swissie | 0.3–1.0 pips | London/NY | Medium |

## Pip Value Calculator
```python
def pip_value(pair: str, lot_size: float, account_currency: str = "USD") -> float:
    """Standard pip values for 1 standard lot (100,000 units)."""
    pip_sizes = {
        "EURUSD": 0.0001, "GBPUSD": 0.0001, "AUDUSD": 0.0001,
        "USDCAD": 0.0001, "USDCHF": 0.0001, "USDJPY": 0.01,
        "XAUUSD": 0.01,   "XAGUSD": 0.001,
    }
    pip = pip_sizes.get(pair.upper(), 0.0001)
    # For USD-quoted pairs: pip_value = pip * lot_size * contract_size
    return pip * lot_size * 100_000
```

## Session Hours & Liquidity Windows
| Session | UTC Open | UTC Close | Key Pairs |
|---------|----------|-----------|-----------|
| Sydney | 22:00 | 07:00 | AUDUSD, NZDUSD |
| Tokyo | 00:00 | 09:00 | USDJPY, AUDJPY |
| London | 07:00 | 16:00 | GBPUSD, EURUSD |
| New York | 12:00 | 21:00 | All majors |
| **London/NY Overlap** | **12:00** | **16:00** | **Highest volume — best for scalping** |

## Carry Trade Framework
```python
def carry_trade_screen(pairs: list, rates: dict) -> list:
    """Find best carry pairs: borrow low-rate currency, invest high-rate."""
    results = []
    for pair in pairs:
        base, quote = pair[:3], pair[3:]
        carry = rates.get(base, 0) - rates.get(quote, 0)
        results.append({"pair": pair, "carry_pct": round(carry, 2),
                        "direction": "LONG" if carry > 0 else "SHORT"})
    return sorted(results, key=lambda x: abs(x["carry_pct"]), reverse=True)
```

## Key Forex Risks
- **Central bank risk**: Unexpected rate decisions cause 100+ pip moves
- **Economic data risk**: NFP, CPI, GDP — trade around releases with caution
- **Correlation risk**: EURUSD and GBPUSD often move together — don't double up
- **Swap/rollover**: Holding past 22:00 UTC server time incurs overnight swap fees

## Exness MT5 Pip Sizes (your broker)
```python
PIP_SIZES = {
    "EURUSDm": 0.0001, "GBPUSDm": 0.0001, "USDJPYm": 0.01,
    "AUDUSDm": 0.0001, "USDCADm": 0.0001, "USDCHFm": 0.0001,
    "XAUUSDm": 0.1,    "XAGUSDm": 0.01,
}
```

---

## Related Skills

- [Session Strategies](../session-scalping.md)
- [Ict Smart Money](../ict-smart-money.md)
- [Cross Asset Relationships](../cross-asset-relationships.md)
- [Liquidity Analysis](../liquidity-analysis.md)
