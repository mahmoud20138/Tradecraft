---
name: spread-slippage-cost-analyzer
description: >
  Measure real execution costs, compare brokers, detect hidden fees and spread widening. Use this
  skill for "spread analysis", "slippage", "execution cost", "broker comparison", "hidden fees",
  "spread widening", "cost of trading", "true spread", "execution quality", "tick cost analysis",
  "best broker", or any question about trading costs. Works with mt5-chart-browser for tick data
  and trade-journal-performance for actual execution data.
kind: analyzer
category: trading/execution
status: active
tags: [analyzer, cost, execution, mt5, slippage, spread, trading]
related_skills: [execution-algo-trading, market-making-hft, tick-data-storage, hedgequantx-prop-trading, market-impact-model]
---

# Spread & Slippage Cost Analyzer

```python
import pandas as pd
import numpy as np

class CostAnalyzer:

    @staticmethod
    def spread_statistics(ticks: pd.DataFrame) -> dict:
        """Comprehensive spread analysis from tick data."""
        spread = ticks["ask"] - ticks["bid"]
        spread_pips = spread * 10000
        return {
            "avg_spread_pips": round(spread_pips.mean(), 2),
            "median_spread_pips": round(spread_pips.median(), 2),
            "min_spread_pips": round(spread_pips.min(), 2),
            "max_spread_pips": round(spread_pips.max(), 2),
            "std_spread_pips": round(spread_pips.std(), 2),
            "p95_spread_pips": round(spread_pips.quantile(0.95), 2),
            "spread_widening_events": int((spread_pips > spread_pips.quantile(0.95)).sum()),
            "pct_time_above_2x_avg": round((spread_pips > 2 * spread_pips.mean()).mean() * 100, 1),
        }

    @staticmethod
    def spread_by_session(ticks: pd.DataFrame) -> dict:
        """Spread behavior per session — find when spreads are tightest."""
        ticks = ticks.copy()
        ticks["spread_pips"] = (ticks["ask"] - ticks["bid"]) * 10000
        ticks["hour"] = ticks.index.hour
        ticks["session"] = ticks["hour"].apply(lambda h:
            "tokyo" if h < 7 else "london" if h < 13 else "overlap" if h < 16 else "ny_late" if h < 22 else "off")
        return ticks.groupby("session")["spread_pips"].agg(["mean", "median", "max"]).round(2).to_dict()

    @staticmethod
    def slippage_analysis(trades: pd.DataFrame) -> dict:
        """Analyze actual slippage from trade execution data."""
        if "expected_price" not in trades.columns or "actual_price" not in trades.columns:
            return {"error": "Need expected_price and actual_price columns"}
        trades = trades.copy()
        trades["slippage"] = (trades["actual_price"] - trades["expected_price"]).abs() * 10000
        return {
            "avg_slippage_pips": round(trades["slippage"].mean(), 2),
            "max_slippage_pips": round(trades["slippage"].max(), 2),
            "pct_positive_slippage": round((trades["actual_price"] > trades["expected_price"]).mean() * 100, 1),
            "total_slippage_cost_pips": round(trades["slippage"].sum(), 1),
            "slippage_per_lot": round(trades["slippage"].mean() * 10, 2),  # USD per lot
        }

    @staticmethod
    def cost_impact_on_strategy(avg_spread: float, avg_slippage: float,
                                 trades_per_year: int, avg_profit_per_trade: float) -> dict:
        """Calculate what % of profit goes to costs."""
        cost_per_trade = avg_spread + avg_slippage
        annual_cost = cost_per_trade * trades_per_year
        annual_profit_gross = avg_profit_per_trade * trades_per_year
        cost_pct = cost_per_trade / max(abs(avg_profit_per_trade), 0.01) * 100
        return {
            "cost_per_trade_pips": round(cost_per_trade, 2),
            "annual_cost_pips": round(annual_cost, 1),
            "cost_as_pct_of_profit": round(cost_pct, 1),
            "net_profit_ratio": round(1 - cost_pct / 100, 3),
            "verdict": "ACCEPTABLE" if cost_pct < 30 else "HIGH — consider fewer trades or tighter broker" if cost_pct < 60 else "CRITICAL — costs eating profits",
        }

    @staticmethod
    def broker_comparison(broker_data: list[dict]) -> pd.DataFrame:
        """Compare multiple brokers on cost metrics."""
        return pd.DataFrame(broker_data).sort_values("avg_spread_pips")
```
