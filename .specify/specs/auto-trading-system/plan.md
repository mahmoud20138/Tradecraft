# Implementation Plan: Auto-Trading AI Agent System

## Spec-Kit Workflow Position

```
1. constitution.md  → Immutable principles & tech stack ✓
2. spec.md          → WHAT to build (user stories, requirements) ✓
3. plan.md          → THIS FILE - HOW to build (architecture)
4. tasks.md         → Ordered implementation tasks
5. [Implement]      → Execute following this plan
```

**This document defines HOW the system will be built, following the principles in constitution.md and requirements in spec.md.**

---

## ENHANCED: Complete Skill Integration Plan

### Overview: 161 Classified Skills → 7-Layer Architecture

This plan maps **all 161 classified skills** from the comprehensive skills taxonomy to specific implementation phases, with continuous monitoring and AI agent orchestration.

**Skill Sources:**
- **161 individual skills** in the classified/ folder taxonomy (the canonical count)
- **56 super-skills** are logical groupings that consolidate related skills for routing
- **Complete Coverage**: All trading, AI development, software engineering, platform, data acquisition, and domain-specific skills
- Skills are Claude Code skills invoked by the AI agent — not runtime application code

**Documentation:**
- See [CLASSIFIED_SKILLS_CATALOG.md](CLASSIFIED_SKILLS_CATALOG.md) for complete 161-skill taxonomy
- Skills are organized by 6 major categories with detailed subcategories

## Core Philosophy: AI-Agent-First Architecture

> **"The AI agents ARE the traders. Code is just their hands."**
>
> This is NOT a coded trading bot with AI features bolted on.
> This is a **team of AI trading experts** that collaborate in real-time,
> each with deep domain skills, debating and deciding together —
> like a professional prop trading desk where every seat is an AI agent.
>
> Tools and code only exist to: fetch data, execute orders, persist state.
> All decisions — what to trade, when, how much, which mode — are made by agents.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HEAD TRADER (Orchestrator Agent)                          │
│           Assigns work, resolves conflicts, makes final calls               │
│           Skills: trading-brain, multi-strategy-orchestration                │
└─────────────────────────────────────────────────────────────────────────────┘
         │              │              │              │              │
         ▼              ▼              ▼              ▼              ▼
┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐
│ WORLD INTEL  ││ TECHNICIAN   ││ STRATEGIST   ││ RISK OFFICER ││ EXECUTOR     │
│ AGENT        ││ AGENT        ││ AGENT        ││ AGENT        ││ AGENT        │
│              ││              ││              ││              ││              │
│ • News/macro ││ • TA/PA/vol  ││ • ICT/SMC    ││ • Sizing     ││ • Order mgmt │
│ • Sentiment  ││ • Regime     ││ • Breakout   ││ • Kill switch││ • SL/TP mgmt │
│ • Correlat.  ││ • Confluence ││ • Mean rev   ││ • DD track   ││ • Fill track  │
│ • Calendar   ││ • S/R levels ││ • Scalping   ││ • Portfolio  ││ • Slippage    │
│ • Geo/econ   ││ • MTF align  ││ • Mode select││ • Exposure   ││ • Reporting   │
│              ││              ││              ││              ││              │
│ 22 skills    ││ 15 skills    ││ 28 skills    ││ 12 skills    ││ 10 skills     │
└──────────────┘└──────────────┘└──────────────┘└──────────────┘└──────────────┘
         │              │              │              │              │
         └──────────────┴──────────────┴──────┬───────┴──────────────┘
                                              │
                                              ▼
                              ┌────────────────────────────┐
                              │    DEVIL'S ADVOCATE AGENT   │
                              │  Challenges every trade     │
                              │  "Why will this FAIL?"      │
                              │  Must be overruled by 3/5   │
                              │  agents to proceed          │
                              └────────────────────────────┘
```

### Agent Collaboration Protocol

Every trade decision follows this flow:

```
1. WORLD INTEL scans news, macro, correlations → publishes WorldBrief
2. TECHNICIAN reads WorldBrief + market data → publishes TechAnalysis
3. STRATEGIST reads both → proposes TradeSetup (mode, entry, SL, TP, R:R)
4. RISK OFFICER evaluates TradeSetup → approves/rejects with RiskVerdict
5. DEVIL'S ADVOCATE challenges → publishes CounterArgument
6. HEAD TRADER resolves: if 3/5 agents agree → sends to EXECUTOR
7. EXECUTOR places order via MT5 Bridge → publishes TradeResult
8. All agents learn from outcome → update their skill weights
```

**Every step is logged with the agent name, skill invoked, input, output, and reasoning.**
The user can see exactly which agent said what, which skill was used, and why.

### Skill-Agent Binding (visible interaction)

Each agent invokes specific skills. Every invocation is logged to Redis Streams:

```python
@dataclass
class SkillInvocation:
    """Logged for every skill call — full transparency"""
    timestamp: datetime
    agent_name: str          # e.g. "TECHNICIAN"
    skill_name: str          # e.g. "technical-analysis"
    input_summary: str       # e.g. "XAUUSD H1 last 200 bars"
    output_summary: str      # e.g. "RSI=72, MACD bearish cross, regime=TRENDING"
    confidence: float        # Agent's confidence in this output
    duration_ms: int         # How long the skill took
    mode_context: str        # Which trading intensity mode this serves (bullet/blitz/rapid)
```

---

## Concurrent Trading Intensitys (Bullet / Blitz / Rapid)

Like chess time controls — **all 3 modes run simultaneously** on the same symbols,
each with its own agent team instance, but sharing the same World Intel feed.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SHARED WORLD INTELLIGENCE                            │
│              (News, Macro, Correlations, Calendar, Sentiment)                │
│              One WORLD INTEL AGENT feeds ALL modes                           │
└───────────────┬─────────────────────┬─────────────────────┬─────────────────┘
                │                     │                     │
                ▼                     ▼                     ▼
┌───────────────────────┐ ┌───────────────────────┐ ┌───────────────────────┐
│   ♟ BULLET MODE       │ │   ♞ BLITZ MODE        │ │   ♜ RAPID MODE        │
│   (= NANO + ULTRA)    │ │   (= MICRO + SCALP)   │ │   (= Standard)        │
│                       │ │                       │ │                       │
│ TF: Tick / M1         │ │ TF: M1 / M5          │ │ TF: M15 / H1 / H4    │
│ Hold: 1s–60s          │ │ Hold: 30s–15 min      │ │ Hold: 15 min–4h+      │
│ TP: 0.5–3 pips        │ │ TP: 3–15 pips         │ │ TP: 15–100+ pips      │
│ SL: 1–2 pips          │ │ SL: 3–5 pips          │ │ SL: 10–50 pips        │
│ R:R: Skills decide    │ │ R:R: Skills decide    │ │ R:R: Skills decide    │
│                       │ │                       │ │                       │
│ ★ Mahmoud's pref:     │ │ Medium frequency      │ │ Swing/position        │
│   High accuracy       │ │ Balanced approach     │ │ High conviction only  │
│   Tight SL/TP         │ │                       │ │                       │
│   Specific killzones  │ │                       │ │                       │
│   Very risky but      │ │                       │ │                       │
│   high win-rate       │ │                       │ │                       │
│                       │ │                       │ │                       │
│ Active sessions:      │ │ Active sessions:      │ │ Active sessions:      │
│ London-NY overlap     │ │ London + NY           │ │ All sessions          │
│ 13:00–16:00 UTC       │ │                       │ │                       │
│                       │ │                       │ │                       │
│ Own agent team:       │ │ Own agent team:       │ │ Own agent team:       │
│ TECH + STRAT + RISK   │ │ TECH + STRAT + RISK   │ │ TECH + STRAT + RISK   │
│ + EXEC + DEVIL        │ │ + EXEC + DEVIL        │ │ + EXEC + DEVIL        │
└───────────────────────┘ └───────────────────────┘ └───────────────────────┘
         │                         │                         │
         └─────────────────────────┴─────────────────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   MODE SELECTOR AGENT        │
                    │   Decides which modes are    │
                    │   active based on:           │
                    │   • Current regime           │
                    │   • Volatility level         │
                    │   • Spread conditions        │
                    │   • Session / killzone       │
                    │   • Recent performance       │
                    │   • News calendar            │
                    │   Skills decide everything.  │
                    └─────────────────────────────┘
```

### Mode Selection Logic (AI-Driven, Not Hardcoded)

The MODE SELECTOR AGENT uses these skills to decide:
- `market-regime-classifier` → Trending? Ranging? Volatile?
- `session-profiler` → Which session? Overlap?
- `spread-slippage-cost-analyzer` → Spread tight enough for bullet?
- `risk-calendar-trade-filter` → News coming? Block bullet, allow rapid.
- `trade-psychology-coach` → Recent losing streak? Reduce to rapid only.
- `market-breadth-analyzer` → How many pairs trending? Worth multi-mode?

**Rules the MODE SELECTOR follows:**
```
IF spread > 2 pips AND session != overlap → disable BULLET
IF regime == VOLATILE AND no clear direction → disable BLITZ, BULLET
IF high-impact news in 30 min → disable all modes (blackout)
IF regime == TRENDING AND session == overlap → enable ALL modes
IF recent 3 losses in BULLET → pause BULLET for 1 hour
IF spread < 1 pip AND session == London-NY overlap → BULLET priority
```

### Bullet Mode — Mahmoud's Preferred Style

