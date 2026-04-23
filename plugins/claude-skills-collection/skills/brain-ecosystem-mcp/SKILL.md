---
name: brain-ecosystem-mcp
description: Brain Ecosystem — 3 autonomous self-learning AI brains as MCP servers for Claude Code. Brain (280 tools): error memory, code intelligence, autonomous research. Trading Brain (181 tools): adaptive trading, paper trading, signal learning, backtesting. 
kind: reference
category: trading/orchestration
status: active
tags: [backtesting, brain, claude-code, ecosystem, mcp, orchestration, trading]
related_skills: [analyze, master-trading-workflow, trading-autopilot]
---

# brain-ecosystem-mcp

USE FOR:
  - "self-learning AI brain for Claude Code"
  - "persistent memory MCP server"
  - "autonomous research agent with hypothesis testing"
  - "trading brain with adaptive strategies"
  - "MCP server with 280+ tools"
  - "AI that learns from errors across sessions"
  - "dream mode memory consolidation"
tags: [MCP, self-learning, autonomous, Claude-Code, Trading-Brain, error-memory, knowledge-graph, CCXT, persistent-memory, Hebbian]
kind: tool
category: mcp-integration

---

## What Is Brain Ecosystem?

3 autonomous self-learning AI brains running as MCP servers, designed for Claude Code.

- Repo: https://github.com/timmeck/brain-ecosystem
- Install: `npm install -g @timmeck/brain && brain setup`
- Architecture: Each brain = separate process, separate SQLite DB, separate port
- Communication: IPC named pipes between brains (Hebbian synapse network)
- Dashboard: Command Center at `localhost:7790` (13 pages of metrics)

> "117+ autonomous engines run in feedback loops — observing, detecting anomalies,
> forming hypotheses, testing and falsifying them statistically"

---

## Three Brains

| Brain | Port | Tools | Specialty |
|-------|------|-------|-----------|
| **Brain** | 7777-7778 | **280** | Error memory, code intelligence, autonomous research |
| **Trading Brain** | 7779-7780 | **181** | Adaptive trading, paper trading, signal learning, backtesting |
| **Marketing Brain** | 7781-7782 | **177** | Content strategy, cross-platform optimization |
| Command Center | 7790 | — | Unified dashboard, 13 monitoring pages |

---

## Installation

```bash
# Main brain
npm install -g @timmeck/brain
brain setup        # configures Claude Code MCP automatically

# Trading brain
npm install -g @timmeck/trading-brain
trading setup

# Marketing brain
npm install -g @timmeck/marketing-brain
marketing setup
```

**For Cursor/Windsurf/Cline** (HTTP/SSE):
```json
{
  "mcpServers": {
    "brain": {
      "url": "http://localhost:7778/sse"
    }
  }
}
```

---

## Brain (280 MCP Tools)

### Core Capabilities
- **Error Memory**: Tracks every error across sessions, learns solutions, never repeats
- **Code Intelligence**: Understands codebase structure, dependencies, patterns
- **Autonomous Research**: Multi-step roadmaps, hypothesis generation + falsification
- **Knowledge Graph**: Persistent cross-session knowledge with entity relationships
- **Dream Mode**: Offline memory consolidation (runs when idle)
- **Self-modification**: Can edit own code with human approval gates

### Research Engine
```
Goal → decompose → sub-goals → hypotheses
    → test statistically (17 falsification methods)
    → confirm/reject → update knowledge graph
    → synthesize report
```

### Data Sources
- Brave Search + Playwright (web research)
- Firecrawl (deep page extraction)
- GitHub (code assimilation from repos)
- Vision: Anthropic + Ollama (image analysis)

---

## Trading Brain (181 MCP Tools)

### Capabilities
- **Adaptive strategies**: Learn which signals work, weight by performance
- **Paper trading**: Simulate with real market data before live
- **Signal learning**: Identify patterns that predicted past moves
- **Backtesting**: Automated strategy evaluation with feedback loops
- **Live data**: CCXT WebSocket (100+ exchanges) + CoinGecko

### How It Adapts
```
Trade executed → outcome recorded
→ signal that preceded it gets weighted up/down
→ strategy parameters auto-adjusted
→ anomaly detection flags regime changes
→ hypothesis: "this pattern no longer works" → test → confirm → disable
```

---

## Self-Learning Architecture

```
Input (error/trade/content event)
    ↓
117 autonomous engines in parallel feedback loops:
    - AnomalyDetector
    - HypothesisGenerator
    - StatisticalFalsifier
    - PatternRecognizer
    - KnowledgeGraphUpdater
    - DreamConsolidator (offline)
    ↓
Hebbian synapse: brains share relevant discoveries
    ↓
Knowledge persists in SQLite → available next session
```

---

## Dream Mode (Memory Consolidation)

When idle (no active requests):
```
Brain enters "dream mode":
1. Replays recent experiences
2. Identifies patterns not obvious during active processing
3. Prunes weak connections (low-weight knowledge)
4. Strengthens high-value patterns
5. Prepares summaries for fast retrieval next session
```

---

## Claude Code Integration

After `brain setup`, Claude Code gets access to all 280 Brain tools:

```
# In Claude Code session — brain remembers across sessions:
> "You made an error with X last week"
→ Brain recalls error memory: exact context + solution applied

> "Research async patterns in Python"  
→ Brain creates 5-step research roadmap, executes autonomously,
  synthesizes findings into knowledge graph entry

> "What patterns have worked for BTCUSDT this month?"
→ Trading Brain queries signal performance history → ranked list
```

---

## Key Advantages Over Standard Memory Tools

| Feature | Brain Ecosystem | Standard MCP Memory |
|---------|----------------|---------------------|
| Error learning | ✓ (auto, cross-session) | Manual |
| Hypothesis testing | ✓ (statistical) | ✗ |
| Dream consolidation | ✓ | ✗ |
| Self-modification | ✓ (human-gated) | ✗ |
| Trading brain | ✓ (181 tools) | ✗ |
| Inter-brain comms | ✓ (Hebbian) | ✗ |
| Vision | ✓ (Anthropic+Ollama) | ✗ |



---
# KNOWLEDGE INJECTION: AntV MCP Server Chart
# Source: https://github.com/antvis/mcp-server-chart
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: mcp-server-chart
name: mcp-server-chart
description: >
  AntV MCP Server Chart - MCP server generating 26+ chart types via AntV.
  Tools: generate_bar_chart, generate_line_chart, generate_pie_chart,
  generate_network_graph, generate_sankey, generate_treemap, generate_spreadsheet, etc.
  npx @antv/mcp-server-chart. Works with Claude, VSCode, Dify.
USE FOR:
  - generate charts via MCP
  - bar/line/pie/scatter chart from data
  - network graph visualization
  - sankey treemap funnel chart
  - Claude generates charts automatically
tags: [MCP, charts, AntV, visualization, bar, line, pie, network-graph, sankey]
kind: tool
category: mcp-integration

---

## What Is mcp-server-chart?

MCP server generating 26+ visualization types using AntV.
- Repo: https://github.com/antvis/mcp-server-chart
- Install: `npm install -g @antv/mcp-server-chart`

### MCP Config (Claude Code / Desktop)
```json
{
  "mcpServers": {
    "mcp-server-chart": {
      "command": "npx",
      "args": ["-y", "@antv/mcp-server-chart"]
    }
  }
}
```

### Available Tools (generate_* pattern)
```
Standard:    area, bar, column, line, pie, scatter, dual_axes
Statistical: boxplot, histogram, violin
Flow:        funnel, sankey, treemap
Hierarchy:   mind_map, fishbone, org_chart
Network:     network_graph, venn
Geographic:  district_map, path_map, pin_map
Other:       radar, word_cloud, liquid, spreadsheet
```

### Usage in Claude
```
User: "Plot this data as a bar chart: [data]"
Claude: calls generate_bar_chart({ data: [...], xField: "x", yField: "y" })
→ returns chart image/URL
```

---
# KNOWLEDGE INJECTION: Dify
# Source: https://github.com/langgenius/dify
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: dify-llm-platform
name: dify-llm-platform
description: >
  Dify - open-source LLM app development platform. Visual canvas for AI workflows,
  RAG pipelines (PDF/PPT ingestion), agent builder (50+ tools: Google, DALL-E, Wolfram),
  LLMOps observability, BaaS APIs. Supports GPT, Claude, Llama3, Mistral, 100+ models.
  Self-host (Docker) or cloud (200 free GPT-4 calls).
USE FOR:
  - build LLM app with visual workflow
  - RAG pipeline from documents
  - AI agent with tools
  - self-hosted ChatGPT alternative
  - LLMOps monitoring
tags: [Dify, LLM, RAG, agent, workflow, visual, self-hosted, open-source, GPT, Claude]
kind: platform
category: ai-agent-builder

---

## What Is Dify?

Open-source LLM application development platform.
- Repo: https://github.com/langgenius/dify
- Stars: 100k+
- Deploy: Docker Compose (2 CPU, 4GB RAM) or dify.ai cloud

### Core Capabilities
- **Visual Workflow Canvas**: drag-and-drop LLM pipeline builder
- **RAG**: ingest PDFs, PPTs, web pages → vector search → grounded answers
- **Agent Builder**: Function Calling or ReAct agents + 50+ built-in tools
- **Model Hub**: GPT-4o, Claude, Llama3, Mistral, Gemini, + OpenAI-compatible
- **LLMOps**: trace every call, monitor cost, replay prompts
- **BaaS API**: REST API for any app to call your workflow

### Docker Install
```bash
git clone https://github.com/langgenius/dify
cd dify/docker
cp .env.example .env
docker compose up -d
# Access: http://localhost/install
```

### Agent Tools (50+)
Google Search, Bing, DuckDuckGo, Wikipedia, DALL-E, Stable Diffusion,
WolframAlpha, Weather API, News API, Code execution, Web scraping, + custom tools

---
# KNOWLEDGE INJECTION: Open WebUI
# Source: https://github.com/open-webui/open-webui
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: open-webui
name: open-webui
description: >
  Open WebUI - self-hosted, offline-capable AI platform. Ollama + OpenAI-compatible
  backends. RAG with 9 vector DBs, web search (15+ providers), image gen (DALL-E/ComfyUI),
  voice/video chat, Python function calling, enterprise auth (LDAP/OAuth/SCIM).
  Docker install. Privacy-first local AI deployment.
USE FOR:
  - self-hosted ChatGPT alternative
  - local Ollama web interface
  - offline AI with RAG
  - multi-model comparison
  - enterprise private AI deployment
tags: [Open-WebUI, Ollama, self-hosted, RAG, local-AI, privacy, ChatGPT-alternative]
kind: platform
category: ai-agent-builder

---

## What Is Open WebUI?

Extensible self-hosted AI platform — runs fully offline.
- Repo: https://github.com/open-webui/open-webui
- Supports: Ollama (local LLMs) + any OpenAI-compatible API

### Quick Install
```bash
# With Ollama bundled
docker run -d -p 3000:8080 --gpus=all   -v ollama:/root/.ollama -v open-webui:/app/backend/data   --name open-webui ghcr.io/open-webui/open-webui:ollama

# Existing Ollama
docker run -d -p 3000:8080   --add-host=host.docker.internal:host-gateway   -v open-webui:/app/backend/data   --name open-webui ghcr.io/open-webui/open-webui:main
# Access: http://localhost:3000
```

### Key Features vs ChatGPT
| Feature | Open WebUI | ChatGPT |
|---------|------------|---------|
| Self-hosted | Yes | No |
| Offline | Yes | No |
| Local models | Ollama | No |
| RAG | 9 vector DBs | Limited |
| Web search | 15+ providers | Yes |
| Image gen | DALL-E/ComfyUI/A1111 | DALL-E only |
| Python tools | Native | Sandboxed |
| Cost | Free | $20/mo |

---
# KNOWLEDGE INJECTION: Awesome MCP Servers (Reference)
# Source: https://github.com/punkpeye/awesome-mcp-servers
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Awesome MCP Servers — Ecosystem Reference

500+ MCP servers across 40+ categories. Key ones by domain:

### Development & Code
| Server | What It Does |
|--------|-------------|
| GitHub MCP | Repos, PRs, issues, code search |
| GitLab MCP | GitLab API integration |
| Filesystem MCP | Local file read/write/search |
| Git MCP | git log, diff, branch operations |
| Docker MCP | Container management |
| Kubernetes MCP | Cluster insights, kubectl |

### AI & Agents
| Server | What It Does |
|--------|-------------|
| Memory MCP | Persistent knowledge graph |
| Sequential Thinking | Chain-of-thought reasoning |
| Fetch/Browser | Web content retrieval |
| Playwright MCP | Browser automation |
| AgentShield | Security vulnerability scanning |

### Data & Databases
| Server | What It Does |
|--------|-------------|
| PostgreSQL MCP | Schema inspection + queries |
| MongoDB MCP | Document DB queries |
| Elasticsearch MCP | Search and analytics |
| Snowflake MCP | Data warehouse queries |
| SQLite MCP | Local database |

### Communication
| Server | What It Does |
|--------|-------------|
| Gmail MCP | Email read/send/search |
| Slack MCP | Channel messages, search |
| Telegram MCP | Bot messages |
| Discord MCP | Server interaction |

### Productivity
| Server | What It Does |
|--------|-------------|
| Notion MCP | Pages, databases, blocks |
| Jira MCP | Issues, sprints, projects |
| Google Calendar MCP | Events, scheduling |
| Airtable MCP | Base/table operations |

### Finance & Trading
| Server | What It Does |
|--------|-------------|
| Crypto APIs | Price feeds, portfolio |
| Payment MCP | Stripe, payment processing |
| Multi-cloud cost | Cloud cost analysis |

### Search & Data
| Server | What It Does |
|--------|-------------|
| Brave Search | Web search |
| Firecrawl | Deep web scraping |
| EXA MCP | AI-powered search |
| 75+ data extractors | Specialized data sources |

Full list: https://github.com/punkpeye/awesome-mcp-servers

---
# KNOWLEDGE INJECTION: Everything Claude Code
# Source: https://github.com/affaan-m/everything-claude-code
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Everything Claude Code — Production Optimization Reference

Complete system for maximizing Claude Code performance (10+ months production-tested).

### Components Overview
| Component | Count | Purpose |
|-----------|-------|---------|
| Agents | 21-25 | Specialized subagents (planner, architect, reviewer, security, language-specific) |
| Skills | 102+ | Domain workflows (TDD, security review, frontend/backend patterns) |
| Commands | 52-57 | Slash commands: /tdd, /plan, /code-review, /build-fix, /e2e |
| Rules | 29-34 | Universal + language-specific (TS, Python, Go, Swift, PHP, Java) |
| Hooks | 8-20+ | PreToolUse, PostToolUse, Stop, SessionStart automations |
| MCP | 14+ | Pre-configured: GitHub, Supabase, Vercel, Railway |

### Key Slash Commands
```
/tdd           - Test-driven development workflow
/plan          - Architecture planning
/code-review   - Security + quality review
/build-fix     - Build error diagnosis
/e2e           - End-to-end test generation
/multi-plan    - Multi-agent orchestration
/instinct-status - Check learned patterns
/evolve        - Extract patterns from session into skills
```

### Token Optimization Strategies
- Use Haiku/Sonnet for simple tasks, Opus for complex reasoning
- Compress context with /compact before long sessions
- Use subagents with limited scope (avoid full context bleed)
- Skills reduce re-explanation overhead
- Auto-extract patterns → reusable skills over time

### Hooks Patterns
```json
{
  "hooks": {
    "PreToolUse": ["secret-detector", "format-checker"],
    "PostToolUse": ["session-persist", "pattern-extractor"],
    "Stop": ["summary-generator"],
    "SessionStart": ["context-loader", "instinct-injector"]
  }
}
```

### Specialized Agents
- **planner**: breaks task into subtasks, creates task graph
- **architect**: system design, file structure decisions
- **code-reviewer**: security + style + logic review
- **security-reviewer**: OWASP, injection, auth vulnerabilities
- **go/python/ts-reviewer**: language-specific best practices

---
# KNOWLEDGE INJECTION: Cherry Studio
# Source: https://github.com/CherryHQ/cherry-studio
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: cherry-studio
name: cherry-studio
description: >
  Cherry Studio - desktop AI client for Windows/Mac/Linux. Unifies 20+ AI providers:
  OpenAI, Anthropic Claude, Gemini, Ollama (local), LM Studio, Qwen, Kimi.
  300+ pre-configured assistants, multi-model simultaneous chat, MCP server support,
  document processing (PDF/Office/images), no environment setup needed.
USE FOR:
  - unified desktop AI client
  - multi-model comparison chat
  - local + cloud AI in one app
  - 300+ pre-built AI assistants
  - MCP integration desktop
tags: [Cherry-Studio, desktop, multi-model, Ollama, Claude, GPT, Gemini, MCP, assistants]
kind: tool
category: ai-agent-builder

---

## What Is Cherry Studio?

Unified desktop AI client — no setup required.
- Repo: https://github.com/CherryHQ/cherry-studio
- Platforms: Windows, macOS, Linux
- Models: 20+ providers, local (Ollama/LM Studio) + cloud

### Supported Providers
OpenAI (GPT-4o) · Anthropic (Claude) · Google (Gemini) · Mistral
Ollama (local) · LM Studio (local) · Qwen · Kimi · Baidu · iFlytek
OpenRouter · Perplexity · Poe · + more

### Key Features
- **300+ assistants**: pre-configured prompts for coding, writing, analysis
- **Multi-model chat**: send same prompt to multiple models simultaneously
- **Document processing**: PDF, Word, Excel, PowerPoint, images
- **MCP support**: connect MCP servers (with Marketplace planned)
- **WebDAV sync**: sync conversations across devices
- **No setup**: download → login/API key → use immediately

---
# KNOWLEDGE INJECTION: AionUi
# Source: https://github.com/iOfficeAI/AionUi
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: aionui-desktop-agent
name: aionui-desktop-agent
description: >
  AionUi - free open-source multi-agent desktop platform (macOS/Windows/Linux).
  Auto-detects Claude Code, Codex, Qwen Code CLI tools. 20+ AI providers.
  Cron scheduling for 24/7 unattended automation. File management, Excel AI,
  PowerPoint generation, image recognition. Remote access via Telegram/Lark/DingTalk.
