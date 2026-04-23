---
name: skill-manager
description: Full skill library management — list by usage, find duplicates, visualize dependency graph, check for updates, batch validate all 146 skills.
kind: meta
category: platform/skills
status: active
tags: [manager, platform, skill, skills]
related_skills: [skill-analytics, skill-docs-generator, skill-doctor, skill-test-suite]
---

# Skill Manager — Library Administration

You are the **skill library administrator**. You manage the full lifecycle of skills in `~/.claude/commands/`.

## Commands

### LIST — Browse skills
```
/skill-manager list                    (all 146, categorized)
/skill-manager list trading            (trading skills only)
/skill-manager list --by-size          (largest first)
/skill-manager list --by-usage         (most used first, from usage.json)
/skill-manager list --unused           (never invoked)
/skill-manager list --by-category      (grouped by domain)
```

### FIND — Search skills
```
/skill-manager find fibonacci          (search by keyword)
/skill-manager find --tag ict          (search by tag)
/skill-manager find --category quant   (search by category)
```

### DEPENDENCY-GRAPH — Visualize relationships
```
/skill-manager dependency-graph trading-brain
```
Outputs ASCII graph:
```
trading-brain
├── requires: market-regime-classifier
├── requires: strategy-selection
├── requires: ict-smart-money
│   ├── requires: market-structure-bos-choch
│   └── requires: liquidity-analysis
└── feeds-into: mt5-integration
               risk-and-portfolio
               trade-journal-analytics
```

### DUPLICATES — Find overlapping skills
```
/skill-manager duplicates
```
Compares skill descriptions and identifies:
- Exact duplicates (100% overlap)
- Near-duplicates (>70% overlap)
- Subset skills (one covers the other)

### UPDATE-CHECK — Flag potentially outdated skills
```
/skill-manager update-check
```
Flags skills referencing:
- Library versions that may have updates
- Deprecated APIs (MT4 functions in MT5 skills, etc.)
- Links that may be broken

### BATCH-TEST — Validate all skills
```
/skill-manager batch-test              (test all 146)
/skill-manager batch-test trading      (test category)
```
For each skill:
1. Check frontmatter is valid
2. Verify `$ARGUMENTS` present
3. Run a sample invocation
4. Grade output quality (1-5)

### ADD — Install a new skill
```
/skill-manager add --from-url https://...
/skill-manager add --from-file path/to/skill.md
/skill-manager add --generate "topic: ICT silver bullet"
```

### REMOVE — Delete a skill
```
/skill-manager remove skill-name       (with confirmation)
/skill-manager remove --unused         (remove all never-used)
```

### MERGE — Combine two skills
```
/skill-manager merge skill-a skill-b --output merged-skill
```

### EXPORT — Package skills
```
/skill-manager export trading          (zip trading skills)
/skill-manager export --all            (zip all 146)
/skill-manager export --format plugin  (package as Claude plugin)
```

### STATS — Library statistics
```
/skill-manager stats
```
Output:
```
Total skills:      146
Total size:        ~2.1MB
Avg skill size:    14KB
Largest:           brain-ecosystem-mcp (144KB)
Smallest:          market-breadth-analyzer (2KB)
Categories:        Trading(101), Dev(21), AI(19), Media(5)
Last modified:     2026-03-18
```
