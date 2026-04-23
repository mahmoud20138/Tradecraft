---
name: markets
description: Entry-point live-market scan. Returns current quote, H1/H4 regime, session state, and watch levels for a default watchlist (gold, US30, US500, US100, EURUSD, GBPUSD, BTCUSD, ETHUSD) — or any custom list. Uses the free yfinance path by default, MT5 if available. USE FOR - scan markets, what's moving, market overview, current prices, what's on the watchlist, show me the markets.
user-invocable: true
kind: tool
category: trading/entry
status: active
tags: [entry-point, markets, scan, quotes, overview, watchlist]
related_skills:
  - fetch-quotes
  - pair-scanner-screener
  - market-regime-classifier
  - market-breadth-analyzer
  - analyze
  - recommendations
skill_level: beginner
---

# Markets — Live Watchlist Entry Point

One of the **five entry-point commands** for Tradecraft. Returns a one-screen snapshot of what's happening right now across a default watchlist or any custom list you pass in.

## Invocation

```text
/tradecraft:markets [SYMBOL,SYMBOL,...]

# examples
/tradecraft:markets                                 # default watchlist
/tradecraft:markets XAUUSD,US30,EURUSD
/tradecraft:markets BTCUSD,ETHUSD                   # crypto-only
/tradecraft:markets US30,US500,US100                # indices only
```

## Default Watchlist

`XAUUSD, US30, US500, US100, EURUSD, GBPUSD, BTCUSD, ETHUSD` — covers metals, US indices, FX majors, and the top 2 crypto.

## What Claude Should Do

1. Parse `$ARGUMENTS` as a comma-separated symbol list. Empty → default watchlist.
2. For each symbol, invoke `fetch-quotes`:
   ```shell
   python "${CLAUDE_PLUGIN_ROOT}/scripts/fetch_quotes.py" --symbol <SYM> --timeframe H1 --bars 50 --source auto
   ```
3. Summarize each as one row. Build the table below.
4. Add a bottom-line session + risk calendar note.

## Output Shape

```
Market snapshot — 2026-04-23 14:30 UTC   (source: yfinance free, ~15min indices)

Symbol   Last      Chg%     H4 bias    H1 ATR   Session   Notes
─────────────────────────────────────────────────────────────────
XAUUSD   2345.80   +0.42%   trend-up   8.5      London    clean pullback to OB
US30     42180.0   -0.18%   range      180      NY-pre    equal highs 42200
US500    5485.2    +0.06%   trend-up   14.3     NY-pre    —
US100    19250.0   +0.31%   trend-up   65       NY-pre    AI names leading
EURUSD   1.0862    -0.05%   range      0.00028  London    CPI in 18h
GBPUSD   1.2645    +0.11%   trend-up   0.00035  London    —
BTCUSD   67420.0   +1.82%   trend-up   410      24/7      weekend flow
ETHUSD   3285.0    +1.14%   trend-up   22.5     24/7      —

Top attention: BTCUSD (highest % move), XAUUSD (cleanest setup).
Risk calendar: US CPI 2026-04-24 14:30 UTC. Reduce size on USD pairs.
```

All numbers above are illustrative — actual values come from the live fetch.

## Column Definitions

| Column | Source | Meaning |
|---|---|---|
| Last | `fetch-quotes.latest.bid` or last close on free path | Most recent quote |
| Chg% | `(latest - bars[0].close) / bars[0].close * 100` over last 24h | Day-over-day % change |
| H4 bias | `market-regime-classifier` at H4 | `trend-up` / `trend-down` / `range` |
| H1 ATR | `mean(high - low)` over last 14 H1 bars | Volatility gauge |
| Session | derived from UTC timestamp + symbol class | London / NY-pre / NY-open / Asian / 24/7 |
| Notes | optional flag (liquidity pool near, news gate, correlation anomaly) | Short actionable hint |

## Design Rules

- One row per symbol; no multi-line per entry.
- Round prices to the symbol's standard precision (2 dp for gold, 1 dp for indices, 4-5 dp for FX).
- If any symbol fails to fetch, show `—` in its row and note the source error at the bottom — don't abort.
- Sort by absolute `Chg%` descending so the big movers are on top.
- End with one sentence flagging the top attention symbol and any USD red-folder news in the next 24h.

## Related

- `fetch-quotes` — underlying data fetcher (free yfinance / optional MT5)
- `pair-scanner-screener` — deeper multi-symbol screener with custom filters
- `market-regime-classifier` — upstream trend/range classification
- `market-breadth-analyzer` — SPX internals / sector-level breadth
- `analyze` / `recommendations` — next step: dig into a specific symbol
