---
name: strategy-validation
description: "End-to-end strategy validation — backtest tearsheet (Sharpe, Sortino, Calmar, VaR), walk-forward optimization, Monte Carlo stress testing, parameter sensitivity heatmaps, and strategy A/B testing. Use for validate strategy, backtest report, walk-forward, Monte Carlo test, parameter sensitivity, or any strategy validation."
kind: reference
category: trading/quant
status: active
tags: [backtesting, monte-carlo, quant, strategy, trading, validation]
related_skills: [backtesting-sim, backtest-report-generator, hurst-exponent-dynamics-crisis-prediction, ml-trading, quant-ml-trading]
---

# Strategy Validation — Tearsheet, WFO, Monte Carlo, Sensitivity, A/B Testing

## Overview
End-to-end strategy validation pipeline:
1. **Backtest Tearsheet** — Sharpe, Sortino, Calmar, VaR, CVaR, Win Rate, HTML report
2. **Walk-Forward Optimization** — anchored and rolling WFO with OOS validation
3. **Monte Carlo Stress Testing** — bootstrap, parameter perturbation, regime shuffle
4. **Parameter Sensitivity** — 2D grid sweep, robustness heatmaps, one-at-a-time
5. **Strategy A/B Testing** — paired t-test, Wilcoxon, KS test, Jobson-Korkie Sharpe diff

---

## Section 1: Backtest Tearsheet

