---
name: recommendations
description: Entry-point ranked-setup feed. Runs the full pair-analyze pipeline against a watchlist and returns the top N highest-grade trade setups right now, sorted by confidence × R:R, with one-line rationale and a copy-pasteable trade plan. USE FOR - what should I trade, recommend trades, best setups, top picks, ranked opportunities, where's the edge.
user-invocable: true
kind: workflow
category: trading/entry
status: active
tags: [entry-point, recommendations, ranking, setups, ai-signal, top-picks]
related_skills:
  - pair-analyze
  - analyze-gold
  - analyze-us30
  - ai-signal-aggregator
  - market-regime-classifier
  - risk-and-portfolio
  - risk-calendar-trade-filter
  - markets
  - analyze
skill_level: intermediate
---

# Recommendations — Ranked Setups Entry Point

One of the **five entry-point commands** for Tradecraft. Returns the top trade setups across a watchlist right now, ranked by quality. Skip the noise — get the picks.

## Invocation

```text
/tradecraft:recommendations [SYMBOL,SYMBOL,...] [N]

# examples
/tradecraft:recommendations                              # default watchlist, top 3
/tradecraft:recommendations XAUUSD,US30,EURUSD           # those 3 only
/tradecraft:recommendations BTCUSD,ETHUSD,SOLUSD 5       # crypto top 5
/tradecraft:recommendations all 10                       # default watchlist, top 10
```

- `[SYMBOL,...]` — comma-separated, default watchlist if omitted (same as `markets`)
- `[N]` — number of recommendations to return; default `3`

## Default Watchlist

`XAUUSD, US30, US500, US100, EURUSD, GBPUSD, BTCUSD, ETHUSD`

## What Claude Should Do

1. Parse args. Empty symbols → default watchlist.
2. For each symbol in parallel: run `pair-analyze <SYM> H1 standard` (or the symbol-specific wrapper if available, e.g. `analyze-gold`, `analyze-us30`).
3. Drop any setup that is `bias: flat` or fails its news gate.
4. Score remaining setups: `score = setup_grade × confidence × min(risk_reward / 2.0, 1.5)` where `setup_grade` maps `A=1.0, B=0.7, C=0.4`.
5. Sort descending; take top `N`.
6. Optional: cross-check with `ai-signal-aggregator` if active for an ML confidence overlay.
7. Render as the table below.

## Output Shape

```
Top 3 setups — 2026-04-23 14:30 UTC   (default watchlist, mode: standard)

# Rank   Symbol    Side    Entry      SL         TP1        R:R    Grade   Conf   Why
─────────────────────────────────────────────────────────────────────────────────────
1        XAUUSD    long    2341.50    2338.00    2348.50    2.0    A       0.74   H4 trend-up + H1 OB + Asian sweep
2        US30      short   42180      42250      41960      3.1    A       0.68   H4 CHoCH + equal-highs sweep target
3        BTCUSD    long    67200      66400      69000      2.3    B       0.61   D1 breakout retest + funding flat

Skipped: EURUSD (CPI 18h), US500 (range, no edge), US100 (regime + CPI overlap)
Risk note: 2 USD-quote setups; if both fill, total USD exposure = 1.5%.
```

All numbers above are illustrative — actual values come from the underlying pair-analyze runs.

## Output Contract Per Row

| Column | Source | Notes |
|---|---|---|
| # | rank | 1 = best |
| Symbol | input | normalized |
| Side | `pair-analyze.bias` | `long` / `short` only — flat is filtered out |
| Entry | `pair-analyze.entry` | broker-precision rounded |
| SL | `pair-analyze.stop_loss` | broker-precision rounded |
| TP1 | `pair-analyze.take_profit_1` | first target |
| R:R | `pair-analyze.risk_reward` | TP1-based |
| Grade | `pair-analyze.setup_grade` | A / B / C |
| Conf | `pair-analyze.confidence` | 0.0 - 1.0 |
| Why | `pair-analyze.confluence` first 2-3 items joined | one short clause |

End the table with a single line listing skipped symbols + reasons, and a portfolio-heat note if multiple setups share an exposure (USD, EUR, risk-on basket).

## Skip Conditions

Skip a symbol entirely (don't show as a setup) if any of these fire:
- `pair-analyze.bias == "flat"`
- News gate blocks within next 2 hours
- Spread > 2× typical for that symbol
- Regime is `high-vol` AND mode is not `swing`
- Symbol fetch failed entirely (note at bottom, don't include in ranking)

## Design Rules

- Cap at user-requested N or 10, whichever is smaller. Asking for "top 100" is meaningless when most filter out.
- Never invent a setup — if `pair-analyze` returns no plan for a symbol, it doesn't appear in the ranking.
- The `Why` column is a short clause from `confluence`, not a paragraph.
- End with one portfolio-heat note (e.g., "2 USD-quote setups, total USD exposure = X%").
- If zero setups pass all gates, return: "No A/B-grade setups right now. Next opportunity window: <time of next non-news session>."

## Related

- `pair-analyze` — underlying per-symbol pipeline this fans out across the watchlist
- `analyze-gold` / `analyze-us30` — symbol-specific wrappers used when applicable
- `ai-signal-aggregator` — optional ML confidence overlay
- `risk-and-portfolio` — portfolio-heat math
- `markets` — sister entry point for raw quotes (no setup ranking)
- `analyze` — sister entry point for deep-dive on one symbol
