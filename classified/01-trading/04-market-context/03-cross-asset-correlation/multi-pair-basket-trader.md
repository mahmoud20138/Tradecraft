---
name: multi-pair-basket-trader
description: >
  Trade currency baskets instead of individual pairs — USD basket, EUR basket, risk-on basket.
  Use for "basket trade", "currency basket", "trade USD strength", "sell EUR basket", "multi pair
  trade", "basket execution", "currency index trade", or any basket-based approach.
  Works with synthetic-pair-constructor and pair-correlation-engine.
kind: reference
category: trading/market-context
status: active
tags: [basket, correlation, market-context, multi, pair, risk-and-portfolio, trader, trading]
related_skills: [cross-asset-relationships, correlation-crisis, correlation-regime-switcher, pair-scanner-screener, synthetic-pair-constructor]
---

# Multi-Pair Basket Trader

```python
import numpy as np

class BasketTrader:
    CURRENCY_BASKETS = {
        "USD_LONG": {"EURUSD": "sell", "GBPUSD": "sell", "AUDUSD": "sell", "NZDUSD": "sell", "USDCAD": "buy", "USDJPY": "buy", "USDCHF": "buy"},
        "USD_SHORT": {"EURUSD": "buy", "GBPUSD": "buy", "AUDUSD": "buy", "NZDUSD": "buy", "USDCAD": "sell", "USDJPY": "sell", "USDCHF": "sell"},
        "EUR_LONG": {"EURUSD": "buy", "EURJPY": "buy", "EURGBP": "buy", "EURAUD": "buy"},
        "RISK_ON": {"AUDUSD": "buy", "NZDUSD": "buy", "USDJPY": "buy", "USDCHF": "sell"},
        "RISK_OFF": {"USDJPY": "sell", "USDCHF": "buy", "XAUUSD": "buy", "AUDUSD": "sell"},
    }

    @staticmethod
    def generate_basket_orders(basket_name: str, total_risk_pct: float = 2.0, account_balance: float = 10000) -> dict:
        basket = BasketTrader.CURRENCY_BASKETS.get(basket_name)
        if not basket: return {"error": f"Unknown basket: {basket_name}"}
        n_pairs = len(basket)
        risk_per_pair = total_risk_pct / n_pairs
        return {
            "basket": basket_name,
            "orders": [{"pair": p, "direction": d, "risk_pct": round(risk_per_pair, 2)} for p, d in basket.items()],
            "total_risk": total_risk_pct,
            "n_pairs": n_pairs,
            "risk_per_pair": round(risk_per_pair, 2),
            "advantage": "Diversified execution — single currency view, spread across pairs to reduce pair-specific noise",
        }

    @staticmethod
    def basket_correlation_check(basket_name: str, correlation_matrix: dict) -> dict:
        """Validate basket pairs aren't too correlated (reduces diversification benefit)."""
        basket = BasketTrader.CURRENCY_BASKETS.get(basket_name)
        if not basket: return {"error": f"Unknown basket: {basket_name}"}
        pairs = list(basket.keys())
        high_corr_pairs = []
        for i, p1 in enumerate(pairs):
            for p2 in pairs[i+1:]:
                key = f"{p1}_{p2}"
                corr = correlation_matrix.get(key, 0)
                if abs(corr) > 0.85:
                    high_corr_pairs.append({"pair1": p1, "pair2": p2, "corr": round(corr, 3)})
        return {
            "basket": basket_name,
            "n_pairs": len(pairs),
            "high_correlation_warnings": high_corr_pairs,
            "diversification_quality": "POOR" if len(high_corr_pairs) > 2 else "MODERATE" if high_corr_pairs else "GOOD",
            "recommendation": "Consider removing highly correlated pairs to improve diversification" if high_corr_pairs else "Basket is well-diversified",
        }
```

## Basket Execution Rules

1. **Enter all pairs simultaneously** — partial fills defeat the purpose of basket diversification
2. **Equal risk per pair** — split total risk evenly across basket components
3. **Single stop for the basket** — if aggregate basket P&L hits -1.5%, close all positions
4. **Monitor basket P&L, not individual pairs** — individual pairs will diverge; basket thesis matters
5. **Exit all at once** — partial exits reintroduce single-pair risk

## Usage

```python
orders = BasketTrader.generate_basket_orders("USD_LONG", total_risk_pct=2.0, account_balance=10000)
for order in orders["orders"]:
    print(f"{order['direction'].upper()} {order['pair']} — {order['risk_pct']}% risk")

health = BasketTrader.basket_correlation_check("USD_LONG", corr_matrix)
print(f"Diversification: {health['diversification_quality']}")
```
