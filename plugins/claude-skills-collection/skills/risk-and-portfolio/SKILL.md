---
name: risk-and-portfolio
description: >
  Complete trading risk management, portfolio construction, performance tracking, and quantitative
  stress testing — all in one skill. The safety layer for all trading decisions.

  RISK MANAGEMENT: "risk management", "position sizing", "lot size calculation", "stop loss placement",
  "drawdown management", "Kelly criterion", "ATR-based sizing", "fixed percentage risk model",
  "risk-reward analysis", "profit factor", "expectancy", "trading psychology", "trade-psychology-coach biases",
  "loss aversion", "FOMO", "revenge trading", "emotional management", "daily loss limit",
  "weekly loss limit", "max drawdown", "portfolio heat", "correlation risk", "trailing stops",
  "losing streak", "drawdown recovery", "risk of ruin", "VaR", "CVaR", "Calmar ratio",
  "Sortino ratio", "margin requirements", "money management", "1% rule trading".

  EXECUTION & COSTS: "best entry timing", "scaling in out", "limit vs market orders",
  "partial fills", "slippage reduction", "scale into position", "split my entry",
  "reduce slippage", "DCA strategy", "pyramid into trade", "trail my stop",
  "order book", "bid ask spread", "microstructure", "spread analysis", "execution cost",
  "broker comparison", "true spread", "market impact", "TWAP", "VWAP execution",
  "transaction cost analysis", "TCA", "Almgren-Chriss".

  TRADE JOURNAL: "log my trade", "journal this trade", "show my stats", "performance report",
  "what's my win rate", "equity curve", "expectancy", "R-multiple", "trade history",
  "best worst trades", "review my trading", "monthly P&L", "streak analysis".

  TRADE FILTER: "should I trade today", "is it safe to trade", "any events to avoid",
  "blackout zones", "when not to trade", "event risk", "news blackout", "rollover time",
  "low liquidity", "NFP week", "FOMC week", "end of month".

  PORTFOLIO: "portfolio optimization", "Markowitz", "efficient frontier", "Black-Litterman",
  "risk parity", "asset allocation", "portfolio weights", "minimum variance", "maximum Sharpe",
  "basket trade", "currency basket", "synthetic pair", "strategy allocation", "ensemble trading",
  "multi-strategy fund", "DXY replica", "capital allocation".

  MULTI-ACCOUNT: "multi account", "track accounts", "aggregate P&L", "compare accounts",
  "total balance", "portfolio across brokers", "account summary", "all my accounts".

  TAIL RISK: "tail risk", "black swan", "crash protection", "hedge portfolio",
  "portfolio insurance", "fat tails", "disaster hedge".

  RISK PREMIA: "risk premia", "factor investing", "value factor", "momentum factor",
  "carry factor", "volatility premium", "alternative risk premia", "ARP", "factor harvesting",
  "smart beta", "systematic factor", "factor portfolio".

  ARBITRAGE: "arbitrage", "stat arb", "pairs trading", "triangular arbitrage",
  "convergence trade", "mean reversion pair", "cointegration", "basis trade",
  "spread trading", "relative value", "mispricing detection", "hedge ratio",
  "spread z-score", "cross-asset arbitrage".

  RISK-ADJUSTED COMPOUNDING: "compounding", "risk-adjusted compounding", "Sharpe ratio",
  "compound projection", "geometric growth rate", "monthly compounding", "CAGR".

  PERFORMANCE ATTRIBUTION: "performance attribution", "P&L by pair", "P&L by setup",
  "P&L by session", "P&L by direction", "best pair", "worst pair", "edge analysis".

  MONTE CARLO: "Monte Carlo", "stress test", "bootstrap returns", "parametric simulation",
  "regime shuffle", "parameter perturbation", "robustness test", "risk of ruin simulation",
  "fat tail simulation", "Student-t Monte Carlo".

  PARAMETER SENSITIVITY: "parameter sensitivity", "grid sweep", "heatmap", "overfit detection",
  "flatness score", "one-at-a-time sensitivity", "curve fitting check", "robustness check".

  TRADE PSYCHOLOGY: "tilt detector", "revenge trading detection", "trade-psychology-coach bias check",
  "discipline score", "pre-trade checklist", "trading psychology coach", "emotional state",
  "consecutive losses", "overtrading detection".

  TRADE-LEVEL RISK: "midpoint entry", "SL halving", "partial close", "break-even rule",
  "FVG midpoint", "R:R improvement", "trade management protocol".

  DO NOT USE FOR: ICT-specific risk rules (use ict-smart-money),
  strategy entry/exit rules (use trading-strategies), options Greeks risk (use options-trading).
related_skills:
  - portfolio-optimization
  - risk-and-portfolio
  - portfolio-optimization
  - trading-fundamentals
tags:
  - trading
  - risk
  - portfolio
  - position-sizing
  - drawdown
  - kelly
skill_level: intermediate
kind: reference
category: trading/risk
status: active
---
> **Skill:** Risk And Portfolio  |  **Domain:** trading  |  **Category:** risk  |  **Level:** intermediate
> **Tags:** `trading`, `risk`, `portfolio`, `position-sizing`, `drawdown`, `kelly`


# Risk & Portfolio — Complete Framework

> The safety layer. No trade should be taken without passing through risk checks.

## Sections

1. **Risk Management** — position sizing, rules, psychology, drawdown recovery
2. **Execution & Costs** — entry timing, scaling, microstructure, spread/slippage
3. **Trade Journal & Performance** — logging, analytics, equity curve
4. **Trade Filter** — when NOT to trade (event blackouts, structural risks)
5. **Portfolio & Allocation** — Markowitz, risk parity, baskets, strategy allocation
6. **Multi-Account Manager** — aggregate P&L across brokers
7. **Tail Risk Hedging** — black swan protection
8. **Risk Premia** — factor investing (momentum, carry, value, volatility premium)
9. **Arbitrage Engine** — cointegration, pairs trading, triangular arb, spread z-score
10. **Risk-Adjusted Compounding** — Sharpe/Sortino/Calmar metrics, Kelly compounding, projections
11. **Performance Attribution** — P&L decomposition by pair, setup, direction, session, day
12. **Monte Carlo Stress Testing** — bootstrap, parametric (fat-tail), regime shuffle, parameter perturbation
13. **Parameter Sensitivity** — 2D grid sweep, OAT analysis, heatmaps, overfit/flatness scoring
14. **Trade Psychology Coach** — tilt detector, trade-psychology-coach bias check, discipline score, pre-trade checklist
15. **Trade-Level Risk Refinement** — midpoint entry (SL halving), partial close & break-even protocol

---

## Reference Files

- **[references/risk-and-portfolio.md](references/risk-and-portfolio.md)** — Core risk rules, position sizing (fixed %, Kelly, ATR), drawdown protocol, portfolio heat, psychology, journal template
- **[references/execution-costs.md](references/execution-costs.md)** — Entry timing, order splitting/scaling, trailing stops, market microstructure, spread/slippage analysis, market impact model
- **[references/journal-and-filter.md](references/journal-and-filter.md)** — Trade journal engine, performance analytics (win rate, equity curve, R-multiple), event blackout filter, should_i_trade()
- **[references/portfolio-allocation.md](references/portfolio-allocation.md)** — Portfolio optimization (Markowitz, Black-Litterman, risk parity), strategy allocator, currency baskets, synthetic instruments
- **[references/account-tail-risk.md](references/account-tail-risk.md)** — Multi-account manager (aggregate P&L) + tail risk hedging (black swan protection)
- **[references/risk-premia.md](references/risk-premia.md)** — Factor investing: momentum factor, carry factor, value factor, volatility premium harvesting, combined factor portfolio
- **[references/arbitrage-engine.md](references/arbitrage-engine.md)** — Cointegration testing, OLS hedge ratio, triangular arbitrage check, spread z-score signals, pair scanner

## Quick Decision Guide

| Task | Load |
|------|------|
| Position sizing, lot size, stop placement | `references/risk-and-portfolio.md` |
| Kelly criterion, drawdown rules, psychology | `references/risk-and-portfolio.md` |
| When to enter, how to scale, slippage | `references/execution-costs.md` |
| Microstructure, spread analysis, TCA | `references/execution-costs.md` |
| Log a trade, check win rate, equity curve | `references/journal-and-filter.md` |
| Should I trade today? Event blackouts? | `references/journal-and-filter.md` |
| Portfolio weights, Markowitz, risk parity | `references/portfolio-allocation.md` |
| Currency basket, DXY replica, multi-strategy | `references/portfolio-allocation.md` |
| Multi-account P&L, broker comparison | `references/account-tail-risk.md` |
| Black swan hedge, crash protection | `references/account-tail-risk.md` |
| Factor investing, momentum/carry/value/vol premia | `references/risk-premia.md` |
| Cointegration, pairs trade, triangular arb, spread z-score | `references/arbitrage-engine.md` |
| Sharpe/Sortino/Calmar, compounding projections, Kelly growth | See **Risk-Adjusted Compounding** below |
| P&L by pair/setup/session/direction, edge analysis | See **Performance Attribution Engine** below |
| Monte Carlo bootstrap, parametric fat-tail, regime shuffle | See **Monte Carlo Stress Tester** below |
| Parameter grid sweep, heatmap, overfit detection | See **Parameter Sensitivity Analyzer** below |
| Tilt detection, revenge trading, trade-psychology-coach biases, discipline | See **Trade Psychology Coach** below |
| Midpoint entry (SL halving), partial close, break-even rule | See **Trade-Level Risk Refinement** below |

## Core Quick Reference Card

