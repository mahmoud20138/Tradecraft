---
name: search
description: Entry-point skill discovery. Given a keyword or task description, returns the shortest list of Tradecraft skills that match, with direct invocation recipes. No keyword = show the 5 main entry points. USE FOR - find skill, which skill, how do I, search skills, list skills, what can this do, find command.
user-invocable: true
kind: reference
category: platform/entry
status: active
tags: [entry-point, search, discovery, routing, help]
related_skills:
  - smart-skill-router
  - analyze
  - markets
  - recommendations
  - strategies
skill_level: beginner
---

# Search — Skill Discovery Entry Point

One of the **five entry-point commands** for Tradecraft. Call it to find the right specialist skill for your task without scrolling through 169 names.

## Invocation

```text
/tradecraft:search [keyword...]

# examples
/tradecraft:search                          # overview of the 5 entry points
/tradecraft:search breakout strategy        # shortlist matching "breakout"
/tradecraft:search risk sizing              # shortlist matching "risk sizing"
/tradecraft:search ict order blocks         # shortlist matching ICT concepts
/tradecraft:search mcp                      # shortlist matching Claude-Code MCP skills
```

## What Claude Should Return

### No keyword — show the 5 primary commands

Output a compact menu:

```
Tradecraft has 169 skills. Start with one of these 5 entry points:

  /tradecraft:analyze <SYMBOL>              One-shot analysis for any ticker
  /tradecraft:search <keyword>              Find the right specialist skill
  /tradecraft:markets [watchlist]           Live scan of key symbols
  /tradecraft:recommendations [watchlist]   Ranked trade setups right now
  /tradecraft:strategies [name]             Strategy selector / deep-dive

Power users: every specialist skill is directly invocable as
  /tradecraft:<skill-name>  (see COMMANDS.md for the full list)
```

### With a keyword — shortlist

1. Invoke `smart-skill-router` if available; otherwise scan `COMMANDS.md` and the `plugins/tradecraft/skills/*/SKILL.md` frontmatter.
2. Return the top 5-8 matches as:

```
Matching "breakout strategy":

  /tradecraft:zone-refinement-sniper-entry   Precise entry inside POI
  /tradecraft:dan-zanger-breakout-strategy   Classic momentum breakout
  /tradecraft:gold-orb-ea                    Opening-range breakout for gold
  /tradecraft:strategy-selection             Pick the right strategy for regime
  /tradecraft:ict-smart-money                BOS/CHoCH structure

Closest fit: /tradecraft:strategy-selection
Quick invoke:   /tradecraft:strategy-selection XAUUSD H1
```

3. Highlight the best match as "Closest fit" with a ready-to-run command.

## Design Rules (so output stays useful, not a data dump)

- Cap matches at 8. If more, show top 5 + "... and N more — run `/tradecraft:search <more-specific-keyword>`".
- Each match is one line: `command` + one-clause purpose (pulled from the skill's frontmatter `description`).
- End with one "Closest fit" recommendation and a copy-pasteable invocation.
- Never return the full 169-skill list — that's what COMMANDS.md is for.

## Related

- `smart-skill-router` — underlying semantic skill search engine this wraps
- `analyze` / `markets` / `recommendations` / `strategies` — the other 4 entry points
- `COMMANDS.md` (repo root) — canonical full reference
