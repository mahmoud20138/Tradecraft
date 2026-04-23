---
name: openspec
description: >
  OpenSpec — lightweight fluid spec framework for AI-assisted development. USE FOR:
  "openspec", "opsx", "/opsx:propose", "propose feature", "spec before coding",
  "iterative spec", "brownfield spec", "AI spec framework", "change proposal",
  "design before implement", "fluid specs", "spec folder", "openspec init".
  Lighter alternative to spec-kit: no rigid phases, works on existing projects.
kind: tool
category: ai/spec
repo: https://github.com/Fission-AI/OpenSpec
related_skills: [spec-kit, ai-agent-builder, claude-md-improver]
tags: [spec-driven, ai-coding, planning, iterative, brownfield]
status: active
---

# OpenSpec — Fluid Spec-Driven Development

> "Fluid not rigid. Iterative not waterfall. Built for brownfield."
> Lighter alternative to Spec Kit — no phase gates, works on existing projects.

## vs Spec Kit

| | OpenSpec | Spec Kit |
|--|---------|---------|
| Style | Fluid, iterative | Structured, gated phases |
| Best for | Brownfield + greenfield | Greenfield projects |
| Phase gates | No | Yes (must complete each phase) |
| Commands | 3 core + 8 extended | 8 ordered commands |
| Install | npm global | uv/uvx |
| Models | Opus 4.5+ recommended | Any |

## Installation
```bash
npm install -g @fission-ai/openspec@latest
cd your-project
openspec init

# Opt out of telemetry
export OPENSPEC_TELEMETRY=0
```

## Core 3-Command Workflow
```
1. /opsx:propose "feature name"  → generates change folder
2. /opsx:apply                   → AI implements tasks
3. /opsx:archive                 → moves to archive
```

## Change Folder Structure
```
.openspec/changes/<feature-name>/
├── proposal.md     ← rationale and scope
├── specs/          ← requirements and scenarios
├── design.md       ← technical approach
└── tasks.md        ← implementation checklist
```

## All Commands

| Command | Purpose |
|---------|---------|
| `/opsx:propose "idea"` | Create new change folder with proposal + specs + design + tasks |
| `/opsx:apply` | Implement tasks from current change |
| `/opsx:archive` | Archive completed change |
| `/opsx:new` | Start fresh change |
| `/opsx:continue` | Resume in-progress change |
| `/opsx:ff` | Fast-forward (skip to implementation) |
| `/opsx:verify` | Validate implementation against spec |
| `/opsx:sync` | Synchronize agent instructions |
| `/opsx:bulk-archive` | Archive multiple completed changes |
| `/opsx:onboard` | Team onboarding setup |

## CLI Commands
```bash
openspec init              # initialize in project
openspec config profile    # select workflow type
openspec update            # refresh agent instructions + slash commands
```

## Key Principles
- **No phase gates** — update any artifact at any time
- **Brownfield first** — works on existing codebases
- **Context management** — clear context before implementation phases
- **Best with Opus 4.5+** — high-reasoning models get best results
- **20+ AI tools** — Claude Code, Cursor, Copilot, Windsurf, etc.