```
BULLET MODE DETAIL (Nano + Ultra-Nano combined):

Entry Triggers (AI agent decides, not code):
├── TECHNICIAN agent detects:
│   ├── Tick velocity spike (>3 std devs from mean)
│   ├── Bid/ask imbalance (>70% delta)
│   ├── Spread compression (below 0.5x normal)
│   ├── M1 candle momentum (body > 80% of range)
│   └── Volume surge on tick data
│
├── STRATEGIST agent confirms:
│   ├── Direction aligns with M5/M15 structure (BOS/CHoCH)
│   ├── Entry near POC or key S/R level
│   ├── Not fighting HTF trend
│   └── No liquidity trap detected (smart-money-trap-detector)
│
├── RISK OFFICER agent validates:
│   ├── Spread < 30% of TP target
│   ├── No high-impact news in next 30 min
│   ├── Not in cooldown from recent loss
│   ├── Max concurrent bullet positions not exceeded
│   └── Account has sufficient margin
│
├── DEVIL'S ADVOCATE challenges:
│   ├── "Is this just noise? Tick spike with no follow-through"
│   ├── "Spread could widen at any moment"
│   ├── "Last 3 bullets on this pair lost — pattern exhausted?"
│   └── Must be overruled by TECH + STRAT + RISK (3/5)
│
└── HEAD TRADER final call:
    ├── If 3/5 agents agree → EXECUTE
    ├── If 2/5 agree but confidence > 0.90 → EXECUTE with half size
    └── Otherwise → PASS

Exit Rules:
├── Hard TP: 0.5–3 pips (set by STRATEGIST based on S/R distance)
├── Hard SL: 1–2 pips (never widened)
├── Time exit: Auto-close at max hold (15s ultra, 60s nano)
├── No breakeven (too fast)
└── EXECUTOR agent monitors tick-by-tick for exit signals
```

### World Intelligence — Open to Everything

The WORLD INTEL AGENT runs continuously and feeds ALL modes:

```
WORLD INTEL AGENT — Always-On Skills:
├── news-intelligence → Breaking news, headlines, sentiment
├── economic-calendar → Upcoming events, NFP, FOMC, CPI
├── macro-economic-dashboard → DXY, VIX, yields, bonds
├── cross-asset-relationships → Gold vs USD, Oil vs CAD, etc.
├── correlation-crisis → Correlation breakdowns
├── correlation-regime-switcher → Regime shifts across markets
├── institutional-timeline → COT data, institutional flows
├── social-sentiment-scraper → Twitter/Reddit/TradingView sentiment
├── market-breadth-analyzer → How many pairs trending/ranging
├── alternative-data-integrator → Google Trends, shipping, satellite proxies
├── hurst-exponent-dynamics-crisis-prediction → Fractal regime detection
└── volatility-surface-analyzer → IV, vol smile, term structure

Output: WorldBrief (published every 60s to Redis Streams)
├── macro_bias: RISK_ON / RISK_OFF / NEUTRAL
├── dxy_direction: UP / DOWN / FLAT
├── vix_level: LOW / NORMAL / ELEVATED / EXTREME
├── correlation_regime: NORMAL / BREAKING / CRISIS
├── upcoming_events: [{event, impact, minutes_until}]
├── sentiment_composite: -1.0 to 1.0
├── trending_pairs: [symbols with strong direction]
├── ranging_pairs: [symbols in consolidation]
└── avoid_pairs: [symbols with anomalous behavior]
```

### Agent-Skill Interaction Map (Full Transparency)

Every agent has assigned skills. When an agent invokes a skill, the interaction is visible:

```
AGENT: TECHNICIAN
├── technical-analysis       → RSI, MACD, ATR, BB, EMA
├── price-action            → Candle patterns, chart patterns
├── volume-analysis         → Volume profile, order flow, delta
├── market-structure-bos-choch → BOS, CHoCH, swing structure
├── liquidity-analysis      → Order flow, spread, DOM
├── mtf-confluence-scorer   → Multi-timeframe alignment
├── fibonacci-harmonic-wave → Fib levels, harmonics
├── elliott-wave-engine     → Wave counting
├── chart-vision            → AI chart pattern recognition
└── harmonic-pattern-engine → Gartley, Butterfly, Bat, Crab

AGENT: STRATEGIST
├── ict-smart-money         → ICT methodology (OB, FVG, OTE)
├── ict-trading-tool        → Automated ICT scanner
├── smart-money-trap-detector → Fake breakout detection
├── breakout-strategy-engine → Volatility breakout
├── mean-reversion-engine   → Bollinger bounce, RSI fade
├── dan-zanger-breakout-strategy → Dan Zanger system
├── zone-refinement-sniper-entry → S&D zone refinement
├── capitulation-mean-reversion → Lance Breitstein framework
├── poc-bounce-strategy     → Volume Profile POC bounce
├── gap-trading-strategy    → Opening gaps
├── grid-trading-engine     → Systematic grid
├── news-straddle-strategy  → Pre-news straddle
├── cross-asset-arbitrage-engine → Stat arb
├── session-scalping        → Session-based scalping
├── asian-session-scalper   → Tokyo range
├── jdub-price-action-strategy → 3-step PA
├── session-profiler        → Session stats
├── borsellino-10-commandments → Discipline rules
├── strategy-selection      → Meta-routing
├── market-regime-classifier → Which strategy fits this regime
└── intensity_strategies     → Bullet/Blitz/Rapid intensity engine

AGENT: RISK OFFICER
├── risk-and-portfolio      → Position sizing, exposure limits
├── risk-of-ruin            → Kelly criterion, ruin probability
├── drawdown-playbook       → DD tiers, response protocols
├── risk-calendar-trade-filter → Pre-trade safety gate
├── portfolio-optimization  → Markowitz, risk parity, HRP
├── real-time-risk-monitor  → Live tracking, alerts
├── spread-slippage-cost-analyzer → Execution cost check
├── trade-psychology-coach  → Tilt detection, discipline scoring
├── correlation-crisis      → Tail risk, hedge evaluation
└── market-impact-model     → Slippage estimation

AGENT: EXECUTOR
├── execution-algo-trading  → TWAP, VWAP, market, limit
├── market-impact-model     → Order impact estimation
├── tick-data-storage       → Tick persistence
├── trade-journal-analytics → Trade logging, P&L tracking
├── trade-copier-signal-broadcaster → Signal distribution
└── realtime-alert-pipeline → Alert routing

AGENT: WORLD INTEL
├── (22 skills listed above in World Intelligence section)

AGENT: DEVIL'S ADVOCATE
├── Uses same skills as TECHNICIAN + STRATEGIST
├── But asks: "What's the COUNTER-argument?"
├── Specifically invokes:
│   ├── smart-money-trap-detector → "Is this a trap?"
│   ├── correlation-crisis → "Are correlations breaking?"
│   ├── trade-psychology-coach → "Are we on tilt?"
│   └── risk-of-ruin → "Can we survive 5 consecutive losses here?"

AGENT: MODE SELECTOR
├── market-regime-classifier, session-profiler
├── spread-slippage-cost-analyzer, risk-calendar-trade-filter
├── trade-psychology-coach, market-breadth-analyzer
└── Decides: which modes are active right now

AGENT: HEAD TRADER
├── trading-brain → Master orchestration
├── multi-strategy-orchestration → Signal arbitration
├── ai-signal-aggregator → Weighted voting
├── master-trading-workflow → 18-phase workflow
└── trading-autopilot → Full automation
```

---

## Technical Decisions

| Dimension | Decision | Status | Rationale |
|-----------|----------|--------|-----------|
| Language | Python 3.11+ | Confirmed | Async ecosystem, ML libraries |
| Async Runtime | asyncio (stdlib) | Confirmed | No uvloop — Windows compatible, <500ms target met |
| State Store | Redis (hot) + PostgreSQL (cold) | Confirmed | Fast cache + durable storage |
| Market Data | MT5 REST Bridge (primary) | Confirmed | Decouples MT5 from Docker; all symbols, all TFs |
| Broker API | MT5 Bridge REST API | Confirmed | FastAPI on Windows host wrapping MT5 Python API |
| MT5 Bridge | FastAPI + MetaTrader5 | Confirmed | Runs natively on Windows, exposes REST + WebSocket |
| Risk Engine | Custom (fractional risk) | Confirmed | Simple, proven approach |
| Signal Aggregation | Weighted voting + ML meta-model | Confirmed | Transparent, debuggable, adaptive |
| Backtesting | pandas + numpy vectorized | Confirmed | Speed for optimization |
| Container | Docker + docker-compose | Confirmed | Reproducible deployment |
| Monitoring | Prometheus + Grafana | Confirmed | Industry standard |
| Process Manager | systemd (Linux) / NSSM (Windows) | Confirmed | Auto-restart capabilities |
| Skill Orchestration | Smart Skill Router | Confirmed | Dynamic skill selection |
| AI Agent API | REST + WebSocket | Confirmed | Real-time agent communication |

---

## COMPLETE SKILL MAPPING: All 161 Classified Skills by Phase

### Phase 0: Setup & Skill Infrastructure (3 tasks, ~1h)

**Classified Skills Involved (3):**
- `spec-kit` — Spec-driven workflow (02-ai-development/04-spec-driven)
- `smart-skill-router` — Skill routing and auto-selection (04-platform-claude-code/04-workflow-routing)
- `skill-execution-governor` — MANDATORY meta-skill governing all skill interactions (04-platform-claude-code/03-automation-governance)

```
T001: Project Scaffold
├── Create directory structure
├── Initialize Python project (pyproject.toml)
├── Set up virtual environment
└── Skill Integration:
    ├── Copy skill-router.py from skills ecosystem
    ├── Import skills_index.json (265+ skills indexed)
    ├── Import skills_graph.json (dependency chains)
    └── Create skill_invoker.py (wraps all skill calls)

T002: Configuration System
├── config/default.yaml (constitution.md tech stack)
├── config/paper.yaml (paper trading overrides)
├── config/live.yaml (live trading overrides)
└── Skill Config Loader:
    ├── Load skill-specific configs from SKILL.md frontmatter
    ├── Merge with user overrides
    └── Validate against skill requirements

T003: Event Bus Foundation
├── Redis Streams setup
├── Event type definitions
└── Skill Event Emitter:
    ├── Publish skill execution events
    ├── Subscribe to skill output topics
    └── Skill invocation logging
```

### Phase 1: Core Infrastructure (4 tasks, ~6.5h)

**Classified Skills Involved (5):**
- `trading-brain` — Master orchestrator (01-trading/13-orchestration/02-trading-brain)
- `pro-code-architecture` — Senior-level architecture (03-software-engineering/01-architecture)
- `generate-snapshot` — Codebase health tracking (03-software-engineering/02-code-review-quality)
- `skill-execution-governor` — Quality gates (04-platform-claude-code/03-automation-governance)
- `system-design-academy` — Real-world design patterns (03-software-engineering/01-architecture)