```
POSITION SIZE      = (Account × Risk%) / Stop Distance
KELLY %            = W − [(1−W) / R]     → Use HALF Kelly
ATR STOP           = ATR × Multiplier (2–4× depending on TF)
EXPECTED VALUE     = (Win% × Avg Win) − (Loss% × Avg Loss)
PROFIT FACTOR      = Gross Profit / Gross Loss  → Target > 1.5
DAILY LIMIT        = 3–5% account loss → STOP
WEEKLY LIMIT       = 5–10% → reduce size
MAX DRAWDOWN       = 15–25% → halt and review
PORTFOLIO HEAT     = 6% max total open risk
LOSING STREAK      = 3 losses → cut 50% | 5 losses → 25% or pause
MIN R:R            = 1:1.5  → prefer 1:2+
BREAKEVEN STOP     = move to entry when +1R reached
KILL SWITCH        = 10% daily DD → stop trading for the day
MARGIN             = never exceed 50% utilization
```

---

# Inline Implementations (merged from risk-and-portfolio)

> The sections below contain full Python implementations for risk-adjusted compounding,
> tail risk hedging, spread/slippage cost analysis, performance attribution,
> Monte Carlo stress testing, parameter sensitivity analysis, trade psychology coaching,
> and trade-level risk refinement techniques.


---

## Risk Adjusted Compounding

# Risk Adjusted Compounding

```python
import numpy as np
import pandas as pd
from typing import Optional

# ── Shared performance metrics ──────────────────────────────────────────────

def _sharpe(returns: np.ndarray, risk_free_daily: float = 0.04 / 252,
            annualise: bool = True) -> float:
    """Annualised Sharpe ratio (excess return / vol)."""
    excess = returns - risk_free_daily
    std    = returns.std(ddof=1)
    if std == 0:
        return 0.0
    sr = excess.mean() / std
    return float(sr * np.sqrt(252) if annualise else sr)


def _sortino(returns: np.ndarray, risk_free_daily: float = 0.04 / 252,
             annualise: bool = True) -> float:
    """Sortino ratio — penalises only downside volatility."""
    excess   = returns - risk_free_daily
    downside = returns[returns < 0]
    down_std = downside.std(ddof=1) if len(downside) > 1 else 0.0
    if down_std == 0:
        return 0.0
    sr = excess.mean() / down_std
    return float(sr * np.sqrt(252) if annualise else sr)


def _calmar(returns: np.ndarray) -> float:
    """Calmar ratio = annualised return / max drawdown."""
    equity   = np.cumprod(1 + returns)
    peak     = np.maximum.accumulate(equity)
    dd       = (equity - peak) / peak
    max_dd   = abs(dd.min())
    ann_ret  = (equity[-1] ** (252 / len(returns)) - 1)
    return float(ann_ret / max_dd) if max_dd > 0 else 0.0


def _max_drawdown(returns: np.ndarray) -> float:
    equity = np.cumprod(1 + returns)
    peak   = np.maximum.accumulate(equity)
    return float(((equity - peak) / peak).min())


def _profit_factor(returns: np.ndarray) -> float:
    gains  = returns[returns > 0].sum()
    losses = abs(returns[returns < 0].sum())
    return float(gains / losses) if losses > 0 else float("inf")


def comprehensive_metrics(
    returns: "pd.Series | np.ndarray",
    risk_free_annual: float = 0.04,
    label: str = "Strategy",
) -> dict:
    """
    Compute a full suite of risk-adjusted performance metrics.

    Parameters
    ----------
    returns          : daily returns series (decimal, e.g. 0.01 = +1 %)
    risk_free_annual : annual risk-free rate (default 4 %)
    label            : name shown in output

    Returns
    -------
    dict with Sharpe, Sortino, Calmar, max drawdown, profit factor, VaR, CVaR, etc.

    Example
    -------
    >>> metrics = comprehensive_metrics(df["returns"], label="My Strategy")
    >>> print(metrics["sharpe"])
    1.42
    """
    r = np.asarray(returns, dtype=float)
    r = r[~np.isnan(r)]
    if len(r) < 5:
        return {"error": "Need at least 5 return observations", "label": label}

    rfr_daily = risk_free_annual / 252
    equity    = np.cumprod(1 + r)
    ann_ret   = float(equity[-1] ** (252 / len(r)) - 1)

    # VaR & CVaR
    var_95  = float(np.percentile(r, 5))
    cvar_95 = float(r[r <= var_95].mean()) if (r <= var_95).any() else var_95

    return {
        "label":           label,
        "n_periods":       len(r),
        "total_return":    round(float(equity[-1] - 1) * 100, 2),
        "ann_return":      round(ann_ret * 100, 2),
        "ann_volatility":  round(float(r.std(ddof=1) * np.sqrt(252)) * 100, 2),
        "sharpe":          round(_sharpe(r, rfr_daily), 3),
        "sortino":         round(_sortino(r, rfr_daily), 3),
        "calmar":          round(_calmar(r), 3),
        "max_drawdown":    round(_max_drawdown(r) * 100, 2),
        "profit_factor":   round(_profit_factor(r), 3),
        "win_rate":        round(float((r > 0).mean()) * 100, 1),
        "var_95":          round(var_95 * 100, 3),
        "cvar_95":         round(cvar_95 * 100, 3),
        "skewness":        round(float(pd.Series(r).skew()), 3),
        "kurtosis":        round(float(pd.Series(r).kurtosis()), 3),
        "grade": (
            "A+" if _sharpe(r, rfr_daily) > 2.0 else
            "A"  if _sharpe(r, rfr_daily) > 1.5 else
            "B"  if _sharpe(r, rfr_daily) > 1.0 else
            "C"  if _sharpe(r, rfr_daily) > 0.5 else "D"
        ),
    }


class CompoundingOptimizer:
    """
    Kelly-criterion compounding and multi-period projection.

    Example
    -------
    >>> opt = CompoundingOptimizer.optimal_growth(0.55, 1.5, 1.0)
    >>> print(opt["recommended"])
    8.33
    """

    @staticmethod
    def optimal_growth(
        win_rate: float,
        avg_win: float,
        avg_loss: float,
        trades_per_year: int = 252,
    ) -> dict:
        """
        Compute Kelly criterion fractions and geometric growth rates.

        Parameters
        ----------
        win_rate        : fraction of winning trades (0–1)
        avg_win         : average win in R-multiples (or % of account)
        avg_loss        : average loss in R-multiples (positive value)
        trades_per_year : used for annualising growth rate

        Returns
        -------
        dict with full/half/quarter kelly and projected growth rates.
        """
        if avg_win <= 0:
            raise ValueError("avg_win must be positive")
        if not 0 < win_rate < 1:
            raise ValueError("win_rate must be between 0 and 1 (exclusive)")

        kelly        = (win_rate * avg_win - (1 - win_rate) * avg_loss) / avg_win
        kelly        = max(kelly, 0.0)         # No negative sizing
        half_kelly   = kelly / 2
        quarter_kelly = kelly / 4

        def _growth_rate(f: float) -> float:
            """Expected log-growth per trade at fraction f."""
            try:
                return (win_rate * np.log1p(f * avg_win / 100)
                        + (1 - win_rate) * np.log1p(-f * avg_loss / 100))
            except (ValueError, ZeroDivisionError):
                return -np.inf

        return {
            "full_kelly_pct":          round(kelly * 100, 2),
            "half_kelly_pct":          round(half_kelly * 100, 2),
            "quarter_kelly_pct":       round(quarter_kelly * 100, 2),
            "recommended":             round(half_kelly * 100, 2),
            "expectancy_r":            round(win_rate * avg_win - (1 - win_rate) * avg_loss, 4),
            "growth_at_half_kelly_ann":    round(_growth_rate(half_kelly) * trades_per_year * 100, 2),
            "growth_at_quarter_kelly_ann": round(_growth_rate(quarter_kelly) * trades_per_year * 100, 2),
            "risk_of_ruin_half_kelly": round(
                ((1 - win_rate) / win_rate) ** (1 / max(half_kelly, 1e-6)), 4
            ),
            "note": (
                "Half Kelly = ~75 % of full Kelly growth with ~50 % of the variance. "
                "Best risk-adjusted choice for most traders."
            ),
        }

    @staticmethod
    def compound_projection(
        balance: float,
        monthly_return_pct: float,
        months: int = 12,
        withdrawal_pct: float = 0.0,
    ) -> dict:
        """
        Project compounded account growth with optional monthly withdrawals.

        Parameters
        ----------
        balance           : starting capital
        monthly_return_pct: expected monthly return (%)
        months            : projection horizon
        withdrawal_pct    : % of balance withdrawn each month (0 = reinvest all)

        Returns
        -------
        dict with ending balance, total return, CAGR, and monthly curve.
        """
        if balance <= 0:
            raise ValueError("balance must be positive")

        curve = [balance]
        r     = monthly_return_pct / 100
        w     = withdrawal_pct / 100

        for _ in range(months):
            prev  = curve[-1]
            after = prev * (1 + r) * (1 - w)
            curve.append(after)

        ending   = curve[-1]
        cagr_ann = ((ending / balance) ** (12 / max(months, 1)) - 1) * 100

        return {
            "starting":           balance,
            "ending":             round(ending, 2),
            "total_return_pct":   round((ending / balance - 1) * 100, 2),
            "cagr_annual_pct":    round(cagr_ann, 2),
            "months":             months,
            "monthly_curve":      [round(v, 2) for v in curve],
            "withdrawal_total":   round(sum(curve[i] * w for i in range(months)), 2),
        }
```


---

## Tail Risk Hedging

# Tail Risk Hedging

