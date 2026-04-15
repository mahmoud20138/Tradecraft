---
name: backtesting-sim
description: >
  Backtesting and simulation: vectorized backtesting, paper trading simulation, strategy A/B
  testing, automated strategy building, natural language to strategy, and trading plan generation.
  USE FOR: backtest, backtesting, paper trading, simulation, strategy builder, A/B test strategies,
  natural language strategy, trading plan, equity curve, drawdown analysis, walk-forward, Monte
  Carlo simulation, performance metrics, Sharpe, Sortino, Calmar, win rate, profit factor,
  expectancy, strategy validation, overfitting prevention, survivorship bias, look-ahead bias.
related_skills:
  - statistics-timeseries
  - backtesting-sim
  - risk-and-portfolio
  - market-data-ingestion
tags:
  - trading
  - quant
  - backtesting
  - simulation
  - paper-trading
  - vectorized
skill_level: intermediate
kind: reference
category: trading/quant
status: active
---
> **Skill:** Backtesting Sim  |  **Domain:** trading  |  **Category:** quantitative  |  **Level:** intermediate
> **Tags:** `trading`, `quant`, `backtesting`, `simulation`, `paper-trading`, `vectorized`


## Vectorized Backtester

# Vectorized Backtester

```python
import pandas as pd
import numpy as np
from typing import Callable, Optional

# ── Shared helpers ──────────────────────────────────────────────────────────

def _sharpe(r: np.ndarray, rfr: float = 0.04 / 252) -> float:
    std = r.std(ddof=1)
    return float((r.mean() - rfr) / std * np.sqrt(252)) if std > 0 else 0.0

def _sortino(r: np.ndarray, rfr: float = 0.04 / 252) -> float:
    down = r[r < rfr]
    std_dn = down.std(ddof=1) if len(down) > 1 else 0.0
    return float((r.mean() - rfr) / std_dn * np.sqrt(252)) if std_dn > 0 else 0.0

def _calmar(r: np.ndarray) -> float:
    eq      = np.cumprod(1 + r)
    peak    = np.maximum.accumulate(eq)
    max_dd  = abs(((eq - peak) / peak).min())
    ann_ret = eq[-1] ** (252 / len(r)) - 1
    return float(ann_ret / max_dd) if max_dd > 0 else 0.0

def _profit_factor(r: np.ndarray) -> float:
    gains  = r[r > 0].sum()
    losses = abs(r[r < 0].sum())
    return float(gains / losses) if losses > 0 else float("inf")


class VectorizedBacktester:
    """
    Production-quality vectorised backtester with full performance metrics.

    Signals must be pre-shifted (no look-ahead bias).
    Supports transaction costs, position sizing, and walk-forward validation.

    Example
    -------
    >>> df["signal"] = np.sign(df["close"].pct_change(5))  # 5-bar momentum
    >>> result = VectorizedBacktester.backtest(df, spread_bps=2.0)
    >>> print(result["sharpe"], result["max_drawdown_pct"])
    1.34  -12.5
    """

    @staticmethod
    def backtest(
        df: pd.DataFrame,
        signal_col: str = "signal",
        spread_bps: float = 2.0,
        slippage_bps: float = 1.0,
        initial_capital: float = 10_000.0,
        position_size: float = 1.0,
        risk_free_annual: float = 0.04,
    ) -> dict:
        """
        Vectorised backtest engine.

        Parameters
        ----------
        df              : OHLCV DataFrame with a signal column
        signal_col      : column name for signal (1=long, -1=short, 0=flat)
        spread_bps      : round-trip spread cost in basis points
        slippage_bps    : round-trip slippage estimate in basis points
        initial_capital : starting capital
        position_size   : fraction of capital at risk (1.0 = fully invested)
        risk_free_annual: used for Sharpe / Sortino calculations

        Returns
        -------
        Comprehensive dict including Sharpe, Sortino, Calmar, max DD,
        win rate, profit factor, equity curve, and full annotated DataFrame.

        Notes
        -----
        ALL signals are shifted by 1 bar to prevent look-ahead.
        Costs are charged on position changes (not every bar).
        """
        if signal_col not in df.columns:
            raise KeyError(f"Column '{signal_col}' not found in DataFrame")
        if len(df) < 10:
            raise ValueError("Need at least 10 bars to backtest")

        out = df.copy()
        cost_rt = (spread_bps + slippage_bps) / 10_000.0   # Round-trip cost fraction

        out["returns"]      = out["close"].pct_change()
        out["position"]     = out[signal_col].shift(1).fillna(0) * position_size
        out["trade"]        = out["position"].diff().abs().fillna(0)
        out["gross_return"] = out["position"] * out["returns"]
        out["cost"]         = out["trade"] * cost_rt
        out["net_return"]   = out["gross_return"] - out["cost"]

        # Equity curve (multiplicative)
        out["equity"]       = initial_capital * (1 + out["net_return"]).cumprod()
        out["peak"]         = out["equity"].cummax()
        out["drawdown"]     = (out["equity"] - out["peak"]) / out["peak"]

        # Trade-level stats
        out["trade_entry"]  = (out["position"] != 0) & (out["position"].shift(1) == 0)
        out["trade_exit"]   = (out["position"] == 0) & (out["position"].shift(1) != 0)
        n_trades            = int(out["trade_entry"].sum())

        net     = out["net_return"].dropna().values
        rfr_d   = risk_free_annual / 252

        # Compute comprehensive metrics from net returns
        total_return = float((out["equity"].iloc[-1] / initial_capital - 1) * 100)
        max_dd       = float(out["drawdown"].min() * 100)
        sharpe       = _sharpe(net, rfr_d)
        sortino      = _sortino(net, rfr_d)
        calmar       = _calmar(net)
        pf           = _profit_factor(net)

        # Win rate on closed trades (more accurate than bar-level)
        exit_returns = out.loc[out["trade_exit"], "net_return"]
        win_rate     = float((exit_returns > 0).mean() * 100) if len(exit_returns) > 0 else 0.0

        # Consecutive loss streak
        signs = np.sign(net)
        streak = 0
        max_streak = 0
        for s in signs:
            if s < 0:
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 0

        return {
            "total_return_pct":   round(total_return, 2),
            "ann_return_pct":     round(float((out["equity"].iloc[-1] / initial_capital)
                                              ** (252 / max(len(net), 1)) - 1) * 100, 2),
            "sharpe":             round(sharpe, 3),
            "sortino":            round(sortino, 3),
            "calmar":             round(calmar, 3),
            "max_drawdown_pct":   round(max_dd, 2),
            "profit_factor":      round(pf, 3),
            "n_trades":           n_trades,
            "win_rate":           round(win_rate, 1),
            "max_consec_losses":  int(max_streak),
            "total_costs_pct":    round(float(out["cost"].sum() * 100), 2),
            "equity_curve":       out["equity"],
            "drawdown_series":    out["drawdown"],
            "df":                 out,
        }

    @staticmethod
    def walk_forward_backtest(
        df: pd.DataFrame,
        signal_fn: Callable,
        optimize_fn: Callable,
        train_bars: int = 500,
        test_bars: int = 100,
        min_folds: int = 3,
        **kwargs,
    ) -> dict:
        """
        Anchored walk-forward validation.

        Parameters
        ----------
        signal_fn   : callable(df, params) → signal Series
        optimize_fn : callable(train_df) → params dict
        train_bars  : in-sample training window
        test_bars   : out-of-sample test window per fold
        min_folds   : minimum folds required for a valid result

        Returns
        -------
        dict with per-fold and aggregate OOS statistics.
        """
        results:    list[dict] = []
        all_equity: list[pd.Series] = []

        for start in range(0, len(df) - train_bars - test_bars, test_bars):
            train = df.iloc[start: start + train_bars]
            test  = df.iloc[start + train_bars: start + train_bars + test_bars].copy()

            try:
                params          = optimize_fn(train)
                test["signal"]  = signal_fn(test, params)
                bt              = VectorizedBacktester.backtest(test, **kwargs)
                results.append({
                    "fold":    len(results),
                    "sharpe":  bt["sharpe"],
                    "sortino": bt["sortino"],
                    "return":  bt["total_return_pct"],
                    "max_dd":  bt["max_drawdown_pct"],
                    "params":  params,
                })
                all_equity.append(bt["equity_curve"])
            except Exception as e:
                results.append({"fold": len(results), "error": str(e)})

        valid = [r for r in results if "sharpe" in r]
        if len(valid) < min_folds:
            return {
                "method":  "walk_forward",
                "error":   f"Only {len(valid)} valid folds (need {min_folds})",
                "n_folds": len(results),
            }

        sharpes  = [r["sharpe"]  for r in valid]
        sortinos = [r["sortino"] for r in valid]
        returns  = [r["return"]  for r in valid]

        # Concatenate OOS equity curves for a continuous equity line
        oos_equity = pd.concat(all_equity).sort_index() if all_equity else pd.Series(dtype=float)

        return {
            "method":            "walk_forward",
            "n_folds":           len(results),
            "n_valid_folds":     len(valid),
            "avg_sharpe":        round(float(np.mean(sharpes)), 3),
            "median_sharpe":     round(float(np.median(sharpes)), 3),
            "std_sharpe":        round(float(np.std(sharpes, ddof=1)), 3),
            "pct_folds_positive": round(float(np.mean([r > 0 for r in returns])) * 100, 1),
            "avg_return":        round(float(np.mean(returns)), 2),
            "avg_sortino":       round(float(np.mean(sortinos)), 3),
            "fold_results":      valid,
            "oos_equity":        oos_equity,
            "WARNING":           "Past performance ≠ future results. OOS validation required.",
        }

    @staticmethod
    def compare_strategies(
        df: pd.DataFrame,
        strategies: dict[str, pd.Series],
        spread_bps: float = 2.0,
        slippage_bps: float = 1.0,
        initial_capital: float = 10_000.0,
    ) -> pd.DataFrame:
        """
        Run multiple strategies on the same data and compare side-by-side.

        Parameters
        ----------
        strategies : {"name": signal_series, ...}

        Returns
        -------
        DataFrame ranked by Sharpe ratio.
        """
        results: list[dict] = []
        for name, signal_series in strategies.items():
            df_copy = df.copy()
            df_copy["signal"] = signal_series
            try:
                bt = VectorizedBacktester.backtest(
                    df_copy,
                    spread_bps=spread_bps,
                    slippage_bps=slippage_bps,
                    initial_capital=initial_capital,
                )
                results.append({
                    "strategy":     name,
                    "return":       bt["total_return_pct"],
                    "sharpe":       bt["sharpe"],
                    "sortino":      bt["sortino"],
                    "calmar":       bt["calmar"],
                    "max_dd":       bt["max_drawdown_pct"],
                    "n_trades":     bt["n_trades"],
                    "win_rate":     bt["win_rate"],
                    "profit_factor": bt["profit_factor"],
                })
            except Exception as e:
                results.append({"strategy": name, "error": str(e)})

        return pd.DataFrame(results).sort_values("sharpe", ascending=False)
```


