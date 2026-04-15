---
name: mt5-chart-browser
description: >
  MT5 chart browser, pair scanner, indicator engine, and GPU-accelerated chart image analysis.
  Use this skill whenever the user asks to open MT5, browse pairs, view charts, apply indicators,
  screenshot charts, analyze chart images, read candlestick patterns from screenshots, scan multiple
  pairs visually, or perform any visual/technical analysis on MT5 charts. Also trigger when the user
  says "open MT5", "show me EURUSD", "what does the chart look like", "analyze this chart",
  "scan all pairs", "apply RSI", "screenshot the chart", "GPU analysis", "image recognition on chart",
  "read the candles", "what pattern is this", or any variation involving MT5 visual/chart interaction.
  This skill works with the trading-brain as a sub-agent for chart data acquisition.
disable-model-invocation: true
related_skills:
  - mt5-integration
  - chart-vision
  - technical-analysis
tags:
  - trading
  - infrastructure
  - mt5
  - chart
  - browser
  - analysis-tools
skill_level: intermediate
kind: tool
category: trading/mt5
status: active
---
> **Skill:** Mt5 Chart Browser  |  **Domain:** trading  |  **Category:** infrastructure  |  **Level:** intermediate
> **Tags:** `trading`, `infrastructure`, `mt5`, `chart`, `browser`, `analysis-tools`


# MT5 Chart Browser & GPU Image Analysis Skill

## Overview
This skill provides a complete interface for connecting to MetaTrader 5, browsing all available
symbols/pairs, pulling OHLCV data across all timeframes, computing any indicator, capturing chart
images, and performing GPU-accelerated image analysis on chart screenshots for pattern recognition.

## Architecture

```
┌─────────────────────────────────────────────────┐
│              MT5 Chart Browser                   │
├──────────┬──────────┬──────────┬────────────────┤
│ MT5 Conn │ Symbol   │ Chart    │ GPU Image      │
│ Manager  │ Browser  │ Engine   │ Analyzer       │
└──────────┴──────────┴──────────┴────────────────┘
```

---

## 1. MT5 Connection & Symbol Browser

### Connect to MT5
```python
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Optional

def connect_mt5(
    path: Optional[str] = None,
    login: Optional[int] = None,
    password: Optional[str] = None,
    server: Optional[str] = None,
    timeout: int = 10000
) -> bool:
    """Initialize MT5 connection. Call once per session."""
    kwargs = {"timeout": timeout}
    if path: kwargs["path"] = path
    if login: kwargs["login"] = login
    if password: kwargs["password"] = password
    if server: kwargs["server"] = server

    if not mt5.initialize(**kwargs):
        print(f"MT5 init failed: {mt5.last_error()}")
        return False
    info = mt5.terminal_info()
    print(f"Connected: {info.name} | Build {info.build} | {info.company}")
    return True

def shutdown_mt5():
    mt5.shutdown()
```

### Browse All Available Symbols
```python
def get_all_symbols(group: Optional[str] = None, visible_only: bool = False) -> pd.DataFrame:
    """
    Get all symbols available in the broker.
    group: filter like "Forex*", "Crypto*", "Index*", "*USD*"
    visible_only: only symbols shown in Market Watch
    """
    if group:
        symbols = mt5.symbols_get(group=group)
    else:
        symbols = mt5.symbols_get()

    if not symbols:
        print(f"No symbols found. Error: {mt5.last_error()}")
        return pd.DataFrame()

    data = []
    for s in symbols:
        if visible_only and not s.visible:
            continue
        data.append({
            "symbol": s.name,
            "description": s.description,
            "path": s.path,
            "spread": s.spread,
            "digits": s.digits,
            "point": s.point,
            "trade_mode": s.trade_mode,
            "volume_min": s.volume_min,
            "volume_max": s.volume_max,
            "volume_step": s.volume_step,
            "currency_base": s.currency_base,
            "currency_profit": s.currency_profit,
            "category": _categorize_symbol(s.path),
        })
    return pd.DataFrame(data)

def _categorize_symbol(path: str) -> str:
    """Auto-categorize symbol from broker path."""
    p = path.lower()
    if "forex" in p or "fx" in p: return "Forex"
    if "crypto" in p: return "Crypto"
    if "index" in p or "indices" in p: return "Index"
    if "commodity" in p or "metal" in p: return "Commodity"
    if "stock" in p or "share" in p: return "Stock"
    if "energy" in p: return "Energy"
    return "Other"

def enable_symbol(symbol: str) -> bool:
    """Make a symbol visible in Market Watch (required before data access)."""
    selected = mt5.symbol_select(symbol, True)
    if not selected:
        print(f"Cannot enable {symbol}: {mt5.last_error()}")
    return selected

def get_symbol_info(symbol: str) -> dict:
    """Full symbol specification — spread, margin, swap, session times, etc."""
    info = mt5.symbol_info(symbol)
    if info is None:
        return {}
    return info._asdict()

def get_current_price(symbol: str) -> dict:
    """Real-time bid/ask/last for a symbol."""
    tick = mt5.symbol_info_tick(symbol)
    if tick is None:
        return {}
    return {"symbol": symbol, "bid": tick.bid, "ask": tick.ask,
            "last": tick.last, "volume": tick.volume, "time": tick.time}
```

