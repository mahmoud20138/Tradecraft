---
name: cross-asset-relationships
description: "Cross-asset and quantitative analysis: pair correlations, correlation heatmaps, currency strength, cross-timeframe divergence, intermarket analysis, market breadth, carry trades, swap rates, risk premia, and multi-pair baskets. USE FOR: correlation, currency strength, intermarket, market breadth, carry trade, swap rate, risk premia, basket, pair trading, cross asset, quant."
related_skills:
  - market-intelligence
  - portfolio-optimization
  - forex-trading
  - risk-and-portfolio
tags:
  - trading
  - fundamentals
  - correlation
  - intermarket
  - carry-trade
  - cross-asset
skill_level: advanced
kind: reference
category: trading/market-context
status: active
---
> **Skill:** Cross Asset Relationships  |  **Domain:** trading  |  **Category:** fundamentals  |  **Level:** advanced
> **Tags:** `trading`, `fundamentals`, `correlation`, `intermarket`, `carry-trade`, `cross-asset`



---

## Pair Correlation Engine

# Pair Correlation Engine

## Overview
Analyzes statistical relationships between financial instruments across multiple timeframes
and historical periods. Detects regime shifts, divergences, lead-lag relationships, and
provides actionable correlation intelligence for trading decisions.

## Architecture

```
┌───────────────────────────────────────────────────┐
│            Pair Correlation Engine                 │
├────────────┬─────────────┬────────────────────────┤
│ Correlation│ History vs  │ Regime Detection &     │
│ Matrix     │ Current     │ Divergence Scanner     │
└────────────┴─────────────┴────────────────────────┘
```

---

## 1. Core Correlation Computation

```python
import pandas as pd
import numpy as np
from scipy import stats
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from typing import Optional
from datetime import datetime, timedelta

def compute_returns(prices: pd.DataFrame, method: str = "log") -> pd.DataFrame:
    """Convert price DataFrame to returns. Columns = symbols."""
    if method == "log":
        return np.log(prices / prices.shift(1)).dropna()
    return prices.pct_change().dropna()

def correlation_matrix(
    prices: pd.DataFrame,
    method: str = "pearson",
    window: Optional[int] = None
) -> pd.DataFrame:
    """
    Full correlation matrix.
    method: pearson, spearman, kendall
    window: if set, uses last N bars only
    """
    returns = compute_returns(prices)
    if window:
        returns = returns.tail(window)
    return returns.corr(method=method)

def rolling_correlation(
    series_a: pd.Series,
    series_b: pd.Series,
    window: int = 60,
    method: str = "pearson"
) -> pd.Series:
    """Rolling window correlation between two series."""
    ret_a = np.log(series_a / series_a.shift(1)).dropna()
    ret_b = np.log(series_b / series_b.shift(1)).dropna()
    aligned = pd.concat([ret_a, ret_b], axis=1).dropna()
    aligned.columns = ["a", "b"]
    return aligned["a"].rolling(window).corr(aligned["b"])
```

---

## 2. Historical vs Current Correlation (Core Feature)

```python
def historical_vs_current(
    prices: pd.DataFrame,
    current_window: int = 30,
    historical_windows: list[int] = [90, 180, 365],
    method: str = "pearson"
) -> dict:
    """
    Compare current correlation regime vs historical norms.
    Returns: {pair: {current, hist_90d, hist_180d, hist_365d, deviation, regime_shift}}
    """
    returns = compute_returns(prices)
    symbols = returns.columns.tolist()
    results = {}

    for i, sym_a in enumerate(symbols):
        for sym_b in symbols[i + 1:]:
            pair_key = f"{sym_a}/{sym_b}"
            pair_data = returns[[sym_a, sym_b]].dropna()

            current_corr = pair_data.tail(current_window).corr().iloc[0, 1]

            hist_corrs = {}
            for w in historical_windows:
                if len(pair_data) >= w:
                    hist_corrs[f"hist_{w}d"] = pair_data.tail(w).corr().iloc[0, 1]
                else:
                    hist_corrs[f"hist_{w}d"] = np.nan

            # Compute deviation from longest available history
            longest_hist = next((hist_corrs[f"hist_{w}d"] for w in sorted(historical_windows, reverse=True)
                                 if not np.isnan(hist_corrs.get(f"hist_{w}d", np.nan))), np.nan)

            deviation = current_corr - longest_hist if not np.isnan(longest_hist) else 0
            regime_shift = abs(deviation) > 0.3  # >0.3 = significant regime change

            results[pair_key] = {
                "current": round(current_corr, 4),
                **{k: round(v, 4) for k, v in hist_corrs.items()},
                "deviation": round(deviation, 4),
                "regime_shift": regime_shift,
                "signal": _interpret_deviation(deviation),
            }

    return results

def _interpret_deviation(dev: float) -> str:
    """Interpret correlation deviation into actionable signal."""
    if abs(dev) < 0.1: return "STABLE — correlations normal"
    if dev > 0.3: return "CONVERGENCE — pairs moving together unusually strongly"
    if dev < -0.3: return "DIVERGENCE — pairs decoupling, watch for mean reversion"
    if dev > 0.1: return "STRENGTHENING — correlation increasing"
    return "WEAKENING — correlation decreasing"
```