---

## Trade Simulator Paper

# Trade Simulator Paper

```python
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Optional

class PaperTradeSimulator:
    """
    Realistic paper trading simulator with proper spread/slippage modelling,
    margin tracking, and full trade history for post-session analysis.

    Uses a reproducible RNG (np.random.default_rng) for slippage simulation.

    Example
    -------
    >>> sim = PaperTradeSimulator(initial_balance=10_000, seed=42)
    >>> sim.open_trade("EURUSD", "buy", lots=0.1, price=1.0850, sl=1.0810, tp=1.0920)
    >>> closed = sim.check_positions({"EURUSD": 1.0920})
    >>> print(closed[0]["reason"], closed[0]["pnl_usd"])
    'TP'  70.0
    """

    PIP_VALUES: dict[str, float] = {
        "default":  10.0,       # USD per pip per standard lot
        "USDJPY":   9.09,       # approximate (varies with rate)
        "XAUUSD":   10.0,
    }

    def __init__(
        self,
        initial_balance: float = 10_000.0,
        leverage: float = 30.0,
        pip_factor: float = 10_000.0,
        seed: int = 42,
    ):
        """
        Parameters
        ----------
        initial_balance : starting account balance in USD
        leverage        : maximum leverage (used for margin check)
        pip_factor      : price-to-pip conversion (10000 for most FX, 100 for JPY pairs)
        seed            : RNG seed for reproducible slippage
        """
        if initial_balance <= 0:
            raise ValueError("initial_balance must be positive")
        self.balance         = initial_balance
        self.equity          = initial_balance
        self.leverage        = leverage
        self.pip_factor      = pip_factor
        self._rng            = np.random.default_rng(seed)
        self.positions:  list[dict] = []
        self.history:    list[dict] = []
        self._trade_id   = 0

    # ── Position management ────────────────────────────────────────────────

    def open_trade(
        self,
        symbol: str,
        direction: str,
        lots: float,
        price: float,
        sl: float,
        tp: float,
        spread: float = 0.0002,
        max_slippage: float = 0.00005,
        comment: str = "",
    ) -> dict:
        """
        Open a simulated position with spread and random slippage applied.

        Parameters
        ----------
        symbol       : instrument (e.g. 'EURUSD')
        direction    : 'buy' or 'sell'
        lots         : position size in standard lots
        price        : requested entry price
        sl           : stop-loss price
        tp           : take-profit price
        spread       : half-spread to apply (price units, not pips)
        max_slippage : maximum slippage magnitude (price units)
        comment      : free-text label for this trade

        Returns
        -------
        dict with status, actual_entry, slippage_pips, and trade metadata.
        """
        direction = direction.lower()
        if direction not in ("buy", "sell"):
            raise ValueError(f"direction must be 'buy' or 'sell', got '{direction}'")
        if lots <= 0:
            raise ValueError("lots must be positive")
        if sl <= 0 or tp <= 0:
            raise ValueError("sl and tp must be positive price levels")

        slippage = float(self._rng.uniform(0, max_slippage))
        if direction == "buy":
            actual_entry = price + spread + slippage
        else:
            actual_entry = price - spread - slippage

        # Margin check
        required_margin = actual_entry * lots * 100_000 / self.leverage
        if required_margin > self.equity:
            return {"status": "REJECTED", "reason": "Insufficient margin",
                    "required_margin": round(required_margin, 2), "equity": round(self.equity, 2)}

        self._trade_id += 1
        pos = {
            "id":          self._trade_id,
            "symbol":      symbol,
            "direction":   direction,
            "lots":        lots,
            "entry":       round(actual_entry, 5),
            "requested":   round(price, 5),
            "sl":          round(sl, 5),
            "tp":          round(tp, 5),
            "spread_pips": round(spread * self.pip_factor, 1),
            "slippage_pips": round(slippage * self.pip_factor, 1),
            "open_time":   datetime.utcnow().isoformat(),
            "comment":     comment,
        }
        self.positions.append(pos)
        return {"status": "OPENED", **pos}

    def check_positions(self, current_prices: dict[str, float]) -> list[dict]:
        """
        Check all open positions against current prices and close those
        that have hit SL or TP.

        Parameters
        ----------
        current_prices : {symbol: bid_price} — use bid for sells, ask for buys
                         (simplified: pass mid-price for paper trading)

        Returns
        -------
        list of closed trade dicts (empty if nothing closed this tick).
        """
        closed: list[dict] = []
        remaining: list[dict] = []

        for pos in self.positions:
            price = current_prices.get(pos["symbol"])
            if price is None:
                remaining.append(pos)
                continue

            hit_sl = hit_tp = False
            if pos["direction"] == "buy":
                hit_sl = price <= pos["sl"]
                hit_tp = price >= pos["tp"]
            else:
                hit_sl = price >= pos["sl"]
                hit_tp = price <= pos["tp"]

            if hit_sl or hit_tp:
                exit_price  = pos["sl"] if hit_sl else pos["tp"]
                reason      = "SL" if hit_sl else "TP"
                pip_val     = self.PIP_VALUES.get(pos["symbol"], self.PIP_VALUES["default"])
                if pos["direction"] == "buy":
                    pnl_pips = (exit_price - pos["entry"]) * self.pip_factor
                else:
                    pnl_pips = (pos["entry"] - exit_price) * self.pip_factor
                pnl_usd = pnl_pips * pip_val * pos["lots"]

                self.balance += pnl_usd
                self.equity   = self.balance   # simplified (no floating P&L)

                trade_result = {
                    **pos,
                    "exit":       round(exit_price, 5),
                    "reason":     reason,
                    "pnl_pips":   round(pnl_pips, 1),
                    "pnl_usd":    round(pnl_usd, 2),
                    "close_time": datetime.utcnow().isoformat(),
                }
                closed.append(trade_result)
            else:
                remaining.append(pos)

        self.positions = remaining
        self.history.extend(closed)
        return closed

    def close_all(self, current_prices: dict[str, float]) -> list[dict]:
        """Force-close all open positions at current prices (market close)."""
        for pos in self.positions:
            price = current_prices.get(pos["symbol"])
            if price:
                current_prices[pos["symbol"]] = pos["sl"] if pos["direction"] == "buy" else pos["tp"]
        return self.check_positions(current_prices)

    # ── Analytics ──────────────────────────────────────────────────────────

    def account_summary(self) -> dict:
        """Return current account state and session statistics."""
        wins   = [t for t in self.history if t.get("pnl_usd", 0) > 0]
        losses = [t for t in self.history if t.get("pnl_usd", 0) < 0]
        total_pnl = sum(t.get("pnl_usd", 0) for t in self.history)
        return {
            "balance":       round(self.balance, 2),
            "equity":        round(self.equity, 2),
            "open_trades":   len(self.positions),
            "closed_trades": len(self.history),
            "win_rate":      round(len(wins) / max(len(self.history), 1) * 100, 1),
            "total_pnl":     round(total_pnl, 2),
            "avg_win_usd":   round(float(np.mean([t["pnl_usd"] for t in wins])), 2)   if wins   else 0.0,
            "avg_loss_usd":  round(float(np.mean([t["pnl_usd"] for t in losses])), 2) if losses else 0.0,
            "profit_factor": round(
                sum(t["pnl_usd"] for t in wins) / max(abs(sum(t["pnl_usd"] for t in losses)), 0.01), 3
            ) if losses else float("inf"),
        }
```


