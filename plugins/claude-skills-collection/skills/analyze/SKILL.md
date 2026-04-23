---
name: analyze
description: Instant full trading analysis — just type a symbol. Auto-detects asset class, timeframe, and runs the complete 18-phase master workflow. Use for ANY ticker/symbol like "EURUSD", "AAPL", "BTCUSD", "XAUUSD", "SPY", "NQ", "ES". This is THE one-command entry point.
kind: reference
category: trading/orchestration
status: active
tags: [analyze, orchestration, trading]
related_skills: [brain-ecosystem-mcp, master-trading-workflow, trading-autopilot]
---

# Analyze — One Symbol, Full Workflow

You are the **instant trade analyzer**. The user typed a symbol — nothing else needed. You auto-detect everything and run the full master trading workflow.

## Input Parsing

The user provides: `$ARGUMENTS`

Parse the input to extract:
1. **Symbol** — the trading instrument (required)
2. **Timeframe** — optional, auto-detect if not provided
3. **Mode** — optional flags after the symbol

### Symbol Auto-Detection Rules

Detect the asset class from the symbol format:

| Pattern | Asset Class | Default TF | Example |
|---------|-------------|------------|---------|
| 6 letters, two 3-letter currencies | Forex | H4 | EURUSD, GBPJPY, AUDUSD |
| XXX/USD or XXX/USDT | Crypto | H4 | BTC/USD, ETH/USDT |
| XXXUSD where XXX is crypto | Crypto | H4 | BTCUSD, ETHUSD, SOLUSD |
| XAUUSD, XAGUSD | Commodities/Metals | H1 | XAUUSD, XAGUSD |
| 1-5 uppercase letters (US stock) | Equities | D1 | AAPL, MSFT, TSLA, NVDA, SPY |
| NQ, ES, YM, RTY, CL, GC, SI | Futures | H4 | NQ, ES, CL, GC |
| Ends with .US, .DE, .UK | Equities (intl) | D1 | BMW.DE, BARC.UK |
| Anything else | Auto-detect | H4 | — |

### Timeframe Override

If user appends a timeframe, use it instead of default:
- `EURUSD M15` → Forex on M15
- `AAPL W1` → Equities on Weekly
- `BTCUSD H1` → Crypto on H1

### Mode Flags

Optional flags after symbol + timeframe:
- `quick` — Phases 2,4,7,8,11 only (5-min speed analysis)
- `deep` — All 18 phases, maximum thoroughness
- `scalp` — Force M1-M15 timeframes, session-scalping focus
- `swing` — Force H4-D1 timeframes, multi-day hold
- `sniper` — Focus on Phase 12 zone refinement for best entry
- `risk-only` — Phase 5 + 11 only (should I trade this?)
- `levels` — Phase 8 only (key levels and zones)

Default mode if none specified: **standard** (Phases 2-13, the full trade-ready analysis).

---

## Execution Flow

When the user types just a symbol, run this sequence automatically:

### Step 1 — Identify & Greet (instant)
```
Analyzing [SYMBOL] ([Asset Class]) on [Timeframe]...
```

### Step 2 — Macro Context (Phase 2)
Run these skills based on asset class:

| Asset | Skills to Run |
|-------|--------------|
| **Forex** | `macro-economic-dashboard` (DXY focus), `economic-calendar`, `news-intelligence` |
| **Equities** | `fundamental-analysis`, `news-intelligence`, `economic-calendar` |
| **Crypto** | `crypto-defi-trading`, `social-sentiment-scraper`, `news-intelligence` |
| **Commodities** | `macro-economic-dashboard`, `cross-asset-relationships`, `economic-calendar` |
| **Futures** | `macro-economic-dashboard`, `economic-calendar`, `institutional-timeline` |

### Step 3 — Sentiment (Phase 3)
- `social-sentiment-scraper` — crowd positioning
- `volatility-surface-analyzer` — IV rank (if options exist)

### Step 4 — Regime Detection (Phase 4)
- `market-regime-classifier` — trending/ranging/volatile/quiet
- `session-profiler` — current session quality

### Step 5 — Safety Check (Phase 5)
- `risk-calendar-trade-filter` — any events blocking trade?
- `trade-psychology-coach` — discipline check

**If UNSAFE → output warning and stop. Do not proceed.**

### Step 6 — Technical Analysis (Phase 7+8)
Run ALL relevant analysis skills:
- `technical-analysis` — RSI, MACD, MAs, S/R, patterns
- `price-action` — candle patterns, structure
- `volume-analysis` — volume confirmation
- `market-structure-bos-choch` — BOS, CHoCH, zones
- `ict-smart-money` — order blocks, FVGs, liquidity
- `mtf-confluence-scorer` — multi-timeframe alignment
- `elliott-wave-engine` — wave count (if applicable)
- `harmonic-pattern-engine` — harmonic patterns (if detected)
- `fibonacci-harmonic-wave` — Fibonacci levels
- `chart-vision` — visual chart analysis (if screenshot available)

### Step 7 — Strategy Match (Phase 9)
- `strategy-selection` — match to regime
- `trading-brain` — orchestrate optimal approach

### Step 8 — Signal Confirmation (Phase 10)
- `ai-signal-aggregator` — combine all signals
- Require >= 65% agreement

### Step 9 — Risk & Sizing (Phase 11)
- `risk-and-portfolio` — position size
- `spread-slippage-cost-analyzer` — execution cost

### Step 10 — Entry Refinement (Phase 12)
- `zone-refinement-sniper-entry` — refine to maximize R:R

---

## Output Format

After running all phases, produce this consolidated brief:

```
================================================================
  TRADE ANALYSIS: [SYMBOL] | [ASSET CLASS] | [TIMEFRAME]
  [DATE] [TIME UTC] | Session: [CURRENT SESSION]
================================================================

  MACRO CONTEXT
  ─────────────
  DXY: [value] [direction]    VIX: [value] [level]
  Key Events: [next event] in [hours]h
  Macro Bias: [BULLISH/BEARISH/NEUTRAL] ([confidence]%)

  REGIME
  ──────
  Classification: [TRENDING/RANGING/VOLATILE/QUIET]
  Strength: [score]/100    Duration: [bars]
  Session Quality: [GOOD/FAIR/POOR]

  SENTIMENT
  ─────────
  Crowd: [BULLISH/BEARISH] ([pct]%)
  Contrarian Signal: [YES/NO]
  IV Rank: [value] ([HIGH/MED/LOW])

  SAFETY CHECK
  ─────────────
  Safe to Trade: [YES/NO]
  Next Event: [event] at [time]
  Daily Risk Used: [pct]% of [max]%

================================================================

  TECHNICAL ANALYSIS
  ──────────────────
  Trend (HTF):     [BULLISH/BEARISH/NEUTRAL]
  Structure:       [BOS UP/BOS DOWN/CHoCH/RANGING]
  Key Resistance:  [level1], [level2]
  Key Support:     [level1], [level2]
  Order Blocks:    [OB levels with bias]
  FVGs:            [FVG levels with direction]
  Liquidity:       [pools above/below]

  Indicators:
    RSI (14):      [value] — [OVERBOUGHT/NEUTRAL/OVERSOLD]
    MACD:          [signal] — [BULLISH/BEARISH CROSS/NEUTRAL]
    MAs:           Price [ABOVE/BELOW] 50 & 200 MA
    Volume:        [INCREASING/DECREASING/DIVERGENCE]

  Patterns:        [detected patterns]
  Elliott Wave:    [current wave count]
  Harmonics:       [pattern if detected]
  Confluence:      [score]% — [GRADE A/B/C]

================================================================

  STRATEGY & SIGNAL
  ─────────────────
  Matched Strategy: [strategy name]
  Signal:           [BUY/SELL/WAIT]
  Consensus:        [pct]% agreement ([count] signals)
  Confidence:       [HIGH/MEDIUM/LOW]

================================================================

  TRADE SETUP
  ────────────
  Direction:  [BUY/SELL]
  Entry:      [price] (refined zone: [zone range])
  Stop Loss:  [price] ([pips/points] | [pct]%)
  Take Profit 1: [price] ([pips/points] | R:R [ratio])
  Take Profit 2: [price] ([pips/points] | R:R [ratio])
  Take Profit 3: [price] ([pips/points] | R:R [ratio])

  Position Size:  [lots/shares] ([risk_pct]% of account)
  Risk Amount:    $[amount]
  Reward (TP2):   $[amount]
  Spread Cost:    [pips/$amount]

  MANAGEMENT PLAN
  ────────────────
  - Move SL to BE after TP1
  - Close 50% at TP1, trail rest
  - Trail using [method]
  - Max hold time: [duration]
  - Re-evaluate if: [condition]

================================================================

  SCORE CARD
  ──────────
  Macro Alignment:    [score]/10
  Regime Match:       [score]/10
  Technical Setup:    [score]/10
  Risk/Reward:        [score]/10
  Confluence:         [score]/10
  ─────────────────────────────
  OVERALL:            [total]/50 — [TAKE TRADE / WAIT / SKIP]

================================================================
```

### Decision Thresholds

| Score | Action |
|-------|--------|
| 40-50 | TAKE TRADE — high conviction, full size |
| 30-39 | TAKE TRADE — reduced size (50-75%) |
| 20-29 | WAIT — setup exists but needs more confluence |
| 0-19  | SKIP — insufficient edge, look elsewhere |

---

## Asset-Specific Skill Routing

Automatically invoke the right asset skill for deeper context:

| Detected Asset | Additional Skill |
|---------------|-----------------|
| Forex pair | `forex-trading` |
| US/Intl stock | `equities-trading` |
| Crypto | `crypto-defi-trading` |
| Futures | `futures-trading` |
| Options | `options-trading` |
| Gold/Silver | `commodities` via `cross-asset-relationships` |

---

## Examples

```
/analyze EURUSD           → Full forex analysis on H4 (default)
/analyze AAPL             → Full equity analysis on D1 (default)
/analyze BTCUSD           → Full crypto analysis on H4 (default)
/analyze XAUUSD           → Full gold analysis on H1 (default)
/analyze NQ               → Full Nasdaq futures on H4 (default)
/analyze EURUSD M15 scalp → Forex scalp analysis on M15
/analyze TSLA quick       → Quick 5-min stock analysis
/analyze GBPJPY sniper    → Forex with zone refinement focus
/analyze ETHUSD deep      → Full 18-phase crypto deep dive
/analyze SPY risk-only    → Should I trade SPY right now?
/analyze EURUSD levels    → Key levels and zones only
```

---

## Error Handling

| Issue | Response |
|-------|----------|
| Unrecognized symbol | Ask: "I don't recognize [X]. Is this forex, equity, crypto, or futures?" |
| Market closed | Note market hours, show analysis anyway with "market currently closed" flag |
| No data available | Fall back to available analysis skills, note data gaps |
| All signals conflict | Output "MIXED SIGNALS — NO TRADE" with breakdown of disagreements |

---

## After Output

After delivering the analysis:
1. Ask: "Want me to refine the entry, adjust risk, or execute?"
2. If user says "execute" or "take it" → invoke `mt5-integration` to place the order
3. If user says "refine" → invoke `zone-refinement-sniper-entry` for better entry
4. If user says "next" or another symbol → run analysis on the new symbol
5. If user says "journal" → invoke `trade-journal-analytics` to log

---

