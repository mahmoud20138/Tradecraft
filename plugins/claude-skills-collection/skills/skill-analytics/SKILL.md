---
name: skill-analytics
description: Track which skills you use most, success rates, token usage, and generate improvement recommendations. Reads ~/.claude/usage.json.
kind: meta
category: platform/skills
status: active
tags: [analytics, claude-code, platform, skill, skills]
related_skills: [skill-docs-generator, skill-doctor, skill-manager, skill-test-suite]
---

# Skill Analytics — Usage Tracker & Optimizer

You are a **skill performance analytics engine**. You analyze usage patterns, identify bottlenecks, and recommend optimizations.

## Usage Data Structure

File: `~/.claude/usage.json`
```json
{
  "skills": {
    "ict-smart-money": {
      "runs": 0, "avg_tokens": 0, "total_tokens": 0,
      "avg_rating": 0, "last_used": null, "errors": 0
    }
  },
  "workflows": {},
  "daily": {},
  "totals": { "runs": 0, "tokens": 0, "sessions": 0 }
}
```

## Commands

### REPORT — Full analytics dashboard
```
/skill-analytics report
```
Output:
- Top 10 most-used skills
- Top 10 highest-rated skills
- Skills never used (candidates for removal)
- Token consumption leaders
- Usage by category (trading/dev/ai/media)
- Weekly trend charts (ASCII)

### LOG — Record a skill usage
```
/skill-analytics log skill=ict-smart-money tokens=3200 rating=5
```

### OPTIMIZE — Get improvement recommendations
```
/skill-analytics optimize
```
Analyzes:
- Skills with high token usage but low ratings → needs trimming
- Skills used frequently → should be kept lean
- Skills never used → consider removing
- Skills with errors → needs fixing

### TRENDING — What's hot this week
```
/skill-analytics trending
```

### COMPARE — Side-by-side skill comparison
```
/skill-analytics compare ict-smart-money trading-brain
```

## Auto-Logging

After each skill invocation, log:
- Skill name
- Estimated tokens used
- User rating (if provided)
- Timestamp
- Session ID

## Sample Report Output

```
═══════════════════════════════════════
        SKILL ANALYTICS REPORT
        Week of 2026-03-18
═══════════════════════════════════════

TOP 5 MOST USED:
  1. ict-smart-money      ████████████ 45 runs
  2. trading-brain        ██████████   38 runs
  3. risk-and-portfolio   ████████     31 runs
  4. backtesting-sim      ██████       24 runs
  5. technical-analysis   █████        19 runs

NEVER USED (review for removal):
  - featool-multiphysics
  - interactive-coding-challenges
  - e2b-sandboxes

TOKEN LEADERS (trim these):
  - brain-ecosystem-mcp   144KB → suggest trim to 30KB
  - ict-smart-money       111KB → frequently used, keep full
  - technical-analysis     98KB → frequently used, keep full

RATING LEADERS:
  1. trading-brain         4.9/5
  2. ict-smart-money       4.8/5
  3. risk-and-portfolio    4.7/5
═══════════════════════════════════════
```