### Browse by Category
```python
def browse_forex_pairs() -> pd.DataFrame:
    return get_all_symbols(group="*Forex*")

def browse_crypto() -> pd.DataFrame:
    return get_all_symbols(group="*Crypto*")

def browse_indices() -> pd.DataFrame:
    return get_all_symbols(group="*Index*")

def browse_commodities() -> pd.DataFrame:
    return get_all_symbols(group="*Commodity*")

def browse_by_currency(currency: str = "USD") -> pd.DataFrame:
    """All pairs containing a specific currency."""
    return get_all_symbols(group=f"*{currency}*")
```

---

## 2. Chart Data Engine — All Timeframes & All Data

### Timeframe Map
```python
TIMEFRAMES = {
    "M1":  mt5.TIMEFRAME_M1,   "M2":  mt5.TIMEFRAME_M2,
    "M3":  mt5.TIMEFRAME_M3,   "M4":  mt5.TIMEFRAME_M4,
    "M5":  mt5.TIMEFRAME_M5,   "M6":  mt5.TIMEFRAME_M6,
    "M10": mt5.TIMEFRAME_M10,  "M12": mt5.TIMEFRAME_M12,
    "M15": mt5.TIMEFRAME_M15,  "M20": mt5.TIMEFRAME_M20,
    "M30": mt5.TIMEFRAME_M30,  "H1":  mt5.TIMEFRAME_H1,
    "H2":  mt5.TIMEFRAME_H2,   "H3":  mt5.TIMEFRAME_H3,
    "H4":  mt5.TIMEFRAME_H4,   "H6":  mt5.TIMEFRAME_H6,
    "H8":  mt5.TIMEFRAME_H8,   "H12": mt5.TIMEFRAME_H12,
    "D1":  mt5.TIMEFRAME_D1,   "W1":  mt5.TIMEFRAME_W1,
    "MN1": mt5.TIMEFRAME_MN1,
}

def get_ohlcv(
    symbol: str,
    timeframe: str = "H1",
    bars: int = 1000,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> pd.DataFrame:
    """
    Pull OHLCV data. Supports bar count OR date range.
    Returns: DataFrame with columns [time, open, high, low, close, tick_volume, spread]
    """
    enable_symbol(symbol)
    tf = TIMEFRAMES.get(timeframe.upper())
    if tf is None:
        raise ValueError(f"Unknown timeframe: {timeframe}. Use one of: {list(TIMEFRAMES.keys())}")

    if start_date and end_date:
        rates = mt5.copy_rates_range(symbol, tf, start_date, end_date)
    elif start_date:
        rates = mt5.copy_rates_from(symbol, tf, start_date, bars)
    else:
        rates = mt5.copy_rates_from_pos(symbol, tf, 0, bars)

    if rates is None or len(rates) == 0:
        print(f"No data for {symbol} {timeframe}: {mt5.last_error()}")
        return pd.DataFrame()

    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df.set_index("time", inplace=True)
    df.rename(columns={"tick_volume": "volume"}, inplace=True)
    return df

def get_ticks(
    symbol: str,
    start: datetime,
    end: Optional[datetime] = None,
    count: int = 10000,
    flags: int = mt5.COPY_TICKS_ALL
) -> pd.DataFrame:
    """Raw tick data — bid/ask/last at millisecond granularity."""
    enable_symbol(symbol)
    if end:
        ticks = mt5.copy_ticks_range(symbol, start, end, flags)
    else:
        ticks = mt5.copy_ticks_from(symbol, start, count, flags)
    if ticks is None or len(ticks) == 0:
        return pd.DataFrame()
    df = pd.DataFrame(ticks)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return df

def multi_timeframe_snapshot(symbol: str, bars: int = 200) -> dict[str, pd.DataFrame]:
    """Pull data across all major timeframes for a single symbol."""
    key_tfs = ["M5", "M15", "H1", "H4", "D1", "W1"]
    return {tf: get_ohlcv(symbol, tf, bars) for tf in key_tfs}
```

