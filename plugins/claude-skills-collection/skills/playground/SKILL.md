---
name: playground
description: Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.
kind: tool
category: dev/ui
status: active
tags: [dev, playground]
related_skills: [elite-ui-design, frontend-design, programmatic-drawing]
---

# Playground Builder

A playground is a self-contained HTML file with interactive controls on one side, a live preview on the other, and a prompt output at the bottom with a copy button. The user adjusts controls, explores visually, then copies the generated prompt back into Claude.

## When to use this skill

When the user asks for an interactive playground, explorer, or visual tool for a topic — especially when the input space is large, visual, or structural and hard to express as plain text.

## How to use this skill

1. **Identify the playground type** from the user's request
2. **Load the matching template** from `templates/`:
   - `templates/design-playground.md` — Visual design decisions (components, layouts, spacing, color, typography)
   - `templates/data-explorer.md` — Data and query building (SQL, APIs, pipelines, regex)
   - `templates/concept-map.md` — Learning and exploration (concept maps, knowledge gaps, scope mapping)
   - `templates/document-critique.md` — Document review (suggestions with approve/reject/comment workflow)
   - `templates/diff-review.md` — Code review (git diffs, commits, PRs with line-by-line commenting)
   - `templates/code-map.md` — Codebase architecture (component relationships, data flow, layer diagrams)
3. **Follow the template** to build the playground. If the topic doesn't fit any template cleanly, use the one closest and adapt.
4. **Open in browser.** After writing the HTML file, run `open <filename>.html` to launch it in the user's default browser.

## Core requirements (every playground)

- **Single HTML file.** Inline all CSS and JS. No external dependencies.
- **Live preview.** Updates instantly on every control change. No "Apply" button.
- **Prompt output.** Natural language, not a value dump. Only mentions non-default choices. Includes enough context to act on without seeing the playground. Updates live.
- **Copy button.** Clipboard copy with brief "Copied!" feedback.
- **Sensible defaults + presets.** Looks good on first load. Include 3-5 named presets that snap all controls to a cohesive combination.
- **Dark theme.** System font for UI, monospace for code/values. Minimal chrome.

## State management pattern

Keep a single state object. Every control writes to it, every render reads from it.

```javascript
const state = { /* all configurable values */ };

function updateAll() {
  renderPreview(); // update the visual
  updatePrompt();  // rebuild the prompt text
}
// Every control calls updateAll() on change
```

## Prompt output pattern

```javascript
function updatePrompt() {
  const parts = [];

  // Only mention non-default values
  if (state.borderRadius !== DEFAULTS.borderRadius) {
    parts.push(`border-radius of ${state.borderRadius}px`);
  }

  // Use qualitative language alongside numbers
  if (state.shadowBlur > 16) parts.push('a pronounced shadow');
  else if (state.shadowBlur > 0) parts.push('a subtle shadow');

  prompt.textContent = `Update the card to use ${parts.join(', ')}.`;
}
```

## Common mistakes to avoid

- Prompt output is just a value dump → write it as a natural instruction
- Too many controls at once → group by concern, hide advanced in a collapsible section
- Preview doesn't update instantly → every control change must trigger immediate re-render
- No defaults or presets → starts empty or broken on load
- External dependencies → if CDN is down, playground is dead
- Prompt lacks context → include enough that it's actionable without the playground


---


---

# ── KNOWLEDGE INJECTION: GitHub Spec Kit — Spec-Driven AI Development ──
> Source: "Spec Kit: Github's NEW tool That FINALLY Fixes AI Coding" — Better Stack (2026)
> Added: 2026-03-17 · Relevant skills: ai-agent-builder, claude-md-improver, skill-development
> Repo: https://github.com/github/spec-kit

## GitHub Spec Kit — Complete Reference

### The Problem It Solves
Traditional AI coding = vague prompts → unpredictable code → fix loops.
**Spec Kit** = structured specs as living contracts → AI agents execute with precision.

> "Intent is the source of truth. Separate stable intent (WHAT) from flexible implementation (HOW)."

---

### Installation
```bash
# Install CLI
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# OR via uvx (no install)
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>

# Initialize project
specify init my-project
# → choose AI agent: Copilot / Claude Code / Gemini CLI / Cursor / Windsurf
# → choose shell: Bash / PowerShell
```

---

### Project Structure
```
my-project/
├── constitution.md   ← non-negotiable principles & tech stack
├── spec.md           ← what you're building (features, user flows)
├── plan.md           ← technical architecture & components
├── tasks.md          ← sequential implementation chunks
└── quickstart.md     ← generated guidance
```

---