```python
import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
from typing import Optional

def compute_tearsheet(equity_curve: pd.Series, returns: pd.Series,
                      trades_df: Optional[pd.DataFrame] = None,
                      benchmark_returns: Optional[pd.Series] = None,
                      risk_free_rate: float = 0.04) -> dict:
    """Compute comprehensive strategy tearsheet metrics."""
    annual_factor = 252
    total_return = (equity_curve.iloc[-1] / equity_curve.iloc[0]) - 1
    years = len(returns) / annual_factor
    cagr = (1 + total_return) ** (1 / max(years, 0.01)) - 1
    peak = equity_curve.cummax()
    dd = (equity_curve - peak) / peak
    max_dd = dd.min()
    dd_durations = []
    in_dd = False; start = None
    for i, d in enumerate(dd):
        if d < 0 and not in_dd: in_dd = True; start = i
        elif d == 0 and in_dd: in_dd = False; dd_durations.append(i - start)
    vol = returns.std() * np.sqrt(annual_factor)
    sharpe = (returns.mean() * annual_factor - risk_free_rate) / max(vol, 1e-10)
    downside_ret = returns[returns < 0]
    sortino = ((returns.mean() * annual_factor - risk_free_rate) /
               (downside_ret.std() * np.sqrt(annual_factor)) if len(downside_ret) > 0 else 0)
    calmar = cagr / abs(max_dd) if max_dd != 0 else 0
    var_95 = returns.quantile(0.05)
    cvar_95 = returns[returns <= var_95].mean()
    trade_stats = {}
    if trades_df is not None and not trades_df.empty:
        closed = trades_df[trades_df["pnl_pips"].notna()]
        wins = closed[closed["pnl_pips"] > 0]; losses = closed[closed["pnl_pips"] <= 0]
        trade_stats = {
            "total_trades": len(closed), "win_rate": round(len(wins) / max(len(closed), 1) * 100, 1),
            "avg_win": round(wins["pnl_pips"].mean(), 1) if len(wins) > 0 else 0,
            "avg_loss": round(losses["pnl_pips"].mean(), 1) if len(losses) > 0 else 0,
            "profit_factor": round(wins["pnl_usd"].sum() / abs(losses["pnl_usd"].sum()), 2) if len(losses) > 0 and losses["pnl_usd"].sum() != 0 else float("inf"),
            "expectancy_pips": round(closed["pnl_pips"].mean(), 2),
            "largest_win": round(wins["pnl_pips"].max(), 1) if len(wins) > 0 else 0,
            "largest_loss": round(losses["pnl_pips"].min(), 1) if len(losses) > 0 else 0,
        }
    return {
        "summary": {"total_return": round(total_return * 100, 2), "cagr": round(cagr * 100, 2),
                    "sharpe": round(sharpe, 3), "sortino": round(sortino, 3), "calmar": round(calmar, 3),
                    "volatility": round(vol * 100, 2), "max_drawdown": round(max_dd * 100, 2),
                    "avg_drawdown_duration": round(np.mean(dd_durations), 0) if dd_durations else 0,
                    "max_drawdown_duration": max(dd_durations) if dd_durations else 0,
                    "var_95": round(var_95 * 100, 4), "cvar_95": round(cvar_95 * 100, 4)},
        "trade_stats": trade_stats,
        "period": f"{equity_curve.index[0]} → {equity_curve.index[-1]}",
        "bars": len(returns), "years": round(years, 2),
    }

def generate_html_report(tearsheet: dict, monte_carlo: dict, strategy_name: str = "Strategy") -> str:
    """Generate a standalone HTML report with Chart.js."""
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{strategy_name} Backtest Report</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>body{{font-family:-apple-system,sans-serif;margin:40px;background:#0f0f1a;color:#e0e0e0}}
.card{{background:#1a1a2e;border-radius:12px;padding:24px;margin:16px 0}}
.metric{{display:inline-block;margin:12px 24px;text-align:center}}
.metric .value{{font-size:28px;font-weight:bold}}.metric .label{{font-size:12px;color:#888}}
.green{{color:#00e676}}.red{{color:#ff5252}}.yellow{{color:#ffd740}}
h1{{color:#7c4dff}}h2{{color:#448aff;border-bottom:1px solid #333;padding-bottom:8px}}
table{{width:100%;border-collapse:collapse}}th,td{{padding:8px 12px;text-align:left;border-bottom:1px solid #333}}
th{{color:#888}}</style></head><body>
<h1>{strategy_name} — Backtest Report</h1>
<p>Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}</p>
<div class="card"><h2>Performance Summary</h2>
<div class="metric"><div class="value {'green' if tearsheet['summary']['total_return'] > 0 else 'red'}">{tearsheet['summary']['total_return']}%</div><div class="label">Total Return</div></div>
<div class="metric"><div class="value">{tearsheet['summary']['cagr']}%</div><div class="label">CAGR</div></div>
<div class="metric"><div class="value">{tearsheet['summary']['sharpe']}</div><div class="label">Sharpe</div></div>
<div class="metric"><div class="value">{tearsheet['summary']['sortino']}</div><div class="label">Sortino</div></div>
<div class="metric"><div class="value red">{tearsheet['summary']['max_drawdown']}%</div><div class="label">Max DD</div></div>
</div>
<div class="card"><h2>Trade Statistics</h2><table><tr><th>Metric</th><th>Value</th></tr>
{''.join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in tearsheet.get('trade_stats', {}).items())}
</table></div>
<div class="card" style="background:#2a1a1a;border:1px solid #ff5252;">
<strong style="color:#ff5252;">⚠ DISCLAIMER:</strong> Past performance does not guarantee future results.
Walk-forward out-of-sample validation required before live deployment.
</div></body></html>"""
```

---

## Section 2: Walk-Forward Optimization

