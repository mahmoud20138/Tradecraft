# Tasks: Auto-Trading AI Agent System

## Spec-Kit Workflow Reference

This tasks document is part of the Spec-Kit workflow:

```
1. constitution.md  → Immutable principles & tech stack (COMPLETED)
2. spec.md          → WHAT to build (user stories, requirements) (COMPLETED)
3. plan.md          → HOW to build (architecture, components) (COMPLETED)
4. tasks.md         → THIS FILE - Ordered implementation tasks
5. [Implement]      → Execute tasks following this document
```

**Before starting any phase:**
- Review [constitution.md](../../memory/constitution.md) for non-negotiable principles
- Reference [spec.md](spec.md) for user stories and requirements
- Consult [plan.md](plan.md) for technical architecture
- Check [data-model.md](data-model.md) for entity schemas

## Legend

- `[P]` = Parallelizable (can run simultaneously with other `[P]` tasks)
- `T###` = Task ID
- `P1/P2/P3` = Priority from spec.md
- `BLOCKS` = This task blocks subsequent tasks
- `📋 Spec-Kit` = Reference to spec.md requirements
- `🏗️ Plan` = Reference to plan.md architecture
- `🔗 Skill` = Claude Code skill integration
- `📊 Monitor` = Continuous monitoring checkpoint

---

## Phase 0 — Project Setup

**Spec-Kit References:**
- 📋 **Constitution**: Python 3.11+, asyncio, Docker, test coverage >80%
- 📋 **Spec**: REQ-001 (data fetching), REQ-011 (recovery)
- 🏗️ **Plan**: Component Architecture, Deployment Stack

**Skill Integration:**
- 🔗 `smart-skill-router` — Skill routing and auto-selection
- 🔗 `skill-execution-governor` — MANDATORY meta-skill governing all skill interactions

**Monitoring:**
- 📊 Skill invocation logging setup
- 📊 Skill health check initialization

- [ ] T000 **Initialize repository structure**
  - Create directory layout from plan.md
  - Initialize git repository
  - Create .gitignore (Python, IDE, secrets)
  - Create README.md with project overview
  - Set up Alembic for PostgreSQL migrations
  - Configure Redis with AOF persistence (appendonly yes)
  - **Skills**: Copy skill_router.py, skills_index.json, skills_graph.json
  - **Estimated**: 30 minutes
  - **Deliverable**: Ready repository with DB migration tooling

- [ ] T001 **[P] Set up Python environment + Skill Bridge**
  - Create pyproject.toml with dependencies
  - Create requirements.txt
  - Set up pre-commit hooks (black, ruff, mypy)
  - Create pytest.ini
  - **Skills**: Create src/skills/skill_bridge.py, skill_invoker.py
  - **Estimated**: 20 minutes
  - **Deliverable**: Working Python dev environment with skill bridge

- [ ] T002 **[P] Create Docker + Skill Config**
  - Write Dockerfile (Python 3.11 slim base)
  - Write docker-compose.yml (includes Redis, PostgreSQL)
  - Create .dockerignore
  - **Skills**: Create config/skills.yaml (skill-specific configs)
  - **Estimated**: 30 minutes
  - **Deliverable**: Working docker-compose up with skill config loader

---

## Phase 1 — Core Infrastructure (BLOCKS everything else)

**Spec-Kit References:**
- 📋 **Constitution**: Statelessness, async-first, structured logging
- 📋 **Spec**: REQ-011 (recovery <30s), REQ-007 (<500ms latency)
- 🏗️ **Plan**: Concurrency Model, Error Handling Strategy

*This phase implements the foundation — all subsequent phases depend on these components.*

- [ ] T010 **Create configuration system** (`src/core/config.py`)
  - Load from YAML with environment overrides
  - Validate with Pydantic
  - Support multiple environments (paper, demo, live)
  - **Estimated**: 1 hour
  - **Deliverable**: Working config loading with tests

- [ ] T011 **Set up structured logging** (`src/core/logging_config.py`)
  - Configure structlog with JSON output
  - Add correlation ID middleware
  - Create log formatters for console/file
  - **Estimated**: 45 minutes
  - **Deliverable**: Structured logs with trace context