```python
import numpy as np, pandas as pd

class TailRiskHedging:
    """
    Quantify tail risk and recommend hedging strategies.

    Uses vectorised numpy for all statistical calculations.
    Supports both empirical VaR/CVaR and parametric (Cornish-Fisher) estimates.

    Example
    -------
    >>> risk = TailRiskHedging.assess_tail_risk(returns)
    >>> print(risk["risk_level"], risk["cvar_99"])
    'HIGH'  -3.21
    """

    @staticmethod
    def assess_tail_risk(returns: "pd.Series | np.ndarray") -> dict:
        """
        Compute full tail-risk profile from a return series.

        Parameters
        ----------
        returns : daily returns (decimal, e.g. -0.02 = -2 %)

        Returns
        -------
        dict with kurtosis, skewness, VaR/CVaR at 95 % and 99 %,
             worst daily/weekly, Cornish-Fisher adjusted VaR, and risk_level.
        """
        r = np.asarray(returns, dtype=float)
        r = r[~np.isnan(r)]
        if len(r) < 10:
            return {"error": "Need at least 10 observations"}

        s    = pd.Series(r)
        kurt = float(s.kurtosis())
        skew = float(s.skew())
        mu   = float(r.mean())
        sig  = float(r.std(ddof=1))

        # Historical VaR / CVaR
        var_95 = float(np.percentile(r, 5))
        var_99 = float(np.percentile(r, 1))
        cvar_95 = float(r[r <= var_95].mean()) if (r <= var_95).any() else var_95
        cvar_99 = float(r[r <= var_99].mean()) if (r <= var_99).any() else var_99

        # Cornish-Fisher adjusted VaR (accounts for skewness & kurtosis)
        z_95 = -1.645
        z_99 = -2.326
        cf_adj = lambda z: (z + (z**2 - 1) * skew / 6 +
                            (z**3 - 3*z) * (kurt - 3) / 24 -
                            (2*z**3 - 5*z) * skew**2 / 36)
        cf_var_95 = float(mu + cf_adj(z_95) * sig)
        cf_var_99 = float(mu + cf_adj(z_99) * sig)

        # Rolling-window worst metrics
        worst_day  = float(r.min())
        worst_week = float(s.rolling(5).sum().min())

        # Max drawdown on the return series
        equity    = np.cumprod(1 + r)
        peak      = np.maximum.accumulate(equity)
        max_dd    = float(((equity - peak) / peak).min())

        risk_level = (
            "EXTREME" if kurt > 10 or cvar_99 < -0.05 else
            "HIGH"    if kurt > 5  or cvar_99 < -0.03 else
            "MODERATE"
        )

        return {
            "n_observations":    len(r),
            "kurtosis":          round(kurt, 3),
            "skewness":          round(skew, 3),
            "fat_tails":         kurt > 3,
            "var_95":            round(var_95 * 100, 3),
            "var_99":            round(var_99 * 100, 3),
            "cvar_95":           round(cvar_95 * 100, 3),
            "cvar_99":           round(cvar_99 * 100, 3),
            "cf_var_95":         round(cf_var_95 * 100, 3),
            "cf_var_99":         round(cf_var_99 * 100, 3),
            "worst_daily_loss":  round(worst_day * 100, 3),
            "worst_weekly_loss": round(worst_week * 100, 3),
            "max_drawdown_pct":  round(max_dd * 100, 2),
            "risk_level":        risk_level,
        }

    @staticmethod
    def hedging_strategies(portfolio_size: float, risk_budget_pct: float = 2.0,
                           vix_level: float = 20.0) -> dict:
        """
        Recommend hedging strategies based on portfolio size, risk budget, and VIX.

        Parameters
        ----------
        portfolio_size   : total account value in USD
        risk_budget_pct  : % of portfolio allocated to hedging
        vix_level        : current VIX for regime-based recommendations

        Returns
        -------
        dict with hedge_budget, ranked strategies, trigger_rules, and urgency.
        """
        if portfolio_size <= 0:
            raise ValueError("portfolio_size must be positive")

        hedge_budget = portfolio_size * risk_budget_pct / 100
        urgency = (
            "CRITICAL"  if vix_level > 40 else
            "HIGH"      if vix_level > 30 else
            "ELEVATED"  if vix_level > 22 else
            "NORMAL"
        )

        return {
            "hedge_budget":  round(hedge_budget, 2),
            "vix_level":     vix_level,
            "urgency":       urgency,
            "strategies": [
                {
                    "name":       "Safe haven allocation",
                    "method":     "Hold 5-10% in JPY, CHF, Gold positions",
                    "cost":       "Low (may earn carry on some)",
                    "protection": "Moderate",
                    "recommended_at": "VIX > 20",
                },
                {
                    "name":       "Correlated short hedge",
                    "method":     "Short small position in highly correlated pair",
                    "cost":       "Spread + potential adverse move",
                    "protection": "Moderate",
                    "recommended_at": "VIX > 25",
                },
                {
                    "name":       "Reduce gross exposure",
                    "method":     "Cut all positions to 50% during high-VIX",
                    "cost":       "Opportunity cost",
                    "protection": "High",
                    "recommended_at": "VIX > 30",
                },
                {
                    "name":       "Tail-triggered stop-all",
                    "method":     "Auto-close everything if portfolio DD > 5% intraday",
                    "cost":       "Slippage on emergency close",
                    "protection": "Maximum",
                    "recommended_at": "VIX > 35",
                },
                {
                    "name":       "Diversification across timeframes",
                    "method":     "Mix scalp + swing + position strategies",
                    "cost":       "Management complexity",
                    "protection": "Moderate — decorrelates drawdowns",
                    "recommended_at": "Always",
                }],
            "trigger_rules": {
                "VIX_above_30":                 "Reduce all positions to 50%",
                "VIX_above_40":                 "Close all positions, go to cash",
                "correlation_spike_above_0.9":  "Close correlated positions — diversification broken",
                "daily_DD_above_3pct":          "Stop trading, review positions",
            },
            "active_recommendations": (
                ["Reduce gross exposure", "Tail-triggered stop-all"]
                if vix_level > 30 else
                ["Correlated short hedge", "Reduce gross exposure"]
                if vix_level > 22 else
                ["Safe haven allocation", "Diversification across timeframes"]
            ),
        }
```


---

## Spread Slippage Cost Analyzer

# Spread & Slippage Cost Analyzer

```python
import pandas as pd
import numpy as np

class CostAnalyzer:
    """
    Analyse transaction costs: spreads, slippage, and their drag on strategy returns.

    All computations are vectorised. Provides breakeven analysis so traders know
    the minimum edge needed to overcome costs.

    Example
    -------
    >>> stats = CostAnalyzer.spread_statistics(tick_df)
    >>> print(stats["avg_spread_pips"], stats["p95_spread_pips"])
    1.2  3.4
    """

    @staticmethod
    def spread_statistics(ticks: pd.DataFrame, pip_factor: float = 10_000.0) -> dict:
        """
        Full spread distribution analysis from tick data.

        Parameters
        ----------
        ticks      : DataFrame with 'ask' and 'bid' columns and DatetimeIndex
        pip_factor : multiplier to convert price diff to pips (10000 for 5-digit pairs)

        Returns
        -------
        dict with full spread distribution, widening events, and quality grade.
        """
        if "ask" not in ticks.columns or "bid" not in ticks.columns:
            raise ValueError("ticks DataFrame must have 'ask' and 'bid' columns")

        spread_pips = (ticks["ask"] - ticks["bid"]) * pip_factor
        avg         = float(spread_pips.mean())
        p95         = float(spread_pips.quantile(0.95))

        grade = (
            "EXCELLENT" if avg < 1.0 else
            "GOOD"      if avg < 2.0 else
            "FAIR"      if avg < 3.5 else
            "POOR"
        )

        return {
            "avg_spread_pips":          round(avg, 3),
            "median_spread_pips":       round(float(spread_pips.median()), 3),
            "min_spread_pips":          round(float(spread_pips.min()), 3),
            "max_spread_pips":          round(float(spread_pips.max()), 3),
            "std_spread_pips":          round(float(spread_pips.std(ddof=1)), 3),
            "p95_spread_pips":          round(p95, 3),
            "p99_spread_pips":          round(float(spread_pips.quantile(0.99)), 3),
            "spread_widening_events":   int((spread_pips > p95).sum()),
            "pct_time_above_2x_avg":    round(float((spread_pips > 2 * avg).mean()) * 100, 1),
            "spread_quality_grade":     grade,
            "n_ticks":                  len(ticks),
        }

    @staticmethod
    def spread_by_session(ticks: pd.DataFrame, pip_factor: float = 10_000.0) -> dict:
        """
        Spread behaviour per trading session — find the cheapest time to trade.

        Returns
        -------
        dict of session → {mean, median, max} spread in pips.
        """
        if not hasattr(ticks.index, "hour"):
            raise ValueError("ticks must have a DatetimeIndex")

        t = ticks.copy()
        t["spread_pips"] = (t["ask"] - t["bid"]) * pip_factor
        t["session"]     = t.index.hour.map(
            lambda h: (
                "tokyo"   if h < 7  else
                "london"  if h < 13 else
                "overlap" if h < 16 else
                "ny_late" if h < 22 else
                "off"
            )
        )
        stats = (
            t.groupby("session")["spread_pips"]
             .agg(mean="mean", median="median", max="max", p95=lambda x: x.quantile(0.95))
             .round(3)
        )
        result = stats.to_dict("index")

        # Flag cheapest session
        if result:
            cheapest = min(result, key=lambda s: result[s].get("mean", 99))
            result["_cheapest_session"] = cheapest

        return result

    @staticmethod
    def slippage_analysis(trades: pd.DataFrame, pip_factor: float = 10_000.0) -> dict:
        """
        Analyse actual slippage from trade execution data.

        Parameters
        ----------
        trades     : DataFrame with 'expected_price', 'actual_price', and optionally 'lot_size'

        Returns
        -------
        dict with average/max slippage, adverse vs favourable split, and breakeven impact.
        """
        if "expected_price" not in trades.columns or "actual_price" not in trades.columns:
            return {"error": "Need 'expected_price' and 'actual_price' columns"}
        if len(trades) == 0:
            return {"error": "No trades to analyse"}

        t = trades.copy()
        raw_slip      = (t["actual_price"] - t["expected_price"]) * pip_factor
        t["slippage"] = raw_slip.abs()
        adverse       = float((raw_slip > 0).mean() * 100)   # bought higher / sold lower

        avg_slip  = float(t["slippage"].mean())
        max_slip  = float(t["slippage"].max())
        total_pip = float(t["slippage"].sum())

        # Per-lot USD cost estimate (1 pip ≈ $10 for standard lot)
        usd_per_lot = avg_slip * 10.0 if "lot_size" not in t.columns else \
            float((t["slippage"] * t["lot_size"] * 10.0).mean())

        return {
            "avg_slippage_pips":          round(avg_slip, 3),
            "max_slippage_pips":          round(max_slip, 3),
            "p95_slippage_pips":          round(float(t["slippage"].quantile(0.95)), 3),
            "pct_adverse_slippage":       round(adverse, 1),
            "pct_favourable_slippage":    round(100 - adverse, 1),
            "total_slippage_cost_pips":   round(total_pip, 1),
            "avg_slippage_usd_per_lot":   round(usd_per_lot, 2),
            "n_trades":                   len(t),
        }

    @staticmethod
    def cost_impact_on_strategy(
        avg_spread: float,
        avg_slippage: float,
        trades_per_year: int,
        avg_profit_per_trade: float,
    ) -> dict:
        """
        Calculate what fraction of gross profit is consumed by transaction costs.

        Parameters
        ----------
        avg_spread           : average round-trip spread cost in pips
        avg_slippage         : average round-trip slippage in pips
        trades_per_year      : number of trades per year
        avg_profit_per_trade : gross average profit per trade in pips

        Returns
        -------
        dict with cost ratios, breakeven trade minimum, and verdict.
        """
        cost_rt          = avg_spread + avg_slippage
        annual_cost      = cost_rt * trades_per_year
        cost_pct         = cost_rt / max(abs(avg_profit_per_trade), 0.01) * 100
        breakeven_trades = int(np.ceil(annual_cost / max(abs(avg_profit_per_trade), 0.01)))

        return {
            "cost_per_trade_pips":   round(cost_rt, 2),
            "annual_cost_pips":      round(annual_cost, 1),
            "cost_as_pct_of_profit": round(cost_pct, 1),
            "net_profit_ratio":      round(1 - cost_pct / 100, 4),
            "breakeven_trades_year": breakeven_trades,
            "min_profit_to_survive": round(cost_rt * 1.5, 2),   # Need ≥ 1.5× cost to be viable
            "verdict": (
                "ACCEPTABLE — costs are manageable"     if cost_pct < 30 else
                "HIGH — reduce trades or find tighter broker" if cost_pct < 60 else
                "CRITICAL — costs are destroying the edge"
            ),
        }

    @staticmethod
    def broker_comparison(broker_data: list[dict]) -> pd.DataFrame:
        """
        Compare multiple brokers on cost metrics, ranked by effective total cost.

        broker_data : list of dicts with keys: broker, avg_spread_pips, commission_pips,
                      overnight_swap_long, overnight_swap_short
        """
        df = pd.DataFrame(broker_data)
        if "avg_spread_pips" not in df.columns:
            raise ValueError("Each broker entry must have 'avg_spread_pips'")

        comm_col = "commission_pips" if "commission_pips" in df.columns else None
        df["total_cost_pips"] = (
            df["avg_spread_pips"] + (df[comm_col] if comm_col else 0)
        )
        return df.sort_values("total_cost_pips").reset_index(drop=True)
```


