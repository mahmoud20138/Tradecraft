---
name: trading-agents-llm
description: Multi-agent LLM trading framework that mirrors real-world trading firm dynamics. Specialized agents (Fundamentals, Sentiment, News, Technical analysts + Researcher debate + Trader + Risk Manager) collaborate to analyze markets and make trading decisi
kind: agent
category: trading/ai-agents
status: active
tags: [ai-agents, ai-agents, llm, news, risk-and-portfolio, sentiment, trading]
related_skills: [ai-trading-crew, analyze, autohedge-swarm, freqtrade-bot, openalice-trading-agent]
---

# trading-agents-llm

USE FOR:
  - "build multi-agent trading system"
  - "LLM-powered stock analysis pipeline"
  - "analyst + researcher + trader + risk manager agent workflow"
  - "AI agent debate for trading decisions"
  - "integrate Claude / GPT / Gemini into trading research"
  - "A-share / HK / US equity LLM analysis"
  - "automate fundamental + sentiment + news + technical analysis"
tags: [multi-agent, LLM, trading, AI, equities, fundamentals, sentiment, technical, risk, LangGraph, Claude, GPT, research]
kind: framework
category: quant-ml-trading

---

## What Is TradingAgents?

Open-source multi-agent LLM framework that simulates a trading firm:
- Specialized agents collaborate across the full research → decision pipeline
- Uses **LangGraph** for agent orchestration
- Supports 6+ LLM providers including Anthropic Claude
- **Research only** — not financial advice

Repos:
- Original: https://github.com/TauricResearch/TradingAgents
- CN Enhanced Fork: https://github.com/hsliuping/TradingAgents-CN

---

## Agent Architecture

```
┌─────────────────── ANALYST TEAM ───────────────────┐
│  Fundamentals Analyst  →  Financial metrics & value │
│  Sentiment Analyst     →  Social media & mood       │
│  News Analyst          →  Macro news & events       │
│  Technical Analyst     →  MACD, RSI, patterns       │
└─────────────────────────────────────────────────────┘
            ↓ Reports fed into ↓
┌─────────────── RESEARCHER TEAM ────────────────────┐
│  Bullish Researcher  ↔  Bearish Researcher (debate) │
│  Critical assessment of analyst findings            │
└─────────────────────────────────────────────────────┘
            ↓ Debate synthesis ↓
┌─────────────── TRADER AGENT ───────────────────────┐
│  Synthesizes all reports → trading decision         │
│  Determines timing and position magnitude           │
└─────────────────────────────────────────────────────┘
            ↓ Proposal submitted ↓
┌─────────── RISK MANAGEMENT TEAM ───────────────────┐
│  Portfolio Manager   → approves / rejects trades    │
│  Risk evaluator      → volatility + liquidity check │
└─────────────────────────────────────────────────────┘
```

---

## Installation (Original)

```bash
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents
conda create -n tradingagents python=3.13
conda activate tradingagents
pip install -r requirements.txt
```

**Required API Keys:**
```bash
export OPENAI_API_KEY="sk-..."         # or any supported provider
export ANTHROPIC_API_KEY="sk-ant-..." # for Claude
export ALPHA_VANTAGE_API_KEY="..."     # market data
```

---

## Usage

### CLI (Interactive)
```bash
python -m cli.main
# Select: ticker, date, LLM provider, research depth
```

### Python API
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "anthropic"          # Use Claude
config["deep_think_llm"] = "claude-opus-4-6"  # Complex reasoning
config["quick_think_llm"] = "claude-haiku-4-5-20251001"  # Fast tasks
config["max_debate_rounds"] = 3               # Researcher debate depth
config["online_tools"] = True                 # Live market data

ta = TradingAgentsGraph(debug=True, config=config)
state, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)  # BUY / SELL / HOLD + rationale
```

---

## LLM Provider Configuration

| Provider | `llm_provider` | Models |
|----------|---------------|--------|
| Anthropic | `"anthropic"` | claude-opus-4-6, claude-sonnet-4-6, claude-haiku-4-5 |
| OpenAI | `"openai"` | gpt-4o, gpt-4o-mini, o1 |
| Google | `"google"` | gemini-2.0-flash, gemini-1.5-pro |
| xAI | `"xai"` | grok-2 |
| OpenRouter | `"openrouter"` | Any model via router |
| Ollama | `"ollama"` | Local models (llama3, mistral, etc.) |
| DeepSeek | `"deepseek"` | deepseek-chat (CN fork) |
| Alibaba | `"alibaba"` | qwen models (CN fork) |

---

## CN Fork (TradingAgents-CN) — Key Enhancements

### Architecture Upgrade
- **Original**: Streamlit UI
- **CN Fork**: FastAPI + Vue 3 (enterprise-grade)

### Regional Market Support
| Market | Data Source |
|--------|-------------|
| A-shares (China) | Tushare, AkShare, BaoStock |
| HK Stocks | AkShare |
| US Equities | Alpha Vantage |

### Additional Features
- MongoDB + Redis dual database (persistent sessions, caching)
- Docker support (amd64 + ARM64)
- Report export: Markdown, Word, PDF
- Batch portfolio analysis
- SSE + WebSocket real-time progress
- News quality filtering + multi-layer assessment
- User auth + operation logging

### CN Fork Installation
```bash
git clone https://github.com/hsliuping/TradingAgents-CN.git
cd TradingAgents-CN
docker-compose up -d  # Easiest path (MongoDB + Redis included)
# or
pip install -r requirements.txt
```

---

## Trading Workflow (Step-by-Step)

```
1. Input: ticker + date
2. Analysts run in parallel → 4 reports
3. Researcher debate (N rounds) → bull/bear synthesis
4. Trader synthesizes → trade proposal (BUY/SELL/HOLD + size)
5. Risk manager evaluates volatility + liquidity
6. Portfolio manager: APPROVE or REJECT
7. Output: final decision + reasoning chain
```

---

## Integration With Claude

Use Claude as the reasoning backbone:
```python
config = {
    "llm_provider": "anthropic",
    "deep_think_llm": "claude-opus-4-6",    # Analyst/Researcher deep work
    "quick_think_llm": "claude-sonnet-4-6", # Fast classification tasks
    "max_debate_rounds": 2,
    "online_tools": True,
}
```

Claude's strength in structured reasoning makes it ideal for:
- Fundamental analysis reports (long-form reasoning)
- Researcher debate synthesis
- Risk rationale explanation

---

## Key Design Patterns (for building similar agents)

```python
# Pattern: Analyst role definition
analyst_prompt = """
You are a Fundamental Analyst. Evaluate the company's:
- Revenue growth, margins, P/E, debt ratios
- Competitive moat and sector dynamics
Return: structured report with BUY/NEUTRAL/SELL signal + confidence
"""

# Pattern: Debate orchestration (LangGraph)
from langgraph.graph import StateGraph

graph = StateGraph(TradingState)
graph.add_node("fundamentals_analyst", run_fundamentals)
graph.add_node("sentiment_analyst", run_sentiment)
graph.add_node("researcher_debate", run_debate)
graph.add_node("trader_decision", run_trader)
graph.add_node("risk_check", run_risk_manager)
graph.add_edge("fundamentals_analyst", "researcher_debate")
# ...
```


---