- [ ] T012 **Create state manager** (`src/core/state_manager.py`)
  - Redis-backed key-value store
  - Get/set/delete with TTL support
  - State snapshot/restore
  - **Estimated**: 2 hours
  - **Deliverable**: State persistence with tests

- [ ] T013 **Create event bus** (`src/core/event_bus.py`)
  - Redis Streams (not Pub/Sub) for message durability
  - Consumer groups for reliable delivery
  - Publish/subscribe methods with acknowledgment
  - Event typing and validation
  - Dead-letter handling for failed events
  - **Estimated**: 2.5 hours
  - **Deliverable**: Durable async event system with tests

- [ ] T014 **Create AI Agent Framework** (`src/agents/base_agent.py`, `src/agents/agent_desk.py`)
  - BaseAgent class: name, assigned skills, invoke_skill(), log_interaction()
  - SkillInvocation logging: agent_name, skill_name, input, output, confidence, duration_ms, mode_context
  - AgentDesk: orchestrates 8 agents, manages collaboration protocol
  - Agent communication via Redis Streams (agent:request, agent:response channels)
  - 8 agents: HEAD_TRADER, WORLD_INTEL, TECHNICIAN, STRATEGIST, RISK_OFFICER, EXECUTOR, DEVILS_ADVOCATE, MODE_SELECTOR
  - Devil's Advocate: challenges every trade, requires 3/5 override
  - AgentVote + TradeDecision logging (data-model entities): persist every vote to Redis+PostgreSQL
  - Skill-agent binding map (which agent owns which skills)
  - **Estimated**: 4 hours
  - **Deliverable**: Agent framework with skill invocation logging + tests

- [ ] T015 **Create Trading Intensity Manager** (`src/agents/mode_manager.py`)
  - 3 concurrent modes: BULLET (tick/M1), BLITZ (M1/M5), RAPID (M15+)
  - Each mode gets its own agent team instance (shared World Intel)
  - Mode Selector agent: uses regime + vol + spread + session + performance to activate/deactivate modes
  - Mode-specific confluence weights (data-model SCALPING_CONFLUENCE_WEIGHTS)
  - Bullet priority during London-NY overlap when spread < 1 pip
  - Auto-pause mode after 3 consecutive losses (1 hour cooldown)
  - **Estimated**: 3 hours
  - **Deliverable**: 3 concurrent trading intensity modes with auto-selection + tests

---

## Phase 2 — Data Layer

**Spec-Kit References:**
- 📋 **Constitution**: MT5 REST Bridge primary, yFinance backup, tick data persistence
- 📋 **Spec**: REQ-001 (real-time OHLCV, <2s delay)
- 🏗️ **Plan**: MT5 Bridge architecture, Event Flow (market:tick channel)
- 📊 **Data Model**: Tick, OHLCVBar, AccountInfo, OrderRequest/Result entities

- [ ] T019 **MT5 REST Bridge service** (`mt5_bridge/`)
  - FastAPI app wrapping MetaTrader5 Python API
  - REST endpoints: /symbols, /ohlcv, /ticks, /account, /order, /positions
  - WebSocket streams: /ws/ticks (multi-symbol), /ws/bars
  - Bearer token auth (ATS_BRIDGE_API_KEY), bind to 127.0.0.1
  - Health check, auto-reconnect, rate limiting
  - Mock mode (--mock flag) for testing without MT5 terminal
  - NSSM service wrapper for auto-start on Windows
  - **Estimated**: 5 hours
  - **Deliverable**: Running bridge on port 8510 with all endpoints + mock mode

- [ ] T020 **[P] Create base feed interface** (`src/data/base_feed.py`)
  - Abstract BaseFeed class
  - Define tick/bar data models
  - Subscription interface
  - **Estimated**: 1 hour
  - **Deliverable**: Abstract interface with tests

