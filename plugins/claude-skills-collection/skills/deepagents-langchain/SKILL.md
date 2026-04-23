---
name: deepagents-langchain
description: DeepAgents — production-ready LangGraph agent framework by LangChain. Batteries-included: planning (write_todos), filesystem ops, shell execution, sub-agents with isolated context, auto context summarization. pip install deepagents → create_deep_agen
kind: agent
category: ai/agents
status: active
tags: [ai-agents, deepagents, langchain]
related_skills: [agent-development, ai-agent-builder]
---

# deepagents-langchain

USE FOR:
  - "production-ready agent with LangGraph"
  - "batteries-included coding/research agent"
  - "sub-agents with isolated context windows"
  - "LangChain agent framework"
  - "agent with planning + filesystem + shell"
  - "MCP tools in LangGraph agent"
tags: [LangGraph, LangChain, agent, production, sub-agents, MCP, planning, filesystem, shell, open-source]
kind: framework
category: ai-agent-builder

---

## What Is DeepAgents?

Production-ready, batteries-included LangGraph agent by LangChain.
No manual setup — `create_deep_agent()` returns a fully functional agent.

- Repo: https://github.com/langchain-ai/deepagents
- Install: `pip install deepagents`
- Framework: **LangGraph** (compiled graph, streaming, persistence, checkpointing)
- LangGraph Studio compatible

---

## Quick Start

```python
pip install deepagents
```

```python
from deepagents import create_deep_agent

agent = create_deep_agent()
result = agent.invoke({
    "messages": [{"role": "user", "content": "Research the latest AI agent frameworks and summarize"}]
})
print(result["messages"][-1].content)
```

---

## Built-in Capabilities

| Capability | Tools Included |
|-----------|---------------|
| **Planning** | `write_todos` — task decomposition + progress tracking |
| **Filesystem** | read, write, edit, search files |
| **Shell** | execute commands (with sandboxing) |
| **Sub-agents** | delegate tasks with isolated context windows |
| **Context** | auto-summarization, large output → file handling |

---

## Architecture (LangGraph)

```python
# Returns a compiled LangGraph graph
agent = create_deep_agent()

# Supports all LangGraph features:
# - Streaming
for chunk in agent.stream({"messages": [("user", "task")]}):
    print(chunk)

# - Persistence / checkpointing
from langgraph.checkpoint.memory import MemorySaver
agent = create_deep_agent(checkpointer=MemorySaver())

# - LangGraph Studio compatibility (visual debug)
```

---

## Customization

```python
from deepagents import create_deep_agent
from langchain_anthropic import ChatAnthropic

# Custom model
agent = create_deep_agent(
    model=ChatAnthropic(model="claude-opus-4-6")
)

# Add custom tools
from langchain_core.tools import tool

@tool
def my_tool(query: str) -> str:
    """Custom tool description"""
    return do_something(query)

agent = create_deep_agent(tools=[my_tool])

# Custom system prompt
agent = create_deep_agent(
    system_prompt="You are an expert financial analyst..."
)
```

---

## MCP Integration

```python
from langchain_mcp_adapters import MCPToolkit

# Connect any MCP server
toolkit = MCPToolkit(server_command=["npx", "gitnexus", "mcp"])
mcp_tools = toolkit.get_tools()

agent = create_deep_agent(tools=mcp_tools)
```

---

## Sub-Agents Pattern

```python
# Main agent delegates to sub-agents with isolated contexts
# Sub-agents don't share main agent's conversation history
# Useful for: parallel research, isolated code execution

agent = create_deep_agent(
    enable_subagents=True,
    subagent_model=ChatAnthropic(model="claude-haiku-4-5-20251001")  # cheaper for subtasks
)
```

---

## Use Cases

- **Research pipeline**: fetch + summarize + synthesize across sources
- **Code automation**: read codebase → plan changes → edit files → run tests
- **Data processing**: ingest files → transform → write outputs
- **Multi-step workflows**: plan → delegate subtasks → aggregate results

---

## vs. Other Agent Frameworks

| Feature | DeepAgents | OpenAlice | AutoHedge |
|---------|-----------|-----------|-----------|
| Framework | LangGraph | Custom TS | Swarms |
| Built-in tools | ✓ (full) | ✓ (trading) | ✓ (trading) |
| Sub-agents | ✓ | ✗ | ✗ |
| MCP support | ✓ | ✓ (planned) | ✗ |
| Domain | General | Trading | Trading |
| Studio UI | ✓ LangGraph | ✓ Web | ✗ |


---
