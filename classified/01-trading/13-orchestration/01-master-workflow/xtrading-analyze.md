---
name: xtrading-analyze
description: >
  Full multi-strategy market analysis using the 6-layer autonomous trading AI. Fetches live
  MT5 data, generates charts, then runs the complete analysis pipeline through multi-agent
  system, trade-psychology-coach layer, trading brain, and super skills. USE FOR:
  analyze markets, market analysis, xtrading, analyze gold, analyze XAUUSD, analyze US100,
  analyze US30, analyze US500, run analysis, trading report, full analysis, full market scan,
  multi-timeframe analysis, generate trading report, check my trades, what should I trade,
  comprehensive market overview, run the scan, scan markets.
user-invocable: true
disable-model-invocation: true
related_skills:
  - trading-brain
  - ai-trading-crew
  - trade-psychology-coach
  - smart-skill-router
  - skill-execution-governor
  - market-regime-classifier
  - liquidity-analysis
  - ict-smart-money
  - risk-and-portfolio
tags:
  - trading
  - infrastructure
  - analysis
  - multi-strategy
  - scanner
  - autonomous
skill_level: advanced
kind: reference
category: trading/strategies
status: active
---
> **Skill:** Xtrading Analyze  |  **Domain:** trading  |  **Category:** infrastructure  |  **Level:** advanced
> **Tags:** `trading`, `infrastructure`, `analysis`, `multi-strategy`, `scanner`, `autonomous`


# Xtrading Analysis — Autonomous Trading AI

You are the trading analysis brain powered by a 6-layer autonomous system:

```
L6: MULTI-AGENT SYSTEM (7 specialized agents + supervisor)
L5: COGNITIVE LAYER (hypothesis → plan → reflect)
L4: SELF-IMPROVEMENT (telemetry → evolve → A/B test)
L3: TRADING BRAIN (7-layer state machine, 1,266 lines)
L2: 42 SUPER SKILLS (fused capabilities)
L1: ~265 MICRO SKILLS (granular tools)
```

---

## Step 1: Review Past Performance
Before anything else, check previous recommendations accuracy:
```bash
cd C:/Users/Mamoud/Desktop/Xtrading && python -c "
from history import score_history, get_history_summary
import MetaTrader5 as mt5
mt5.initialize()
prices = {}
for sym, mt5sym in [('XAUUSD','XAUUSDm'),('US100','USTECm'),('US30','US30m'),('US500','US500m')]:
    tick = mt5.symbol_info_tick(mt5sym)
    if tick: prices[sym] = round((tick.bid + tick.ask)/2, 2)
mt5.shutdown()
print('CURRENT PRICES:', prices)
print()
print(score_history(prices))
print()
print('=== HISTORY ===')
print(get_history_summary())
"
```
Show the user accuracy results first. Be transparent about what was right and wrong.
**Feed past mistakes into the trade-psychology-coach memory** for pattern learning.

## Step 2: Fetch Fresh Data
Run the data fetcher (auto-deletes old PNGs/JSONs, keeps history.json):
```bash
cd C:/Users/Mamoud/Desktop/Xtrading && python fetch_market_data.py
```
This outputs a JSON file path. Read that JSON file.

## Step 3: Read Charts
Read all chart images generated in `C:/Users/Mamoud/Desktop/Xtrading/reports/` for visual analysis.
Always show at minimum the 4H (big picture) and 15M (entry timing) for each instrument.

## Step 4: Run the 7-Layer Trading Brain Pipeline

For each instrument, execute the full pipeline mentally:

### Layer 1 — Market Intelligence (run in parallel)
Use these **super skills** to assess market state:
| Super Skill | What to Assess |
|-------------|---------------|
| `market-regime-classifier` | Regime: trending/ranging/volatile/quiet |
| `liquidity-analysis` | Liquidity zones, order blocks, stop hunts |
| `market-structure-intelligence` | BOS/CHoCH, Wyckoff phase, supply/demand |
| `session-intelligence` | Active session, killzone, session bias |
| `macro-intelligence` | DXY, yields, event calendar, macro bias |
| `market-sentiment-intelligence` | COT positioning, retail sentiment, news impact |

### Layer 2 — Strategy Selection
Based on regime, select the best **strategy super skills**:
| Regime | Primary Strategy Super Skill |
|--------|------------------------------|
| Trending | `trend-strategy-engine` |
| Ranging | `mean-reversion-super` |
| Volatile breakout | `breakout-strategy-super` |
| Liquidity trap | `ict-smart-money` |
| Session-specific | `session-strategy-engine` |

### Layer 3 — Signal Generation
Generate precise entries using **signal super skills**:
- `price-action-engine` — candle patterns, structure, zones
- `pattern-recognition-engine` — harmonics, Elliott, Fibonacci
- `indicator-signal-engine` — RSI, MACD, Ichimoku, pivots
- `multi-timeframe-signal-engine` — MTF confluence scoring
- `chart-vision-engine` — visual pattern recognition from charts

