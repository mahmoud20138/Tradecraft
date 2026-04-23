---
name: ai-agent-builder
description: Expert guide for building AI-powered coding agents that produce professional-quality output. Trigger whenever the user asks to build an AI agent, coding assistant, automation pipeline, tool-using LLM system, or says "agent", "agentic", "tool use", "function calling", "LLM pipeline", "AI workflow", "coding bot", or "autonomous AI". Covers agent architecture, tool design, skill loading, prompt engineering, context management, evaluation loops, and multi-step orchestration using the Claude API or any LLM API.
kind: reference
category: ai/agents
status: active
tags: [agent, agents, builder, claude-code]
related_skills: [agent-development, deepagents-langchain]
---

# AI Agent Builder Skill — Agentic System Design

## Identity
You architect AI agents that reliably produce professional-quality outputs.
You understand that the gap between a "chatbot wrapper" and a real agent is:
structured tool use, skill-based prompting, iterative execution, and quality gates.

---

## CORE PRINCIPLE

> **An agent is a loop, not a call.**
> Single LLM call = chatbot. LLM + tools + iteration + validation = agent.

```
┌─────────────────────────────────────────┐
│           AGENT EXECUTION LOOP          │
│                                         │
│  Plan → Execute → Observe → Validate    │
│    ↑                           │        │
│    └───── Fix if invalid ──────┘        │
│                                         │
│  Stop when: success OR max_retries      │
└─────────────────────────────────────────┘
```

---

## ARCHITECTURE PATTERNS

### Pattern 1: Tool-Using Agent (Most Common)
```
User Request
    ↓
System Prompt + Skill Context
    ↓
LLM generates plan
    ↓
LLM calls tools (file_write, shell_exec, web_search, etc.)
    ↓
Tool results fed back to LLM
    ↓
LLM validates output
    ↓
Deliver or retry
```

**Best for:** Code generation, file manipulation, data analysis, research

### Pattern 2: Skill-Loaded Agent
```
User Request → Classify task type → Load relevant skill(s)
    ↓
Inject skill into system prompt
    ↓
Execute with tool use
    ↓
Quality gate from skill checklist
```

**Best for:** Multi-domain agents (code + UI + docs + data)

### Pattern 3: Multi-Agent Pipeline
```
Agent 1: Planner    → Decomposes task into subtasks
Agent 2: Implementer → Executes each subtask with tools
Agent 3: Reviewer    → Reviews output, requests fixes
Agent 4: Integrator  → Combines outputs into final deliverable
```

**Best for:** Complex multi-file projects, but higher cost and latency.
**Warning:** Start with single-agent + tools. Only add agents when single-agent fails.

### Pattern 4: ReAct (Reason + Act)
```
Thought: I need to find the user's API key location
Action: search_files("*.env", "API_KEY")
Observation: Found in .env line 3: CLAUDE_API_KEY=sk-...
Thought: Now I need to read the config to see how it's loaded
Action: read_file("config.py")
Observation: Uses os.environ.get("CLAUDE_API_KEY")
Thought: The key is loaded correctly. Now I can...
```

**Best for:** Complex reasoning tasks requiring multiple observations

---

## TOOL DESIGN

### Tool Design Principles
```
1. ATOMIC: Each tool does ONE thing well
2. TYPED: Clear input/output schemas with descriptions
3. SAFE: Tools validate inputs and handle errors gracefully
4. OBSERVABLE: Tools return structured results the LLM can reason about
5. IDEMPOTENT: Safe to call multiple times with same input (where possible)
```

### Essential Tool Set for a Coding Agent
```python
TOOLS = [
    {
        "name": "read_file",
        "description": "Read the contents of a file at the given path. Returns file content as string.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Absolute or relative file path"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write content to a file. Creates the file if it doesn't exist, overwrites if it does.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path to write to"},
                "content": {"type": "string", "description": "Full file content to write"}
            },
            "required": ["path", "content"]
        }
    },
    {
        "name": "edit_file",
        "description": "Replace a specific string in a file. The old_str must appear exactly once.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "old_str": {"type": "string", "description": "Exact string to find (must be unique)"},
                "new_str": {"type": "string", "description": "Replacement string"}
            },
            "required": ["path", "old_str", "new_str"]
        }
    },
    {
        "name": "run_command",
        "description": "Execute a shell command and return stdout/stderr. Use for running tests, linters, builds.",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "Shell command to execute"},
                "timeout": {"type": "integer", "description": "Timeout in seconds (default 30)", "default": 30}
            },
            "required": ["command"]
        }
    },
    {
        "name": "search_files",
        "description": "Search for a pattern across files in a directory. Returns matching file paths and line numbers.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string", "description": "Regex or text pattern to search for"},
                "directory": {"type": "string", "description": "Directory to search in", "default": "."},
                "file_glob": {"type": "string", "description": "File glob pattern (e.g., '*.py')", "default": "*"}
            },
            "required": ["pattern"]
        }
    },
    {
        "name": "list_directory",
        "description": "List files and directories at the given path, up to 2 levels deep.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Directory path", "default": "."}
            }
        }
    }
]
```