---

## 3. Divergence Detection

```python
def detect_divergences(
    prices: pd.DataFrame,
    lookback: int = 60,
    threshold: float = 0.3
) -> list[dict]:
    """
    Find pairs that have recently diverged from their historical correlation.
    These are potential mean-reversion or trend-change signals.
    """
    hvc = historical_vs_current(prices, current_window=lookback // 2)
    divergences = []
    for pair, data in hvc.items():
        if data["regime_shift"]:
            divergences.append({
                "pair": pair,
                "current_corr": data["current"],
                "historical_corr": data.get("hist_365d", data.get("hist_180d", np.nan)),
                "deviation": data["deviation"],
                "type": "convergence_anomaly" if data["deviation"] > 0 else "divergence_anomaly",
                "signal": data["signal"],
                "priority": abs(data["deviation"]),
            })
    return sorted(divergences, key=lambda x: x["priority"], reverse=True)

def spread_analysis(
    price_a: pd.Series,
    price_b: pd.Series,
    window: int = 60
) -> pd.DataFrame:
    """
    Compute normalized spread between two series for pair trading.
    Z-score indicates mean-reversion opportunity.
    """
    # Normalize both series to start at 1.0
    norm_a = price_a / price_a.iloc[0]
    norm_b = price_b / price_b.iloc[0]
    spread = norm_a - norm_b
    z_score = (spread - spread.rolling(window).mean()) / spread.rolling(window).std()
    return pd.DataFrame({
        "spread": spread, "z_score": z_score,
        "upper_band": spread.rolling(window).mean() + 2 * spread.rolling(window).std(),
        "lower_band": spread.rolling(window).mean() - 2 * spread.rolling(window).std(),
    })
```

---

## 4. Lead-Lag Analysis

```python
def lead_lag_analysis(
    series_a: pd.Series,
    series_b: pd.Series,
    max_lag: int = 10
) -> pd.DataFrame:
    """
    Cross-correlation at different lags to detect if one pair leads another.
    Positive lag = A leads B. Negative lag = B leads A.
    """
    ret_a = np.log(series_a / series_a.shift(1)).dropna()
    ret_b = np.log(series_b / series_b.shift(1)).dropna()
    aligned = pd.concat([ret_a, ret_b], axis=1).dropna()
    aligned.columns = ["a", "b"]

    results = []
    for lag in range(-max_lag, max_lag + 1):
        if lag >= 0:
            corr = aligned["a"].iloc[lag:].reset_index(drop=True).corr(aligned["b"].iloc[:len(aligned) - lag].reset_index(drop=True))
        else:
            corr = aligned["a"].iloc[:len(aligned) + lag].reset_index(drop=True).corr(aligned["b"].iloc[-lag:].reset_index(drop=True))
        results.append({"lag": lag, "correlation": round(corr, 4)})

    df = pd.DataFrame(results)
    best = df.loc[df["correlation"].abs().idxmax()]
    df.attrs["best_lag"] = int(best["lag"])
    df.attrs["best_corr"] = float(best["correlation"])
    df.attrs["interpretation"] = (
        f"{'A leads B' if best['lag'] > 0 else 'B leads A' if best['lag'] < 0 else 'Synchronous'} "
        f"by {abs(int(best['lag']))} bars (r={best['correlation']:.4f})"
    )
    return df
```

---

## 5. Cluster Analysis — Group Correlated Pairs