---

## Performance Attribution Engine

# Performance Attribution Engine

```python
import pandas as pd, numpy as np
class PerformanceAttribution:
    """
    Decompose P&L into contributions by pair, setup, direction, day, session, and
    time-of-entry — to identify where the true edge lives.

    Example
    -------
    >>> report = PerformanceAttribution.attribute(journal_df)
    >>> print(report["best_pair"], report["best_setup"])
    'EURUSD'  'ICT_FVG'
    """

    @staticmethod
    def attribute(trades: pd.DataFrame) -> dict:
        """
        Full P&L attribution across all available dimensions.

        Parameters
        ----------
        trades : DataFrame with at minimum 'pnl_usd' column.
                 Optional: 'symbol', 'setup_type', 'direction', 'entry_time', 'lot_size'

        Returns
        -------
        dict with attribution by pair, setup, direction, day-of-week, session,
             hour-of-day, win-rate breakdowns, and actionable insight.
        """
        if trades.empty:
            return {"error": "No trades"}

        closed = trades[trades["pnl_usd"].notna()].copy()
        if closed.empty:
            return {"error": "No closed trades with P&L data"}

        result: dict = {}

        # ── P&L attribution by dimension ──
        def _attr(col: str) -> dict:
            if col not in closed.columns:
                return {}
            grp   = closed.groupby(col)
            pnl   = grp["pnl_usd"].sum().sort_values(ascending=False)
            count = grp["pnl_usd"].count()
            wr    = grp["pnl_usd"].apply(lambda x: (x > 0).mean() * 100).round(1)
            return {
                k: {
                    "total_pnl": round(float(pnl[k]), 2),
                    "n_trades":  int(count[k]),
                    "win_rate":  float(wr[k]),
                }
                for k in pnl.index
            }

        result["by_pair"]      = _attr("symbol")
        result["by_setup"]     = _attr("setup_type")
        result["by_direction"] = _attr("direction")

        # Day-of-week
        if "entry_time" in closed.columns:
            closed["_dow"]     = pd.to_datetime(closed["entry_time"]).dt.day_name()
            closed["_hour"]    = pd.to_datetime(closed["entry_time"]).dt.hour
            closed["_session"] = closed["_hour"].map(
                lambda h: "tokyo" if h < 7 else "london" if h < 13 else "overlap" if h < 16 else "ny" if h < 22 else "off"
            )
            result["by_day"]     = _attr("_dow")
            result["by_hour"]    = _attr("_hour")
            result["by_session"] = _attr("_session")

        # Lot-size consistency (risk management check)
        if "lot_size" in closed.columns:
            lots = closed["lot_size"]
            result["lot_size_stats"] = {
                "mean":   round(float(lots.mean()), 2),
                "std":    round(float(lots.std(ddof=1)), 2),
                "cv_pct": round(float(lots.std(ddof=1) / max(lots.mean(), 1e-10) * 100), 1),
                "note":   "CV > 50% suggests inconsistent sizing" if lots.std(ddof=1) / max(lots.mean(), 1e-10) > 0.5 else "Sizing is consistent",
            }

        # Summary leaders
        bp = result["by_pair"]
        bs = result["by_setup"]
        result["best_pair"]      = max(bp, key=lambda k: bp[k]["total_pnl"]) if bp else None
        result["worst_pair"]     = min(bp, key=lambda k: bp[k]["total_pnl"]) if bp else None
        result["best_setup"]     = max(bs, key=lambda k: bs[k]["total_pnl"]) if bs else None
        result["worst_setup"]    = min(bs, key=lambda k: bs[k]["total_pnl"]) if bs else None
        result["overall_pnl"]    = round(float(closed["pnl_usd"].sum()), 2)
        result["overall_trades"] = len(closed)
        result["overall_wr"]     = round(float((closed["pnl_usd"] > 0).mean() * 100), 1)
        result["insight"] = (
            f"Best edge: {result['best_pair']} / {result['best_setup']}. "
            f"Eliminate or reduce: {result['worst_pair']} / {result['worst_setup']}. "
            "Concentrate capital on what works."
        )
        return result
```


---

## Monte Carlo Stress Tester

# Monte Carlo Stress Tester