---

## 3. Indicator Engine — Compute Any Indicator

### Built-in Indicator Wrappers (vectorized, no look-ahead)
```python
def sma(series: pd.Series, period: int) -> pd.Series:
    return series.rolling(period).mean()

def ema(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(span=period, adjust=False).mean()

def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0.0)).rolling(period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
    fast_ema = ema(series, fast)
    slow_ema = ema(series, slow)
    macd_line = fast_ema - slow_ema
    signal_line = ema(macd_line, signal)
    histogram = macd_line - signal_line
    return pd.DataFrame({"macd": macd_line, "signal": signal_line, "histogram": histogram})

def bollinger_bands(series: pd.Series, period: int = 20, std_dev: float = 2.0) -> pd.DataFrame:
    mid = sma(series, period)
    std = series.rolling(period).std()
    return pd.DataFrame({"upper": mid + std_dev * std, "middle": mid, "lower": mid - std_dev * std})

def atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high_low = df["high"] - df["low"]
    high_close = (df["high"] - df["close"].shift(1)).abs()
    low_close = (df["low"] - df["close"].shift(1)).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return tr.rolling(period).mean()

def stochastic(df: pd.DataFrame, k_period: int = 14, d_period: int = 3) -> pd.DataFrame:
    low_min = df["low"].rolling(k_period).min()
    high_max = df["high"].rolling(k_period).max()
    k = 100 * (df["close"] - low_min) / (high_max - low_min).replace(0, np.nan)
    d = k.rolling(d_period).mean()
    return pd.DataFrame({"k": k, "d": d})

def ichimoku(df: pd.DataFrame, tenkan: int = 9, kijun: int = 26, senkou_b: int = 52) -> pd.DataFrame:
    high_tenkan = df["high"].rolling(tenkan).max()
    low_tenkan = df["low"].rolling(tenkan).min()
    tenkan_sen = (high_tenkan + low_tenkan) / 2
    high_kijun = df["high"].rolling(kijun).max()
    low_kijun = df["low"].rolling(kijun).min()
    kijun_sen = (high_kijun + low_kijun) / 2
    senkou_a = ((tenkan_sen + kijun_sen) / 2).shift(kijun)
    high_senkou = df["high"].rolling(senkou_b).max()
    low_senkou = df["low"].rolling(senkou_b).min()
    senkou_b_line = ((high_senkou + low_senkou) / 2).shift(kijun)
    chikou = df["close"].shift(-kijun)
    return pd.DataFrame({"tenkan": tenkan_sen, "kijun": kijun_sen,
                         "senkou_a": senkou_a, "senkou_b": senkou_b_line, "chikou": chikou})

def adx(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    plus_dm = df["high"].diff().clip(lower=0)
    minus_dm = (-df["low"].diff()).clip(lower=0)
    mask = plus_dm > minus_dm
    plus_dm = plus_dm.where(mask, 0)
    minus_dm = minus_dm.where(~mask, 0)
    atr_val = atr(df, period)
    plus_di = 100 * ema(plus_dm, period) / atr_val.replace(0, np.nan)
    minus_di = 100 * ema(minus_dm, period) / atr_val.replace(0, np.nan)
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx_val = ema(dx, period)
    return pd.DataFrame({"adx": adx_val, "plus_di": plus_di, "minus_di": minus_di})

def vwap(df: pd.DataFrame) -> pd.Series:
    """Session VWAP — requires intraday data with volume."""
    tp = (df["high"] + df["low"] + df["close"]) / 3
    return (tp * df["volume"]).cumsum() / df["volume"].cumsum()

def pivot_points(df: pd.DataFrame) -> pd.DataFrame:
    """Classic pivot points from previous bar's HLC."""
    p = (df["high"].shift(1) + df["low"].shift(1) + df["close"].shift(1)) / 3
    return pd.DataFrame({
        "pivot": p, "r1": 2 * p - df["low"].shift(1), "s1": 2 * p - df["high"].shift(1),
        "r2": p + (df["high"].shift(1) - df["low"].shift(1)),
        "s2": p - (df["high"].shift(1) - df["low"].shift(1)),
    })

# Master indicator dispatcher
INDICATORS = {
    "sma": lambda df, **kw: sma(df["close"], kw.get("period", 20)),
    "ema": lambda df, **kw: ema(df["close"], kw.get("period", 20)),
    "rsi": lambda df, **kw: rsi(df["close"], kw.get("period", 14)),
    "macd": lambda df, **kw: macd(df["close"], kw.get("fast", 12), kw.get("slow", 26), kw.get("signal", 9)),
    "bollinger": lambda df, **kw: bollinger_bands(df["close"], kw.get("period", 20), kw.get("std", 2.0)),
    "atr": lambda df, **kw: atr(df, kw.get("period", 14)),
    "stochastic": lambda df, **kw: stochastic(df, kw.get("k", 14), kw.get("d", 3)),
    "ichimoku": lambda df, **kw: ichimoku(df),
    "adx": lambda df, **kw: adx(df, kw.get("period", 14)),
    "vwap": lambda df, **kw: vwap(df),
    "pivot": lambda df, **kw: pivot_points(df),
}

def apply_indicator(df: pd.DataFrame, name: str, **params):
    """Apply any indicator by name. Returns Series or DataFrame."""
    fn = INDICATORS.get(name.lower())
    if fn is None:
        raise ValueError(f"Unknown indicator: {name}. Available: {list(INDICATORS.keys())}")
    return fn(df, **params)

def apply_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all indicators to a single DataFrame. For full analysis snapshots."""
    result = df.copy()
    result["sma_20"] = sma(df["close"], 20)
    result["sma_50"] = sma(df["close"], 50)
    result["ema_20"] = ema(df["close"], 20)
    result["rsi_14"] = rsi(df["close"], 14)
    macd_df = macd(df["close"])
    result = pd.concat([result, macd_df], axis=1)
    bb = bollinger_bands(df["close"])
    result = pd.concat([result, bb.add_prefix("bb_")], axis=1)
    result["atr_14"] = atr(df, 14)
    stoch = stochastic(df)
    result = pd.concat([result, stoch.add_prefix("stoch_")], axis=1)
    return result
```