```python
def cluster_pairs(
    prices: pd.DataFrame,
    n_clusters: int = 4,
    method: str = "ward"
) -> dict:
    """
    Hierarchical clustering of instruments by correlation.
    Returns cluster assignments and cluster statistics.
    """
    corr = correlation_matrix(prices)
    distance = np.sqrt(2 * (1 - corr))
    np.fill_diagonal(distance.values, 0)

    condensed = distance.values[np.triu_indices_from(distance.values, k=1)]
    Z = linkage(condensed, method=method)
    labels = fcluster(Z, t=n_clusters, criterion="maxclust")

    clusters = {}
    for sym, cluster_id in zip(corr.columns, labels):
        cid = int(cluster_id)
        if cid not in clusters:
            clusters[cid] = []
        clusters[cid].append(sym)

    return {
        "n_clusters": n_clusters,
        "clusters": clusters,
        "linkage": Z,
        "assignments": dict(zip(corr.columns.tolist(), [int(l) for l in labels])),
    }

def find_hedge_pairs(
    prices: pd.DataFrame,
    target_symbol: str,
    min_negative_corr: float = -0.5
) -> list[dict]:
    """Find instruments negatively correlated to target — potential hedges."""
    corr = correlation_matrix(prices)
    if target_symbol not in corr.columns:
        return []
    target_corr = corr[target_symbol].drop(target_symbol).sort_values()
    hedges = []
    for sym, c in target_corr.items():
        if c <= min_negative_corr:
            hedges.append({"symbol": sym, "correlation": round(c, 4), "hedge_quality": "strong" if c < -0.7 else "moderate"})
    return hedges
```

---

## 6. Correlation Report Generator

```python
def full_correlation_report(
    prices: pd.DataFrame,
    current_window: int = 30
) -> dict:
    """
    Complete correlation intelligence report.
    Pipe this to trading-brain for decision-making.
    """
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "symbols_analyzed": prices.columns.tolist(),
        "n_bars": len(prices),
        "current_matrix": correlation_matrix(prices, window=current_window).to_dict(),
        "historical_matrix": correlation_matrix(prices).to_dict(),
        "historical_vs_current": historical_vs_current(prices, current_window),
        "divergences": detect_divergences(prices),
        "clusters": cluster_pairs(prices),
    }
```

---

## Usage Conventions

1. **Always use log returns** for correlation — more statistically stable than simple returns
2. **Check sample size** — need minimum 30 bars for meaningful correlation
3. **Multi-timeframe** — compute correlations on H1, H4, and D1 for robust signals
4. **Regime shifts > 0.3** are significant and should trigger alerts
5. **Lead-lag > 2 bars** with |r| > 0.3 is a potential predictive signal
6. **Correlation ≠ causation** — always note this in reports


---

## Correlation Heatmap Visualizer

# Correlation Heatmap Visualizer

```python
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, base64

class CorrelationHeatmapVisualizer:
    @staticmethod
    def render(prices: pd.DataFrame, method: str = "pearson", window: int = None, save_path: str = None) -> str:
        returns = np.log(prices / prices.shift(1)).dropna()
        if window: returns = returns.tail(window)
        corr = returns.corr(method=method)
        fig, ax = plt.subplots(figsize=(12, 10), facecolor="#131722")
        ax.set_facecolor("#131722")
        im = ax.imshow(corr.values, cmap="RdYlGn", vmin=-1, vmax=1, aspect="auto")
        ax.set_xticks(range(len(corr.columns))); ax.set_yticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=45, ha="right", fontsize=8, color="#e0e0e0")
        ax.set_yticklabels(corr.columns, fontsize=8, color="#e0e0e0")
        for i in range(len(corr)):
            for j in range(len(corr)):
                color = "white" if abs(corr.values[i, j]) > 0.5 else "gray"
                ax.text(j, i, f"{corr.values[i,j]:.2f}", ha="center", va="center", fontsize=7, color=color)
        plt.colorbar(im, label="Correlation")
        ax.set_title(f"Correlation Matrix ({method}, {'all data' if not window else f'last {window} bars'})", color="#e0e0e0")
        plt.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, facecolor="#131722")
        plt.close(fig)
        buf.seek(0)
        if save_path:
            with open(save_path, "wb") as f: f.write(buf.read()); buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")
```


---

## Currency Strength Meter

# Currency Strength Meter