- [ ] T021 **[P] Implement MT5 Bridge client** (`src/data/mt5_bridge_client.py`)
  - Async HTTP client (httpx) for REST endpoints
  - WebSocket tick subscription for real-time data
  - Connection pooling + retry logic + circuit breaker
  - Fallback to yFinance on bridge down
  - Publish ticks to Redis event bus
  - All symbols, all timeframes (M1→MN1)
  - **Estimated**: 3 hours
  - **Deliverable**: Working bridge client with tests

- [ ] T022 **Create OHLCV cache** (`src/data/ohlcv_cache.py`)
  - Aggregate ticks to bars (M1, M5, M15, M30, H1, H4, D1, W1, MN1)
  - Redis caching with TTL
  - Historical bar queries via bridge REST
  - **Estimated**: 2 hours
  - **Deliverable**: Cached bar data with tests

- [ ] T023 **Create tick storage** (`src/data/tick_storage.py`)
  - Append-only PostgreSQL storage
  - Bulk insert optimization
  - Cleanup old data (retention policy)
  - **Estimated**: 2 hours
  - **Deliverable**: Persistent tick storage

---

## Phase 3 — Analysis Layer

**Spec-Kit References:**
- 📋 **Constitution**: Fail-safe defaults (regime fail → RANGING)
- 📋 **Spec**: REQ-002 (regime classification), REQ-005 (news blacklist)
- 🏗️ **Plan**: Analysis Layer components, Skill Integration
- 📊 **Data Model**: MarketState entity
- 🔗 **Skills**: market-regime-classifier, technical-analysis, news-intelligence

- [ ] T030 **[P] Implement regime classifier** (`src/analysis/regime_classifier.py`)
  - Input: OHLCV bars
  - Output: TRENDING / RANGING / VOLATILE
  - Use ADX + directional movement
  - **Estimated**: 3 hours
  - **Deliverable**: Regime classification with tests

- [ ] T031 **[P] Implement technical indicators** (`src/analysis/technical_indicators.py`)
  - RSI, MACD, ATR, EMA, Bollinger Bands
  - Vectorized with pandas/numpy
  - **Estimated**: 2 hours
  - **Deliverable**: Indicator calculations with tests

- [ ] T032 **[P] Implement news filter** (`src/analysis/news_filter.py`)
  - Economic calendar integration
  - High-impact event blacklist
  - Session time filtering
  - **Estimated**: 2 hours
  - **Deliverable**: Pre-trade filtering with tests

- [ ] T033 **Create market intelligence aggregator** (`src/analysis/market_intelligence.py`)
  - Combine all analysis outputs
  - Publish MarketState to event bus
  - **Estimated**: 2 hours
  - **Deliverable**: Unified market state

---

## Phase 4 — Strategy Layer

**Spec-Kit References:**
- 📋 **Constitution**: Strategy isolation (one crash cannot affect others)
- 📋 **Spec**: REQ-003 (signals with SL/TP), REQ-013 (3 strategies min)
- 🏗️ **Plan**: Strategy Layer components, Signal Flow
- 📊 **Data Model**: TradingSignal, StrategyConfig entities
- 🔗 **Skills**: breakout-strategy-engine, mean-reversion-engine, ict-smart-money

- [ ] T040 **[P] Create base strategy interface** (`src/strategies/base_strategy.py`)
  - Abstract BaseStrategy class
  - Signal generation interface
  - Configuration schema
  - **Estimated**: 1 hour
  - **Deliverable**: Strategy interface with tests

- [ ] T041 **[P] Implement breakout strategy** (`src/strategies/breakout_strategy.py`)
  - Bollinger Band squeeze detection
  - Volume confirmation
  - **Estimated**: 3 hours
  - **Deliverable**: Working breakout strategy

- [ ] T042 **[P] Implement mean reversion strategy** (`src/strategies/mean_reversion_strategy.py`)
  - RSI extreme + Bollinger bounce
  - Ranging regime filter
  - **Estimated**: 2 hours
  - **Deliverable**: Working mean reversion strategy

- [ ] T043 **[P] Implement ICT SMC strategy** (`src/strategies/ict_smc_strategy.py`)
  - Order block detection
  - Break of structure
  - **Estimated**: 4 hours
  - **Deliverable**: Working ICT strategy

