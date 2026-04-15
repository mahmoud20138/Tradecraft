# Project Constitution — Auto-Trading AI Agent System

## Non-Negotiable Principles

1. **AI-Agent-First**
   - AI agents control ALL trading decisions — code is tools, not brain
   - 8 specialist agents collaborate like a prop trading desk
   - Every skill invocation logged with agent, skill, input, output, confidence
   - Devil's Advocate must challenge every trade (3/5 override to proceed)
   - 3 concurrent trading intensity modes (Bullet/Blitz/Rapid) run simultaneously

2. **Safety First**
   - All trades MUST pass through risk gate before execution
   - Kill switches must be accessible within 1 second
   - No position sizing without validated stop-loss
   - Max 2% risk per trade, 6% total portfolio exposure

3. **Async-First Architecture**
   - All I/O operations must be async (market data, API calls)
   - Non-blocking strategy evaluation
   - Parallel execution where safe (independent strategies)

4. **Statelessness**
   - No in-memory trade state — persist everything
   - System restart must not lose active positions
   - Recovery from last persisted state within 30 seconds

5. **Fail-Safe Defaults**
   - If risk check fails → BLOCK trade
   - If regime detection fails → assume RANGING (lowest risk)
   - If data feed fails → halt trading, notify
   - If API rate limited → back off exponentially

6. **Immutable Audit Trail**
   - Every decision logged with timestamp, rationale, state snapshot
   - Every trade logged with full context before/after
   - Never delete or modify historical logs

## Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Language** | Python 3.11+ | Async ecosystem, ML libraries |
| **Async Runtime** | asyncio (stdlib) | No uvloop — Windows compatible, sufficient for <500ms target |
| **State Management** | Redis (hot, AOF persistence) + PostgreSQL (cold) | Fast cache with durability + persistent storage |
| **Message Queue** | Redis Streams | Durable delivery with consumer groups + acknowledgment |
| **Market Data** | MT5 REST Bridge (primary), yFinance (backup) | Real-time + fallback |
| **MT5 Bridge** | FastAPI REST wrapper on Windows host | Decouples MT5 from Docker; all symbols, all timeframes |
| **Backtesting** | Vectorized pandas + numpy | Speed for optimization |
| **Monitoring** | Prometheus + Grafana | Industry standard metrics |
| **Container** | Docker + docker-compose | Reproducible deployment |
| **Process Management** | systemd (Linux) / NSSM (Windows) | Auto-restart on crash |

## Code Conventions

- **File naming**: `snake_case` for modules, `PascalCase` for classes
- **Async functions**: Prefixed with `async_` if wrapper around sync lib
- **Constants**: UPPER_CASE in `constants.py`
- **Logging**: Structured logging with `structlog`, always include `trade_id`, `strategy_id`
- **Error handling**: Explicit exception types, never catch `Exception` bare
- **Type hints**: Required on all public functions (mypy strict mode)
- **Tests**: pytest with >80% coverage required

## Architecture Constraints

- **No global state** — pass dependencies explicitly
- **No blocking I/O in event loop** — use thread pool for sync libs
- **Strategy isolation** — one strategy crash cannot affect others
- **Rate limiting** — built-in to all API clients, respect broker limits
- **Circuit breakers** — auto-disable failing components after 3 errors

## Trading Constraints (Immutable)

| Constraint | Value | Override |
|------------|-------|----------|
| Max risk per trade | User-configurable in settings (default 2%) | Applies to all modes equally; user decides risk tolerance |
| Max total exposure | 6% of capital | Requires manual approval |
| Max drawdown limit | Disabled (demo account) | Re-enable for live |
| Positions per symbol | 3 max total (long+short combined; e.g., 2L+1S=full) | Configurable |
| Symbol watchlist | Configurable subset of MT5 demo symbols | Default: top 20 forex + gold + indices |
| News blackout window | ±30 min around high-impact events | Non-negotiable |
| Trading hours | Unrestricted (demo account) | Re-enable per-asset session rules for live |
| Minimum win rate (live) | 45% | Halt trading if below (demo: disabled) |
| Minimum profit factor | 1.5 | Halt trading if below (demo: disabled) |

## Skill Integration (All 161 Classified Skills)

The system integrates with **ALL 161 classified skills** from the comprehensive skills taxonomy:

**TRADING (95 skills)**

**Core Knowledge (7):**
- `trading-fundamentals`, `forex-trading`, `equities-trading`, `futures-trading`, `options-trading`, `crypto-defi-trading`, `cow-protocol-sdk`

**Analysis (9):**
- `price-action`, `technical-analysis`, `volume-analysis`, `mtf-confluence-scorer`, `chart-vision`, `elliott-wave-engine`, `fibonacci-harmonic-wave`, `harmonic-pattern-engine`, `fundamental-analysis`

**Strategies (24):**
- ICT/SMC (6): `ict-smart-money`, `ict-trading-tool`, `market-structure-bos-choch`, `smart-money-trap-detector`, `smc-beginner-pro-guide`, `smc-python-library`
- Breakout (3): `breakout-strategy-engine`, `dan-zanger-breakout-strategy`, `zone-refinement-sniper-entry`
- Mean Reversion (3): `mean-reversion-engine`, `capitulation-mean-reversion`, `poc-bounce-strategy`
- Session (4): `asian-session-scalper`, `jdub-price-action-strategy`, `session-profiler`, `session-scalping`
- Other (8): `gap-trading-strategy`, `grid-trading-engine`, `news-straddle-strategy`, `cross-asset-arbitrage-engine`, `borsellino-10-commandments`