```python
import pandas as pd, numpy as np

MAJOR_PAIRS = {
    "USD": ["EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD", "USDCAD", "NZDUSD"],
    "EUR": ["EURUSD", "EURJPY", "EURGBP", "EURAUD", "EURCHF", "EURCAD", "EURNZD"],
    "GBP": ["GBPUSD", "EURGBP", "GBPJPY", "GBPAUD", "GBPCAD", "GBPCHF", "GBPNZD"],
    "JPY": ["USDJPY", "EURJPY", "GBPJPY", "AUDJPY", "CADJPY", "CHFJPY", "NZDJPY"],
    "AUD": ["AUDUSD", "EURAUD", "GBPAUD", "AUDJPY", "AUDCAD", "AUDCHF", "AUDNZD"],
    "NZD": ["NZDUSD", "EURNZD", "GBPNZD", "NZDJPY", "AUDNZD", "NZDCAD", "NZDCHF"],
    "CAD": ["USDCAD", "EURCAD", "GBPCAD", "CADJPY", "AUDCAD", "NZDCAD", "CADCHF"],
    "CHF": ["USDCHF", "EURCHF", "GBPCHF", "CHFJPY", "AUDCHF", "NZDCHF", "CADCHF"],
}

class CurrencyStrengthMeter:

    @staticmethod
    def compute(pair_returns: dict, period: int = 20) -> dict:
        """
        Compute relative strength for each currency from pair returns.
        pair_returns: {"EURUSD": pd.Series, "GBPUSD": pd.Series, ...}
        """
        strengths = {}
        for currency in ["USD", "EUR", "GBP", "JPY", "AUD", "NZD", "CAD", "CHF"]:
            scores = []
            for pair in MAJOR_PAIRS.get(currency, []):
                if pair not in pair_returns: continue
                ret = pair_returns[pair].tail(period).sum()
                # If currency is base, positive return = currency strong
                if pair.startswith(currency):
                    scores.append(ret)
                else:
                    scores.append(-ret)  # Currency is quote — inverse
            strengths[currency] = round(np.mean(scores) * 100, 3) if scores else 0

        ranked = sorted(strengths.items(), key=lambda x: x[1], reverse=True)
        strongest = ranked[0]
        weakest = ranked[-1]

        return {
            "strengths": dict(ranked),
            "strongest": {"currency": strongest[0], "score": strongest[1]},
            "weakest": {"currency": weakest[0], "score": weakest[1]},
            "best_trade": f"LONG {strongest[0]} / SHORT {weakest[0]} = {strongest[0]}{weakest[0]}",
            "ranking": [r[0] for r in ranked],
            "period": period,
            "spread": round(strongest[1] - weakest[1], 3),
            "note": "Trade strongest vs weakest for maximum directional edge.",
        }

    @staticmethod
    def divergence_alert(current: dict, previous: dict) -> list[str]:
        """Detect currency strength ranking changes — potential trend shifts."""
        alerts = []
        curr_rank = current["ranking"]
        prev_rank = previous["ranking"]
        for currency in curr_rank:
            curr_pos = curr_rank.index(currency)
            prev_pos = prev_rank.index(currency)
            shift = prev_pos - curr_pos
            if abs(shift) >= 3:
                direction = "STRENGTHENING" if shift > 0 else "WEAKENING"
                alerts.append(f"{currency} {direction} rapidly (moved {abs(shift)} ranks)")
        return alerts
```


---

## Cross Timeframe Divergence Scanner

# Cross Timeframe Divergence Scanner

```python
import pandas as pd, numpy as np
class CrossTFDivergenceScanner:
    @staticmethod
    def scan(data_by_tf: dict) -> dict:
        def _rsi(close, p=14):
            d = close.diff()
            g = d.where(d > 0, 0).rolling(p).mean()
            l = (-d.where(d < 0, 0)).rolling(p).mean()
            return (100 - 100 / (1 + g / l.replace(0, np.nan))).iloc[-1]
        tf_signals = {}
        for tf, df in data_by_tf.items():
            if df.empty or len(df) < 50: continue
            rsi = _rsi(df["close"])
            ema50 = df["close"].ewm(span=50).mean().iloc[-1]
            above_ema = df["close"].iloc[-1] > ema50
            tf_signals[tf] = {"rsi": round(rsi, 1), "above_ema50": above_ema,
                             "bias": "BULLISH" if rsi > 50 and above_ema else "BEARISH" if rsi < 50 and not above_ema else "MIXED"}
        biases = [s["bias"] for s in tf_signals.values()]
        all_agree = len(set(biases)) == 1
        conflicts = []
        tfs = list(tf_signals.keys())
        for i in range(len(tfs)):
            for j in range(i+1, len(tfs)):
                if tf_signals[tfs[i]]["bias"] != tf_signals[tfs[j]]["bias"]:
                    conflicts.append(f"{tfs[i]}({tf_signals[tfs[i]]['bias']}) vs {tfs[j]}({tf_signals[tfs[j]]['bias']})")
        return {
            "tf_signals": tf_signals, "all_aligned": all_agree, "conflicts": conflicts,
            "n_conflicts": len(conflicts),
            "action": "CLEAR — all TFs agree" if all_agree else f"CAUTION — {len(conflicts)} TF conflict(s): {', '.join(conflicts[:3])}",
        }
```


