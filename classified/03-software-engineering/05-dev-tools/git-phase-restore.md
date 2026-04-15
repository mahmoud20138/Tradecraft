---
name: git-phase-restore
description: >
  Autonomous Git-based project phase restoration. Uses Git history (commits, tags,
  branches, diffs, semantic messages) to identify and restore any development phase
  automatically. Trigger for: "restore to when X worked", "go back to before Y broke",
  "show project phases", "undo the last feature", "roll back to [phase]", "find when
  this bug was introduced", "restore to [tag/commit/date]", "time travel", "git timeline",
  "diff between phases", "what changed since X", or any variation of wanting to revisit,
  inspect, or restore a previous state via Git. Also trigger for just "go back" or "undo"
  in a Git project. Complements git-workflow by handling backward navigation and phase
  awareness. Works on any Git repository.
kind: workflow
category: dev/tools
status: active
tags: [dev, git, phase, restore, tools]
related_skills: [python-manager-discovery]
---

# Git Phase Restore — Autonomous Development Phase Recovery

Leverage Git's full history to identify development phases and restore any project
state automatically. No manual snapshots needed — Git already has everything.

---

## Core Philosophy

Every Git repository already contains a complete record of every development phase.
This skill teaches Claude to **read that record intelligently** and act on it:

- Commits with conventional messages → semantic phase boundaries
- Tags → explicit version milestones
- Branches → parallel development tracks
- Timestamps → temporal navigation
- Diffs → understanding what each phase changed

Instead of maintaining separate snapshot systems, this skill **mines Git itself**
as the single source of truth.

---

## When to Trigger

Always trigger this skill when the user wants to:

| Intent | Example phrases |
|---|---|
| Restore a phase | "go back to when auth worked", "restore to v1.2", "undo last feature" |
| Explore history | "show project phases", "what was the state on March 1st", "git timeline" |
| Find a regression | "when did this bug appear", "find when X broke", "bisect this issue" |
| Compare phases | "diff between auth and current", "what changed since last week" |
| Inspect a past state | "show me the code before the refactor", "what did file X look like in phase Y" |
| Undo / rollback | "roll back", "undo", "revert", "go back" (in any Git project context) |

---

## Phase Detection Strategy

Development phases are identified by analyzing Git history through multiple lenses.
Run `scripts/detect_phases.sh` in the project root to get a structured phase map,
or follow the manual steps below.

### 1. Tag-Based Phases (highest confidence)

Tags are explicit developer-placed milestones. Always check these first.

```bash
# List all tags with dates and messages
git tag -l --sort=-creatordate --format='%(creatordate:short) %(refname:short) %(subject)'
```

### 2. Semantic Commit Phases (high confidence)

Parse conventional commit messages to detect phase boundaries. A new phase starts when:

- A `feat:` commit introduces a major new capability
- Multiple related commits cluster around a single feature/module
- A `refactor:` or `chore:` commit restructures the project
- A merge commit lands a feature branch

```bash
# Show commit history with type prefixes for phase detection
git log --oneline --decorate --all --date=short --format='%h %ad %s'
```

Group consecutive commits by their semantic prefix and the files they touch.
A phase = a cluster of commits that share a purpose.

### 3. Branch-Based Phases

Each feature/bugfix branch represents a development phase.

```bash
# All branches (local + remote) with last commit date
git branch -a --sort=-committerdate --format='%(committerdate:short) %(refname:short)'

# Merged branches = completed phases
git branch --merged main
```

### 4. Time-Based Phases

When the user references a date or relative time period.

```bash
# Commits in a date range
git log --after="2025-01-01" --before="2025-02-01" --oneline

# Find the exact commit at a point in time
git rev-list -1 --before="2025-01-15" HEAD
```

### 5. File-Change-Based Phases

When the user references a specific feature or module, find phases by file paths.

```bash
# All commits that touched a specific path
git log --oneline -- src/auth/

# First and last commit touching a path = phase boundaries
git log --diff-filter=A --oneline -- src/auth/  # First appearance
git log -1 --oneline -- src/auth/                # Last change
```

---

## Core Workflows

### Workflow 1: List Project Phases

**Trigger:** "show phases", "project timeline", "what phases exist"

**Steps:**

1. Verify the project is a Git repository (`git rev-parse --is-inside-work-tree`)
2. Run phase detection across all lenses (tags → semantic → branches → time)
3. Present a structured timeline to the user:

```
PROJECT PHASE TIMELINE
━━━━━━━━━━━━━━━━━━━━━
Phase 1: Project Init          [abc1234] 2025-01-10
  └─ Initial scaffold, deps, config

Phase 2: Database Layer        [def5678] 2025-01-12 → [ghi9012] 2025-01-15
  └─ Room setup, DAOs, migrations (12 commits)

Phase 3: Auth System           [jkl3456] 2025-01-16 → [mno7890] 2025-01-22
  └─ JWT auth, login/register, token refresh (18 commits)
  └─ TAG: v0.1.0-alpha

Phase 4: Profile Feature       [pqr1234] 2025-01-23 → [stu5678] 2025-01-28
  └─ User profile CRUD, avatar upload (9 commits)

Phase 5: Current (HEAD)        [vwx9012] 2025-01-29 → now
  └─ Settings screen, bug fixes (6 commits)
```

4. Ask the user which phase they want to explore or restore.

---

### Workflow 2: Restore to a Specific Phase

**Trigger:** "restore to phase X", "go back to [tag/commit/date/description]"

**Steps:**

1. **Identify the target commit:**
   - If tag: `git rev-parse <tag>`
   - If commit hash: use directly
   - If date: `git rev-list -1 --before="<date>" HEAD`
   - If description: search commit messages: `git log --all --grep="<keyword>" --oneline`
   - If phase name: use phase detection to find the boundary commit