```python
import numpy as np
import pandas as pd
from typing import Callable, Optional

class MonteCarloStressTester:
    """
    Vectorised Monte Carlo stress testing for trading strategies.
    All simulations use numpy vectorisation — no Python loops over paths.

    Example
    -------
    >>> result = MonteCarloStressTester.bootstrap_returns(returns, n_sims=5000)
    >>> print(result["sharpe_median"])
    1.23
    """

    @staticmethod
    def _batch_metrics(paths: np.ndarray, initial: float) -> dict:
        """
        Compute metrics across all simulation paths — fully vectorised.

        Parameters
        ----------
        paths   : (n_sims, n_steps) equity array
        initial : starting equity value

        Returns
        -------
        dict with median/percentile finals and drawdowns.
        """
        finals   = paths[:, -1]                                        # (n_sims,)
        peaks    = np.maximum.accumulate(paths, axis=1)                # (n_sims, n_steps)
        dds      = (paths - peaks) / peaks                             # (n_sims, n_steps)
        max_dds  = dds.min(axis=1)                                     # (n_sims,)

        # Annualised returns per path
        n_steps  = paths.shape[1]
        ann_rets = (finals / initial) ** (252 / n_steps) - 1

        # Per-path Sharpe (approximate — log returns on each path)
        log_ret  = np.diff(np.log(paths), axis=1)                      # (n_sims, n_steps-1)
        path_sr  = (log_ret.mean(axis=1) / (log_ret.std(axis=1, ddof=1) + 1e-10)) * np.sqrt(252)

        return {
            "median_final":    round(float(np.median(finals)), 2),
            "mean_final":      round(float(finals.mean()), 2),
            "p5_final":        round(float(np.percentile(finals, 5)), 2),
            "p95_final":       round(float(np.percentile(finals, 95)), 2),
            "prob_profit":     round(float((finals > initial).mean() * 100), 1),
            "prob_ruin_50":    round(float((finals < initial * 0.5).mean() * 100), 2),
            "prob_ruin_25":    round(float((finals < initial * 0.25).mean() * 100), 2),
            "median_max_dd":   round(float(np.median(max_dds) * 100), 2),
            "worst_max_dd":    round(float(max_dds.min() * 100), 2),
            "p95_max_dd":      round(float(np.percentile(max_dds, 5) * 100), 2),
            "sharpe_median":   round(float(np.median(path_sr)), 3),
            "sharpe_p5":       round(float(np.percentile(path_sr, 5)), 3),
            "ann_return_p50":  round(float(np.median(ann_rets) * 100), 2),
        }

    @staticmethod
    def bootstrap_returns(
        returns: pd.Series,
        n_sims: int = 5000,
        n_days: int = 252,
        initial: float = 10_000,
        seed: int = 42,
    ) -> dict:
        """
        Bootstrap resampling — randomly shuffle return order to test path dependency.

        Uses fully vectorised numpy sampling (no Python for-loop over paths).

        Parameters
        ----------
        returns : daily return Series
        n_sims  : number of Monte Carlo paths
        n_days  : path length in trading days
        initial : starting equity
        seed    : random seed for reproducibility

        Returns
        -------
        dict with distributional statistics across all paths.
        """
        rng  = np.random.default_rng(seed)
        r_arr = returns.dropna().values

        # Vectorised sample: draw entire (n_sims × n_days) matrix at once
        sampled = rng.choice(r_arr, size=(n_sims, n_days), replace=True)
        paths   = initial * np.cumprod(1 + sampled, axis=1)

        result  = MonteCarloStressTester._batch_metrics(paths, initial)
        result["type"]   = "bootstrap"
        result["n_sims"] = n_sims
        return result

    @staticmethod
    def parametric_simulation(
        returns: pd.Series,
        n_sims: int = 5_000,
        n_days: int = 252,
        initial: float = 10_000,
        fat_tails: bool = True,
        seed: int = 42,
    ) -> dict:
        """
        Parametric Monte Carlo using fitted normal (or Student-t for fat tails).

        Parameters
        ----------
        fat_tails : if True, uses Student-t distribution (df=5) instead of normal

        Returns
        -------
        dict with same keys as bootstrap_returns, plus distribution parameters.
        """
        rng     = np.random.default_rng(seed)
        r_clean = returns.dropna().values
        mu      = r_clean.mean()
        sigma   = r_clean.std(ddof=1)

        if fat_tails:
            from scipy.stats import t as t_dist
            df_fit = 5.0    # Student-t degrees of freedom (fat tails)
            # Scale t-distributed samples to match empirical mu/sigma
            raw    = rng.standard_t(df=df_fit, size=(n_sims, n_days))
            samples = mu + sigma * raw / np.sqrt(df_fit / (df_fit - 2))
        else:
            samples = rng.normal(mu, sigma, size=(n_sims, n_days))

        paths  = initial * np.cumprod(1 + samples, axis=1)
        result = MonteCarloStressTester._batch_metrics(paths, initial)
        result.update({
            "type":       "parametric_fat_tails" if fat_tails else "parametric_normal",
            "n_sims":     n_sims,
            "fitted_mu":  round(mu, 6),
            "fitted_sigma": round(sigma, 6),
        })
        return result

    @staticmethod
    def parameter_perturbation(
        strategy_fn: Callable,
        base_params: dict,
        data: pd.DataFrame,
        perturbation_pct: float = 0.1,
        n_tests: int = 100,
        seed: int = 42,
    ) -> dict:
        """
        Randomly perturb strategy parameters ±X% and check robustness.

        Parameters
        ----------
        strategy_fn     : callable(data, params) → pd.Series of returns
        base_params     : baseline parameter dict
        data            : OHLCV DataFrame
        perturbation_pct: fraction of each param to perturb (0.1 = ±10 %)
        n_tests         : number of random perturbations

        Returns
        -------
        dict with Sharpe distribution and robustness verdict.
        """
        rng     = np.random.default_rng(seed)
        sharpes: list[float] = []

        for _ in range(n_tests):
            perturbed = {
                k: (type(v)(v * (1 + perturbation_pct * rng.uniform(-1, 1)))
                    if isinstance(v, (int, float)) else v)
                for k, v in base_params.items()
            }
            try:
                ret = strategy_fn(data, perturbed)
                r   = np.asarray(ret, dtype=float)
                r   = r[~np.isnan(r)]
                if len(r) < 5:
                    continue
                sharpe = float((r.mean() / r.std(ddof=1)) * np.sqrt(252)) if r.std(ddof=1) > 0 else 0.0
                sharpes.append(sharpe)
            except Exception:
                pass   # Silently skip invalid parameter combinations

        if not sharpes:
            return {"type": "parameter_perturbation", "error": "No valid perturbations"}

        s_arr = np.array(sharpes)
        pct_pos = float((s_arr > 0).mean() * 100)

        return {
            "type":             "parameter_perturbation",
            "perturbation_pct": perturbation_pct,
            "n_tests":          n_tests,
            "n_valid":          len(sharpes),
            "mean_sharpe":      round(float(s_arr.mean()), 3),
            "median_sharpe":    round(float(np.median(s_arr)), 3),
            "std_sharpe":       round(float(s_arr.std(ddof=1)), 3),
            "p5_sharpe":        round(float(np.percentile(s_arr, 5)), 3),
            "pct_profitable":   round(pct_pos, 1),
            "robust":           float(s_arr.mean()) > 0.3 and pct_pos > 70,
            "verdict": (
                "ROBUST — parameters don't matter much" if float(s_arr.mean()) > 0.3 else
                "FRAGILE — strategy is parameter-sensitive"
            ),
        }

    @staticmethod
    def regime_shuffle(
        returns: pd.Series,
        regime_labels: pd.Series,
        n_sims: int = 1_000,
        initial: float = 10_000,
        seed: int = 42,
    ) -> dict:
        """
        Shuffle regime blocks (not individual returns) to test regime robustness.
        More realistic than pure bootstrap — preserves within-regime autocorrelation.

        Parameters
        ----------
        returns       : daily return Series
        regime_labels : same-length Series of regime labels (e.g. "bull"/"bear")

        Returns
        -------
        dict with distributional statistics and regime-sensitivity flag.
        """
        rng    = np.random.default_rng(seed)
        r      = returns.values
        labels = regime_labels.values

        # Split returns into contiguous regime blocks
        blocks: list[np.ndarray] = []
        start = 0
        for i in range(1, len(labels)):
            if labels[i] != labels[i - 1]:
                blocks.append(r[start:i])
                start = i
        blocks.append(r[start:])

        finals: list[float] = []
        for _ in range(n_sims):
            idx     = rng.permutation(len(blocks))
            shuffled = np.concatenate([blocks[j] for j in idx])
            finals.append(float(initial * np.cumprod(1 + shuffled)[-1]))

        finals_arr = np.array(finals)
        coeff_var  = float(finals_arr.std() / finals_arr.mean())

        return {
            "type":              "regime_shuffle",
            "n_regimes":         int(len(set(labels))),
            "n_blocks":          len(blocks),
            "n_sims":            n_sims,
            "median_final":      round(float(np.median(finals_arr)), 2),
            "p5_final":          round(float(np.percentile(finals_arr, 5)), 2),
            "p95_final":         round(float(np.percentile(finals_arr, 95)), 2),
            "prob_profit":       round(float((finals_arr > initial).mean() * 100), 1),
            "coeff_variation":   round(coeff_var, 3),
            "regime_sensitive":  coeff_var > 0.3,
        }

    @staticmethod
    def full_stress_test(
        returns: pd.Series,
        strategy_fn: Optional[Callable] = None,
        params: Optional[dict] = None,
        data: Optional[pd.DataFrame] = None,
        n_sims: int = 5_000,
    ) -> dict:
        """
        Run all stress tests in sequence and return a consolidated report.

        Parameters
        ----------
        returns     : daily return Series
        strategy_fn : optional callable for parameter perturbation test
        params      : optional base parameter dict for perturbation test
        data        : optional DataFrame for perturbation test
        n_sims      : number of Monte Carlo simulations

        Returns
        -------
        dict with bootstrap, parametric, perturbation results and overall verdict.
        """
        report: dict = {
            "bootstrap":   MonteCarloStressTester.bootstrap_returns(returns, n_sims=n_sims),
            "parametric":  MonteCarloStressTester.parametric_simulation(returns, n_sims=n_sims),
            "metrics":     comprehensive_metrics(returns),
        }

        if strategy_fn and params and data is not None:
            report["perturbation"] = MonteCarloStressTester.parameter_perturbation(
                strategy_fn, params, data
            )

        bs = report["bootstrap"]
        report["overall_verdict"] = (
            "ROBUST"   if bs["prob_profit"] > 80 and bs["median_max_dd"] > -20 else
            "FRAGILE"  if bs["prob_profit"] < 60                              else
            "MODERATE"
        )
        return report
```


---

## Parameter Sensitivity Analyzer

# Parameter Sensitivity Analyzer