---

## Strategy Ab Tester

# Strategy A/B Tester

```python
import pandas as pd
import numpy as np
from scipy import stats

class StrategyABTester:
    """
    Head-to-head strategy comparison with parametric and non-parametric
    significance tests, plus rolling performance analysis.

    Example
    -------
    >>> result = StrategyABTester.compare(returns_a, returns_b)
    >>> print(result["winner"], result["statistically_significant"])
    'Strategy A'  True
    """

    @staticmethod
    def _metrics(r: pd.Series, name: str, rfr: float = 0.04 / 252) -> dict:
        """Compute a full metric set for one strategy."""
        r    = r.dropna()
        std  = float(r.std(ddof=1))
        equity = (1 + r).cumprod()
        max_dd = float(((equity / equity.cummax()) - 1).min())

        sharpe  = float((r.mean() - rfr) / std * np.sqrt(252)) if std > 0 else 0.0
        # Sortino: penalise downside vol only
        dn      = r[r < rfr]
        dn_std  = float(dn.std(ddof=1)) if len(dn) > 1 else 0.0
        sortino = float((r.mean() - rfr) / dn_std * np.sqrt(252)) if dn_std > 0 else 0.0
        # Calmar: annualised return / max drawdown
        ann_ret = float(equity.iloc[-1] ** (252 / max(len(r), 1)) - 1)
        calmar  = float(ann_ret / abs(max_dd)) if max_dd < 0 else 0.0

        return {
            "name":           name,
            "total_return":   round(float((equity.iloc[-1] - 1) * 100), 2),
            "ann_return":     round(ann_ret * 100, 2),
            "sharpe":         round(sharpe, 3),
            "sortino":        round(sortino, 3),
            "calmar":         round(calmar, 3),
            "max_drawdown":   round(max_dd * 100, 2),
            "volatility_ann": round(std * np.sqrt(252) * 100, 2),
            "win_rate":       round(float((r > 0).mean() * 100), 1),
            "skewness":       round(float(r.skew()), 3),
            "kurtosis":       round(float(r.kurtosis()), 3),
            "n_periods":      len(r),
        }

    @staticmethod
    def compare(
        returns_a: pd.Series,
        returns_b: pd.Series,
        name_a: str = "Strategy A",
        name_b: str = "Strategy B",
        risk_free: float = 0.04 / 252,
        alpha: float = 0.05,
    ) -> dict:
        """
        Comprehensive head-to-head comparison with four significance tests.

        Parameters
        ----------
        returns_a / b : daily return Series for each strategy
        alpha         : significance level (default 5 %)

        Returns
        -------
        dict with metrics for both strategies, statistical test results,
             winner, and actionable recommendation.
        """
        m_a = StrategyABTester._metrics(returns_a, name_a, risk_free)
        m_b = StrategyABTester._metrics(returns_b, name_b, risk_free)

        n   = min(len(returns_a.dropna()), len(returns_b.dropna()))
        ra  = returns_a.dropna().values[:n]
        rb  = returns_b.dropna().values[:n]

        # 1. Paired t-test
        t_stat, t_pval = stats.ttest_rel(ra, rb)

        # 2. Wilcoxon signed-rank (non-parametric)
        try:
            w_stat, w_pval = stats.wilcoxon(ra, rb)
        except Exception:
            w_stat, w_pval = 0.0, 1.0

        # 3. Kolmogorov-Smirnov (distribution difference)
        ks_stat, ks_pval = stats.ks_2samp(ra, rb)

        # 4. Jobson-Korkie Sharpe difference test
        sharpe_diff = m_a["sharpe"] - m_b["sharpe"]
        corr        = float(pd.Series(ra).corr(pd.Series(rb)))
        se_diff     = np.sqrt(
            (2 / n) * (1 - corr + 0.5 * m_a["sharpe"]**2 + 0.5 * m_b["sharpe"]**2)
        )
        jk_z    = sharpe_diff / max(se_diff, 1e-10)
        jk_pval = float(2 * (1 - stats.norm.cdf(abs(jk_z))))

        # Determine winner and significance (require at least t-test significant)
        better      = name_a if m_a["sharpe"] > m_b["sharpe"] else name_b
        significant = float(t_pval) < alpha

        return {
            "strategy_a":               m_a,
            "strategy_b":               m_b,
            "winner":                   better,
            "sharpe_advantage":         round(abs(sharpe_diff), 3),
            "statistically_significant": significant,
            "n_shared_periods":         n,
            "return_correlation":       round(corr, 3),
            "tests": {
                "paired_ttest":      {"t_stat": round(float(t_stat), 3),  "p_value": round(float(t_pval), 4),  "significant": float(t_pval) < alpha},
                "wilcoxon":          {"w_stat": round(float(w_stat), 3),  "p_value": round(float(w_pval), 4),  "significant": float(w_pval) < alpha},
                "ks_test":           {"ks_stat": round(float(ks_stat), 3), "p_value": round(float(ks_pval), 4), "significant": float(ks_pval) < alpha},
                "sharpe_difference": {"z_stat": round(jk_z, 3),          "p_value": round(jk_pval, 4),         "significant": jk_pval < alpha},
            },
            "verdict": (
                f"{better} is SIGNIFICANTLY better (t-test p={t_pval:.4f}). Confidence is high."
                if significant else
                f"{better} leads but NOT significantly (p={t_pval:.4f}). Difference may be noise."
            ),
            "recommendation": (
                f"Deploy {better}."
                if significant else
                "Run both over a longer sample or run walk-forward validation before deciding."
            ),
        }

    @staticmethod
    def rolling_comparison(
        returns_a: pd.Series,
        returns_b: pd.Series,
        window: int = 60,
    ) -> pd.DataFrame:
        """
        Rolling Sharpe comparison to identify regime-dependent leadership.

        Returns
        -------
        DataFrame with columns: sharpe_a, sharpe_b, difference, a_leads (bool),
                                 rolling_alpha (A return - B return, annualised %).
        """
        def _rolling_sharpe(r: pd.Series) -> pd.Series:
            mu  = r.rolling(window).mean()
            std = r.rolling(window).std(ddof=1)
            return (mu / std.replace(0, np.nan)) * np.sqrt(252)

        sa = _rolling_sharpe(returns_a).rename("sharpe_a")
        sb = _rolling_sharpe(returns_b).rename("sharpe_b")

        # Rolling alpha: annualised outperformance of A over B
        rolling_alpha = (
            (returns_a - returns_b).rolling(window).mean() * 252 * 100
        ).rename("rolling_alpha_pct")

        return pd.DataFrame({
            "sharpe_a":          sa,
            "sharpe_b":          sb,
            "difference":        sa - sb,
            "a_leads":           sa > sb,
            "rolling_alpha_pct": rolling_alpha,
        })
```