2. **Safety check — protect current work:**
   ```bash
   # Check for uncommitted changes
   git status --porcelain

   # If dirty, auto-stash
   git stash push -m "auto-stash before phase restore $(date +%Y%m%d_%H%M%S)"
   ```

3. **Choose restoration strategy** (present options to user if ambiguous):

   **Option A: Detached HEAD inspection (non-destructive, default for "show me")**
   ```bash
   git checkout <target-commit>
   # User can look around, then return with:
   git checkout -
   ```

   **Option B: New branch from phase (recommended for "restore and continue")**
   ```bash
   git checkout -b restore/<phase-label> <target-commit>
   ```

   **Option C: Hard reset (destructive — ONLY with explicit user confirmation)**
   ```bash
   git reset --hard <target-commit>
   # Original HEAD saved in reflog for 90 days
   ```

   **Option D: Revert range (safe undo of specific phases)**
   ```bash
   git revert --no-commit <start-commit>..<end-commit>
   git commit -m "revert: undo phase [label] (commits <start>..<end>)"
   ```

4. **Post-restore verification:**
   ```bash
   # Confirm HEAD is where expected
   git log -1 --oneline

   # Show what's different from where we were
   git diff --stat <original-head> HEAD
   ```

5. **Report to user:**
   - Which commit was restored
   - Which strategy was used
   - How to get back (reflog, stash, branch name)
   - What files changed

---

### Workflow 3: Find When Something Broke (Git Bisect)

**Trigger:** "when did X break", "find the regression", "bisect"

**Steps:**

1. Identify the "good" state (when it last worked) and "bad" state (current or reported)
2. Run automated bisect:

```bash
git bisect start
git bisect bad HEAD
git bisect good <known-good-commit>

# If there's a test command:
git bisect run <test-command>

# Otherwise, manual bisect — Claude checks each midpoint
```

3. Report the exact commit that introduced the issue
4. Offer to revert just that commit: `git revert <bad-commit>`

---

### Workflow 4: Compare Phases

**Trigger:** "diff between phases", "what changed since X", "compare auth phase to current"

**Steps:**

```bash
# Stat summary between two phase boundary commits
git diff --stat <phase-start>..<phase-end>

# Detailed diff for specific files
git diff <commit-a> <commit-b> -- <path>

# Show which files were added/modified/deleted
git diff --name-status <commit-a> <commit-b>
```

Present as a structured summary:
- Files added / modified / deleted
- Lines added / removed per file
- Key changes in plain English

---

### Workflow 5: Inspect a File at a Past Phase

**Trigger:** "show me file X at phase Y", "what did config look like before"

```bash
# Show file content at a specific commit
git show <commit>:<file-path>

# Compare a file between two commits
git diff <commit-a> <commit-b> -- <file-path>
```

---

## Safety Rules

These are non-negotiable safeguards:

1. **Never force-push** to shared branches (main, master, develop) without explicit user confirmation
2. **Always stash or commit** uncommitted work before any checkout or reset
3. **Prefer non-destructive operations** — detached HEAD and new branches over hard resets
4. **Always tell the user** the reflog entry so they can recover: `git reflog` shows the safety net
5. **Verify the repo is clean** before any restoration — `git status --porcelain` must be empty or stashed
6. **Log the restore action** — if project-history or restore-points skills are active, update their logs too
7. **Never rewrite history** on branches that others may have pulled from

---

## Automatic Phase Labeling

When commits follow conventional commit format (`feat:`, `fix:`, `refactor:`, etc.),
Claude should auto-generate human-readable phase labels:

| Commit pattern | Auto-label |
|---|---|
| `feat: add user authentication` | "Auth System" |
| `feat: implement payment gateway` | "Payment Integration" |
| `refactor: extract service layer` | "Service Layer Refactor" |
| `chore: initial project setup` | "Project Init" |
| Cluster of `fix:` commits | "Bug Fix Sprint" |
| Merge of `feature/X` branch | Phase named after branch |

---

## Integration with Other Skills

- **git-workflow**: This skill handles backward navigation; git-workflow handles forward progress. They complement each other.
- **project-history**: After a restore, update PROJECT_HISTORY.md's Active Context to reflect the restored state.
- **project-restore-points**: If the user also has filesystem snapshots, cross-reference them with Git phases for richer context.
- **codebase-understanding**: Before restoring, understand the current codebase structure so the restore doesn't break active work.

---

## Quick Reference Commands

```bash
# Phase detection
git log --oneline --graph --decorate --all          # Visual history
git tag -l --sort=-creatordate                       # Tags = milestones
git branch -a --sort=-committerdate                  # Branches = phases

# Time travel
git checkout <commit>                                # Inspect (detached HEAD)
git checkout -b restore/<label> <commit>             # Restore as branch
git stash push -m "before restore"                   # Save current work

# Investigation
git bisect start && git bisect bad && git bisect good <commit>
git log --all --grep="<keyword>" --oneline           # Search commits
git log --after="<date>" --before="<date>" --oneline # Time range

# Recovery (always available)
git reflog                                           # Full undo history
git stash list                                       # Stashed work
git checkout -                                       # Go back to previous branch
```

---

## Error Handling

| Situation | Action |
|---|---|
| Not a git repo | Tell user, offer to `git init` + initial commit |
| Dirty working tree | Auto-stash with descriptive message |
| Commit not found | Broaden search: try `--all`, check reflog, search by message |
| Merge conflicts on revert | Show conflicts, help resolve, or abort and try different strategy |
| Detached HEAD confusion | Explain clearly, offer to create a branch or return |
| User wants to undo the restore | Use reflog: `git reset --hard HEAD@{1}` or pop stash |