---

## Intermarket Divergence Trader

# Intermarket Divergence Trader

```python
import pandas as pd, numpy as np

KNOWN_RELATIONSHIPS = {
    "XAUUSD_DXY": {"correlation": -0.80, "logic": "Gold and USD are inversely correlated"},
    "USDCAD_OIL": {"correlation": -0.70, "logic": "CAD strengthens when oil rises"},
    "USDJPY_SPX": {"correlation": 0.65, "logic": "Risk-on: stocks up, JPY weakens"},
    "EURUSD_DE10Y_US10Y": {"correlation": 0.60, "logic": "EUR follows yield differential"},
    "AUDUSD_COPPER": {"correlation": 0.70, "logic": "AUD follows commodity demand"},
}

class IntermarketDivergenceTrader:
    @staticmethod
    def detect_divergence(series_a: pd.Series, series_b: pd.Series, expected_corr: float,
                           window: int = 30) -> dict:
        norm_a = series_a / series_a.iloc[0]
        norm_b = series_b / series_b.iloc[0]
        recent_corr = norm_a.tail(window).pct_change().corr(norm_b.tail(window).pct_change())
        diverging = abs(recent_corr - expected_corr) > 0.3
        a_move = (norm_a.iloc[-1] / norm_a.iloc[-window] - 1) * 100
        b_move = (norm_b.iloc[-1] / norm_b.iloc[-window] - 1) * 100
        return {
            "expected_correlation": expected_corr,
            "current_correlation": round(recent_corr, 3),
            "diverging": diverging,
            "a_move_pct": round(a_move, 2), "b_move_pct": round(b_move, 2),
            "signal": f"CONVERGENCE TRADE — expect reversion to normal relationship" if diverging else "NO DIVERGENCE",
            "trade": f"If A moved more, fade A. If B moved more, fade B." if diverging else "No trade.",
        }
```


---

## Market Breadth Analyzer

# Market Breadth Analyzer

```python
import pandas as pd, numpy as np

class MarketBreadthAnalyzer:
    @staticmethod
    def scan_breadth(pairs_data: dict, trend_threshold: float = 25) -> dict:
        trending_up = []; trending_down = []; ranging = []
        for sym, df in pairs_data.items():
            if df.empty or len(df) < 50: continue
            close = df["close"]
            ema50 = close.ewm(span=50).mean().iloc[-1]
            plus_dm = df["high"].diff().clip(lower=0).rolling(14).mean()
            minus_dm = (-df["low"].diff()).clip(lower=0).rolling(14).mean()
            atr = (df["high"] - df["low"]).rolling(14).mean()
            dx = abs(plus_dm - minus_dm) / (plus_dm + minus_dm + 1e-10) * 100
            adx = dx.rolling(14).mean().iloc[-1]
            if adx > trend_threshold and close.iloc[-1] > ema50: trending_up.append(sym)
            elif adx > trend_threshold and close.iloc[-1] < ema50: trending_down.append(sym)
            else: ranging.append(sym)
        total = len(trending_up) + len(trending_down) + len(ranging)
        return {
            "trending_up": trending_up, "trending_down": trending_down, "ranging": ranging,
            "breadth_score": round((len(trending_up) - len(trending_down)) / max(total, 1) * 100, 1),
            "pct_trending": round((len(trending_up) + len(trending_down)) / max(total, 1) * 100, 1),
            "market_mode": "TRENDING" if len(trending_up) + len(trending_down) > len(ranging) else "RANGE-BOUND",
            "bias": "RISK-ON" if len(trending_up) > len(trending_down) * 1.5 else "RISK-OFF" if len(trending_down) > len(trending_up) * 1.5 else "MIXED",
        }
```


