---
name: market-data-ingestion
description: >
  Market data ingestion pipelines: OHLCV data fetching from MT5, yfinance, Alpha Vantage,
  data cleaning, normalization, missing bar handling, multi-symbol batch fetching.
  USE FOR: market data, OHLCV, fetch data, download data, historical data, MT5 data,
  yfinance, Alpha Vantage, data pipeline, data ingestion, price data, candle data,
  bar data, multi-symbol, batch fetch, data cleaning, normalize prices.
related_skills:
  - mt5-integration
  - tick-data-storage
  - market-data-ingestion
  - news-intelligence
tags:
  - trading
  - data
  - ingestion
  - mt5
  - ohlcv
  - batch
skill_level: intermediate
kind: reference
category: trading/data
status: active
---
> **Skill:** Market Data Ingestion  |  **Domain:** trading  |  **Category:** data  |  **Level:** intermediate
> **Tags:** `trading`, `data`, `ingestion`, `mt5`, `ohlcv`, `batch`


# Market Data Ingestion

## MT5 Data Fetcher (Primary — your setup)
```python
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

def fetch_mt5(symbol: str, timeframe: int, bars: int = 1000) -> pd.DataFrame:
    """Fetch OHLCV from MT5. Timeframe: mt5.TIMEFRAME_M5, H1, D1, etc."""
    mt5.initialize()
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    mt5.shutdown()
    if rates is None:
        raise ValueError(f"No data for {symbol}")
    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df.set_index("time", inplace=True)
    df.rename(columns={"open":"open","high":"high","low":"low",
                        "close":"close","tick_volume":"volume"}, inplace=True)
    return df[["open","high","low","close","volume"]]

def fetch_multi_mt5(symbols: list, timeframe: int, bars: int = 500) -> dict:
    """Batch fetch multiple symbols from MT5."""
    mt5.initialize()
    data = {}
    for sym in symbols:
        rates = mt5.copy_rates_from_pos(sym, timeframe, 0, bars)
        if rates is not None:
            df = pd.DataFrame(rates)
            df["time"] = pd.to_datetime(df["time"], unit="s")
            df.set_index("time", inplace=True)
            data[sym] = df[["open","high","low","close","tick_volume"]].rename(
                columns={"tick_volume": "volume"})
    mt5.shutdown()
    return data
```

## Your 23 Watched Symbols
```python
WATCHED = [
    "XAUUSDm","XAGUSDm","EURUSDm","GBPUSDm","USDJPYm","AUDUSDm","USDCADm","USDCHFm",
    "BTCUSDm","ETHUSDm","USOILm","USTECm","US500m","US30m",
    "TSLAm","AAPLm","MSFTm","NVDAm","AMZNm","GOOGm","METAm","JPMm","BAm"
]
TIMEFRAMES = {
    "M5": mt5.TIMEFRAME_M5, "M15": mt5.TIMEFRAME_M15,
    "H1": mt5.TIMEFRAME_H1, "H4": mt5.TIMEFRAME_H4, "D1": mt5.TIMEFRAME_D1,
}
```

## Data Cleaning Pipeline
```python
def clean_ohlcv(df: pd.DataFrame, max_gap_bars: int = 5) -> pd.DataFrame:
    """Remove bad bars, fill small gaps, validate OHLC logic."""
    # Drop bars where OHLC relationship is broken
    df = df[(df["high"] >= df["low"]) &
            (df["high"] >= df["open"]) & (df["high"] >= df["close"]) &
            (df["low"]  <= df["open"]) & (df["low"]  <= df["close"])]
    # Drop zero-volume bars (market closed)
    df = df[df["volume"] > 0]
    # Forward-fill small gaps (weekend gaps etc.)
    df = df.resample("1min").asfreq()
    gap_size = df["close"].isna().rolling(max_gap_bars + 1).sum()
    df = df[gap_size <= max_gap_bars].ffill()
    return df.dropna()
```

## yfinance Fallback (for research/backtesting)
```python
import yfinance as yf

def fetch_yf(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """Fetch from Yahoo Finance. interval: 1m,5m,15m,1h,1d,1wk."""
    df = yf.download(ticker, period=period, interval=interval, auto_adjust=True, progress=False)
    df.columns = [c.lower() for c in df.columns]
    return df[["open","high","low","close","volume"]]
```

---

## Related Skills

- [Mt5 Integration](../mt5-integration.md)
- [Tick Data Storage](../tick-data-storage.md)
- [Data Pipelines](../market-data-ingestion.md)
- [News Data Stream](../news-intelligence.md)
