---
name: analyze-us30
description: Pre-configured combination command for US30 (Dow Jones Industrial Average CFD) analysis. Runs the full pair-analyze pipeline tuned for US30's session-driven flow, earnings sensitivity, and Fed-rate reactivity. USE FOR - analyze US30, analyze Dow, analyze Dow Jones, US30 setup, trade US30, DJ30 plan.
user-invocable: true
kind: workflow
category: trading/orchestration
status: active
tags: [trading, orchestration, combination, us30, dow, indices]
related_skills:
  - pair-analyze
  - master-trading-workflow
  - xtrading-analyze
  - ict-smart-money
  - liquidity-analysis
  - risk-and-portfolio
  - risk-calendar-trade-filter
  - market-breadth-analyzer
skill_level: intermediate
---

# Analyze US30 — Combination Command

Pre-configured wrapper around `pair-analyze` for **US30** (Dow Jones Industrial Average CFD) with index-specific calibration. Pick this when the user says "analyze US30" or "Dow setup" so defaults match how the index actually trades.

## Invocation

```text
/claude-skills-collection:analyze-us30 [TIMEFRAME] [MODE]

# Examples
/claude-skills-collection:analyze-us30              # defaults: H1, standard
/claude-skills-collection:analyze-us30 H4 conservative
/claude-skills-collection:analyze-us30 M15 scalp
/claude-skills-collection:analyze-us30 D1 swing
```

Arguments are exposed via `$ARGUMENTS`. Symbol is locked to `US30`.

## What This Wrapper Does

1. Binds symbol = `US30` (also accepts broker variants: `US30.cash`, `DJ30`, `YM`, `DOW` — normalize before dispatch).
2. Applies **US30-specific overrides** (see below).
3. Delegates to the `pair-analyze` pipeline.
4. Returns the same JSON output contract as `pair-analyze`, plus a `us30_context` block.

## US30-Specific Calibration

| Aspect | Override vs. generic `pair-analyze` |
|---|---|
| Pip / point | 1.0 USD per unit — price quoted to 1 decimal |
| Typical spread | 1.0 – 3.0 during cash session; 4.0 – 10.0 overnight |
| Active sessions | US pre-market and cash session (12:00 – 21:00 UTC) |
| Dead zone | Asian session — wide spreads, low volume, gap risk |
| Volatility reference | H1 ATR(14) typically 60–160 pts; >250 = elevated |
| SL minimum | Max(structure-based, 0.8 × H1 ATR, 40 pts) |
| High-impact drivers | FOMC, CPI, NFP, ISM, mega-cap earnings (AAPL/MSFT/GS/UNH), yields |
| News gate buffer | 15 min before / 45 min after red-folder USD events |
| Correlation to monitor | SPX (high positive), VIX (inverse), USTs (context), DXY (weak inverse) |
| Gap behavior | Weekend and overnight gaps are common — open positions past cash close at risk |

## Mode Defaults Adjusted for US30

| Mode | Per-trade risk | Min R:R | Notes |
|---|---:|---:|---|
| conservative | 0.5% | 3.0 | H4/D1 only; avoid FOMC week and earnings peaks |
| standard | 1.0% | 2.0 | H1/H4; cash session only |
| aggressive | 1.5% | 1.5 | H1/M15; first 90 min of US open, or post-FOMC trend |
| scalp | 0.5% | 1.5 | M5/M15; cash session only — never overnight |
| swing | 1.0% | 3.0 | H4/D1; align with SPX and breadth trend |

## Worked Example: US30 H4 conservative

Assume current price = 42180, D1 uptrend, H4 consolidation, FOMC minutes in ~18h.

1. **Regime** — D1 trend-up, H4 range-in-trend (42060 – 42230).
2. **News gate** — clear for an H4 setup; flag FOMC minutes for position management.
3. **Structure** — H4 CHoCH rejected at range top; bearish order block 42150 – 42220.
4. **Liquidity** — equal highs at 42200 untouched → likely sweep target, not entry.
5. **Entry refinement** — short 42180 after liquidity sweep of 42200 with M15 rejection.
6. **Risk** — SL 42250 (70 pts, above ATR and equal-highs sweep); $10k × 0.5% = $50. Using the common US30 CFD spec of **$1 per index-point per 1.0 lot**: lots = $50 / (70 × $1) = **0.71**. If your broker uses a $10-per-point spec, the same risk gives 0.07 lots — verify from your broker's symbol info before sizing.
7. **Plan** — short 42180, SL 42250, TP1 41960 (3.1R, range bottom + buffer), grade A, confidence 0.74.

```json
{
  "symbol": "US30",
  "timeframe": "H4",
  "mode": "conservative",
  "regime": "trend-up-h4-range",
  "bias": "short",
  "setup_grade": "A",
  "confluence": ["H4 CHoCH", "bearish order block", "equal-highs sweep", "SPX neutral"],
  "entry": 42180.0,
  "stop_loss": 42250.0,
  "take_profit_1": 41960.0,
  "risk_reward": 3.1,
  "position_size": {"lots": 0.71, "risk_pct": 0.5, "usd_per_point_per_lot": 1.0},
  "invalidation": "H4 close above 42250",
  "news_gate": {"clear_until": "19:00 UTC next day", "next_event": "FOMC Minutes"},
  "us30_context": {
    "atr_h4": 180.0,
    "spx_bias": "neutral",
    "vix": 14.8,
    "session": "NY afternoon",
    "spread": 1.5
  },
  "confidence": 0.74,
  "notes": "Short on sweep-and-reject of equal highs; manage into FOMC minutes next day"
}
```

## Skip Conditions (US30-specific)

Do NOT emit a trade plan when:
- Outside US cash session and mode is not `swing` (overnight spreads + gap risk)
- Within 15 min before or 45 min after CPI, NFP, FOMC, ISM, or a Dow-30 mega-cap earnings print
- VIX > 28 AND mode is not `swing` (regime = panic, intraday mean reversion is unreliable)
- SPX breaking major level in the opposite direction (breadth divergence)
- Spread > 5.0 at entry time

## Validation Checklist

- [ ] Symbol normalized to `US30`
- [ ] SL ≥ max(structure, 0.8×ATR, 40 pts)
- [ ] News gate checked for USD red-folder events AND DJIA earnings
- [ ] SPX correlation not opposing the signal
- [ ] Current session is US cash (or swing mode with explicit overnight plan)

## Position Management Notes

US30 gaps weekends and frequently gaps overnight on earnings. If a trade must be held past cash close:
- Reduce size by 50%
- Move SL to breakeven only if structure supports it (do not tighten mechanically)
- Log the gap risk in the trade journal (see `trading-fundamentals` journaling section)

## See Also

- `pair-analyze` — the underlying generic combination
- `analyze-gold` — sister wrapper for XAUUSD
- `market-breadth-analyzer` — use alongside for SPX / sector internals
- `xtrading-analyze` — full multi-agent scan (broader scope than this wrapper)