```python
from typing import Callable

class WalkForwardOptimizer:
    @staticmethod
    def anchored_wfo(data: pd.DataFrame, strategy_fn: Callable, optimize_fn: Callable,
                     train_pct: float = 0.7, n_folds: int = 5) -> dict:
        """Anchored WFO: training window grows, test window is fixed."""
        total = len(data); test_size = total // (n_folds + 1); results = []
        for fold in range(n_folds):
            train_end = total - test_size * (n_folds - fold)
            test_end = train_end + test_size
            train = data.iloc[:train_end]; test = data.iloc[train_end:test_end]
            best_params = optimize_fn(train)
            oos_returns = strategy_fn(test, best_params)
            sharpe = (oos_returns.mean() / oos_returns.std()) * np.sqrt(252) if oos_returns.std() > 0 else 0
            results.append({"fold": fold, "train_size": len(train), "test_size": len(test),
                            "params": best_params, "oos_sharpe": round(sharpe, 3),
                            "oos_return": round(oos_returns.sum() * 100, 2),
                            "oos_trades": len(oos_returns[oos_returns != 0])})
        avg_oos_sharpe = np.mean([r["oos_sharpe"] for r in results])
        stabilities = []
        params_list = [r["params"] for r in results if isinstance(r["params"], dict)]
        if params_list:
            for key in params_list[0]:
                vals = [p.get(key) for p in params_list if isinstance(p.get(key), (int, float))]
                if vals and np.mean(vals) != 0:
                    stabilities.append(max(1 - np.std(vals) / abs(np.mean(vals)), 0))
        param_stability = round(np.mean(stabilities), 3) if stabilities else 0
        return {
            "method": "anchored_walk_forward", "n_folds": n_folds, "fold_results": results,
            "avg_oos_sharpe": round(avg_oos_sharpe, 3), "param_stability": param_stability,
            "verdict": "ROBUST" if avg_oos_sharpe > 0.5 and param_stability > 0.6
                      else "MARGINAL" if avg_oos_sharpe > 0
                      else "FAILED — strategy does not generalize",
        }

    @staticmethod
    def rolling_wfo(data: pd.DataFrame, strategy_fn: Callable, optimize_fn: Callable,
                    train_bars: int = 500, test_bars: int = 100) -> dict:
        """Rolling WFO: fixed-size training window moves forward."""
        results = []
        for start in range(0, len(data) - train_bars - test_bars, test_bars):
            train = data.iloc[start:start + train_bars]
            test = data.iloc[start + train_bars:start + train_bars + test_bars]
            best_params = optimize_fn(train)
            oos_returns = strategy_fn(test, best_params)
            sharpe = (oos_returns.mean() / oos_returns.std()) * np.sqrt(252) if oos_returns.std() > 0 else 0
            results.append({"fold": len(results), "params": best_params, "oos_sharpe": round(sharpe, 3)})
        return {"method": "rolling_walk_forward", "n_folds": len(results),
                "avg_oos_sharpe": round(np.mean([r["oos_sharpe"] for r in results]), 3), "fold_results": results}
```

---

## Section 3: Monte Carlo Stress Testing

```python
class MonteCarloStressTester:
    @staticmethod
    def monte_carlo_simulation(returns: pd.Series, n_simulations: int = 1000,
                               n_periods: int = 252, initial_capital: float = 10000) -> dict:
        np.random.seed(42)
        all_paths = np.zeros((n_simulations, n_periods))
        for sim in range(n_simulations):
            sampled = np.random.choice(returns.values, size=n_periods, replace=True)
            all_paths[sim] = initial_capital * np.cumprod(1 + sampled)
        final_values = all_paths[:, -1]
        max_drawdowns = []
        for path in all_paths:
            peak = np.maximum.accumulate(path)
            max_drawdowns.append((path - peak).min() / peak.max())
        return {
            "n_simulations": n_simulations,
            "median_final": round(np.median(final_values), 2),
            "p5_final": round(np.percentile(final_values, 5), 2),
            "p95_final": round(np.percentile(final_values, 95), 2),
            "prob_profit": round((final_values > initial_capital).mean() * 100, 1),
            "prob_ruin_50pct": round((final_values < initial_capital * 0.5).mean() * 100, 1),
            "worst_case_dd": round(min(max_drawdowns) * 100, 2),
            "median_max_dd": round(np.median(max_drawdowns) * 100, 2),
        }

    @staticmethod
    def parameter_perturbation(strategy_fn, base_params: dict, data: pd.DataFrame,
                                perturbation_pct: float = 0.1, n_tests: int = 100) -> dict:
        results = []
        for _ in range(n_tests):
            perturbed = {}
            for k, v in base_params.items():
                if isinstance(v, (int, float)):
                    delta = v * perturbation_pct * np.random.uniform(-1, 1)
                    perturbed[k] = type(v)(v + delta)
                else: perturbed[k] = v
            try:
                ret = strategy_fn(data, perturbed)
                sharpe = (ret.mean() / ret.std()) * np.sqrt(252) if ret.std() > 0 else 0
                results.append({"params": perturbed, "sharpe": sharpe})
            except: results.append({"params": perturbed, "sharpe": -999})
        sharpes = [r["sharpe"] for r in results if r["sharpe"] > -999]
        return {
            "type": "parameter_perturbation", "n_tests": n_tests,
            "mean_sharpe": round(np.mean(sharpes), 3), "std_sharpe": round(np.std(sharpes), 3),
            "pct_profitable": round(sum(1 for s in sharpes if s > 0) / max(len(sharpes), 1) * 100, 1),
            "verdict": "ROBUST" if np.mean(sharpes) > 0.3 else "FRAGILE — parameter-sensitive",
        }
```

