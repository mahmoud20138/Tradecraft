# Feature: Auto-Trading AI Agent System

## Spec-Kit Workflow Position

```
1. constitution.md  → Immutable principles & tech stack ✓
2. spec.md          → THIS FILE - WHAT to build (requirements)
3. plan.md          → HOW to build (architecture, components)
4. tasks.md         → Ordered implementation tasks
5. [Implement]      → Execute following this spec
```

**This document defines WHAT the system must do, following the principles in constitution.md. Requirements here drive the architecture in plan.md.**

---

## Problem Statement

Manual trading is limited by human cognitive constraints:
- Cannot monitor multiple markets simultaneously 24/7
- Emotional decision-making leads to inconsistent results
- Slow reaction to market opportunities and risks
- Difficult to backtest and iterate on strategies

We need an **AI-agent-driven trading desk** where:
- AI agents ARE the traders — code/tools only accelerate their work
- 8 specialist agents collaborate like a prop trading desk (Head Trader, World Intel, Technician, Strategist, Risk Officer, Executor, Devil's Advocate, Mode Selector)
- 3 concurrent trading intensity modes (Bullet/Blitz/Rapid) run simultaneously like chess time controls
- Skills + data + conditions decide the mode, timing, and R:R — not hardcoded rules
- System is open to world changes: news, correlations, macro, sentiment, geo-economics
- Every skill invocation by every agent is visible and auditable
- Profitability comes from skill synergy: 161 skills working together beat any single strategy

## User Stories

### P1 — Must Have (MVP)

- [P1] As a **trader**, I want the system to **automatically analyze market conditions** so that I can identify trading opportunities without manual chart monitoring
  - Independently testable: Yes (analysis output can be validated)
  - MVP slice: Yes (all symbols, all timeframes)

- [P1] As a **trader**, I want **pre-trade risk filtering** so that the system never trades during high-risk conditions (news, low liquidity)
  - Independently testable: Yes (filter decisions are binary)
  - MVP slice: Yes (basic news calendar + session filter)

- [P1] As a **trader**, I want **automatic position sizing** based on account balance and stop-loss distance so that each trade risks exactly 1-2%
  - Independently testable: Yes (calculation is deterministic)
  - MVP slice: Yes (fixed fractional risk model)

- [P1] As a **trader**, I want the system to **automatically execute trades** when signal criteria are met so that I don't miss opportunities while away from the screen
  - Independently testable: Yes (execution can be paper traded)
  - MVP slice: Yes (single entry/exit, no partial fills)

- [P1] As a **trader**, I want **real-time monitoring** of open positions with automatic stop-loss and take-profit so that losses are contained and profits are protected
  - Independently testable: Yes (position tracking is isolated)
  - MVP slice: Yes (basic SL/TP, no trailing)

- [P1] As a **trader**, I want a **kill switch** that immediately halts all trading and closes positions so that I can stop the system in emergencies
  - Independently testable: Yes (kill switch action is verifiable)
  - MVP slice: Yes (manual trigger only)

### P2 — Should Have

- [P2] As a **trader**, I want **multiple strategies running in parallel** with signal aggregation so that I benefit from diverse analysis approaches
  - Independently testable: Yes (each strategy outputs independently)
  - MVP slice: No (requires orchestration layer)

- [P2] As a **trader**, I want **regime-aware strategy selection** so that trend-following strategies only activate in trending markets and mean-reversion in ranging markets
  - Independently testable: Yes (regime classification is isolated)
  - MVP slice: No (requires ML classifier)

- [P2] As a **trader**, I want **backtesting** of all strategies before live deployment so that I can verify historical performance
  - Independently testable: Yes (backtest is self-contained)
  - MVP slice: No (requires historical data infrastructure)

- [P2] As a **trader**, I want **performance analytics** showing win rate, profit factor, and drawdown so that I can evaluate system effectiveness
  - Independently testable: Yes (analytics read from trade log)
  - MVP slice: No (requires sufficient trade history)

### P3 — Nice to Have

- [P3] As a **trader**, I want **parameter optimization** using genetic algorithms so that strategies automatically adapt to market changes
  - Independently testable: Yes (optimization is offline process)
  - MVP slice: No

- [P3] As a **trader**, I want **Telegram/Discord notifications** for trade signals and position updates so that I can monitor the system remotely
  - Independently testable: Yes (notification is output side-effect)
  - MVP slice: No

- [P1] As a **trader**, I want **multi-asset support** (forex, stocks, crypto, commodities) so that I can diversify across markets
  - Independently testable: Yes (each asset is independent)
  - MVP slice: Yes (all symbols available on MT5 demo account)

- [P1] As a **trader**, I want **3 concurrent trading intensity modes** (Bullet, Blitz, Rapid — like chess time controls) running simultaneously so that the AI agents can trade at different speeds based on conditions
  - Independently testable: Yes (each mode has distinct TP/SL/hold-time, separate agent teams)
  - MVP slice: Yes (Mode Selector agent auto-activates based on regime+vol+spread+session)

## Functional Requirements

- [REQ-001] System must fetch real-time OHLCV data at minimum 1-minute granularity
- [REQ-002] System must classify market regime as TRENDING / RANGING / VOLATILE
- [REQ-003] System must generate trading signals with entry price, stop-loss, and take-profit
- [REQ-004] System must calculate position size based on user-configured risk % per trade (default 2%, editable in settings); scalping modes differ by TP/SL pip distance and hold time, NOT by risk %
- [REQ-005] System must reject trades during high-impact news events (±30 minutes)
- [REQ-006] System must support unrestricted trading hours (demo); re-enable per-asset session rules for live
- [REQ-007] System must execute market orders within 500ms of signal generation
- [REQ-008] System must log every trade with full context (market state, signal rationale, risk metrics)
- [REQ-009] System must enforce maximum 3 open positions per symbol (combined long+short; e.g., 2 long + 1 short = full)
- [REQ-010] System must trigger kill-switch within 1 second of user activation
- [REQ-011] System must recover previous state within 30 seconds after restart
- [REQ-012] System must track drawdown (enforcement disabled for demo account, re-enable for live)
- [REQ-013] System must run at least 3 independent strategies in parallel
- [REQ-014] System must aggregate strategy signals using weighted voting:
  - Confluence: Weighted linear score (0.0–1.0) with 10 factors, continuous inputs, hard gates on spread/news
  - Weights: htf_trend(0.20), regime_match(0.15), mtf_agreement(0.12), sr_proximity(0.12), volume(0.10), momentum(0.08), news_clear(0.08 gate), session(0.05), spread(0.05 gate), no_streak(0.05)
  - Min confluence threshold: 0.60 to take trade, 0.80 for full position size
  - Consensus: min 2/3 strategies agree; single strategy OK if confidence > 0.85 AND confluence > 0.70
  - Conflicting long/short = no trade
  - Confidence: weighted ratio of conditions met (each condition weighted by importance)
- [REQ-015] System must validate strategies via backtesting before deployment
- [REQ-016] System must support 3 concurrent trading intensity modes (Bullet tick/M1, Blitz M1/M5, Rapid M15+) each with distinct TP/SL/hold-time and spread guards, running simultaneously; Mode Selector agent decides activation
- [REQ-017] System must be controlled by 8 AI agents (Head Trader, World Intel, Technician, Strategist, Risk Officer, Executor, Devil's Advocate, Mode Selector) — code is tools only
- [REQ-018] Every skill invocation must be logged with agent name, skill name, input, output, confidence, and duration — full transparency
- [REQ-019] Devil's Advocate agent must challenge every trade; requires 3/5 agent agreement to override
- [REQ-020] World Intel agent must continuously feed news, macro, correlations, sentiment, calendar data to all modes
- [REQ-021] Mode Selector agent must use skills + conditions to decide which modes are active (not hardcoded rules)
- [REQ-022] Bullet mode (Mahmoud's preference): tick-level entries, 0.5-3 pip TP, 1-2 pip SL, London-NY overlap only, high accuracy, specific killzones

## Non-Functional Requirements

| Requirement | Metric | Priority |
|-------------|--------|----------|
| Latency (signal to order) | < 500ms p95 | P1 |
| Uptime | > 99.5% monthly | P1 |
| Data freshness | < 2 second delay | P1 |
| Recovery time | < 30 seconds | P1 |
| Memory usage | < 2GB baseline | P2 |
| CPU usage | < 50% average | P2 |
| API rate limit compliance | 100% | P1 |
| Test coverage | > 80% | P2 |

## Success Criteria

- [ ] **Profitability**: Positive return over 6-month backtest period
- [ ] **Risk Control**: Drawdown monitoring present (enforcement disabled for demo)
- [ ] **Win Rate**: Minimum 45% win rate in backtests
- [ ] **Profit Factor**: Minimum 1.5 (gross wins / gross losses)
- [ ] **Reliability**: Zero missed signals due to system errors in 30-day paper trading
- [ ] **Recovery**: Successful recovery from simulated crash 100% of times
- [ ] **Speed**: 95th percentile order latency under 500ms

## Dependencies

### External Services
- MT5 REST Bridge (FastAPI wrapper on Windows host, exposing MT5 terminal data + execution)
- PostgreSQL (for persistent storage)
- Redis (for state management and Streams)

### Internal Skills (from Claude Code ecosystem)

**ALL 161 CLASSIFIED SKILLS** integrated into the system:

**TRADING SKILLS (95)**

**Core Knowledge & Analysis (16):**
- `trading-fundamentals`, `forex-trading`, `equities-trading`, `futures-trading`, `options-trading`, `crypto-defi-trading`
- `technical-analysis`, `price-action`, `volume-analysis`, `mtf-confluence-scorer`
- `elliott-wave-engine`, `fibonacci-harmonic-wave`, `harmonic-pattern-engine`
- `fundamental-analysis`, `chart-vision`

**Strategies (24):**
- ICT/SMC (6): `ict-smart-money`, `ict-trading-tool`, `market-structure-bos-choch`, `smart-money-trap-detector`, `smc-beginner-pro-guide`, `smc-python-library`
- Breakout (3): `breakout-strategy-engine`, `dan-zanger-breakout-strategy`, `zone-refinement-sniper-entry`
- Mean Reversion (3): `mean-reversion-engine`, `capitulation-mean-reversion`, `poc-bounce-strategy`
- Session (4): `asian-session-scalper`, `jdub-price-action-strategy`, `session-profiler`, `session-scalping`
- Other (8): `gap-trading-strategy`, `grid-trading-engine`, `news-straddle-strategy`, `cross-asset-arbitrage-engine`, `borsellino-10-commandments`

**Market Context & Risk (21):**
- `market-regime-classifier`, `economic-calendar`, `economic-indicator-tracker`, `macro-economic-dashboard`
- `correlation-crisis`, `correlation-regime-switcher`, `cross-asset-relationships`, `multi-pair-basket-trader`, `pair-scanner-screener`, `synthetic-pair-constructor`
- `market-breadth-analyzer`, `hurst-exponent-dynamics-crisis-prediction`, `volatility-surface-analyzer`, `institutional-timeline`
- `risk-of-ruin`, `drawdown-playbook`, `risk-calendar-trade-filter`, `portfolio-optimization`, `risk-and-portfolio`, `real-time-risk-monitor`

**Execution & Data (19):**
- `execution-algo-trading`, `market-impact-model`, `market-making-hft`, `spread-slippage-cost-analyzer`, `tick-data-storage`, `hedgequantx-prop-trading`
- `market-data-ingestion`, `alternative-data-integrator`, `social-sentiment-scraper`, `stocksight-sentiment`
- `market-intelligence`, `news-intelligence`, `ai-signal-aggregator`
- `mt5-integration`, `mt5-chart-browser`, `gold-orb-ea`

**Quant/ML & AI Agents (16):**
- `backtesting-sim`, `backtest-report-generator`, `ml-trading`, `quant-ml-trading`, `tensortrade-rl`, `trading-gym-rl-env`, `strategy-genetic-optimizer`, `statistics-timeseries`, `strategy-validation`
- `ai-trading-crew`, `autohedge-swarm`, `trading-agents-llm`, `freqtrade-bot`, `openalice-trading-agent`, `ritmex-crypto-agent`, `polymarket-prediction-agents`

**Operations & Orchestration (14):**
- `trade-psychology-coach`, `trade-journal-analytics`, `trading-plan-builder`
- `realtime-alert-pipeline`, `discord-webhook`, `telegram-bot`, `trade-copier-signal-broadcaster`, `notion-sync`
- `analyze`, `master-trading-workflow`, `xtrading-analyze`, `brain-ecosystem-mcp`, `trading-brain`, `trading-autopilot`, `strategy-selection`, `multi-strategy-orchestration`

**AI DEVELOPMENT (13)**
- `agent-development`, `ai-agent-builder`, `deepagents-langchain`, `agentic-storage`, `mcp-integration`
- `few-shot-quality-prompting`, `transformersjs`, `openspec`, `spec-kit`

**SOFTWARE ENGINEERING (20)**
- `pro-code-architecture`, `gitnexus-codebase-intelligence`, `system-design-academy`, `build-your-own-x`
- `code-review`, `generate-snapshot`
- `debug-failing-test`, `run-e2e-tests`, `run-integration-tests`, `run-pre-commit-checks`, `run-smoke-tests`
- `elite-ui-design`, `frontend-design`, `programmatic-drawing`, `playground`
- `e2b-sandboxes`, `git-phase-restore`, `github-actions-trigger`, `httpie-cli`, `ip-rotation`, `python-manager-discovery`
- `interactive-coding-challenges`

**PLATFORM CLAUDE-CODE (23)**
- `plugin-structure`, `plugin-settings`, `skill-development`, `command-development`, `hook-development`
- `skill-manager`, `skill-analytics`, `skill-docs-generator`, `skill-doctor`, `skill-test-suite`
- `claude-automation-recommender`, `claude-md-improver`, `skill-execution-governor` (MANDATORY), `writing-rules`
- `smart-skill-router`, `skill-pipeline`, `context-memory`, `workflow-builder`

**DATA ACQUISITION (5)**
- `firecrawl-cli`, `video-knowledge-extractor`, `youtube-video-to-knowledge`, `video-gen`

**DOMAIN SPECIFIC (2)**
- `featool-multiphysics`, `stripe-best-practices`

**See [CLASSIFIED_SKILLS_CATALOG.md](CLASSIFIED_SKILLS_CATALOG.md) for complete 161-skill taxonomy**

## Out of Scope

- [ ] Predictive ML models for price forecasting (deferred to future phase)
- [ ] Social sentiment analysis from Twitter/Reddit (P3 feature)
- [ ] High-frequency trading (sub-second strategies)
- [ ] Options/futures derivatives (spot + CFDs in MVP, all symbols)
- [ ] Web UI (CLI and API only in MVP)

---

## Spec-Kit Completion Criteria

This spec is complete when:
- [ ] All user stories are independently testable
- [ ] All requirements have measurable acceptance criteria
- [ ] Success criteria are defined and quantifiable
- [ ] Dependencies and out-of-scope items are clearly listed

**Next Step:** Proceed to plan.md (architecture) or run `/speckit.clarify` for any ambiguities.

---

**Spec Status:** AI-Agent-First — Major Redesign
**Version:** 7.0
**Date:** 2026-03-19
**Spec-Kit:** ✓ Specification Complete + ✓ Scalping Modes
**Changes v7.0:**
- AI-Agent-First philosophy: 8 specialist agents, code is tools only
- REQ-017–REQ-022: Agent framework, transparency, Devil's Advocate, World Intel, Mode Selector, Bullet mode
- 3 concurrent trading intensity modes (Bullet/Blitz/Rapid) replace 4 scalping modes
- Problem statement rewritten for agent-driven trading desk
**Prior (v6.0):** Scalping modes, risk % user-configurable, confluence scoring
