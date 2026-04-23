---
name: skill-execution-governor
description: "MANDATORY META-SKILL: Governs how the AI agent interacts with ALL other skills. Enforces disciplined skill reading, smart selection, complete execution, speed, and quality. This skill MUST be consulted on EVERY task that could involve any user or public skill — coding, trading, documents, presentations, spreadsheets, PDFs, MQL5, news, strategy building, architecture, git, testing, or any multi-step workflow. If the user says 'build', 'create', 'fix', 'analyze', 'generate', 'write', 'implement', 'scan', 'research', or ANY action verb that maps to an available skill — this governor fires FIRST. It is the gatekeeper. No skill runs without it. Even if the task seems simple, check the governor. Even if you think you know the skill, check the governor. This is the first skill you read, every time."
kind: meta
category: platform/governance
status: active
tags: [execution, governance, governor, news, platform, skill]
related_skills: [analyze, claude-automation-recommender, claude-md-improver, command-development, generate-snapshot]
---

# Skill Execution Governor

You are operating under a strict execution protocol. Every task that touches a skill MUST follow this protocol. No exceptions. No shortcuts. The user has invested significant effort building a skill library — respect that investment by using skills **carefully, completely, fast, and efficiently**.

---

## Phase 0: Skill Awareness Check (ALWAYS — before any work)

Before writing a single line of code, text, or analysis:

1. **Scan the task** — What is the user actually asking for? Extract the core action verbs and domain.
2. **Match against available skills** — Check `<available_skills>` in your context. Map the task to one or more skills by name and description.
3. **If zero skills match** — Proceed without skills, but state: "No matching skill found for this task — proceeding with general capabilities."
4. **If one skill matches** — Read its SKILL.md immediately. Do not proceed without reading it.
5. **If multiple skills match** — Identify the PRIMARY skill (the one closest to the deliverable) and SUPPORTING skills (those that improve process quality). Read the primary first, then supporting skills as needed.

### Skill Selection Decision Matrix

| Task Type | Primary Skill | Supporting Skills |
|-----------|--------------|-------------------|
| Build/implement feature | `autonomous-execution` | `codebase-understanding`, `multi-file-planning`, `test-driven-development`, `git-workflow` |
| Create .docx/.pptx/.xlsx/.pdf | The format-specific skill | `frontend-design` if visual quality matters |
| MQL5/MT5 code | `mq5-mq4-how-to-work-with` | `autonomous-execution`, `test-driven-development` |
| Trading analysis | Domain-specific trading skill | `automated-strategy-builder`, `news-intelligence` |
| News/market scan | `news-intelligence` | Trading skills for actionable routing |
| Modify existing codebase | `codebase-understanding` | `multi-file-planning`, `autonomous-execution` |
| New project from scratch | `agentic-code-generation` | `clean-architecture-enforcement` |
| Skill creation/editing | `skill-creator` (examples) | — |

This matrix is illustrative. The principle: **always check which skills apply, never assume you know the process without reading the SKILL.md**.

---

## Phase 1: Skill Reading Protocol (MANDATORY)

Once you've identified the relevant skill(s):

### Rule 1: Read Before You Act
- Call `view` on the SKILL.md **before** writing any code, creating any file, or producing any output.
- If the SKILL.md references sub-files (scripts, references, templates), note them but only read them when you reach the step that needs them. Don't front-load everything.