### 7 Slash Commands (Sequential Workflow)

| Step | Command | Purpose |
|------|---------|---------|
| 1 | `/constitution` | Set non-negotiable principles, tech stack, code style |
| 2 | `/specify` | Define features, pages, user flows (NO implementation detail) |
| 3 | `/clarify` | Resolve ambiguities before planning |
| 4 | `/plan` | Translate specs → architecture, components, dependencies |
| 5 | `/tasks` | Break work into small, reviewable AI-executable chunks |
| 6 | `/analyze` | Validate consistency across all files vs constitution |
| 7 | `/implement` | Agent executes tasks sequentially |

---

### File Contents

**`constitution.md`** — unchanging decisions:
```markdown
## Tech Stack
- Framework: React + Vite + TypeScript
- Styling: Tailwind CSS
- State: useState / useReducer / Context API
- HTTP: Axios for external API calls
- No class components — functional only
```

**`spec.md`** — functional requirements (user-facing, no tech):
```markdown
## Features
- Product listing page: grid of book cover, title, author, price
- Product detail page: larger image, description, add-to-cart button
- Cart page: item list, quantity controls, remove button, total price
```

**`plan.md`** — technical architecture:
```markdown
## Components
- App.tsx (router root)
- ProductListPage.tsx + ProductCard.tsx
- ProductDetailPage.tsx
- CartPage.tsx
- CartContext.tsx (global state)
- api.ts (Axios data fetching)

## Routes
- / → product listing
- /product/:id → detail
- /cart → cart
```

**`tasks.md`** — sequential implementation:
```markdown
## Tasks
- [] Scaffold project with Vite + React + TypeScript
- [] Create CartContext with add/remove/quantity actions
- [] Build ProductCard component
- [] Build ProductListPage with grid layout
- [] Build ProductDetailPage
- [] Build CartPage with totals
- [] Connect api.ts to Open Library API
```

---

### Compatible AI Agents
- GitHub Copilot
- **Claude Code** ← (us!)
- Gemini CLI
- Cursor
- Windsurf

---

### Use Cases
| Scenario | Benefit |
|----------|---------|
| **Greenfield projects** | Prevents generic solutions — intent defined upfront |
| **Feature additions** | New code integrates naturally with existing architecture |
| **Legacy modernization** | Captures business logic while rebuilding with modern stack |
| **Team collaboration** | All devs + AI share identical project context |

---

### Key Principles
1. **Specs as living contracts** — not one-shot prompts
2. **Gate each phase** — don't implement until spec + plan + tasks are validated
3. **`/analyze` before `/implement`** — catches inconsistencies early
4. **Constitution = immutable** — tech decisions made once, respected always
5. **Tasks = atomic** — each task independently reviewable

---

### Apply to Claude Code Projects
When starting any new project in Claude Code:
```bash
specify init <project-name>
# Then work through: /constitution → /specify → /clarify → /plan → /tasks → /analyze → /implement
```
This replaces ad-hoc CLAUDE.md prompting with a structured, validated spec system.


---

# ── KNOWLEDGE INJECTION: GitHub Spec Kit — Deep Dive (from GitHub Repo) ──
> Source: https://github.com/github/spec-kit · Fetched: 2026-03-17
> Extends: prior Spec Kit knowledge injection (Better Stack video)

## Complete CLI Reference

### Installation
```bash
# Persistent install (recommended)
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# One-time (no install)
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>

# Upgrade
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git

# Check prerequisites
specify check
```

### `specify init` — All Options
```bash
specify init <project-name>          # create in new directory
specify init --here                  # init in current directory
specify init . --ai claude           # Claude Code agent
specify init . --ai gemini           # Gemini CLI
specify init . --ai copilot          # GitHub Copilot
specify init . --ai cursor-agent     # Cursor
specify init . --ai windsurf         # Windsurf
specify init . --ai generic --ai-commands-dir ./my-cmds  # custom agent
specify init . --script ps           # PowerShell scripts
specify init . --no-git              # skip git init
specify init . --force               # skip merge confirmation
specify init . --ai-skills           # install Prompt.MD skill templates
specify init . --debug               # verbose output
```

### Supported Agents (24+)
Claude Code, Gemini CLI, GitHub Copilot, Cursor, Windsurf, Kiro CLI, Codex CLI,
Qwen Code, Roo Code, Kilo Code, OpenCode, Amp, SHAI, Tabnine CLI, Kimi Code,
IBM Bob, Jules, CodeBuddy CLI, Mistral Vibe, Auggie CLI, Antigravity, Trae, Qoder CLI, generic

---

