# Skills Collection

> **161 curated skills** across **6 domains** and **33 categories** — AI-powered knowledge bases for trading, development, and automation.

[![Skills](https://img.shields.io/badge/skills-161-blue)](.)
[![Domains](https://img.shields.io/badge/domains-6-green)](.)
[![Categories](https://img.shields.io/badge/categories-33-orange)](.)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

---

## What's Inside

A classified collection of prompt-driven skills organized into a hierarchical directory structure. Each skill is a self-contained Markdown file with knowledge, instructions, and often executable code blocks designed for AI coding assistants (Claude Code, Cursor, Copilot, Windsurf, etc.).

### Quick Stats

| Domain | Skills | Focus |
|--------|--------|-------|
| **01 - Trading** | 106 | Strategies, analysis, risk, execution, MT5, quant/ML, AI agents |
| **02 - AI Development** | 9 | Agent frameworks, prompt engineering, MCP integration, ML tools |
| **03 - Software Engineering** | 22 | Architecture, testing, UI design, dev tools, code quality |
| **04 - Platform (Claude Code)** | 18 | Plugin development, skill management, workflow routing, governance |
| **05 - Data Acquisition** | 4 | Web scraping, video knowledge, media generation |
| **06 - Domain Specific** | 2 | Scientific computing, payments/SaaS |

---

## Directory Structure

```
.
├── classified/
│   ├── 01-trading/
│   │   ├── 01-core-knowledge/        (7)   — Fundamentals, asset classes
│   │   ├── 02-analysis/              (9)   — Technical, fundamental, chart vision
│   │   ├── 03-strategies/            (22)  — ICT/SMC, breakout, mean-reversion, sessions
│   │   ├── 04-market-context/        (14)  — Regime, macro, correlation, volatility
│   │   ├── 05-risk-management/       (6)   — Position sizing, drawdown, portfolio
│   │   ├── 06-execution/             (6)   — Algo execution, HFT, prop trading
│   │   ├── 07-data-signals/          (7)   — Data ingestion, sentiment, intelligence
│   │   ├── 08-mt5-platform/          (3)   — Integration, charts, EAs
│   │   ├── 09-quant-ml/              (9)   — Backtesting, ML, RL, statistics
│   │   ├── 10-ai-trading-agents/     (7)   — Multi-agent, autonomous, prediction
│   │   ├── 11-psychology-ops/        (3)   — Psychology, journaling, plans
│   │   ├── 12-infrastructure/        (5)   — Alerts, Telegram/Discord, trade copier
│   │   └── 13-orchestration/         (8)   — Master workflow, trading brain, autopilot
│   ├── 02-ai-development/
│   │   ├── 01-agent-building/        — Frameworks, architecture, MCP
│   │   ├── 02-prompt-engineering/    — Few-shot quality prompting
│   │   ├── 03-ml-tools/              — Transformers.js
│   │   └── 04-spec-driven/           — OpenSpec, Spec-Kit
│   ├── 03-software-engineering/
│   │   ├── 01-architecture/          — System design, codebase intelligence
│   │   ├── 02-code-review-quality/   — Code review, snapshots
│   │   ├── 03-testing/               — E2E, integration, smoke, pre-commit
│   │   ├── 04-ui-design/             — Frontend, visualization, playground
│   │   ├── 05-dev-tools/             — Git, GitHub Actions, HTTPie, sandboxes
│   │   └── 06-learning/              — Interactive coding challenges
│   ├── 04-platform-claude-code/
│   │   ├── 01-plugin-development/    — Commands, hooks, skills, plugins
│   │   ├── 02-skill-management/      — Analytics, docs, doctor, test suite
│   │   ├── 03-automation-governance/ — Recommender, governor, writing rules
│   │   └── 04-workflow-routing/      — Memory, pipeline, router, builder
│   ├── 05-data-acquisition/
│   │   ├── 01-web-scraping/          — Firecrawl
│   │   ├── 02-video-knowledge/       — YouTube, video extraction
│   │   └── 03-media-generation/      — Video generation
│   └── 06-domain-specific/
│       ├── 01-scientific-computing/  — FEATool multiphysics
│       └── 02-payments-saas/         — Stripe best practices
├── .specify/                          — Specs, memory, scripts
├── .vscode/                           — Editor settings
├── SKILLS_CATALOG.md                  — Full catalog with categories
└── skills_index.json                  — Machine-readable index (tags, related skills)
```

---

## Trading Skills Highlights

The trading domain is the largest section with **106 skills** covering the full trading lifecycle:

| Category | Key Skills |
|----------|-----------|
| **ICT / Smart Money** | ict-smart-money (2,658L), liquidity-analysis, market-structure-bos-choch, smart-money-trap-detector, smc-python-library |
| **Strategies** | breakout-engine, mean-reversion-engine, session-scalping (1,261L), capitulation-mean-reversion, grid-trading |
| **Technical Analysis** | technical-analysis (2,609L), price-action (1,188L), volume-analysis, fibonacci-harmonic-wave |
| **Risk Management** | risk-and-portfolio (2,020L), portfolio-optimization, real-time-risk-monitor, risk-of-ruin, drawdown-playbook |
| **Execution** | market-making-hft (1,335L), execution-algo-trading, hedgequantx-prop-trading |
| **Quant / ML** | backtesting-sim (1,156L), ml-trading, tensortrade-rl, strategy-genetic-optimizer |
| **Orchestration** | trading-brain (1,256L), brain-ecosystem-mcp (4,437L), master-trading-workflow, trading-autopilot |
| **Data / Signals** | market-intelligence (1,291L), crypto-defi-trading (1,436L), news-intelligence, social-sentiment |
| **MT5** | mt5-integration (1,501L), mt5-chart-browser (602L), gold-orb-ea |

---

## How to Use

### As AI Assistant Knowledge

1. Point your AI coding assistant to the `classified/` directory
2. Skills are auto-discovered from the index or referenced directly
3. Each `.md` file contains context, instructions, and often executable code

### As a Reference Library

```bash
# Browse the catalog
cat SKILLS_CATALOG.md

# Search for a skill
grep -r "ict-smart-money" classified/

# Use the machine-readable index
python -c "import json; idx=json.load(open('skills_index.json')); print(len(idx['skills']))"
```

### With VS Code / Cursor

The included `.vscode/settings.json` enables Copilot agent mode. Skills can be referenced via `@file` in your AI chat.

---

## Index Files

| File | Description |
|------|-------------|
| `SKILLS_CATALOG.md` | Human-readable catalog grouped by category with line counts |
| `skills_index.json` | Machine-readable JSON with name, path, kind, category, tags, related skills, line count |
| `.specify/specs/` | System specs, data models, plans, and task breakdowns |

---

## Skill Metadata

Each skill in `skills_index.json` includes:

```json
{
  "name": "ict-smart-money",
  "path": "01-trading/03-strategies/01-ict-smart-money/ict-smart-money.md",
  "kind": "reference",
  "category": "trading/strategies",
  "status": "active",
  "tags": ["trading", "strategy", "ict", "smc", "liquidity", "orderflow"],
  "related_skills": ["session-scalping", "technical-analysis", "liquidity-analysis"],
  "lines": 2658,
  "has_code": true
}
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. PRs welcome — whether it's new skills, improvements to existing ones, or better categorization.

## License

[MIT](LICENSE) — use freely in personal and commercial projects.