```
T010: Trading Brain Core
├── Implement TradingBrain class (trading-brain/SKILL.md)
│   ├── Layer 1: analyze_market() → MarketState
│   ├── Layer 2: select_strategy() → list[Strategy]
│   ├── Layer 3: generate_signals() → list[Signal]
│   ├── Layer 4: aggregate_signals() → FinalSignal
│   ├── Layer 5: validate_risk() → RiskApproval
│   ├── Layer 6: execute() → TradeResult
│   └── Layer 7: learn() → LearningUpdate
└── Skill Bridges:
    ├── SkillBridge.invoke_skill() — call any skill by name
    ├── SkillResultCollector — aggregate skill outputs
    └── SkillHealthMonitor — track skill performance

T011: State Manager (Redis)
├── State persistence
├── State recovery (< 30s)
└── Skill State Cache:
    ├── Cache skill outputs
    ├── Cache skill dependencies
    └── Cache skill execution history

T012: Event Bus (Redis Streams — durable delivery)
├── Event definitions
├── Consumer groups with acknowledgment
└── Skill Event Channels:
    ├── skill:invoked — track all skill calls
    ├── skill:result — capture skill outputs
    ├── skill:error — skill failure notifications
    └── skill:health — skill health status

T013: Logging System
├── Structured JSON logging
├── Skill execution logging
└── Skill Audit Trail:
    ├── Log every skill invocation
    ├── Log skill parameters
    ├── Log skill outputs
    └── Log skill performance metrics
```

### Phase 2: Data Layer (5 tasks, ~12h)

**Classified Skills Involved (5):**
- `market-data-ingestion` — MT5 data fetching (01-trading/07-data-signals/01-market-data-ingestion)
- `tick-data-storage` — Tick persistence (01-trading/06-execution/04-tick-data)
- `mt5-integration` — MT5 Python API (01-trading/08-mt5-platform/01-integration)
- `mt5-chart-browser` — Chart browsing (01-trading/08-mt5-platform/02-chart-browser)
- `market-regime-classifier` — Regime detection (01-trading/04-market-context/01-regime-classification)

**ARCHITECTURE CHANGE: MT5 REST Bridge**

The MetaTrader5 Python package only runs on Windows. Instead of coupling
the trading system directly to MT5, we introduce a **separate FastAPI
service** (the "MT5 Bridge") that runs natively on the Windows host
alongside the MT5 terminal. The main trading system communicates with it
over HTTP/WebSocket.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     WINDOWS HOST                                     │
│                                                                       │
│  ┌──────────────┐        ┌──────────────────────────────────────┐   │
│  │  MT5 Terminal │◄──────▶│  MT5 REST Bridge (FastAPI)           │   │
│  │  (native)     │  MT5   │  ├── GET  /symbols                  │   │
│  └──────────────┘  Python │  ├── GET  /ohlcv/{symbol}/{tf}      │   │
│                    API    │  ├── GET  /ticks/{symbol}            │   │
│                           │  ├── GET  /account                  │   │
│                           │  ├── POST /order                    │   │
│                           │  ├── GET  /positions                │   │
│                           │  ├── DELETE /position/{ticket}      │   │
│                           │  ├── WS   /ws/ticks                 │   │
│                           │  └── WS   /ws/bars                  │   │
│                           │  Port: 8510 (configurable)          │   │
│                           └──────────────────────────────────────┘   │
│                                      │ HTTP / WebSocket              │
│  ┌───────────────────────────────────┼──────────────────────────┐   │
│  │        TRADING SYSTEM (Docker or native)                      │   │
│  │  src/data/mt5_bridge_client.py ◄──┘                          │   │
│  │  ├── async fetch_ohlcv(symbol, tf, bars)                     │   │
│  │  ├── async fetch_ticks(symbol)                               │   │
│  │  ├── async subscribe_ticks(symbols, callback)  # WebSocket   │   │
│  │  ├── async place_order(request) → OrderResult                │   │
│  │  ├── async get_positions() → list[Position]                  │   │
│  │  ├── async close_position(ticket) → CloseResult              │   │
│  │  └── async get_account() → AccountInfo                       │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

**MT5 Bridge REST API Spec:**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/symbols` | GET | List all available symbols from MT5 |
| `/ohlcv/{symbol}/{timeframe}` | GET | Fetch OHLCV bars (params: bars, start, end) |
| `/ticks/{symbol}` | GET | Fetch recent ticks |
| `/account` | GET | Account balance, equity, margin |
| `/order` | POST | Place market/limit/stop order |
| `/positions` | GET | List open positions |
| `/position/{ticket}` | DELETE | Close specific position |
| `/positions/close-all` | POST | Emergency close all |
| `/ws/ticks` | WebSocket | Real-time tick stream (multi-symbol) |
| `/ws/bars` | WebSocket | Real-time bar completion stream |

**Supported Symbols:** ALL symbols available on the MT5 demo account
**Supported Timeframes:** M1, M5, M15, M30, H1, H4, D1, W1, MN1

```
T019: MT5 REST Bridge Service (NEW — runs on Windows host)
├── FastAPI application (mt5_bridge/)
│   ├── app.py — main FastAPI app
│   ├── mt5_connector.py — MetaTrader5 Python API wrapper
│   ├── routes/
│   │   ├── market_data.py — /symbols, /ohlcv, /ticks
│   │   ├── trading.py — /order, /positions, /position/{ticket}
│   │   └── account.py — /account
│   ├── websocket/
│   │   ├── tick_stream.py — /ws/ticks (multi-symbol subscription)
│   │   └── bar_stream.py — /ws/bars (bar completion events)
│   └── models.py — Pydantic request/response models
├── Health check endpoint (/health)
├── Bearer token authentication (ATS_BRIDGE_API_KEY env var)
├── Auto-reconnect to MT5 on disconnect
├── Rate limiting (respect MT5 API limits)
└── NSSM service wrapper for auto-start

T020: MT5 Bridge Client (replaces direct MT5 integration)
├── src/data/mt5_bridge_client.py
│   ├── Async HTTP client (httpx/aiohttp)
│   ├── WebSocket tick subscription
│   ├── Connection pooling + retry logic
│   ├── Circuit breaker on bridge failure
│   └── Fallback to yFinance on bridge down
├── Publish ticks to Redis event bus
└── All symbols, all timeframes

T021: Tick Storage (tick-data-storage)
├── Real-time tick capture from bridge WebSocket
├── Tick compression (OHLCV aggregation)
├── Redis hot storage
└── PostgreSQL cold storage

T022: OHLCV Cache (ohlcv-cache)
├── Multi-timeframe caching (M1→MN1)
├── Query optimization
└── Backfill capability via bridge REST

T023: Regime Classifier (market-regime-classifier)
├── ML-powered regime detection
├── RegimeType: TRENDING, RANGING, VOLATILE
├── Feature extraction:
│   ├── Volatility profile
│   ├── Trend strength
│   ├── Volume patterns
│   └── Price structure
├── Per-symbol regime tracking
└── Real-time classification
```

### Phase 3: Analysis Layer (4 tasks, ~9h)

**Classified Skills Involved (12):**
- `technical-analysis` — Indicators, oscillators (01-trading/02-analysis/01-technical-analysis/03-indicators-volume)
- `price-action` — Candlestick patterns (01-trading/02-analysis/01-technical-analysis/01-price-action)
- `volume-analysis` — Volume Profile, Order Flow (01-trading/02-analysis/01-technical-analysis/03-indicators-volume)
- `market-structure-bos-choch` — BOS/CHoCH (01-trading/03-strategies/01-ict-smart-money)
- `liquidity-analysis` — Order flow, pools (01-trading/03-strategies/01-ict-smart-money)
- `chart-vision` — AI chart recognition (01-trading/02-analysis/03-chart-vision-ai)
- `elliott-wave-engine` — Wave counting (01-trading/02-analysis/01-technical-analysis/02-chart-patterns-advanced)
- `fibonacci-harmonic-wave` — Fib levels (01-trading/02-analysis/01-technical-analysis/02-chart-patterns-advanced)
- `harmonic-pattern-engine` — Harmonic patterns (01-trading/02-analysis/01-technical-analysis/02-chart-patterns-advanced)
- `fundamental-analysis` — Fundamentals (01-trading/02-analysis/02-fundamental-analysis)
- `market-intelligence` — Aggregate intelligence (01-trading/07-data-signals/05-news-intelligence)
- `mtf-confluence-scorer` — MTF alignment (01-trading/02-analysis/01-technical-analysis/04-multi-timeframe)

```
T030: Technical Indicators (technical-analysis subset)
├── Indicator calculations
├── Supported indicators:
│   ├── RSI, MACD, ATR
│   ├── Bollinger Bands
│   ├── Moving Averages (SMA, EMA)
│   ├── Volume indicators
│   └── Custom indicators
└── Multi-timeframe support

T031: Liquidity Analysis (liquidity-analysis subset)
├── Order flow analysis
├── Spread analysis
├── Depth of market
└── Liquidity scoring

T032: Market Structure (market-structure-bos-choch subset)
├── Break of Structure (BOS)
├── Change of Character (CHoCH)
├── Higher highs/lows tracking
└── Support/resistance levels