USE FOR:
  - multi-agent desktop automation
  - unify Claude Code + Codex in one UI
  - cron scheduled AI tasks
  - file batch rename organize
  - Excel AI processing
  - remote AI control via Telegram
tags: [AionUi, desktop-agent, multi-agent, Claude-Code, automation, scheduling, Telegram, remote]
kind: tool
category: ai-agent-builder

---

## What Is AionUi?

Multi-agent desktop platform — AI agents operate autonomously on your computer.
- Repo: https://github.com/iOfficeAI/AionUi
- Platforms: macOS · Windows · Linux
- Install: download desktop app, sign in with Google or API key

### Key Differentiators
- **Auto-detects** existing Claude Code, Codex, Qwen Code CLIs → unifies them
- **Built-in agent**: no CLI setup needed (full file/web/code capabilities)
- **Multi-agent**: run Claude Code + Codex simultaneously, independent contexts

### Supported Models (20+ providers)
Gemini · Anthropic Claude · OpenAI · Qwen · Kimi · Baidu · Ollama · LM Studio

### Automation Capabilities
| Feature | Description |
|---------|-------------|
| Cron scheduling | Natural language task descriptions, runs 24/7 |
| File management | Batch rename, intelligent classification |
| Excel processing | AI analysis, formatting, report generation |
| Document generation | PowerPoint, Word, Markdown automated creation |
| Image operations | Text-to-image, editing, recognition |

### Remote Access
- WebUI (browser access)
- Telegram bot integration
- Lark/Feishu (enterprise)
- DingTalk


---
# KNOWLEDGE INJECTION: Awesome Agent Skills (VoltAgent)
# Source: https://github.com/VoltAgent/awesome-agent-skills
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Awesome Agent Skills — Curated Registry (549+ skills)

Real-world agent skills from 40+ organizations. Works with Claude Code, Codex,
Gemini CLI, Cursor, GitHub Copilot.

Source: https://github.com/VoltAgent/awesome-agent-skills

### Notable Skills by Category

**Official / Anthropic**
- `anthropics/docx` — Create, edit, analyze Word documents
- PDF, presentations, design, web artifacts

**Infrastructure & DevOps**
- Vercel, Cloudflare, Netlify, AWS, Google Cloud skills
- HashiCorp Terraform code generation
- Kubernetes, Docker, CI/CD workflows

**Databases & Data**
- Supabase, Neon, ClickHouse, Tinybird

**Dev Frameworks**
- React, Next.js, React Native, Expo, WordPress

**AI/ML**
- Hugging Face, Replicate, fal.ai, OpenAI integration

**Security (Trail of Bits — 23 skills)**
- Insecure defaults detection
- Property-based testing + smart contracts
- Semgrep rule creation for vulnerability detection

**Product & SaaS**
- Content strategy planning
- Pricing/packaging/monetization strategy
- CAC, LTV, payback period calculations (saas-economics-efficiency-metrics)
- Investor materials, fundraising

**Web3/Crypto**
- Binance trading tools
- Blockchain interaction skills

**Security warning**: Skills are curated, not audited. Review before install.
Scanners: Snyk Skill Security Scanner, Agent Trust Hub.

---
# KNOWLEDGE INJECTION: wshobson/ai-trading-crew (112 agents, 146 skills)
# Source: https://github.com/wshobson/agents
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## wshobson/ai-trading-crew — 112 Agents + 146 Skills System

Production Claude Code plugin system: 112 agents, 146 skills, 79 tools, 72 plugins.

### Architecture
- 72 focused single-purpose plugins (1-6 per category)
- 23 categories, mix-and-match install
- 3-tier model: Opus (complex) / Sonnet (mid) / Haiku (simple)
- Progressive disclosure: skills load only when activated

### Install
```
/plugin marketplace add wshobson/agents
/plugin install python-development
/plugin install security-audit
```

### Key Plugin Categories
- Language specialists: Python, JS/TS, Go, Rust, systems
- Infrastructure: Kubernetes, cloud, CI/CD
- Security + compliance
- Data engineering + MLOps
- Full-stack + framework-specific
- Business ops + documentation
- Quantitative trading + risk management (limited)
- Payments: Stripe, PayPal, billing

---
# KNOWLEDGE INJECTION: Ruflo (Enterprise Agent Orchestration)
# Source: https://github.com/ruvnet/ruflo
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: ruflo-agent-orchestration
name: ruflo-agent-orchestration
description: >
  Ruflo (formerly Claude Flow) - enterprise multi-agent orchestration for Claude Code.
  60+ specialized agents in swarms (hierarchical/mesh/ring/star topologies).
  Self-learning SONA architecture, HNSW vector search (150x-12500x faster retrieval),
  EWC++ anti-forgetting, Mixture of Experts routing. MCP server.
  npx ruflo@latest init
USE FOR:
  - enterprise multi-agent orchestration
  - Claude Code swarm of agents
  - self-learning agent routing
  - 60+ specialized agents
  - MCP server for Claude Code
tags: [ruflo, multi-agent, swarm, orchestration, Claude-Code, MCP, self-learning, HNSW]
kind: framework
category: ai-agent-builder

---

## What Is Ruflo?

Enterprise AI agent orchestration platform built on Claude Code.
- Repo: https://github.com/ruvnet/ruflo
- Install: `npx ruflo@latest init --wizard`
- Claude Code MCP: `claude mcp add ruflo -- npx ruflo@latest mcp start`

### Key Differentiators vs CrewAI/LangGraph
| Feature | Ruflo | CrewAI | LangGraph |
|---------|-------|--------|-----------|
| Self-learning | SONA (0.05ms adapt) | No | No |
| Anti-forgetting | EWC++ | No | No |
| Vector retrieval | HNSW (12500x faster) | Basic | Basic |
| Agent topologies | 4 (hier/mesh/ring/star) | Hierarchical | Graph |
| Swarm size | Unlimited | Limited | Limited |

### Installation
```bash
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/claude-flow@main/scripts/install.sh | bash
# or
npx ruflo@latest init --wizard
```

### Usage
```bash
npx ruflo@latest --agent coder --task "Implement user authentication"
npx ruflo@latest --list                    # list all 60+ agents
npx ruflo@latest mcp start                 # start MCP server
```

### Swarm Topologies
```
Hierarchical: Queen agent → Worker agents (tree structure)
Mesh:         All agents peer-to-peer (collaborative)
Ring:         Sequential pipeline (A→B→C→A)
Star:         Central coordinator → spoke agents
```

---
# KNOWLEDGE INJECTION: alirezarezvani/claude-skills (204 skills)
# Source: https://github.com/alirezarezvani/claude-skills
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## claude-skills — 204 Production Skills Library

Most comprehensive open-source Claude Code skills library (204 skills, 266 Python CLI tools).
Compatible with 11 AI coding platforms.

### Skill Domains
| Domain | Skills | Notable |
|--------|--------|---------|
| Engineering Core | 25 | Architecture, DevOps, security, AI/ML |
| Engineering POWERFUL | 30 | Advanced tier skills |
| Playwright Testing | 9+ | Test generation, migration |
| Product Management | 13 | Strategy, UX research, analytics |
| Marketing | 43 | 7 specialized pods |
| Project Management | 6 | PM, scrum, Jira/Confluence |
| Regulatory/Quality | 12 | FDA, ISO, MDR, GDPR |
| C-Level Advisory | 28 | Full executive suite |
| Business & Growth | 4 | Customer success, sales |
| Finance | 2 | Financial analysis, SaaS metrics |

### Skill Structure
```
skill-name/
├── SKILL.md          # structured instructions + workflow
├── tools/            # Python CLI tools (standard library only)
│   └── tool_name.py
├── scripts/          # optional automation scripts
└── references/       # templates + domain knowledge
```

### Install
```bash
# Claude Code plugin marketplace
/plugin install alirezarezvani/claude-skills/engineering

# Manual: copy skill folder to ~/.claude/skills/
cp -r marketing-pod ~/.claude/skills/
```

---
# KNOWLEDGE INJECTION: ARIS (Auto Research in Sleep)
# Source: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: aris-auto-research
name: aris-auto-research
description: >
  ARIS - Autonomous ML research methodology using Claude Code + GPT adversarial reviewer.
  4 workflows: idea discovery, experiment bridge, auto-review loop, paper writing.
  20 composable skills. State file recovery (no daemon needed). GPU automation via SSH.
  Proven: borderline reject (5/10) -> submission-ready (7.5/10) in 4 overnight rounds.
USE FOR:
  - autonomous ML research overnight
  - auto paper review and improvement loop
  - GPU experiment automation SSH
  - academic paper writing Claude Code
  - cross-model adversarial review (Claude + GPT)
tags: [research, autonomous, ML, paper-writing, GPU, Claude-Code, adversarial-review, overnight]
kind: methodology
category: ai-agent-builder

---

## What Is ARIS?

Autonomous ML research methodology — Claude Code executes, GPT-5.4 reviews adversarially.

- Repo: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- Result: borderline reject → submission-ready in 4 overnight rounds (5/10 → 7.5/10)
- Philosophy: cross-model collaboration avoids local minima of self-critique

### 4 Workflows

```
Workflow 1:   Idea Discovery
              literature survey → 8-12 ideas → novelty check → GPU pilots → ranked report

Workflow 1.5: Experiment Bridge
              reads plan → implements code → validates small-scale → deploys full GPU suite

Workflow 2:   Auto Review Loop (key workflow)
              GPT-5.4 reviews paper → identifies gaps → Claude Code writes experiments
              → SSH deploys to GPU → monitors → rewrites sections → repeat (max 4 rounds)

Workflow 3:   Paper Writing
              narrative → claims-evidence matrix → figures/tables → LaTeX → PDF → 2-round auto-improve
```

### Slash Commands
```bash
/research-pipeline "your direction"   # full pipeline
/idea-discovery "topic"               # workflow 1
/experiment-bridge                    # workflow 1.5
/auto-review-loop "paper scope"       # workflow 2 (overnight key)
/paper-writing "NARRATIVE_REPORT.md"  # workflow 3

# With overrides:
/research-pipeline "topic" -- AUTO_PROCEED: false, wandb: true
```

### State Recovery (Persistence)
```
Each skill saves progress to JSON after every round:
  REVIEW_STATE.json
  AUTO_REVIEW.md

If session terminates mid-loop:
  Restart Claude Code → skill reads state → resumes from last checkpoint
```

### GPU Automation
Configure in project CLAUDE.md:
```
SSH_HOST: your-gpu-server.com
SSH_USER: ubuntu
CONDA_ENV: research
SLURM: true  # if using SLURM cluster
```
Skills handle: ssh → rsync code → conda activate → run experiments → fetch results

---
# KNOWLEDGE INJECTION: AI Maestro
# Source: https://github.com/23blocks-OS/ai-maestro
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: ai-maestro-orchestration
name: ai-maestro-orchestration
description: >
  AI Maestro - centralized dashboard for managing 35+ AI agents across machines.
  Peer mesh network (no central server), agent-to-agent messaging (AMP protocol),
  Code Graph visualization, Kanban task tracking, persistent memory, tmux auto-discovery.
  Gateway: Slack/Discord/Email/WhatsApp. curl install, Node.js 18+, tmux required.
USE FOR:
  - manage many AI agents from one dashboard
  - agent-to-agent communication
  - multi-machine AI coordination
  - Code Graph codebase visualization
  - tmux session management for agents
tags: [AI-Maestro, multi-agent, dashboard, tmux, mesh-network, AMP, Code-Graph, Kanban]
kind: tool
category: ai-agent-builder

---

## What Is AI Maestro?

Centralized dashboard for managing distributed AI agent workforces.
- Repo: https://github.com/23blocks-OS/ai-maestro
- Use case: built for devs managing 35+ agents across terminals

### Install
```bash
curl -fsSL https://raw.githubusercontent.com/23blocks-OS/ai-maestro/main/scripts/remote-install.sh | sh
# Requirements: Node.js 18+, tmux
```

### Core Features

| Feature | Description |
|---------|-------------|
| Auto-discovery | Finds existing tmux sessions automatically |
| Peer mesh | No central server — equal-status machines |
| AMP protocol | Agent-to-Agent Messaging with priority + crypto signatures |
| Code Graph | Interactive codebase visualization, delta indexing |
| Kanban | Task dependencies + status tracking |
| Persistent memory | Cross-session contextual continuity |
| War rooms | Multi-agent team assembly |
| Gateways | Slack, Discord, Email, WhatsApp routing |

### Agent Messaging Protocol (AMP)
```
Message types: command, query, response, broadcast
Priority: critical > high > normal > low
Signature: cryptographic for auth
Push notifications: real-time delivery
```

---
# KNOWLEDGE INJECTION: Babysitter (Agent Workflow Control)
# Source: https://github.com/a5c-ai/babysitter
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: babysitter-agent-control
name: babysitter-agent-control
description: >
  Babysitter - deterministic agent workflow framework. Process-as-code (JS functions),
  mandatory stops between steps, enforced quality gates, event-sourced audit journal.
  50-67% token compression. 2000+ pre-built process templates. 4 modes:
  interactive, autonomous (yolo), planning, continuous (forever monitoring).
USE FOR:
  - deterministic agent workflow (no hallucination drift)
  - quality convergence loops
  - human-in-the-loop agent control
  - resume interrupted agent workflows
  - parallel dependent task execution
  - 2000+ pre-built process templates
tags: [babysitter, deterministic, agent-control, quality-gates, audit-journal, workflow, Claude-Code]
kind: framework
category: ai-agent-builder

---

## What Is Babysitter?

Deterministic agent workflow framework — agents can only execute what the process permits.

- Repo: https://github.com/a5c-ai/babysitter
- Install: via Claude Code plugin marketplace

### Core Mechanisms

```
Process as Code  → JS functions define exactly what agents may do
Mandatory Stops  → every step halts; process logic decides next action
Enforced Gates   → quality thresholds block progression
Event Journal    → immutable audit trail, replay from any checkpoint
```

### 4 Execution Modes
```bash
/babysitter:call     # Interactive — pauses for human approval
/babysitter:yolo     # Autonomous — fully automatic
/babysitter:plan     # Planning — review before executing
/babysitter:forever  # Continuous — indefinite monitoring
```

### Quality Convergence
```javascript
// Automated refinement until threshold met
process.qualityGate({
  check: () => runTests(),
  threshold: 0.95,          // 95% pass rate required
  maxRounds: 5,             // max refinement attempts
  onFail: "refine-code"     // action if threshold not met
})
```

### Token Compression
50-67% context reduction built-in — summarizes completed steps, retains only active context.

### Run Resumption
```bash
/babysitter:observe    # live dashboard
/babysitter:resume     # continue interrupted workflow from checkpoint
```

### Pre-Built Process Library
2,000+ templates covering:
- Code review + refactoring
- Test generation
- Documentation
- Security audits
- Data pipeline validation
- Content generation


---
# KNOWLEDGE INJECTION: Skills Manager (jiweiyeah)
# Source: https://github.com/jiweiyeah/Skills-Manager
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: skills-manager-desktop
name: skills-manager-desktop
description: >
  Skills Manager - desktop app (Tauri 2.0 + React 19) for managing AI skills across
  multiple coding assistants. Write a skill once, sync via symlinks to Claude Code,
  Codex, Opencode simultaneously. Granular enable/disable per tool. Cross-platform
  (macOS/Windows/Linux). Monaco Editor for in-app skill editing.
USE FOR:
  - manage Claude Code skills across multiple AI tools
  - sync skills via symlinks no duplication
  - enable/disable skills per tool
  - visual skill editor desktop app
  - cross-tool skill management
tags: [skills-manager, Claude-Code, Codex, skills-sync, symlinks, Tauri, desktop, cross-platform]
kind: tool
category: ai-agent-builder

---

## What Is Skills Manager?

Centralized desktop app to manage AI assistant skills across Claude Code, Codex, Opencode, etc.
- Repo: https://github.com/jiweiyeah/Skills-Manager
- Stack: Tauri 2.0 (Rust) + React 19 + TypeScript + Tailwind CSS v4 + Radix UI + Monaco Editor
- Install: download from Releases (.dmg / .msi / .exe / .deb / .AppImage / .rpm)

### Key Features
- **Unified hub**: one place to write, edit, and organize skills
- **Smart sync**: symlinks prevent file duplication across tools
- **Granular control**: enable/disable skills per AI tool independently
- **In-app editor**: Monaco Editor for rich code/markdown editing
- **Auto-detect**: finds installed AI tools and their skill directories automatically

### Supported Tools
- Claude Code: `~/.claude/skills/`
- Codex CLI: `~/.codex/skills/`
- Opencode: `~/.opencode/skills/`
- Custom tools: configurable paths

### Windows Note
Requires Administrator privileges or Developer Mode enabled for symlink creation.

---
# KNOWLEDGE INJECTION: Claude Code Karma
# Source: https://github.com/JayantDevkar/claude-code-karma
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: claude-code-karma
name: claude-code-karma
description: >
  Claude Code Karma - local-first analytics dashboard for Claude Code sessions.
  Reads ~/.claude/ JSONL files, serves via FastAPI (port 8000), displays in SvelteKit UI
  (port 5173). No cloud, no accounts, no telemetry. Shows token usage, costs, cache hit rates,
  tool/agent distribution, file operations, plugin/skill/hook inventory, live session monitoring.
USE FOR:
  - visualize Claude Code session analytics
  - token usage and cost tracking
  - cache hit rate analysis
  - tool and agent usage statistics
  - file operation monitoring
  - plugin/skill/hook inventory dashboard
tags: [claude-code-karma, analytics, dashboard, token-usage, costs, sessions, FastAPI, SvelteKit]
kind: tool
category: ai-agent-builder

---

## What Is Claude Code Karma?

Local analytics dashboard for your Claude Code sessions.
- Repo: https://github.com/JayantDevkar/claude-code-karma
- Architecture: ~/.claude/ JSONL → FastAPI (8000) → SvelteKit (5173) → SQLite index
- No external calls — completely local