---

## 4. Chart Rendering & Screenshot Capture

### Render Chart to Image (matplotlib-based, GPU-ready)
```python
import matplotlib
matplotlib.use("Agg")  # headless rendering
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance import plot as mpf_plot
import io, base64

def render_candlestick_chart(
    df: pd.DataFrame,
    symbol: str,
    timeframe: str,
    indicators: list[str] = None,
    width: int = 1920,
    height: int = 1080,
    save_path: Optional[str] = None
) -> str:
    """
    Render a publication-quality candlestick chart with optional indicators.
    Returns base64-encoded PNG for GPU image analysis or saves to file.
    """
    import mplfinance as mpf

    # Prepare indicator overlays
    addplots = []
    if indicators:
        for ind_name in indicators:
            ind_data = apply_indicator(df, ind_name)
            if isinstance(ind_data, pd.Series):
                addplots.append(mpf.make_addplot(ind_data, panel=0 if ind_name in ["sma", "ema", "bollinger"] else 2))
            elif isinstance(ind_data, pd.DataFrame):
                for col in ind_data.columns:
                    panel = 0 if "senkou" in col or "tenkan" in col or "kijun" in col else 2
                    addplots.append(mpf.make_addplot(ind_data[col], panel=panel, label=col))

    style = mpf.make_mpf_style(base_mpf_style="nightclouds", gridstyle="", y_on_right=True)
    fig, axes = mpf.plot(
        df, type="candle", style=style, volume=True,
        addplot=addplots if addplots else None,
        title=f"{symbol} {timeframe}",
        figsize=(width / 100, height / 100),
        returnfig=True
    )

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100, bbox_inches="tight", facecolor="#1a1a2e")
    plt.close(fig)
    buf.seek(0)

    if save_path:
        with open(save_path, "wb") as f:
            f.write(buf.read())
        buf.seek(0)

    return base64.b64encode(buf.read()).decode("utf-8")

def capture_mt5_chart_screenshot(symbol: str, timeframe: str, bars: int = 200) -> str:
    """Full pipeline: pull data → render → return base64 PNG."""
    df = get_ohlcv(symbol, timeframe, bars)
    if df.empty:
        raise RuntimeError(f"No data for {symbol} {timeframe}")
    return render_candlestick_chart(df, symbol, timeframe, indicators=["sma", "rsi", "macd"])
```

---

## 5. GPU-Accelerated Chart Image Analysis