T033: Market Intelligence (market-intelligence)
├── News sentiment NLP
├── Economic calendar
├── Session timing
├── Seasonality analyzer
└── Institutional positioning
```

### Phase 4: Strategy Layer (5 tasks, ~11h)

**Classified Skills Involved (24):**

**ICT/SMC Strategies (6):**
- `ict-smart-money` — Complete ICT methodology (01-trading/03-strategies/01-ict-smart-money)
- `ict-trading-tool` — MT5 ICT automation (01-trading/03-strategies/01-ict-smart-money)
- `market-structure-bos-choch` — BOS/CHoCH (01-trading/03-strategies/01-ict-smart-money)
- `smart-money-trap-detector` — Fake breakout detection (01-trading/03-strategies/01-ict-smart-money)
- `smc-beginner-pro-guide` — SMC framework (01-trading/03-strategies/01-ict-smart-money)
- `smc-python-library` — Python SMC implementation (01-trading/03-strategies/01-ict-smart-money)

**Breakout Strategies (3):**
- `breakout-strategy-engine` — Volatility breakout (01-trading/03-strategies/02-breakout)
- `dan-zanger-breakout-strategy` — 1000%+ system (01-trading/03-strategies/02-breakout)
- `zone-refinement-sniper-entry` — S&D zones (01-trading/03-strategies/02-breakout)

**Mean Reversion (3):**
- `mean-reversion-engine` — Bollinger bounce (01-trading/03-strategies/03-mean-reversion)
- `capitulation-mean-reversion` — $100M+ framework (01-trading/03-strategies/03-mean-reversion)
- `poc-bounce-strategy` — Volume Profile POC (01-trading/03-strategies/03-mean-reversion)

**Session-Based (4):**
- `asian-session-scalper` — Tokyo range (01-trading/03-strategies/04-session-based)
- `jdub-price-action-strategy` — 3-step PA (01-trading/03-strategies/04-session-based)
- `session-profiler` — Session stats (01-trading/03-strategies/04-session-based)
- `session-scalping` — Time-based scalping (01-trading/03-strategies/04-session-based)

**Other Strategies (8):**
- `gap-trading-strategy` — Opening gaps (01-trading/03-strategies/05-gap-trading)
- `grid-trading-engine` — Systematic grid (01-trading/03-strategies/06-grid-systematic)
- `news-straddle-strategy` — Pre-news straddle (01-trading/03-strategies/07-news-event)
- `cross-asset-arbitrage-engine` — Statistical/triangular arb (01-trading/03-strategies/08-arbitrage)
- `borsellino-10-commandments` — Discipline rules (01-trading/03-strategies/09-named-strategies)

```
T040: Base Strategy Interface
├── Abstract base class
├── Signal generation protocol
├── Position sizing hooks
└── Skill registration system

T041: Breakout Strategy (breakout-strategy-engine)
├── Volatility squeeze detection
├── Donchian channel breakout
├── ATR-based entries
└── Killzone alignment

T042: Mean Reversion Strategy (mean-reversion-engine)
├── Bollinger Band fade
├── RSI extreme entries
├── Support/resistance bounces
└── Capitulation detection

T043: ICT SMC Strategy (ict-smart-money-complete)
├── Order Block detection
├── Fair Value Gap (FVG) scanning
├── Premium/Discount zones
├── Liquidity sweeps
└── Optimal Trade Entry (OTE)

T044: Session Scalper (session-scalping)
├── Tokyo session range trades
├── London open breakout
├── NY open volatility
└── Session overlap plays

T045: Trading Intensity Strategy Engine
├── 3 trading intensity modes with distinct parameters:
│
│   ┌──────────────────────────────────────────────────────────────────┐
│   │ Mode    │ Timeframe │ Hold Time    │ TP (pips) │ SL (pips)     │
│   │─────────┼───────────┼──────────────┼───────────┼───────────────│
│   │ BULLET  │ Tick/M1   │ 1s–60s       │ 0.5–3     │ 1–2           │
│   │ BLITZ   │ M1/M5     │ 30s–15 min   │ 3–15      │ 3–5           │
│   │ RAPID   │ M15/H1+   │ 15 min–4h+   │ 15–100+   │ 10–50         │
│   └──────────────────────────────────────────────────────────────────┘
│   Risk % per trade: user-configurable in settings (NOT per mode)
│
├── Per-mode configuration:
│   ├── Timeframe selection (analysis + entry)
│   ├── Max hold duration (auto-close if exceeded)
│   ├── TP/SL pip targets (tighter for faster intensities)
│   ├── Max concurrent positions per mode
│   ├── Min spread threshold (reject if spread > TP target)
│   └── Cooldown between trades (shorter for faster intensities)
│
├── Entry triggers by intensity:
│   ├── BULLET: Tick velocity spike + bid/ask imbalance + spread compression
│   ├── BLITZ: M1 candle patterns + momentum + order flow delta + S/R
│   └── RAPID: M15/H1 structure + HTF confluence + regime alignment
│
├── Exit rules by intensity:
│   ├── All: Hard SL/TP (never widen SL)
│   ├── BULLET: Time exit at 60s, no breakeven (too fast)
│   ├── BLITZ: Time exit at 15 min, breakeven at 50% TP
│   └── RAPID: Standard SL/TP management, trailing stop optional
│
├── Spread guard (CRITICAL for Bullet/Blitz):
│   ├── Reject if current_spread > max(mode_tp_target * 0.3, 1 pip)
│   ├── Monitor spread in real-time, pause mode if spread widens
│   └── Auto-resume when spread normalizes
│
├── Session filter per intensity:
│   ├── BULLET: London-NY overlap 13:00–16:00 UTC only
│   ├── BLITZ: London + NY sessions
│   └── RAPID: All sessions
│
└── Mode selection by MODE SELECTOR agent (AI-driven):
    ├── Uses skills + conditions, not hardcoded rules
    ├── All 3 can run simultaneously on different symbols
    └── Auto-pause after 3 consecutive losses (1h cooldown)
```

### Phase 5: Signal Layer (4 tasks, ~7h)

**Classified Skills Involved (3):**
- `ai-signal-aggregator` — ML-powered signal combination (01-trading/07-data-signals/06-signal-aggregation)
- `multi-strategy-orchestration` — Signal arbitration pipeline (01-trading/13-orchestration/05-multi-strategy)
- `strategy-selection` — Meta-skill for strategy routing (01-trading/13-orchestration/04-strategy-selection)

```
T050: Signal Generator
├── Individual signal creation
├── Signal metadata:
│   ├── Strategy source
│   ├── Confidence score
│   ├── Confluence factors
│   └── Risk parameters
└── Signal validation

T051: Signal Aggregator (ai-signal-aggregator)
├── Confluence Scoring (Tier 1: Weighted Linear):
│   ├── 10 factors with continuous inputs (0.0–1.0)
│   ├── Weights (sum to 1.0):
│   │   ├── htf_trend:        0.20  (strongest predictor)
│   │   ├── regime_match:     0.15
│   │   ├── mtf_agreement:    0.12
│   │   ├── sr_proximity:     0.12
│   │   ├── volume_confirm:   0.10
│   │   ├── momentum_align:   0.08
│   │   ├── news_clear:       0.08  (HARD GATE — reject if < 0.5)
│   │   ├── session_quality:  0.05
│   │   ├── spread_normal:    0.05  (HARD GATE — reject if < 0.5)
│   │   └── no_losing_streak: 0.05
│   ├── Thresholds:
│   │   ├── < 0.60 → NO TRADE
│   │   ├── 0.60–0.80 → scaled position (25%–100%)
│   │   └── > 0.80 → full position size
│   └── Hard gates: news_clear + spread_normal must pass before scoring
├── Confidence Scoring:
│   ├── Per-strategy confidence = weighted ratio of conditions met
│   ├── Each condition has an importance weight (from backtest IC)
│   ├── confidence = sum(met_i * weight_i) / sum(weight_i)
│   └── Range: 0.0–1.0
├── Consensus Rules:
│   ├── Min 2/3 strategies must agree on direction
│   ├── Single strategy OK if confidence > 0.85 AND confluence > 0.70
│   └── Conflicting long/short = NO TRADE
├── Walk-forward weight optimization (future: Tier 2/3 upgrade)
└── Final signal output with full factor breakdown for journaling

T052: Signal Arbitration (multi-strategy-orchestration)
├── Consensus rules:
│   ├── Minimum 2 of 3 strategies must agree
│   ├── Single strategy OK if confidence > 0.85 AND confluence > 7/10
│   ├── Conflicting long/short signals = NO TRADE
│   └── Correlated pair filtering
├── Conflict resolution:
│   ├── HTF wins rule
│   ├── Higher confluence wins
│   └── Equal signals = no trade
├── Priority ranking:
│   ├── Multi-strategy confluence (3+)
│   ├── HTF-aligned + high confluence
│   ├── Killzone-aligned signals
│   └── Single strategy entries
└── Capital allocation per strategy

T053: Signal History
├── Complete audit log
├── Signal-to-trade tracking
├── Performance attribution
└── Learning feedback
```

### Phase 6: Risk Layer (5 tasks, ~9.5h)

**Classified Skills Involved (8):**
- `risk-and-portfolio` — Complete risk framework (01-trading/05-risk-management/04-portfolio-construction)
- `risk-of-ruin` — Risk of Ruin, Kelly Criterion (01-trading/05-risk-management/01-position-sizing-ruin)
- `drawdown-playbook` — DD taxonomy, response protocols (01-trading/05-risk-management/02-drawdown-management)
- `risk-calendar-trade-filter` — Pre-trade safety gate (01-trading/05-risk-management/03-trade-filters)
- `portfolio-optimization` — Portfolio construction (01-trading/05-risk-management/04-portfolio-construction)
- `real-time-risk-monitor` — Live portfolio tracking (01-trading/05-risk-management/05-risk-monitoring)

```
T060: Position Sizer (risk-and-portfolio)
├── Fractional risk calculation:
│   ├── User-configurable risk % in settings (default 2%)
│   ├── Same risk % applies to ALL modes (scalping modes differ by TP/SL pips, not risk %)
│   ├── ATR-based stops (non-scalping)
│   ├── Fixed pip stops (scalping modes — from ScalpingModeConfig)
│   ├── Volatility-adjusted size
│   └── Kelly criterion (optional)
├── Position limits:
│   ├── Max 3 positions per symbol (non-scalping)
│   ├── Max concurrent per scalping mode (from config)
│   ├── Max 6% total exposure
│   └── Correlation clustering
└── Sizing output: quantity, SL, TP

T061: Risk Filter (risk-calendar-trade-filter)
├── Pre-trade safety gate
├── News blacklist:
│   ├── High-impact events (±30 min)
│   ├── ECB, FOMC, NFP, CPI
│   ├── Earnings season
│   └── Geopolitical events
├── Session filter:
│   ├── Approved trading hours
│   ├── Spread thresholds
│   ├── Liquidity requirements
│   └── Volatility limits
└── Kill switch integration

T062: Portfolio Monitor (real-time-risk-monitor)
├── Real-time P&L tracking
├── Exposure dashboard:
│   ├── By asset class
│   ├── By direction
│   ├── By correlation cluster
│   └── By strategy
├── Drawdown tracker
└── Margin utilization

