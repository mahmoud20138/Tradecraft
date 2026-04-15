# Auto-Trading AI Agent System — Spec Kit Summary (Enhanced v3.0)

## Spec-Kit Workflow Status

```
✓ constitution.md  → Immutable principles & tech stack
✓ spec.md          → WHAT to build (requirements)
✓ plan.md          → HOW to build (architecture) ★ ENHANCED WITH ALL 161 SKILLS
✓ tasks.md         → Implementation breakdown
✓ data-model.md    → Entity schemas
✓ contracts/       → API specifications
★ CLASSIFIED_SKILLS_CATALOG.md → Complete 161-skill taxonomy

STATUS: READY FOR IMPLEMENTATION WITH COMPLETE 161-SKILL MAPPING
```

**Current Phase:** Enhanced Plan Complete — All 161 Classified Skills Mapped
**Next Action:** Run `/speckit.implement` or begin Phase 0 (T000-T002)

---

## ENHANCED: Complete 161 Classified Skills Integration

This plan now includes **step-by-step mapping for all 161 classified skills** from the comprehensive skills taxonomy:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   ALL 161 CLASSIFIED SKILLS MAPPED                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  TRADING (95 skills)                                                     │
│  ├── 01-core-knowledge (7) — Fundamentals, asset classes               │
│  ├── 02-analysis (9) — Technical, fundamental, chart vision              │
│  ├── 03-strategies (24) — ICT, breakout, mean reversion, sessions      │
│  ├── 04-market-context (13) — Regime, macro, correlation, breadth      │
│  ├── 05-risk-management (8) — Position sizing, drawdown, filtering      │
│  ├── 06-execution (8) — Algo trading, HFT, market impact               │
│  ├── 07-data-signals (8) — Market data, alternative data, news         │
│  ├── 08-mt5-platform (3) — Integration, chart browser, EA               │
│  ├── 09-quant-ml (9) — Backtesting, ML, RL, optimization              │
│  ├── 10-ai-trading-agents (7) — Multi-agent frameworks, autonomous     │
│  ├── 11-psychology-ops (3) — Journal, psychology, plans                │
│  ├── 12-infrastructure (6) — Alerts, Discord, Telegram, Notion        │
│  └── 13-orchestration (8) — Trading brain, autopilot, workflows       │
│                                                                          │
│  AI DEVELOPMENT (13 skills)                                              │
│  ├── Agent building (5) — Agent development, LangChain, storage        │
│  ├── Prompt engineering (1) — Quality prompting                         │
│  ├── ML tools (1) — Transformers.js                                     │
│  └── Spec driven (2) — OpenSpec, Spec-Kit                               │
│                                                                          │
│  SOFTWARE ENGINEERING (20 skills)                                        │
│  ├── Architecture (4) — Pro code, system design, build from scratch     │
│  ├── Code review (2) — Review, snapshots                                │
│  ├── Testing (5) — E2E, integration, pre-commit, smoke, debug          │
│  ├── UI design (4) — Elite UI, frontend, visualization, playgrounds    │
│  ├── Dev tools (7) — Sandboxes, Git, HTTPie, IP rotation, Python       │
│  └── Learning (1) — Interactive coding challenges                       │
│                                                                          │
│  PLATFORM CLAUDE-CODE (23 skills)                                        │
│  ├── Plugin development (5) — Plugins, skills, commands, hooks          │
│  ├── Skill management (5) — Manager, analytics, docs, doctor, tests    │
│  ├── Automation (4) — Recommender, CLAUDE.md, governor, rules          │
│  └── Workflow routing (4) — Router, pipeline, context, builder         │
│                                                                          │
│  DATA ACQUISITION (5 skills)                                             │
│  ├── Web scraping (1) — Firecrawl                                        │
│  ├── Video knowledge (2) — YouTube, video extraction                     │
│  └── Media generation (1) — AI video generation                          │
│                                                                          │
│  DOMAIN SPECIFIC (2 skills)                                             │
│  ├── Scientific (1) — FEATool multiphysics                             │
│  └── Payments (1) — Stripe best practices                               │
│                                                                          │
│  Each skill is mapped to a specific implementation phase with:          │
│  • Step-by-step integration points                                       │
│  • Continuous monitoring of skill outputs                                │
│  • AI agent API/CLI integration                                          │
│  • No-restart continuous operation design                                │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

**See [CLASSIFIED_SKILLS_CATALOG.md](CLASSIFIED_SKILLS_CATALOG.md) for complete taxonomy**

---

## Overview

A fully automated trading system built with Python 3.11+, integrating **all 161 classified skills** from the comprehensive skills taxonomy for market analysis, strategy execution, risk management, AI agent orchestration, and continuous monitoring.

---

## Quick Reference

