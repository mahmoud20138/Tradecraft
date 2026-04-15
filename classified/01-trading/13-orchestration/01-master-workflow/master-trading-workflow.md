---
name: master-trading-workflow
description: Master 18-phase trading workflow — the definitive skill sequence for any trade. Covers infrastructure through automation. Use for "trading workflow", "full process", "trade checklist", "how to trade", "complete trading plan", "master plan", "what skills to run", "trade from scratch".
kind: workflow
category: trading/orchestration
status: active
tags: [defi, master, orchestration, trading, workflow]
related_skills: [analyze, brain-ecosystem-mcp, trading-autopilot]
---

# Master Trading Workflow — 18-Phase Skill Sequence

You are a **master trading process orchestrator**. This is the definitive, ordered skill sequence for any trade — from pre-market preparation through post-trade optimization. Every phase gates the next. **Never skip upstream phases.**

## Invocation

```
/master-trading-workflow EURUSD H4
/master-trading-workflow XAUUSD H1 phase:scan
/master-trading-workflow all-pairs morning-brief
/master-trading-workflow BTCUSD daily review-only
```

Options:
- `phase:<name>` — Start from a specific phase (assumes prior phases done)
- `morning-brief` — Phases 1-7 only (pre-market routine)
- `review-only` — Phases 15-17 only (post-trade review)
- `full-auto` — All 18 phases, autonomous execution
- `conservative` — 0.5% risk, R:R min 3:1, A-grade setups only
- `aggressive` — 2% risk, R:R min 1.5:1, A+B setups
- `analysis-only` — Phases 1-10 (no execution)

---

## THE MASTER SEQUENCE

```
PREPARE → CONTEXT → SENTIMENT → REGIME → FILTER → PLAN → SCAN → ANALYZE → STRATEGY → CONFIRM → RISK → REFINE → EXECUTE → MANAGE → REVIEW → BACKTEST → OPTIMIZE → AUTOMATE
  P1        P2         P3         P4       P5      P6     P7       P8        P9         P10      P11     P12      P13       P14      P15       P16        P17        P18
```

---

## Phase 1 — Infrastructure & Data Setup
**Gate:** Platform connected, data flowing, alerts configured.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 1.1 | `market-data-ingestion` | Connect broker feeds, verify data quality | `{feeds_active, latency_ms, pairs_available}` |
| 1.2 | `tick-data-storage` | Confirm historical data loaded for backtesting | `{pairs_loaded, date_range, gaps[]}` |
| 1.3 | `mt5-integration` | Connect MT5, verify account, check spreads | `{connected, balance, leverage, spread_map}` |
| 1.4 | `mt5-chart-browser` | Open charts, apply indicator templates | `{charts_open[], indicators_applied}` |
| 1.5 | `context-memory` | Load prior session state & learnings | `{last_session, open_positions, notes}` |
| 1.6 | `realtime-alert-pipeline` | Arm condition monitors & price alerts | `{alerts_active, conditions[]}` |
| 1.7 | `discord-webhook` | Verify Discord alert channel ready | `{webhook_active}` |
| 1.8 | `telegram-bot` | Verify Telegram notifications ready | `{bot_active}` |
| 1.9 | `notion-sync` | Pull watchlist & notes from Notion | `{watchlist[], notes}` |

**Skip condition:** If platform already connected and session is continuing, skip to Phase 2.

---

## Phase 2 — Macro & Big-Picture Context
**Gate:** You have a macro bias before looking at any chart.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 2.1 | `news-intelligence` | Morning brief — what happened overnight? | `{headlines[], impact_summary}` |
| 2.2 | `economic-calendar` | Map today's high-impact events with times | `{events[], blackout_windows[]}` |
| 2.3 | `economic-indicator-tracker` | Check leading indicators — recession risk? | `{indicators{}, cycle_phase, risk_level}` |
| 2.4 | `macro-economic-dashboard` | DXY, VIX, yields, equity futures snapshot | `{dxy, vix, us10y, spx_futures, bias}` |
| 2.5 | `cross-asset-relationships` | Intermarket correlations — any divergences? | `{correlations{}, divergences[], flags[]}` |
| 2.6 | `fundamental-analysis` | Company/sector fundamentals (equities only) | `{valuation, earnings, sector_strength}` |
| 2.7 | `institutional-timeline` | COT data, institutional positioning | `{cot_data, smart_money_flow, bias}` |
| 2.8 | `market-intelligence` | Full intelligence synthesis | `{macro_score, direction_bias, confidence}` |

