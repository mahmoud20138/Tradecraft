---
name: news-intelligence
description: >
  Multi-source news intelligence gathering, cross-domain analysis, and skill routing for comprehensive
  situational awareness. Use this skill whenever the user asks "what's happening", "news today",
  "catch me up", "morning brief", "market news", "what's affecting gold/forex/USD", "AI news",
  "scan the news", "what should I know", or any request for current events awareness. Also trigger
  when user asks about market impact of events, cross-domain connections, or wants to understand
  how news in one area (geopolitics, macro, tech) affects another (trading, career, currencies).
  Works with currency-strength-meter, automated-strategy-builder, cross-timeframe-divergence-scanner,
  multi-tf-order-block-mapper, candlestick-statistics-engine, youtube-video-to-knowledge, and
  mq5-mq4-how-to-work-with for actionable routing.
kind: reference
category: trading/data
status: active
tags: [data, forex, intelligence, news, radar, trading]
related_skills: [economic-calendar, market-data-ingestion, alternative-data-integrator, economic-indicator-tracker, market-intelligence]
---

# News Intelligence Radar

Comprehensive situational awareness engine that gathers news across domains, identifies cross-domain
connections, assesses impact, and routes actionable intelligence to your other skills.

## When This Skill Triggers

- "What's happening?" / "Catch me up" / "Morning brief"
- "News about gold / forex / AI / tech"
- "What's affecting [instrument/market]?"
- "How does [event X] impact [domain Y]?"
- "Scan news for [topic]"
- "What should I be watching today?"
- Any question about current events that benefits from multi-source analysis
- References to market-moving events, geopolitical situations, or industry developments

## Architecture

```
User Query
    │
    ├─[1] CLASSIFY REQUEST → What type of scan?
    │     ├── Morning Brief (all priority domains)
    │     ├── Topic Scan (specific subject)
    │     ├── Event Analysis (single event, deep)
    │     └── Domain Scan (one domain, thorough)
    │
    ├─[2] GENERATE SEARCH PLAN → QueryGenerator
    │     └── 4-12 targeted web_search queries
    │
    ├─[3] EXECUTE SEARCHES → web_search + web_fetch
    │     └── Collect titles, summaries, sources, URLs
    │
    ├─[4] PROCESS RESULTS
    │     ├── DomainClassifier → Tag each item by domain
    │     ├── EntityExtractor → Pull currencies, orgs, numbers
    │     ├── ImpactAssessor → Rate high/medium/low
    │     └── RelationshipMapper → Find cross-domain chains
    │
    ├─[5] ROUTE TO SKILLS → SkillRouter
    │     └── Recommend which skills to activate next
    │
    └─[6] FORMAT OUTPUT → IntelligenceBrief
          ├── Priority Alerts
          ├── Domain Sections
          ├── Cross-Domain Connections
          ├── Skill Route Suggestions
          └── Narrative (Claude-generated synthesis)
```

## How to Execute This Skill

### Step 0: Load the Engine

```python
import sys
sys.path.insert(0, '/path/to/news-intelligence/scripts')
from news_engine import (
    QueryGenerator, DomainClassifier, EntityExtractor,
    ImpactAssessor, SkillRouter, IntelligenceBrief,
    generate_search_plan, get_upcoming_events, DOMAINS
)
from relationship_mapper import RelationshipMapper, build_narrative_prompt
```

### Step 1: Determine Scan Type

Based on what the user asked:

| User Says | Scan Mode | Domains |
|-----------|-----------|---------|
| "Morning brief" / "Catch me up" | `morning_brief` | forex, gold, ai, geopolitics |
| "Gold news" / "What's affecting XAUUSD" | `custom` | gold_commodities, forex_macro |
| "AI job market" | `custom` | ai_tech, freelance_career |
| "How does [X] affect [Y]" | `event` | auto-detect from X |
| "Full scan" / "Everything" | `full_scan` | all domains |
| "What happened with [event]" | `event` | auto-detect |

### Step 2: Generate & Execute Search Plan

```python
plan = generate_search_plan(mode="morning_brief")
# plan["queries"] → list of {"query": str, "domain": str}
# plan["upcoming_events"] → scheduled economic events today

# Then execute each query using web_search tool
# Collect results into news_items list
```

**CRITICAL — Search Execution Pattern:**

For each query in the plan, Claude should:
1. Call `web_search` with the query
2. Read the top 3-5 results
3. For high-impact items, call `web_fetch` to get the full article
4. Build a news_item dict for each meaningful result:

```python
news_item = {
    "title": "...",
    "source": "Reuters",
    "summary": "2-3 sentence summary in your own words",
    "url": "https://...",
    "domain": "",  # Will be classified
    "entities": {},  # Will be extracted
    "impact_level": "",  # Will be assessed
    "timestamp": "2025-01-01",
}
```

### Step 3: Process Results

After collecting all news items:

```python
for item in news_items:
    # Classify domain
    domains = DomainClassifier.classify(item["summary"], item["title"])
    if domains:
        item["domain"] = domains[0]["domain"]
        item["classified"] = domains

    # Extract entities
    item["entities"] = EntityExtractor.extract(f"{item['title']} {item['summary']}")

    # Assess impact
    item["impact_level"] = ImpactAssessor.assess(item["title"], item["summary"])
```

### Step 4: Find Connections & Route

```python
# Cross-domain connections
connections = RelationshipMapper.find_connections(news_items)
shared = RelationshipMapper.find_shared_entities(news_items)

# Skill routing
all_domains = []
for item in news_items:
    all_domains.extend(item.get("classified", []))
skill_routes = SkillRouter.route(all_domains)
```

### Step 5: Format the Brief

```python
brief = IntelligenceBrief.format_brief(
    news_items=news_items,
    skill_routes=skill_routes,
    brief_type="morning"
)

# Add connections report
connections_report = RelationshipMapper.format_connections_report(connections, shared)
```

### Step 6: Write the Narrative (This is YOU, Claude)

After formatting the structured brief, write a 3-4 paragraph narrative that:
- Tells the story connecting the dots across domains
- Highlights the single most important development
- Explains cascading effects (e.g., "Fed dovish → USD weak → Gold up → trading opportunity")
- Suggests 2-3 concrete actions linked to specific skills

Use the `build_narrative_prompt()` function from relationship_mapper.py as a starting guide,
but you should write the narrative directly since YOU have all the context.

## Covered Domains

| Domain | Key Topics | Linked Skills |
|--------|-----------|---------------|
| **Forex & Macro** | Central banks, rates, inflation, employment | currency-strength-meter, divergence-scanner, strategy-builder |
| **Gold & Commodities** | XAUUSD, oil, metals, safe havens | strategy-builder, order-block-mapper, candlestick-engine, MQL |
| **AI & Technology** | LLMs, AI tools, chips, startups, hiring | development-agent, codebase-understanding, MCP builder |
| **Geopolitics** | Conflicts, sanctions, elections, trade wars | currency-strength-meter |
| **Egypt Legal** | Family law, EGP exchange rate, courts | — |
| **Jordan Local** | Amman news, JOD, local economy | — |
| **Freelance & Career** | Upwork, job market, AI demand, remote work | — |

## Economic Calendar Integration

The engine includes awareness of recurring high-impact events:
- US NFP (first Friday), CPI, FOMC (mid-month)
- ECB/BOJ rate decisions
- Weekly jobless claims (Thursday), oil inventory (Wednesday)

Call `get_upcoming_events()` to check if any are scheduled today. Always mention relevant upcoming events in the brief — they affect how to interpret current news.

## Output Formats

### Morning Brief (Default)
Full structured brief with priority alerts, domain sections, connections, and skill routes.

### Quick Scan
Single-topic focused scan. Use `IntelligenceBrief.format_quick_scan(topic, findings)`.

### Event Analysis
Deep dive into a single event with multi-angle coverage and impact assessment.

### Mermaid Relationship Graph
Visual graph of cross-domain connections. Use `RelationshipMapper.generate_mermaid_graph()`.

## Practical Examples

### "What's happening with gold today?"
1. Search: gold price today, XAUUSD analysis, gold market drivers
2. Also search: Fed news (macro driver), geopolitics (safe haven driver)
3. Classify, connect (geopolitics → gold, rates → gold)
4. Route to: automated-strategy-builder, order-block-mapper
5. Output: Quick scan + trading implications

### "Morning brief"
1. Search across: forex, gold, AI, geopolitics (12-16 queries)
2. Process all results through the full pipeline
3. Output: Full intelligence brief with narrative

### "How does the new AI regulation affect my job search?"
1. Search: AI regulation news, AI job market impact, AI engineer demand
2. Classify: ai_tech + freelance_career
3. Connect: regulation → hiring patterns → freelance demand
4. Output: Event analysis with career-specific implications

## Script Locations

```
news-intelligence/
├── SKILL.md                              ← You are here
├── scripts/
│   ├── news_engine.py                    ← Core engine (queries, classify, assess, route, format)
│   └── relationship_mapper.py            ← Cross-domain connections & causal chains
└── references/
    └── domain_deep_dives.md              ← Extended domain analysis templates
```

## Tips for Best Results

1. **Scale searches to query complexity**: Morning brief = 12-16 searches. Quick topic scan = 4-6.
2. **Always check the economic calendar** via `get_upcoming_events()` — scheduled events change everything.
3. **Use web_fetch for high-impact items** — search snippets are often too brief for good analysis.
4. **Write the narrative yourself** — don't just dump the structured data. The user wants your synthesis.
5. **Route to skills proactively** — if gold is moving, suggest running the strategy builder without being asked.
6. **Cross-domain connections are the value add** — anyone can search news. The skill is connecting dots.