- [ ] T045 **Implement trading intensity mode strategies** (`src/strategies/intensity_strategies.py`)
  - 3 trading intensity modes: BULLET (tick/M1), BLITZ (M1/M5), RAPID (M15+)
  - Per-mode config: timeframe, hold duration, TP/SL pips, max concurrent (risk % is global user setting)
  - Spread guard: reject if spread > TP * 0.3, pause mode on spread widening
  - Continuous spread monitor loop: subscribe to tick stream, auto-pause/resume modes
  - Time exit: auto-close at max hold duration
  - Breakeven rules: 50% TP for blitz, none for bullet (too fast), standard for rapid
  - Bullet entries: tick velocity spike, bid/ask imbalance, spread compression
  - Blitz entries: M1 candle patterns + momentum + order flow delta
  - Rapid entries: M15/H1 structure + confluence + HTF alignment
  - Works WITH T015 Mode Manager (T015 = which modes active, T045 = mode-specific strategy logic)
  - **Estimated**: 4 hours
  - **Deliverable**: 3 trading intensity mode strategies with spread guard + time exit tests

- [ ] T044 **Create strategy registry** (`src/strategies/strategy_registry.py`)
  - Dynamic strategy loading (including scalping modes)
  - Strategy enable/disable per config
  - **Estimated**: 1 hour
  - **Deliverable**: Dynamic strategy management

---

## Phase 5 — Signal Processing

**Spec-Kit References:**
- 📋 **Constitution**: Immutable audit trail (every decision logged)
- 📋 **Spec**: REQ-008 (full context logging), REQ-014 (signal aggregation)
- 🏗️ **Plan**: Signal Processing components, Event Flow (signal:new channel)
- 📊 **Data Model**: TradingSignal lifecycle (PENDING → VALIDATED → FILLED)
- 🔗 **Skills**: ai-signal-aggregator, smart-skill-router

- [ ] T050 **Create signal generator** (`src/signals/signal_generator.py`)
  - Convert strategy output to TradingSignal
  - Assign signal IDs
  - **Estimated**: 1.5 hours
  - **Deliverable**: Signal generation with tests

- [ ] T051 **Implement signal validator** (`src/signals/signal_validator.py`)
  - Check regime compatibility
  - Validate price levels
  - **Estimated**: 1.5 hours
  - **Deliverable**: Signal validation with tests

- [ ] T052 **Implement signal aggregator** (`src/signals/signal_aggregator.py`)
  - Confluence scoring: Weighted linear (Tier 1), 10 factors, continuous 0.0–1.0
  - Weights: htf_trend(0.20), regime(0.15), mtf(0.12), sr(0.12), volume(0.10), momentum(0.08), news(0.08 gate), session(0.05), spread(0.05 gate), streak(0.05)
  - Hard gates: news_clear + spread_normal must pass (>= 0.5) before scoring
  - Thresholds: <0.60 = no trade, 0.60–0.80 = scaled size, >0.80 = full size
  - Confidence: per-strategy weighted ratio of conditions met
  - Consensus: min 2/3 agree; single OK if confidence > 0.85 AND confluence > 0.70
  - Conflicting long/short = no trade
  - Output: score + factor breakdown for journaling
  - **Estimated**: 3 hours
  - **Deliverable**: Confluence scorer with threshold + consensus tests

- [ ] T053 **Create signal history** (`src/signals/signal_history.py`)
  - PostgreSQL audit log
  - Query by symbol/time/strategy
  - **Estimated**: 2 hours
  - **Deliverable**: Signal audit trail

---

## Phase 6 — Risk Management (CRITICAL PATH)

**Spec-Kit References:**
- 📋 **Constitution**: Max 2% risk/trade, 6% total, drawdown tracking (demo: no enforcement), kill switch <1s
- 📋 **Spec**: REQ-004 (position sizing 1-2%), REQ-005 (news filter), REQ-009 (max 3 positions/symbol), REQ-010 (kill switch <1s), REQ-012 (drawdown tracking only for demo)
- 🏗️ **Plan**: Risk Management Layer, Error Handling (risk breach → kill switch)
- 📊 **Data Model**: Portfolio entity with risk metrics
- 🔗 **Skills**: risk-and-portfolio, risk-calendar-trade-filter, real-time-risk-monitor, drawdown-playbook