**Decision point:** If macro is extremely uncertain or conflicting — reduce size in Phase 11.

---

## Phase 3 — Sentiment & Alternative Data
**Gate:** Gauge crowd positioning to avoid crowded trades.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 3.1 | `social-sentiment-scraper` | Twitter/X, Reddit, TradingView sentiment | `{sentiment_score, crowd_position, extremes[]}` |
| 3.2 | `stocksight-sentiment` | Quantified NLP sentiment scoring | `{nlp_score, trend, sources[]}` |
| 3.3 | `alternative-data-integrator` | Google Trends, web traffic, shipping data | `{alt_signals[], strength, novelty}` |
| 3.4 | `volatility-surface-analyzer` | IV rank, vol skew, term structure | `{iv_rank, skew, term_structure, signal}` |

**Contrarian flag:** If crowd sentiment >80% one direction → flag potential reversal.

---

## Phase 4 — Market Regime Classification
**Gate:** Know the regime BEFORE choosing a strategy.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 4.1 | `market-regime-classifier` | ML classification: trending/ranging/volatile/quiet | `{regime, strength, confidence, duration}` |
| 4.2 | `market-breadth-analyzer` | Broad market health — how many pairs trending? | `{trending_pct, breadth_score, divergences[]}` |
| 4.3 | `correlation-crisis` | Are correlations breaking down? | `{crisis_level, affected_pairs[], risk}` |
| 4.4 | `correlation-regime-switcher` | Should we switch strategy sets? | `{switch_signal, from_regime, to_regime}` |
| 4.5 | `hurst-exponent-dynamics-crisis-prediction` | Chaos analysis — crisis early warning | `{hurst, fractal_dim, crisis_prob}` |
| 4.6 | `session-profiler` | Current session stats & historical edge | `{session, avg_range, best_pairs[], volatility}` |

**Critical rule:** Trending regime → trend-following strategies only. Ranging → mean reversion only. Volatile → reduce size or sit out.

---

## Phase 5 — Risk Calendar & Trade Filter
**Gate:** Decide IF you should trade at all today. This phase has VETO power.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 5.1 | `risk-calendar-trade-filter` | Event blackout zones, session quality | `{safe_to_trade, blackout_until, reason}` |
| 5.2 | `trade-psychology-coach` | Emotional check-in — am I tilted? | `{emotional_state, tilt_score, discipline_rating}` |
| 5.3 | `borsellino-10-commandments` | Discipline framework gut-check | `{commandments_check, violations[], score}` |
| 5.4 | `drawdown-playbook` | Am I in drawdown? Size reduction needed? | `{drawdown_pct, playbook_action, size_modifier}` |

**HARD STOP conditions (do NOT proceed):**
- `safe_to_trade = false` (high-impact news within 30min)
- `tilt_score > 7` (emotional compromise)
- `drawdown_pct > 6%` (playbook says sit out)
- `discipline_rating < 5` (broken rules recently)

If any HARD STOP triggers → **LOG reason, STOP, revisit next session.**

---

## Phase 6 — Pre-Market Planning & Watchlist
**Gate:** Have a written plan before any analysis.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 6.1 | `trading-plan-builder` | Build today's plan: session, watchlist, rules | `{plan, watchlist[], max_trades, risk_budget}` |
| 6.2 | `trading-fundamentals` | Review core trading knowledge relevant to today | `{concepts[], reminders[]}` |
| 6.3 | `smc-beginner-pro-guide` | SMC methodology refresher (if using ICT/SMC) | `{checklist, key_concepts}` |

**Deliverable:** A written daily plan with:
- Max 6 pairs on watchlist (ranked A/B/C)
- Max trades today: 3
- Max daily risk: 2-4%
- Max per-trade risk: 1-2%
- Session focus (London/NY/Tokyo)
- Rules for today (written, not mental)

---

