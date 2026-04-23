---
name: pair-analyze
description: Parametric combination command that runs a full multi-skill trading analysis for any symbol. Composes regime classification, structure (ICT/SMC), liquidity, entry refinement, risk sizing, and an execution plan. USE FOR - analyze pair, analyze symbol, pair analysis, full setup, combination analysis, trade plan, what should I trade, run full analysis.
user-invocable: true
kind: workflow
category: trading/orchestration
status: active
tags: [trading, orchestration, combination, workflow, multi-skill]
related_skills:
  - fetch-quotes
  - master-trading-workflow
  - xtrading-analyze
  - market-regime-classifier
  - trading-fundamentals
  - ict-smart-money
  - smc-beginner-pro-guide
  - liquidity-analysis
  - zone-refinement-sniper-entry
  - risk-and-portfolio
  - risk-calendar-trade-filter
  - strategy-selection
skill_level: intermediate
---

# Pair Analyze — Combination Command

Runs a fixed, ordered pipeline of specialist skills against one symbol and returns a single consolidated trade plan. Use this when you want "one command" to cover the full path from regime classification to an actionable entry with stops and targets.

## Invocation

```text
/claude-skills-collection:pair-analyze <SYMBOL> [TIMEFRAME] [MODE]

# Examples
/claude-skills-collection:pair-analyze XAUUSD H1
/claude-skills-collection:pair-analyze US30 H4 conservative
/claude-skills-collection:pair-analyze EURUSD M15 scalp
/claude-skills-collection:pair-analyze BTCUSD D1 swing
```

- `<SYMBOL>` — any broker-recognized symbol (XAUUSD, US30, EURUSD, BTCUSD, ...)
- `[TIMEFRAME]` — M5, M15, H1, H4, D1 (defaults to H1)
- `[MODE]` — one of: `conservative`, `standard` (default), `aggressive`, `scalp`, `swing`

Arguments are exposed to the skill via `$ARGUMENTS`.

## Pipeline (do not skip upstream steps)

| # | Step | Skill invoked | Output expected |
|---|---|---|---|
| 0 | Data feed | `fetch-quotes` | OHLCV bars + latest quote (yfinance free by default, MT5 if available) |
| 1 | Regime classification | `market-regime-classifier` | Trend/range/volatility label; session state |
| 2 | Fundamentals filter | `risk-calendar-trade-filter` + `trading-fundamentals` | High-impact news gate; macro context |
| 3 | Structure | `ict-smart-money` | BOS/CHoCH, order blocks, fair value gaps |
| 4 | Liquidity map | `liquidity-analysis` | Pools, sweeps, equal highs/lows, inducement |
| 5 | Entry refinement | `zone-refinement-sniper-entry` | Precise entry zone inside the POI |
| 6 | Risk & sizing | `risk-and-portfolio` | Position size, SL, TP, R:R, max-daily-loss check |
| 7 | Synthesis | (this skill) | Single consolidated JSON trade plan |

Every step gates the next. If regime fails (e.g., dead range on an M15 scalp mode), stop and report.

## Mode Calibration

| Mode | Per-trade risk | Min R:R | Setup grade | Timeframes |
|---|---:|---:|---|---|
| conservative | 0.5% | 3.0 | A only | H4, D1 |
| standard | 1.0% | 2.0 | A, B | H1, H4 |
| aggressive | 2.0% | 1.5 | A, B, C | M15, H1 |
| scalp | 0.5% | 1.5 | A only | M5, M15 |
| swing | 1.0% | 3.0 | A, B | H4, D1 |

> Symbol-specific wrappers (e.g., `analyze-gold`, `analyze-us30`) may **lower** the per-trade risk for a mode to reflect that symbol's volatility profile. They must never raise it above this parent table.

## Output Contract

Return exactly one JSON block followed by a short human summary:

```json
{
  "symbol": "XAUUSD",
  "timeframe": "H1",
  "mode": "standard",
  "regime": "trend-up | trend-down | range | high-vol",
  "bias": "long | short | flat",
  "setup_grade": "A | B | C",
  "confluence": ["ICT order block", "liquidity sweep", "H4 trend"],
  "entry": 2345.80,
  "stop_loss": 2340.50,
  "take_profit_1": 2356.40,
  "take_profit_2": 2367.00,
  "risk_reward": 2.2,
  "position_size": {"lots": 0.35, "risk_pct": 1.0},
  "invalidation": "Close below 2338.00 on H1",
  "news_gate": {"clear_until": "14:30 UTC", "next_event": "US CPI 14:30 UTC"},
  "confidence": 0.72,
  "notes": "Short summary of why this setup passed every gate"
}
```

Reject and explain (do NOT emit a trade plan) if:
- News gate blocks trading in the next 2 hours
- Regime is incompatible with mode (e.g., range + scalp = skip)
- Position sizing would breach daily loss limit
- Structure and liquidity disagree on direction

## Anti-Patterns

- Running on a symbol the broker does not provide
- Skipping regime because "the setup looks nice"
- Forcing an entry outside the refined zone because the market moved
- Using `aggressive` mode on illiquid sessions (Asian session for US indices, US close for gold majors)
- Stacking multiple open positions without portfolio heat check (see `risk-and-portfolio`)

## Worked Walkthrough: Gold (XAUUSD) H1, standard mode

1. **Regime** — H4 trend up, H1 pullback, London session, ATR(14) = 8.5 points. Trend-up.
2. **News gate** — no red-folder events next 3 hours. Clear.
3. **Structure** — H1 bullish order block at 2340-2343, prior BOS at 2348.
4. **Liquidity** — equal lows at 2341 swept 2 hours ago; next pool above at 2365.
5. **Entry refinement** — 50% of OB refined to 2341.50 entry.
6. **Risk** — 1% of $10k = $100. SL at 2338.00 (3.5 pts). Lot size = 0.28.
7. **Synthesis** — long 2341.50, SL 2338.00, TP1 2348.50 (2R), TP2 2355.00 (3.8R), grade B, confidence 0.68.

## Worked Walkthrough: US30 H4, conservative mode

1. **Regime** — D1 uptrend, H4 consolidation. Range-in-trend.
2. **News gate** — FOMC minutes in 18 hours. Still clear for an H4 setup.
3. **Structure** — H4 CHoCH rejected; bearish order block at 42150-42220.
4. **Liquidity** — equal highs at 42200 untouched (target for sweep, not entry).
5. **Entry refinement** — short at 42180 after liquidity sweep of 42200.
6. **Risk** — 0.5% of $10k = $50. SL above equal highs at 42250 (70 pts). Assuming the common US30 CFD spec of $1 per index-point per 1.0 lot, lots = $50 / (70 × $1) = **0.71** (round DOWN to 0.71 to stay under the risk cap). For a $10-per-point broker spec, the same risk gives 0.07 lots — always check your symbol specification.
7. **Synthesis** — short 42180, SL 42250, TP1 41960 (3.1R), grade A, confidence 0.74.

## Lot-Size Formula (universal)

```text
lots = risk_usd / (sl_points × usd_per_point_per_lot)
```

- Gold (XAUUSD): `usd_per_point_per_lot = $100` where 1 point = $1.00 move × 100 oz contract
- US30: `usd_per_point_per_lot = $1` (most retail CFD) or `$10` (some MT5 cash-CFD specs) — **always verify from the broker's symbol info before sizing**
- Round DOWN to the broker's lot step (typically 0.01) so actual risk stays ≤ the cap

## Validation Test Cases

Use these to self-check the pipeline output before shipping a plan:

- Symbol is normalized (no broker suffix like `XAUUSDm`, `US30.cash`) — if suffix is present, strip it and proceed.
- Every numeric price field has at most 5 significant digits for gold, 1 decimal for indices, 5 for FX majors.
- `risk_reward >= min_RR` from the Mode Calibration table.
- `invalidation` cites a price level and condition, never "if price falls."
- `position_size.lots` respects the broker's min lot (usually 0.01) and step.

## See Also

- `analyze-gold` — pre-configured wrapper for XAUUSD
- `analyze-us30` — pre-configured wrapper for US30
- `master-trading-workflow` — full 18-phase workflow (this skill is its condensed form)
