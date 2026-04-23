---
name: smart-skill-router
description: >
  Intelligent skill routing, auto-selection, dependency resolution, and bundle execution
  for the entire 265+ skill ecosystem. The brain that decides which skills to run, in what
  order, with what priority. Uses skills_index.json for instant lookup, skills_graph.json
  for dependency chains, and skill_router.py for scoring/ranking.
  Use this skill for "which skill should I use", "find skill for", "route to skill",
  "skill search", "skill lookup", "auto select skill", "run skill bundle", "skill dependencies",
  "skill graph", "skill stats", "how many skills", "list skills for", "best skill for".
  This is the ENTRY POINT for all skill-related routing decisions.
kind: meta
category: platform/routing
status: active
tags: [platform, router, routing, skill, smart]
related_skills: [context-memory, skill-pipeline, workflow-builder]
---

# Smart Skill Router

## Architecture

```
User Request
      |
      v
+------------------+
| Query Analyzer   | <-- Extract intent, domain, keywords
+------------------+
      |
      v
+------------------+
| Skill Matcher    | <-- skills_index.json (instant lookup)
+------------------+
      |
      v
+------------------+
| Ranking Engine   | <-- Score: relevance + tags + priority + deps
+------------------+
      |
      v
+------------------+
| Dependency       | <-- skills_graph.json (load prerequisites)
| Resolver         |
+------------------+
      |
      v
+------------------+
| Bundle Detector  | <-- If query spans a bundle, activate it
+------------------+
      |
      v
Execute Top Skills (max 3-5 concurrently)
```

## Quick Usage

### From Python
```python
import sys
sys.path.insert(0, r'C:\Users\Mamoud\.claude\skills')
from skill_router import find_skill, route_query, resolve_deps, get_bundle

# Search by keyword
results = find_skill("liquidity")

# Search by tags
results = find_skill(tags=["orderflow", "liquidity"])

# Full routing with scoring
top_skills = route_query("analyze liquidity trap on EURUSD H1")

# Dependency chain
deps = resolve_deps("ict-smart-money")

# Get a bundle
bundle = get_bundle("scalping")
```

### From CLI
```bash
python C:\Users\Mamoud\.claude\skills\skill_router.py search "breakout strategy"
python C:\Users\Mamoud\.claude\skills\skill_router.py route "analyze smart money on gold"
python C:\Users\Mamoud\.claude\skills\skill_router.py deps ict-smart-money
python C:\Users\Mamoud\.claude\skills\skill_router.py bundle scalping
python C:\Users\Mamoud\.claude\skills\skill_router.py stats
python C:\Users\Mamoud\.claude\skills\skill_router.py info risk-and-portfolio
```

## Scoring Formula

```
score = relevance + tag_match + dependency_bonus + priority - overlap_penalty

Where:
  relevance       = keyword match in name (+10) or description (+5)
  tag_match       = keyword match in tags (+8 per tag)
  dependency_bonus = +3 if a matched skill depends on this one
  priority        = skill priority value (1-10)
  overlap_penalty = -2 if another higher-scoring skill covers same topic
```

## Predefined Bundles

| Bundle | Skills | Use When |
|--------|--------|----------|
| **scalping** | session-scalping, order-flow-delta, liquidity-analysis, scalping-framework, trendline-sr-vision | Fast intraday trades |
| **quant** | statistics-timeseries, backtesting-sim, monte-carlo, strategy-validation, vectorized-backtester | Quantitative analysis |
| **risk** | risk-and-portfolio, risk-of-ruin, tail-risk-hedging, drawdown-playbook, drawdown-recovery | Risk assessment |
| **smc** | ict-smc, ict-smart-money, ict-smart-money, liquidity-order-flow-mapper, smart-money-trap-detector, market-structure-bos-choch | Smart money analysis |
| **chart-vision** | chart-vision, chart-vision-ai, chart-vision-renderer, chart-annotation-overlay, chart-image-preprocessor, trendline-sr-vision | Chart image analysis |
| **mean-reversion** | mean-reversion-engine, mean-reversion-oscillators, capitulation-mean-reversion, divergence-strategy-engine | Fade/reversion trades |
| **trend** | trend-following-systems, trend-breakout, breakout-strategy-engine, ma-ribbon-strategy, ichimoku-complete | Trend following |
| **news** | news-intelligence, news-sentiment, news-sentiment-nlp-engine, social-sentiment-scraper, economic-calendar | News/sentiment analysis |
| **portfolio** | portfolio-optimization, portfolio-optimizer, portfolio-allocation, portfolio-optimization | Portfolio construction |
| **mt5** | mt5-ea-code-generator, mt5-chart-browser, mt5-integration, mt5-integration, ea-code-generator | MT5 development |
| **session** | session-profiler, session-trading, session-scalping, session-scalping, session-breakout-strategies | Session-based trading |
| **fibonacci** | fibonacci-strategy-engine, fibonacci-harmonic-wave, harmonic-pattern-engine, elliott-wave-engine | Fib/harmonic analysis |
| **azure** | azure-ai, azure-deploy, azure-prepare, azure-diagnostics, azure-compute, ... (18 skills) | Azure cloud work |

## Auto-Selection Protocol

When the user makes a request:

1. **Extract keywords** from the request
2. **Run `route_query()`** to get ranked skills
3. **Check if a bundle applies** — if 3+ skills from one bundle match, activate the full bundle
4. **Resolve dependencies** for the top skills
5. **Execute in order**: dependencies first, then primary skills
6. **Record usage** via skill_health.py

## Files

| File | Purpose |
|------|---------|
| `skills_index.json` | Compiled index of all 265 skills (instant lookup) |
| `skills_graph.json` | Dependency graph, bundles, hierarchy |
| `skill_router.py` | Search, route, resolve CLI + importable module |
| `skill_health.py` | Usage tracking, confidence scoring |
| `skill_cache.py` | Result caching for expensive operations |
| `skill_usage.json` | Persistent usage statistics |
| `SKILLS_MAP.md` | Human-readable documentation |