## Full Project Structure
```
.specify/
├── memory/
│   └── constitution.md         ← non-negotiable principles (immutable)
├── scripts/
│   ├── check-prerequisites.sh
│   ├── common.sh
│   ├── create-new-feature.sh   ← scaffold new feature spec
│   ├── setup-plan.sh
│   └── update-claude-md.sh
├── specs/
│   └── <FEATURE_ID>/           ← one folder per feature
│       ├── spec.md             ← what & why (no tech detail)
│       ├── plan.md             ← technical architecture
│       ├── tasks.md            ← ordered implementation chunks
│       ├── data-model.md       ← entities & schema
│       ├── quickstart.md       ← generated setup guide
│       ├── research.md         ← pre-implementation research
│       └── contracts/
│           ├── api-spec.json   ← OpenAPI/REST contracts
│           └── signalr-spec.md ← realtime contracts
└── templates/
    ├── spec-template.md
    ├── plan-template.md
    ├── tasks-template.md
    └── CLAUDE-template.md
```

---

## 8 Slash Commands
```
/speckit.constitution  → Define project governance & tech decisions (immutable)
/speckit.specify       → Write spec.md: user stories, requirements, success criteria
/speckit.clarify       → Resolve ambiguities before planning
/speckit.plan          → Write plan.md: architecture, components, dependencies
/speckit.analyze       → Cross-validate all artifacts for consistency gaps
/speckit.tasks         → Write tasks.md: ordered, dependency-aware, parallelizable
/speckit.implement     → Execute tasks systematically (test-driven)
/speckit.checklist     → Generate quality validation checklist
```

---

## Template Blueprints

### spec.md structure
```markdown
# Feature: <NAME>

## User Stories (prioritized)
- P1: As a <user>, I want to <action> so that <value>
  - INDEPENDENTLY TESTABLE: yes
  - MVP slice: yes

## Functional Requirements
- [] REQ-01: <specific capability>
- [] REQ-02: <specific capability>  ← NEEDS CLARIFICATION: <question>

## Key Entities
- Entity: <Name> — <description>

## Success Criteria (measurable, tech-agnostic)
- [] <metric>: <target>
```

### plan.md structure
```markdown
# Implementation Plan: <FEATURE>

## Summary
<Core requirement + proposed technical strategy>

## Technical Decisions
| Dimension | Decision | Notes |
|-----------|----------|-------|
| Language | TypeScript | — |
| Framework | React + Vite | NEEDS CLARIFICATION: Next.js? |
| Storage | PostgreSQL | — |
| Performance | <200ms p95 | — |

## Constitution Check ✓
- [] Follows naming conventions
- [] Uses approved dependencies
- [] Passes security review gate

## Project Structure
<source tree with file paths>

## Complexity Justification
| Decision | Why complexity is necessary |
|----------|---------------------------|
```

### tasks.md structure
```markdown
# Tasks: <FEATURE>

## Phase 1 — Project Init
- [] T001 Scaffold project structure

## Phase 2 — Foundation (BLOCKS all subsequent phases)
- [] T002 Set up database schema
- [] T003 [P] Configure auth middleware   ← [P] = parallelizable
- [] T004 [P] Set up API routes

## Phase 3 — P1 User Story: <name>
- [] T010 [P1] Build <component> — src/components/Foo.tsx
- [] T011 [P1] Write unit tests — src/tests/Foo.test.ts

## Implementation Strategy
- MVP First: complete foundation → validate one story → stop
- Incremental: add stories sequentially, validate each
- Parallel: multiple devs on different stories after foundation
```

---

## Environment Variables
```bash
SPECIFY_FEATURE=my-feature   # override feature detection (non-Git repos)
GH_TOKEN=ghp_xxx             # GitHub API auth
GITHUB_TOKEN=ghp_xxx         # alternative GitHub auth
```

---

## Use Cases
| Phase | Description |
|-------|-------------|
| **0-to-1 Greenfield** | Build from scratch with full spec |
| **Brownfield feature** | Add feature to existing system |
| **Creative exploration** | Parallel implementations across tech stacks |
| **Team collaboration** | All devs + agents share identical context |

---

## Apply with Claude Code
```bash
# 1. Init for Claude Code
specify init my-project --ai claude --here

# 2. Open project in Claude Code, then run slash commands:
# /speckit.constitution → /speckit.specify → /speckit.clarify
# → /speckit.plan → /speckit.analyze → /speckit.tasks → /speckit.implement

# 3. New feature on existing project
bash .specify/scripts/create-new-feature.sh my-new-feature
# Then: /speckit.specify → /speckit.plan → /speckit.tasks → /speckit.implement
```

---