T063: Drawdown Tracker (drawdown-playbook)
├── Peak equity tracking
├── Drawdown duration
├── Drawdown severity classification
├── Logging only (demo account — no enforcement)
└── Configurable enforcement (re-enable for live):
    ├── 3% DD — reduce size 25%     [DEMO: log only]
    ├── 5% DD — reduce size 50%     [DEMO: log only]
    ├── 10% DD — minimum size only  [DEMO: log only]
    └── 15% DD — KILL SWITCH        [DEMO: log only]

T064: Kill Switch (real-time-risk-monitor + kill-switch)
├── Emergency shutdown:
│   ├── Manual trigger (< 1 second)
│   ├── Scalping-aware: POST /positions/close-all uses asyncio.gather
│   │   for parallel closure of all positions (handles 10+ rapid scalp positions)
│   ├── Auto trigger on drawdown > 15%  [DEMO: disabled]
│   ├── Auto trigger on margin < 150%
│   └── Auto trigger on daily loss > 5% [DEMO: disabled]
├── Position closure:
│   ├── Close all positions
│   ├── Cancel pending orders
│   └── Lock trading (configurable duration)
└── Notification system
```

### Phase 7: Execution Layer (4 tasks, ~8.5h)

**Classified Skills Involved (8):**
- `execution-algo-trading` — TWAP, VWAP, IS, POV algorithms (01-trading/06-execution/01-algo-execution)
- `market-impact-model` — Order impact estimation (01-trading/06-execution/01-algo-execution)
- `market-making-hft` — Market making, HFT strategies (01-trading/06-execution/02-market-making-hft)
- `spread-slippage-cost-analyzer` — Execution cost analysis (01-trading/06-execution/03-spread-slippage)
- `tick-data-storage` — Tick capture/persistence (01-trading/06-execution/04-tick-data)
- `hedgequantx-prop-trading` — Prop firm futures trading (01-trading/06-execution/05-prop-trading)

```
T070: Order Router (execution-algo-trading)
├── Order submission via MT5 Bridge REST API (POST /order)
├── Execution algorithms:
│   ├── Market orders (immediate)
│   ├── Limit orders (pullback entries)
│   ├── Stop orders (breakout entries)
│   └── Iceberg orders (large size)
├── Slippage analysis
└── Transaction cost analysis (TCA)

T071: SL/TP Manager
├── Automatic stop-loss placement
├── Take-profit levels:
│   ├── Risk:reward ratio (min 1:2)
│   ├── Partial TP levels
│   └── Trailing stop (optional)
├── Breakeven trigger
└── Position management

T072: Execution Reporter
├── Fill confirmation
├── Slippage measurement
├── Execution quality score
└── Trade logging

T073: Position Tracker
├── Open position state
├── Real-time P&L
├── Time in trade
└── Exit reason tracking
```

### Phase 8: Monitoring Layer (4 tasks, ~8h)

**Classified Skills Involved (7):**
- `realtime-alert-pipeline` — Condition monitoring, alerts (01-trading/12-infrastructure/01-alerts-notifications)
- `discord-webhook` — Discord alert integration (01-trading/12-infrastructure/02-discord-telegram)
- `telegram-bot` — Telegram notifications (01-trading/12-infrastructure/02-discord-telegram)
- `skill-analytics` — Skill usage/performance tracking (04-platform-claude-code/02-skill-management)
- `skill-doctor` — Skill health diagnostics (04-platform-claude-code/02-skill-management)
- `generate-snapshot` — Codebase health checks (03-software-engineering/02-code-review-quality)
- `run-smoke-tests` — Smoke test suite (03-software-engineering/03-testing)

```
T080: Metrics Collector (Prometheus)
├── System metrics:
│   ├── Uptime
│   ├── Latency (tick to signal)
│   ├── Memory/CPU usage
│   └── Event queue depth
├── Trading metrics:
│   ├── Trades per hour
│   ├── Win rate
│   ├── Profit factor
│   ├── Current drawdown
│   └── Exposure %
├── Skill metrics:
│   ├── Skill invocation count
│   ├── Skill success rate
│   ├── Skill latency
│   └── Skill output quality
└── Custom metrics

T081: Health Check
├── Component health
├── Dependency health
├── MT5 connection status
├── Redis connection status
├── PostgreSQL connection status
└── Skill health dashboard

T082: Alert Manager (realtime-alert-pipeline)
├── Multi-channel alerts:
│   ├── Console (ASCII dashboard)
│   ├── Telegram bot
│   ├── Discord webhook
│   └── Email (digest)
├── Alert conditions:
│   ├── Risk threshold breaches
│   ├── System errors
│   ├── Skill failures
│   └── Trading anomalies
└── Alert throttling

T083: Dashboard (CLI + Web)
├── Rich/textual terminal UI
├── Real-time updates
├── Sections:
│   ├── Account summary
│   ├── Open positions
│   ├── Today's P&L
│   ├── Active signals
│   ├── Skill status
│   └── System health
└── Color-coded status
```

### Phase 9: Backtest Layer (3 tasks, ~9h) — P2

**Classified Skills Involved (9):**
- `backtesting-sim` — Vectorized backtesting (01-trading/09-quant-ml/01-backtesting)
- `backtest-report-generator` — Publication-quality reports (01-trading/09-quant-ml/01-backtesting)
- `strategy-genetic-optimizer` — Evolutionary optimization (01-trading/09-quant-ml/04-genetic-optimization)
- `strategy-validation` — Out-of-sample validation (01-trading/09-quant-ml/06-strategy-validation)
- `ml-trading` — Supervised ML for trading (01-trading/09-quant-ml/02-ml-models)
- `quant-ml-trading` — Complete quant/ML toolkit (01-trading/09-quant-ml/02-ml-models)
- `tensortrade-rl` — RL trading framework (01-trading/09-quant-ml/03-reinforcement-learning)
- `trading-gym-rl-env` — OpenAI Gym trading env (01-trading/09-quant-ml/03-reinforcement-learning)
- `statistics-timeseries` — Time series modeling (01-trading/09-quant-ml/05-statistics-timeseries)

```
T090: Backtest Engine (backtesting-sim)
├── Vectorized backtesting
├── Multi-strategy support
├── Walk-forward optimization
├── Performance metrics:
│   ├── Total return
│   ├── Sharpe ratio
│   ├── Sortino ratio
│   ├── Calmar ratio
│   ├── Maximum drawdown
│   ├── Win rate
│   └── Profit factor
└── Report generation

T091: Strategy Validation (strategy-validation)
├── Out-of-sample testing
├── Cross-validation
├── Parameter stability
├── Regime-specific performance
└── Tearsheet generation

T092: Genetic Optimizer (strategy-genetic-optimizer)
├── Evolutionary algorithm:
│   ├── Gene encoding (strategy parameters)
│   ├── Fitness functions (Sharpe, Sortino, Calmar)
│   ├── Population management (50 individuals)
│   ├── Selection (tournament)
│   ├── Crossover (uniform)
│   └── Mutation (Gaussian)
├── Anti-overfitting:
│   ├── Walk-forward validation
│   ├── Diversity enforcement
│   └── Complexity penalty
└── Optimal parameter discovery
```

### Phase 10: Integration (2 tasks, ~5h)

**Classified Skills Involved (11):**
- `agent-development` — Create Claude Code agents (04-platform-claude-code/01-plugin-development)
- `ai-agent-builder` — AI-powered coding agents (02-ai-development/01-agent-building)
- `deepagents-langchain` — LangChain agent framework (02-ai-development/01-agent-building)
- `agentic-storage` — Persistent agent memory (02-ai-development/01-agent-building)
- `trading-brain` — Master orchestrator (01-trading/13-orchestration/02-trading-brain)
- `trading-autopilot` — Full orchestration meta-skill (01-trading/13-orchestration/03-autopilot)
- `analyze` — Instant full trading analysis (01-trading/13-orchestration/01-master-workflow)
- `master-trading-workflow` — 18-phase workflow (01-trading/13-orchestration/01-master-workflow)
- `xtrading-analyze` — Extended analysis (01-trading/13-orchestration/01-master-workflow)
- `ai-trading-crew` — 50-agent AutoGen system (01-trading/10-ai-trading-agents/01-multi-agent-frameworks)
- `autohedge-swarm` — Auto-hedge swarm (01-trading/10-ai-trading-agents/01-multi-agent-frameworks)
- `trading-agents-llm` — Multi-agent LLM framework (01-trading/10-ai-trading-agents/01-multi-agent-frameworks)
- `freqtrade-bot` — Open-source crypto bot (01-trading/10-ai-trading-agents/02-autonomous-agents)
- `openalice-trading-agent` — File-driven autonomous agent (01-trading/10-ai-trading-agents/02-autonomous-agents)
- `ritmex-crypto-agent` — Binance research platform (01-trading/10-ai-trading-agents/02-autonomous-agents)
- `polymarket-prediction-agents` — Prediction market agents (01-trading/10-ai-trading-agents/03-prediction-markets)

```
T100: End-to-End Integration
├── Full pipeline test
├── Skill chain validation
├── Event flow testing
├── Risk gate testing
└── Recovery testing

T101: AI Agent API/CLI
├── REST API endpoints:
│   ├── POST /api/v1/agent/invoke-skill
│   ├── POST /api/v1/agent/skill-status
│   ├── GET /api/v1/agent/skill-outputs
│   ├── POST /api/v1/control/start
│   ├── POST /api/v1/control/stop
│   └── POST /api/v1/control/emergency-stop
├── WebSocket streams:
│   ├── /ws/skill-output — real-time skill results
│   ├── /ws/market-data — live market updates
│   ├── /ws/signals — new trading signals
│   └── /ws/positions — position updates
└── CLI interface:
    ├── ats invoke <skill> <params>
    ├── ats status
    ├── ats skills list
    ├── ats skills outputs <skill>
    └── ats monitor