```python
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, base64

class ParameterSensitivity:
    """
    Sweep strategy parameters to identify robust vs overfit regions.

    Provides 2-D Sharpe heatmaps, one-at-a-time (OAT) sensitivity,
    and a flatness score to distinguish genuine edges from curve-fitting.

    Example
    -------
    >>> result = ParameterSensitivity.grid_sweep_2d(
    ...     my_fn, data,
    ...     {"name": "fast", "values": [5, 10, 20]},
    ...     {"name": "slow", "values": [50, 100, 200]},
    ... )
    >>> print(result["flatness"], result["robust"])
    0.82  True
    """

    @staticmethod
    def _safe_sharpe(ret: "pd.Series | np.ndarray") -> float:
        """Annualised Sharpe from a return array — NaN-safe."""
        r = np.asarray(ret, dtype=float)
        r = r[~np.isnan(r)]
        if len(r) < 5:
            return float("nan")
        std = r.std(ddof=1)
        return float((r.mean() / std) * np.sqrt(252)) if std > 0 else 0.0

    @staticmethod
    def grid_sweep_2d(
        strategy_fn: "Callable",
        data: pd.DataFrame,
        param_a: dict,
        param_b: dict,
        fixed_params: Optional[dict] = None,
        metric: str = "sharpe",
    ) -> dict:
        """
        Sweep two parameters and compute Sharpe (or other metric) at each combination.

        Parameters
        ----------
        strategy_fn  : callable(data, params) → return Series
        param_a / b  : {"name": "fast_period", "values": [5, 10, 15, 20]}
        fixed_params : parameters held constant during sweep
        metric       : currently supports "sharpe" (extendable)

        Returns
        -------
        dict with matrix, best params, flatness score, and robustness verdict.
        """
        fixed   = fixed_params or {}
        a_vals  = param_a["values"]
        b_vals  = param_b["values"]
        matrix  = np.full((len(a_vals), len(b_vals)), np.nan)

        for i, va in enumerate(a_vals):
            for j, vb in enumerate(b_vals):
                params = {**fixed, param_a["name"]: va, param_b["name"]: vb}
                try:
                    ret = strategy_fn(data, params)
                    matrix[i, j] = ParameterSensitivity._safe_sharpe(ret)
                except Exception:
                    pass   # Leave as NaN

        if np.all(np.isnan(matrix)):
            return {"error": "All parameter combinations failed"}

        best_idx = np.unravel_index(np.nanargmax(matrix), matrix.shape)
        best_a   = a_vals[best_idx[0]]
        best_b   = b_vals[best_idx[1]]
        peak     = float(matrix[best_idx])

        # Robustness: flatness of the surface around the global peak
        r0, c0   = best_idx
        neighbors = matrix[
            max(0, r0 - 1): r0 + 2,
            max(0, c0 - 1): c0 + 2]
        valid_n  = neighbors[~np.isnan(neighbors)]
        flatness = (1 - float(np.nanstd(valid_n)) / max(abs(peak), 0.01)) if len(valid_n) > 1 else 0.5

        # Pct of grid that is profitable
        pct_pos = float(np.nansum(matrix > 0) / np.sum(~np.isnan(matrix)) * 100)

        return {
            "param_a":      param_a["name"],
            "param_b":      param_b["name"],
            "matrix":       matrix.tolist(),
            "a_values":     a_vals,
            "b_values":     b_vals,
            "best": {
                param_a["name"]: best_a,
                param_b["name"]: best_b,
                "sharpe": round(peak, 3),
            },
            "flatness":     round(flatness, 3),
            "pct_positive": round(pct_pos, 1),
            "robust":       flatness > 0.7 and pct_pos > 60,
            "note": (
                "ROBUST — flat peak, most params profitable. Low overfit risk."
                if flatness > 0.7 else
                "FRAGILE — sharp peak. Strategy is curve-fitted to these parameters."
            ),
        }

    @staticmethod
    def render_heatmap(result: dict, save_path: Optional[str] = None) -> str:
        """
        Render 2D Sharpe heatmap to a base64-encoded PNG string.

        Parameters
        ----------
        result    : output dict from grid_sweep_2d
        save_path : optional file path to also save the PNG

        Returns
        -------
        base64-encoded PNG string (embed in HTML as <img src="data:image/png;base64,...">)
        """
        fig, ax = plt.subplots(figsize=(10, 8), facecolor="#131722")
        ax.set_facecolor("#131722")

        matrix   = np.array(result["matrix"])
        a_vals   = result.get("a_values", list(range(matrix.shape[0])))
        b_vals   = result.get("b_values", list(range(matrix.shape[1])))

        im = ax.imshow(matrix, cmap="RdYlGn", aspect="auto", interpolation="nearest",
                       vmin=float(np.nanpercentile(matrix, 5)),
                       vmax=float(np.nanpercentile(matrix, 95)))

        ax.set_xticks(range(len(b_vals)))
        ax.set_xticklabels(b_vals, color="#787b86", fontsize=8)
        ax.set_yticks(range(len(a_vals)))
        ax.set_yticklabels(a_vals, color="#787b86", fontsize=8)
        ax.set_xlabel(result["param_b"], color="#e0e0e0")
        ax.set_ylabel(result["param_a"], color="#e0e0e0")
        ax.set_title(
            f"Sharpe Sensitivity: {result['param_a']} vs {result['param_b']}\n"
            f"Best Sharpe={result['best']['sharpe']:.3f}  |  Flatness={result['flatness']:.2f}  |  "
            f"{'ROBUST' if result['robust'] else 'FRAGILE'}",
            color="#e0e0e0",
        )

        # Mark best point
        best_r = a_vals.index(result["best"][result["param_a"]])
        best_c = b_vals.index(result["best"][result["param_b"]])
        ax.plot(best_c, best_r, "w*", markersize=15, label=f"Best: {result['best']['sharpe']:.3f}")
        ax.legend(facecolor="#1a1a2e", edgecolor="#444", labelcolor="#e0e0e0")

        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label("Sharpe Ratio", color="#e0e0e0")
        cbar.ax.yaxis.set_tick_params(color="#787b86")

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", facecolor="#131722")
        plt.close(fig)
        buf.seek(0)

        if save_path:
            with open(save_path, "wb") as f:
                f.write(buf.getvalue())

        return base64.b64encode(buf.read()).decode("utf-8")

    @staticmethod
    def one_at_a_time(
        strategy_fn: "Callable",
        data: pd.DataFrame,
        base_params: dict,
        param_ranges: dict,
    ) -> dict:
        """
        Vary one parameter at a time while holding all others at base_params.

        Returns per-parameter sensitivity scores and a ranked list so traders know
        which parameters to be most careful about over-optimising.

        Parameters
        ----------
        param_ranges : {"param_name": [v1, v2, v3, ...], ...}

        Returns
        -------
        dict with per-parameter sharpe curves, sensitivity scores, and ranking.
        """
        results: dict = {}
        for param_name, values in param_ranges.items():
            sharpes: list[float] = []
            for v in values:
                params = {**base_params, param_name: v}
                try:
                    ret = strategy_fn(data, params)
                    sharpes.append(ParameterSensitivity._safe_sharpe(ret))
                except Exception:
                    sharpes.append(float("nan"))

            valid = [s for s in sharpes if not np.isnan(s)]
            sensitivity = (
                float(np.std(valid, ddof=1)) / max(abs(float(np.mean(valid))), 0.01)
                if len(valid) > 1 else 0.0
            )
            results[param_name] = {
                "values":         values,
                "sharpes":        [round(s, 3) if not np.isnan(s) else None for s in sharpes],
                "best_value":     values[int(np.nanargmax(sharpes))] if valid else None,
                "mean_sharpe":    round(float(np.nanmean(sharpes)), 3) if valid else None,
                "sensitivity":    round(sensitivity, 3),
                "is_sensitive":   sensitivity > 0.5,
            }

        ranked = sorted(results.items(), key=lambda x: x[1]["sensitivity"], reverse=True)
        return {
            "parameters":          results,
            "sensitivity_ranking": [(k, round(v["sensitivity"], 3)) for k, v in ranked],
            "most_sensitive":      ranked[0][0] if ranked else None,
            "least_sensitive":     ranked[-1][0] if ranked else None,
            "note":                "Most sensitive param = highest overfit risk. Focus robustness checks there.",
        }
```


---

## Trade Psychology Coach

# Trade Psychology Coach

