---
name: analyze-gold
description: Pre-configured combination command for gold (XAUUSD) analysis. Runs the full pair-analyze pipeline tuned for gold's volatility profile, session behavior, and dollar sensitivity. USE FOR - analyze gold, analyze XAUUSD, gold setup, trade gold, gold analysis, XAUUSD plan.
user-invocable: true
kind: workflow
category: trading/orchestration
status: active
tags: [trading, orchestration, combination, gold, xauusd, commodities]
related_skills:
  - pair-analyze
  - master-trading-workflow
  - xtrading-analyze
  - ict-smart-money
  - liquidity-analysis
  - risk-and-portfolio
  - risk-calendar-trade-filter
  - gold-orb-ea
skill_level: intermediate
---

# Analyze Gold — Combination Command

Pre-configured wrapper around `pair-analyze` for **XAUUSD** with gold-specific calibration. Pick this when the user says "analyze gold" or "gold setup" so defaults match how gold actually trades.

## Invocation

```text
/claude-skills-collection:analyze-gold [TIMEFRAME] [MODE]

# Examples
/claude-skills-collection:analyze-gold              # defaults: H1, standard
/claude-skills-collection:analyze-gold H4 conservative
/claude-skills-collection:analyze-gold M15 scalp
/claude-skills-collection:analyze-gold D1 swing
```

Arguments are exposed via `$ARGUMENTS`. Symbol is locked to `XAUUSD`.

## What This Wrapper Does

1. Binds symbol = `XAUUSD` (also accepts broker variants: `XAUUSDm`, `GOLD`, `XAU/USD` — normalize before dispatch).
2. Applies **gold-specific overrides** (see below).
3. Delegates to the `pair-analyze` pipeline.
4. Returns the same JSON output contract as `pair-analyze`, plus a `gold_context` block.

## Gold-Specific Calibration

| Aspect | Override vs. generic `pair-analyze` |
|---|---|
| Pip / point | 0.01 USD per unit — price quoted to 2 decimals |
| Typical spread | 0.15 – 0.40 on ECN; 0.25 – 0.60 on standard |
| Active sessions | London open → US close (08:00 – 21:00 UTC) |
| Dead zone | Asian session outside the Tokyo/London overlap (~06:00 – 09:00 UTC) |
| Volatility reference | H1 ATR(14) typically 3–12 pts; >20 = elevated |
| SL minimum | Max(structure-based, 1.0 × H1 ATR, 2.5 pts) — gold wicks hunt tight stops |
| High-impact drivers | FOMC, NFP, CPI, PPI, DXY moves, real yields, geopolitical risk |
| News gate buffer | 30 min before / 60 min after red-folder USD events |
| Correlation to monitor | DXY (inverse), US10Y real yield (inverse), SPX (weak positive in risk-on) |

## Mode Defaults Adjusted for Gold

| Mode | Per-trade risk | Min R:R | Notes |
|---|---:|---:|---|
| conservative | 0.5% | 3.0 | H4/D1 only; avoid during NY lunch |
| standard | 1.0% | 2.0 | H1/H4; skip the first 15 min after London open |
| aggressive | 1.5% | 1.5 | H1 only; never during CPI/FOMC week |
| scalp | 0.5% | 1.5 | M5/M15; London and NY overlap only |
| swing | 1.0% | 3.0 | H4/D1; align with weekly bias |

## Worked Example: XAUUSD H1 standard

Assume current price = 2345.00, London session, no red news next 2h.

1. **Regime** — H4 trend-up (HH/HL intact), H1 pullback into demand.
2. **News gate** — clear until US PMI at 15:00 UTC.
3. **Structure** — H1 bullish order block 2340–2343, BOS at 2348 confirms bullish intent.
4. **Liquidity** — equal lows at 2341 swept during Asian session (1-candle wick); next upside pool 2365.
5. **Entry refinement** — 50% of OB → entry 2341.50; rejection candle required.
6. **Risk** — SL 2338.00 (3.5 pts, above 1×ATR minimum); $10k account × 1% = $100; lots = 0.28.
7. **Plan** — long 2341.50, SL 2338.00, TP1 2348.50 (2R), TP2 2355.00 (3.8R), grade B, confidence 0.68.

```json
{
  "symbol": "XAUUSD",
  "timeframe": "H1",
  "mode": "standard",
  "regime": "trend-up-h4-pullback-h1",
  "bias": "long",
  "setup_grade": "B",
  "confluence": ["H4 trend-up", "H1 bullish order block", "Asian sweep of equal lows"],
  "entry": 2341.50,
  "stop_loss": 2338.00,
  "take_profit_1": 2348.50,
  "take_profit_2": 2355.00,
  "risk_reward": 2.0,
  "position_size": {"lots": 0.28, "risk_pct": 1.0, "usd_per_point_per_lot": 100.0},
  "invalidation": "H1 close below 2338.00",
  "news_gate": {"clear_until": "15:00 UTC", "next_event": "US PMI"},
  "gold_context": {
    "atr_h1": 8.5,
    "dxy_bias": "weakening",
    "session": "London",
    "spread": 0.25
  },
  "confidence": 0.68,
  "notes": "Long at 50% retrace of H1 OB after liquidity sweep; exit TP1 before US PMI"
}
```

## Skip Conditions (gold-specific)

Do NOT emit a trade plan when:
- DXY is breaking a major level in the same direction as a gold short/long signal (decorrelation risk)
- Within 30 min before or 60 min after CPI, NFP, FOMC, or Fed Chair testimony
- Spread > 1.0 at the candidate entry time (suggests thin liquidity — common during rollover 22:00 UTC)
- H1 ATR > 20 (regime = high-vol; switch to larger SL or stand aside)

## Validation Checklist

- [ ] Symbol normalized to `XAUUSD`
- [ ] SL ≥ max(structure, 1×ATR, 2.5 pts)
- [ ] News gate checked for USD red-folder events
- [ ] DXY correlation not opposing the signal
- [ ] Session is London or NY (or London-NY overlap for scalp)

## See Also

- `pair-analyze` — the underlying generic combination
- `analyze-us30` — sister wrapper for the Dow index
- `gold-orb-ea` — opening-range breakout strategy specific to gold
- `xtrading-analyze` — full multi-agent scan (broader scope than this wrapper)