### Install
```bash
git clone https://github.com/JayantDevkar/claude-code-karma.git
cd claude-code-karma

# Terminal 1 — backend
cd api && pip install -e ".[dev]" && pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Terminal 2 — frontend
cd frontend && npm install && npm run dev
# Access: http://localhost:5173
```

### Dashboard Features
| View | What It Shows |
|------|---------------|
| Session Browser | All sessions with search/filter, real-time status |
| Analytics | Token usage, costs, cache hit rates, tool distribution |
| Project Organization | Workspaces by git repo + activity tracking |
| Tool & Agent Tracking | Built-in + MCP tools + custom agents + usage stats |
| File & Task Management | File operations, task creation/completion |
| Live Monitoring | Real-time via Claude Code hooks (optional) |
| Plugin Ecosystem | Installed plugins, skills, commands, hooks |

---
# KNOWLEDGE INJECTION: Swing Skills (whynowlab)
# Source: https://github.com/whynowlab/swing-skills
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: swing-trade-psychology-coach-firewall
name: swing-trade-psychology-coach-firewall
description: >
  Swing - 6-skill AI trade-psychology-coach firewall suite. Prevents systematic AI reasoning failures:
  ambiguous execution, unverified claims, anchoring, sycophancy, hidden reasoning, optimism bias.
  Skills: swing-clarify (5W1H), swing-research (4-stage verification), swing-options (5 alternatives),
  swing-review (steel-man + 3-vector critique), swing-trace (assumption mapping), swing-mortem
  (5-category failure projection). npx skills add whynowlab/swing-skills --all.
USE FOR:
  - prevent AI hallucination and overconfidence
  - 5W1H request decomposition before execution
  - source-tiered research with cross-validation
  - generate 5 probability-weighted alternatives
  - steel-man critique of decisions
  - assumption mapping and confidence analysis
  - pre-mortem failure projection
tags: [swing, trade-psychology-coach-firewall, clarify, research, options, review, trace, mortem, reasoning, Claude-Code]
kind: skills-suite
category: ai-agent-builder

---

## What Is Swing?

6-skill trade-psychology-coach firewall that addresses systematic AI reasoning failures.
- Repo: https://github.com/whynowlab/swing-skills
- Compatible: Claude Code (primary), Cursor, GitHub Copilot, Codex CLI

### Install
```bash
npx skills add whynowlab/swing-skills --all   # all 6 skills

# Individual:
npx skills add whynowlab/swing-skills/swing-clarify
npx skills add whynowlab/swing-skills/swing-research

# Manual:
cp -r swing-skills/skills/* ~/.claude/skills/
```

### The 6 Skills

| Skill | Problem Solved | Method |
|-------|---------------|--------|
| swing-clarify | Ambiguous requests rushed | 5W1H decomposition |
| swing-research | Unverified claims | 4-stage verification, S/A/B/C source grading |
| swing-options | Anchoring on obvious answer | 5 probability-weighted alternatives |
| swing-review | Sycophancy / no critique | Steel-man then 3-vector critical analysis |
| swing-trace | Hidden reasoning | Assumption map, decision forks, weakest-link |
| swing-mortem | Optimism bias | 5-category failure projection + leading indicators |

### Usage
```bash
/swing-clarify Build me an auth system
/swing-research Is gRPC better than REST for mobile?
/swing-review We chose Kubernetes for our 3-person startup
/swing-options Which database for real-time leaderboard?
/swing-trace Why do you recommend microservices?
/swing-mortem We are migrating to microservices in Q3
```

### Recommended Chain
```
clarify -> (research decision) -> options -> research -> review
        -> (risk analysis)     -> mortem
```

---
# KNOWLEDGE INJECTION: Spec-Flow (echoVic)
# Source: https://github.com/echoVic/spec-flow
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: spec-flow
name: spec-flow
description: >
  Spec-Flow - structured feature development workflow for AI coding agents. 5 sequential phases
  with approval gates: Proposal -> Requirements (EARS syntax) -> Design -> Tasks -> Implementation.
  Generates living markdown docs in .spec-flow/ directory. 3 modes: Step, Batch, Phase.
  Triggers: "spec-flow", "spec mode", "need a plan", "structured development".
  Install: git clone into ~/.claude/skills.
USE FOR:
  - structured feature development with AI
  - requirements specification EARS syntax
  - phase-gated AI coding workflow
  - living documentation .spec-flow directory
  - proposal -> requirements -> design -> tasks -> implementation
tags: [spec-flow, structured-development, requirements, EARS, phases, AI-workflow, Claude-Code]
kind: skill
category: ai-agent-builder

---

## What Is Spec-Flow?

Phase-gated structured development workflow for AI coding agents.
- Repo: https://github.com/echoVic/spec-flow
- Install: `cd ~/.claude/skills && git clone https://github.com/echoVic/spec-flow.git`
- Trigger: "spec-flow", "spec mode", "need a plan", or Chinese: "写个方案"

### 5 Phases (with human approval gates)
```
1. Proposal       → overview, scope, success criteria
2. Requirements   → EARS syntax specs (SHALL/WHEN/WHERE/IF clauses)
3. Design         → architecture, components, data models, interfaces
4. Tasks          → numbered implementation checklist, dependencies
5. Implementation → execute tasks one by one, verify each
```

### Execution Modes
```bash
# Default (step-by-step, confirmation at each phase)
spec-flow: Build user authentication system

# Fast (skip confirmations)
spec-flow --fast: Add dark mode toggle

# Simple (skip design phase)
spec-flow --skip-design: Fix the login bug
```

### Documentation Structure
```
.spec-flow/
  steering/     # project context, conventions
  active/       # in-progress feature docs
    feature-name/
      proposal.md
      requirements.md
      design.md
      tasks.md
  archive/      # completed features
```

### EARS Requirements Format
```
WHEN user submits login form
IF credentials are valid
THE SYSTEM SHALL authenticate the user and redirect to dashboard

WHERE the user is not authenticated
THE SYSTEM SHALL redirect to login page
```

---
# KNOWLEDGE INJECTION: HAM — Hierarchical Agent Memory
# Source: https://github.com/kromahlusenii-ops/ham
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: ham-hierarchical-memory
name: ham-hierarchical-memory
description: >
  HAM (Hierarchical Agent Memory) - reduces Claude Code token consumption 50% by replacing
  one massive CLAUDE.md with small scoped CLAUDE.md files at each directory level.
  Agent loads only 2-3 relevant files per session. Auto-detects project stack, self-maintaining
  (updates decision/pattern files as work progresses). Analytics dashboard at localhost:7777.
  Install: git clone into ~/.claude/skills/ham.
USE FOR:
  - reduce Claude Code token usage by 50%
  - hierarchical scoped CLAUDE.md files
  - context reduction hundreds vs thousands of tokens
  - self-maintaining memory decision files
  - ham dashboard analytics token savings
  - benchmark baseline vs HAM performance
tags: [HAM, hierarchical-memory, token-reduction, CLAUDE.md, context-management, Claude-Code, analytics]
kind: skill
category: ai-agent-builder

---

## What Is HAM?

Hierarchical Agent Memory — cuts Claude Code starting context from thousands of tokens to hundreds.
- Repo: https://github.com/kromahlusenii-ops/ham
- Install: `git clone https://github.com/kromahlusenii-ops/ham.git ~/.claude/skills/ham`
- Token reduction: up to 50%

### Core Concept
```
Before HAM:  One massive CLAUDE.md → loads entire project context every session
After HAM:   Small CLAUDE.md at each directory level → loads only 2-3 relevant files
```

### Commands
```bash
# Setup
go ham              # auto-configures everything
ham update          # refresh memory files
ham status          # show current memory state
ham route           # show which files will load for current directory

# Analytics (web UI at localhost:7777)
ham dashboard       # open analytics dashboard
ham savings         # show token savings report
ham carbon          # environmental impact calculator

# Benchmarking
ham benchmark       # run benchmark vs baseline
ham baseline start  # start baseline measurement
ham baseline stop   # stop baseline, compute metrics

# Maintenance
ham audit           # check for stale/missing memory files
ham commands        # list all available commands
```

### Memory Structure
```
project/
  CLAUDE.md              # global conventions, project overview
  src/
    CLAUDE.md            # frontend/backend patterns
    components/
      CLAUDE.md          # component-specific conventions
    api/
      CLAUDE.md          # API patterns, auth flows
  tests/
    CLAUDE.md            # testing patterns, fixtures
```

### Self-Maintaining Cycle
```
Read:  agent reads directory CLAUDE.md before starting work
Write: agent updates CLAUDE.md after completing work
       (new patterns, decisions, gotchas discovered)
```


---
# KNOWLEDGE INJECTION: geo-lint (IJONIS)
# Source: https://github.com/IJONIS/geo-lint
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: geo-lint
name: geo-lint
description: >
  geo-lint - first open-source linter for GEO (Generative Engine Optimization). 97 rules across
  5 categories: GEO (AI citation readiness, E-E-A-T, RAG optimization), SEO (metadata/schema/keywords),
  content quality, technical (broken links/perf), i18n. Agent-first JSON output for auto-fix loops.
  Ensures content gets cited by ChatGPT, Perplexity, Google AI Overviews, Gemini.
  npm install -D @ijonis/geo-lint. Claude Code skill: /geo-lint audit.
USE FOR:
  - optimize content for AI citation (GEO)
  - lint markdown for AI search visibility
  - automated fix loop until zero violations
  - E-E-A-T signal validation
  - RAG optimization for content
  - SEO + GEO combined content audit
tags: [geo-lint, GEO, SEO, AI-citation, content-optimization, RAG, E-E-A-T, Claude-Code, linter]
kind: tool
category: ai-agent-builder

---

## What Is geo-lint?

First open-source linter for Generative Engine Optimization — ensures content gets cited by AI search engines.
- Repo: https://github.com/IJONIS/geo-lint
- Install: `npm install -D @ijonis/geo-lint`
- Node.js 18+ required, zero peer dependencies

### Install
```bash
npm install -D @ijonis/geo-lint

# Claude Code users:
curl -fsSL https://raw.githubusercontent.com/IJONIS/geo-lint/main/install.sh | bash
```

### Commands
```bash
npx geo-lint                  # human-readable output
npx geo-lint --format=json    # machine-readable for AI agents
/geo-lint audit               # Claude Code skill: full site scan + fix
/content-creator setup        # create SEO/GEO-optimized content
```

### 97 Rules Across 5 Categories
| Category | Rules | Focus |
|----------|-------|-------|
| GEO | 36 | AI citation readiness, E-E-A-T signals, RAG optimization |
| SEO | 34 | Metadata, schema markup, keywords |
| Content Quality | 14 | Readability, word count, jargon |
| Technical | 10 | Broken links, performance |
| i18n | 3 | Translation pairs |

### Agent-First Fix Loop
```
geo-lint --format=json → violations with fix suggestions
→ AI agent modifies content
→ geo-lint re-runs
→ repeat until violations == 0
```

Each violation includes: file location, rule name, severity, plain-language fix instruction, machine-readable fix pattern.

### Supported Formats
- Markdown / MDX (native)
- Extensible: Astro, HTML, CMS platforms


---
# KNOWLEDGE INJECTION: Awesome Claude Code (hesreallyhim)
# Source: https://github.com/hesreallyhim/awesome-claude-code
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Awesome Claude Code — 400+ Resource Reference

Curated index of 400+ Claude Code extensions, skills, tools, hooks, and workflows.

### Agent Skills (Highlights)
- **Trail of Bits Security Skills** — 12+ skills for code auditing + vulnerability detection
- **Everything Claude Code** — Wide-ranging engineering domain skills
- **Fullstack Dev Skills** — 65 skills across full-stack frameworks + Jira
- **Claude Scientific Skills** — Research, engineering, finance, writing
- **Superpowers** — SDLC planning through debugging competencies
- **TACHES Resources** — Sub agents, skills, meta-skills, workflow adaptation
- **AgentSys** — Task-to-production, PR management, multi-agent review
- **Compound Engineering Plugin** — Error-to-learning discipline agents

### Orchestrators
- **Claude Swarm** — Multi-agent session orchestration
- **Claude Squad** — Terminal app, multiple agents in separate workspaces
- **Claude Task Master** — Task management for AI-driven development
- **Auto-Claude** — Multi-agent kanban UI for full SDLC automation
- **Claude Code Flow** — Code-first orchestration for autonomous agent cycles
- **TSK** — Rust CLI delegating to sandboxed Docker agents
- **Happy Coder** — Multi-instance control from phone/desktop

### Key Tools
- **claudekit** — CLI toolkit: auto-save, quality hooks, 20+ subagents
- **SuperClaude** — Configuration framework with commands and personas
- **cchistory** — Session command history like shell history
- **cclogviewer** — HTML UI for JSONL conversation files
- **recall** — Full-text session search with terminal interface
- **Container Use** — Safe multi-agent isolation environments
- **Rulesync** — Auto-generates configs for Claude Code, Cursor, others
- **claude-code-karma** — Analytics dashboard for sessions/tokens/costs (see separate entry)
- **Vibe-Log** — Local prompt analysis with session analytics

### Hooks (Highlights)
- **parry** — Prompt injection scanner detecting attacks/exfiltration
- **TDD Guard** — Blocks TDD-violating changes in real-time
- **Dippy** — Auto-approve safe bash, prompt for destructive operations
- **CC Notify** — Desktop notifications for input needs + task completion
- **cchooks** — Lightweight Python SDK with clean API

### Status Lines
- **claude-code-statusline** — 4-line statusline with themes and cost tracking
- **ccstatusline** — Customizable: model, branch, token usage
- **claude-powerline** — Vim-style powerline with real-time tracking
- **CCometixLine** — High-performance Rust statusline with git integration

### Key Slash Commands
| Command | Purpose |
|---------|---------|
| /commit | Conventional commit with emojis |
| /create-pr | PR creation workflow |
| /tdd | TDD enforcement |
| /check | Code quality + security checks |
| /context-prime | Comprehensive project priming |
| /prd-generator | Product Requirements Document generation |
| /optimize | Performance bottleneck identification |
| /mermaid | ER diagram generation from SQL |

### Workflow Systems (Highlights)
- **RIPER Workflow** — Research, Innovate, Plan, Execute, Review phases
- **AB Method** — Spec-driven, large problems into focused missions
- **Ralph Wiggum Techniques** — Autonomous loop with exit detection + safety
- **Claude Code PM** — Project management with specialized agents + commands
- **Simone** — Broader PM with documents, guidelines, processes
- **Spec-Flow** — Phase-gated structured development (see separate entry)

### Usage Monitors
- **Claude Code Usage Monitor** — Real-time terminal with burn rate predictions
- **CC Usage** — Dashboard for cost + token analysis
- **ccflare** — Web UI usage dashboard with comprehensive metrics

Full index: https://github.com/hesreallyhim/awesome-claude-code

---
# KNOWLEDGE INJECTION: Refly (refly-ai)
# Source: https://github.com/refly-ai/refly
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: refly-agent-skill-builder
name: refly-agent-skill-builder
description: >
  Refly - open-source platform transforming enterprise workflows into versioned agent skills.
  Copilot-led DSL compiler: describe workflow in natural language, compiles in <3 minutes.
  Intervenable runtime (pause/audit/redirect mid-execution). Exports to Claude Code, Cursor, MCP.
  3000+ native integrations: Stripe, Slack, Salesforce, GitHub, MCP servers.
  Central skill registry, version-controlled, team-shareable.
USE FOR:
  - codify business workflows as agent skills
  - natural language to agent skill compiler
  - intervenable runtime pause audit redirect
  - deploy skills as API webhook or Claude Code tool
  - 3000+ tool integrations for agent skills
tags: [Refly, agent-skills, enterprise, workflow, DSL, MCP, Claude-Code, versioned, registry]
kind: platform
category: ai-agent-builder

---

## What Is Refly?

Open-source platform for building versioned enterprise agent skills.
- Repo: https://github.com/refly-ai/refly
- Install: `npm install -g @powerformer/refly-cli`

### Architecture
```
Input Layer:     3000+ tools, MCP servers, private connectors
Processing Layer: Vibe-driven DSL compiler + stateful intervenable runtime
Output Layer:    Claude Code, Cursor, APIs, webhooks, agent frameworks
```

### Usage
```bash
npm install -g @powerformer/refly-cli

# Install a skill from registry
refly skill install <skill-id>

# Publish your skill
refly skill publish <skill-id>

# Execute workflow via API
curl -X POST https://instance/api/v1/workflows/{WORKFLOW_ID}/execute \
  -H "Authorization: Bearer API_KEY"
```

### Key Differentiators
- **Under 3 minutes** from natural language description to deployed skill
- **Intervenable**: pause, audit, redirect agent logic during execution (compliance-friendly)
- **Universal export**: skills become APIs, webhooks, or native Claude Code/Cursor tools
- **Central registry**: version-controlled skills shareable across teams

---
# KNOWLEDGE INJECTION: prompts.chat (f/prompts.chat)
# Source: https://github.com/f/prompts.chat
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## prompts.chat — World Largest Open-Source Prompt Library

143,000+ GitHub stars. Works with ChatGPT, Claude, Gemini, Llama, Mistral.
Originally launched as Awesome ChatGPT Prompts (Dec 2022).

### Access
```bash
# CLI
npx prompts.chat

# Claude Code plugin
/plugin install prompts.chat

# MCP server
# add to MCP config

# Browse online: https://prompts.chat/prompts
# CSV/Markdown/Hugging Face dataset available
```

### Key Facts
- 143,000+ GitHub stars
- 40+ academic citations
- Most liked dataset on Hugging Face
- CC0 1.0 license (public domain, unrestricted use)
- Featured by Forbes, Harvard, Columbia
- Self-hosting option available

### Categories
- Act As prompts (persona-based): Linux terminal, SQL terminal, JavaScript console, Excel sheet, etc.
- Writing and communication
- Analysis and research
- Code generation and review
- Educational explanations

### Prompt Engineering Guide
Free interactive guide with 25+ chapters on techniques:
- Zero-shot, few-shot, chain-of-thought
- Role prompting, output formatting
- Task decomposition, context injection

Full prompt browser: https://prompts.chat/prompts


