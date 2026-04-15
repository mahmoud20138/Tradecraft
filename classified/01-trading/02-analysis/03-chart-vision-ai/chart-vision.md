---
name: chart-vision
description: >
  Complete chart vision pipeline — render charts, preprocess images, detect candlestick
  patterns, detect classical chart patterns, detect trendlines and S/R levels, and annotate
  results back onto charts. Use this skill for ANY chart image task: "render a chart",
  "create chart image", "screenshot chart", "generate candlestick chart", "draw chart with
  indicators", "produce chart for analysis", "make a chart PNG", "render OHLCV", "chart to
  image", "visual chart output", "clean chart image", "preprocess chart", "enhance chart",
  "remove grid from chart", "prepare chart for analysis", "normalize chart image",
  "read candles from image", "what candlestick pattern is this", "analyze candles in
  screenshot", "identify candle pattern from chart", "visual candle detection", "find
  patterns in chart image", "what chart pattern is this", "pattern recognition from
  screenshot", "detect triangle from chart image", "visual pattern scan", "AI chart pattern
  detection", "head and shoulders from image", "detect double top from screenshot",
  "identify engulfing candle", "doji", "hammer", "pin bar", "morning star", "evening star",
  "three soldiers", "ascending triangle", "descending triangle", "flag", "wedge",
  "cup and handle", "find support resistance from image", "detect trendlines", "draw
  trendlines on chart", "key levels from screenshot", "S/R detection", "find channels",
  "horizontal levels", "automatic trendline detection", "annotate chart", "draw levels on
  chart", "mark patterns on image", "highlight trade setup", "overlay analysis on
  screenshot", "visual markup", "label candles on chart", "draw buy/sell on chart",
  "head and shoulders", "double top", "double bottom", "triangle", "channel", "pennant",
  "pattern scan", "chart patterns", "find patterns", "bull flag", "bear flag",
  "AI signal aggregation", "combine strategy signals", "weighted vote", "meta-model",
  "trading data science", "feature engineering", "ML model", "anomaly detection",
  "mplfinance chart", "publication-quality chart PNG", "base64 chart output",
  "indicator overlay", "multi-signal AI analysis", or any
  chart rendering, image preprocessing, visual pattern detection, chart annotation,
  or AI signal aggregation task.
  Full pipeline: render → preprocess → analyze → annotate → aggregate.
kind: reference
category: trading/analysis
status: active
tags: [analysis, chart, grid-trading, trading, vision]
related_skills: [analyze]
---

# Chart Vision — Complete Pipeline

## Overview
Unified skill covering the entire chart image pipeline in one place:

1. **Rendering** — produce high-quality candlestick chart images from OHLCV data
2. **Preprocessing** — clean, denoise, and normalize raw chart screenshots
3. **Candlestick Vision** — detect single and multi-candle patterns from images
4. **Chart Pattern Vision** — detect H&S, triangles, wedges, double tops from images
5. **Pattern Scanner** — algorithmic classical pattern detection from price data
6. **Trendline & S/R Vision** — detect trendlines, channels, S/R zones from images
7. **Annotation Overlay** — draw all analysis results back onto the chart image

## Pipeline Order
```
chart-vision-renderer       → render OHLCV to PNG
chart-image-preprocessor    → clean, denoise, extract ROI
chart-pattern-vision        → detect candle + chart patterns from image
trendline-sr-vision         → detect S/R and trendlines from image
chart-pattern-scanner       → detect patterns from price data (no image needed)
chart-annotation-overlay    → draw everything back onto chart  ← final step
```

## Reference Files

| File | Contents |
|------|----------|
| `references/rendering.md` | Chart renderer: mplfinance + matplotlib, indicators, dark/light themes |
| `references/preprocessing.md` | Image preprocessing: denoise, ROI extract, grid removal, contrast, color analysis |
| `references/pattern-vision.md` | CV candlestick detection + classical chart pattern detection from images |
| `references/trendline-sr.md` | Hough transforms, LSD, horizontal projection, S/R clustering, channels |
| `references/scanner-and-annotation.md` | Price-data pattern scanner (swing-based) + annotation overlay drawing engine |

## Stack
- **mplfinance** — candlestick rendering
- **matplotlib 3.10** — rendering engine
- **OpenCV 4.13** — all CV operations (Hough, LSD, morphology, edge detection, drawing)
- **scikit-image 0.26** — region props, probabilistic Hough, restoration
- **scipy 1.17** — peak finding, signal processing, clustering
- **Pillow 12.1** — text rendering, image post-processing
- **numpy 2.4** — array operations
- **sklearn** — RandomForest, GradientBoosting, calibration, TimeSeriesSplit (AI signal aggregation & ML)
- **statsmodels** — ADF, Granger causality (statistical analysis)

## Quick Usage Examples

### Render a chart from OHLCV data

```python
import mplfinance as mpf
import pandas as pd

df = pd.read_csv("ohlcv.csv", index_col="date", parse_dates=True)
mpf.plot(df, type="candle", style="charles", volume=True,
         mav=(20, 50), savefig="chart.png", figsize=(14, 8))
```

### Preprocess a chart screenshot

```python
import cv2
import numpy as np

img = cv2.imread("screenshot.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Remove grid lines
denoised = cv2.fastNlMeansDenoising(gray, h=15)
# Enhance edges for pattern detection
edges = cv2.Canny(denoised, 50, 150)
# Extract ROI (crop to chart area)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest)
chart_roi = img[y:y+h, x:x+w]
```

### Detect support/resistance from image

```python
from scipy.signal import find_peaks

# Project pixel intensities horizontally to find price levels
projection = np.mean(gray, axis=1)
peaks, props = find_peaks(-projection, distance=20, prominence=10)
sr_levels = peaks  # pixel y-coordinates of S/R lines

# Draw detected levels
for level in sr_levels:
    cv2.line(img, (0, level), (img.shape[1], level), (0, 255, 0), 1)
```

### Annotate chart with analysis

```python
from PIL import Image, ImageDraw, ImageFont

img = Image.open("chart.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 14)

# Draw buy signal
draw.text((entry_x, entry_y - 20), "BUY", fill="green", font=font)
draw.rectangle([sl_x-2, sl_y-2, sl_x+2, sl_y+2], fill="red")
draw.text((sl_x + 5, sl_y), f"SL: {sl_price:.5f}", fill="red", font=font)
draw.text((tp_x + 5, tp_y), f"TP: {tp_price:.5f}", fill="green", font=font)
img.save("annotated_chart.png")
```
