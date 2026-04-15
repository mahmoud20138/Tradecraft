---
name: autohedge-swarm
description: AutoHedge — enterprise-grade autonomous hedge fund using swarm agent architecture. Sequential pipeline: Director → Quant → Risk Manager → Execution agents. Risk-first design: position sizing before any trade execution. Currently supports Solana; Coin
kind: agent
category: trading/ai-agents
status: active
tags: [ai-agents, autohedge, risk-and-portfolio, swarm, trading]
related_skills: [ai-trading-crew, freqtrade-bot, openalice-trading-agent, polymarket-prediction-agents, ritmex-crypto-agent]
---

# autohedge-swarm

USE FOR:
  - "autonomous hedge fund agent"
  - "swarm agents for trading"
  - "director + quant + risk manager pipeline"
  - "Solana autonomous trading"
  - "enterprise AI trading system"
  - "risk-first automated trading"
tags: [swarm, agents, hedge-fund, autonomous, Solana, risk-and-portfolio, enterprise, multi-agent, quant]
kind: framework
category: quant-ml-trading

---

## What Is AutoHedge?

Enterprise-grade autonomous agent hedge fund using **swarm intelligence**.
Specialized agents sequentially handle strategy, analysis, risk, and execution.

- Repo: https://github.com/The-Swarm-Corporation/AutoHedge
- Install: `pip install -U autohedge`
- Current: Solana trading (Coinbase planned)
- Philosophy: **Risk-first** — position sizing happens before execution

---

## Swarm Agent Pipeline

```
Director Agent
    ↓ Strategy generation + market context
Quant Agent
    ↓ Quantitative analysis + signal generation
Risk Manager Agent
    ↓ Position sizing + risk assessment + approval
Execution Agent
    ↓ Order construction + submission
Trade Output (JSON)
```

---

## Installation

```bash
pip install -U autohedge
```

**Environment variables:**
```bash
JUPITER_API_KEY="..."          # Solana DEX aggregator
OPENAI_API_KEY="sk-..."        # or ANTHROPIC_API_KEY
WALLET_PRIVATE_KEY="..."       # Solana wallet
```

---

## Usage

```bash
autohedge
```

Or programmatically:
```python
from autohedge import AutoHedge

fund = AutoHedge(
    llm_provider="anthropic",     # Director/Quant use Claude
    risk_threshold=0.02,          # Max 2% portfolio risk per trade
    chain="solana",
)

result = fund.analyze_and_trade("SOL/USDC")
print(result)  # JSON: analysis + decision + risk metrics
```

---

## Agent Responsibilities

| Agent | Role |
|-------|------|
| **Director** | Market context, strategy selection |
| **Quant** | Price analysis, signals, technicals |
| **Risk Manager** | Position sizing, max drawdown limits |
| **Execution** | Order construction, submission |

---

## Output Format (JSON)

```json
{
  "ticker": "SOL/USDC",
  "director_analysis": "Bullish momentum...",
  "quant_signals": {"rsi": 58, "macd": "bullish"},
  "risk_assessment": {"position_size": 0.015, "stop_loss": 0.02},
  "decision": "BUY",
  "execution": {"order_type": "market", "size": 10.5}
}
```

---

## Key Design Principles

1. **Risk-first**: Never execute without risk approval
2. **Audit trail**: Enterprise logging at every step
3. **Modular**: Swap any agent or add custom stages
4. **Structured outputs**: All agents return JSON for system integration


---
