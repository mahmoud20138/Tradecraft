#!/usr/bin/env python3
"""
fetch_quotes.py - cascading market-data fetcher for Claude Skills Collection.

Priority (when --source auto):
  1. Local MT5 terminal, if the MetaTrader5 library imports AND initialize() succeeds.
  2. yfinance (free, no credentials, no account).

Usage:
  python fetch_quotes.py --symbol XAUUSD --timeframe H1 --bars 200
  python fetch_quotes.py --symbol US30   --timeframe H4 --bars 150 --source free
  python fetch_quotes.py --symbol EURUSD --timeframe M15 --chart out.png
"""

import argparse
import json
import sys
from datetime import datetime, timezone


# canonical name -> (list of MT5 broker variants to try, yfinance ticker)
SYMBOL_MAP = {
    "XAUUSD": (["XAUUSD", "XAUUSDm", "XAUUSD.r", "GOLD"], "GC=F"),
    "US30":   (["US30", "US30.cash", "US30m", "DJ30", "DOWJ30"], "^DJI"),
    "US500":  (["US500", "SPX500", "US500m", "US500.cash"], "^GSPC"),
    "US100":  (["NAS100", "US100", "USTECm", "NAS100.r"], "^NDX"),
    "EURUSD": (["EURUSD", "EURUSDm", "EURUSD.r"], "EURUSD=X"),
    "GBPUSD": (["GBPUSD", "GBPUSDm"], "GBPUSD=X"),
    "USDJPY": (["USDJPY", "USDJPYm"], "USDJPY=X"),
    "AUDUSD": (["AUDUSD", "AUDUSDm"], "AUDUSD=X"),
    "USDCAD": (["USDCAD", "USDCADm"], "USDCAD=X"),
    "USDCHF": (["USDCHF", "USDCHFm"], "USDCHF=X"),
    "BTCUSD": (["BTCUSD", "BTCUSDm", "BTCUSD.cash"], "BTC-USD"),
    "ETHUSD": (["ETHUSD", "ETHUSDm"], "ETH-USD"),
}

# Timeframe -> yfinance interval. H4 has no native yfinance interval; we resample from 1h.
YF_INTERVAL = {
    "M1": "1m", "M5": "5m", "M15": "15m", "M30": "30m",
    "H1": "1h", "H4": "1h",  # H4 is resampled
    "D1": "1d", "W1": "1wk",
}

# yfinance period caps per interval - stay well under Yahoo's documented limits.
YF_PERIOD = {
    "1m": "5d", "5m": "30d", "15m": "30d", "30m": "30d",
    "1h": "60d", "1d": "2y", "1wk": "5y",
}


def normalize_symbol(raw: str) -> str:
    """Strip common broker suffixes and return the canonical symbol."""
    s = raw.upper().strip()
    for suf in (".CASH", ".R", ".ECN", "_STD", ".STD"):
        if s.endswith(suf):
            s = s[: -len(suf)]
    # single trailing 'M' is a common broker marker (e.g. XAUUSDm)
    if s.endswith("M") and s[:-1] in SYMBOL_MAP:
        s = s[:-1]
    aliases = {
        "GOLD": "XAUUSD", "XAU": "XAUUSD",
        "DJ30": "US30", "DOWJ30": "US30", "DOW": "US30", "YM": "US30",
        "SPX": "US500", "SPX500": "US500",
        "NAS100": "US100", "USTEC": "US100", "NDX": "US100",
        "BTC": "BTCUSD", "ETH": "ETHUSD",
    }
    return aliases.get(s, s)


def try_mt5(symbol: str, timeframe: str, bars: int):
    """Attempt MT5. Returns a result dict or None if unavailable."""
    try:
        import MetaTrader5 as mt5  # type: ignore
    except ImportError:
        return None
    if not mt5.initialize():
        return None

    mt5_tf = {
        "M1": mt5.TIMEFRAME_M1, "M5": mt5.TIMEFRAME_M5,
        "M15": mt5.TIMEFRAME_M15, "M30": mt5.TIMEFRAME_M30,
        "H1": mt5.TIMEFRAME_H1, "H4": mt5.TIMEFRAME_H4,
        "D1": mt5.TIMEFRAME_D1, "W1": mt5.TIMEFRAME_W1,
    }
    tf = mt5_tf.get(timeframe.upper())
    if tf is None:
        mt5.shutdown()
        return None

    canonical = normalize_symbol(symbol)
    candidates = list(SYMBOL_MAP.get(canonical, ([symbol], None))[0])
    if symbol not in candidates:
        candidates.insert(0, symbol)

    chosen = None
    for cand in candidates:
        info = mt5.symbol_info(cand)
        if info is None:
            continue
        if not info.visible:
            mt5.symbol_select(cand, True)
        chosen = cand
        break

    if chosen is None:
        mt5.shutdown()
        return None

    rates = mt5.copy_rates_from_pos(chosen, tf, 0, bars)
    tick = mt5.symbol_info_tick(chosen)
    info = mt5.symbol_info(chosen)
    mt5.shutdown()

    if rates is None or len(rates) == 0:
        return None

    out_bars = []
    for r in rates:
        out_bars.append({
            "time": datetime.fromtimestamp(int(r["time"]), tz=timezone.utc).isoformat(),
            "open": float(r["open"]), "high": float(r["high"]),
            "low": float(r["low"]), "close": float(r["close"]),
            "volume": int(r["tick_volume"]),
        })

    latest = None
    if tick is not None:
        latest = {
            "bid": float(tick.bid), "ask": float(tick.ask),
            "spread": float(tick.ask - tick.bid),
            "time": datetime.fromtimestamp(int(tick.time), tz=timezone.utc).isoformat(),
        }

    return {
        "source": "mt5",
        "symbol": canonical,
        "broker_symbol": chosen,
        "timeframe": timeframe.upper(),
        "bars": out_bars,
        "latest": latest,
        "point_value": float(info.point) if info is not None else None,
    }


