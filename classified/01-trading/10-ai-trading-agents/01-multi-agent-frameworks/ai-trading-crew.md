---
name: ai-trading-crew
description: AI Trading Crew — 50-agent AutoGen system for US stock analysis. 8 specialized teams (Technical, Fundamental, Macro, Sentiment, Quant, Risk, Execution, Strategy) reporting to a Head Coach supervisor. Risk team has veto power. Devil's Advocate agent f
kind: agent
category: trading/ai-agents
status: active
tags: [ai-agents, crew, risk-and-portfolio, sentiment, trading]
related_skills: [autohedge-swarm, freqtrade-bot, openalice-trading-agent, polymarket-prediction-agents, ritmex-crypto-agent]
---

# AI Trading Crew

USE FOR:
  - "50-agent trading crew simulation"
  - "AutoGen multi-agent stock analysis"
  - "devil's advocate + risk veto trading system"
  - "US stock consensus trading agent"
  - "multi-team agent debate for trading decisions"
  - "ChromaDB RAG for trading knowledge"
tags: [AutoGen, multi-agent, trading, US-stocks, Alpaca, Polygon, ChromaDB, RAG, risk-veto, paper-trading]
kind: framework
category: quant-ml-trading

---

## What Is AI Trading Crew?

50-agent AutoGen system simulating a collaborative trading firm for US equities.
- Repo: https://github.com/omer475/ai-trading-crew
- Framework: **AutoGen** (Microsoft multi-agent)
- LLM: OpenAI
- Broker: Alpaca (paper trading)
- Data: Polygon.io real-time market data
- Memory: ChromaDB RAG knowledge base

---

## Agent Architecture: 8 Teams + Head Coach

```
                    Head Coach (Supervisor)
                          ↑ synthesis
    ┌──────────┬──────────┼──────────┬──────────┐
    │          │          │          │          │
Technical  Fundamental  Macro    Sentiment   Quant
(7 agents) (7 agents) (6 agents) (6 agents) (6 agents)
    │          │          │          │          │
    └──────────┴──────────┼──────────┴──────────┘
                          │
                    Risk Management (5 agents) ← VETO POWER
                          │ approved?
                    Execution & Ops (5 agents)
                    Strategy & Special (8 agents)
                          │
                    Devil's Advocate ← contrarian challenge
                          │
                    Final Decision + Order
```

---

## Team Responsibilities

| Team | Agents | Specialty |
|------|--------|-----------|
| Technical Analysis | 7 | Chart patterns, indicators, price action |
| Fundamental Analysis | 7 | Earnings, P/E, balance sheet, moat |
| Macro & Economics | 6 | Fed policy, rates, sectors, macro |
| Sentiment & News | 6 | News NLP, social sentiment, analyst ratings |
| Quantitative | 6 | Statistical models, factor analysis, signals |
| **Risk Management** | 5 | **VETO authority** over all trades |
| Execution & Ops | 5 | Order routing, timing, slippage management |
| Strategy & Special | 8 | Special situations, M&A, catalysts |

---

## Trading Workflow

```
1. Input: python main.py --symbol AAPL

2. Teams debate internally via AutoGen GroupChat
   → Each team reaches internal consensus

3. Team leaders report to Head Coach
   → Cross-team synthesis

4. Risk Management review
   → Can VETO any trade (overrides Head Coach)

5. Devil's Advocate challenges recommendation
   → Forces bull/bear stress test

6. Head Coach final decision

7. Human approval gate (configurable)

8. Execution team submits order to Alpaca
```

---

## Installation

```bash
git clone https://github.com/omer475/ai-trading-crew
cd agents
pip install -r requirements.txt
cp .env.example .env
```

**`.env` keys required:**
```bash
OPENAI_API_KEY="sk-..."
ALPACA_API_KEY="..."
ALPACA_SECRET_KEY="..."
POLYGON_API_KEY="..."
```

---

## Usage

```bash
# Full 50-agent analysis
python main.py --symbol AAPL

# Quick 5-agent test mode
python main.py --symbol NVDA --test

# Output: consensus decision + rationale + risk assessment + order
```

---

## Key Design Patterns

### AutoGen GroupChat per Team
```python
# Each team runs internal debate
groupchat = autogen.GroupChat(
    agents=[tech_agent_1, tech_agent_2, ..., tech_agent_7],
    messages=[],
    max_round=5
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
```

### Risk Veto Pattern
```python
class RiskManager(autogen.AssistantAgent):
    def check_veto(self, proposal: dict) -> bool:
        if proposal["position_size"] > self.max_risk:
            return True   # VETO
        if proposal["volatility"] > self.vol_threshold:
            return True   # VETO
        return False      # Approved
```

### ChromaDB RAG Knowledge Base
```python
import chromadb
client = chromadb.Client()
collection = client.get_or_create_collection("trading_knowledge")

# Query before analysis
results = collection.query(
    query_texts=["AAPL earnings history semiconductor cycle"],
    n_results=5
)
```

---

## Unique Features vs Other Trading Agent Frameworks

| Feature | AI Trading Crew | TradingAgents | AutoHedge |
|---------|----------------|---------------|-----------|
| Agent count | **50 agents** | ~8 agents | ~4 agents |
| Veto mechanism | Risk team veto | Risk approval | Risk gate |
| Contrarian agent | Devil's Advocate | Bearish researcher | No |
| Framework | AutoGen | LangGraph | Swarms |
| Knowledge base | ChromaDB RAG | None | None |
| Markets | US stocks only | US stocks | Solana crypto |


---
