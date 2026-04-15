---
name: market-impact-model
description: >
  Estimate your own orders' market impact and optimize execution for larger accounts. Use this
  skill whenever the user asks about "market impact", "slippage model", "order impact", "large
  order execution", "TWAP", "VWAP execution", "implementation shortfall", "transaction cost
  analysis", "TCA", "optimal execution speed", "Almgren-Chriss", or any question about executing
  larger positions without moving the market. Works with execution-algo-trading and
  market-microstructure-analyzer.
kind: reference
category: trading/execution
status: active
tags: [execution, impact, market, model, trading]
related_skills: [execution-algo-trading, market-making-hft, tick-data-storage, analyze, hedgequantx-prop-trading]
---

# Market Impact Model

```python
import numpy as np
from dataclasses import dataclass

@dataclass
class MarketParams:
    daily_volume: float          # average daily volume in lots
    avg_spread_pips: float
    volatility_daily_pips: float
    symbol: str = ""

class MarketImpactModel:

    @staticmethod
    def almgren_chriss_impact(order_size_lots: float, market: MarketParams,
                               urgency: float = 0.5) -> dict:
        """
        Almgren-Chriss market impact model.
        Estimates permanent and temporary impact of an order.
        urgency: 0 (patient) to 1 (aggressive)
        """
        participation_rate = order_size_lots / max(market.daily_volume, 1)
        # Temporary impact (goes away after execution)
        temp_impact = market.avg_spread_pips * 0.5 + market.volatility_daily_pips * participation_rate * urgency * 2
        # Permanent impact (stays)
        perm_impact = market.volatility_daily_pips * np.sqrt(participation_rate) * 0.1
        total_impact = temp_impact + perm_impact
        return {
            "order_size_lots": order_size_lots,
            "participation_rate": round(participation_rate * 100, 2),
            "temporary_impact_pips": round(temp_impact, 2),
            "permanent_impact_pips": round(perm_impact, 2),
            "total_estimated_impact_pips": round(total_impact, 2),
            "cost_in_spread_multiples": round(total_impact / market.avg_spread_pips, 1),
            "recommendation": MarketImpactModel._execution_recommendation(participation_rate, urgency),
        }

    @staticmethod
    def optimal_execution_schedule(order_size_lots: float, market: MarketParams,
                                    execution_hours: float = 4) -> list[dict]:
        """TWAP-style execution schedule to minimize impact."""
        n_slices = max(int(execution_hours * 4), 1)  # One slice per 15 min
        base_size = order_size_lots / n_slices
        schedule = []
        for i in range(n_slices):
            # Vary size: slightly larger at open/close (more liquidity)
            hour = i / 4
            liquidity_factor = 1.2 if hour < 1 or hour > execution_hours - 1 else 0.9
            size = round(base_size * liquidity_factor, 2)
            schedule.append({"slice": i + 1, "lots": max(size, 0.01),
                            "minutes_from_start": i * 15})
        return schedule

    @staticmethod
    def _execution_recommendation(participation: float, urgency: float) -> str:
        if participation < 0.01:
            return "SMALL ORDER — execute immediately, impact negligible"
        if participation < 0.05:
            return "MODERATE — consider splitting into 3-5 slices over 1 hour"
        if participation < 0.15:
            return "LARGE — use TWAP over 2-4 hours, consider limit orders"
        return "VERY LARGE — use TWAP over full session, consider iceberg orders"

    @staticmethod
    def transaction_cost_analysis(trades: list[dict], market: MarketParams) -> dict:
        """Post-trade TCA: measure actual vs expected costs."""
        slippages = [t.get("slippage_pips", 0) for t in trades]
        return {
            "avg_slippage_pips": round(np.mean(slippages), 2),
            "max_slippage_pips": round(max(slippages), 2),
            "total_cost_pips": round(sum(slippages) + len(trades) * market.avg_spread_pips, 2),
            "cost_vs_benchmark": round(np.mean(slippages) / market.avg_spread_pips, 2),
        }
```