---

## Automated Strategy Builder

# Automated Strategy Builder

```python
class AutoStrategyBuilder:
    """
    Parse natural-language strategy descriptions and generate executable Python signal code.

    Maps trigger phrases to pandas-based code snippets, extracts numeric parameters
    from context, infers trade direction, and outputs a ready-to-run signal function.

    Example
    -------
    >>> result = AutoStrategyBuilder.parse_description(
    ...     "Buy when RSI is below 30 and price crosses above the 50 EMA"
    ... )
    >>> print(result["direction"], result["can_auto_generate"])
    'long'  True
    >>> print(result["generated_code"])
    """

    CONDITION_MAP: dict[str, str] = {
        "rsi above":           "df['rsi_{p}'] > {value}",
        "rsi below":           "df['rsi_{p}'] < {value}",
        "price above sma":     "df['close'] > df['close'].rolling({value}).mean()",
        "price below sma":     "df['close'] < df['close'].rolling({value}).mean()",
        "price above ema":     "df['close'] > df['close'].ewm(span={value}).mean()",
        "price below ema":     "df['close'] < df['close'].ewm(span={value}).mean()",
        "macd cross up":       "(df['macd'] > df['signal']) & (df['macd'].shift(1) <= df['signal'].shift(1))",
        "macd cross down":     "(df['macd'] < df['signal']) & (df['macd'].shift(1) >= df['signal'].shift(1))",
        "bollinger lower":     "df['close'] < df['close'].rolling(20).mean() - 2 * df['close'].rolling(20).std()",
        "bollinger upper":     "df['close'] > df['close'].rolling(20).mean() + 2 * df['close'].rolling(20).std()",
        "volume above average": "df['volume'] > df['volume'].rolling(20).mean() * 1.5",
        "new high":            "df['close'] > df['close'].rolling({value}).max().shift(1)",
        "new low":             "df['close'] < df['close'].rolling({value}).min().shift(1)",
        "bullish engulfing":   "(df['close'] > df['open']) & (df['close'] > df['open'].shift(1)) & (df['open'] < df['close'].shift(1))",
        "bearish engulfing":   "(df['close'] < df['open']) & (df['close'] < df['open'].shift(1)) & (df['open'] > df['close'].shift(1))",
        "above cloud":         "df['close'] > df[['senkou_a','senkou_b']].max(axis=1)",
        "below cloud":         "df['close'] < df[['senkou_a','senkou_b']].min(axis=1)",
        "golden cross":        "(df['close'].rolling(50).mean() > df['close'].rolling(200).mean()) & (df['close'].rolling(50).mean().shift(1) <= df['close'].rolling(200).mean().shift(1))",
        "death cross":         "(df['close'].rolling(50).mean() < df['close'].rolling(200).mean()) & (df['close'].rolling(50).mean().shift(1) >= df['close'].rolling(200).mean().shift(1))",
        "atr breakout":        "df['high'] - df['low'] > {value} * df['atr']",
    }

    _LONG_WORDS  = {"buy", "long", "bullish", "uptrend", "above", "breakout up"}
    _SHORT_WORDS = {"sell", "short", "bearish", "downtrend", "below", "breakdown"}

    @staticmethod
    def _extract_number(text: str, default: int = 14) -> int:
        """Extract the first integer from a text string."""
        import re
        m = re.search(r"\b(\d{1,3})\b", text)
        return int(m.group(1)) if m else default

    @staticmethod
    def parse_description(text: str) -> dict:
        """
        Parse a natural-language strategy description into structured conditions
        and optionally generate executable Python signal code.

        Parameters
        ----------
        text : free-form strategy description

        Returns
        -------
        dict with parsed_conditions, direction, generated_code, and completeness assessment.
        """
        import re
        text_lower = text.lower()

        conditions: list[dict] = []
        for trigger, code_template in AutoStrategyBuilder.CONDITION_MAP.items():
            if trigger in text_lower:
                # Extract a numeric parameter from the surrounding context
                context = text_lower[max(text_lower.find(trigger) - 20, 0):
                                     text_lower.find(trigger) + 40]
                param = AutoStrategyBuilder._extract_number(context)
                code  = code_template.replace("{value}", str(param)).replace("{p}", str(param))
                conditions.append({
                    "natural":   trigger,
                    "code":      code,
                    "param":     param,
                })

        # Direction inference
        long_hits  = sum(w in text_lower for w in AutoStrategyBuilder._LONG_WORDS)
        short_hits = sum(w in text_lower for w in AutoStrategyBuilder._SHORT_WORDS)
        direction  = "long" if long_hits > short_hits else "short" if short_hits > long_hits else "unknown"

        # Generate executable signal code when conditions are available
        generated_code = ""
        if len(conditions) >= 1:
            signal_val = "1" if direction == "long" else "-1" if direction == "short" else "1"
            cond_lines = "\n    & ".join(f"({c['code']})" for c in conditions)
            generated_code = (
                "import numpy as np\n\n"
                "def generate_signal(df: pd.DataFrame) -> pd.Series:\n"
                f"    mask = (\n    {cond_lines}\n    )\n"
                f"    signal = pd.Series(0, index=df.index)\n"
                f"    signal[mask] = {signal_val}\n"
                "    return signal.shift(1).fillna(0)  # Shift to prevent look-ahead\n"
            )

        return {
            "parsed_conditions":  conditions,
            "direction":          direction,
            "n_conditions":       len(conditions),
            "can_auto_generate":  len(conditions) >= 2,
            "generated_code":     generated_code,
            "next_step": (
                "Generated code ready — add to a DataFrame and backtest with VectorizedBacktester."
                if len(conditions) >= 2 else
                "Add more specific conditions (e.g., 'RSI below 30', 'price above 50 EMA') for code generation."
            ),
        }
```