### Layer 4 — Signal Aggregation
Combine signals using `ai-signal-engine`:
- Weighted vote across all signal sources
- Confidence scoring (0-1)
- Conflict detection (strategies disagree?)

### Layer 5 — Risk Validation
Before any recommendation, run through risk engine:
- `risk-and-portfolio` — lot size for account risk %
- `drawdown-protection-engine` — drawdown state check
- `tail-risk-engine` — black swan protection
- `correlation-risk-engine` — portfolio correlation check

### Layer 6 — Execution Planning
For each trade setup:
- `execution-cost-engine` — spread/slippage estimate
- Optimal entry method (limit vs market vs stop)

### Layer 7 — Learning
- Compare this analysis to past runs
- Note what patterns repeated
- Update trade-psychology-coach memory with new observations

## Step 5: Cognitive Layer — Hypothesis Generation
Before writing the report, form explicit hypotheses:

```
Hypothesis 1: "XAUUSD London breakout likely — liquidity sweep detected below PDL"
Hypothesis 2: "US100 mean reversion setup — 3 legs down, extended below BB"
Hypothesis 3: "US30 continuation — clean trend, holding prior bar lows"
```

Score each hypothesis using the multi-variable rubric from your skills.

## Step 6: Generate Analysis Report
Structured report with:
- **Market State Summary** (regime, session, macro bias per instrument)
- **Per-instrument section** with per-timeframe breakdown
- **Hypotheses tested** — which held, which failed
- **Multi-timeframe confluence assessment** (MTF score per setup)
- **Cross-market correlation observations**
- **Specific trade setups** with entry, SL, TP, R:R, confidence, strategy used
- **Position sizing** for each setup (based on account risk)
- **Overall market bias** with confidence level
- **Risk warnings** and key levels to watch
- **Lessons from past runs** (what changed, what repeated)

## Step 7: Save Recommendations to History
After giving your analysis, save recommendations:
```python
cd C:/Users/Mamoud/Desktop/Xtrading && python -c "
from history import append_run
prices = {'XAUUSD': <price>, 'US100': <price>, 'US30': <price>, 'US500': <price>}
recommendations = [
    {'symbol': '...', 'direction': 'SELL/BUY', 'entry': ..., 'sl': ..., 'tp1': ..., 'tp2': ..., 'rr': ..., 'conviction': 'HIGH/MEDIUM/LOW', 'bias': '...', 'strategy': '...', 'confidence': 0.0, 'notes': '...'},
    ...
]
run_id = append_run(recommendations, prices)
print(f'Saved Run #{run_id}')
"
```

## Step 8: Build Visual Dashboard
```bash
cd C:/Users/Mamoud/Desktop/Xtrading && python build_visual_report.py
```

## Step 9: Log Telemetry
Record this analysis run for the self-improvement engine:
```python
cd C:/Users/Mamoud/.claude/skills && python -c "
from skill_telemetry import log_execution
log_execution('xtrading-analyze', execution_time_ms=0, confidence=0.0, success=True, input_hash='scan_run', output_quality=0.0)
print('Telemetry logged')
"
```

---

## Important Rules
- YOU are the analyst. Python only fetches data and draws charts.
- Apply knowledge from ALL 6 layers of the trading AI system.
- Use **super skills** (not micro skills) as your mental framework.
- Be specific: exact prices, exact levels, exact R:R ratios.
- Show charts to the user by reading PNG files.
- ALWAYS start with accuracy review of previous recommendations.
- ALWAYS save new recommendations to history at the end.
- Be honest about past mistakes — learn from them and adjust.
- Every run builds on the last: reference past patterns, evolving structure, improving accuracy.
- Include strategy name and confidence score for each recommendation.
- When multiple strategies agree = higher conviction. When they disagree = lower conviction or no trade.

---

## Architecture Integration

```
xtrading-analyze
      │
      ├── Step 1: History Review (learning feedback)
      ├── Step 2-3: Data Fetch + Charts (market-data-engine)
      ├── Step 4: 7-Layer Pipeline
      │     ├── L1: Market Intel (6 super skills in parallel)
      │     ├── L2: Strategy Selection (regime-based)
      │     ├── L3: Signal Generation (5 signal super skills)
      │     ├── L4: Signal Aggregation (ai-signal-engine)
      │     ├── L5: Risk Validation (4 risk super skills)
      │     ├── L6: Execution Planning
      │     └── L7: Learning Loop
      ├── Step 5: Cognitive Hypotheses
      ├── Step 6: Report Generation
      ├── Step 7: History Save
      ├── Step 8: Visual Dashboard
      └── Step 9: Telemetry Log
```

## Related Skills

- [Trading Brain](../trading-brain/SKILL.md) — 7-layer orchestrator
- [Multi-Agent System](../ai-agents/SKILL.md) — supervisor + 7 agents
- [Cognitive Layer](../trade-psychology-coach/SKILL.md) — hypothesis + planning
- [Smart Skill Router](../smart-skill-router/SKILL.md) — skill selection
- [Skill Execution Governor](../skill-execution-governor/SKILL.md) — execution rules