## Phase 7 — Scanning & Screening
**Gate:** Find the 3-6 best opportunities from the entire universe.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 7.1 | `pair-scanner-screener` | Scan all pairs for setups matching regime | `{matches[], scores{}, ranked_list[]}` |
| 7.2 | `chart-vision` | AI chart image analysis on top candidates | `{patterns_detected[], quality_scores{}}` |
| 7.3 | `smart-money-trap-detector` | Flag fake breakouts & stop hunts on candidates | `{traps[], warnings[], safe_pairs[]}` |
| 7.4 | `liquidity-analysis` | Map liquidity pools & order flow on candidates | `{liquidity_map{}, targets[], sweeps[]}` |

**Filter rule:** Only advance pairs with scanner score > 70 AND no active traps.

---

## Phase 8 — Technical Analysis (Deep Dive)
**Gate:** Full analysis on shortlisted pairs only (max 3-4).

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 8.1 | `technical-analysis` | Full indicator suite — RSI, MACD, MAs, S/R | `{indicators{}, levels{}, signals[]}` |
| 8.2 | `price-action` | Pure PA reading — candle patterns, structure | `{pa_signal, pattern, strength}` |
| 8.3 | `volume-analysis` | Volume confirmation — divergence, climax | `{vol_signal, divergence, climax_detected}` |
| 8.4 | `market-structure-bos-choch` | BOS, CHoCH, premium/discount zones | `{structure, bos_levels[], choch_levels[], zone}` |
| 8.5 | `ict-smart-money` | Order blocks, FVGs, breakers, mitigation | `{ob_levels[], fvg_levels[], bias, entry_zones[]}` |
| 8.6 | `ict-trading-tool` | ICT tool-specific implementation | `{tool_output}` |
| 8.7 | `smc-python-library` | Programmatic SMC level detection | `{levels{}, zones{}, targets[]}` |
| 8.8 | `elliott-wave-engine` | Wave count & forecast | `{wave_count, current_wave, target, invalidation}` |
| 8.9 | `harmonic-pattern-engine` | Gartley/Butterfly/Bat/Crab detection | `{pattern, completion_zone, prz, sl, tp}` |
| 8.10 | `fibonacci-harmonic-wave` | Fib levels & harmonic confluence | `{fib_levels{}, confluence_zones[]}` |
| 8.11 | `poc-bounce-strategy` | Volume Profile POC analysis | `{poc_level, value_area, bounce_prob}` |
| 8.12 | `mtf-confluence-scorer` | Multi-timeframe alignment score | `{mtf_score, aligned_tfs[], direction, grade}` |

**Minimum confluence requirement:** MTF score >= 70% AND at least 3 confirming factors.

---

## Phase 9 — Strategy Selection & Signal Generation
**Gate:** Match the RIGHT strategy to the regime + setup.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 9.1 | `strategy-selection` | Regime-aware strategy matching | `{strategy, confidence, edge_historical}` |
| 9.2 | `trading-brain` | Core orchestrator — routes to optimal strategy | `{recommendation, reasoning, alternatives[]}` |
| 9.3 | `smart-skill-router` | Auto-select optimal skill chain | `{chain[], priority, estimated_edge}` |

**Then execute the matched strategy:**

| Regime | Primary Skills | Fallback |
|--------|---------------|----------|
| **Trending** | `breakout-strategy-engine`, `dan-zanger-breakout-strategy` | `ict-smart-money` |
| **Ranging** | `mean-reversion-engine`, `poc-bounce-strategy` | `grid-trading-engine` |
| **Volatile** | `news-straddle-strategy`, `capitulation-mean-reversion` | `risk-calendar-trade-filter` → WAIT |
| **Quiet/Asian** | `asian-session-scalper`, `session-scalping` | `gap-trading-strategy` |
| **Breakout** | `breakout-strategy-engine`, `dan-zanger-breakout-strategy` | `zone-refinement-sniper-entry` |
| **Reversal** | `capitulation-mean-reversion`, `jdub-price-action-strategy` | `harmonic-pattern-engine` |
| **Multi-pair** | `multi-pair-basket-trader`, `cross-asset-arbitrage-engine` | `synthetic-pair-constructor` |
| **Grid/DCA** | `grid-trading-engine` | `mean-reversion-engine` |
| **Gold** | `gold-orb-ea` | `breakout-strategy-engine` |

