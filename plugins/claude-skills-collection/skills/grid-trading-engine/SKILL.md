---
name: grid-trading-engine
description: >
  Systematic grid trading — place buy/sell orders at fixed intervals across a price range.
  Use for "grid trading", "grid bot", "grid strategy", "buy the dips grid", "DCA grid",
  "range grid", "grid order placement", or any systematic interval-based order strategy.
  Works with market-regime-classifier (best in RANGING regimes) and risk-and-portfolio.
kind: engine
category: trading/strategies
status: active
tags: [engine, grid, grid-trading, regime, risk-and-portfolio, strategies, trading]
related_skills: [jdub-price-action-strategy, session-scalping, asian-session-scalper, gap-trading-strategy, market-regime-classifier]
---

# Grid Trading Engine

```python
import numpy as np

class GridTradingEngine:

    @staticmethod
    def build_grid(center_price: float, range_pct: float = 2.0, n_levels: int = 10,
                   lot_per_level: float = 0.01, grid_type: str = "symmetric") -> dict:
        upper = center_price * (1 + range_pct / 100)
        lower = center_price * (1 - range_pct / 100)
        step = (upper - lower) / (n_levels - 1)
        buy_levels = [{"price": round(lower + i * step, 5), "lots": lot_per_level, "side": "buy"}
                      for i in range(n_levels // 2)]
        sell_levels = [{"price": round(center_price + (i + 1) * step, 5), "lots": lot_per_level, "side": "sell"}
                       for i in range(n_levels // 2)]
        return {
            "strategy": f"grid_{grid_type}",
            "center": round(center_price, 5),
            "range": f"{round(lower, 5)} — {round(upper, 5)}",
            "step_size": round(step, 5),
            "buy_orders": buy_levels,
            "sell_orders": sell_levels,
            "total_lots": round(lot_per_level * n_levels, 2),
            "max_risk": f"All {n_levels // 2} buy levels filled = {round(lot_per_level * n_levels // 2, 2)} lots long",
            "WARNING": "Grid trading has UNLIMITED risk if price trends beyond grid. Always use a master stop-loss.",
        }

    @staticmethod
    def profit_calculator(step_pips: float, lot_per_level: float, pip_value: float = 10.0,
                          fill_rate: float = 0.7) -> dict:
        profit_per_cycle = step_pips * pip_value * lot_per_level
        return {
            "profit_per_grid_cycle": round(profit_per_cycle, 2),
            "estimated_daily_cycles": round(fill_rate * 3, 1),
            "estimated_daily_profit": round(profit_per_cycle * fill_rate * 3, 2),
            "note": "Profits depend on price oscillating within the grid. Trending = losses.",
        }

    @staticmethod
    def adaptive_grid(df_ohlc, center_price: float, lookback: int = 50,
                      lot_per_level: float = 0.01, n_levels: int = 10) -> dict:
        """ATR-adaptive grid that adjusts spacing to current volatility."""
        import pandas as pd
        atr = (df_ohlc["high"] - df_ohlc["low"]).rolling(lookback).mean().iloc[-1]
        range_pct = (atr * 3 / center_price) * 100
        grid = GridTradingEngine.build_grid(center_price, range_pct, n_levels, lot_per_level)
        grid["strategy"] = "grid_adaptive_atr"
        grid["atr"] = round(atr, 5)
        grid["auto_range_pct"] = round(range_pct, 2)
        return grid

    @staticmethod
    def grid_monitor(open_orders: list[dict], current_price: float) -> dict:
        """Monitor grid fill status and P&L."""
        filled_buys = [o for o in open_orders if o["side"] == "buy" and current_price > o["price"]]
        filled_sells = [o for o in open_orders if o["side"] == "sell" and current_price < o["price"]]
        unrealized_pnl = sum((current_price - o["price"]) * o.get("lots", 0.01) * 100000 for o in filled_buys)
        unrealized_pnl += sum((o["price"] - current_price) * o.get("lots", 0.01) * 100000 for o in filled_sells)
        return {
            "filled_buys": len(filled_buys),
            "filled_sells": len(filled_sells),
            "unrealized_pnl": round(unrealized_pnl, 2),
            "net_exposure": len(filled_buys) - len(filled_sells),
            "status": "BALANCED" if abs(len(filled_buys) - len(filled_sells)) <= 1 else "SKEWED",
        }
```

## Grid Type Selection

| Market Condition | Grid Type | Notes |
| --- | --- | --- |
| Ranging (ADX < 20) | Symmetric | Equal buy/sell levels around center |
| Slight uptrend | Buy-heavy | More buy levels, fewer sell levels |
| High volatility | Adaptive ATR | Wider spacing auto-calculated from ATR |
| Low volatility | Tight fixed | Narrow range, more levels |

## Risk Rules

1. **Always set a master stop-loss** outside the grid — grid trading has unlimited risk without one
2. **Best in ranging markets** — use with `market-regime-classifier` to confirm RANGING regime
3. **Monitor net exposure** — if all buys fill and no sells, you have concentrated directional risk
4. **Scale lots down** for wider grids — total exposure = lot_per_level x n_levels
5. **Avoid during news events** — sudden moves can blow through entire grid