def try_yfinance(symbol: str, timeframe: str, bars: int):
    """Free path. Raises on fundamental failures; returns None if no data."""
    import yfinance as yf
    import pandas as pd

    canonical = normalize_symbol(symbol)
    yf_ticker = SYMBOL_MAP.get(canonical, (None, None))[1]
    if yf_ticker is None:
        yf_ticker = symbol  # assume user supplied a valid yfinance ticker

    interval = YF_INTERVAL.get(timeframe.upper())
    if interval is None:
        raise ValueError(f"Unsupported timeframe: {timeframe}")
    period = YF_PERIOD[interval]

    df = yf.download(
        yf_ticker, period=period, interval=interval,
        progress=False, auto_adjust=False, prepost=False,
    )
    if df is None or df.empty:
        return None

    # Flatten multi-index columns from yfinance 1.x
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    # H4 = resample hourly bars into 4-hour bars
    if timeframe.upper() == "H4" and interval == "1h":
        df = df.resample("4h", origin="start_day").agg({
            "Open": "first", "High": "max", "Low": "min",
            "Close": "last", "Volume": "sum",
        }).dropna()

    df = df.tail(bars)
    out_bars = []
    for idx, row in df.iterrows():
        t = idx.tz_localize("UTC") if idx.tzinfo is None else idx.tz_convert("UTC")
        vol = row["Volume"]
        out_bars.append({
            "time": t.isoformat(),
            "open": float(row["Open"]), "high": float(row["High"]),
            "low": float(row["Low"]), "close": float(row["Close"]),
            "volume": int(vol) if not pd.isna(vol) else 0,
        })

    if not out_bars:
        return None

    last = out_bars[-1]
    return {
        "source": "yfinance",
        "symbol": canonical,
        "broker_symbol": yf_ticker,
        "timeframe": timeframe.upper(),
        "bars": out_bars,
        "latest": {
            "bid": last["close"], "ask": last["close"],
            "spread": 0.0, "time": last["time"],
        },
        "note": (
            "Yahoo Finance data. Indices and futures are often delayed ~15 min. "
            "bid/ask are both the last close (no L1 depth). For broker-exact "
            "pricing, run with --source mt5 on a machine with MT5 logged in."
        ),
    }


def maybe_render_chart(result: dict, chart_path: str) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        result["chart_error"] = "matplotlib not installed; pip install matplotlib"
        return
    closes = [b["close"] for b in result["bars"]]
    highs = [b["high"] for b in result["bars"]]
    lows = [b["low"] for b in result["bars"]]
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(range(len(closes)), closes, linewidth=1.2, label="close")
    ax.fill_between(range(len(closes)), lows, highs, alpha=0.15, label="range")
    ax.set_title(f"{result['symbol']} {result['timeframe']}  -  source: {result['source']}")
    ax.set_xlabel("bar")
    ax.set_ylabel("price")
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left")
    plt.tight_layout()
    plt.savefig(chart_path, dpi=110)
    plt.close()
    result["chart_path"] = chart_path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--symbol", required=True, help="e.g. XAUUSD, US30, EURUSD, BTCUSD")
    ap.add_argument("--timeframe", default="H1",
                    choices=list(YF_INTERVAL.keys()),
                    help="M1, M5, M15, M30, H1, H4, D1, W1")
    ap.add_argument("--bars", type=int, default=200, help="Number of bars to return")
    ap.add_argument("--source", default="auto",
                    choices=["auto", "free", "mt5"],
                    help="auto=MT5 if available else free; free=yfinance only; mt5=MT5 only")
    ap.add_argument("--chart", help="Optional PNG path to render")
    args = ap.parse_args()

    result = None

    if args.source in ("auto", "mt5"):
        result = try_mt5(args.symbol, args.timeframe, args.bars)
        if result is None and args.source == "mt5":
            print(json.dumps({
                "error": "MT5 unavailable (no terminal running, not logged in, or lib missing)",
                "requested": args.symbol,
            }))
            sys.exit(2)

    if result is None:
        try:
            result = try_yfinance(args.symbol, args.timeframe, args.bars)
        except Exception as exc:
            print(json.dumps({
                "error": f"yfinance failed: {exc}", "requested": args.symbol,
            }))
            sys.exit(3)

    if result is None:
        print(json.dumps({
            "error": "no data from any source", "requested": args.symbol,
        }))
        sys.exit(4)

    if args.chart:
        maybe_render_chart(result, args.chart)

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
