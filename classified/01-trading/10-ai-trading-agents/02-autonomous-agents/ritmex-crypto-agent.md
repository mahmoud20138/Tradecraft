---
name: ritmex-crypto-agent
description: ritmex-ai-trader — multi-agent crypto trading research platform for Binance. Automated market data ingestion, PineScript-based technical analysis, signal generation, risk management, and compliance reporting. Built on Bun (TypeScript). Agents: data p
kind: agent
category: trading/ai-agents
status: active
tags: [agent, ai-agents, crypto, risk-and-portfolio, ritmex, trading, typescript]
related_skills: [ai-trading-crew, autohedge-swarm, freqtrade-bot, openalice-trading-agent, polymarket-prediction-agents]
---

# ritmex-crypto-agent

USE FOR:
  - "crypto trading agent on Binance"
  - "PineScript indicators in TypeScript"
  - "multi-agent crypto signal pipeline"
  - "automated Binance market analysis"
  - "crypto compliance and audit trail"
tags: [crypto, Binance, multi-agent, PineScript, TypeScript, Bun, signal-generation, risk, compliance]
kind: framework
category: crypto-defi-trading

---

## What Is ritmex-ai-trader?

Multi-agent crypto trading research platform targeting Binance.
- Repo: https://github.com/valentinov4169/ritmex-ai-trader
- Runtime: **Bun v1.2.20** (TypeScript)
- Data source: Binance real-time market data
- Analysis: PineScript indicators via `pinets` library

---

## Agent Pipeline

```
Data Agent      → real-time Binance market data ingestion
Technical Agent → PineScript indicators (trend, momentum, volume)
Signal Agent    → signal derivation from indicator confluence
Risk Agent      → exposure control + position sizing
Compliance Agent→ regulatory reporting + audit trail
```

---

## Installation

```bash
git clone https://github.com/valentinov4169/ritmex-ai-trader
cd ritmex-ai-trader
cp env.example .env   # Configure Binance API keys, etc.
bun install
bun run index.ts
```

**Requirements**: Bun v1.2.20+, 4GB RAM, stable internet

---

## Key Components

| Component | Function |
|-----------|---------|
| Market Data | Real-time Binance OHLCV ingest |
| PineScript via `pinets` | Technical indicators in TS |
| Signal Engine | Confluence-based trade signals |
| Risk Manager | Exposure limits + sizing rules |
| Compliance | Audit trail + regulatory docs |

---

## PineScript Indicators in TypeScript

```typescript
import { pinets } from "pinets"

// RSI
const rsi = pinets.rsi(closes, 14)

// MACD
const [macdLine, signalLine, histogram] = pinets.macd(closes, 12, 26, 9)

// Bollinger Bands
const [upper, middle, lower] = pinets.bbands(closes, 20, 2.0)
```


---
