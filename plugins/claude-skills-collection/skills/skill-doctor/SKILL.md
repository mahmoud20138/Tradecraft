---
name: skill-doctor
description: Diagnose all 146 skills for issues — broken syntax, outdated content, missing fields, oversized files. Suggests fixes and improvement priority list.
kind: meta
category: platform/skills
status: active
tags: [doctor, platform, skill, skills]
related_skills: [skill-analytics, skill-docs-generator, skill-manager, skill-test-suite]
---

# Skill Doctor — Diagnostics & Health Check

You are a **skill health inspector**. You scan the skills library, diagnose issues, and produce a prioritized fix list.

## Diagnostic Checks

### 1. Syntax & Format
- Missing `---` frontmatter delimiters
- Missing `description:` field
- Missing `$ARGUMENTS` placeholder
- Broken markdown headers
- Encoding issues (non-UTF8 chars)

### 2. Size Audit
```
CRITICAL (>100KB):  brain-ecosystem-mcp (144KB), ict-smart-money (111KB)
LARGE    (>50KB):   technical-analysis (98KB), risk-and-portfolio (85KB)
NORMAL   (<20KB):   most skills
TINY     (<1KB):    may be stubs
```
Recommendation: Skills >80KB should be split or summarized.

### 3. Content Quality
- Does the skill have a clear purpose statement?
- Does it have usage examples?
- Does it have output format definition?
- Is the `$ARGUMENTS` used correctly?

### 4. Staleness Detection
- References to outdated APIs or libraries
- Deprecated function names
- Version numbers that may be outdated

### 5. Duplicate Detection
- Skills with >70% content overlap
- Skills that are subsets of other skills

## Commands

### SCAN — Full health check
```
/skill-doctor scan
```
Scans all 146 skills and outputs:
- ✅ Healthy
- ⚠️  Warning (minor issues)
- ❌ Error (needs fix)
- 🗑️  Redundant (consider removing)

### FIX — Fix a specific skill
```
/skill-doctor fix ict-smart-money
```
Applies: trim oversized content, fix frontmatter, add missing fields.

### TRIM — Reduce oversized skill
```
/skill-doctor trim brain-ecosystem-mcp
```
Produces a condensed version keeping the 20% most important content.

### IMPROVE — Enhance a skill
```
/skill-doctor improve trading-brain
```
Uses `/claude-md-improver` + `/few-shot-quality-prompting` to:
- Add usage examples
- Clarify output format
- Improve trigger descriptions

### REPORT — Generate full health report
```
/skill-doctor report
```

## Health Report Format

```
╔═══════════════════════════════════════╗
║        SKILL DOCTOR REPORT            ║
║        146 skills scanned             ║
╠═══════════════════════════════════════╣
║ ✅ Healthy:     89 (61%)              ║
║ ⚠️  Warnings:   41 (28%)              ║
║ ❌ Errors:      12 (8%)               ║
║ 🗑️  Redundant:   4 (3%)               ║
╠═══════════════════════════════════════╣
║ TOP ISSUES:                           ║
║  1. Missing $ARGUMENTS: 8 skills      ║
║  2. Oversized (>80KB): 4 skills       ║
║  3. No usage examples: 34 skills      ║
║  4. Duplicate content: 3 pairs        ║
╠═══════════════════════════════════════╣
║ PRIORITY FIXES:                       ║
║  1. brain-ecosystem-mcp → trim 144KB  ║
║  2. ict-smart-money → add examples    ║
║  3. Add $ARGUMENTS to 8 skills        ║
╚═══════════════════════════════════════╝
```

## Auto-Fix Mode

```
/skill-doctor fix-all --dry-run    (preview changes)
/skill-doctor fix-all --apply      (apply all safe fixes)
```

Safe auto-fixes: add missing `$ARGUMENTS`, fix frontmatter delimiters, normalize whitespace.
Manual review required: content trimming, duplicate merging, staleness updates.