---

## Phase 10 — Signal Aggregation & Confirmation
**Gate:** Never trade on a single signal. Require consensus.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 10.1 | `ai-signal-aggregator` | Weighted voting across ALL active strategies | `{aggregate_signal, confidence, agreement_pct}` |
| 10.2 | `ai-trading-crew` | 50-agent debate → consensus (for high-conviction) | `{consensus, bull_count, bear_count, veto}` |
| 10.3 | `trading-agents-llm` | Multi-agent LLM cross-validation | `{llm_signal, reasoning[], dissent[]}` |
| 10.4 | `skill-pipeline` | Auto-chain verification pipeline | `{pipeline_result, stages_passed}` |
| 10.5 | `workflow-builder` | Custom multi-skill confirmation chain | `{workflow_result, all_passed}` |

**Minimum consensus:** `agreement_pct >= 65%` AND no veto from risk team.

---

## Phase 11 — Risk Sizing & Pre-Trade Checks
**Gate:** Know your exact risk BEFORE entering.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 11.1 | `risk-and-portfolio` | Position sizing (% risk model) | `{lots, risk_dollars, risk_pct, portfolio_heat}` |
| 11.2 | `risk-of-ruin` | Probability of ruin at this size | `{ruin_prob, kelly_fraction, optimal_size}` |
| 11.3 | `real-time-risk-monitor` | Current portfolio exposure check | `{open_risk, correlation_risk, max_drawdown}` |
| 11.4 | `portfolio-optimization` | Optimal allocation vs existing positions | `{allocation, rebalance_needed, conflicts[]}` |
| 11.5 | `spread-slippage-cost-analyzer` | True cost of this trade | `{spread_cost, expected_slippage, total_cost}` |
| 11.6 | `market-impact-model` | Will my order move the market? | `{impact_bps, optimal_algo, split_recommended}` |

**Hard rules:**
- Never risk > 2% per trade (1% default)
- Portfolio heat never > 6% total
- R:R minimum 2:1 (1.5:1 aggressive only)
- Ruin probability must be < 1%

**Size modifiers from earlier phases:**
- Drawdown active → multiply size by drawdown modifier (Phase 5.4)
- Low confidence signal → reduce by 50%
- Macro uncertainty → reduce by 25%

---

## Phase 12 — Entry Refinement (Sniper Entry)
**Gate:** Refine entry to maximize R:R. Don't market-order in.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 12.1 | `zone-refinement-sniper-entry` | Drop TF, find smaller zones inside larger zones | `{refined_entry, refined_sl, new_rr, improvement}` |
| 12.2 | `strategy-validation` | Final pre-entry validation checklist | `{valid, checklist{}, warnings[]}` |

**Sniper entry rules:**
- Drop from H4 → H1 → M15 to find nested zone
- Entry must be inside the refined zone
- SL behind the refined zone (not the original)
- This alone can improve R:R from 2:1 to 5:1+

---

## Phase 13 — Execution
**Gate:** Pull the trigger. No hesitation if all phases passed.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 13.1 | `execution-algo-trading` | TWAP/VWAP/Iceberg for larger orders | `{algo, slices[], estimated_fill}` |
| 13.2 | `mt5-integration` | Place order on MT5 | `{ticket, entry, sl, tp, status}` |
| 13.3 | `trading-autopilot` | Full autonomous execution (if full-auto mode) | `{autopilot_result}` |
| 13.4 | `multi-strategy-orchestration` | Manage multiple concurrent strategies | `{active_strategies[], positions[]}` |
| 13.5 | `autohedge-swarm` | Auto-hedge correlated positions if needed | `{hedge_orders[], net_exposure}` |
| 13.6 | `trade-copier-signal-broadcaster` | Broadcast signal to copier/followers | `{broadcast_sent, recipients}` |
| 13.7 | `market-making-hft` | Market making execution (if applicable) | `{mm_orders[], spread_captured}` |

**Post-execution immediate:**
- Confirm fill price vs expected
- Verify SL/TP are set correctly
- Log entry in journal
- Set alerts for TP1, TP2, breakeven