### Tool Implementation Pattern (Python)
```python
import subprocess
import os
from pathlib import Path

def execute_tool(name: str, input_data: dict) -> str:
    """Execute a tool and return result as string for the LLM."""
    try:
        match name:
            case "read_file":
                path = Path(input_data["path"])
                if not path.exists():
                    return f"ERROR: File not found: {path}"
                if path.stat().st_size > 100_000:
                    return f"ERROR: File too large ({path.stat().st_size} bytes). Read specific sections."
                return path.read_text(encoding="utf-8")

            case "write_file":
                path = Path(input_data["path"])
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(input_data["content"], encoding="utf-8")
                return f"SUCCESS: Wrote {len(input_data['content'])} chars to {path}"

            case "run_command":
                result = subprocess.run(
                    input_data["command"],
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=input_data.get("timeout", 30),
                    cwd=os.getcwd()
                )
                output = ""
                if result.stdout:
                    output += f"STDOUT:\n{result.stdout[:5000]}\n"
                if result.stderr:
                    output += f"STDERR:\n{result.stderr[:2000]}\n"
                output += f"EXIT CODE: {result.returncode}"
                return output

            case _:
                return f"ERROR: Unknown tool: {name}"

    except Exception as e:
        return f"ERROR: {type(e).__name__}: {str(e)}"
```

---

## SKILL LOADING SYSTEM

### Skill File Structure
```
skills/
├── frontend-ui/
│   └── SKILL.md          # Design system, component patterns, animation rules
├── backend-api/
│   └── SKILL.md          # REST design, error handling, auth patterns
├── database/
│   └── SKILL.md          # Schema design, query optimization, migrations
├── testing/
│   └── SKILL.md          # Test patterns, mocking, coverage targets
├── drawing/
│   └── SKILL.md          # SVG, Canvas, p5.js, visualization patterns
└── devops/
    └── SKILL.md          # Docker, CI/CD, deployment, monitoring
```

### Skill Loader
```python
from pathlib import Path
from typing import Optional

SKILL_DIR = Path("skills")

SKILL_TRIGGERS = {
    "frontend-ui": ["ui", "component", "page", "layout", "design", "css", "react", "html", "dashboard", "landing"],
    "backend-api": ["api", "endpoint", "route", "server", "rest", "graphql", "middleware", "auth"],
    "database": ["database", "sql", "query", "schema", "migration", "model", "orm", "table"],
    "testing": ["test", "spec", "coverage", "mock", "assert", "tdd", "unit test", "integration test"],
    "drawing": ["draw", "svg", "canvas", "chart", "diagram", "visualize", "art", "graphic", "illustration"],
    "devops": ["deploy", "docker", "ci", "cd", "pipeline", "kubernetes", "monitor", "infrastructure"],
}

def detect_skills(user_message: str) -> list[str]:
    """Detect which skills to load based on the user's message."""
    message_lower = user_message.lower()
    matched = []
    for skill_name, triggers in SKILL_TRIGGERS.items():
        if any(trigger in message_lower for trigger in triggers):
            matched.append(skill_name)
    return matched or ["backend-api"]  # Default skill

def load_skills(skill_names: list[str]) -> str:
    """Load and concatenate skill contents."""
    contents = []
    for name in skill_names:
        skill_path = SKILL_DIR / name / "SKILL.md"
        if skill_path.exists():
            contents.append(f"# ACTIVE SKILL: {name}\n\n{skill_path.read_text()}")
    return "\n\n---\n\n".join(contents)
```

---

## AGENT ORCHESTRATOR

### Full Agent Loop (Python + Claude API)
```python
import anthropic
from typing import Any

client = anthropic.Anthropic()

def run_agent(
    user_request: str,
    skills: list[str],
    tools: list[dict],
    max_iterations: int = 25
) -> str:
    """Run the full agent loop until task completion or max iterations."""

    skill_context = load_skills(skills)

    system_prompt = f"""You are an elite software engineer agent.

{skill_context}

## Execution Rules
1. PLAN before coding. State your approach in 2-3 sentences.
2. Read existing code before modifying it.
3. Write complete, runnable code. Never use placeholders.
4. Run tests/linters after every change.
5. If tests fail, analyze the error and fix it. Retry up to 3 times.
6. When done, verify all requirements are met.

## Quality Gates
Before marking as complete, verify:
- All tests pass
- No linter errors
- All imports present
- Edge cases handled
- Code follows the loaded skill guidelines
"""

    messages = [{"role": "user", "content": user_request}]

    for iteration in range(max_iterations):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )

        # Check if agent is done (no more tool calls)
        if response.stop_reason == "end_turn":
            final_text = "".join(
                block.text for block in response.content if block.type == "text"
            )
            return final_text

        # Process tool calls
        assistant_content = response.content
        messages.append({"role": "assistant", "content": assistant_content})

        tool_results = []
        for block in assistant_content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        messages.append({"role": "user", "content": tool_results})

    return "ERROR: Agent exceeded maximum iterations without completing."
```

---

## CONTEXT MANAGEMENT (Critical for Quality)

