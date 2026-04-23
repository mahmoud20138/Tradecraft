---
name: polymarket-prediction-agents
description: AI agent framework for autonomous trading on Polymarket prediction markets. Connects LLMs to Polymarket's DEX via Gamma API, supports RAG with Chroma DB, integrates news/betting/web-search data sources. Uses py-clob-client for on-chain order executio
kind: agent
category: trading/ai-agents
status: active
tags: [ai-agents, ai-agents, ict, news, polymarket, prediction, trading]
related_skills: [ai-trading-crew, autohedge-swarm, freqtrade-bot, openalice-trading-agent, ritmex-crypto-agent]
---

# polymarket-prediction-agents

USE FOR:
  - "trade on prediction markets with AI"
  - "Polymarket agent / bot"
  - "prediction market analysis with LLM"
  - "autonomous betting / event trading agent"
  - "RAG-powered market research pipeline"
  - "crypto prediction market automation"
tags: [polymarket, prediction-markets, crypto, DeFi, agents, LLM, RAG, Polygon, CLOB]
kind: framework
category: crypto-defi-trading

---

## What Is Polymarket Agents?

Developer framework for building autonomous AI agents that trade on **Polymarket** —
a decentralized prediction market platform on Polygon.

- Repo: https://github.com/Polymarket/agents
- License: MIT
- Runtime: Python 3.9
- **Note**: US persons and restricted jurisdictions cannot trade per ToS

---

## Architecture

```
┌──────────────── DATA LAYER ──────────────────┐
│  Gamma API       → market metadata & events   │
│  News providers  → relevant articles          │
│  Web search      → real-time information      │
│  Betting APIs    → odds & market sentiment    │
└───────────────────────┬──────────────────────┘
                        ↓
┌──────────────── AI LAYER ────────────────────┐
│  LLM (OpenAI / any)  → reasoning             │
│  RAG (Chroma DB)     → vectorized context    │
│  Prompt utilities    → structured queries    │
└───────────────────────┬──────────────────────┘
                        ↓
┌──────────────── EXECUTION LAYER ─────────────┐
│  py-clob-client  → CLOB order generation     │
│  Polygon wallet  → on-chain signing          │
│  Polymarket DEX  → order execution           │
└──────────────────────────────────────────────┘
```

---

## Installation

```bash
git clone https://github.com/Polymarket/agents.git
cd agents
virtualenv --python=python3.9 .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

**`.env` Configuration:**
```bash
POLYGON_WALLET_PRIVATE_KEY="0x..."   # Polygon wallet for trading
OPENAI_API_KEY="sk-..."              # LLM provider
POLYMARKET_API_KEY="..."             # Optional: API key tier
```

---

## CLI Usage

```bash
# List markets by volume
python scripts/python/cli.py get-all-markets --limit 5 --sort-by volume

# Get specific event
python scripts/python/cli.py get-market --market-id <id>

# Search markets by keyword
python scripts/python/cli.py get-markets --keyword "election" --limit 10
```

---

## Trading Execution

```python
# Run autonomous trading agent
python agents/application/trade.py

# The agent will:
# 1. Fetch current markets via Gamma API
# 2. Retrieve relevant news + RAG context
# 3. Query LLM for probability assessment
# 4. Compare to market price → find edge
# 5. Sign + submit order via py-clob-client
```

---

## RAG Integration

```python
from agents.utils.chroma import ChromaClient

# Vectorize news articles for retrieval
client = ChromaClient()
client.add_documents(news_articles)

# Query for market-relevant context
results = client.query("US election 2026 polling", n_results=5)
```

---

## Prediction Market Edge Formula

```
Edge = Estimated_Probability - Market_Price

If Edge > threshold → BUY YES / NO token
If Edge < -threshold → SELL or BUY opposite
```

LLM assesses probability from news + context; market price is the current token price (0–1).

---

## Key Components

| Component | Description |
|-----------|-------------|
| `Gamma API` | Polymarket's REST API for markets/events data |
| `py-clob-client` | Order book client for CLOB trading |
| `Chroma DB` | Vector store for RAG-based news retrieval |
| `Prompt utils` | LLM prompt engineering helpers |
| `trade.py` | Main agent execution loop |
| `cli.py` | CLI for market exploration |

---

## Extending the Agent

```python
# Custom analyst agent pattern
class MyPredictionAgent:
    def analyze(self, market: dict) -> float:
        context = self.rag.query(market["question"])
        news = self.news_api.get_recent(market["question"])
        
        prompt = f"""
        Question: {market['question']}
        Context: {context}
        News: {news}
        Current market price: {market['price']}
        
        Estimate the true probability (0-1) and justify.
        """
        response = self.llm.complete(prompt)
        return self.parse_probability(response)
```


---