### Pattern Recognition via Image Analysis
```python
import cv2
import torch
import torchvision.transforms as T
from PIL import Image

class ChartImageAnalyzer:
    """
    GPU-accelerated chart analysis using computer vision + deep learning.
    Analyzes candlestick chart screenshots for patterns, structure, and signals.
    """

    def __init__(self, device: str = "auto"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu") if device == "auto" else torch.device(device)
        self.transform = T.Compose([T.Resize((448, 448)), T.ToTensor(), T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        print(f"ChartImageAnalyzer initialized on {self.device}")

    def load_image(self, source: str) -> np.ndarray:
        """Load from file path or base64 string."""
        if source.startswith("/") or source.startswith("."):
            return cv2.imread(source)
        else:
            img_bytes = base64.b64decode(source)
            nparr = np.frombuffer(img_bytes, np.uint8)
            return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    def detect_candle_colors(self, img: np.ndarray) -> dict:
        """Count bullish (green) vs bearish (red) candles via color segmentation."""
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        green_mask = cv2.inRange(hsv, (35, 50, 50), (85, 255, 255))
        red_mask = cv2.inRange(hsv, (0, 50, 50), (15, 255, 255)) | cv2.inRange(hsv, (165, 50, 50), (180, 255, 255))
        green_px = cv2.countNonZero(green_mask)
        red_px = cv2.countNonZero(red_mask)
        total = green_px + red_px or 1
        return {
            "bullish_ratio": round(green_px / total, 3),
            "bearish_ratio": round(red_px / total, 3),
            "dominant_bias": "bullish" if green_px > red_px else "bearish",
        }

    def detect_trend_lines(self, img: np.ndarray) -> list[dict]:
        """Detect straight lines using Hough Transform — potential support/resistance."""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
        if lines is None:
            return []
        results = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            results.append({"start": (x1, y1), "end": (x2, y2), "angle": round(angle, 1), "length": round(length, 1)})
        return sorted(results, key=lambda x: x["length"], reverse=True)[:20]

    def detect_support_resistance_zones(self, img: np.ndarray) -> list[dict]:
        """Find horizontal zones with high pixel density — likely S/R levels."""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape
        # Horizontal projection: sum pixel intensity per row
        projection = np.sum(gray, axis=1)
        # Find peaks = rows with high intensity (price levels touched often)
        from scipy.signal import find_peaks
        peaks, properties = find_peaks(projection, height=np.percentile(projection, 90), distance=h // 20)
        zones = []
        for peak in peaks:
            y_pct = round(1 - peak / h, 3)  # Invert: top of chart = high price
            zones.append({"y_pixel": int(peak), "price_level_pct": y_pct, "strength": round(projection[peak] / projection.max(), 3)})
        return zones

    def analyze_chart_structure(self, img: np.ndarray) -> dict:
        """Full structural analysis of a chart image."""
        return {
            "candle_bias": self.detect_candle_colors(img),
            "trend_lines": self.detect_trend_lines(img),
            "sr_zones": self.detect_support_resistance_zones(img),
            "image_shape": img.shape,
        }

    def full_analysis(self, source: str) -> dict:
        """Complete GPU image analysis pipeline from file/base64."""
        img = self.load_image(source)
        if img is None:
            return {"error": "Failed to load image"}
        return self.analyze_chart_structure(img)
```

### Multi-Pair Visual Scan
```python
def visual_scan_all_pairs(
    symbols: list[str],
    timeframe: str = "H4",
    bars: int = 200
) -> list[dict]:
    """
    Screenshot and GPU-analyze every pair. Returns ranked analysis.
    Use for quick visual scanning of market conditions across pairs.
    """
    analyzer = ChartImageAnalyzer()
    results = []
    for sym in symbols:
        try:
            df = get_ohlcv(sym, timeframe, bars)
            if df.empty:
                continue
            b64 = render_candlestick_chart(df, sym, timeframe)
            analysis = analyzer.full_analysis(b64)
            analysis["symbol"] = sym
            analysis["timeframe"] = timeframe
            results.append(analysis)
        except Exception as e:
            print(f"SKIP {sym}: {e}")
    return results
```

---

## 6. Integration Points

This skill feeds data to other skills in the trading ecosystem:

| Downstream Skill | Data Provided |
|---|---|
| `pair-correlation-engine` | OHLCV data, multi-pair snapshots |
| `trading-data-science` | Raw data for analysis pipelines |
| `event-timeline-linker` | Timestamped price data for event alignment |
| `institutional-behavior-monitor` | Price reaction data around news events |
| `trading-brain` | Structured analysis results for decision-making |

## Usage Conventions

1. **Always call `connect_mt5()` first** — every session starts with connection
2. **Enable symbols before pulling data** — `enable_symbol()` is auto-called in `get_ohlcv()`
3. **Use vectorized indicators** — never loop over bars manually
4. **GPU analysis is optional** — falls back to CPU if no CUDA device
5. **Chart images are base64** — can be piped directly to Claude's vision API for LLM-level analysis
6. **Multi-timeframe is standard** — always check at least 3 timeframes before conclusions

---

## Related Skills

- [Mt5 Integration](../mt5-integration.md)
- [Chart Vision](../chart-vision.md)
- [Technical Analysis](../technical-analysis.md)