*⚠️ CRITICAL PATH: All trading flows through this layer. No trade executes without passing risk gate.*

- [ ] T060 **Implement position sizer** (`src/risk/position_sizer.py`)
  - Fractional risk calculation (1-2%)
  - ATR-based stop loss
  - Risk:reward ratio validation (min 1:2)
  - **Estimated**: 2 hours
  - **Deliverable**: Position sizing with tests

- [ ] T061 **Implement risk filter** (`src/risk/risk_filter.py`)
  - Max 3 positions per symbol
  - Max 6% total exposure
  - News blacklist enforcement
  - **Estimated**: 2 hours
  - **Deliverable**: Pre-trade gate with tests

- [ ] T062 **Implement portfolio monitor** (`src/risk/portfolio_monitor.py`)
  - Real-time PnL tracking
  - Drawdown calculation
  - Exposure per symbol
  - **Estimated**: 2 hours
  - **Deliverable**: Portfolio tracking with tests

- [ ] T063 **Implement drawdown tracker** (`src/risk/drawdown_tracker.py`)
  - High water mark tracking
  - Current drawdown % calculation
  - Logging only for demo (no enforcement)
  - Configurable enforcement tiers (re-enable for live)
  - **Estimated**: 1.5 hours
  - **Deliverable**: Drawdown monitoring with tests

- [ ] T064 **Implement kill switch** (`src/risk/kill_switch.py`)
  - Immediate halt of all trading
  - Close all positions via MT5 Bridge (POST /positions/close-all)
  - Manual trigger only for demo (auto-triggers disabled)
  - Restore state after review
  - **Estimated**: 2 hours
  - **Deliverable**: Emergency shutdown with tests

---

## Phase 7 — Execution Layer

**Spec-Kit References:**
- 📋 **Constitution**: No blocking I/O in event loop, retry on failure
- 📋 **Spec**: REQ-007 (execute within 500ms), REQ-008 (full context logging)
- 🏗️ **Plan**: Execution Layer components, Event Flow (trade:open/close channels)
- 📊 **Data Model**: Trade, Position entities
- 🔗 **Skills**: execution-algo-trading, market-impact-model

- [ ] T070 **Implement order router** (`src/execution/order_router.py`)
  - Submit orders via MT5 Bridge REST API (POST /order)
  - Uses OrderRequest/OrderResult models from data-model.md
  - Retry on failure with circuit breaker
  - Order confirmation handling
  - **Estimated**: 3 hours
  - **Deliverable**: Order execution with tests

- [ ] T071 **Implement SL/TP manager** (`src/execution/sltp_manager.py`)
  - Set stop-loss on position open
  - Set take-profit on position open
  - Trailing stop (P2 feature)
  - **Estimated**: 2 hours
  - **Deliverable**: SL/TP management with tests

- [ ] T072 **Implement position tracker** (`src/execution/position_tracker.py`)
  - Track open positions via MT5 Bridge (GET /positions)
  - Close positions via bridge (DELETE /position/{ticket})
  - Sync with internal state in Redis
  - Publish position updates to event bus
  - **Estimated**: 2 hours
  - **Deliverable**: Position sync with tests

- [ ] T073 **Implement execution reporter** (`src/execution/execution_reporter.py`)
  - Log all fills
  - Calculate slippage
  - **Estimated**: 1.5 hours
  - **Deliverable**: Execution logging with tests

---

## Phase 8 — Monitoring & Control

**Spec-Kit References:**
- 📋 **Constitution**: Kill switch accessible within 1 second
- 📋 **Spec**: REQ-010 (kill switch <1s), NFR (uptime >99.5%, memory <2GB)
- 🏗️ **Plan**: Monitoring components, Prometheus metrics definitions
- 📊 **Data Model**: Portfolio state in Redis (hot storage)
- 🔗 **Skills**: real-time-risk-monitor, realtime-alert-pipeline

