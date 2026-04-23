---
name: backtest-report-generator
description: >
  Generates publication-quality backtest reports with equity curves, Monte Carlo simulations,
  tearsheets, and comprehensive risk analysis. Use this skill whenever the user asks to
  "generate a backtest report", "create tearsheet", "equity curve", "Monte Carlo simulation",
  "strategy report", "performance tearsheet", "backtest results", "drawdown analysis",
  "strategy statistics", "risk report", "publish backtest", "PDF report", "HTML report",
  or any request to visualize and document strategy backtesting results. Works with
  quant-trading-pipeline for backtest data and trading-data-science for statistics.
kind: generator
category: trading/quant
status: active
tags: [backtest, backtesting, drawdown, generator, monte-carlo, quant, report, risk-and-portfolio]
related_skills: [backtesting-sim, hurst-exponent-dynamics-crisis-prediction, ml-trading, quant-ml-trading, statistics-timeseries]
---

# Backtest Report Generator

## Overview
Transforms raw backtest results into professional reports with full statistical analysis,
equity curves, drawdown visualization, Monte Carlo simulation, and distribution analysis.
Outputs as HTML (interactive) or PDF.

---

## 1. Report Data Structure

```python
import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
from typing import Optional

def compute_tearsheet(
    equity_curve: pd.Series,
    returns: pd.Series,
    trades_df: Optional[pd.DataFrame] = None,
    benchmark_returns: Optional[pd.Series] = None,
    risk_free_rate: float = 0.04,
) -> dict:
    """Compute comprehensive strategy tearsheet metrics."""
    annual_factor = 252
    total_return = (equity_curve.iloc[-1] / equity_curve.iloc[0]) - 1
    years = len(returns) / annual_factor
    cagr = (1 + total_return) ** (1 / max(years, 0.01)) - 1

    # Drawdown analysis
    peak = equity_curve.cummax()
    dd = (equity_curve - peak) / peak
    max_dd = dd.min()
    dd_durations = []
    in_dd = False
    start = None
    for i, d in enumerate(dd):
        if d < 0 and not in_dd:
            in_dd = True
            start = i
        elif d == 0 and in_dd:
            in_dd = False
            dd_durations.append(i - start)

    # Risk metrics
    vol = returns.std() * np.sqrt(annual_factor)
    sharpe = (returns.mean() * annual_factor - risk_free_rate) / max(vol, 1e-10)
    downside_ret = returns[returns < 0]
    sortino = (returns.mean() * annual_factor - risk_free_rate) / (downside_ret.std() * np.sqrt(annual_factor)) if len(downside_ret) > 0 else 0
    calmar = cagr / abs(max_dd) if max_dd != 0 else 0
    var_95 = returns.quantile(0.05)
    cvar_95 = returns[returns <= var_95].mean()

    # Win/loss analysis from trades
    trade_stats = {}
    if trades_df is not None and not trades_df.empty:
        closed = trades_df[trades_df["pnl_pips"].notna()]
        wins = closed[closed["pnl_pips"] > 0]
        losses = closed[closed["pnl_pips"] <= 0]
        trade_stats = {
            "total_trades": len(closed),
            "win_rate": round(len(wins) / max(len(closed), 1) * 100, 1),
            "avg_win": round(wins["pnl_pips"].mean(), 1) if len(wins) > 0 else 0,
            "avg_loss": round(losses["pnl_pips"].mean(), 1) if len(losses) > 0 else 0,
            "profit_factor": round(wins["pnl_usd"].sum() / abs(losses["pnl_usd"].sum()), 2) if len(losses) > 0 and losses["pnl_usd"].sum() != 0 else float("inf"),
            "expectancy_pips": round(closed["pnl_pips"].mean(), 2),
            "largest_win": round(wins["pnl_pips"].max(), 1) if len(wins) > 0 else 0,
            "largest_loss": round(losses["pnl_pips"].min(), 1) if len(losses) > 0 else 0,
            "avg_hold_bars": "from timestamps",
        }

    return {
        "summary": {
            "total_return": round(total_return * 100, 2),
            "cagr": round(cagr * 100, 2),
            "sharpe": round(sharpe, 3),
            "sortino": round(sortino, 3),
            "calmar": round(calmar, 3),
            "volatility": round(vol * 100, 2),
            "max_drawdown": round(max_dd * 100, 2),
            "avg_drawdown_duration": round(np.mean(dd_durations), 0) if dd_durations else 0,
            "max_drawdown_duration": max(dd_durations) if dd_durations else 0,
            "var_95": round(var_95 * 100, 4),
            "cvar_95": round(cvar_95 * 100, 4),
        },
        "trade_stats": trade_stats,
        "period": f"{equity_curve.index[0]} → {equity_curve.index[-1]}",
        "bars": len(returns),
        "years": round(years, 2),
    }
```

---

## 2. Monte Carlo Simulation