### Context Window Budget
```
TOTAL CONTEXT: ~200K tokens (Claude Sonnet)

BUDGET ALLOCATION:
  System prompt + skills:   10-15K tokens (keep lean)
  Conversation history:     50-80K tokens
  Tool results:             50-80K tokens
  Working space for output: 20-30K tokens

RULES:
  1. Truncate old tool results after they're processed
  2. Summarize conversation history every 10 turns
  3. Keep skill files under 5K tokens each
  4. Limit tool output to 5K chars per result
  5. If context > 60% full, summarize and compress
```

### Context Compression
```python
def compress_messages(messages: list[dict], max_tokens: int = 80000) -> list[dict]:
    """Compress conversation history to fit within budget."""
    # Keep first message (original request) and last 10 messages
    if len(messages) <= 12:
        return messages

    first = messages[0]
    recent = messages[-10:]

    # Summarize middle messages
    middle_summary = {
        "role": "user",
        "content": f"[Previous {len(messages) - 11} messages summarized: "
                   f"Agent worked on the task, made {count_tool_calls(messages)} tool calls, "
                   f"key files modified: {get_modified_files(messages)}]"
    }

    return [first, middle_summary] + recent
```

---

## PROMPT ENGINEERING FOR AGENTS

### System Prompt Structure
```
1. IDENTITY (who the agent is)
2. SKILLS (loaded dynamically)
3. TOOLS (available tools with descriptions)
4. RULES (execution constraints)
5. QUALITY GATES (what "done" looks like)
6. OUTPUT FORMAT (how to report results)
```

### Few-Shot Examples in Skills
```markdown
## Example: Creating a React Dashboard Card

USER: "Create a metrics card component showing revenue"

GOOD OUTPUT:
- Uses design system tokens (--space-*, --radius-*, etc.)
- Includes hover animation
- Shows loading skeleton state
- Has responsive breakpoints
- Uses real-looking placeholder data ($12,847.32 not "100")

BAD OUTPUT:
- Hardcoded colors (#333)
- No hover/focus states
- "Lorem ipsum" placeholder text
- Missing responsive handling
- No loading state
```

### Prompt Patterns That Improve Quality
```
1. CHAIN OF THOUGHT: "Think step by step before writing code"
2. SELF-VERIFICATION: "After writing, review your code against the checklist"
3. NEGATIVE EXAMPLES: "Do NOT use placeholder text, hardcoded colors, or missing imports"
4. ROLE ANCHORING: "You are a principal engineer at Stripe/Vercel/Linear"
5. FORMAT LOCKING: "Respond with ONLY the code. No explanations before or after."
6. CONSTRAINT INJECTION: "The code must be under 200 lines and use only stdlib"
```

---

## EVALUATION & QUALITY GATES

### Automated Quality Checks
```python
def quality_gate(output_files: list[str]) -> dict:
    """Run automated quality checks on agent output."""
    results = {"passed": True, "checks": []}

    for file_path in output_files:
        ext = Path(file_path).suffix

        # Syntax check
        if ext == ".py":
            r = subprocess.run(["python", "-m", "py_compile", file_path], capture_output=True)
            results["checks"].append({"check": "python_syntax", "passed": r.returncode == 0})

        elif ext in (".js", ".jsx", ".ts", ".tsx"):
            r = subprocess.run(["node", "--check", file_path], capture_output=True)
            results["checks"].append({"check": "js_syntax", "passed": r.returncode == 0})

        # Lint check
        if ext == ".py":
            r = subprocess.run(["ruff", "check", file_path], capture_output=True)
            results["checks"].append({"check": "python_lint", "passed": r.returncode == 0})

        # Test run
        test_file = file_path.replace(".py", "_test.py")
        if Path(test_file).exists():
            r = subprocess.run(["pytest", test_file, "-v"], capture_output=True)
            results["checks"].append({"check": "tests", "passed": r.returncode == 0, "output": r.stdout[:2000]})

    results["passed"] = all(c["passed"] for c in results["checks"])
    return results
```

### Human-in-the-Loop Checkpoints
```
LOW RISK (auto-approve):
  - Formatting changes
  - Adding comments/docs
  - Test additions
  - Linter fixes

MEDIUM RISK (show diff, ask to continue):
  - New file creation
  - API endpoint changes
  - Database schema changes
  - Config file modifications

HIGH RISK (require explicit approval):
  - File deletions
  - Production deployment
  - External API calls with side effects
  - Anything touching auth/security
```

---

## ANTI-PATTERNS TO AVOID

```
1. GIANT SYSTEM PROMPT: > 20K tokens of instructions = context dilution
2. TOO MANY TOOLS: > 15 tools = decision paralysis. Keep to 6-10 core tools.
3. NO VALIDATION LOOP: Generate once → deliver. ALWAYS validate.
4. STATELESS CALLS: Not passing conversation history. Agent forgets what it did.
5. OVER-ENGINEERING: Multi-agent when single-agent + tools suffices.
6. VAGUE SKILLS: "Write good code" instead of concrete patterns and examples.
7. NO ERROR RECOVERY: Agent hits error → crashes. Must have retry logic.
8. UNLIMITED CONTEXT: Not truncating tool output → context overflow → quality collapse.
```
