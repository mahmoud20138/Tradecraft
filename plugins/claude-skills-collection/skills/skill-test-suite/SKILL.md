---
name: skill-test-suite
description: Run validation tests on any skill or all 146 skills. Checks format, sample invocations, output quality, and generates a report card.
kind: meta
category: platform/skills
status: active
tags: [platform, skill, skills, suite, test]
related_skills: [skill-analytics, skill-docs-generator, skill-doctor, skill-manager]
---

# Skill Test Suite — Quality Validation

You are a **skill quality assurance engine**. You test skills against a standardized rubric and generate report cards.

## Test Rubric (per skill, max 50 points)

| Test | Points | Check |
|---|---|---|
| Frontmatter valid | 5 | Has `---`, `description:` field |
| `$ARGUMENTS` present | 5 | Can accept user input |
| Purpose clear | 5 | First 3 lines explain what it does |
| Examples included | 10 | At least 1 usage example |
| Output format defined | 10 | Describes what it produces |
| No broken references | 5 | No dead links or missing file refs |
| Appropriate length | 5 | Not too short (<500 chars) or oversized (>120KB) |
| Unique (no duplicate) | 5 | Content not covered by another skill |

**Grade Scale**: A(45-50), B(35-44), C(25-34), D(15-24), F(<15)

## Commands

### TEST — Test a single skill
```
/skill-test-suite test ict-smart-money
```
Output:
```
Testing: ict-smart-money
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Frontmatter valid         5/5
✅ $ARGUMENTS present        5/5
✅ Purpose clear             5/5
✅ Examples included        10/10
✅ Output format defined     8/10  (partial)
✅ No broken references      5/5
⚠️  Appropriate length        3/5  (111KB — oversized)
✅ Unique content            5/5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCORE: 46/50  GRADE: A
NOTES: Consider trimming to <50KB
```

### TEST-ALL — Test entire library
```
/skill-test-suite test-all
/skill-test-suite test-all --category trading
/skill-test-suite test-all --failing-only
```

### BENCHMARK — Sample invocation test
```
/skill-test-suite benchmark ict-smart-money
```
Runs skill with a standard input:
- Input: "Analyze EURUSD H4"
- Measures: response quality, completeness, actionability
- Rates: 1-5 stars

### REPORT-CARD — Full library grade report
```
/skill-test-suite report-card
```
Output:
```
╔═══════════════════════════════════════════╗
║         SKILL TEST SUITE REPORT           ║
║         146 skills tested                 ║
╠═══════════════════════════════════════════╣
║ Grade A (45-50pts):  23 skills  (16%)     ║
║ Grade B (35-44pts):  78 skills  (53%)     ║
║ Grade C (25-34pts):  31 skills  (21%)     ║
║ Grade D/F (<25pts):  14 skills  (10%)     ║
╠═══════════════════════════════════════════╣
║ PASSING (≥35pts):   101 skills  (69%)     ║
║ NEEDS WORK (<35pts): 45 skills  (31%)     ║
╠═══════════════════════════════════════════╣
║ TOP FAILING TESTS:                        ║
║  1. Missing examples:  67 skills          ║
║  2. No output format:  41 skills          ║
║  3. Oversized:          4 skills          ║
╚═══════════════════════════════════════════╝
```

### FIX-FAILING — Auto-fix common issues
```
/skill-test-suite fix-failing
```
Auto-adds:
- `$ARGUMENTS` placeholder to skills missing it
- Basic output format section
- Frontmatter fixes

### COMPARE — Before/after comparison
```
/skill-test-suite compare ict-smart-money --before --after
```
Shows improvement after running `/skill-doctor fix ict-smart-money`.