- [ ] T080 **[P] Create metrics collector** (`src/monitoring/metrics_collector.py`)
  - Prometheus metrics export
  - System and trading metrics
  - **Estimated**: 2 hours
  - **Deliverable**: Prometheus endpoint

- [ ] T081 **[P] Create health check** (`src/monitoring/health_check.py`)
  - Component health status
  - HTTP health endpoint
  - **Estimated**: 1 hour
  - **Deliverable**: Health check endpoint

- [ ] T082 **[P] Create CLI dashboard** (`src/monitoring/dashboard.py`)
  - Rich/textual TUI
  - Real-time position display
  - **Estimated**: 3 hours
  - **Deliverable**: Interactive dashboard

- [ ] T083 **Implement alert manager** (`src/monitoring/alert_manager.py`)
  - Alert routing (console, file, webhook)
  - Alert severity levels
  - **Estimated**: 2 hours
  - **Deliverable**: Alert notifications

---

## Phase 9 — Backtesting (P2)

**Spec-Kit References:**
- 📋 **Constitution**: Test coverage >80%, validate strategies before deployment
- 📋 **Spec**: Success criteria (positive return, drawdown <15%, win rate >45%, profit factor >1.5)
- 🏗️ **Plan**: Backtesting components, Performance metrics
- 🔗 **Skills**: backtesting-sim, strategy-genetic-optimizer, backtest-report-generator

*📌 P2 Feature: Not required for MVP, but essential for strategy validation before live trading.*

- [ ] T090 **Implement backtest engine** (`src/backtest/engine.py`)
  - Vectorized historical testing
  - Slippage and spread simulation
  - **Estimated**: 4 hours
  - **Deliverable**: Working backtester

- [ ] T091 **Implement metrics calculator** (`src/backtest/metrics.py`)
  - Sharpe, Sortino, Calmar
  - Win rate, profit factor
  - **Estimated**: 2 hours
  - **Deliverable**: Performance metrics

- [ ] T092 **Implement report generator** (`src/backtest/reports.py`)
  - HTML/Markdown reports
  - Equity curve visualization
  - **Estimated**: 3 hours
  - **Deliverable**: Backtest reports

---

## Phase 10 — Integration & Main Loop

**Spec-Kit References:**
- 📋 **Constitution**: Async event loop, graceful shutdown, state recovery
- 📋 **Spec**: REQ-011 (recovery <30s), REQ-007 (<500ms latency)
- 🏗️ **Plan**: Concurrency Model, Main Event Loop, Component Architecture
- 🔗 **Skills**: trading-brain (orchestration), multi-strategy-orchestration

*🔗 This phase connects all components. T100 is the main entry point implementing the full trading flow.*

- [ ] T100 **Create main entry point** (`src/main.py`)
  - Initialize all components
  - Start async event loop
  - Graceful shutdown handling
  - **Estimated**: 2 hours
  - **Deliverable**: Working application

- [ ] T101 **End-to-end integration tests**
  - Full trading flow test (using MT5 Bridge mock mode)
  - Kill switch test (<1s response)
  - Recovery test (<30s state restore)
  - **Estimated**: 3 hours
  - **Deliverable**: Integration test suite

- [ ] T102 **Latency budget verification + load test**
  - Measure per-hop latency: tick→regime→strategy→confluence→risk→order
  - Target: total <500ms p95
  - Simulate 100+ ticks/sec across 20 symbols
  - Verify <50% CPU, <2GB memory under load
  - **Estimated**: 2 hours
  - **Deliverable**: Latency report + load test script

---

## Phase 11 — Documentation & Deployment

**Spec-Kit References:**
- 📋 **Constitution**: Deployment via Docker, systemd process management
- 📋 **Spec**: Success criteria (system reliability, zero missed signals)
- 🏗️ **Plan**: Deployment Architecture, Security Considerations
- 🔗 **Skills**: Full integration with 20+ Claude Code trading skills

*📚 Completes the Spec-Kit workflow: Constitution → Spec → Plan → Tasks → Implement → Deploy*