```

### Phase 11: Documentation & DevOps (2 tasks, ~5h)

**Classified Skills Involved (15):**
- `e2b-sandboxes` — Code execution sandboxes (03-software-engineering/05-dev-tools)
- `git-phase-restore` — Git phase restoration (03-software-engineering/05-dev-tools)
- `github-actions-trigger` — Trigger GitHub Actions (03-software-engineering/05-dev-tools)
- `httpie-cli` — Human-friendly HTTP CLI (03-software-engineering/05-dev-tools)
- `ip-rotation` — Proxy rotation (03-software-engineering/05-dev-tools)
- `python-manager-discovery` — Python environment detection (03-software-engineering/05-dev-tools)
- `debug-failing-test` — Iterative test debugging (03-software-engineering/03-testing)
- `run-e2e-tests` — End-to-end workflow tests (03-software-engineering/03-testing)
- `run-integration-tests` — Component integration tests (03-software-engineering/03-testing)
- `run-pre-commit-checks` — Pre-commit validation (03-software-engineering/03-testing)
- `code-review` — CodeRabbit AI review (03-software-engineering/02-code-review-quality)
- `pro-code-architecture` — Senior-level architecture (03-software-engineering/01-architecture)
- `system-design-academy` — Real-world system design (03-software-engineering/01-architecture)
- `build-your-own-x` — Build tech from scratch (03-software-engineering/01-architecture)
- `interactive-coding-challenges` — 120+ Jupyter challenges (03-software-engineering/06-learning)

```
T110: System Documentation
├── Architecture diagrams
├── Skill integration guide
├── API documentation
└── Deployment guide

T111: User Documentation
├── Installation guide
├── Configuration reference
├── Operation manual
└── Troubleshooting guide
```

---

## Continuous Monitoring Architecture

### Skill Output Monitoring Dashboard

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SKILL EXECUTION MONITOR                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ACTIVE SKILLS (56 total super-skills mapped)                           │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ Skill                    │ Status │ Calls/min │ Avg Lat │ Last Out │ │
│  │─────────────────────────┼────────┼───────────┼──────────┼──────────│ │
│  │ trading-brain           │ RUNNING │ 0.1       │ 150ms   │ OK       │ │
│  │ market-analysis         │ RUNNING │ 10.5      │ 45ms    │ OK       │ │
│  │ regime-classifier       │ RUNNING │ 0.5       │ 80ms    │ RANGING  │ │
│  │ technical-analysis      │ RUNNING │ 15.2      │ 12ms    │ OK       │ │
│  │ ict-smc                 │ RUNNING │ 8.3       │ 95ms    │ OB_DETECTED│ │
│  │ breakout-strategy       │ RUNNING │ 2.1       │ 35ms    │ NO_SIGNAL│ │
│  │ mean-reversion          │ RUNNING │ 2.1       │ 28ms    │ NO_SIGNAL│ │
│  │ signal-aggregator       │ IDLE    │ 0.0       │ —       │ —        │ │
│  │ risk-filter             │ RUNNING │ 1.5       │ 15ms    │ ALLOW    │ │
│  │ execution-algo          │ IDLE    │ 0.0       │ —       │ —        │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  AGENT STATUS                                                             │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ Agent           │ State    │ Queue │ Errors │ Last Heartbeat       │ │
│  │─────────────────┼──────────┼───────┼────────┼──────────────────────│ │
│  │ orchestrator    │ ACTIVE   │ 0     │ 0      │ 2026-03-19 14:32:15  │ │
│  │ data-feed       │ ACTIVE   │ 125   │ 0      │ 2026-03-19 14:32:15  │ │
│  │ signal-scanner  │ ACTIVE   │ 3     │ 0      │ 2026-03-19 14:32:14  │ │
│  │ risk-manager    │ ACTIVE   │ 0     │ 0      │ 2026-03-19 14:32:15  │ │
│  │ executor        │ ACTIVE   │ 0     │ 0      │ 2026-03-19 14:32:15  │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                          │
│  SYSTEM HEALTH                                                            │
│  ├─ Uptime: 3d 14h 32m                                                  │
│  ├─ Memory: 458 MB / 2 GB                                               │
│  ├─ CPU: 12%                                                            │
│  ├─ Redis: CONNECTED (latency: 2ms)                                     │
│  ├─ PostgreSQL: CONNECTED (latency: 8ms)                                │
│  ├─ MT5: CONNECTED (ticks/sec: 125)                                     │
│  └─ Events/min: 1,250                                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Skill Output Event Stream

```python
# All skill outputs are published to Redis channels

class SkillOutputMonitor:
    """Monitors all skill executions in real-time."""

    CHANNELS = {
        "skill:invoked": "Every skill call",
        "skill:result": "Successful skill output",
        "skill:error": "Skill failure",
        "skill:latency": "Skill execution time",
        "skill:health": "Skill health status",
    }

    async def monitor_skill_outputs(self):
        """Subscribe to all skill output streams (Redis Streams)."""
        # Create consumer group for each channel
        for channel in self.CHANNELS:
            await self.redis.xgroup_create(channel, "monitor", mkstream=True)

        while True:
            entries = await self.redis.xreadgroup(
                "monitor", "monitor-1", {ch: ">" for ch in self.CHANNELS}, block=1000
            )
            for stream, messages in entries:
                for msg_id, data in messages:
                    await self.process_skill_event(stream, data)
                    await self.redis.xack(stream, "monitor", msg_id)

    async def process_skill_event(self, message):
        """Process and log skill events."""
        data = json.loads(message['data'])

        # Log to file
        self.skill_logger.log(
            skill=data['skill'],
            event=message['channel'],
            timestamp=data['timestamp'],
            data=data
        )

        # Update dashboard
        await self.dashboard.update_skill_status(data)

        # Check for alerts
        if self.should_alert(data):
            await self.alert_manager.send(data)
```

---

## AI Agent API/CLI Integration

### REST API Endpoints

```python
# FastAPI application for external AI agent communication

from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

app = FastAPI(title="Auto-Trading System Agent API")

class SkillInvocationRequest(BaseModel):
    skill: str
    parameters: dict
    priority: int = 5  # 1-10, 1 = highest

class SkillInvocationResponse(BaseModel):
    skill_id: str
    status: str  # queued, running, completed, failed
    result: Optional[dict]
    error: Optional[str]
    execution_time_ms: int

# Invoke any skill by name
@app.post("/api/v1/agent/invoke-skill", response_model=SkillInvocationResponse)
async def invoke_skill(request: SkillInvocationRequest):
    """
    Invoke a trading skill and return its output.

    Example:
        POST /api/v1/agent/invoke-skill
        {
            "skill": "market-regime-classifier",
            "parameters": {
                "symbol": "XAUUSD",
                "timeframe": "H1"
            }
        }
    """
    result = await skill_bridge.invoke_skill(
        skill_name=request.skill,
        params=request.parameters
    )
    return SkillInvocationResponse(
        skill_id=result['id'],
        status=result['status'],
        result=result.get('output'),
        error=result.get('error'),
        execution_time_ms=result['latency_ms']
    )

# Get current status of all skills
@app.get("/api/v1/agent/skill-status")
async def get_skill_status():
    """Return the current status of all 56 super-skills."""
    return skill_monitor.get_all_skill_status()

# Get outputs from a specific skill
@app.get("/api/v1/agent/skill-outputs/{skill_name}")
async def get_skill_outputs(skill_name: str, limit: int = 100):
    """Return the last N outputs from a specific skill."""
    return skill_history.get_outputs(skill_name, limit)

# WebSocket for real-time skill outputs
@app.websocket("/ws/skill-output")
async def skill_output_stream(websocket: WebSocket):
    """Stream real-time skill outputs to connected clients."""
    await websocket.accept()
    async for output in skill_output_stream.stream():
        await websocket.send_json(output)
```

### CLI Interface

```bash
# Command-line interface for skill interaction

# List all available skills
ats skills list
ats skills list --filter trading
ats skills list --filter analysis

# Invoke a skill directly
ats invoke market-regime-classifier --symbol XAUUSD --timeframe H1

# Get skill output history
ats skills outputs market-regime-classifier --last 10

# Monitor system status
ats monitor
ats monitor --skills
ats monitor --positions

# Control the system
ats control start
ats control stop
ats control emergency-stop

# Get agent status
ats agent status
ats agent queue
```

---

## Continuous Operation Architecture

### No-Restart Design

```python
class ContinuousOperationManager:
    """
    Manages continuous operation without restarts.

    Key features:
    - Hot-reload of skill configurations
    - Dynamic skill loading/unloading
    - Graceful error recovery
    - State checkpointing
    """

    async def run(self):
        """Main continuous operation loop."""
        while self.should_run:
            try:
                # Process market events
                await self.process_events()

                # Execute skills as needed
                await self.execute_active_skills()

                # Check for configuration changes
                if self.config_changed:
                    await self.hot_reload_config()

                # Periodic health check
                if self.should_health_check():
                    await self.health_check()

            except Exception as e:
                # Log but don't stop
                await self.handle_error(e)
                await asyncio.sleep(1)  # Brief pause before retry

    async def hot_reload_config(self):
        """Reload configuration without restart."""
        new_config = self.load_config()
        self.config.merge(new_config)
        self.notify_config_change()

    async def handle_error(self, error):
        """Handle errors without stopping."""
        self.error_logger.log(error)

        if self.is_critical(error):
            await self.kill_switch.trigger()
        else:
            # Continue operation
            pass
```

### Agent Orchestration

```python
class AgentOrchestrator:
    """
    Coordinates multiple AI agents running simultaneously.

    Each agent is responsible for a specific domain:
    - Data Agent: Fetches market data
    - Analysis Agent: Runs market analysis skills
    - Strategy Agent: Runs strategy skills
    - Risk Agent: Runs risk management skills
    - Execution Agent: Executes trades
    - Monitor Agent: Tracks system health
    """

    AGENTS = {
        'data': DataAgent,
        'analysis': AnalysisAgent,
        'strategy': StrategyAgent,
        'risk': RiskAgent,
        'execution': ExecutionAgent,
        'monitor': MonitorAgent,
    }

    async def start_all_agents(self):
        """Start all agents concurrently."""
        tasks = []
        for name, agent_class in self.AGENTS.items():
            agent = agent_class(
                name=name,
                event_bus=self.event_bus,
                config=self.config
            )
            tasks.append(agent.run())
            self.agents[name] = agent

        # Run all agents concurrently
        await asyncio.gather(*tasks, return_exceptions=True)

    async def get_agent_status(self):
        """Get status of all agents."""
        return {
            name: agent.get_status()
            for name, agent in self.agents.items()
        }