---

## Carry Trade Calculator

# Carry Trade Calculator

```python
import pandas as pd
import numpy as np

CENTRAL_BANK_RATES = {
    "USD": 5.50, "EUR": 4.50, "GBP": 5.25, "JPY": 0.10,
    "AUD": 4.35, "NZD": 5.50, "CAD": 5.00, "CHF": 1.75,
}  # UPDATE via web_search before using

class CarryTradeCalculator:

    @staticmethod
    def rate_differential(base: str, quote: str) -> dict:
        r_base = CENTRAL_BANK_RATES.get(base, 0)
        r_quote = CENTRAL_BANK_RATES.get(quote, 0)
        diff = r_base - r_quote
        return {
            "pair": f"{base}{quote}",
            "base_rate": r_base, "quote_rate": r_quote,
            "differential": round(diff, 2),
            "carry_direction": "LONG" if diff > 0 else "SHORT" if diff < 0 else "NEUTRAL",
            "annual_carry_pct": round(abs(diff), 2),
            "daily_carry_pct": round(abs(diff) / 365, 4),
        }

    @staticmethod
    def swap_income(lot_size: float, daily_swap_pips: float, hold_days: int) -> dict:
        total_swap = daily_swap_pips * lot_size * 10 * hold_days  # $10 per pip per lot
        return {
            "daily_swap_usd": round(daily_swap_pips * lot_size * 10, 2),
            "total_swap_usd": round(total_swap, 2),
            "hold_days": hold_days,
            "annualized_pct": round(total_swap / (lot_size * 100000) * 365 / max(hold_days, 1) * 100, 2),
        }

    @staticmethod
    def rank_carry_pairs() -> list[dict]:
        """Rank all major pairs by carry attractiveness."""
        pairs = []
        currencies = list(CENTRAL_BANK_RATES.keys())
        for i, base in enumerate(currencies):
            for quote in currencies[i+1:]:
                diff = CarryTradeCalculator.rate_differential(base, quote)
                pairs.append(diff)
                # Reverse pair
                diff_rev = CarryTradeCalculator.rate_differential(quote, base)
                pairs.append(diff_rev)
        return sorted(pairs, key=lambda x: abs(x["differential"]), reverse=True)[:20]

    @staticmethod
    def carry_risk_assessment(pair: str, annual_vol: float, carry_pct: float) -> dict:
        """Carry-to-risk ratio: is the carry worth the volatility?"""
        ratio = carry_pct / max(annual_vol, 0.01)
        return {
            "pair": pair,
            "carry_pct": carry_pct,
            "annual_vol_pct": annual_vol,
            "carry_to_risk": round(ratio, 3),
            "verdict": "ATTRACTIVE" if ratio > 0.5 else "MARGINAL" if ratio > 0.25 else "NOT WORTH IT",
        }
```


---

## Swap Rate Optimizer

# Swap Rate Optimizer

```python
class SwapOptimizer:
    @staticmethod
    def optimize(swap_data: dict, risk_tolerance: float = 0.5) -> dict:
        """swap_data: {pair: {long_swap: X, short_swap: Y}}"""
        positive_swaps = []
        for pair, swaps in swap_data.items():
            if swaps.get("long_swap", 0) > 0:
                positive_swaps.append({"pair": pair, "direction": "long", "daily_swap": swaps["long_swap"]})
            if swaps.get("short_swap", 0) > 0:
                positive_swaps.append({"pair": pair, "direction": "short", "daily_swap": swaps["short_swap"]})
        ranked = sorted(positive_swaps, key=lambda x: x["daily_swap"], reverse=True)
        return {
            "best_swaps": ranked[:10],
            "triple_swap_day": "Wednesday (covers weekend — 3x swap charged)",
            "strategy": "Hold positive-swap positions through Wednesday close for 3x income",
            "warning": "Swap income is secondary to directional P&L. Never hold a losing trade just for swap.",
        }
```


---

## Risk Premia Harvester

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


---

## Multi Pair Basket Trader

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
```

---

## CointegrationEngine & HMMRegimeDetector (Enhancement)

Ctrl click to launch VS Code Native REPL

---

## Related Skills

- [Market Intelligence](../market-intelligence.md)
- [Portfolio Optimization](../portfolio-optimization.md)
- [Forex Trading](../forex-trading.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