| File | Purpose |
|------|---------|
| [constitution.md](../../memory/constitution.md) | Immutable principles, tech stack, constraints |
| [spec.md](spec.md) | WHAT to build (user stories, requirements) |
| [plan.md](plan.md) | HOW to build (architecture, **COMPLETE 161-SKILL MAPPING**) |
| [CLASSIFIED_SKILLS_CATALOG.md](CLASSIFIED_SKILLS_CATALOG.md) | Complete taxonomy of all 161 skills |
| [tasks.md](tasks.md) | Ordered implementation tasks with skill integration |
| [data-model.md](data-model.md) | Entity schemas, Redis/PostgreSQL design |
| [contracts/api-spec.json](contracts/api-spec.json) | REST API specification (OpenAPI 3.1) |

---

## NEW: Continuous Skill Monitoring Dashboard

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SKILL EXECUTION MONITOR                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ACTIVE SKILLS (161 total classified skills mapped)                     │
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

---

## NEW: AI Agent API/CLI Integration

### REST API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v1/agent/invoke-skill` | Invoke any of the 161 skills by name |
| GET | `/api/v1/agent/skill-status` | Get status of all 161 skills |
| GET | `/api/v1/agent/skill-outputs/{skill}` | Get skill output history |
| WS | `/ws/skill-output` | Real-time skill output stream |
| WS | `/ws/market-data` | Live market data stream |
| WS | `/ws/signals` | New trading signals stream |
| WS | `/ws/positions` | Position updates stream |
| POST | `/api/v1/control/start` | Start trading system |
| POST | `/api/v1/control/stop` | Stop trading system |
| POST | `/api/v1/control/emergency-stop` | Kill switch (< 1 second) |

### CLI Interface