```

---

## Complete Directory Structure (Generated)

```
auto-trading-system/
├── mt5_bridge/                            # ★ SEPARATE SERVICE — runs natively on Windows
│   ├── app.py                             # FastAPI entry point (port 8510)
│   ├── mt5_connector.py                   # MetaTrader5 Python API wrapper
│   ├── routes/
│   │   ├── market_data.py                 # GET /symbols, /ohlcv, /ticks
│   │   ├── trading.py                     # POST /order, GET /positions, DELETE /position
│   │   └── account.py                     # GET /account
│   ├── websocket/
│   │   ├── tick_stream.py                 # WS /ws/ticks (multi-symbol)
│   │   └── bar_stream.py                  # WS /ws/bars (bar completion)
│   ├── models.py                          # Pydantic request/response schemas
│   ├── requirements.txt                   # MetaTrader5, FastAPI, uvicorn
│   └── install_service.bat                # NSSM service installer
│
├── src/
│   ├── __init__.py
│   ├── main.py                          # Application entry point
│   │
│   ├── core/                            # Core infrastructure
│   │   ├── __init__.py
│   │   ├── config.py                    # Configuration management
│   │   ├── logging_config.py            # Structured logging setup
│   │   ├── state_manager.py             # Redis-backed state management
│   │   ├── event_bus.py                 # Redis Streams event system
│   │   └── skill_bridge.py              # Bridge to Claude Code skills
│   │
│   ├── skills/                          # Skill integration layer
│   │   ├── __init__.py
│   │   ├── skill_router.py              # Copied from skills ecosystem
│   │   ├── skill_invoker.py             # Wraps all skill calls
│   │   ├── skill_monitor.py             # Monitors skill execution
│   │   ├── skill_output_collector.py    # Collects skill outputs
│   │   └── skills_index.json            # 265+ skills index
│   │
│   ├── trading_brain/                   # Master orchestrator
│   │   ├── __init__.py
│   │   ├── orchestrator.py              # TradingBrain main class
│   │   ├── layer_1_intelligence.py      # Market analysis
│   │   ├── layer_2_strategy.py          # Strategy selection
│   │   ├── layer_3_signals.py            # Signal generation
│   │   ├── layer_4_aggregation.py       # Signal aggregation
│   │   ├── layer_5_risk.py               # Risk validation
│   │   ├── layer_6_execution.py          # Trade execution
│   │   └── layer_7_learning.py           # Learning & adaptation
│   │
│   ├── data/                            # Market data layer
│   │   ├── __init__.py
│   │   ├── base_feed.py                 # Abstract data feed interface
│   │   ├── mt5_bridge_client.py         # ★ HTTP/WS client for MT5 Bridge
│   │   ├── yfinance_feed.py             # yFinance backup feed
│   │   ├── tick_storage.py              # Tick data persistence
│   │   └── ohlcv_cache.py               # OHLCV caching layer
│   │
│   ├── analysis/                        # Market analysis layer
│   │   ├── __init__.py
│   │   ├── regime_classifier.py         # Trending/ranging/volatile detection
│   │   ├── technical_indicators.py      # RSI, MACD, ATR, etc.
│   │   ├── liquidity_analyzer.py        # Order flow, spread analysis
│   │   ├── market_intelligence.py       # Aggregate analysis coordinator
│   │   ├── news_filter.py               # Event blacklist/whitelist
│   │   └── ict_smc_analyzer.py          # ICT/SMC analysis
│   │
│   ├── strategies/                      # Trading strategies
│   │   ├── __init__.py
│   │   ├── base_strategy.py             # Abstract strategy interface
│   │   ├── breakout_strategy.py         # Volatility breakout
│   │   ├── mean_reversion_strategy.py   # Bollinger bounce, RSI fade
│   │   ├── ict_smc_strategy.py          # Smart Money Concepts
│   │   ├── session_scalper.py           # Time-based scalping
│   │   ├── intensity_strategies.py     # Bullet/Blitz/Rapid strategy engine
│   │   └── strategy_registry.py         # Dynamic strategy loading
│   │
│   ├── signals/                         # Signal processing
│   │   ├── __init__.py
│   │   ├── signal_generator.py          # Individual signal creation
│   │   ├── signal_aggregator.py         # Combine multiple signals (ML)
│   │   ├── signal_validator.py          # Pre-signal validation
│   │   ├── signal_arbitrator.py         # Conflict resolution
│   │   └── signal_history.py            # Signal audit log
│   │
│   ├── risk/                            # Risk management layer
│   │   ├── __init__.py
│   │   ├── position_sizer.py            # Fractional risk calculation
│   │   ├── risk_filter.py               # Pre-trade risk gate
│   │   ├── portfolio_monitor.py         # Real-time exposure tracking
│   │   ├── drawdown_tracker.py          # Drawdown calculation
│   │   ├── kill_switch.py               # Emergency shutdown
│   │   └── risk_calendar.py             # News/session filter
│   │
│   ├── execution/                       # Order execution layer
│   │   ├── __init__.py
│   │   ├── order_router.py              # Order submission to MT5
│   │   ├── execution_reporter.py        # Fill confirmation and logging
│   │   ├── sltp_manager.py              # Stop-loss / take-profit management
│   │   ├── execution_algo.py            # TWAP, VWAP, etc.
│   │   └── position_tracker.py          # Open position state
│   │
│   ├── monitoring/                      # Monitoring and alerts
│   │   ├── __init__.py
│   │   ├── metrics_collector.py         # Prometheus metrics
│   │   ├── health_check.py              # System health status
│   │   ├── alert_manager.py             # Notification routing
│   │   ├── dashboard.py                 # CLI dashboard (rich/textual)
│   │   └── skill_monitor.py             # Skill execution monitoring
│   │
│   ├── backtest/                        # Backtesting engine
│   │   ├── __init__.py
│   │   ├── engine.py                    # Vectorized backtest runner
│   │   ├── metrics.py                   # Performance metrics calculation
│   │   ├── reports.py                   # Report generation
│   │   ├── optimizer.py                 # Genetic parameter optimization
│   │   └── validation.py                # Out-of-sample validation
│   │
│   ├── agents/                          # ★ AI AGENT TRADING DESK
│   │   ├── __init__.py
│   │   ├── base_agent.py               # BaseAgent class + skill invocation logging
│   │   ├── agent_desk.py               # AgentDesk: 8-agent collaboration protocol
│   │   ├── head_trader.py              # HEAD TRADER — final decisions, conflict resolution
│   │   ├── world_intel.py              # WORLD INTEL — news, macro, correlations, sentiment
│   │   ├── technician.py              # TECHNICIAN — TA, PA, regime, confluence
│   │   ├── strategist.py              # STRATEGIST — ICT, breakout, mean-rev, scalping
│   │   ├── risk_officer.py            # RISK OFFICER — sizing, exposure, kill switch
│   │   ├── executor.py                # EXECUTOR — order management, fill tracking
│   │   ├── devils_advocate.py         # DEVIL'S ADVOCATE — challenges every trade
│   │   ├── intensity_selector.py           # MODE SELECTOR — Bullet/Blitz/Rapid activation
│   │   └── intensity_manager.py            # Game mode manager: 3 concurrent mode instances
│   │
│   └── api/                             # REST API (FastAPI)
│       ├── __init__.py
│       ├── app.py                       # FastAPI application
│       ├── routes/
│       │   ├── status.py                # System status endpoint
│       │   ├── trades.py                # Trade history endpoint
│       │   ├── skills.py                # Skill invocation endpoint
│       │   └── control.py               # Kill switch, config endpoint
│       ├── websocket/
│       │   ├── skill_output.py          # Skill output stream
│       │   ├── market_data.py           # Market data stream
│       │   └── signals.py               # Signal stream
│       └── models/                      # Pydantic models
│           ├── requests.py
│           └── responses.py
│
├── tests/                               # Test suite
│   ├── __init__.py
│   ├── conftest.py                      # Pytest fixtures
│   ├── unit/                            # Unit tests
│   ├── integration/                     # Integration tests
│   └── fixtures/                        # Test data fixtures
│
├── config/                              # Configuration files
│   ├── default.yaml                     # Default configuration
│   ├── paper.yaml                       # Paper trading overrides
│   ├── live.yaml                        # Live trading overrides
│   └── skills.yaml                      # Skill-specific configs
│
├── scripts/                             # Utility scripts
│   ├── setup_db.py                      # Database initialization
│   ├── migrate_state.py                 # State migration
│   ├── backtest_runner.py               # Standalone backtest runner
│   └── skill_invoker.py                 # CLI skill invocation
│
├── docker/                              # Docker configuration
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── requirements.txt                     # Python dependencies
├── pyproject.toml                       # Project metadata, tool config
├── pytest.ini                           # Pytest configuration
└── README.md                            # Project documentation
```

---

## Data Models

### Core Entities

```python
@dataclass
class MarketState:
    """Complete snapshot of market conditions (Layer 1 output)"""
    timestamp: datetime
    symbol: str
    bid: float
    ask: float
    spread: float
    regime: RegimeType  # TRENDING, RANGING, VOLATILE
    volatility: float
    liquidity_score: float
    news_risk: NewsRiskLevel
    skill_sources: list[str]  # Which skills contributed

@dataclass
class TradingSignal:
    """Generated trading signal from a strategy (Layer 3 output)"""
    id: str
    timestamp: datetime
    symbol: str
    strategy: str
    direction: Direction  # LONG, SHORT
    entry_price: float
    stop_loss: float
    take_profit: float
    confidence: float  # 0.0–1.0, weighted ratio of conditions met
    rationale: str
    regime_required: RegimeType
    skill_sources: list[str]