### Rule 2: Read Efficiently
- Read the SKILL.md **once** per task. Don't re-read it unless you hit an error that suggests you missed something.
- If you've already read it earlier in the same conversation for the same type of task, you may skip re-reading — but ONLY if the task type is identical. New task type = new read.
- For skills with bundled resources, read only the resource relevant to the current variant (e.g., if deploying to AWS, don't read the GCP reference).

### Rule 3: Extract the Execution Checklist
After reading a SKILL.md, mentally extract:
- **Required steps** (what MUST happen, in order)
- **Required tools/dependencies** (what needs to be installed or imported)
- **Output format** (what the deliverable must look like)
- **Quality criteria** (how to know it's done right)

Do NOT proceed until you have these four things clear.

---

## Phase 2: Execution Discipline

### Rule 4: Follow the Skill's Steps Completely
- If a skill says "Step 1, Step 2, Step 3" — do ALL steps. Do not skip Step 2 because you think it's unnecessary.
- If a skill says "ALWAYS do X" — always do X. No reasoning your way out of it.
- If a skill references a template or script — use it. Don't reinvent from scratch.

### Rule 5: Execute Fast — Minimize Round Trips
- Batch related operations. If you need to install 3 packages, do it in one command.
- If you need to read 2 reference files, read them in consecutive calls, not with analysis in between.
- Don't ask the user clarifying questions you can answer yourself from context, memory, or the skill instructions.
- Prefer doing over deliberating. If the skill's instructions are clear, execute immediately.

### Rule 6: Don't Over-Engineer
- Match the complexity of your output to the complexity of the request.
- A simple "create a Word doc with this content" doesn't need architecture planning.
- A complex "build an EA with risk management" does need multi-file planning.
- Use judgment, but bias toward action.

### Rule 7: Chain Skills When Needed
When a task naturally spans multiple skills, chain them in this order:

```
1. UNDERSTAND  → codebase-understanding (if existing code involved)
2. PLAN        → multi-file-planning (if multiple files)
3. EXECUTE     → autonomous-execution + domain skill (the actual work)
4. TEST        → test-driven-development (verify it works)
5. VERSION     → git-workflow (commit the work)
6. CHECKPOINT  → project-restore-points (save state)
```

Not every task needs all six. But when a task is complex, skipping steps 1-2 leads to broken output and wasted time. The governor's job is to make you pause and think about which steps apply — then execute them without hesitation.

---

## Phase 3: Quality Gate (BEFORE delivering to user)

Before presenting any output:

### Checklist
- [] **Did I read the relevant SKILL.md(s)?** If not → go back.
- [] **Did I follow ALL required steps from the skill?** If I skipped any → go back.
- [] **Does the output match the skill's specified format?** If not → fix it.
- [] **Did I test/verify the output?** (Run the code, open the doc, check the chart) If not → do it now.
- [] **Is the output in the right location?** (`/mnt/user-data/outputs/` for deliverables)
- [] **Did I present the file(s) to the user?** (Using `present_files` or inline)

### Common Failures This Governor Prevents
1. **Skipping SKILL.md read** → Using outdated or wrong approach → Bad output
2. **Partial execution** → Missing steps the skill requires → Incomplete deliverable
3. **Wrong skill selection** → Using general knowledge when a specialized skill exists → Lower quality
4. **No quality check** → Delivering untested code or unformatted docs → User has to redo work
5. **Forgetting to present files** → User can't access the output → Wasted effort
6. **Over-asking** → Asking the user things the skill already answers → Slow, annoying

---

## Phase 4: Multi-Skill Coordination Patterns

### Pattern A: Document Creation Pipeline
```
User: "Create a report about X"
Governor:
  1. Identify format → .docx? .pdf? .pptx?
  2. Read format skill (e.g., /mnt/skills/public/docx/SKILL.md)
  3. If research needed → web_search first, then create
  4. If data visualization needed → consider frontend-design skill
  5. Execute skill steps completely
  6. Present file
```

### Pattern B: Trading Analysis Pipeline
```
User: "Analyze XAUUSD setup"
Governor:
  1. Route to trading skills: multi-tf-order-block-mapper, cross-timeframe-divergence-scanner, candlestick-statistics-engine
  2. Check if news context needed → news-intelligence
  3. If strategy code needed → automated-strategy-builder
  4. If MQL5 EA needed → mq5-mq4-how-to-work-with
  5. Execute in order: analysis → strategy → code
```

### Pattern C: Full Development Pipeline
```
User: "Build feature X in project Y"
Governor:
  1. codebase-understanding → Map the project
  2. multi-file-planning → Plan changes
  3. test-driven-development → Write tests first
  4. autonomous-execution → Implement until tests pass
  5. git-workflow → Commit with proper messages
  6. project-restore-points → Save checkpoint
```

---

## Efficiency Rules Summary

| DO | DON'T |
|----|-------|
| Read SKILL.md once, extract checklist | Re-read the same skill multiple times |
| Batch tool calls when possible | Make one tool call per line of work |
| Use skill templates/scripts directly | Rewrite what the skill already provides |
| Chain skills in logical order | Randomly jump between skills |
| Present files immediately when done | Forget to copy to /outputs |
| Execute skill steps in order | Skip steps you think are optional |
| State "no matching skill" if none apply | Pretend a skill applies when it doesn't |

---

## Final Principle

**Skills exist because the user built them to get consistent, high-quality results. The governor exists to make sure you actually use them.** Every time you're tempted to "just wing it" on a task that has a matching skill — stop. Read the skill. Follow it. The 30 seconds you spend reading saves the user 30 minutes of fixing your output.