---

## Section 4: Parameter Sensitivity

```python
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, base64

class ParameterSensitivity:
    @staticmethod
    def grid_sweep_2d(strategy_fn, data: pd.DataFrame, param_a: dict, param_b: dict,
                      fixed_params: dict = None) -> dict:
        """Sweep two parameters, compute Sharpe at each combination."""
        fixed = fixed_params or {}
        results = np.zeros((len(param_a["values"]), len(param_b["values"])))
        for i, va in enumerate(param_a["values"]):
            for j, vb in enumerate(param_b["values"]):
                params = {**fixed, param_a["name"]: va, param_b["name"]: vb}
                try:
                    ret = strategy_fn(data, params)
                    results[i, j] = (ret.mean() / ret.std()) * np.sqrt(252) if ret.std() > 0 else 0
                except: results[i, j] = np.nan
        best_idx = np.unravel_index(np.nanargmax(results), results.shape)
        peak = results[best_idx]
        neighbors = results[max(0, best_idx[0]-1):best_idx[0]+2, max(0, best_idx[1]-1):best_idx[1]+2]
        flatness = 1 - np.nanstd(neighbors) / max(abs(peak), 0.01)
        return {
            "param_a": param_a["name"], "param_b": param_b["name"], "matrix": results.tolist(),
            "best": {param_a["name"]: param_a["values"][best_idx[0]],
                     param_b["name"]: param_b["values"][best_idx[1]], "sharpe": round(peak, 3)},
            "flatness": round(flatness, 3), "robust": flatness > 0.7,
            "note": "Flat surface = robust. Spiky surface = overfit." if flatness < 0.5 else "Good parameter stability.",
        }

    @staticmethod
    def render_heatmap(result: dict, save_path: str = None) -> str:
        fig, ax = plt.subplots(figsize=(10, 8), facecolor="#131722")
        ax.set_facecolor("#131722")
        matrix = np.array(result["matrix"])
        im = ax.imshow(matrix, cmap="RdYlGn", aspect="auto", interpolation="nearest")
        ax.set_xlabel(result["param_b"], color="#e0e0e0")
        ax.set_ylabel(result["param_a"], color="#e0e0e0")
        ax.set_title(f"Sharpe Sensitivity: {result['param_a']} vs {result['param_b']}", color="#e0e0e0")
        plt.colorbar(im, label="Sharpe Ratio")
        ax.tick_params(colors="#787b86")
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", facecolor="#131722")
        plt.close(fig); buf.seek(0)
        if save_path:
            with open(save_path, "wb") as f: f.write(buf.read())
            buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")
```

---

## Section 5: Strategy A/B Testing

