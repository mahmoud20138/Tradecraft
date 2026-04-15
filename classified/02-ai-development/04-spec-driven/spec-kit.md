---
name: spec-kit
description: >
  GitHub Spec Kit — Spec-Driven Development with AI coding agents. Structures AI coding
  by creating living spec artifacts before implementation. USE FOR: "spec kit", "spec-driven",
  "specify init", "write a spec", "create constitution", "spec before coding", "structured AI coding",
  "spec driven development", "speckit", "/speckit", "constitution.md", "plan before coding",
  "fix AI coding", "make AI follow specs", "spec then implement", "structured prompting",
  "define requirements first", "tasks breakdown AI", any new project setup with AI agent,
  or any request to set up a project with structure before coding.
kind: orchestrator
category: ai/spec
status: active
skill_level: intermediate
related_skills:
  - ai-agent-builder
  - claude-md-improver
  - skill-development
  - pro-code-architecture
tags:
  - spec-driven
  - ai-coding
  - claude-code
  - project-setup
  - requirements
---

# GitHub Spec Kit — Spec-Driven Development

> "Stop vibe coding. Define intent first. Let AI execute with precision."
> Repo: https://github.com/github/spec-kit

---

## When Claude Should Use This Skill

Trigger automatically when user:
- Starts a new project and wants AI to help build it
- Says "let's build X" without any existing spec
- Asks to "plan before coding" or "structure this project"
- Shares a GitHub URL to `github/spec-kit`
- Mentions "constitution", "spec.md", "speckit", "/speckit.*"

---

## Installation (One-Time)

```bash
# Install CLI permanently
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# Upgrade
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git

# Verify tools
specify check
```

---

## Quickstart for Claude Code

```bash
# New project
specify init my-project --ai claude

# Existing project (init in-place)
cd my-project
specify init . --ai claude --here

# New feature on existing project
bash .specify/scripts/create-new-feature.sh my-feature-name
```

---

## 8-Command Workflow (Always in this order)

```
1. /speckit.constitution   → Set immutable principles & tech stack
2. /speckit.specify        → Define WHAT to build (user stories, no tech)
3. /speckit.clarify        → Resolve any ambiguities
4. /speckit.plan           → Define HOW (architecture, components, dependencies)
5. /speckit.analyze        → Validate consistency across all artifacts
6. /speckit.tasks          → Break into ordered, parallelizable tasks
7. /speckit.implement      → Execute tasks (test-driven)
8. /speckit.checklist      → Quality validation
```

---

## Project File Structure

```
.specify/
├── memory/
│   └── constitution.md          ← IMMUTABLE: tech stack, principles, conventions
├── specs/
│   └── <FEATURE_ID>/
│       ├── spec.md              ← WHAT & WHY (no implementation detail)
│       ├── plan.md              ← HOW (architecture, components)
│       ├── tasks.md             ← ordered tasks with [P] parallel markers
│       ├── data-model.md        ← entities & schema
│       ├── research.md          ← pre-implementation research
│       └── contracts/
│           ├── api-spec.json    ← REST/OpenAPI contracts
│           └── signalr-spec.md  ← realtime contracts
└── scripts/
    ├── create-new-feature.sh
    ├── setup-plan.sh
    └── update-claude-md.sh
```

---

## File Templates

### constitution.md
```markdown
# Project Constitution

## Non-Negotiable Principles
- No class components — functional only
- All async operations must have error handling
- Tests required for all business logic

## Tech Stack
- Framework: React + Vite + TypeScript
- Styling: Tailwind CSS
- State: useState / Context API (no Redux)
- HTTP: Axios
- Testing: Vitest + Testing Library

## Code Conventions
- Files: PascalCase for components, camelCase for utils
- Max function length: 50 lines
- No magic numbers — use named constants
```

### spec.md
```markdown
# Feature: <NAME>

## Problem Statement
<What problem does this solve? For whom?>

## User Stories (P1 = must-have, P2 = should-have, P3 = nice-to-have)
- [P1] As a <user>, I want to <action> so that <value>
  - Independently testable: ✓
  - MVP slice: ✓

## Functional Requirements
- [] REQ-01: <specific capability>
- [] REQ-02: <specific capability> ← NEEDS CLARIFICATION: <question>

## Success Criteria (measurable, tech-agnostic)
- [] <metric>: <target value>
```

### plan.md
```markdown
# Implementation Plan: <FEATURE>

## Technical Decisions
| Dimension      | Decision        | Status              |
|---------------|-----------------|---------------------|
| Language       | TypeScript      | ✓ confirmed         |
| Framework      | React + Vite    | ✓ confirmed         |
| Storage        | PostgreSQL      | NEEDS CLARIFICATION |
| Performance    | <200ms p95      | ✓ confirmed         |

## Constitution Check
- [] Follows naming conventions
- [] Uses only approved dependencies
- [] Passes security review

## Component Architecture
<file tree with component responsibilities>
```

### tasks.md
```markdown
# Tasks: <FEATURE>

## Phase 1 — Init
- [] T001 Scaffold project

## Phase 2 — Foundation (BLOCKS all subsequent)
- [] T002 Set up DB schema
- [] T003 [P] Auth middleware     ← [P] = parallelizable
- [] T004 [P] API routes

## Phase 3 — P1 Story: <name>
- [] T010 [P1] Build <Component> — src/components/Foo.tsx
- [] T011 [P1] Tests — src/tests/Foo.test.ts

## Strategy
- [] Commit after each task
- [] Validate P1 before starting P2
```

---

## Claude Code Execution Flow

When user says **"let's build X"**, Claude should:

```
1. Run: specify init . --ai claude --here
2. Open .specify/memory/constitution.md → ask user to confirm/edit tech stack
3. Run /speckit.specify → fill spec.md with user's requirements
4. Run /speckit.clarify → ask 3-5 clarifying questions
5. Run /speckit.plan → generate plan.md
6. Run /speckit.analyze → check for gaps
7. Run /speckit.tasks → generate tasks.md
8. Run /speckit.implement → start building task by task
9. Commit after each completed task
```

---

## Key Principles

| Principle | Rule |
|-----------|------|
| **Intent first** | Never write code before spec.md exists |
| **Constitution = immutable** | Tech decisions made once, never revisited per feature |
| **Gate each phase** | Don't plan until spec is approved; don't implement until tasks exist |
| **Atomic tasks** | Each task independently reviewable, committable |
| **`/analyze` gate** | Always run before `/implement` to catch gaps |
| **Parallel tasks** | Mark `[P]` for tasks touching different files |

---

## Supported AI Agents (24+)
`claude` · `gemini` · `copilot` · `cursor-agent` · `windsurf` · `kiro-cli` · `codex`
`qwen` · `roo` · `kilo` · `opencode` · `amp` · `shai` · `tabnine` · `kimi`
`ibm-bob` · `jules` · `codebuddy` · `vibe` · `auggie` · `antigravity` · `trae` · `qoder` · `generic`