```python
import pandas as pd, numpy as np
from datetime import datetime, timedelta

class TradePsychologyCoach:
    """
    Detect trading tilt, score discipline, identify trade-psychology-coach biases, and coach
    pre/post-trade behaviour — all from structured journal data.

    Example
    -------
    >>> result = TradePsychologyCoach.tilt_detector(journal_df)
    >>> print(result["tilt_level"], result["action"])
    'HIGH'  'STOP TRADING IMMEDIATELY...'
    """

    # ── Tilt thresholds ────────────────────────────────────────────────────
    _TILT_CONSEC_LOSSES   = 3     # consecutive losses to flag
    _TILT_GAP_MINUTES     = 15    # rapid-fire: avg minutes between trades
    _TILT_SL_WIDENING_PCT = 1.5   # stop wider than average × this → flagged
    _TILT_SIZE_INCREASE   = True  # flag monotone lot increase after losses

    @staticmethod
    def tilt_detector(trades: pd.DataFrame, n_recent: int = 10) -> dict:
        """
        Detect revenge trading, tilt, and overtrading from trade history.

        Parameters
        ----------
        trades   : journal DataFrame (requires 'pnl_pips'; optional lot_size, entry_time, etc.)
        n_recent : look at last N trades for tilt signals

        Returns
        -------
        dict with tilt_level (CALM/ELEVATED/MODERATE/HIGH), signals, and action.
        """
        if trades.empty or len(trades) < 3:
            return {"tilt_level": "INSUFFICIENT DATA", "n_trades": len(trades)}

        recent  = trades.tail(n_recent).copy()
        signals: list[str] = []

        # ── Consecutive loss streak (vectorised) ──
        pnl_col = "pnl_pips" if "pnl_pips" in recent.columns else "pnl_usd"
        if pnl_col in recent.columns:
            pnl_arr = recent[pnl_col].values
            streak  = 0
            max_streak = 0
            for p in pnl_arr:
                if p < 0:
                    streak += 1
                    max_streak = max(max_streak, streak)
                else:
                    streak = 0
            if max_streak >= TradePsychologyCoach._TILT_CONSEC_LOSSES:
                signals.append(f"{max_streak} consecutive losses detected")
        else:
            max_streak = 0

        # ── Increasing position sizes after losses ──
        if "lot_size" in recent.columns and pnl_col in recent.columns:
            pnl_s = recent[pnl_col].values
            lots  = recent["lot_size"].values
            # Check if last 3 lots are monotonically increasing following losses
            recent_lots = lots[-3:]
            if len(recent_lots) == 3 and all(recent_lots[i] > recent_lots[i-1] for i in range(1, 3)):
                if pnl_s[-4] < 0 if len(pnl_s) >= 4 else True:
                    signals.append("DANGER: Lot size increasing after loss — revenge pattern")

        # ── Rapid-fire entries ──
        if "entry_time" in recent.columns and len(recent) >= 3:
            times = pd.to_datetime(recent["entry_time"]).sort_values()
            gaps  = times.diff().dt.total_seconds().dropna() / 60
            avg_gap = float(gaps.tail(3).mean()) if len(gaps) >= 3 else 99.0
            if avg_gap < TradePsychologyCoach._TILT_GAP_MINUTES:
                signals.append(f"Rapid-fire entries (avg {avg_gap:.0f} min apart) — possible overtrading")

        # ── Widening stop losses ──
        if "stop_loss" in recent.columns and "entry_price" in recent.columns:
            sl_dist = (recent["entry_price"] - recent["stop_loss"]).abs()
            if sl_dist.tail(3).mean() > sl_dist.mean() * TradePsychologyCoach._TILT_SL_WIDENING_PCT:
                signals.append("Stop losses widening — hope trading detected")

        # ── Tilt score ──
        tilt_level = (
            "HIGH"     if len(signals) >= 3 else
            "MODERATE" if len(signals) >= 2 else
            "ELEVATED" if signals else
            "CALM"
        )

        actions = {
            "HIGH":     "STOP TRADING IMMEDIATELY. Walk away ≥4 hours. Review journal before returning.",
            "MODERATE": "Take a 30-minute break. Halve position size on next trade.",
            "ELEVATED": "Caution. Next trade must be an A+ setup only.",
            "CALM":     "Emotional state appears normal. Continue with plan.",
        }

        return {
            "tilt_level":        tilt_level,
            "tilt_score":        len(signals),
            "signals":           signals,
            "consecutive_losses": max_streak,
            "n_trades_analysed": len(recent),
            "action":            actions[tilt_level],
        }

    @staticmethod
    def trade-psychology-coach_bias_check(trade_context: dict) -> list[dict]:
        """
        Flag active trade-psychology-coach biases from a trade context dict.

        trade_context keys (all optional booleans):
            adding_to_loser, moved_stop_loss_further, closed_winner_early,
            entered_because_others_said, big_win_then_bigger_risk,
            missed_trade_then_chased, trading_outside_plan_hours,
            increased_size_after_loss
        """
        BIAS_REGISTRY = [
            ("adding_to_loser",             "Sunk Cost Fallacy",      "Your entry price is irrelevant now. Would you enter fresh at current price?"),
            ("moved_stop_loss_further",      "Loss Aversion",          "Moving a stop is breaking your contract with yourself. Your system trusted that level."),
            ("closed_winner_early",          "Disposition Effect",     "You're cutting winners and riding losers. Reverse this: trail winners, cut losers at plan."),
            ("entered_because_others_said",  "Herding Bias",           "Others' analysis is noise unless you independently verified it on your own chart."),
            ("big_win_then_bigger_risk",     "House Money Effect",     "Profits are real money. They are not 'free' to risk. Maintain standard sizing."),
            ("missed_trade_then_chased",     "FOMO",                   "There will always be another setup. Chasing produces bad fills and destroys edge."),
            ("trading_outside_plan_hours",   "Boredom / Impulsivity",  "Trading outside your planned sessions exposes you to low-liquidity, unpredictable moves."),
            ("increased_size_after_loss",    "Martingale Fallacy",     "The market does not owe you a win. Past losses have no predictive value on the next trade.")]
        biases = []
        for key, name, fix in BIAS_REGISTRY:
            if trade_context.get(key):
                biases.append({
                    "bias":     name,
                    "trigger":  key,
                    "fix":      fix,
                    "severity": "HIGH" if key in ("adding_to_loser", "moved_stop_loss_further") else "MODERATE",
                })
        return biases

    @staticmethod
    def discipline_score(journal: pd.DataFrame) -> dict:
        """
        Score trading discipline across multiple dimensions from journal data.

        Parameters
        ----------
        journal : DataFrame with columns like followed_plan (bool), setup_type (str),
                  lot_size (float), pnl_pips (float)

        Returns
        -------
        dict with weighted discipline_score (0–100), grade, and component breakdown.
        """
        if journal.empty:
            return {"discipline_score": 0.0, "grade": "F", "error": "No journal data"}

        components: dict[str, float] = {}

        # Plan adherence (highest weight)
        if "followed_plan" in journal.columns:
            components["plan_adherence"] = float(journal["followed_plan"].mean() * 100)

        # Setup quality (only named setups)
        if "setup_type" in journal.columns:
            components["setup_quality"] = float((journal["setup_type"].astype(str).str.strip() != "").mean() * 100)

        # Sizing consistency after losses
        if "lot_size" in journal.columns and "pnl_pips" in journal.columns:
            losers   = journal[journal["pnl_pips"] < 0]
            if len(losers) > 0:
                next_lots = journal["lot_size"].shift(-1).reindex(losers.index)
                pct_not_revenge = float((next_lots <= losers["lot_size"]).mean() * 100)
                components["sizing_after_loss"] = pct_not_revenge

        # Emotional score (if present)
        if "emotional_score" in journal.columns:
            components["emotional_score"] = float(journal["emotional_score"].mean() / 10 * 100)

        # Weighted average (plan_adherence counts more)
        weights = {
            "plan_adherence":   3,
            "setup_quality":    2,
            "sizing_after_loss": 2,
            "emotional_score":  1,
        }
        total_w = sum(weights[k] for k in components)
        avg     = sum(components[k] * weights[k] for k in components) / max(total_w, 1)

        return {
            "discipline_score": round(avg, 1),
            "grade":            "A" if avg >= 85 else "B" if avg >= 70 else "C" if avg >= 55 else "D" if avg >= 40 else "F",
            "components":       {k: round(v, 1) for k, v in components.items()},
            "n_trades":         len(journal),
            "advice": (
                "Excellent discipline. Maintain current process."     if avg >= 85 else
                "Good. Work on weakest component above."             if avg >= 70 else
                "Average. Implement a stricter pre-trade checklist." if avg >= 55 else
                "Below average. Consider reducing frequency until score > 70." if avg >= 40 else
                "CRITICAL. Stop live trading and return to demo until score > 70."
            ),
        }

    @staticmethod
    def pre_trade_checklist() -> dict:
        """Return a structured pre-trade checklist with pass/fail criteria."""
        return {
            "questions": [
                {"q": "Is this setup in my playbook?",                          "fail_action": "Do NOT trade — random setups destroy consistency."},
                {"q": "Am I entering because of the setup, not boredom/FOMO?",  "fail_action": "Step away for 30 minutes and reassess."},
                {"q": "Is my position size within my daily risk rules?",        "fail_action": "Resize to comply before entering."},
                {"q": "Have I defined entry, stop, and take-profit?",           "fail_action": "Define levels first — no undefined exits."},
                {"q": "Am I emotionally neutral (not tilted or overconfident)?", "fail_action": "Run tilt_detector() first."},
                {"q": "Is there a high-impact news event in the next 30 min?",  "fail_action": "Wait until after the release."},
                {"q": "Is current session quality acceptable?",                 "fail_action": "Avoid low-liquidity sessions unless planned."}],
            "rule": "Answer all 7 honestly. If ANY is NO — do NOT place the trade.",
            "pass_threshold": 7,
        }
```

---

## Trade-Level Risk Refinement (ICT/SMC)

### Midpoint Entry Technique (SL Halving)

When a FVG or PD Array zone is large, entering at the **top/bottom edge** results in an oversized SL. Instead:

- Place entry at the **50% midpoint** of the zone
- Effect: SL distance roughly **halved** → R:R approximately **doubled** on the same setup
- Application: any large FVG, OB, or Breaker Block where edge-entry SL is too wide
- Same principle applies to very small zones: use a wider surrouding structure as SL to avoid stop hunts

```python
def midpoint_entry_rr(zone_top, zone_bottom, sl_beyond, tp_target):
    """
    Compare edge-entry vs midpoint-entry R:R for a PD Array zone.
    zone_top/bottom: price levels of the zone
    sl_beyond:       SL price (below zone for longs, above for shorts)
    tp_target:       TP price
    """
    midpoint = (zone_top + zone_bottom) / 2
    edge_entry = zone_top          # long entry at top of zone (full zone SL)
    mid_entry  = midpoint          # long entry at midpoint

    edge_sl_dist = abs(edge_entry - sl_beyond)
    mid_sl_dist  = abs(mid_entry  - sl_beyond)

    edge_rr = abs(tp_target - edge_entry) / edge_sl_dist if edge_sl_dist else 0
    mid_rr  = abs(tp_target - mid_entry)  / mid_sl_dist  if mid_sl_dist  else 0

    return {
        "edge_entry": edge_entry, "edge_rr": round(edge_rr, 2),
        "mid_entry":  mid_entry,  "mid_rr":  round(mid_rr, 2),
        "rr_improvement": f"{round((mid_rr / edge_rr - 1) * 100, 1)}%" if edge_rr else "N/A",
    }
```

### Partial Close & Break-Even Rule (Systematic Trade Management)

A standard trade management protocol to lock in gains and remove risk:

| Stage | Action |
|-------|--------|
| Entry | Full position in, SL at planned level |
| TP1 (1:1 R:R) | Close **50% of position**, move SL to **break-even** |
| TP2 (final) | First key HTF level in front of price |
| Stop trail (after TP1) | Trail using LTF swing points |

- The 1:1 partial close guarantees the trade cannot be a net loss after TP1 is hit
- Use when trading with HTF FVG context (FVG-in-FVG strategy) or any multi-target setup
- Do not move SL to break-even prematurely — only after TP1 is confirmed hit

---

## Related Skills

- [Portfolio Optimization](../portfolio-optimization.md)
- [Risk Performance](../risk-and-portfolio.md)
- [Portfolio Strategy Allocation](../portfolio-optimization.md)
- [Trading Fundamentals](../trading-fundamentals.md)

status: active
---

# Multi-Account Manager & Tail Risk Hedging

## Part 1: Multi-Account Manager

Track P&L across multiple broker accounts, aggregate reporting, and performance comparison.