```python
class StrategyABTester:
    @staticmethod
    def compare(returns_a: pd.Series, returns_b: pd.Series,
                name_a: str = "Strategy A", name_b: str = "Strategy B",
                risk_free: float = 0.04/252) -> dict:
        def metrics(r, name):
            sharpe = (r.mean() - risk_free) / r.std() * np.sqrt(252) if r.std() > 0 else 0
            equity = (1 + r).cumprod()
            max_dd = ((equity / equity.cummax()) - 1).min()
            return {"name": name, "total_return": round((equity.iloc[-1] - 1) * 100, 2),
                    "sharpe": round(sharpe, 3), "max_drawdown": round(max_dd * 100, 2),
                    "win_rate": round((r > 0).mean() * 100, 1)}
        m_a = metrics(returns_a, name_a); m_b = metrics(returns_b, name_b)
        n = min(len(returns_a), len(returns_b))
        t_stat, t_pval = stats.ttest_rel(returns_a.values[:n], returns_b.values[:n])
        try: w_stat, w_pval = stats.wilcoxon(returns_a.values[:n], returns_b.values[:n])
        except: w_stat, w_pval = 0, 1.0
        ks_stat, ks_pval = stats.ks_2samp(returns_a.values, returns_b.values)
        better = name_a if m_a["sharpe"] > m_b["sharpe"] else name_b
        return {
            "strategy_a": m_a, "strategy_b": m_b, "winner": better,
            "statistically_significant": t_pval < 0.05,
            "tests": {"paired_ttest": {"t_stat": round(t_stat, 3), "p_value": round(t_pval, 4)},
                      "wilcoxon": {"p_value": round(float(w_pval), 4)},
                      "ks_test": {"p_value": round(ks_pval, 4)}},
            "verdict": f"{better} is {'SIGNIFICANTLY' if t_pval < 0.05 else 'NOT significantly'} better (p={t_pval:.4f})",
        }
```

## Validation Workflow
```
1. compute_tearsheet()          ← Sharpe, Sortino, Calmar, VaR, CVaR
2. monte_carlo_simulation()     ← Probability of profit, ruin risk
3. WalkForwardOptimizer         ← OOS: does the edge generalize?
4. parameter_perturbation()     ← Robustness: ±10% parameters = still works?
5. grid_sweep_2d() + heatmap    ← Flat surface = robust, spiky = overfit
6. StrategyABTester.compare()   ← Is variant A statistically better?
7. generate_html_report()       ← Publish with disclaimer
```
| Test | Pass Criteria |
|------|--------------|
| OOS Sharpe (WFO) | > 0.5 across folds |
| Parameter Stability | > 0.6 across folds |
| Bootstrap Prob Profit | > 80% |
| Perturbation Robustness | > 70% profitable |
| Heatmap Flatness | > 0.7 |
| A/B p-value | < 0.05 |

---

## Sharpe Ratio as Validation Metric (Wall Street Quants)

> Source: "The Sharpe Ratio Explained (by a quant trader)" by Wall Street Quants (Aug 2024)

- **t-statistic = SR * sqrt(N trading days)** — the Sharpe ratio directly determines the statistical significance of a strategy's returns. A higher SR over more trading days yields a larger t-stat, making it easier to reject the null hypothesis that returns equal zero.
- A strategy's SR automatically **rank-orders it against alternatives** by the confidence that returns are greater than zero. No separate hypothesis test is needed; SR itself encodes that ranking.
- **Benchmarks**: S&P 500 ~0.45, Buffett ~0.75, good hedge funds 2.0+, near-arbitrage strategies ~20.
- **Low-SR high-return strategies are NOT superior** to high-SR low-return strategies, because leverage preserves the Sharpe ratio while scaling returns. A strategy with SR 2.0 and 5% return can be levered to 20% return while maintaining SR 2.0, whereas a strategy with SR 0.3 and 20% return cannot improve its SR through leverage.
- **When comparing strategies**: prefer the higher SR, then lever to the desired return level. This principle makes SR the single most important metric for strategy selection in quantitative finance.