**Market Context (13):**
- `market-regime-classifier`, `economic-calendar`, `economic-indicator-tracker`, `macro-economic-dashboard`, `correlation-crisis`, `correlation-regime-switcher`, `cross-asset-relationships`, `multi-pair-basket-trader`, `pair-scanner-screener`, `synthetic-pair-constructor`, `market-breadth-analyzer`, `hurst-exponent-dynamics-crisis-prediction`, `volatility-surface-analyzer`, `institutional-timeline`

**Risk Management (8):**
- `risk-of-ruin`, `drawdown-playbook`, `risk-calendar-trade-filter`, `portfolio-optimization`, `risk-and-portfolio`, `real-time-risk-monitor`

**Execution (8):**
- `execution-algo-trading`, `market-impact-model`, `market-making-hft`, `spread-slippage-cost-analyzer`, `tick-data-storage`, `hedgequantx-prop-trading`

**Data & Signals (8):**
- `market-data-ingestion`, `alternative-data-integrator`, `social-sentiment-scraper`, `stocksight-sentiment`, `market-intelligence`, `news-intelligence`, `ai-signal-aggregator`

**MT5 Platform (3):**
- `mt5-integration`, `mt5-chart-browser`, `gold-orb-ea`

**Quant/ML (9):**
- `backtesting-sim`, `backtest-report-generator`, `ml-trading`, `quant-ml-trading`, `tensortrade-rl`, `trading-gym-rl-env`, `strategy-genetic-optimizer`, `statistics-timeseries`, `strategy-validation`

**AI Trading Agents (7):**
- `ai-trading-crew`, `autohedge-swarm`, `trading-agents-llm`, `freqtrade-bot`, `openalice-trading-agent`, `ritmex-crypto-agent`, `polymarket-prediction-agents`

**Psychology & Operations (3):**
- `trade-psychology-coach`, `trade-journal-analytics`, `trading-plan-builder`

**Infrastructure (6):**
- `realtime-alert-pipeline`, `discord-webhook`, `telegram-bot`, `trade-copier-signal-broadcaster`, `notion-sync`

**Orchestration (8):**
- `analyze`, `master-trading-workflow`, `xtrading-analyze`, `brain-ecosystem-mcp`, `trading-brain`, `trading-autopilot`, `strategy-selection`, `multi-strategy-orchestration`

**AI DEVELOPMENT (13 skills)**

**Agent Building (5):**
- `agent-development`, `ai-agent-builder`, `deepagents-langchain`, `agentic-storage`, `mcp-integration`

**Other (3):**
- `few-shot-quality-prompting`, `transformersjs`, `openspec`, `spec-kit`

**SOFTWARE ENGINEERING (20 skills)**

**Architecture (4):**
- `pro-code-architecture`, `gitnexus-codebase-intelligence`, `system-design-academy`, `build-your-own-x`

**Code Review (2):**
- `code-review`, `generate-snapshot`

**Testing (5):**
- `debug-failing-test`, `run-e2e-tests`, `run-integration-tests`, `run-pre-commit-checks`, `run-smoke-tests`

**UI Design (4):**
- `elite-ui-design`, `frontend-design`, `programmatic-drawing`, `playground`

**Dev Tools (7):**
- `e2b-sandboxes`, `git-phase-restore`, `github-actions-trigger`, `httpie-cli`, `ip-rotation`, `python-manager-discovery`

**Learning (1):**
- `interactive-coding-challenges`

**PLATFORM CLAUDE-CODE (23 skills)**

**Plugin Development (5):**
- `plugin-structure`, `plugin-settings`, `skill-development`, `command-development`, `hook-development`

**Skill Management (5):**
- `skill-manager`, `skill-analytics`, `skill-docs-generator`, `skill-doctor`, `skill-test-suite`

**Automation (4):**
- `claude-automation-recommender`, `claude-md-improver`, `skill-execution-governor` (MANDATORY), `writing-rules`

**Workflow Routing (4):**
- `smart-skill-router`, `skill-pipeline`, `context-memory`, `workflow-builder`

**DATA ACQUISITION (5 skills)**
- `firecrawl-cli`, `video-knowledge-extractor`, `youtube-video-to-knowledge`, `video-gen`

**DOMAIN SPECIFIC (2 skills)**
- `featool-multiphysics`, `stripe-best-practices`

**See [CLASSIFIED_SKILLS_CATALOG.md](../specs/auto-trading-system/CLASSIFIED_SKILLS_CATALOG.md) for complete taxonomy**

## Deployment Targets

| Environment | Purpose | Data Source | Trading |
|-------------|---------|-------------|---------|
| `paper` | Development & testing | Delayed 15min | Simulated |
| `demo` | Pre-production validation | Real-time | Simulated |
| `live` | Production trading | Real-time | Real money |

## Version

Constitution v7.0 — Updated 2026-03-19
- **FUNDAMENTAL**: Added AI-Agent-First as Principle #1
- **Added**: 8 specialist agents, Devil's Advocate, 3/5 override rule
- **Added**: 3 concurrent trading intensity modes (Bullet/Blitz/Rapid)
**Prior (v6.0):** Redis Streams, AOF, watchlist, Bearer auth