```bash
# List all available skills (161 total)
ats skills list
ats skills list --filter trading
ats skills list --filter ai-development
ats skills list --filter software-engineering

# Invoke a skill directly
ats invoke market-regime-classifier --symbol XAUUSD --timeframe H1
ats invoke ict-smart-money --symbol EURUSD --timeframe H4

# Get skill output history
ats skills outputs market-regime-classifier --last 10
ats skills outputs ict-smart-money --last 20

# Monitor system status
ats monitor
ats monitor --skills
ats monitor --positions
ats monitor --agents

# Control the system
ats control start
ats control stop
ats control emergency-stop

# Get agent status
ats agent status
ats agent queue
```

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        TRADING BRAIN (Orchestrator)                     │
│              trading-brain (7-layer architecture)                         │
│                     Coordinates all 161 skills                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐         ┌────────────────┐         ┌─────────────────┐
│ INTELLIGENCE  │         │   EXECUTION    │         │    RISK LAYER    │
│     LAYER     │         │     LAYER      │         │                 │
│  (95 skills)  │         │   (8 skills)   │         │   (8 skills)    │
└───────────────┘         └────────────────┘         └─────────────────┘
```

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Async Runtime | asyncio + uvloop |
| State Store | Redis (hot) + PostgreSQL (cold) |
| Market Data | MetaTrader5 API |
| Container | Docker + docker-compose |
| Monitoring | Prometheus + Grafana |
| Skill Integration | Smart Skill Router (161 classified skills) |
| AI Agent API | FastAPI + WebSocket |

---

## Key Features

### P1 — Must Have (MVP)
- Real-time market analysis with regime classification
- 3 parallel strategies: Breakout, Mean Reversion, ICT SMC (24 total available)
- Pre-trade risk filtering (news, session, exposure)
- Automatic position sizing (1-2% risk per trade)
- Order execution via MT5
- Real-time portfolio monitoring
- Kill switch (< 1 second response)
- **NEW: Continuous monitoring of all 161 skill outputs**
- **NEW: AI agent API/CLI for invoking any skill**
- **NEW: No-restart continuous operation**

### P2 — Should Have
- Signal aggregation across strategies
- Backtesting engine with genetic optimization
- Performance analytics
- Strategy parameter optimization
- Multi-agent AI orchestration

---

## Risk Rules (Non-Negotiable)

| Rule | Value |
|------|-------|
| Max risk per trade | 2% of account |
| Max total exposure | 6% of account |
| Max drawdown | 15% (auto kill-switch) |
| News blackout | ±30 min around high-impact events |
| Max positions per symbol | 3 |

---

## Implementation Timeline

| Phase | Tasks | Time | Skills Involved |
|-------|-------|------|-----------------|
| 0 — Setup | 3 | 1h | 3 skills |
| 1 — Core | 4 | 6.5h | 5 skills |
| 2 — Data | 4 | 9h | 5 skills |
| 3 — Analysis | 4 | 9h | 12 skills |
| 4 — Strategies | 5 | 11h | 24 skills |
| 5 — Signals | 4 | 7h | 3 skills |
| 6 — Risk | 5 | 9.5h | 8 skills |
| 7 — Execution | 4 | 8.5h | 8 skills |
| 8 — Monitor | 4 | 8h | 7 skills |
| 9 — Backtest | 3 | 9h | 9 skills |
| 10 — Integration | 2 | 5h | 11 skills |
| 11 — Docs | 2 | 5h | 15 skills |
| **MVP Total** | **37** | **~65h** | **95 trading skills** |

---

## Complete Skills Distribution

### By Category

| Category | Skills | Phases |
|----------|--------|--------|
| Trading — Core Knowledge | 7 | 2, 3 |
| Trading — Analysis | 9 | 3 |
| Trading — Strategies | 24 | 4 |
| Trading — Market Context | 13 | 2, 3 |
| Trading — Risk Management | 8 | 6 |
| Trading — Execution | 8 | 7 |
| Trading — Data & Signals | 8 | 2, 5 |
| Trading — MT5 Platform | 3 | 2 |
| Trading — Quant/ML | 9 | 9 |
| Trading — AI Agents | 7 | 10 |
| Trading — Psychology | 3 | 11 |
| Trading — Infrastructure | 6 | 8 |
| Trading — Orchestration | 8 | 1, 5, 10 |
| AI Development | 13 | 0, 10, 11 |
| Software Engineering | 20 | 0, 1, 10, 11 |
| Platform Claude-Code | 23 | 0, 1, 8 |
| Data Acquisition | 5 | 11 |
| Domain Specific | 2 | 11 |
| **TOTAL** | **161** | **All** |

---

## Claude Code Skills Integration

### MANDATORY Meta-Skills
- `skill-execution-governor` — MANDATORY: Governs all skill interactions
- `smart-skill-router` — Dynamic skill selection and routing
- `spec-kit` — Spec-driven development workflow

### Core Trading Skills (P1)
- `trading-brain` — Master orchestrator (7-layer architecture)
- `market-regime-classifier` — Regime detection
- `technical-analysis` — Indicator calculations
- `ict-smart-money` — Complete ICT/SMC methodology
- `risk-and-portfolio` — Position sizing and risk
- `risk-calendar-trade-filter` — Pre-trade safety gate
- `execution-algo-trading` — Order execution algorithms
- `backtesting-sim` — Strategy validation

### Additional Skills (All 161 Mapped)
- See [CLASSIFIED_SKILLS_CATALOG.md](CLASSIFIED_SKILLS_CATALOG.md) for complete list
- Each skill mapped to specific implementation phase in plan.md
- All skills monitored continuously during system operation
- All skills accessible via AI Agent API/CLI

---

## Next Steps

1. **Review Skills Catalog** — Check [CLASSIFIED_SKILLS_CATALOG.md](CLASSIFIED_SKILLS_CATALOG.md) for complete 161-skill taxonomy
2. **Verify Enhanced Plan** — Check plan.md for complete skill mapping by phase
3. **Begin Implementation** — Start with Phase 0 (T000-T002)
4. **Track Progress** — Use tasks.md as checklist with skill monitoring

---

## Important Notes

- **161 Skills**: All classified skills from 6 major categories mapped to implementation phases
- **Continuous Monitoring**: All skill outputs monitored in real-time via dashboard
- **No-Restart Operation**: System runs continuously without re-runs (hot-reload config)
- **AI Agent API**: Invoke any of 161 skills via REST API or CLI
- **Safety First**: All trades pass through risk gate before execution
- **Kill Switch**: Always accessible within 1 second
- **Audit Trail**: Every decision logged with full context + skill sources
- **Stateless**: System restart recovers within 30 seconds
- **Fail-Safe**: Risk check failures BLOCK trades by default
- **Skill-First Design**: Every component integrates with specific classified skills

---

## Spec-Kit Workflow Summary

The Spec-Kit workflow ensures intent-first development:

| Phase | Document | Status | Purpose |
|-------|----------|--------|---------|
| 1 | [constitution.md](../../memory/constitution.md) | ✓ Complete | Immutable principles, tech stack |
| 2 | [spec.md](spec.md) | ✓ Complete | WHAT to build (requirements) |
| 3 | [plan.md](plan.md) | ✓ Enhanced | HOW to build (architecture + **161-SKILL MAPPING**) |
| 4 | [tasks.md](tasks.md) | ✓ Complete | Ordered implementation tasks |
| 5 | [data-model.md](data-model.md) | ✓ Complete | Entity schemas, database design |
| 6 | [contracts/api-spec.json](contracts/api-spec.json) | ✓ Complete | REST API specification (OpenAPI) |
| 7 | **CLASSIFIED_SKILLS_CATALOG.md** | ✓ New | Complete 161-skill taxonomy |
| 8 | **Implement** | Pending | Execute tasks following this spec |

### Before Implementing

1. **Review Constitution** — Confirm you agree with all non-negotiable principles
2. **Validate Spec** — Ensure all user stories are understood
3. **Check Enhanced Plan** — Verify architecture + 161-skill integration
4. **Review Skills Catalog** — Understand complete skill taxonomy
5. **Review Tasks** — Understand the order and dependencies + skill mapping

---

**Spec Status**: Enhanced v3.0 — Ready for Implementation with All 161 Classified Skills
**Version:** 3.0
**Date:** 2026-03-19
**Spec-Kit**: ✓ Full Specification Complete + ★ All 161 Classified Skills Mapped