- [ ] T110 **Write user documentation**
  - Installation guide
  - Configuration guide
  - Operation guide
  - **Estimated**: 3 hours
  - **Deliverable**: Complete README

- [ ] T111 **Create deployment scripts**
  - Production deployment
  - Monitoring setup
  - **Estimated**: 2 hours
  - **Deliverable**: Deploy-ready system

---

## Task Summary

| Phase | Tasks | Estimated Time | Priority | Spec-Kit Reference |
|-------|-------|----------------|----------|-------------------|
| 0 — Setup | 3 | 1.25h | P1 | Constitution, Spec REQ-001, Alembic + Redis AOF |
| 1 — Core + Agents | 6 | 14h | P1 | Agent framework, trading intensity modes, Redis Streams |
| 2 — Data | 5 | 13h | P1 | MT5 Bridge (auth + mock) + Data Model |
| 3 — Analysis | 4 | 9h | P1 | Skills: regime-classifier, technical-analysis |
| 4 — Strategies | 6 | 15h | P1 | Skills: breakout, mean-rev, ICT + 3 intensity modes |
| 5 — Signals | 4 | 8h | P1 | Skills: ai-signal-aggregator, confluence scorer |
| 6 — Risk | 5 | 9.5h | P1 | Constitution (2% rule), DD tracking only (demo) |
| 7 — Execution | 4 | 8.5h | P1 | Via MT5 Bridge REST (authenticated) |
| 8 — Monitor | 4 | 8h | P1 | Constitution (kill switch), Plan Metrics |
| 9 — Backtest | 3 | 9h | P2 | Skills: backtesting-sim, genetic-optimizer |
| 10 — Integration | 3 | 7h | P1 | E2E tests + latency budget + load test |
| 11 — Docs | 2 | 5h | P1 | Complete Spec-Kit workflow |
| **TOTAL** | **49** | **~106.25 hours** | — | **Full Spec-Kit implementation** |

---

## Spec-Kit Phase Completion Checklist

Before marking a phase complete, verify:

- [ ] **Constitution** — All code follows immutable principles
- [ ] **Spec** — All user stories implemented and testable
- [ ] **Plan** — Architecture matches actual implementation
- [ ] **Data Model** — Schemas correctly implemented
- [ ] **Tests** — Unit tests with >80% coverage
- [ ] **Documentation** — Code documented, README updated

---

## MVP Definition (Minimum Viable Product)

The MVP consists of **Phases 0-8 + 10-11** (excluding P2 backtesting features).

**MVP Scope:**
- All symbols, all timeframes (MT5 demo account)
- 3 core strategies (breakout, mean reversion, ICT)
- Risk management (position sizing, exposure limits, drawdown tracking)
- Demo account trading (unrestricted hours, no DD enforcement)
- MT5 REST Bridge for data + execution
- CLI monitoring dashboard

**MVP Timeline:** ~68 hours of development

---

## Spec-Kit Workflow Complete

```
.specify/memory/constitution.md     ────┐
.specify/specs/auto-trading-system/  │
├── spec.md                          ├──▶ Complete Specification
├── plan.md                          │
├── tasks.md          (THIS FILE)     │
├── data-model.md                    │
└── contracts/api-spec.json          │
                                      │
         READY FOR IMPLEMENTATION ────┘
```

**Next Step:** Run `/speckit.implement` or begin Phase 0 (T000-T002)

---

**Tasks Status:** AI-Agent-First Architecture
**Version:** 7.0
**Date:** 2026-03-19
**Spec-Kit:** Workflow Complete ✓
**Changes v7.0:**
- T014: NEW — AI Agent Framework (8 agents, skill invocation logging, collaboration protocol)
- T015: NEW — Trading Intensity Manager (Bullet/Blitz/Rapid concurrent modes)
- Phase 1 expanded: 4 → 6 tasks, 7h → 14h (agent infrastructure is foundational)
- REQ-017–REQ-022: Agent control, transparency, Devil's Advocate, World Intel, Mode Selector, Bullet
- Total: 49 tasks, ~107.25 hours
**Prior (v6.0):** Scalping modes, risk user-configurable, confluence weights
