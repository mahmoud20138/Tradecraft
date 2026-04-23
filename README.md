# Claude Skills Collection

> **161 curated AI skills** as a Claude Code plugin — trading, AI development, software engineering, Claude Code platform, data acquisition, and domain knowledge.

[![Skills](https://img.shields.io/badge/skills-161-blue?style=for-the-badge)](.)
[![Domains](https://img.shields.io/badge/domains-6-green?style=for-the-badge)](.)
[![Plugin](https://img.shields.io/badge/claude_code-plugin-2dd4bf?style=for-the-badge)](https://code.claude.com/docs/en/plugins)
[![License](https://img.shields.io/badge/license-MIT-informational?style=for-the-badge)](LICENSE)

---

## Quick Install

Inside Claude Code:

```shell
/plugin marketplace add mahmoud20138/Claude-Skills-Collection
/plugin install claude-skills-collection@claude-skills-collection
```

Then invoke any skill by name:

```shell
/claude-skills-collection:trading-fundamentals
/claude-skills-collection:ict-smart-money
/claude-skills-collection:mcp-integration
/claude-skills-collection:agent-development
# ...161 skills total
```

Each skill is also model-invocable — Claude will auto-select the right skill based on your task context. Run `/help` to browse all skills under the `claude-skills-collection:` namespace.

---

## What's Inside

| Domain | Skills | Examples |
|---|---:|---|
| **Trading** | 106 | `trading-fundamentals`, `ict-smart-money`, `smc-beginner-pro-guide`, `risk-and-portfolio`, `backtesting-systems` |
| **AI Development** | 9 | `agent-development`, `mcp-integration`, `prompt-engineering`, `rag-systems` |
| **Software Engineering** | 22 | `system-design`, `api-design`, `testing-strategies`, `git-workflows` |
| **Claude Code Platform** | 18 | `plugin-development`, `hook-development`, `skill-management`, `automation-governance` |
| **Data Acquisition** | 4 | `web-scraping`, `api-integration`, `data-pipelines`, `streaming-ingestion` |
| **Domain Specific** | 2 | Specialized vertical knowledge |

Each skill is a self-contained Markdown knowledge base with:
- **Domain expertise** — curated knowledge on a focused topic
- **Executable code** — runnable blocks in Python, TypeScript, MQL5, SQL, etc.
- **Trigger keywords** — YAML frontmatter so Claude auto-selects the right skill
- **Cross-references** — links to related skills, forming a navigable graph

---

## Plugin Structure

```
Claude-Skills-Collection/
├── .claude-plugin/
│   └── marketplace.json                ← Marketplace catalog (entry point)
└── plugins/
    └── claude-skills-collection/
        ├── .claude-plugin/
        │   └── plugin.json             ← Plugin manifest
        └── skills/
            ├── trading-fundamentals/
            │   └── SKILL.md
            ├── ict-smart-money/
            │   └── SKILL.md
            └── ... (161 total)
```

Layout follows the [Claude Code plugin marketplace spec](https://code.claude.com/docs/en/plugin-marketplaces).

---

## Local Development

Test a change without publishing:

```shell
claude --plugin-dir ./plugins/claude-skills-collection
```

Edit any `plugins/claude-skills-collection/skills/<name>/SKILL.md`, then inside Claude run `/reload-plugins` to pick up changes.

Validate the marketplace catalog:

```shell
claude plugin validate .
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or edit skills.

---

## License

MIT — see [LICENSE](LICENSE).
