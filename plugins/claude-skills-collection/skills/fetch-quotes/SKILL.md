---
name: fetch-quotes
description: Cascading market-data fetcher. Prefers yfinance (free, no credentials) and falls back to a local MT5 terminal when available for broker-exact pricing. Returns OHLCV bars plus a latest quote as JSON, optionally with a PNG chart. USE FOR - get quotes, get data, fetch bars, live data, market data, price data, get chart, quotes for XAUUSD, quotes for US30, any symbol data.
user-invocable: true
kind: tool
category: trading/data
status: active
tags: [trading, data, free, yfinance, mt5, fetch, quotes, bars]
related_skills:
  - pair-analyze
  - analyze-gold
  - analyze-us30
  - mt5-integration
  - mt5-chart-browser
  - xtrading-analyze
skill_level: beginner
---

# Fetch Quotes — Free-First Data Source

Primary data source: **yfinance** (free, no account, no API key). Automatic upgrade to **local MT5 terminal** when it is running and logged in. Pick this when you need OHLCV bars or a current quote for any symbol and don't want to maintain credentials.

## Invocation

```text
/claude-skills-collection:fetch-quotes <SYMBOL> [TIMEFRAME] [BARS] [SOURCE] [CHART]

# Examples
/claude-skills-collection:fetch-quotes XAUUSD                  # defaults: H1, 200 bars, auto
/claude-skills-collection:fetch-quotes US30 H4
/claude-skills-collection:fetch-quotes EURUSD M15 100 free
/claude-skills-collection:fetch-quotes BTCUSD D1 300 auto chart
```

- `<SYMBOL>` — e.g. `XAUUSD`, `US30`, `EURUSD`, `BTCUSD`. Broker suffixes (`XAUUSDm`, `US30.cash`) are normalized automatically.
- `[TIMEFRAME]` — `M1 M5 M15 M30 H1 H4 D1 W1`. Default `H1`. (`H4` via `--source free` is resampled from yfinance 1-hour bars.)
- `[BARS]` — number of bars to return. Default `200`.
- `[SOURCE]` — `auto` (default), `free` (yfinance only), `mt5` (MT5 only, fails if unavailable).
- `[CHART]` — pass `chart` or a PNG path to render a line chart.

## What Claude Should Execute

First-time setup (free path only):

```shell
pip install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"
```

Optional, Windows only, for broker-exact pricing:

```shell
pip install MetaTrader5
```

Then, per invocation, shell out to the fetcher:

```shell
python "${CLAUDE_PLUGIN_ROOT}/scripts/fetch_quotes.py" \
  --symbol <SYMBOL> \
  --timeframe <TIMEFRAME> \
  --bars <BARS> \
  --source <SOURCE> \
  [--chart <path.png>]
```

The script writes JSON to stdout. Parse it; if `source == "yfinance"`, remind the user that prices may be ~15 min delayed for indices and futures.

## Output Contract

```json
{
  "source": "yfinance | mt5",
  "symbol": "XAUUSD",
  "broker_symbol": "XAUUSDm | GC=F",
  "timeframe": "H1",
  "bars": [
    {"time": "2026-04-23T10:00:00+00:00",
     "open": 2340.1, "high": 2343.5, "low": 2339.8, "close": 2342.7,
     "volume": 1234}
  ],
  "latest": {
    "bid": 2342.70, "ask": 2342.85, "spread": 0.15,
    "time": "2026-04-23T10:58:12+00:00"
  },
  "point_value": 0.01,
  "note": "Only present on yfinance path - explains delay and missing L1 depth.",
  "chart_path": "out.png"
}
```

- `source` tells you which feed answered. Always check it before reporting a price.
- `broker_symbol` is the actual ticker the feed used after symbol normalization — helpful when a user's broker uses a suffix.
- `spread = 0` on yfinance because Yahoo gives no L1 depth. Don't treat that as real spread.
- Times are ISO-8601 UTC (`+00:00`).