```python
def monte_carlo_simulation(
    returns: pd.Series,
    n_simulations: int = 1000,
    n_periods: int = 252,
    initial_capital: float = 10000,
    confidence_levels: list[float] = [0.05, 0.25, 0.50, 0.75, 0.95],
) -> dict:
    """
    Bootstrap Monte Carlo — resample from actual returns to generate
    distribution of possible outcomes. Tests strategy robustness.
    """
    np.random.seed(42)
    all_paths = np.zeros((n_simulations, n_periods))

    for sim in range(n_simulations):
        sampled = np.random.choice(returns.values, size=n_periods, replace=True)
        equity = initial_capital * np.cumprod(1 + sampled)
        all_paths[sim] = equity

    final_values = all_paths[:, -1]
    max_drawdowns = []
    for path in all_paths:
        peak = np.maximum.accumulate(path)
        dd = (path - peak) / peak
        max_drawdowns.append(dd.min())

    percentiles = {f"p{int(cl*100)}": round(np.percentile(final_values, cl * 100), 2) for cl in confidence_levels}
    dd_percentiles = {f"p{int(cl*100)}": round(np.percentile(max_drawdowns, cl * 100) * 100, 2) for cl in confidence_levels}

    return {
        "n_simulations": n_simulations,
        "n_periods": n_periods,
        "initial_capital": initial_capital,
        "final_value_percentiles": percentiles,
        "median_final": round(np.median(final_values), 2),
        "mean_final": round(np.mean(final_values), 2),
        "prob_profit": round((final_values > initial_capital).mean() * 100, 1),
        "prob_double": round((final_values > initial_capital * 2).mean() * 100, 1),
        "prob_ruin_50pct": round((final_values < initial_capital * 0.5).mean() * 100, 1),
        "max_drawdown_percentiles": dd_percentiles,
        "worst_case_dd": round(min(max_drawdowns) * 100, 2),
        "paths_summary": "Use all_paths array for visualization",
    }
```

---

## 3. HTML Report Generator

```python
def generate_html_report(tearsheet: dict, monte_carlo: dict, strategy_name: str = "Strategy") -> str:
    """Generate a standalone HTML report with charts using Chart.js."""
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{strategy_name} Backtest Report</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body {{ font-family: -apple-system, sans-serif; margin: 40px; background: #0f0f1a; color: #e0e0e0; }}
.card {{ background: #1a1a2e; border-radius: 12px; padding: 24px; margin: 16px 0; }}
.metric {{ display: inline-block; margin: 12px 24px; text-align: center; }}
.metric .value {{ font-size: 28px; font-weight: bold; }}
.metric .label {{ font-size: 12px; color: #888; }}
.green {{ color: #00e676; }} .red {{ color: #ff5252; }} .yellow {{ color: #ffd740; }}
h1 {{ color: #7c4dff; }} h2 {{ color: #448aff; border-bottom: 1px solid #333; padding-bottom: 8px; }}
table {{ width: 100%; border-collapse: collapse; }}
th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #333; }}
th {{ color: #888; }}
</style></head><body>
<h1>{strategy_name} — Backtest Report</h1>
<p>Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}</p>

<div class="card"><h2>Performance Summary</h2>
<div class="metric"><div class="value {'green' if tearsheet['summary']['total_return'] > 0 else 'red'}">{tearsheet['summary']['total_return']}%</div><div class="label">Total Return</div></div>
<div class="metric"><div class="value">{tearsheet['summary']['cagr']}%</div><div class="label">CAGR</div></div>
<div class="metric"><div class="value">{tearsheet['summary']['sharpe']}</div><div class="label">Sharpe</div></div>
<div class="metric"><div class="value">{tearsheet['summary']['sortino']}</div><div class="label">Sortino</div></div>
<div class="metric"><div class="value red">{tearsheet['summary']['max_drawdown']}%</div><div class="label">Max DD</div></div>
<div class="metric"><div class="value">{tearsheet['summary']['volatility']}%</div><div class="label">Volatility</div></div>
</div>

<div class="card"><h2>Trade Statistics</h2>
<table><tr><th>Metric</th><th>Value</th></tr>
{''.join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in tearsheet.get('trade_stats', {}).items())}
</table></div>

<div class="card"><h2>Monte Carlo Analysis ({monte_carlo['n_simulations']} simulations)</h2>
<div class="metric"><div class="value green">{monte_carlo['prob_profit']}%</div><div class="label">Probability of Profit</div></div>
<div class="metric"><div class="value">{monte_carlo['median_final']}</div><div class="label">Median Final Value</div></div>
<div class="metric"><div class="value red">{monte_carlo['prob_ruin_50pct']}%</div><div class="label">Prob of 50% Loss</div></div>
<div class="metric"><div class="value red">{monte_carlo['worst_case_dd']}%</div><div class="label">Worst DD</div></div>
</div>

<div class="card"><h2>Risk Metrics</h2>
<table><tr><th>Metric</th><th>Value</th></tr>
<tr><td>VaR (95%)</td><td>{tearsheet['summary']['var_95']}%</td></tr>
<tr><td>CVaR (95%)</td><td>{tearsheet['summary']['cvar_95']}%</td></tr>
<tr><td>Calmar Ratio</td><td>{tearsheet['summary']['calmar']}</td></tr>
<tr><td>Avg DD Duration</td><td>{tearsheet['summary']['avg_drawdown_duration']} bars</td></tr>
</table></div>

<div class="card" style="background:#2a1a1a; border: 1px solid #ff5252;">
<strong style="color:#ff5252;">⚠ DISCLAIMER:</strong> Past performance does not guarantee future results.
This backtest may suffer from overfitting, survivorship bias, data snooping, and transaction cost
underestimation. Walk-forward out-of-sample validation is required before live deployment.
</div>
</body></html>"""
```

---

## Usage Conventions
1. **Always include Monte Carlo** — single-path equity curves are meaningless
2. **Always include the disclaimer** — non-negotiable
3. **Report both gross and net** (after costs) — gross backtest results are misleading
4. **Walk-forward OOS section** must be included if available
5. **Compare to benchmark** when possible (buy-and-hold, random)


---