@dataclass
class FinalSignal:
    """Aggregated and arbitrated signal (Layer 4 output)"""
    id: str
    timestamp: datetime
    symbol: str
    direction: Direction
    entry_price: float
    stop_loss: float
    take_profit: float
    confidence: float  # Aggregated confidence across strategies
    contributing_strategies: list[str]  # Which strategies agreed
    confluence_score: float  # 0.0–1.0 weighted linear score
    confluence_factors: dict  # Factor breakdown {name: {signal, weight, contribution}}
    gates_passed: bool  # news_clear + spread_normal gates
    position_size_multiplier: float  # 0.0, 0.25–1.0 from confluence
    regime_aligned: bool
    intensity_mode: Optional[TradingIntensity]  # BULLET / BLITZ / RAPID / None
    skill_sources: list[str]

@dataclass
class RiskApproval:
    """Risk filter decision (Layer 5 output)"""
    approved: bool
    signal_id: str
    position_size: float
    risk_pct: float  # Actual risk % of account
    rejection_reason: Optional[str]
    warnings: list[str]
    skill_sources: list[str]

@dataclass
class TradeResult:
    """Executed trade record (Layer 6 output)"""
    id: str
    signal_id: str
    symbol: str
    direction: Direction
    entry_price: float
    quantity: float
    stop_loss: float
    take_profit: float
    entry_time: datetime
    execution_method: str  # market, limit, iceberg, etc.
    slippage_bps: float
    status: TradeStatus
    skill_sources: list[str]

@dataclass
class Position:
    """Current open position"""
    trade_id: str
    symbol: str
    quantity: float
    entry_price: float
    current_price: float
    unrealized_pnl: float
    sl_price: float
    tp_price: float
    duration: timedelta
    skill_sources: list[str]
```

---

## Event Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      EVENT BUS (Redis Streams)                          │
└─────────────────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
   [market:tick]        [signal:new]         [trade:filled]
         │                    │                    │
         ▼                    ▼                    ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Data Feed   │    │  Strategies  │    │  Execution   │
│  Subscribers │    │  Subscribers │    │  Subscribers │
└──────────────┘    └──────────────┘    └──────────────┘
```

### Event Types

| Channel | Payload | Producers | Consumers |
|---------|---------|-----------|-----------|
| `market:tick` | MarketState | MT5BridgeClient | All strategies |
| `market:ohlcv` | OHLCVBar | MT5BridgeClient | Indicators, regime classifier |
| `signal:new` | TradingSignal | Strategies | Signal aggregator |
| `signal:validated` | TradingSignal | Signal validator | Risk filter |
| `trade:open` | Trade | Execution | Portfolio monitor |
| `trade:close` | Trade | Execution | Analytics |
| `risk:alert` | RiskAlert | Portfolio monitor | Kill switch |
| `system:shutdown` | ShutdownReason | Kill switch | All components |
| `skill:invoked` | SkillInvocation | All components | Skill monitor |
| `skill:result` | SkillResult | All components | Skill monitor |
| `skill:error` | SkillError | All components | Skill monitor, alert manager |

---

## Concurrency Model

```python
# Main event loop
async def main():
    # Create event bus
    event_bus = RedisEventBus(redis_url)

    # Create core components
    data_feed = MT5BridgeClient(event_bus, bridge_url="http://localhost:8510")
    regime_classifier = RegimeClassifier(event_bus)
    strategies = load_strategies()
    signal_aggregator = SignalAggregator(event_bus)
    risk_filter = RiskFilter(event_bus)
    execution = ExecutionEngine(event_bus)
    monitor = PortfolioMonitor(event_bus)
    skill_monitor = SkillMonitor(event_bus)

    # Create AI agents
    orchestrator = AgentOrchestrator(event_bus)

    # Create tasks (run concurrently)
    tasks = [
        data_feed.run(),           # Continuously fetch ticks
        regime_classifier.run(),   # Classify regime every tick
        *[s.run() for s in strategies],  # Each strategy analyzes
        signal_aggregator.run(),   # Aggregate signals
        risk_filter.run(),         # Validate signals
        execution.run(),           # Execute orders
        monitor.run(),             # Track positions
        skill_monitor.run(),       # Monitor skill health
        orchestrator.run(),        # Coordinate agents
    ]

    # Run until shutdown
    await asyncio.gather(*tasks, return_exceptions=True)
```

---

## Error Handling Strategy

| Error Type | Handler | Recovery |
|------------|---------|----------|
| MT5 Bridge down | Circuit breaker + yFinance fallback | Log alert, retry with backoff |
| Data feed failure | Fallback to backup feed | Log alert, switch feeds |
| API rate limit | Exponential backoff | Wait, retry with jitter |
| Order rejection | Immediate log | Cancel signal, notify |
| Risk limit breach | Kill switch | Close all positions, halt |
| State corruption | Load from snapshot | Recover last known good state |
| Strategy crash | Isolated process | Restart strategy, log error |
| Skill invocation failure | Skill retry with fallback | Use alternative skill |
| Agent crash | Agent restart | Restore from checkpoint |

---

## Monitoring Metrics

### System Metrics
- `trading_system_uptime` — Seconds since start
- `trading_system_latency` — Tick to signal latency (ms)
- `trading_system_memory` — Memory usage (bytes)
- `trading_system_cpu` — CPU usage percent

### Trading Metrics
- `trades_total` — Total trades executed
- `trades_win_rate` — Winning trade percentage
- `trades_profit_factor` — Gross wins / gross losses
- `trades_max_drawdown` — Maximum drawdown percentage
- `trades_current_exposure` — Current portfolio risk percent

### Skill Metrics
- `skill_invocations_total` — Total skill invocations by skill name
- `skill_success_rate` — Successful skill execution percentage
- `skill_latency_p95` — 95th percentile skill execution time
- `skill_error_rate` — Failed skill invocations
- `skill_output_quality` — Skill output validation score

### Component Metrics
- `data_feed_ticks_received` — Ticks per second
- `data_feed_latency_p95` — Feed latency percentile
- `strategies_active` — Number of active strategies
- `signals_generated` — Signals per strategy
- `orders_submitted` — Orders per minute
- `orders_fill_rate` — Successful fill percentage

---

## Security Considerations

1. **Credentials**: API keys in environment variables, never in code
2. **Trading System API**: Bearer token auth (ATS_API_KEY env var), required on all endpoints
3. **MT5 Bridge API**: Bearer token auth (ATS_BRIDGE_API_KEY env var), localhost-only by default
4. **Database**: PostgreSQL with row-level security for audit logs
5. **Redis**: Password authenticated, AOF persistence enabled, TLS in production
6. **API**: Rate limiting on all endpoints, CORS restricted to localhost
7. **Kill Switch**: Available via API (authenticated) and CLI (local-only)
8. **Skill Execution**: Sandboxed skill invocation with timeout limits
9. **Network**: MT5 Bridge binds to 127.0.0.1 by default (not exposed externally)

---

## Deployment Architecture

```
┌───────────────────────────────────────────────────────────────────────────┐
│                           WINDOWS HOST                                     │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────────────────────────────────┐                             │
│  │  NATIVE WINDOWS SERVICES                 │                             │
│  │                                          │                             │
│  │  ┌─────────────┐    ┌─────────────────┐  │                             │
│  │  │ MT5 Terminal │◄──▶│ MT5 REST Bridge │  │                             │
│  │  │ (broker)     │    │ (FastAPI:8510)  │  │                             │
│  │  └─────────────┘    └────────┬────────┘  │                             │
│  │                              │ REST/WS   │                             │
│  └──────────────────────────────┼───────────┘                             │
│                                 │                                         │
│  ┌──────────────────────────────┼───────────────────────────────────┐     │
│  │  DOCKER CONTAINERS          │                                    │     │
│  │                              │                                    │     │
│  │  ┌─────────────┐    ┌───────▼───────┐    ┌─────────────┐        │     │
│  │  │  PostgreSQL │    │ Trading System│    │   Redis     │        │     │
│  │  │  (Data/Logs)│◄──▶│  (Python)     │◄──▶│  (State)    │        │     │
│  │  └─────────────┘    │               │    └─────────────┘        │     │
│  │                      │ ┌───────────┐│                            │     │
│  │                      │ │ AI Agents ││                            │     │
│  │                      │ │ • Data    ││                            │     │
│  │                      │ │ • Analysis││                            │     │
│  │                      │ │ • Strategy││                            │     │
│  │                      │ │ • Risk    ││                            │     │
│  │                      │ │ • Execute ││                            │     │
│  │                      │ │ • Monitor ││                            │     │
│  │                      │ └───────────┘│                            │     │
│  │                      └──────────────┘                            │     │
│  └──────────────────────────────────────────────────────────────────┘     │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘

Key: MT5 Bridge runs NATIVELY on Windows (MetaTrader5 Python API requirement).
     Everything else runs in Docker. Communication via REST/WebSocket on port 8510.
```

---

## Spec-Kit Completion Criteria

This plan is complete when:
- [x] All technical decisions are finalized
- [x] Component architecture is fully defined
- [x] Data models and schemas are specified
- [x] All 161 classified skills are mapped to implementation phases
- [x] Continuous monitoring architecture is defined
- [x] AI agent API/CLI integration is specified
- [x] Security and deployment considerations are addressed
- [x] Integration points with Claude Code skills are documented
- [x] Complete skills catalog created (CLASSIFIED_SKILLS_CATALOG.md)

**Next Step:** Proceed to tasks.md (implementation breakdown)

---

**Plan Status:** AI-Agent-First Architecture — Major Redesign
**Version:** 8.0
**Date:** 2026-03-19
**Spec-Kit:** ✓ AI Agent Trading Desk Architecture
**Changes v8.0:**
- FUNDAMENTAL SHIFT: AI agents are the traders, code is tools
- 8 specialist agents: Head Trader, World Intel, Technician, Strategist, Risk Officer, Executor, Devil's Advocate, Mode Selector
- 3 concurrent trading intensity modes: Bullet (tick, Mahmoud's pref), Blitz (M1-M5), Rapid (M15+)
- Agent collaboration protocol: 7-step flow with Devil's Advocate challenge
- Full skill-agent binding map (161 skills → 8 agents)
- World Intel always-on: news, macro, correlations, sentiment, calendar
- Bullet mode detail: tick velocity, bid/ask imbalance, spread compression entries
- Mode Selector: AI-driven, not hardcoded rules
- Agent transparency: SkillInvocation logging for every call
- Updated directory: agents/ with 8 specialist + desk + mode manager
**Prior (v7.0):** Scalping modes, spread guard, session filters