---

## Natural Language To Strategy

# Natural Language To Strategy

```python
class NLStrategyParser:
    """
    Parse a free-text strategy description into structured entry, exit, risk,
    and filter rules — ready for review or downstream code generation.

    Example
    -------
    >>> result = NLStrategyParser.parse(
    ...     "Buy when RSI crosses above 30. Exit when RSI exceeds 70 or SL at 1%. "
    ...     "Only trade during London session. Avoid Fridays."
    ... )
    >>> print(result["completeness"])
    'COMPLETE'
    """

    _ENTRY_WORDS  = {"enter", "buy", "sell", "open", "go long", "go short", "long when", "short when"}
    _EXIT_WORDS   = {"exit", "close", "take profit", "stop loss", "stop-loss", "tp", "sl at"}
    _RISK_WORDS   = {"risk", "lot size", "position size", "max loss", "2r", "1r", "r:r", "risk reward"}
    _FILTER_WORDS = {"only", "filter", "avoid", "when", "must", "unless", "not on", "session", "news"}

    @staticmethod
    def parse(text: str) -> dict:
        """
        Parse strategy text into structured rule categories.

        Parameters
        ----------
        text : multi-sentence strategy description

        Returns
        -------
        dict with categorised rules, completeness score, and a gap analysis
             highlighting what is missing before the strategy can be coded.
        """
        import re
        rules: dict[str, list[str]] = {"entry": [], "exit": [], "risk": [], "filters": []}

        sentences = re.split(r"[.;!\n]", text)
        for s in sentences:
            s_stripped = s.strip()
            s_lower    = s_stripped.lower()
            if not s_lower:
                continue

            # Categorise by keyword presence (in order of specificity)
            if any(w in s_lower for w in NLStrategyParser._RISK_WORDS):
                rules["risk"].append(s_stripped)
            elif any(w in s_lower for w in NLStrategyParser._EXIT_WORDS):
                rules["exit"].append(s_stripped)
            elif any(w in s_lower for w in NLStrategyParser._ENTRY_WORDS):
                rules["entry"].append(s_stripped)
            elif any(w in s_lower for w in NLStrategyParser._FILTER_WORDS):
                rules["filters"].append(s_stripped)

        # Gap analysis
        gaps: list[str] = []
        if not rules["entry"]:   gaps.append("No entry rule — when do you enter?")
        if not rules["exit"]:    gaps.append("No exit rule — when do you close?")
        if not rules["risk"]:    gaps.append("No risk rule — what % do you risk per trade?")

        has_entry  = bool(rules["entry"])
        has_exit   = bool(rules["exit"])
        has_risk   = bool(rules["risk"])
        score      = sum([has_entry, has_exit, has_risk])

        completeness = (
            "COMPLETE"             if score == 3 else
            "MOSTLY COMPLETE"      if score == 2 else
            "INCOMPLETE"
        )

        return {
            "parsed_rules":   rules,
            "n_entry_rules":  len(rules["entry"]),
            "n_exit_rules":   len(rules["exit"]),
            "n_risk_rules":   len(rules["risk"]),
            "n_filters":      len(rules["filters"]),
            "completeness":   completeness,
            "completeness_score": score,
            "gaps":           gaps,
            "ready_to_code":  score == 3,
            "next_step": (
                "Strategy is well-defined. Use AutoStrategyBuilder to generate signal code."
                if score == 3 else
                f"Fill in missing rules: {'; '.join(gaps)}"
            ),
        }
```