## Source Cascade

| `--source` | Behavior | When to use |
|---|---|---|
| `auto` (default) | MT5 if `MetaTrader5` imports AND `initialize()` succeeds; otherwise yfinance | Any machine — best data available |
| `free` | yfinance only — never touches MT5 | Zero credentials, portable, demo/CI |
| `mt5` | MT5 only — fails fast if terminal isn't up | You know MT5 is running and want broker-exact prices; CI gate against silent fallback |

## Symbol Mapping (canonical → yfinance ticker, MT5 variants tried)

| Canonical | yfinance | MT5 variants attempted |
|---|---|---|
| XAUUSD | `GC=F` | XAUUSD, XAUUSDm, XAUUSD.r, GOLD |
| US30 | `^DJI` | US30, US30.cash, US30m, DJ30, DOWJ30 |
| US500 | `^GSPC` | US500, SPX500, US500m, US500.cash |
| US100 | `^NDX` | NAS100, US100, USTECm, NAS100.r |
| EURUSD | `EURUSD=X` | EURUSD, EURUSDm, EURUSD.r |
| GBPUSD | `GBPUSD=X` | GBPUSD, GBPUSDm |
| USDJPY | `USDJPY=X` | USDJPY, USDJPYm |
| BTCUSD | `BTC-USD` | BTCUSD, BTCUSDm, BTCUSD.cash |
| ETHUSD | `ETH-USD` | ETHUSD, ETHUSDm |
| Unmapped | (pass-through) | (pass-through) |

Unmapped symbols are forwarded verbatim to both feeds — handy for less common instruments, but verify the ticker on the vendor side.

## Known Limits of the Free Path

- **Delay** — Yahoo indices and futures are typically ~15 min delayed. FX and crypto quotes are close to real-time.
- **No L1 depth** — `bid == ask == close`. Don't trust `spread` from this source.
- **Gold quoted as `GC=F`** (COMEX continuous front-month futures). For FX-spot XAUUSD use `--source mt5` or override the mapping.
- **H4 is resampled** from 1-hour bars when on yfinance — calendar-aligned 4h buckets, not the broker's session-aligned H4 candles.
- **Rate limits** — Yahoo throttles heavy polling. For monitoring loops, cache at the bar-close boundary.

## Skip Conditions

- `--source mt5` but no terminal running → returns error JSON with exit code 2. Do not fall through silently; surface the error so the user can decide.
- Symbol not resolvable on either side → exit code 4. Check the spelling and whether the broker quote differs.

## Worked Examples

### Gold, auto source, default bars

```shell
python "${CLAUDE_PLUGIN_ROOT}/scripts/fetch_quotes.py" --symbol XAUUSD --timeframe H1 --bars 50
# -> source: "mt5" if terminal is up, otherwise "yfinance" (GC=F)
```

### US30, free only

```shell
python "${CLAUDE_PLUGIN_ROOT}/scripts/fetch_quotes.py" --symbol US30 --timeframe H4 --bars 120 --source free
# -> source: "yfinance", broker_symbol: "^DJI"
```

### Gold with chart

```shell
python "${CLAUDE_PLUGIN_ROOT}/scripts/fetch_quotes.py" --symbol XAUUSD --timeframe H1 --bars 200 --chart /tmp/gold-h1.png
# -> writes /tmp/gold-h1.png; response JSON carries "chart_path"
```

Claude can then read the PNG with its vision capability for visual pattern analysis (same pattern used by `mt5-chart-browser`).

## See Also

- `pair-analyze` — the generic combination that calls `fetch-quotes` as Step 0
- `analyze-gold` / `analyze-us30` — pre-configured wrappers that go through this skill for data
- `mt5-integration` — deeper MT5 integration guide (broker-exact only)
- `mt5-chart-browser` — read PNG charts once they are generated
- `xtrading-analyze` — full multi-agent scan (assumes a more elaborate local pipeline)