---

## Phase 14 — Position Management & Monitoring
**Gate:** Manage the trade — don't just set and forget.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 14.1 | `realtime-alert-pipeline` | Price alerts at key levels, TP1/TP2/BE | `{alerts_armed[]}` |
| 14.2 | `real-time-risk-monitor` | Live P&L, drawdown, exposure tracking | `{live_pnl, max_adverse, risk_status}` |
| 14.3 | `trade-psychology-coach` | Mid-trade emotional check (don't move stops!) | `{discipline_check, urges_detected[], advice}` |
| 14.4 | `discord-webhook` | Push live updates to Discord | `{notifications_sent}` |
| 14.5 | `telegram-bot` | Push mobile alerts for key events | `{alerts_sent}` |
| 14.6 | `loop` | Poll position status on interval | `{monitoring_active, interval}` |

**Management rules:**
- Move SL to breakeven after TP1 hit
- Trail stop using prior-bar-highs/lows method
- Partial close 50% at TP1, let rest run to TP2
- NEVER widen stop loss
- NEVER add to a losing position
- Re-check regime if trade duration exceeds 2x expected

---

## Phase 15 — Post-Trade Review & Journaling
**Gate:** Every trade teaches something. No exceptions.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 15.1 | `trade-journal-analytics` | Log full trade: entry, exit, setup type, R-multiple | `{journal_entry, r_multiple, tags[]}` |
| 15.2 | `notion-sync` | Sync journal entry to Notion database | `{synced, notion_page_id}` |
| 15.3 | `trade-psychology-coach` | Post-trade emotional debrief | `{debrief, emotional_errors[], discipline_score}` |
| 15.4 | `context-memory` | Save learnings for next session | `{memories_saved[]}` |

**Journal must include:**
- Screenshot of entry & exit
- Setup type and strategy used
- R-multiple result
- What went right
- What went wrong
- Emotional state during trade
- Would you take this trade again? Why/why not?
- One lesson for next time

---

## Phase 16 — Backtesting & Validation
**Gate:** Prove the strategy works over N trades before sizing up.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 16.1 | `backtesting-sim` | Run historical simulation on strategy | `{trades, win_rate, profit_factor, max_dd}` |
| 16.2 | `backtest-report-generator` | Equity curves, Monte Carlo, tearsheets | `{report_url, sharpe, sortino, calmar}` |
| 16.3 | `statistics-timeseries` | Statistical edge validation — is it real? | `{p_value, t_stat, edge_significant}` |
| 16.4 | `strategy-validation` | Walk-forward, out-of-sample testing | `{oos_result, degradation_pct, robust}` |

**Minimum requirements before live:**
- 100+ backtest trades
- Win rate > 45% with R:R > 2:1 (or > 55% with R:R > 1:1)
- Profit factor > 1.5
- Max drawdown < 15%
- Walk-forward efficiency > 50%
- Monte Carlo 95th percentile still profitable

---

## Phase 17 — Optimization & Evolution
**Gate:** Continuously improve what's working. Kill what isn't.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 17.1 | `strategy-genetic-optimizer` | Evolve parameters via genetic algorithms | `{optimized_params, improvement_pct}` |
| 17.2 | `ml-trading` | Train ML models on trade features | `{model, accuracy, feature_importance[]}` |
| 17.3 | `quant-ml-trading` | Quantitative ML strategy development | `{quant_model, alpha_decay, signals[]}` |
| 17.4 | `skill-analytics` | Which skills & strategies perform best? | `{top_skills[], underperformers[], recommendations[]}` |

**Optimization rules:**
- Never optimize on less than 200 trades
- Always hold out 30% for validation
- If optimized result is >2x better than base → suspect overfitting
- Re-validate quarterly

---

## Phase 18 — Automation & Bot Deployment
**Gate:** Automate proven, validated strategies only.

| Step | Skill | Action | Output |
|------|-------|--------|--------|
| 18.1 | `freqtrade-bot` | Deploy crypto trading bot | `{bot_id, strategy, pairs[], status}` |
| 18.2 | `tensortrade-rl` | Train RL agent on strategy | `{agent, reward_curve, episodes}` |
| 18.3 | `trading-gym-rl-env` | RL environment for training | `{env_config, observation_space, action_space}` |
| 18.4 | `openalice-trading-agent` | Deploy autonomous AI agent | `{agent_id, status, watchlist[]}` |
| 18.5 | `polymarket-prediction-agents` | Prediction market bot | `{agent_id, markets[], edge}` |
| 18.6 | `ritmex-crypto-agent` | Crypto agent deployment | `{agent_id, strategy, status}` |

**Automation rules:**
- Only automate strategies with 6+ months live track record
- Start with 25% of manual size
- Kill switch: auto-stop if drawdown > 10%
- Weekly human review mandatory
- Never automate a strategy you don't fully understand

---

## Asset-Specific Reference Layer
**Called as-needed based on instrument type.**

| Asset | Skill | When to Invoke |
|-------|-------|----------------|
| Stocks | `equities-trading` | Equity-specific edge, market hours, earnings |
| Forex | `forex-trading` | FX sessions, pip calculations, carry |
| Futures | `futures-trading` | Contract specs, rollover, margin |
| Options | `options-trading` | Greeks, spreads, expiry management |
| Crypto | `crypto-defi-trading` | DeFi, funding rates, on-chain data |

---

## Quick Reference: Phase Gates

```
Phase 1  → Platform connected?               YES → Continue | NO → Fix setup
Phase 2  → Macro bias formed?                YES → Continue | NO → Wait for clarity
Phase 3  → Sentiment extreme?                YES → Flag contrarian | NO → Continue
Phase 4  → Regime identified?                YES → Continue | NO → Default to ranging
Phase 5  → Safe to trade?                    YES → Continue | NO → STOP (hard veto)
Phase 6  → Plan written?                     YES → Continue | NO → Write it now
Phase 7  → Setups found?                     YES → Continue | NO → No trade today
Phase 8  → Confluence >= 70%?                YES → Continue | NO → Skip this pair
Phase 9  → Strategy matched to regime?       YES → Continue | NO → Re-check Phase 4
Phase 10 → Consensus >= 65%?                 YES → Continue | NO → Downgrade or skip
Phase 11 → Risk sized correctly?             YES → Continue | NO → Recalculate
Phase 12 → Sniper entry refined?             YES → Continue | NO → Use standard entry
Phase 13 → Order placed & confirmed?         YES → Continue | NO → Troubleshoot
Phase 14 → Monitoring active?                YES → Continue | NO → Set alerts NOW
Phase 15 → Trade journaled?                  YES → Continue | NO → Journal before next trade
Phase 16 → Strategy backtested?              YES → Continue | NO → Paper trade first
Phase 17 → Parameters current?               YES → Continue | NO → Schedule optimization
Phase 18 → Bot supervised?                   YES → Continue | NO → Add kill switch
```

---

## Daily Routine Template

### Pre-Market (35 min)
```
06:30  Phase 2 — Macro scan (5 min)
06:35  Phase 3 — Sentiment check (5 min)
06:40  Phase 4 — Regime classification (3 min)
06:43  Phase 5 — Risk filter & psychology (5 min)
06:48  Phase 6 — Write today's plan (7 min)
06:55  Phase 7 — Scan & shortlist (10 min)
07:05  READY — Wait for session open
```

### Active Trading
```
Phase 8-12 — On each setup (5-15 min per pair)
Phase 13    — Execute when all gates pass
Phase 14    — Monitor until exit
```

### Post-Market (15 min)
```
Phase 15 — Journal all trades (10 min)
Phase 15 — Lessons & memory save (5 min)
```

### Weekly
```
Phase 16 — Backtest new ideas
Phase 17 — Review & optimize parameters
Phase 18 — Review bot performance
```

---

## Emergency Protocols

| Situation | Action |
|-----------|--------|
| Flash crash | Close all positions, invoke `drawdown-playbook` |
| Black swan news | `risk-calendar-trade-filter` → assess, likely close all |
| Platform disconnect | Use mobile backup, don't panic-close |
| Tilt detected | `trade-psychology-coach` → STOP trading, walk away |
| Max daily loss hit | STOP. No more trades today. Journal and review. |
| Correlation breakdown | `correlation-crisis` → reduce exposure, hedge |