---

## Trading Plan Builder

# Trading Plan Builder

```python
from datetime import datetime, timedelta
from dataclasses import dataclass, field

@dataclass
class DailyTradingPlan:
    """Structured daily trading plan with session context, risk budget, and rules."""
    date:           str
    session_focus:  str
    watchlist:      list[dict] = field(default_factory=list)
    macro_context:  str = ""
    key_events:     list[str] = field(default_factory=list)
    bias:           dict = field(default_factory=dict)
    risk_budget:    dict = field(default_factory=dict)
    rules_today:    list[str] = field(default_factory=list)
    checklist:      dict = field(default_factory=dict)
    notes:          str = ""

    def to_markdown(self) -> str:
        """Export plan as a readable markdown string for journaling."""
        event_lines   = [f"- {e}" for e in self.key_events] or ["- None"]
        budget_lines  = [f"- **{k}:** {v}" for k, v in self.risk_budget.items()]
        rule_lines    = [f"- {r}" for r in self.rules_today]
        watch_lines   = [
            f"- {w['pair']} | Bias: {w.get('bias','?')} | Priority: {w.get('priority','?')} | Confluence: {w.get('confluence_pct', 0)}%"
            for w in self.watchlist
        ]
        lines = (
            [f"# Trading Plan \u2014 {self.date}",
             f"**Session:** {self.session_focus.upper()}",
             f"**Macro Context:** {self.macro_context or 'N/A'}",
             "",
             "## Key Events Today"]
            + event_lines
            + ["", "## Risk Budget"]
            + budget_lines
            + ["", "## Rules"]
            + rule_lines
            + ["", "## Watchlist"]
            + watch_lines
        )
        return "\n".join(lines)


class TradingPlanBuilder:
    """
    Build, structure, and export daily trading plans with pre-market checklists,
    watchlist generation, and end-of-day review templates.

    Example
    -------
    >>> plan = TradingPlanBuilder.build_plan()
    >>> print(plan.session_focus)
    'london'
    >>> md = plan.to_markdown()
    """

    SESSION_HOURS = {
        "tokyo":    (0, 7),
        "london":   (7, 13),
        "overlap":  (13, 16),
        "new_york": (13, 22),
        "off":      (22, 24),
    }

    @staticmethod
    def current_session(hour: Optional[int] = None) -> str:
        """Return the current or given-hour trading session name."""
        h = hour if hour is not None else datetime.utcnow().hour
        if 0 <= h < 7:   return "tokyo"
        if 7 <= h < 13:  return "london"
        if 13 <= h < 16: return "overlap"
        if 16 <= h < 22: return "new_york"
        return "off"

    @staticmethod
    def pre_market_checklist() -> dict:
        """Return a structured pre-market checklist with estimated times."""
        return {
            "1_macro_scan": {
                "task":  "Check DXY, VIX, yield curves, equity futures",
                "tools": ["macro-economic-dashboard"],
                "time":  "5 min",
                "why":   "Sets the risk-on/risk-off context for the day",
            },
            "2_news_check": {
                "task":  "Review upcoming high-impact events and overnight news",
                "tools": ["market-news-impact", "risk-calendar-trade-filter"],
                "time":  "5 min",
                "why":   "Avoid entering before news that can spike against position",
            },
            "3_htf_analysis": {
                "task":  "D1 and H4 analysis on watchlist pairs — set daily directional bias",
                "tools": ["mt5-chart-browser", "mtf-confluence-scorer"],
                "time":  "10 min",
                "why":   "Higher timeframe bias defines where the order flow is likely going",
            },
            "4_key_levels": {
                "task":  "Mark S/R, order blocks, FVGs, and liquidity pools on H1 charts",
                "tools": ["trendline-sr-vision", "liquidity-order-flow-mapper"],
                "time":  "10 min",
                "why":   "These are the decision points where institutional orders cluster",
            },
            "5_risk_budget": {
                "task":  "Set max daily loss, max trades, and check portfolio heat",
                "tools": ["risk-and-portfolio"],
                "time":  "2 min",
                "why":   "Pre-defined loss limits prevent emotional overtrading",
            },
            "6_session_check": {
                "task":  "Verify current session quality — is today suitable for trading?",
                "tools": ["session-profiler", "risk-calendar-trade-filter"],
                "time":  "2 min",
                "why":   "Thin liquidity sessions (e.g., bank holidays) produce false signals",
            },
            "7_tilt_check": {
                "task":  "Run tilt_detector() on last 10 trades — check emotional state",
                "tools": ["TradePsychologyCoach.tilt_detector"],
                "time":  "1 min",
                "why":   "Emotional residue from prior losses causes the worst trading decisions",
            },
            "_total_time": "~35 minutes",
        }

    @staticmethod
    def generate_watchlist(
        pairs: list[str],
        confluence_scores: dict,
        max_pairs: int = 6,
    ) -> list[dict]:
        """
        Rank pairs by confluence score and return a focused watchlist.

        Parameters
        ----------
        pairs             : all candidate pairs
        confluence_scores : {pair: {"overall_score": float, "direction": str, "confluence_pct": float}}
        max_pairs         : maximum number of pairs to include

        Returns
        -------
        List of dicts sorted by confluence_pct descending, with priority grades.
        """
        watchlist: list[dict] = []
        for pair in pairs:
            score = confluence_scores.get(pair, {})
            conf  = float(score.get("confluence_pct", 0))
            watchlist.append({
                "pair":           pair,
                "mtf_score":      score.get("overall_score", 0),
                "bias":           score.get("direction", "NEUTRAL"),
                "confluence_pct": round(conf, 1),
                "priority":       "A+" if conf >= 85 else "A" if conf >= 75 else "B" if conf >= 50 else "C",
                "tradeable":      conf >= 50,
            })

        return sorted(watchlist, key=lambda w: w["confluence_pct"], reverse=True)[:max_pairs]

    @staticmethod
    def end_of_day_review() -> dict:
        """Return a structured end-of-day review template."""
        return {
            "1_log_trades":        "Journal all trades: setup type, entry/exit reasoning, R-multiple achieved",
            "2_plan_adherence":    "Did you follow the plan exactly? Rate 1–10. Identify deviations.",
            "3_what_worked":       "List setups that worked and why (be specific about the edge)",
            "4_what_failed":       "List setups that failed and the true reason (execution vs setup vs bad luck)",
            "5_lessons":           "One concrete lesson to apply in tomorrow's session",
            "6_emotional_state":   "Rate emotional discipline 1–10. Flag any tilt episodes.",
            "7_plan_adjustments":  "Any rule changes for tomorrow? Document and date them.",
            "8_equity_review":     "Update equity curve. Compare to plan expectations.",
        }

    @staticmethod
    def build_plan(
        now: Optional[datetime] = None,
        max_risk_pct: float = 4.0,
        max_trades: int = 3,
        risk_per_trade_pct: float = 1.5,
        extra_rules: Optional[list[str]] = None,
    ) -> DailyTradingPlan:
        """
        Build a complete daily trading plan for the current (or given) time.

        Parameters
        ----------
        now                : UTC datetime (defaults to now)
        max_risk_pct       : maximum total risk allowed today (% of account)
        max_trades         : maximum number of trades
        risk_per_trade_pct : risk per individual trade (% of account)
        extra_rules        : additional trader-specific rules to include

        Returns
        -------
        DailyTradingPlan dataclass with all fields populated.
        """
        now     = now or datetime.utcnow()
        session = TradingPlanBuilder.current_session(now.hour)

        base_rules = [
            "Follow the plan. No improvised trades.",
            "Only A and B grade setups — wait for confluence.",
            "No revenge trades after a loss. Take a break.",
            f"Stop after {max_trades} trades (win or lose) — protect the day.",
            "No trading 30 minutes before or after high-impact news.",
            "If daily loss exceeds 50% of risk budget — stop for the day."]
        if extra_rules:
            base_rules.extend(extra_rules)

        return DailyTradingPlan(
            date          = now.strftime("%Y-%m-%d"),
            session_focus = session,
            risk_budget   = {
                "max_risk_today_pct":   f"{max_risk_pct}%",
                "max_trades":           max_trades,
                "risk_per_trade_pct":   f"{risk_per_trade_pct}%",
                "max_loss_stop_pct":    f"{max_risk_pct / 2:.1f}%",
            },
            rules_today   = base_rules,
            checklist     = TradingPlanBuilder.pre_market_checklist(),
            macro_context = f"Built at {now.strftime('%H:%M')} UTC — {session.upper()} session",
        )
```

---

## Related Skills

- [Statistical Analysis](../statistics-timeseries.md)
- [Algorithmic Strategies](../backtesting-sim.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
- [Data Pipelines](../market-data-ingestion.md)