---
# KNOWLEDGE INJECTION: LobeHub
# Source: https://github.com/lobehub/lobehub
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: lobehub-platform
name: lobehub-platform
description: >
  LobeHub - open-source AI platform for human-agent co-evolution. Web app + desktop + PWA.
  Multi-model (OpenAI, Ollama, 100+ providers), 10,000+ MCP plugins marketplace, agent builder,
  agent groups, personal memory, real-time internet search, chain-of-thought visualization,
  voice TTS/STT, image generation, knowledge base. Self-host via Docker or Vercel one-click.
USE FOR:
  - self-hosted multi-model AI platform
  - agent builder with customizable skills
  - MCP marketplace 10000+ plugins
  - team agent groups collaboration
  - personal memory adaptive learning
  - chain-of-thought visualization
tags: [LobeHub, LobeChat, multi-model, self-hosted, agents, MCP, Ollama, GPT, Claude, voice]
kind: platform
category: ai-agent-builder

---

## What Is LobeHub?

Open-source AI platform — web app, desktop, PWA with 10,000+ MCP plugins.
- Repo: https://github.com/lobehub/lobehub
- Main product: LobeChat — https://github.com/lobehub/lobe-chat

### Quick Deploy
```bash
# Docker
docker run -d -p 3210:3210 lobehub/lobe-chat

# Vercel one-click (or Zeabur, Sealos, Alibaba Cloud)
# Set OPENAI_API_KEY or other provider credentials
```

### Key Features
| Feature | Details |
|---------|---------|
| Multi-model | OpenAI, Ollama (local), Anthropic, Gemini, 100+ providers |
| MCP Marketplace | 10,000+ compatible plugins |
| Agent Builder | Custom agents with tools, memory, persona |
| Agent Groups | Team-based agent collaboration |
| Personal Memory | Adaptive learning across sessions |
| Internet Search | Real-time web integration |
| Chain of Thought | Visualize AI reasoning steps |
| Voice | TTS/STT conversational interface |
| Image Gen | Generation + visual recognition |
| Knowledge Base | File uploads, RAG |

---
# KNOWLEDGE INJECTION: claude-mem (thedotmack)
# Source: https://github.com/thedotmack/claude-mem
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: claude-mem
name: claude-mem
description: >
  claude-mem - persistent memory compression system for Claude Code. Auto-captures tool usage,
  generates semantic summaries, persists across sessions. Progressive disclosure (layered retrieval
  with token costs). mem-search skill for natural language history queries. 4 MCP tools: search,
  timeline, get_observations. Web viewer at localhost:37777. Private tag for sensitive content.
  Install via /plugin marketplace add thedotmack/claude-mem.
USE FOR:
  - persistent Claude Code memory across sessions
  - semantic session history search
  - context compression and retrieval
  - web UI for memory visualization
  - MCP tools for memory queries
tags: [claude-mem, persistent-memory, Claude-Code, session-continuity, compression, MCP, search]
kind: tool
category: ai-agent-builder

---

## What Is claude-mem?

Persistent memory compression system — context survives Claude Code session restarts.
- Repo: https://github.com/thedotmack/claude-mem
- Web UI: http://localhost:37777

### Install
```bash
# Via Claude Code Plugin Marketplace (recommended)
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
# Restart Claude Code

# Via OpenClaw Gateway
curl -fsSL https://install.cmem.ai/openclaw.sh | bash
```

### Features
- **Automatic**: captures tool usage, generates semantic summaries with no manual action
- **Progressive Disclosure**: layered retrieval showing token costs per memory level
- **mem-search skill**: natural language queries into project history
- **Privacy**: wrap content in `<private>` tags to exclude from memory
- **Citations**: reference past observations by ID

### MCP Tools
| Tool | Purpose |
|------|---------|
| search | Query memory index by natural language |
| timeline | Chronological context view |
| get_observations | Fetch full details by observation ID |

### Web Viewer (localhost:37777)
Real-time memory stream visualization + settings management.

---
# KNOWLEDGE INJECTION: Continue (continuedev)
# Source: https://github.com/continuedev/continue
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: continue-ai-code-review
name: continue-ai-code-review
description: >
  Continue - open-source AI-powered code review platform running agents on every PR as GitHub
  status checks. Review rules stored as markdown in .continue/checks/ directories (source-controlled).
  Returns green pass or red with suggested diffs. VS Code extension available. CLI via npm
  @continuedev/cli (cn command). macOS/Linux/Windows install. Custom checks for security,
  best practices, team conventions.
USE FOR:
  - AI code review on every pull request
  - source-controlled review rules markdown
  - GitHub status checks from AI agents
  - custom security and best practice checks
  - automated PR quality enforcement
tags: [Continue, AI-code-review, PR, GitHub-status-checks, CI, VS-Code, open-source]
kind: tool
category: ai-agent-builder

---

## What Is Continue?

Open-source AI code review platform — agents run on every PR as GitHub status checks.
- Repo: https://github.com/continuedev/continue
- CLI command: `cn`

### Install
```bash
# macOS/Linux
curl -fsSL https://install.continue.dev | bash

# Windows (PowerShell)
iwr https://install.continue.dev/windows -useb | iex

# Node.js alternative (Node 20+)
npm install -g @continuedev/cli
```

### How It Works
```
1. Store review rules as markdown in .continue/checks/
2. Continue runs agents on every PR
3. Returns GitHub status check: green (pass) or red (with suggested diffs)
4. Teams enforce rules as required status checks
```

### Review Rule Structure
```
.continue/
  checks/
    security.md       # security vulnerability rules
    best-practices.md # team coding standards
    custom-check.md   # any custom requirement
```

### VS Code Extension
Available through VS Code marketplace — provides IDE-level AI assistance integrated with the same agent framework.


---
# KNOWLEDGE INJECTION: memU (NevaMind-AI)
# Source: https://github.com/NevaMind-AI/memU
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: memu-proactive-memory
name: memu-proactive-memory
description: >
  memU - 24/7 always-on proactive memory framework for AI agents. Continuously captures user
  intent without explicit commands. Hierarchical 3-layer memory (Resource/Item/Category).
  Dual pathways: memorize() continuous learning + retrieve() RAG fast or LLM deep reasoning.
  92.09% accuracy on benchmarks. Reduces LLM token costs via cached insights.
  Storage: in-memory or PostgreSQL (pgvector). pip install -e .  Python 3.13+.
USE FOR:
  - 24/7 always-on agent memory
  - proactive user intent capture
  - hierarchical memory for AI agents
  - reduce LLM token costs via memory cache
  - RAG-based fast context retrieval
  - persistent agent memory PostgreSQL pgvector
tags: [memU, proactive-memory, AI-ai-agents, hierarchical-memory, RAG, pgvector, token-reduction, 24-7]
kind: framework
category: ai-agent-builder

---

## What Is memU?

24/7 proactive memory framework — AI agents learn continuously without explicit prompts.
- Repo: https://github.com/NevaMind-AI/memU
- Cloud: memu.so
- Python 3.13+ | OpenAI API key required

### Install
```bash
pip install -e .
export OPENAI_API_KEY=your_api_key
```

### Architecture
```
3-Layer Hierarchical Memory:
  Resource   → mountable data sources (docs, sessions, external feeds)
  Item       → individual memory facts with cross-references
  Category   → auto-organized topic clusters

Dual Retrieval Pathways:
  memorize() → continuous learning pipeline (immediate memory update)
  retrieve() → RAG fast (sub-second embedding) OR LLM deep (complex anticipation)
```

### Storage Options
```bash
# In-memory (default)
python tests/test_inmemory.py

# PostgreSQL with pgvector (persistent)
docker run -d --name memu-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 pgvector/pgvector:pg16
python tests/test_postgres.py
```

### Examples
```bash
python examples/example_1_conversation_memory.py  # session persistence
python examples/example_2_skill_extraction.py     # learn user skills
python examples/example_3_multimodal_memory.py    # images + text
```

### Performance
- 92.09% average accuracy on benchmark reasoning tasks
- Sub-second RAG retrieval
- Reduces redundant LLM calls via cached intent insights


---
# KNOWLEDGE INJECTION: LangChain
# Source: https://github.com/langchain-ai/langchain
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: langchain-framework
name: langchain-framework
description: >
  LangChain - leading framework for building LLM-powered applications and agents.
  Core: chains (sequential LLM pipelines), agents (tool-using reasoning loops),
  memory (conversation + long-term), RAG (retrieval-augmented generation), 100+ integrations
  (OpenAI, Anthropic, HuggingFace, Pinecone, Chroma, etc.). Model-agnostic: swap providers
  without code changes. Ecosystem: LangGraph (orchestration), LangSmith (debug/deploy).
  pip install langchain.
USE FOR:
  - build LLM application chains
  - tool-using agent with ReAct or function calling
  - RAG pipeline retrieval augmented generation
  - conversation memory management
  - swap LLM providers without changing code
  - integrate with vector stores Pinecone Chroma FAISS
tags: [LangChain, LLM, agents, chains, RAG, memory, tools, OpenAI, Anthropic, LangGraph, LangSmith]
kind: framework
category: ai-agent-builder

---

## What Is LangChain?

Framework for building LLM-powered applications — agents, chains, RAG, memory, tools.
- Repo: https://github.com/langchain-ai/langchain
- Stars: 100k+
- Ecosystem: LangChain + LangGraph + LangSmith

### Install
```bash
pip install langchain
pip install langchain-openai        # OpenAI provider
pip install langchain-anthropic     # Anthropic/Claude
pip install langchain-community     # community integrations
# or
uv add langchain
```

### Quick Start
```python
from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-4o")
result = model.invoke("Explain quantum computing in one sentence")

# Or Claude:
model = init_chat_model("anthropic:claude-sonnet-4-6")
```

### Core Components

**Chains** — Sequential LLM pipelines:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("Translate to French: {text}")
chain = prompt | ChatOpenAI(model="gpt-4o")
result = chain.invoke({"text": "Hello world"})
```

**Agents** — Tool-using reasoning loops:
```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun

tools = [DuckDuckGoSearchRun()]
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)
executor.invoke({"input": "What happened in AI this week?"})
```

**Memory** — Conversation persistence:
```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory)
```

**RAG Pipeline**:
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
qa_chain.invoke({"query": "What does the document say about X?"})
```

### Ecosystem
| Tool | Purpose |
|------|---------|
| LangGraph | Stateful multi-agent orchestration (cycles + branching) |
| LangSmith | LLM app monitoring, debugging, evaluation, deployment |
| LangServe | Deploy chains as REST APIs |

### 100+ Integrations
Models: OpenAI, Anthropic, HuggingFace, Cohere, Google, Ollama, Mistral
Vector Stores: Pinecone, Chroma, FAISS, Weaviate, Qdrant, pgvector
Tools: DuckDuckGo, SerpAPI, Wikipedia, Python REPL, SQL, Playwright
Document Loaders: PDF, Word, HTML, CSV, YouTube, Notion, GitHub


---
# KNOWLEDGE INJECTION: Vercel AI SDK
# Source: https://github.com/vercel/ai
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: vercel-ai-sdk
name: vercel-ai-sdk
description: >
  Vercel AI SDK - TypeScript toolkit for building AI apps with React/Next.js/Vue/Svelte/Node.js.
  Unified API across 20+ providers (OpenAI, Anthropic, Google, Groq, Mistral, DeepSeek, etc.).
  Core: generateText, streamText, generateObject, streamObject, tool calling, embeddings.
  UI hooks: useChat, useCompletion. npm install ai. Two libraries: AI SDK Core + AI SDK UI.
USE FOR:
  - build AI app with Next.js React
  - unified LLM API swap providers easily
  - streaming text and structured objects
  - tool calling function integration
  - useChat hook chat UI React
  - generateObject typed JSON from LLM
tags: [Vercel-AI-SDK, TypeScript, Next.js, React, streaming, generateText, useChat, tool-calling, OpenAI, Anthropic]
kind: framework
category: ai-agent-builder

---

## What Is the Vercel AI SDK?

TypeScript toolkit for building AI apps — unified API across 20+ LLM providers.
- Repo: https://github.com/vercel/ai
- Docs: https://ai-sdk.dev/docs
- Works with: React, Next.js, Vue, Svelte, Node.js

### Install
```bash
npm install ai
npm install @ai-sdk/openai      # OpenAI provider
npm install @ai-sdk/anthropic   # Anthropic/Claude
npm install @ai-sdk/google      # Google Gemini
```

### AI SDK Core

**Text Generation:**
```typescript
import { generateText, streamText } from "ai";
import { anthropic } from "@ai-sdk/anthropic";

// Single response
const { text } = await generateText({
  model: anthropic("claude-sonnet-4-6"),
  prompt: "Explain quantum computing",
});

// Streaming
const result = streamText({
  model: anthropic("claude-sonnet-4-6"),
  prompt: "Write a short story",
});
for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

**Structured Output:**
```typescript
import { generateObject } from "ai";
import { z } from "zod";

const { object } = await generateObject({
  model: openai("gpt-4o"),
  schema: z.object({
    name: z.string(),
    age: z.number(),
    skills: z.array(z.string()),
  }),
  prompt: "Generate a fictional developer profile",
});
```

**Tool Calling:**
```typescript
import { tool } from "ai";

const result = await generateText({
  model: openai("gpt-4o"),
  tools: {
    getWeather: tool({
      description: "Get weather for a city",
      parameters: z.object({ city: z.string() }),
      execute: async ({ city }) => fetchWeather(city),
    }),
  },
  prompt: "What is the weather in Paris?",
});
```

### AI SDK UI (React Hooks)

**useChat:**
```typescript
import { useChat } from "ai/react";