```python
import pandas as pd
from dataclasses import dataclass
from datetime import datetime
import json, os

@dataclass
class BrokerAccount:
    id: str
    broker: str
    account_number: str
    currency: str       = "USD"
    balance: float      = 0.0
    equity: float       = 0.0
    margin_used: float  = 0.0
    open_positions: int = 0
    daily_pnl: float    = 0.0
    total_pnl: float    = 0.0
    leverage: int       = 100
    last_updated: str   = ""

class MultiAccountManager:

    def __init__(self, path: str = "/home/claude/trading_data_store/accounts"):
        self.path = path
        os.makedirs(path, exist_ok=True)
        self.file     = f"{path}/accounts.json"
        self.accounts = self._load()

    def _load(self) -> list[dict]:
        if os.path.exists(self.file):
            with open(self.file) as f:
                return json.load(f)
        return []

    def _save(self):
        with open(self.file, "w") as f:
            json.dump(self.accounts, f, indent=2, default=str)

    def add_account(self, account: BrokerAccount):
        self.accounts.append(account.__dict__)
        self._save()

    def update_account(self, account_id: str, **kwargs):
        for acc in self.accounts:
            if acc["id"] == account_id:
                acc.update(kwargs)
                acc["last_updated"] = datetime.utcnow().isoformat()
        self._save()

    def aggregate_summary(self) -> dict:
        if not self.accounts:
            return {"error": "No accounts registered"}
        total_balance  = sum(a["balance"]      for a in self.accounts)
        total_equity   = sum(a["equity"]       for a in self.accounts)
        total_daily    = sum(a["daily_pnl"]    for a in self.accounts)
        total_margin   = sum(a["margin_used"]  for a in self.accounts)
        return {
            "n_accounts":           len(self.accounts),
            "total_balance":        round(total_balance, 2),
            "total_equity":         round(total_equity, 2),
            "total_daily_pnl":      round(total_daily, 2),
            "total_margin_used":    round(total_margin, 2),
            "margin_utilization_pct": round(total_margin / max(total_equity, 1) * 100, 2),
            "best_performer":  max(self.accounts, key=lambda a: a["daily_pnl"])["id"] if self.accounts else None,
            "worst_performer": min(self.accounts, key=lambda a: a["daily_pnl"])["id"] if self.accounts else None,
            "accounts":        self.accounts,
        }

    def compare_accounts(self) -> pd.DataFrame:
        return pd.DataFrame(self.accounts)[[
            "id", "broker", "balance", "equity", "daily_pnl", "total_pnl", "leverage"
        ]].sort_values("total_pnl", ascending=False)

    def total_exposure_check(self, max_margin_pct: float = 50.0) -> dict:
        """Check if total margin utilization across all accounts is within limits."""
        summary = self.aggregate_summary()
        if "error" in summary:
            return summary
        margin_pct = summary["margin_utilization_pct"]
        return {
            "total_equity":      summary["total_equity"],
            "total_margin_used": summary["total_margin_used"],
            "margin_pct":        margin_pct,
            "status": "OK" if margin_pct < max_margin_pct else "WARNING — reduce exposure",
            "recommendation": f"Margin at {margin_pct:.1f}% — target below {max_margin_pct}%",
        }
```

---

## Part 2: Tail Risk Hedging

Black swan protection, portfolio insurance, and crash scenario preparation.

```python
import numpy as np
import pandas as pd

class TailRiskHedging:

    @staticmethod
    def assess_tail_risk(returns: pd.Series) -> dict:
        """Measure fat tails, skewness, and extreme loss metrics."""
        kurtosis    = returns.kurtosis()
        skew        = returns.skew()
        var_99      = returns.quantile(0.01)
        cvar_99     = returns[returns <= var_99].mean()
        worst_day   = returns.min()
        worst_week  = returns.rolling(5).sum().min()
        return {
            "kurtosis":         round(kurtosis, 2),
            "skewness":         round(skew, 3),
            "fat_tails":        kurtosis > 3,
            "var_99_pct":       round(var_99 * 100, 3),
            "cvar_99_pct":      round(cvar_99 * 100, 3),
            "worst_day_pct":    round(worst_day * 100, 3),
            "worst_week_pct":   round(worst_week * 100, 3),
            "risk_level":       "EXTREME" if kurtosis > 10 else "HIGH" if kurtosis > 5 else "MODERATE",
        }

    @staticmethod
    def hedging_strategies(portfolio_size: float, risk_budget_pct: float = 2.0) -> dict:
        """Return a menu of tail hedging strategies ranked by cost and protection."""
        hedge_budget = portfolio_size * risk_budget_pct / 100
        return {
            "hedge_budget": round(hedge_budget, 2),
            "strategies": [
                {
                    "name":       "Safe haven allocation",
                    "method":     "Hold 5-10% in JPY, CHF, Gold positions",
                    "cost":       "Low (may earn carry on some)",
                    "protection": "Moderate",
                    "when":       "Always — baseline tail hedge",
                },
                {
                    "name":       "Correlated short hedge",
                    "method":     "Short small position in highly correlated pair",
                    "cost":       "Spread + potential adverse move",
                    "protection": "Moderate",
                    "when":       "When directional exposure is concentrated",
                },
                {
                    "name":       "Reduce gross exposure",
                    "method":     "Cut all positions to 50% when VIX > 25",
                    "cost":       "Opportunity cost",
                    "protection": "High",
                    "when":       "Elevated volatility regime",
                },
                {
                    "name":       "Tail-triggered stop-all",
                    "method":     "Auto-close everything if portfolio DD > 5% intraday",
                    "cost":       "Slippage on emergency close",
                    "protection": "Maximum",
                    "when":       "As a hard circuit breaker",
                },
                {
                    "name":       "Timeframe diversification",
                    "method":     "Mix scalp + swing + position strategies",
                    "cost":       "Management complexity",
                    "protection": "Moderate — decorrelates drawdowns",
                    "when":       "Multi-strategy portfolio construction",
                }],
            "trigger_rules": {
                "VIX_above_25":                "Reduce all positions to 75%",
                "VIX_above_30":                "Reduce all positions to 50%",
                "VIX_above_40":                "Close all positions, go to cash",
                "correlation_spike_above_0.9": "Close correlated positions — diversification broken",
                "daily_DD_above_3pct":         "Stop trading, review positions",
                "daily_DD_above_5pct":         "KILL SWITCH — close everything",
            },
        }

    @staticmethod
    def scenario_stress_test(portfolio_returns: pd.Series) -> dict:
        """Estimate portfolio loss under historical crash scenarios."""
        # Reference historical crash magnitudes (monthly % losses)
        scenarios = {
            "2008 GFC":          -0.40,
            "2020 COVID crash":  -0.30,
            "2015 China shock":  -0.15,
            "2011 Euro crisis":  -0.20,
            "1987 Black Monday": -0.25,
        }
        vol = portfolio_returns.std() * np.sqrt(252)
        results = {}
        for scenario, market_shock in scenarios.items():
            # Beta-adjusted estimate (assumes ~60% correlation to market)
            estimated_loss = market_shock * 0.6
            results[scenario] = {
                "market_shock_pct":     round(market_shock * 100, 1),
                "estimated_loss_pct":   round(estimated_loss * 100, 1),
                "verdict": "SURVIVABLE" if estimated_loss > -0.20 else "SEVERE",
            }
        return {
            "portfolio_annual_vol": round(vol * 100, 2),
            "scenario_results":     results,
            "recommendation": "Hold ≥5% safe havens and set hard kill switch at 10% DD",
        }
```

---

## Tail Risk Quick Reference

| Trigger | Action |
|---|---|
| VIX > 25 | Reduce to 75% normal size |
| VIX > 30 | Reduce to 50% |
| VIX > 40 | Go to cash |
| Correlation spike > 0.9 | Close correlated positions |
| Daily DD > 3% | Stop new trades, review |
| Daily DD > 5% | Close everything (kill switch) |
| Drawdown > 15% | Pause trading, revalidate strategy |

### Baseline Tail Hedge Allocation
- 5% JPY/CHF pairs (long)
- 5% Gold (XAU/USD long)
- Hard intraday DD circuit breaker at 5%
- Weekly loss limit at 10%
# Risk Premia Harvester

```python
import pandas as pd, numpy as np

class RiskPremiaHarvester:
    @staticmethod
    def momentum_factor(returns_by_pair: pd.DataFrame, lookback: int = 60) -> dict:
        """Long top momentum, short bottom momentum. Classic cross-sectional momentum."""
        mom = returns_by_pair.tail(lookback).sum()
        ranked = mom.rank(pct=True)
        longs = ranked[ranked > 0.7].index.tolist()
        shorts = ranked[ranked < 0.3].index.tolist()
        return {"factor": "momentum", "longs": longs, "shorts": shorts, "lookback": lookback,
                "spread_return": round((mom[longs].mean() - mom[shorts].mean()) * 100, 2) if longs and shorts else 0}

    @staticmethod
    def value_factor(pairs: dict) -> dict:
        """Value = trade towards PPP or REER fair value. Long undervalued, short overvalued."""
        longs = [p for p, v in pairs.items() if v.get("undervalued")]
        shorts = [p for p, v in pairs.items() if v.get("overvalued")]
        return {"factor": "value", "longs": longs, "shorts": shorts,
                "note": "PPP-based value reverts over 1-3 year horizons. Very slow factor."}

    @staticmethod
    def carry_factor(rate_diffs: dict) -> dict:
        """Long high-yielding, short low-yielding currencies."""
        sorted_pairs = sorted(rate_diffs.items(), key=lambda x: x[1], reverse=True)
        longs = [p for p, r in sorted_pairs[:3]]
        shorts = [p for p, r in sorted_pairs[-3:]]
        return {"factor": "carry", "longs": longs, "shorts": shorts,
                "carry_spread": round(sorted_pairs[0][1] - sorted_pairs[-1][1], 2)}

    @staticmethod
    def volatility_factor(vol_by_pair: dict) -> dict:
        """Sell high IV, buy low IV. Variance risk premium harvesting."""
        sorted_pairs = sorted(vol_by_pair.items(), key=lambda x: x[1].get("iv_rank", 50), reverse=True)
        sells = [p for p, v in sorted_pairs[:3] if v.get("iv_rank", 50) > 70]
        buys = [p for p, v in sorted_pairs[-3:] if v.get("iv_rank", 50) < 30]
        return {"factor": "volatility", "sell_vol": sells, "buy_vol": buys}

    @staticmethod
    def combined_portfolio(momentum: dict, carry: dict, vol: dict) -> dict:
        """Equal-weight across factors for diversified risk premia portfolio."""
        all_longs = set(momentum.get("longs", []) + carry.get("longs", []))
        all_shorts = set(momentum.get("shorts", []) + vol.get("sell_vol", []))
        return {
            "portfolio_longs": list(all_longs),
            "portfolio_shorts": list(all_shorts),
            "n_factors": 3,
            "rebalance": "Monthly",
            "note": "Factor portfolios earn ~2-5% annually each. Combined = ~6-12% with lower vol than any single factor.",
        }
```
