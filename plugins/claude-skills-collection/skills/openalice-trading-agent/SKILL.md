---
name: openalice-trading-agent
description: OpenAlice — experimental file-driven autonomous AI trading agent running locally. "Your research desk, quant team, trading floor, and risk manager on your laptop 24/7." Uses "Trading-as-Git" workflow (stage → commit → push to execute). Natively integ
kind: agent
category: trading/ai-agents
status: active
tags: [agent, ai-agents, openalice, risk-and-portfolio, trading]
related_skills: [ai-trading-crew, autohedge-swarm, freqtrade-bot, polymarket-prediction-agents, ritmex-crypto-agent]
---

# openalice-trading-agent

USE FOR:
  - "autonomous AI trading agent on local machine"
  - "Claude Code CLI for trading"
  - "Trading-as-Git workflow"
  - "Alpaca / CCXT automated trading"
  - "persistent trading agent with memory"
  - "self-modifying trading agent"
  - "file-driven trading automation"
tags: [autonomous-agent, Claude-Code, trading, Alpaca, CCXT, IBKR, git-workflow, TypeScript, local, equity, crypto, forex]
kind: tool
category: quant-ml-trading

---

## What Is OpenAlice?

Experimental file-driven autonomous AI trading agent.
- Repo: https://github.com/TraderAlice/OpenAlice
- Stack: TypeScript / Node.js 22+ / pnpm
- AI: **Claude Code CLI (default)**, Vercel AI SDK, Agent SDK — switchable at runtime
- Status: Experimental — **do not use with real funds**

> "Your own research desk, quant team, trading floor, and risk management —
> all running on your laptop 24/7."

---

## Installation

```bash
# Prerequisites: Node.js 22+, pnpm 10+, Claude Code CLI (authenticated)
git clone https://github.com/TraderAlice/OpenAlice.git
cd OpenAlice
pnpm install && pnpm build
pnpm dev
# Access at: http://localhost:3002
```

**No API keys required** for default Claude Code setup.

---

## Architecture

```
┌──────────── AgentCenter (orchestration) ─────────────┐
│                                                       │
│  ProviderRouter  → Claude Code / Vercel AI / SDK      │
│  ToolCenter      → centralized capability registry    │
│                                                       │
│  Extensions:                                          │
│    trading/    → orders, positions, risk              │
│    analysis/   → technicals, fundamentals, news       │
│    news/       → RSS archive, searchable              │
│                                                       │
│  Connectors:                                          │
│    Web UI  · Telegram  · MCP                          │
└──────────────────────────────────────────────────────┘
```

---

## Trading-as-Git Workflow

```bash
# Stage an order
alice stage buy AAPL 100 --limit 195.00

# Review staged orders
alice status

# Commit with intent message
alice commit -m "buy AAPL on earnings dip"
# Returns: commit hash (8 chars) e.g. a1b2c3d4

# Execute (push to broker)
alice push

# View history
alice log
```

---

## Unified Trading Account (UTA) Architecture

Each account owns:
- Its own broker connection (Alpaca / CCXT / IBKR)
- Operation history (git-style)
- Safety checks (position limits, cooldowns, symbol whitelist)

```typescript
// Safety guard pipeline (pre-execution)
const guards = [
  new PositionLimitGuard({ maxPositions: 10 }),
  new TradeCooldownGuard({ cooldownMs: 60_000 }),
  new SymbolWhitelistGuard({ symbols: ["AAPL", "NVDA", "BTC"] })]
```

---

## Supported Markets & Brokers

| Broker | Status | Assets |
|--------|--------|--------|
| **Alpaca** | Active | US Equities, Crypto |
| **CCXT** | Active | 100+ Crypto exchanges |
| **IBKR** | Pending | Stocks, Futures, Forex, Options |

**Data coverage**: Equities, Crypto, Forex, Commodities, Macro indicators,
Fundamentals, Financial statements, Analyst estimates, Insider trading

---

## Cognitive Features

| Feature | Description |
|---------|-------------|
| **Working memory** | Persistent across sessions |
| **Emotion tracking** | Agent confidence state |
| **Cron scheduling** | Event-driven strategies |
| **Heartbeat** | Periodic health + position checks |
| **Evolution mode** | Agent modifies own source code (sandboxed) |

---

## Claude Code Integration

OpenAlice uses Claude Code CLI as its default AI backend:
```typescript
// ProviderRouter selects Claude Code by default
const agent = new AgentCenter({ provider: "claude-code" })

// Claude Code handles:
// - Natural language order interpretation
// - Research and analysis tasks
// - Risk reasoning
// - Self-modification (evolution mode)
```

This makes OpenAlice unique: it's built specifically around the Claude Code workflow,
meaning your Claude Code session can directly control the trading agent.

---

## News & Research

```typescript
// RSS-based news collection
const news = await alice.news.search("AAPL earnings Q1 2026")

// Fundamentals + financials
const fundamentals = await alice.analysis.company("AAPL")
// Returns: P/E, EPS, revenue growth, analyst estimates, insider trades
```

---

## Roadmap (v1 targets)

- [] Tool confirmation mechanisms (human-in-the-loop)
- [] Stable trading interfaces
- [] Account analytics dashboard
- [] IBKR broker implementation
- [] MCP connector for Claude Code integration


---