export default function ChatPage() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    api: "/api/chat",
  });
  return (
    <div>
      {messages.map(m => <div key={m.id}>{m.role}: {m.content}</div>)}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

### Supported Providers (20+)
OpenAI · Anthropic · Google · Azure · Amazon Bedrock · Groq · Mistral
Cohere · DeepSeek · xAI Grok · Together.ai · Fireworks · Perplexity · + more

### Core Functions Reference
| Function | Purpose |
|----------|---------|
| generateText | Single text response |
| streamText | Streaming text + tool calls |
| generateObject | Typed JSON (Zod schema) |
| streamObject | Streaming structured data |
| embed | Generate embeddings |
| embedMany | Batch embeddings |
| useChat | React hook for chat UI |
| useCompletion | React hook for text completion |
| useObject | React hook for streaming objects |


---
# KNOWLEDGE INJECTION: TensorZero
# Source: https://github.com/tensorzero/tensorzero
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: tensorzero-llm-gateway
name: tensorzero-llm-gateway
description: >
  TensorZero - open-source LLM gateway + optimization platform. Sub-millisecond routing to 18+
  providers (Anthropic, OpenAI, Google, AWS, etc.). Observability (PostgreSQL storage + OpenTelemetry),
  optimization (fine-tuning, GEPA prompt engineering, dynamic in-context learning), evaluation
  (heuristic + LLM judge), A/B testing + adaptive routing + fallbacks. Docker deploy.
  OpenAI-compatible API. Fortune 50 production use.
USE FOR:
  - unified LLM gateway 18+ providers
  - LLM observability and feedback collection
  - prompt optimization and fine-tuning
  - A/B testing LLM models
  - adaptive routing fallbacks retries
  - evaluate LLM outputs with judges
tags: [TensorZero, LLM-gateway, optimization, observability, fine-tuning, A/B-testing, OpenAI-compatible]
kind: platform
category: ai-agent-builder

---

## What Is TensorZero?

Production-grade LLM gateway with optimization, observability, evaluation, and experimentation.
- Repo: https://github.com/tensorzero/tensorzero
- Deploy: Docker
- API: OpenAI-compatible (drop-in replacement)

### Quick Start
```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:3000/openai/v1")
response = client.chat.completions.create(
    model="tensorzero::my_function::anthropic::claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Core Capabilities
| Feature | Details |
|---------|---------|
| Gateway | 18+ providers, sub-ms overhead, tool use, structured outputs, multimodal, caching |
| Observability | Stores inferences + feedback in PostgreSQL, OpenTelemetry, Prometheus |
| Optimization | Fine-tuning, GEPA automated prompt engineering, dynamic in-context learning |
| Evaluation | Heuristic benchmarks + LLM-as-judge for individual inferences |
| Experimentation | Built-in A/B testing, adaptive routing, fallbacks, retries |

### Supported Providers
Anthropic · OpenAI · Google Vertex/Gemini · AWS Bedrock/SageMaker · Azure
DeepSeek · Groq · Mistral · Together AI · vLLM · OpenAI-compatible APIs

---
# KNOWLEDGE INJECTION: PentAGI (vxcontrol)
# Source: https://github.com/vxcontrol/pentagi
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: pentagi-security-agents
name: pentagi-security-agents
description: >
  PentAGI - autonomous AI penetration testing platform. Multi-agent architecture:
  Orchestrator + Researcher + Developer + Executor + Searcher/Enricher/Memorist/Reporter.
  20+ built-in security tools (nmap, metasploit, sqlmap). Long-term vector memory (PostgreSQL).
  Knowledge graph (Neo4j). Sandboxed Docker execution. 10+ LLM providers. REST+GraphQL API.
  Grafana/Prometheus monitoring. For authorized security testing and research only.
USE FOR:
  - authorized automated penetration testing
  - multi-agent security research platform
  - vulnerability assessment automation
  - nmap metasploit sqlmap integration
  - AI-driven security tool orchestration
tags: [PentAGI, penetration-testing, security, multi-agent, nmap, metasploit, Docker, authorized-testing]
kind: platform
category: ai-agent-builder

---

## What Is PentAGI?

**For authorized security testing only.** Autonomous AI penetration testing platform.
- Repo: https://github.com/vxcontrol/pentagi
- Deploy: Docker Compose

### Agent Architecture
```
Orchestrator
  Researcher    → target analysis, intelligence gathering
  Developer     → attack strategy planning
  Executor      → implements attack plan
  Searcher      → information retrieval
  Enricher      → context enrichment
  Memorist      → long-term memory management
  Reporter      → results documentation
  Adviser       → strategy recommendations
  Reflector     → execution review
  Planner       → task decomposition (3-7 steps)
```

### Built-in Security Tools (20+)
nmap · metasploit · sqlmap · + 17 others

### Memory & Knowledge
- Long-term memory: vector embeddings in PostgreSQL
- Knowledge graph: Neo4j for semantic relationships
- Mentor supervision: detects repetitive patterns, suggests alternatives

### Supported LLM Providers
OpenAI · Anthropic · Google AI · AWS Bedrock · Ollama · + 5 others

### Limits & Safety
- Tool call limits: 100 (general agents), 20 (limited agents)
- Sandboxed Docker execution (complete isolation)
- Execution monitoring with automatic mentor intervention


---
# KNOWLEDGE INJECTION: Arize Phoenix
# Source: https://github.com/Arize-ai/phoenix
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: arize-phoenix-observability
name: arize-phoenix-observability
description: >
  Arize Phoenix - open-source AI observability platform. OpenTelemetry-based LLM tracing,
  LLM-powered evaluation (response + retrieval quality), version-controlled datasets, experiment
  tracking (prompts/models/retrieval). Integrates LangGraph, LlamaIndex, CrewAI, DSPy,
  Claude Agent SDK, OpenAI, Anthropic, Bedrock. Prompt playground + management.
  pip install arize-phoenix. Local/notebook/Docker/cloud.
USE FOR:
  - LLM application tracing and observability
  - evaluate LLM response and retrieval quality
  - version-controlled test datasets
  - track prompt model retrieval experiments
  - LangChain LangGraph LlamaIndex tracing
  - Claude agent SDK observability
tags: [Phoenix, Arize, observability, tracing, evaluation, LLM, OpenTelemetry, LangChain, LlamaIndex]
kind: platform
category: ai-agent-builder

---

## What Is Arize Phoenix?

Open-source AI observability — trace, evaluate, and experiment on LLM applications.
- Repo: https://github.com/Arize-ai/phoenix
- Cloud: app.phoenix.arize.com
- Vendor and language agnostic

### Install
```bash
pip install arize-phoenix

# Docker
docker pull arizephoenix/phoenix
docker run -p 6006:6006 arizephoenix/phoenix
# UI: http://localhost:6006
```

### 4 Core Capabilities
| Capability | What It Does |
|------------|-------------|
| Tracing | OpenTelemetry-based runtime tracing of LLM calls, chains, agents |
| Evaluation | LLM-powered benchmarks: response quality, retrieval accuracy |
| Datasets | Version-controlled example collections for testing + fine-tuning |
| Experiments | Track changes to prompts, models, retrieval — compare results |

### Quick Start
```python
import phoenix as px
from openinference.instrumentation.langchain import LangChainInstrumentor

# Start local Phoenix
session = px.launch_app()

# Auto-instrument LangChain
LangChainInstrumentor().instrument()

# All LangChain calls now traced at http://localhost:6006
```

### Supported Frameworks
LangGraph · LlamaIndex · CrewAI · DSPy · Claude Agent SDK
OpenAI · Anthropic · Google GenAI · AWS Bedrock

### Prompt Management
- Version-controlled prompt templates
- Tagging and rollback
- A/B comparison in playground
- Model comparison side-by-side


---
# KNOWLEDGE INJECTION: Awesome Agent Skills (VoltAgent)
# Source: https://github.com/VoltAgent/awesome-agent-skills
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Awesome Agent Skills — Curated Registry (549+ skills)

Real-world agent skills from 40+ organizations. Works with Claude Code, Codex,
Gemini CLI, Cursor, GitHub Copilot.

Source: https://github.com/VoltAgent/awesome-agent-skills

### Notable Skills by Category

**Official / Anthropic**
- `anthropics/docx` — Create, edit, analyze Word documents
- PDF, presentations, design, web artifacts

**Infrastructure & DevOps**
- Vercel, Cloudflare, Netlify, AWS, Google Cloud skills
- HashiCorp Terraform code generation
- Kubernetes, Docker, CI/CD workflows

**Databases & Data**
- Supabase, Neon, ClickHouse, Tinybird

**Dev Frameworks**
- React, Next.js, React Native, Expo, WordPress

**AI/ML**
- Hugging Face, Replicate, fal.ai, OpenAI integration

**Security (Trail of Bits — 23 skills)**
- Insecure defaults detection
- Property-based testing + smart contracts
- Semgrep rule creation for vulnerability detection

**Product & SaaS**
- Content strategy planning
- Pricing/packaging/monetization strategy
- CAC, LTV, payback period calculations (saas-economics-efficiency-metrics)
- Investor materials, fundraising

**Web3/Crypto**
- Binance trading tools
- Blockchain interaction skills

**Security warning**: Skills are curated, not audited. Review before install.
Scanners: Snyk Skill Security Scanner, Agent Trust Hub.

---
# KNOWLEDGE INJECTION: wshobson/ai-trading-crew (112 agents, 146 skills)
# Source: https://github.com/wshobson/agents
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## wshobson/ai-trading-crew — 112 Agents + 146 Skills System

Production Claude Code plugin system: 112 agents, 146 skills, 79 tools, 72 plugins.

### Architecture
- 72 focused single-purpose plugins (1-6 per category)
- 23 categories, mix-and-match install
- 3-tier model: Opus (complex) / Sonnet (mid) / Haiku (simple)
- Progressive disclosure: skills load only when activated

### Install
```
/plugin marketplace add wshobson/agents
/plugin install python-development
/plugin install security-audit
```

### Key Plugin Categories
- Language specialists: Python, JS/TS, Go, Rust, systems
- Infrastructure: Kubernetes, cloud, CI/CD
- Security + compliance
- Data engineering + MLOps
- Full-stack + framework-specific
- Business ops + documentation
- Quantitative trading + risk management (limited)
- Payments: Stripe, PayPal, billing

---
# KNOWLEDGE INJECTION: Ruflo (Enterprise Agent Orchestration)
# Source: https://github.com/ruvnet/ruflo
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: ruflo-agent-orchestration
name: ruflo-agent-orchestration
description: >
  Ruflo (formerly Claude Flow) - enterprise multi-agent orchestration for Claude Code.
  60+ specialized agents in swarms (hierarchical/mesh/ring/star topologies).
  Self-learning SONA architecture, HNSW vector search (150x-12500x faster retrieval),
  EWC++ anti-forgetting, Mixture of Experts routing. MCP server.
  npx ruflo@latest init
USE FOR:
  - enterprise multi-agent orchestration
  - Claude Code swarm of agents
  - self-learning agent routing
  - 60+ specialized agents
  - MCP server for Claude Code
tags: [ruflo, multi-agent, swarm, orchestration, Claude-Code, MCP, self-learning, HNSW]
kind: framework
category: ai-agent-builder

---

## What Is Ruflo?

Enterprise AI agent orchestration platform built on Claude Code.
- Repo: https://github.com/ruvnet/ruflo
- Install: `npx ruflo@latest init --wizard`
- Claude Code MCP: `claude mcp add ruflo -- npx ruflo@latest mcp start`

### Key Differentiators vs CrewAI/LangGraph
| Feature | Ruflo | CrewAI | LangGraph |
|---------|-------|--------|-----------|
| Self-learning | SONA (0.05ms adapt) | No | No |
| Anti-forgetting | EWC++ | No | No |
| Vector retrieval | HNSW (12500x faster) | Basic | Basic |
| Agent topologies | 4 (hier/mesh/ring/star) | Hierarchical | Graph |
| Swarm size | Unlimited | Limited | Limited |

### Installation
```bash
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/claude-flow@main/scripts/install.sh | bash
# or
npx ruflo@latest init --wizard
```

### Usage
```bash
npx ruflo@latest --agent coder --task "Implement user authentication"
npx ruflo@latest --list                    # list all 60+ agents
npx ruflo@latest mcp start                 # start MCP server
```

### Swarm Topologies
```
Hierarchical: Queen agent → Worker agents (tree structure)
Mesh:         All agents peer-to-peer (collaborative)
Ring:         Sequential pipeline (A→B→C→A)
Star:         Central coordinator → spoke agents
```

---
# KNOWLEDGE INJECTION: alirezarezvani/claude-skills (204 skills)
# Source: https://github.com/alirezarezvani/claude-skills
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## claude-skills — 204 Production Skills Library

Most comprehensive open-source Claude Code skills library (204 skills, 266 Python CLI tools).
Compatible with 11 AI coding platforms.

### Skill Domains
| Domain | Skills | Notable |
|--------|--------|---------|
| Engineering Core | 25 | Architecture, DevOps, security, AI/ML |
| Engineering POWERFUL | 30 | Advanced tier skills |
| Playwright Testing | 9+ | Test generation, migration |
| Product Management | 13 | Strategy, UX research, analytics |
| Marketing | 43 | 7 specialized pods |
| Project Management | 6 | PM, scrum, Jira/Confluence |
| Regulatory/Quality | 12 | FDA, ISO, MDR, GDPR |
| C-Level Advisory | 28 | Full executive suite |
| Business & Growth | 4 | Customer success, sales |
| Finance | 2 | Financial analysis, SaaS metrics |

### Skill Structure
```
skill-name/
├── SKILL.md          # structured instructions + workflow
├── tools/            # Python CLI tools (standard library only)
│   └── tool_name.py
├── scripts/          # optional automation scripts
└── references/       # templates + domain knowledge
```

### Install
```bash
# Claude Code plugin marketplace
/plugin install alirezarezvani/claude-skills/engineering

# Manual: copy skill folder to ~/.claude/skills/
cp -r marketing-pod ~/.claude/skills/
```

---
# KNOWLEDGE INJECTION: ARIS (Auto Research in Sleep)
# Source: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: aris-auto-research
name: aris-auto-research
description: >
  ARIS - Autonomous ML research methodology using Claude Code + GPT adversarial reviewer.
  4 workflows: idea discovery, experiment bridge, auto-review loop, paper writing.
  20 composable skills. State file recovery (no daemon needed). GPU automation via SSH.
  Proven: borderline reject (5/10) -> submission-ready (7.5/10) in 4 overnight rounds.
USE FOR:
  - autonomous ML research overnight
  - auto paper review and improvement loop
  - GPU experiment automation SSH
  - academic paper writing Claude Code
  - cross-model adversarial review (Claude + GPT)
tags: [research, autonomous, ML, paper-writing, GPU, Claude-Code, adversarial-review, overnight]
kind: methodology
category: ai-agent-builder

---

## What Is ARIS?

Autonomous ML research methodology — Claude Code executes, GPT-5.4 reviews adversarially.

- Repo: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
- Result: borderline reject → submission-ready in 4 overnight rounds (5/10 → 7.5/10)
- Philosophy: cross-model collaboration avoids local minima of self-critique

### 4 Workflows

```
Workflow 1:   Idea Discovery
              literature survey → 8-12 ideas → novelty check → GPU pilots → ranked report

Workflow 1.5: Experiment Bridge
              reads plan → implements code → validates small-scale → deploys full GPU suite

Workflow 2:   Auto Review Loop (key workflow)
              GPT-5.4 reviews paper → identifies gaps → Claude Code writes experiments
              → SSH deploys to GPU → monitors → rewrites sections → repeat (max 4 rounds)

Workflow 3:   Paper Writing
              narrative → claims-evidence matrix → figures/tables → LaTeX → PDF → 2-round auto-improve
```

### Slash Commands
```bash
/research-pipeline "your direction"   # full pipeline
/idea-discovery "topic"               # workflow 1
/experiment-bridge                    # workflow 1.5
/auto-review-loop "paper scope"       # workflow 2 (overnight key)
/paper-writing "NARRATIVE_REPORT.md"  # workflow 3

# With overrides:
/research-pipeline "topic" -- AUTO_PROCEED: false, wandb: true
```

### State Recovery (Persistence)
```
Each skill saves progress to JSON after every round:
  REVIEW_STATE.json
  AUTO_REVIEW.md

If session terminates mid-loop:
  Restart Claude Code → skill reads state → resumes from last checkpoint
```

### GPU Automation
Configure in project CLAUDE.md:
```
SSH_HOST: your-gpu-server.com
SSH_USER: ubuntu
CONDA_ENV: research
SLURM: true  # if using SLURM cluster
```
Skills handle: ssh → rsync code → conda activate → run experiments → fetch results

---
# KNOWLEDGE INJECTION: AI Maestro
# Source: https://github.com/23blocks-OS/ai-maestro
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: ai-maestro-orchestration
name: ai-maestro-orchestration
description: >
  AI Maestro - centralized dashboard for managing 35+ AI agents across machines.
  Peer mesh network (no central server), agent-to-agent messaging (AMP protocol),
  Code Graph visualization, Kanban task tracking, persistent memory, tmux auto-discovery.
  Gateway: Slack/Discord/Email/WhatsApp. curl install, Node.js 18+, tmux required.
USE FOR:
  - manage many AI agents from one dashboard
  - agent-to-agent communication
  - multi-machine AI coordination
  - Code Graph codebase visualization
  - tmux session management for agents
tags: [AI-Maestro, multi-agent, dashboard, tmux, mesh-network, AMP, Code-Graph, Kanban]
kind: tool
category: ai-agent-builder

---

## What Is AI Maestro?

Centralized dashboard for managing distributed AI agent workforces.
- Repo: https://github.com/23blocks-OS/ai-maestro
- Use case: built for devs managing 35+ agents across terminals

### Install
```bash
curl -fsSL https://raw.githubusercontent.com/23blocks-OS/ai-maestro/main/scripts/remote-install.sh | sh
# Requirements: Node.js 18+, tmux
```

### Core Features

| Feature | Description |
|---------|-------------|
| Auto-discovery | Finds existing tmux sessions automatically |
| Peer mesh | No central server — equal-status machines |
| AMP protocol | Agent-to-Agent Messaging with priority + crypto signatures |
| Code Graph | Interactive codebase visualization, delta indexing |
| Kanban | Task dependencies + status tracking |
| Persistent memory | Cross-session contextual continuity |
| War rooms | Multi-agent team assembly |
| Gateways | Slack, Discord, Email, WhatsApp routing |

### Agent Messaging Protocol (AMP)
```
Message types: command, query, response, broadcast
Priority: critical > high > normal > low
Signature: cryptographic for auth
Push notifications: real-time delivery
```

---
# KNOWLEDGE INJECTION: Babysitter (Agent Workflow Control)
# Source: https://github.com/a5c-ai/babysitter
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: babysitter-agent-control
name: babysitter-agent-control
description: >
  Babysitter - deterministic agent workflow framework. Process-as-code (JS functions),
  mandatory stops between steps, enforced quality gates, event-sourced audit journal.
  50-67% token compression. 2000+ pre-built process templates. 4 modes:
  interactive, autonomous (yolo), planning, continuous (forever monitoring).
USE FOR:
  - deterministic agent workflow (no hallucination drift)
  - quality convergence loops
  - human-in-the-loop agent control
  - resume interrupted agent workflows
  - parallel dependent task execution
  - 2000+ pre-built process templates
tags: [babysitter, deterministic, agent-control, quality-gates, audit-journal, workflow, Claude-Code]
kind: framework
category: ai-agent-builder

---

## What Is Babysitter?

Deterministic agent workflow framework — agents can only execute what the process permits.

- Repo: https://github.com/a5c-ai/babysitter
- Install: via Claude Code plugin marketplace

### Core Mechanisms

```
Process as Code  → JS functions define exactly what agents may do
Mandatory Stops  → every step halts; process logic decides next action
Enforced Gates   → quality thresholds block progression
Event Journal    → immutable audit trail, replay from any checkpoint
```

### 4 Execution Modes
```bash
/babysitter:call     # Interactive — pauses for human approval
/babysitter:yolo     # Autonomous — fully automatic
/babysitter:plan     # Planning — review before executing
/babysitter:forever  # Continuous — indefinite monitoring
```

### Quality Convergence
```javascript
// Automated refinement until threshold met
process.qualityGate({
  check: () => runTests(),
  threshold: 0.95,          // 95% pass rate required
  maxRounds: 5,             // max refinement attempts
  onFail: "refine-code"     // action if threshold not met
})
```

### Token Compression
50-67% context reduction built-in — summarizes completed steps, retains only active context.

### Run Resumption
```bash
/babysitter:observe    # live dashboard
/babysitter:resume     # continue interrupted workflow from checkpoint
```

### Pre-Built Process Library
2,000+ templates covering:
- Code review + refactoring
- Test generation
- Documentation
- Security audits
- Data pipeline validation
- Content generation


---
# KNOWLEDGE INJECTION: Awesome Claude Code (hesreallyhim)
# Source: https://github.com/hesreallyhim/awesome-claude-code
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Awesome Claude Code — 400+ Resource Reference

Curated index of 400+ Claude Code extensions, skills, tools, hooks, and workflows.

### Agent Skills (Highlights)
- **Trail of Bits Security Skills** — 12+ skills for code auditing + vulnerability detection
- **Everything Claude Code** — Wide-ranging engineering domain skills
- **Fullstack Dev Skills** — 65 skills across full-stack frameworks + Jira
- **Claude Scientific Skills** — Research, engineering, finance, writing
- **Superpowers** — SDLC planning through debugging competencies
- **TACHES Resources** — Sub agents, skills, meta-skills, workflow adaptation
- **AgentSys** — Task-to-production, PR management, multi-agent review
- **Compound Engineering Plugin** — Error-to-learning discipline agents

### Orchestrators
- **Claude Swarm** — Multi-agent session orchestration
- **Claude Squad** — Terminal app, multiple agents in separate workspaces
- **Claude Task Master** — Task management for AI-driven development
- **Auto-Claude** — Multi-agent kanban UI for full SDLC automation
- **Claude Code Flow** — Code-first orchestration for autonomous agent cycles
- **TSK** — Rust CLI delegating to sandboxed Docker agents
- **Happy Coder** — Multi-instance control from phone/desktop

### Key Tools
- **claudekit** — CLI toolkit: auto-save, quality hooks, 20+ subagents
- **SuperClaude** — Configuration framework with commands and personas
- **cchistory** — Session command history like shell history
- **cclogviewer** — HTML UI for JSONL conversation files
- **recall** — Full-text session search with terminal interface
- **Container Use** — Safe multi-agent isolation environments
- **Rulesync** — Auto-generates configs for Claude Code, Cursor, others
- **claude-code-karma** — Analytics dashboard for sessions/tokens/costs (see separate entry)
- **Vibe-Log** — Local prompt analysis with session analytics

### Hooks (Highlights)
- **parry** — Prompt injection scanner detecting attacks/exfiltration
- **TDD Guard** — Blocks TDD-violating changes in real-time
- **Dippy** — Auto-approve safe bash, prompt for destructive operations
- **CC Notify** — Desktop notifications for input needs + task completion
- **cchooks** — Lightweight Python SDK with clean API

### Status Lines
- **claude-code-statusline** — 4-line statusline with themes and cost tracking
- **ccstatusline** — Customizable: model, branch, token usage
- **claude-powerline** — Vim-style powerline with real-time tracking
- **CCometixLine** — High-performance Rust statusline with git integration

### Key Slash Commands
| Command | Purpose |
|---------|---------|
| /commit | Conventional commit with emojis |
| /create-pr | PR creation workflow |
| /tdd | TDD enforcement |
| /check | Code quality + security checks |
| /context-prime | Comprehensive project priming |
| /prd-generator | Product Requirements Document generation |
| /optimize | Performance bottleneck identification |
| /mermaid | ER diagram generation from SQL |

### Workflow Systems (Highlights)
- **RIPER Workflow** — Research, Innovate, Plan, Execute, Review phases
- **AB Method** — Spec-driven, large problems into focused missions
- **Ralph Wiggum Techniques** — Autonomous loop with exit detection + safety
- **Claude Code PM** — Project management with specialized agents + commands
- **Simone** — Broader PM with documents, guidelines, processes
- **Spec-Flow** — Phase-gated structured development (see separate entry)

### Usage Monitors
- **Claude Code Usage Monitor** — Real-time terminal with burn rate predictions
- **CC Usage** — Dashboard for cost + token analysis
- **ccflare** — Web UI usage dashboard with comprehensive metrics

Full index: https://github.com/hesreallyhim/awesome-claude-code

---
# KNOWLEDGE INJECTION: Refly (refly-ai)
# Source: https://github.com/refly-ai/refly
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: refly-agent-skill-builder
name: refly-agent-skill-builder
description: >
  Refly - open-source platform transforming enterprise workflows into versioned agent skills.
  Copilot-led DSL compiler: describe workflow in natural language, compiles in <3 minutes.
  Intervenable runtime (pause/audit/redirect mid-execution). Exports to Claude Code, Cursor, MCP.
  3000+ native integrations: Stripe, Slack, Salesforce, GitHub, MCP servers.
  Central skill registry, version-controlled, team-shareable.
USE FOR:
  - codify business workflows as agent skills
  - natural language to agent skill compiler
  - intervenable runtime pause audit redirect
  - deploy skills as API webhook or Claude Code tool
  - 3000+ tool integrations for agent skills
tags: [Refly, agent-skills, enterprise, workflow, DSL, MCP, Claude-Code, versioned, registry]
kind: platform
category: ai-agent-builder

---

## What Is Refly?

Open-source platform for building versioned enterprise agent skills.
- Repo: https://github.com/refly-ai/refly
- Install: `npm install -g @powerformer/refly-cli`

### Architecture
```
Input Layer:     3000+ tools, MCP servers, private connectors
Processing Layer: Vibe-driven DSL compiler + stateful intervenable runtime
Output Layer:    Claude Code, Cursor, APIs, webhooks, agent frameworks
```

### Usage
```bash
npm install -g @powerformer/refly-cli

# Install a skill from registry
refly skill install <skill-id>

# Publish your skill
refly skill publish <skill-id>

# Execute workflow via API
curl -X POST https://instance/api/v1/workflows/{WORKFLOW_ID}/execute \
  -H "Authorization: Bearer API_KEY"
```

### Key Differentiators
- **Under 3 minutes** from natural language description to deployed skill
- **Intervenable**: pause, audit, redirect agent logic during execution (compliance-friendly)
- **Universal export**: skills become APIs, webhooks, or native Claude Code/Cursor tools
- **Central registry**: version-controlled skills shareable across teams

---
# KNOWLEDGE INJECTION: prompts.chat (f/prompts.chat)
# Source: https://github.com/f/prompts.chat
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## prompts.chat — World Largest Open-Source Prompt Library

143,000+ GitHub stars. Works with ChatGPT, Claude, Gemini, Llama, Mistral.
Originally launched as Awesome ChatGPT Prompts (Dec 2022).

### Access
```bash
# CLI
npx prompts.chat

# Claude Code plugin
/plugin install prompts.chat

# MCP server
# add to MCP config

# Browse online: https://prompts.chat/prompts
# CSV/Markdown/Hugging Face dataset available
```

### Key Facts
- 143,000+ GitHub stars
- 40+ academic citations
- Most liked dataset on Hugging Face
- CC0 1.0 license (public domain, unrestricted use)
- Featured by Forbes, Harvard, Columbia
- Self-hosting option available

### Categories
- Act As prompts (persona-based): Linux terminal, SQL terminal, JavaScript console, Excel sheet, etc.
- Writing and communication
- Analysis and research
- Code generation and review
- Educational explanations

### Prompt Engineering Guide
Free interactive guide with 25+ chapters on techniques:
- Zero-shot, few-shot, chain-of-thought
- Role prompting, output formatting
- Task decomposition, context injection

Full prompt browser: https://prompts.chat/prompts


---
# KNOWLEDGE INJECTION: AntV MCP Server Chart
# Source: https://github.com/antvis/mcp-server-chart
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: mcp-server-chart
name: mcp-server-chart
description: >
  AntV MCP Server Chart - MCP server generating 26+ chart types via AntV.
  Tools: generate_bar_chart, generate_line_chart, generate_pie_chart,
  generate_network_graph, generate_sankey, generate_treemap, generate_spreadsheet, etc.
  npx @antv/mcp-server-chart. Works with Claude, VSCode, Dify.
USE FOR:
  - generate charts via MCP
  - bar/line/pie/scatter chart from data
  - network graph visualization
  - sankey treemap funnel chart
  - Claude generates charts automatically
tags: [MCP, charts, AntV, visualization, bar, line, pie, network-graph, sankey]
kind: tool
category: mcp-integration

---

## What Is mcp-server-chart?

MCP server generating 26+ visualization types using AntV.
- Repo: https://github.com/antvis/mcp-server-chart
- Install: `npm install -g @antv/mcp-server-chart`

### MCP Config (Claude Code / Desktop)
```json
{
  "mcpServers": {
    "mcp-server-chart": {
      "command": "npx",
      "args": ["-y", "@antv/mcp-server-chart"]
    }
  }
}
```

### Available Tools (generate_* pattern)
```
Standard:    area, bar, column, line, pie, scatter, dual_axes
Statistical: boxplot, histogram, violin
Flow:        funnel, sankey, treemap
Hierarchy:   mind_map, fishbone, org_chart
Network:     network_graph, venn
Geographic:  district_map, path_map, pin_map
Other:       radar, word_cloud, liquid, spreadsheet
```

### Usage in Claude
```
User: "Plot this data as a bar chart: [data]"
Claude: calls generate_bar_chart({ data: [...], xField: "x", yField: "y" })
→ returns chart image/URL
```

---
# KNOWLEDGE INJECTION: Dify
# Source: https://github.com/langgenius/dify
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: dify-llm-platform
name: dify-llm-platform
description: >
  Dify - open-source LLM app development platform. Visual canvas for AI workflows,
  RAG pipelines (PDF/PPT ingestion), agent builder (50+ tools: Google, DALL-E, Wolfram),
  LLMOps observability, BaaS APIs. Supports GPT, Claude, Llama3, Mistral, 100+ models.
  Self-host (Docker) or cloud (200 free GPT-4 calls).
USE FOR:
  - build LLM app with visual workflow
  - RAG pipeline from documents
  - AI agent with tools
  - self-hosted ChatGPT alternative
  - LLMOps monitoring
tags: [Dify, LLM, RAG, agent, workflow, visual, self-hosted, open-source, GPT, Claude]
kind: platform
category: ai-agent-builder

---

## What Is Dify?

Open-source LLM application development platform.
- Repo: https://github.com/langgenius/dify
- Stars: 100k+
- Deploy: Docker Compose (2 CPU, 4GB RAM) or dify.ai cloud

### Core Capabilities
- **Visual Workflow Canvas**: drag-and-drop LLM pipeline builder
- **RAG**: ingest PDFs, PPTs, web pages → vector search → grounded answers
- **Agent Builder**: Function Calling or ReAct agents + 50+ built-in tools
- **Model Hub**: GPT-4o, Claude, Llama3, Mistral, Gemini, + OpenAI-compatible
- **LLMOps**: trace every call, monitor cost, replay prompts
- **BaaS API**: REST API for any app to call your workflow

### Docker Install
```bash
git clone https://github.com/langgenius/dify
cd dify/docker
cp .env.example .env
docker compose up -d
# Access: http://localhost/install
```

### Agent Tools (50+)
Google Search, Bing, DuckDuckGo, Wikipedia, DALL-E, Stable Diffusion,
WolframAlpha, Weather API, News API, Code execution, Web scraping, + custom tools

---
# KNOWLEDGE INJECTION: Open WebUI
# Source: https://github.com/open-webui/open-webui
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: open-webui
name: open-webui
description: >
  Open WebUI - self-hosted, offline-capable AI platform. Ollama + OpenAI-compatible
  backends. RAG with 9 vector DBs, web search (15+ providers), image gen (DALL-E/ComfyUI),
  voice/video chat, Python function calling, enterprise auth (LDAP/OAuth/SCIM).
  Docker install. Privacy-first local AI deployment.
USE FOR:
  - self-hosted ChatGPT alternative
  - local Ollama web interface
  - offline AI with RAG
  - multi-model comparison
  - enterprise private AI deployment
tags: [Open-WebUI, Ollama, self-hosted, RAG, local-AI, privacy, ChatGPT-alternative]
kind: platform
category: ai-agent-builder

---

## What Is Open WebUI?

Extensible self-hosted AI platform — runs fully offline.
- Repo: https://github.com/open-webui/open-webui
- Supports: Ollama (local LLMs) + any OpenAI-compatible API

### Quick Install
```bash
# With Ollama bundled
docker run -d -p 3000:8080 --gpus=all   -v ollama:/root/.ollama -v open-webui:/app/backend/data   --name open-webui ghcr.io/open-webui/open-webui:ollama

# Existing Ollama
docker run -d -p 3000:8080   --add-host=host.docker.internal:host-gateway   -v open-webui:/app/backend/data   --name open-webui ghcr.io/open-webui/open-webui:main
# Access: http://localhost:3000
```

### Key Features vs ChatGPT
| Feature | Open WebUI | ChatGPT |
|---------|------------|---------|
| Self-hosted | Yes | No |
| Offline | Yes | No |
| Local models | Ollama | No |
| RAG | 9 vector DBs | Limited |
| Web search | 15+ providers | Yes |
| Image gen | DALL-E/ComfyUI/A1111 | DALL-E only |
| Python tools | Native | Sandboxed |
| Cost | Free | $20/mo |

---
# KNOWLEDGE INJECTION: Awesome MCP Servers (Reference)
# Source: https://github.com/punkpeye/awesome-mcp-servers
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Awesome MCP Servers — Ecosystem Reference

500+ MCP servers across 40+ categories. Key ones by domain:

### Development & Code
| Server | What It Does |
|--------|-------------|
| GitHub MCP | Repos, PRs, issues, code search |
| GitLab MCP | GitLab API integration |
| Filesystem MCP | Local file read/write/search |
| Git MCP | git log, diff, branch operations |
| Docker MCP | Container management |
| Kubernetes MCP | Cluster insights, kubectl |

### AI & Agents
| Server | What It Does |
|--------|-------------|
| Memory MCP | Persistent knowledge graph |
| Sequential Thinking | Chain-of-thought reasoning |
| Fetch/Browser | Web content retrieval |
| Playwright MCP | Browser automation |
| AgentShield | Security vulnerability scanning |

### Data & Databases
| Server | What It Does |
|--------|-------------|
| PostgreSQL MCP | Schema inspection + queries |
| MongoDB MCP | Document DB queries |
| Elasticsearch MCP | Search and analytics |
| Snowflake MCP | Data warehouse queries |
| SQLite MCP | Local database |

### Communication
| Server | What It Does |
|--------|-------------|
| Gmail MCP | Email read/send/search |
| Slack MCP | Channel messages, search |
| Telegram MCP | Bot messages |
| Discord MCP | Server interaction |

### Productivity
| Server | What It Does |
|--------|-------------|
| Notion MCP | Pages, databases, blocks |
| Jira MCP | Issues, sprints, projects |
| Google Calendar MCP | Events, scheduling |
| Airtable MCP | Base/table operations |

### Finance & Trading
| Server | What It Does |
|--------|-------------|
| Crypto APIs | Price feeds, portfolio |
| Payment MCP | Stripe, payment processing |
| Multi-cloud cost | Cloud cost analysis |

### Search & Data
| Server | What It Does |
|--------|-------------|
| Brave Search | Web search |
| Firecrawl | Deep web scraping |
| EXA MCP | AI-powered search |
| 75+ data extractors | Specialized data sources |

Full list: https://github.com/punkpeye/awesome-mcp-servers

---
# KNOWLEDGE INJECTION: Everything Claude Code
# Source: https://github.com/affaan-m/everything-claude-code
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

## Everything Claude Code — Production Optimization Reference

Complete system for maximizing Claude Code performance (10+ months production-tested).

### Components Overview
| Component | Count | Purpose |
|-----------|-------|---------|
| Agents | 21-25 | Specialized subagents (planner, architect, reviewer, security, language-specific) |
| Skills | 102+ | Domain workflows (TDD, security review, frontend/backend patterns) |
| Commands | 52-57 | Slash commands: /tdd, /plan, /code-review, /build-fix, /e2e |
| Rules | 29-34 | Universal + language-specific (TS, Python, Go, Swift, PHP, Java) |
| Hooks | 8-20+ | PreToolUse, PostToolUse, Stop, SessionStart automations |
| MCP | 14+ | Pre-configured: GitHub, Supabase, Vercel, Railway |

### Key Slash Commands
```
/tdd           - Test-driven development workflow
/plan          - Architecture planning
/code-review   - Security + quality review
/build-fix     - Build error diagnosis
/e2e           - End-to-end test generation
/multi-plan    - Multi-agent orchestration
/instinct-status - Check learned patterns
/evolve        - Extract patterns from session into skills
```

### Token Optimization Strategies
- Use Haiku/Sonnet for simple tasks, Opus for complex reasoning
- Compress context with /compact before long sessions
- Use subagents with limited scope (avoid full context bleed)
- Skills reduce re-explanation overhead
- Auto-extract patterns → reusable skills over time

### Hooks Patterns
```json
{
  "hooks": {
    "PreToolUse": ["secret-detector", "format-checker"],
    "PostToolUse": ["session-persist", "pattern-extractor"],
    "Stop": ["summary-generator"],
    "SessionStart": ["context-loader", "instinct-injector"]
  }
}
```

### Specialized Agents
- **planner**: breaks task into subtasks, creates task graph
- **architect**: system design, file structure decisions
- **code-reviewer**: security + style + logic review
- **security-reviewer**: OWASP, injection, auth vulnerabilities
- **go/python/ts-reviewer**: language-specific best practices

---
# KNOWLEDGE INJECTION: Cherry Studio
# Source: https://github.com/CherryHQ/cherry-studio
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: cherry-studio
name: cherry-studio
description: >
  Cherry Studio - desktop AI client for Windows/Mac/Linux. Unifies 20+ AI providers:
  OpenAI, Anthropic Claude, Gemini, Ollama (local), LM Studio, Qwen, Kimi.
  300+ pre-configured assistants, multi-model simultaneous chat, MCP server support,
  document processing (PDF/Office/images), no environment setup needed.
USE FOR:
  - unified desktop AI client
  - multi-model comparison chat
  - local + cloud AI in one app
  - 300+ pre-built AI assistants
  - MCP integration desktop
tags: [Cherry-Studio, desktop, multi-model, Ollama, Claude, GPT, Gemini, MCP, assistants]
kind: tool
category: ai-agent-builder

---

## What Is Cherry Studio?

Unified desktop AI client — no setup required.
- Repo: https://github.com/CherryHQ/cherry-studio
- Platforms: Windows, macOS, Linux
- Models: 20+ providers, local (Ollama/LM Studio) + cloud

### Supported Providers
OpenAI (GPT-4o) · Anthropic (Claude) · Google (Gemini) · Mistral
Ollama (local) · LM Studio (local) · Qwen · Kimi · Baidu · iFlytek
OpenRouter · Perplexity · Poe · + more

### Key Features
- **300+ assistants**: pre-configured prompts for coding, writing, analysis
- **Multi-model chat**: send same prompt to multiple models simultaneously
- **Document processing**: PDF, Word, Excel, PowerPoint, images
- **MCP support**: connect MCP servers (with Marketplace planned)
- **WebDAV sync**: sync conversations across devices
- **No setup**: download → login/API key → use immediately

---
# KNOWLEDGE INJECTION: AionUi
# Source: https://github.com/iOfficeAI/AionUi
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: aionui-desktop-agent
name: aionui-desktop-agent
description: >
  AionUi - free open-source multi-agent desktop platform (macOS/Windows/Linux).
  Auto-detects Claude Code, Codex, Qwen Code CLI tools. 20+ AI providers.
  Cron scheduling for 24/7 unattended automation. File management, Excel AI,
  PowerPoint generation, image recognition. Remote access via Telegram/Lark/DingTalk.
USE FOR:
  - multi-agent desktop automation
  - unify Claude Code + Codex in one UI
  - cron scheduled AI tasks
  - file batch rename organize
  - Excel AI processing
  - remote AI control via Telegram
tags: [AionUi, desktop-agent, multi-agent, Claude-Code, automation, scheduling, Telegram, remote]
kind: tool
category: ai-agent-builder

---

## What Is AionUi?

Multi-agent desktop platform — AI agents operate autonomously on your computer.
- Repo: https://github.com/iOfficeAI/AionUi
- Platforms: macOS · Windows · Linux
- Install: download desktop app, sign in with Google or API key

### Key Differentiators
- **Auto-detects** existing Claude Code, Codex, Qwen Code CLIs → unifies them
- **Built-in agent**: no CLI setup needed (full file/web/code capabilities)
- **Multi-agent**: run Claude Code + Codex simultaneously, independent contexts

### Supported Models (20+ providers)
Gemini · Anthropic Claude · OpenAI · Qwen · Kimi · Baidu · Ollama · LM Studio

### Automation Capabilities
| Feature | Description |
|---------|-------------|
| Cron scheduling | Natural language task descriptions, runs 24/7 |
| File management | Batch rename, intelligent classification |
| Excel processing | AI analysis, formatting, report generation |
| Document generation | PowerPoint, Word, Markdown automated creation |
| Image operations | Text-to-image, editing, recognition |

### Remote Access
- WebUI (browser access)
- Telegram bot integration
- Lark/Feishu (enterprise)
- DingTalk


---
# KNOWLEDGE INJECTION: geo-lint (IJONIS)
# Source: https://github.com/IJONIS/geo-lint
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: geo-lint
name: geo-lint
description: >
  geo-lint - first open-source linter for GEO (Generative Engine Optimization). 97 rules across
  5 categories: GEO (AI citation readiness, E-E-A-T, RAG optimization), SEO (metadata/schema/keywords),
  content quality, technical (broken links/perf), i18n. Agent-first JSON output for auto-fix loops.
  Ensures content gets cited by ChatGPT, Perplexity, Google AI Overviews, Gemini.
  npm install -D @ijonis/geo-lint. Claude Code skill: /geo-lint audit.
USE FOR:
  - optimize content for AI citation (GEO)
  - lint markdown for AI search visibility
  - automated fix loop until zero violations
  - E-E-A-T signal validation
  - RAG optimization for content
  - SEO + GEO combined content audit
tags: [geo-lint, GEO, SEO, AI-citation, content-optimization, RAG, E-E-A-T, Claude-Code, linter]
kind: tool
category: ai-agent-builder

---

## What Is geo-lint?

First open-source linter for Generative Engine Optimization — ensures content gets cited by AI search engines.
- Repo: https://github.com/IJONIS/geo-lint
- Install: `npm install -D @ijonis/geo-lint`
- Node.js 18+ required, zero peer dependencies

### Install
```bash
npm install -D @ijonis/geo-lint

# Claude Code users:
curl -fsSL https://raw.githubusercontent.com/IJONIS/geo-lint/main/install.sh | bash
```

### Commands
```bash
npx geo-lint                  # human-readable output
npx geo-lint --format=json    # machine-readable for AI agents
/geo-lint audit               # Claude Code skill: full site scan + fix
/content-creator setup        # create SEO/GEO-optimized content
```

### 97 Rules Across 5 Categories
| Category | Rules | Focus |
|----------|-------|-------|
| GEO | 36 | AI citation readiness, E-E-A-T signals, RAG optimization |
| SEO | 34 | Metadata, schema markup, keywords |
| Content Quality | 14 | Readability, word count, jargon |
| Technical | 10 | Broken links, performance |
| i18n | 3 | Translation pairs |

### Agent-First Fix Loop
```
geo-lint --format=json → violations with fix suggestions
→ AI agent modifies content
→ geo-lint re-runs
→ repeat until violations == 0
```

Each violation includes: file location, rule name, severity, plain-language fix instruction, machine-readable fix pattern.

### Supported Formats
- Markdown / MDX (native)
- Extensible: Astro, HTML, CMS platforms


---
# KNOWLEDGE INJECTION: LangChain
# Source: https://github.com/langchain-ai/langchain
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: langchain-framework
name: langchain-framework
description: >
  LangChain - leading framework for building LLM-powered applications and agents.
  Core: chains (sequential LLM pipelines), agents (tool-using reasoning loops),
  memory (conversation + long-term), RAG (retrieval-augmented generation), 100+ integrations
  (OpenAI, Anthropic, HuggingFace, Pinecone, Chroma, etc.). Model-agnostic: swap providers
  without code changes. Ecosystem: LangGraph (orchestration), LangSmith (debug/deploy).
  pip install langchain.
USE FOR:
  - build LLM application chains
  - tool-using agent with ReAct or function calling
  - RAG pipeline retrieval augmented generation
  - conversation memory management
  - swap LLM providers without changing code
  - integrate with vector stores Pinecone Chroma FAISS
tags: [LangChain, LLM, agents, chains, RAG, memory, tools, OpenAI, Anthropic, LangGraph, LangSmith]
kind: framework
category: ai-agent-builder

---

## What Is LangChain?

Framework for building LLM-powered applications — agents, chains, RAG, memory, tools.
- Repo: https://github.com/langchain-ai/langchain
- Stars: 100k+
- Ecosystem: LangChain + LangGraph + LangSmith

### Install
```bash
pip install langchain
pip install langchain-openai        # OpenAI provider
pip install langchain-anthropic     # Anthropic/Claude
pip install langchain-community     # community integrations
# or
uv add langchain
```

### Quick Start
```python
from langchain.chat_models import init_chat_model

model = init_chat_model("openai:gpt-4o")
result = model.invoke("Explain quantum computing in one sentence")

# Or Claude:
model = init_chat_model("anthropic:claude-sonnet-4-6")
```

### Core Components

**Chains** — Sequential LLM pipelines:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("Translate to French: {text}")
chain = prompt | ChatOpenAI(model="gpt-4o")
result = chain.invoke({"text": "Hello world"})
```

**Agents** — Tool-using reasoning loops:
```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun

tools = [DuckDuckGoSearchRun()]
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools)
executor.invoke({"input": "What happened in AI this week?"})
```

**Memory** — Conversation persistence:
```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory)
```

**RAG Pipeline**:
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
qa_chain.invoke({"query": "What does the document say about X?"})
```

### Ecosystem
| Tool | Purpose |
|------|---------|
| LangGraph | Stateful multi-agent orchestration (cycles + branching) |
| LangSmith | LLM app monitoring, debugging, evaluation, deployment |
| LangServe | Deploy chains as REST APIs |

### 100+ Integrations
Models: OpenAI, Anthropic, HuggingFace, Cohere, Google, Ollama, Mistral
Vector Stores: Pinecone, Chroma, FAISS, Weaviate, Qdrant, pgvector
Tools: DuckDuckGo, SerpAPI, Wikipedia, Python REPL, SQL, Playwright
Document Loaders: PDF, Word, HTML, CSV, YouTube, Notion, GitHub


---
# KNOWLEDGE INJECTION: LobeHub
# Source: https://github.com/lobehub/lobehub
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: lobehub-platform
name: lobehub-platform
description: >
  LobeHub - open-source AI platform for human-agent co-evolution. Web app + desktop + PWA.
  Multi-model (OpenAI, Ollama, 100+ providers), 10,000+ MCP plugins marketplace, agent builder,
  agent groups, personal memory, real-time internet search, chain-of-thought visualization,
  voice TTS/STT, image generation, knowledge base. Self-host via Docker or Vercel one-click.
USE FOR:
  - self-hosted multi-model AI platform
  - agent builder with customizable skills
  - MCP marketplace 10000+ plugins
  - team agent groups collaboration
  - personal memory adaptive learning
  - chain-of-thought visualization
tags: [LobeHub, LobeChat, multi-model, self-hosted, agents, MCP, Ollama, GPT, Claude, voice]
kind: platform
category: ai-agent-builder

---

## What Is LobeHub?

Open-source AI platform — web app, desktop, PWA with 10,000+ MCP plugins.
- Repo: https://github.com/lobehub/lobehub
- Main product: LobeChat — https://github.com/lobehub/lobe-chat

### Quick Deploy
```bash
# Docker
docker run -d -p 3210:3210 lobehub/lobe-chat

# Vercel one-click (or Zeabur, Sealos, Alibaba Cloud)
# Set OPENAI_API_KEY or other provider credentials
```

### Key Features
| Feature | Details |
|---------|---------|
| Multi-model | OpenAI, Ollama (local), Anthropic, Gemini, 100+ providers |
| MCP Marketplace | 10,000+ compatible plugins |
| Agent Builder | Custom agents with tools, memory, persona |
| Agent Groups | Team-based agent collaboration |
| Personal Memory | Adaptive learning across sessions |
| Internet Search | Real-time web integration |
| Chain of Thought | Visualize AI reasoning steps |
| Voice | TTS/STT conversational interface |
| Image Gen | Generation + visual recognition |
| Knowledge Base | File uploads, RAG |

---
# KNOWLEDGE INJECTION: claude-mem (thedotmack)
# Source: https://github.com/thedotmack/claude-mem
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: claude-mem
name: claude-mem
description: >
  claude-mem - persistent memory compression system for Claude Code. Auto-captures tool usage,
  generates semantic summaries, persists across sessions. Progressive disclosure (layered retrieval
  with token costs). mem-search skill for natural language history queries. 4 MCP tools: search,
  timeline, get_observations. Web viewer at localhost:37777. Private tag for sensitive content.
  Install via /plugin marketplace add thedotmack/claude-mem.
USE FOR:
  - persistent Claude Code memory across sessions
  - semantic session history search
  - context compression and retrieval
  - web UI for memory visualization
  - MCP tools for memory queries
tags: [claude-mem, persistent-memory, Claude-Code, session-continuity, compression, MCP, search]
kind: tool
category: ai-agent-builder

---

## What Is claude-mem?

Persistent memory compression system — context survives Claude Code session restarts.
- Repo: https://github.com/thedotmack/claude-mem
- Web UI: http://localhost:37777

### Install
```bash
# Via Claude Code Plugin Marketplace (recommended)
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
# Restart Claude Code

# Via OpenClaw Gateway
curl -fsSL https://install.cmem.ai/openclaw.sh | bash
```

### Features
- **Automatic**: captures tool usage, generates semantic summaries with no manual action
- **Progressive Disclosure**: layered retrieval showing token costs per memory level
- **mem-search skill**: natural language queries into project history
- **Privacy**: wrap content in `<private>` tags to exclude from memory
- **Citations**: reference past observations by ID

### MCP Tools
| Tool | Purpose |
|------|---------|
| search | Query memory index by natural language |
| timeline | Chronological context view |
| get_observations | Fetch full details by observation ID |

### Web Viewer (localhost:37777)
Real-time memory stream visualization + settings management.

---
# KNOWLEDGE INJECTION: Continue (continuedev)
# Source: https://github.com/continuedev/continue
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: continue-ai-code-review
name: continue-ai-code-review
description: >
  Continue - open-source AI-powered code review platform running agents on every PR as GitHub
  status checks. Review rules stored as markdown in .continue/checks/ directories (source-controlled).
  Returns green pass or red with suggested diffs. VS Code extension available. CLI via npm
  @continuedev/cli (cn command). macOS/Linux/Windows install. Custom checks for security,
  best practices, team conventions.
USE FOR:
  - AI code review on every pull request
  - source-controlled review rules markdown
  - GitHub status checks from AI agents
  - custom security and best practice checks
  - automated PR quality enforcement
tags: [Continue, AI-code-review, PR, GitHub-status-checks, CI, VS-Code, open-source]
kind: tool
category: ai-agent-builder

---

## What Is Continue?

Open-source AI code review platform — agents run on every PR as GitHub status checks.
- Repo: https://github.com/continuedev/continue
- CLI command: `cn`

### Install
```bash
# macOS/Linux
curl -fsSL https://install.continue.dev | bash

# Windows (PowerShell)
iwr https://install.continue.dev/windows -useb | iex

# Node.js alternative (Node 20+)
npm install -g @continuedev/cli
```

### How It Works
```
1. Store review rules as markdown in .continue/checks/
2. Continue runs agents on every PR
3. Returns GitHub status check: green (pass) or red (with suggested diffs)
4. Teams enforce rules as required status checks
```

### Review Rule Structure
```
.continue/
  checks/
    security.md       # security vulnerability rules
    best-practices.md # team coding standards
    custom-check.md   # any custom requirement
```

### VS Code Extension
Available through VS Code marketplace — provides IDE-level AI assistance integrated with the same agent framework.


---
# KNOWLEDGE INJECTION: memU (NevaMind-AI)
# Source: https://github.com/NevaMind-AI/memU
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: memu-proactive-memory
name: memu-proactive-memory
description: >
  memU - 24/7 always-on proactive memory framework for AI agents. Continuously captures user
  intent without explicit commands. Hierarchical 3-layer memory (Resource/Item/Category).
  Dual pathways: memorize() continuous learning + retrieve() RAG fast or LLM deep reasoning.
  92.09% accuracy on benchmarks. Reduces LLM token costs via cached insights.
  Storage: in-memory or PostgreSQL (pgvector). pip install -e .  Python 3.13+.
USE FOR:
  - 24/7 always-on agent memory
  - proactive user intent capture
  - hierarchical memory for AI agents
  - reduce LLM token costs via memory cache
  - RAG-based fast context retrieval
  - persistent agent memory PostgreSQL pgvector
tags: [memU, proactive-memory, AI-ai-agents, hierarchical-memory, RAG, pgvector, token-reduction, 24-7]
kind: framework
category: ai-agent-builder

---

## What Is memU?

24/7 proactive memory framework — AI agents learn continuously without explicit prompts.
- Repo: https://github.com/NevaMind-AI/memU
- Cloud: memu.so
- Python 3.13+ | OpenAI API key required

### Install
```bash
pip install -e .
export OPENAI_API_KEY=your_api_key
```

### Architecture
```
3-Layer Hierarchical Memory:
  Resource   → mountable data sources (docs, sessions, external feeds)
  Item       → individual memory facts with cross-references
  Category   → auto-organized topic clusters

Dual Retrieval Pathways:
  memorize() → continuous learning pipeline (immediate memory update)
  retrieve() → RAG fast (sub-second embedding) OR LLM deep (complex anticipation)
```

### Storage Options
```bash
# In-memory (default)
python tests/test_inmemory.py

# PostgreSQL with pgvector (persistent)
docker run -d --name memu-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 pgvector/pgvector:pg16
python tests/test_postgres.py
```

### Examples
```bash
python examples/example_1_conversation_memory.py  # session persistence
python examples/example_2_skill_extraction.py     # learn user skills
python examples/example_3_multimodal_memory.py    # images + text
```

### Performance
- 92.09% average accuracy on benchmark reasoning tasks
- Sub-second RAG retrieval
- Reduces redundant LLM calls via cached intent insights


---
# KNOWLEDGE INJECTION: Skills Manager (jiweiyeah)
# Source: https://github.com/jiweiyeah/Skills-Manager
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: skills-manager-desktop
name: skills-manager-desktop
description: >
  Skills Manager - desktop app (Tauri 2.0 + React 19) for managing AI skills across
  multiple coding assistants. Write a skill once, sync via symlinks to Claude Code,
  Codex, Opencode simultaneously. Granular enable/disable per tool. Cross-platform
  (macOS/Windows/Linux). Monaco Editor for in-app skill editing.
USE FOR:
  - manage Claude Code skills across multiple AI tools
  - sync skills via symlinks no duplication
  - enable/disable skills per tool
  - visual skill editor desktop app
  - cross-tool skill management
tags: [skills-manager, Claude-Code, Codex, skills-sync, symlinks, Tauri, desktop, cross-platform]
kind: tool
category: ai-agent-builder

---

## What Is Skills Manager?

Centralized desktop app to manage AI assistant skills across Claude Code, Codex, Opencode, etc.
- Repo: https://github.com/jiweiyeah/Skills-Manager
- Stack: Tauri 2.0 (Rust) + React 19 + TypeScript + Tailwind CSS v4 + Radix UI + Monaco Editor
- Install: download from Releases (.dmg / .msi / .exe / .deb / .AppImage / .rpm)

### Key Features
- **Unified hub**: one place to write, edit, and organize skills
- **Smart sync**: symlinks prevent file duplication across tools
- **Granular control**: enable/disable skills per AI tool independently
- **In-app editor**: Monaco Editor for rich code/markdown editing
- **Auto-detect**: finds installed AI tools and their skill directories automatically

### Supported Tools
- Claude Code: `~/.claude/skills/`
- Codex CLI: `~/.codex/skills/`
- Opencode: `~/.opencode/skills/`
- Custom tools: configurable paths

### Windows Note
Requires Administrator privileges or Developer Mode enabled for symlink creation.

---
# KNOWLEDGE INJECTION: Claude Code Karma
# Source: https://github.com/JayantDevkar/claude-code-karma
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: claude-code-karma
name: claude-code-karma
description: >
  Claude Code Karma - local-first analytics dashboard for Claude Code sessions.
  Reads ~/.claude/ JSONL files, serves via FastAPI (port 8000), displays in SvelteKit UI
  (port 5173). No cloud, no accounts, no telemetry. Shows token usage, costs, cache hit rates,
  tool/agent distribution, file operations, plugin/skill/hook inventory, live session monitoring.
USE FOR:
  - visualize Claude Code session analytics
  - token usage and cost tracking
  - cache hit rate analysis
  - tool and agent usage statistics
  - file operation monitoring
  - plugin/skill/hook inventory dashboard
tags: [claude-code-karma, analytics, dashboard, token-usage, costs, sessions, FastAPI, SvelteKit]
kind: tool
category: ai-agent-builder

---

## What Is Claude Code Karma?

Local analytics dashboard for your Claude Code sessions.
- Repo: https://github.com/JayantDevkar/claude-code-karma
- Architecture: ~/.claude/ JSONL → FastAPI (8000) → SvelteKit (5173) → SQLite index
- No external calls — completely local

### Install
```bash
git clone https://github.com/JayantDevkar/claude-code-karma.git
cd claude-code-karma

# Terminal 1 — backend
cd api && pip install -e ".[dev]" && pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Terminal 2 — frontend
cd frontend && npm install && npm run dev
# Access: http://localhost:5173
```

### Dashboard Features
| View | What It Shows |
|------|---------------|
| Session Browser | All sessions with search/filter, real-time status |
| Analytics | Token usage, costs, cache hit rates, tool distribution |
| Project Organization | Workspaces by git repo + activity tracking |
| Tool & Agent Tracking | Built-in + MCP tools + custom agents + usage stats |
| File & Task Management | File operations, task creation/completion |
| Live Monitoring | Real-time via Claude Code hooks (optional) |
| Plugin Ecosystem | Installed plugins, skills, commands, hooks |

---
# KNOWLEDGE INJECTION: Swing Skills (whynowlab)
# Source: https://github.com/whynowlab/swing-skills
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: swing-trade-psychology-coach-firewall
name: swing-trade-psychology-coach-firewall
description: >
  Swing - 6-skill AI trade-psychology-coach firewall suite. Prevents systematic AI reasoning failures:
  ambiguous execution, unverified claims, anchoring, sycophancy, hidden reasoning, optimism bias.
  Skills: swing-clarify (5W1H), swing-research (4-stage verification), swing-options (5 alternatives),
  swing-review (steel-man + 3-vector critique), swing-trace (assumption mapping), swing-mortem
  (5-category failure projection). npx skills add whynowlab/swing-skills --all.
USE FOR:
  - prevent AI hallucination and overconfidence
  - 5W1H request decomposition before execution
  - source-tiered research with cross-validation
  - generate 5 probability-weighted alternatives
  - steel-man critique of decisions
  - assumption mapping and confidence analysis
  - pre-mortem failure projection
tags: [swing, trade-psychology-coach-firewall, clarify, research, options, review, trace, mortem, reasoning, Claude-Code]
kind: skills-suite
category: ai-agent-builder

---

## What Is Swing?

6-skill trade-psychology-coach firewall that addresses systematic AI reasoning failures.
- Repo: https://github.com/whynowlab/swing-skills
- Compatible: Claude Code (primary), Cursor, GitHub Copilot, Codex CLI

### Install
```bash
npx skills add whynowlab/swing-skills --all   # all 6 skills

# Individual:
npx skills add whynowlab/swing-skills/swing-clarify
npx skills add whynowlab/swing-skills/swing-research

# Manual:
cp -r swing-skills/skills/* ~/.claude/skills/
```

### The 6 Skills

| Skill | Problem Solved | Method |
|-------|---------------|--------|
| swing-clarify | Ambiguous requests rushed | 5W1H decomposition |
| swing-research | Unverified claims | 4-stage verification, S/A/B/C source grading |
| swing-options | Anchoring on obvious answer | 5 probability-weighted alternatives |
| swing-review | Sycophancy / no critique | Steel-man then 3-vector critical analysis |
| swing-trace | Hidden reasoning | Assumption map, decision forks, weakest-link |
| swing-mortem | Optimism bias | 5-category failure projection + leading indicators |

### Usage
```bash
/swing-clarify Build me an auth system
/swing-research Is gRPC better than REST for mobile?
/swing-review We chose Kubernetes for our 3-person startup
/swing-options Which database for real-time leaderboard?
/swing-trace Why do you recommend microservices?
/swing-mortem We are migrating to microservices in Q3
```

### Recommended Chain
```
clarify -> (research decision) -> options -> research -> review
        -> (risk analysis)     -> mortem
```

---
# KNOWLEDGE INJECTION: Spec-Flow (echoVic)
# Source: https://github.com/echoVic/spec-flow
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: spec-flow
name: spec-flow
description: >
  Spec-Flow - structured feature development workflow for AI coding agents. 5 sequential phases
  with approval gates: Proposal -> Requirements (EARS syntax) -> Design -> Tasks -> Implementation.
  Generates living markdown docs in .spec-flow/ directory. 3 modes: Step, Batch, Phase.
  Triggers: "spec-flow", "spec mode", "need a plan", "structured development".
  Install: git clone into ~/.claude/skills.
USE FOR:
  - structured feature development with AI
  - requirements specification EARS syntax
  - phase-gated AI coding workflow
  - living documentation .spec-flow directory
  - proposal -> requirements -> design -> tasks -> implementation
tags: [spec-flow, structured-development, requirements, EARS, phases, AI-workflow, Claude-Code]
kind: skill
category: ai-agent-builder

---

## What Is Spec-Flow?

Phase-gated structured development workflow for AI coding agents.
- Repo: https://github.com/echoVic/spec-flow
- Install: `cd ~/.claude/skills && git clone https://github.com/echoVic/spec-flow.git`
- Trigger: "spec-flow", "spec mode", "need a plan", or Chinese: "写个方案"

### 5 Phases (with human approval gates)
```
1. Proposal       → overview, scope, success criteria
2. Requirements   → EARS syntax specs (SHALL/WHEN/WHERE/IF clauses)
3. Design         → architecture, components, data models, interfaces
4. Tasks          → numbered implementation checklist, dependencies
5. Implementation → execute tasks one by one, verify each
```

### Execution Modes
```bash
# Default (step-by-step, confirmation at each phase)
spec-flow: Build user authentication system

# Fast (skip confirmations)
spec-flow --fast: Add dark mode toggle

# Simple (skip design phase)
spec-flow --skip-design: Fix the login bug
```

### Documentation Structure
```
.spec-flow/
  steering/     # project context, conventions
  active/       # in-progress feature docs
    feature-name/
      proposal.md
      requirements.md
      design.md
      tasks.md
  archive/      # completed features
```

### EARS Requirements Format
```
WHEN user submits login form
IF credentials are valid
THE SYSTEM SHALL authenticate the user and redirect to dashboard

WHERE the user is not authenticated
THE SYSTEM SHALL redirect to login page
```

---
# KNOWLEDGE INJECTION: HAM — Hierarchical Agent Memory
# Source: https://github.com/kromahlusenii-ops/ham
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: ham-hierarchical-memory
name: ham-hierarchical-memory
description: >
  HAM (Hierarchical Agent Memory) - reduces Claude Code token consumption 50% by replacing
  one massive CLAUDE.md with small scoped CLAUDE.md files at each directory level.
  Agent loads only 2-3 relevant files per session. Auto-detects project stack, self-maintaining
  (updates decision/pattern files as work progresses). Analytics dashboard at localhost:7777.
  Install: git clone into ~/.claude/skills/ham.
USE FOR:
  - reduce Claude Code token usage by 50%
  - hierarchical scoped CLAUDE.md files
  - context reduction hundreds vs thousands of tokens
  - self-maintaining memory decision files
  - ham dashboard analytics token savings
  - benchmark baseline vs HAM performance
tags: [HAM, hierarchical-memory, token-reduction, CLAUDE.md, context-management, Claude-Code, analytics]
kind: skill
category: ai-agent-builder

---

## What Is HAM?

Hierarchical Agent Memory — cuts Claude Code starting context from thousands of tokens to hundreds.
- Repo: https://github.com/kromahlusenii-ops/ham
- Install: `git clone https://github.com/kromahlusenii-ops/ham.git ~/.claude/skills/ham`
- Token reduction: up to 50%

### Core Concept
```
Before HAM:  One massive CLAUDE.md → loads entire project context every session
After HAM:   Small CLAUDE.md at each directory level → loads only 2-3 relevant files
```

### Commands
```bash
# Setup
go ham              # auto-configures everything
ham update          # refresh memory files
ham status          # show current memory state
ham route           # show which files will load for current directory

# Analytics (web UI at localhost:7777)
ham dashboard       # open analytics dashboard
ham savings         # show token savings report
ham carbon          # environmental impact calculator

# Benchmarking
ham benchmark       # run benchmark vs baseline
ham baseline start  # start baseline measurement
ham baseline stop   # stop baseline, compute metrics

# Maintenance
ham audit           # check for stale/missing memory files
ham commands        # list all available commands
```

### Memory Structure
```
project/
  CLAUDE.md              # global conventions, project overview
  src/
    CLAUDE.md            # frontend/backend patterns
    components/
      CLAUDE.md          # component-specific conventions
    api/
      CLAUDE.md          # API patterns, auth flows
  tests/
    CLAUDE.md            # testing patterns, fixtures
```

### Self-Maintaining Cycle
```
Read:  agent reads directory CLAUDE.md before starting work
Write: agent updates CLAUDE.md after completing work
       (new patterns, decisions, gotchas discovered)
```


---
# KNOWLEDGE INJECTION: Arize Phoenix
# Source: https://github.com/Arize-ai/phoenix
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: arize-phoenix-observability
name: arize-phoenix-observability
description: >
  Arize Phoenix - open-source AI observability platform. OpenTelemetry-based LLM tracing,
  LLM-powered evaluation (response + retrieval quality), version-controlled datasets, experiment
  tracking (prompts/models/retrieval). Integrates LangGraph, LlamaIndex, CrewAI, DSPy,
  Claude Agent SDK, OpenAI, Anthropic, Bedrock. Prompt playground + management.
  pip install arize-phoenix. Local/notebook/Docker/cloud.
USE FOR:
  - LLM application tracing and observability
  - evaluate LLM response and retrieval quality
  - version-controlled test datasets
  - track prompt model retrieval experiments
  - LangChain LangGraph LlamaIndex tracing
  - Claude agent SDK observability
tags: [Phoenix, Arize, observability, tracing, evaluation, LLM, OpenTelemetry, LangChain, LlamaIndex]
kind: platform
category: ai-agent-builder

---

## What Is Arize Phoenix?

Open-source AI observability — trace, evaluate, and experiment on LLM applications.
- Repo: https://github.com/Arize-ai/phoenix
- Cloud: app.phoenix.arize.com
- Vendor and language agnostic

### Install
```bash
pip install arize-phoenix

# Docker
docker pull arizephoenix/phoenix
docker run -p 6006:6006 arizephoenix/phoenix
# UI: http://localhost:6006
```

### 4 Core Capabilities
| Capability | What It Does |
|------------|-------------|
| Tracing | OpenTelemetry-based runtime tracing of LLM calls, chains, agents |
| Evaluation | LLM-powered benchmarks: response quality, retrieval accuracy |
| Datasets | Version-controlled example collections for testing + fine-tuning |
| Experiments | Track changes to prompts, models, retrieval — compare results |

### Quick Start
```python
import phoenix as px
from openinference.instrumentation.langchain import LangChainInstrumentor

# Start local Phoenix
session = px.launch_app()

# Auto-instrument LangChain
LangChainInstrumentor().instrument()

# All LangChain calls now traced at http://localhost:6006
```

### Supported Frameworks
LangGraph · LlamaIndex · CrewAI · DSPy · Claude Agent SDK
OpenAI · Anthropic · Google GenAI · AWS Bedrock

### Prompt Management
- Version-controlled prompt templates
- Tagging and rollback
- A/B comparison in playground
- Model comparison side-by-side


---
# KNOWLEDGE INJECTION: TensorZero
# Source: https://github.com/tensorzero/tensorzero
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: tensorzero-llm-gateway
name: tensorzero-llm-gateway
description: >
  TensorZero - open-source LLM gateway + optimization platform. Sub-millisecond routing to 18+
  providers (Anthropic, OpenAI, Google, AWS, etc.). Observability (PostgreSQL storage + OpenTelemetry),
  optimization (fine-tuning, GEPA prompt engineering, dynamic in-context learning), evaluation
  (heuristic + LLM judge), A/B testing + adaptive routing + fallbacks. Docker deploy.
  OpenAI-compatible API. Fortune 50 production use.
USE FOR:
  - unified LLM gateway 18+ providers
  - LLM observability and feedback collection
  - prompt optimization and fine-tuning
  - A/B testing LLM models
  - adaptive routing fallbacks retries
  - evaluate LLM outputs with judges
tags: [TensorZero, LLM-gateway, optimization, observability, fine-tuning, A/B-testing, OpenAI-compatible]
kind: platform
category: ai-agent-builder

---

## What Is TensorZero?

Production-grade LLM gateway with optimization, observability, evaluation, and experimentation.
- Repo: https://github.com/tensorzero/tensorzero
- Deploy: Docker
- API: OpenAI-compatible (drop-in replacement)

### Quick Start
```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:3000/openai/v1")
response = client.chat.completions.create(
    model="tensorzero::my_function::anthropic::claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Core Capabilities
| Feature | Details |
|---------|---------|
| Gateway | 18+ providers, sub-ms overhead, tool use, structured outputs, multimodal, caching |
| Observability | Stores inferences + feedback in PostgreSQL, OpenTelemetry, Prometheus |
| Optimization | Fine-tuning, GEPA automated prompt engineering, dynamic in-context learning |
| Evaluation | Heuristic benchmarks + LLM-as-judge for individual inferences |
| Experimentation | Built-in A/B testing, adaptive routing, fallbacks, retries |

### Supported Providers
Anthropic · OpenAI · Google Vertex/Gemini · AWS Bedrock/SageMaker · Azure
DeepSeek · Groq · Mistral · Together AI · vLLM · OpenAI-compatible APIs

---
# KNOWLEDGE INJECTION: PentAGI (vxcontrol)
# Source: https://github.com/vxcontrol/pentagi
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: pentagi-security-agents
name: pentagi-security-agents
description: >
  PentAGI - autonomous AI penetration testing platform. Multi-agent architecture:
  Orchestrator + Researcher + Developer + Executor + Searcher/Enricher/Memorist/Reporter.
  20+ built-in security tools (nmap, metasploit, sqlmap). Long-term vector memory (PostgreSQL).
  Knowledge graph (Neo4j). Sandboxed Docker execution. 10+ LLM providers. REST+GraphQL API.
  Grafana/Prometheus monitoring. For authorized security testing and research only.
USE FOR:
  - authorized automated penetration testing
  - multi-agent security research platform
  - vulnerability assessment automation
  - nmap metasploit sqlmap integration
  - AI-driven security tool orchestration
tags: [PentAGI, penetration-testing, security, multi-agent, nmap, metasploit, Docker, authorized-testing]
kind: platform
category: ai-agent-builder

---

## What Is PentAGI?

**For authorized security testing only.** Autonomous AI penetration testing platform.
- Repo: https://github.com/vxcontrol/pentagi
- Deploy: Docker Compose

### Agent Architecture
```
Orchestrator
  Researcher    → target analysis, intelligence gathering
  Developer     → attack strategy planning
  Executor      → implements attack plan
  Searcher      → information retrieval
  Enricher      → context enrichment
  Memorist      → long-term memory management
  Reporter      → results documentation
  Adviser       → strategy recommendations
  Reflector     → execution review
  Planner       → task decomposition (3-7 steps)
```

### Built-in Security Tools (20+)
nmap · metasploit · sqlmap · + 17 others

### Memory & Knowledge
- Long-term memory: vector embeddings in PostgreSQL
- Knowledge graph: Neo4j for semantic relationships
- Mentor supervision: detects repetitive patterns, suggests alternatives

### Supported LLM Providers
OpenAI · Anthropic · Google AI · AWS Bedrock · Ollama · + 5 others

### Limits & Safety
- Tool call limits: 100 (general agents), 20 (limited agents)
- Sandboxed Docker execution (complete isolation)
- Execution monitoring with automatic mentor intervention


---
# KNOWLEDGE INJECTION: Vercel AI SDK
# Source: https://github.com/vercel/ai
# Routed to: claude-ai-tools.md
# Date: 2026-03-18

# SKILL: vercel-ai-sdk
name: vercel-ai-sdk
description: >
  Vercel AI SDK - TypeScript toolkit for building AI apps with React/Next.js/Vue/Svelte/Node.js.
  Unified API across 20+ providers (OpenAI, Anthropic, Google, Groq, Mistral, DeepSeek, etc.).
  Core: generateText, streamText, generateObject, streamObject, tool calling, embeddings.
  UI hooks: useChat, useCompletion. npm install ai. Two libraries: AI SDK Core + AI SDK UI.
USE FOR:
  - build AI app with Next.js React
  - unified LLM API swap providers easily
  - streaming text and structured objects
  - tool calling function integration
  - useChat hook chat UI React
  - generateObject typed JSON from LLM
tags: [Vercel-AI-SDK, TypeScript, Next.js, React, streaming, generateText, useChat, tool-calling, OpenAI, Anthropic]
kind: framework
category: ai-agent-builder

---

## What Is the Vercel AI SDK?

TypeScript toolkit for building AI apps — unified API across 20+ LLM providers.
- Repo: https://github.com/vercel/ai
- Docs: https://ai-sdk.dev/docs
- Works with: React, Next.js, Vue, Svelte, Node.js

### Install
```bash
npm install ai
npm install @ai-sdk/openai      # OpenAI provider
npm install @ai-sdk/anthropic   # Anthropic/Claude
npm install @ai-sdk/google      # Google Gemini
```

### AI SDK Core

**Text Generation:**
```typescript
import { generateText, streamText } from "ai";
import { anthropic } from "@ai-sdk/anthropic";

// Single response
const { text } = await generateText({
  model: anthropic("claude-sonnet-4-6"),
  prompt: "Explain quantum computing",
});

// Streaming
const result = streamText({
  model: anthropic("claude-sonnet-4-6"),
  prompt: "Write a short story",
});
for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}
```

**Structured Output:**
```typescript
import { generateObject } from "ai";
import { z } from "zod";

const { object } = await generateObject({
  model: openai("gpt-4o"),
  schema: z.object({
    name: z.string(),
    age: z.number(),
    skills: z.array(z.string()),
  }),
  prompt: "Generate a fictional developer profile",
});
```

**Tool Calling:**
```typescript
import { tool } from "ai";

const result = await generateText({
  model: openai("gpt-4o"),
  tools: {
    getWeather: tool({
      description: "Get weather for a city",
      parameters: z.object({ city: z.string() }),
      execute: async ({ city }) => fetchWeather(city),
    }),
  },
  prompt: "What is the weather in Paris?",
});
```

### AI SDK UI (React Hooks)

**useChat:**
```typescript
import { useChat } from "ai/react";

export default function ChatPage() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    api: "/api/chat",
  });
  return (
    <div>
      {messages.map(m => <div key={m.id}>{m.role}: {m.content}</div>)}
      <form onSubmit={handleSubmit}>
        <input value={input} onChange={handleInputChange} />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
```

### Supported Providers (20+)
OpenAI · Anthropic · Google · Azure · Amazon Bedrock · Groq · Mistral
Cohere · DeepSeek · xAI Grok · Together.ai · Fireworks · Perplexity · + more

### Core Functions Reference
| Function | Purpose |
|----------|---------|
| generateText | Single text response |
| streamText | Streaming text + tool calls |
| generateObject | Typed JSON (Zod schema) |
| streamObject | Streaming structured data |
| embed | Generate embeddings |
| embedMany | Batch embeddings |
| useChat | React hook for chat UI |
| useCompletion | React hook for text completion |
| useObject | React hook for streaming objects |

