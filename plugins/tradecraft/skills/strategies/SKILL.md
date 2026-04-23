---
name: strategies
description: Entry-point strategy selector. Lists the available trading strategies with a one-line when-to-use for each, plus a deep-dive drill-down by name. Routes to the right specialist skill (ICT/SMC, breakout, scalping, swing, trend-following, mean-reversion). USE FOR - which strategy, what strategies, strategy selector, strategy list, how should I trade, pick a strategy, ICT or SMC, breakout or trend.
user-invocable: true
kind: reference
category: trading/entry
status: active
tags: [entry-point, strategies, selector, guide, routing]
related_skills:
  - strategy-selection
  - ict-smart-money
  - smc-beginner-pro-guide
  - zone-refinement-sniper-entry
  - market-regime-classifier
  - trading-fundamentals
  - risk-and-portfolio
  - master-trading-workflow
  - analyze
  - recommendations
skill_level: beginner
---

# Strategies — Strategy Selector Entry Point

One of the **five entry-point commands** for Tradecraft. Starts here when the question is "which strategy should I use?" rather than "analyze this symbol." Tells you the right approach for the current regime + asset class, then drills into the specialist skill.

## Invocation

```text
/tradecraft:strategies [NAME] [SYMBOL]

# examples
/tradecraft:strategies                        # overview + selector
/tradecraft:strategies ict                    # deep-dive on ICT Smart Money
/tradecraft:strategies smc XAUUSD             # SMC guide tuned for gold
/tradecraft:strategies breakout US30          # breakout guide for US30
/tradecraft:strategies scalp EURUSD           # scalping guide for EURUSD
```

- `[NAME]` — optional. One of: `ict`, `smc`, `breakout`, `scalp`, `swing`, `trend`, `mean-reversion`. Omit to see the full selector.
- `[SYMBOL]` — optional. When present, tailor the answer to that symbol.

## What Claude Should Do

### No args — show the selector table

```
Tradecraft strategies — pick one based on regime + style

Strategy                  Best regime      Timeframe   Specialist skill
──────────────────────────────────────────────────────────────────────────
ICT Smart Money           trending+pullback  M15-H4    /tradecraft:ict-smart-money
SMC (beginner-friendly)   trending           M15-H4    /tradecraft:smc-beginner-pro-guide
Order-block entry         trending pullback  M15-H1    /tradecraft:zone-refinement-sniper-entry
Breakout (opening range)  range breaking     M5-H1     /tradecraft:gold-orb-ea
Momentum breakout         trending           H1-D1     /tradecraft:dan-zanger-breakout-strategy
Scalping                  high-liquidity     M1-M15    /tradecraft:xtrading-analyze
Swing                     D1 trend           H4-D1     /tradecraft:master-trading-workflow
Regime classifier (pre)   any                any       /tradecraft:market-regime-classifier

Not sure which? Run /tradecraft:strategies <YOUR_SYMBOL> and we'll recommend.
```

### With a NAME arg — deep-dive

Invoke the specialist skill directly and summarize its core rules in 5-8 bullets (entry, invalidation, target logic, when NOT to use, position sizing note).

Example for `ict`:
```
ICT Smart Money (deep-dive)

Specialist: /tradecraft:ict-smart-money
When to use: clean H4 trend with a pullback to a displacement zone on H1/M15
Structure concepts: BOS, CHoCH, order block, fair value gap, liquidity pool
Entry: 50% retrace of the order block AFTER a liquidity sweep in the opposite direction
Invalidation: H1 close beyond the order block
Targets: next internal liquidity, then external
When NOT to use: ranging / news-driven / low-liquidity sessions
Next step: /tradecraft:pair-analyze <YOUR_SYMBOL> H1 standard
```

### With NAME + SYMBOL args

Same as above, but (a) call `market-regime-classifier` for that symbol to confirm the strategy fits the current regime, (b) show a concrete entry zone if the regime matches, (c) pipe the user to `/tradecraft:pair-analyze <SYMBOL> <TIMEFRAME>` as the next action.

## Strategy Name Aliases

| Input | Routes to |
|---|---|
| `ict`, `smart-money`, `smartmoney` | `ict-smart-money` |
| `smc` | `smc-beginner-pro-guide` |
| `breakout`, `brk` | `dan-zanger-breakout-strategy` |
| `orb`, `opening-range` | `gold-orb-ea` |
| `scalp`, `scalping` | `xtrading-analyze` with M5/M15 mode |
| `swing` | `master-trading-workflow` with `swing` mode |
| `trend`, `trend-following` | `strategy-selection` filtered to trend strategies |
| `mean-reversion`, `mr` | `strategy-selection` filtered to mean-reversion |

## Design Rules

- Never list more than 8 strategies in the selector. Keep it one-screen.
- Every row has a working `/tradecraft:` command the user can copy-paste.
- Deep-dive sections max 8 bullets — not a textbook, a reference card.
- If the user asks about a strategy not in the alias table, route to `/tradecraft:search <name>` for a broader match instead of inventing one.
- Always end with a concrete next step (usually `/tradecraft:pair-analyze <SYMBOL>` or `/tradecraft:recommendations`).

## Related

- `strategy-selection` — underlying strategy-picker logic this wraps
- `ict-smart-money`, `smc-beginner-pro-guide`, `zone-refinement-sniper-entry`, `dan-zanger-breakout-strategy`, `gold-orb-ea`, `xtrading-analyze`, `master-trading-workflow` — specialist strategy skills this routes to
- `market-regime-classifier` — upstream regime check that gates strategy suitability
- `analyze` / `recommendations` / `markets` / `search` — other four entry points
