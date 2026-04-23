# Tradecraft

> **165 curated AI skills** as a Claude Code plugin — trading, AI development, software engineering, Claude Code platform, data acquisition, and more. Every skill runs as a slash command: `/tradecraft:<skill>`.

[![Skills](https://img.shields.io/badge/skills-165-blue?style=for-the-badge)](COMMANDS.md)
[![Domains](https://img.shields.io/badge/domains-6-green?style=for-the-badge)](COMMANDS.md)
[![Plugin](https://img.shields.io/badge/claude_code-plugin-2dd4bf?style=for-the-badge)](https://code.claude.com/docs/en/plugins)
[![License](https://img.shields.io/badge/license-MIT-informational?style=for-the-badge)](LICENSE)

**📖 [Install manual](INSTALL.md) · [Full command reference](COMMANDS.md) · [Contributing](CONTRIBUTING.md)**

---

## Quick Install

Inside Claude Code:

```shell
/plugin marketplace add mahmoud20138/Tradecraft
/plugin install tradecraft@tradecraft
```

For live market data on the `fetch-quotes` / `analyze-*` combination skills (free path, no account, no API key):

```shell
pip install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"
```

Then invoke any skill by name:

```shell
/tradecraft:analyze-gold                   # XAUUSD combination (fetch -> regime -> ICT -> risk -> plan)
/tradecraft:analyze-us30 H4 conservative   # Dow combination, H4 conservative mode
/tradecraft:pair-analyze EURUSD M15 scalp  # parametric combination for any pair
/tradecraft:fetch-quotes BTCUSD D1 300     # free market data (yfinance) + MT5 if installed
/tradecraft:trading-fundamentals           # any of the 164+ knowledge skills
# full list: see COMMANDS.md
```

Each skill is also model-invocable — Claude will auto-select the right skill based on your task context. Run `/help` to browse all skills under the `tradecraft:` namespace. Full step-by-step setup (including optional MT5 for broker-exact prices) is in **[INSTALL.md](INSTALL.md)**.

---

## What's Inside

| Domain | Skills | Examples |
|---|---:|---|
| **Trading** | 101 | `trading-fundamentals`, `ict-smart-money`, `smc-beginner-pro-guide`, `risk-and-portfolio`, `analyze-gold`, `analyze-us30`, `pair-analyze` |
| **AI Development** | 7 | `agent-development`, `mcp-integration`, `ai-agent-builder`, `few-shot-quality-prompting` |
| **Software Engineering** | 20 | `pro-code-architecture`, `elite-ui-design`, `system-design-academy`, `debug-failing-test` |
| **Claude Code Platform** | 19 | `plugin-structure`, `hook-development`, `skill-development`, `command-development` |
| **Data Acquisition** | 4 | `firecrawl`, `video-gen`, `video-knowledge-extractor`, `youtube-video-to-knowledge` |
| **Domain Specific** | 2 | Specialized vertical knowledge |

(Counts match [COMMANDS.md](COMMANDS.md). A further 12 skills are currently uncategorized — see that reference.)

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
    └── tradecraft/
        ├── .claude-plugin/
        │   └── plugin.json             ← Plugin manifest
        └── skills/
            ├── trading-fundamentals/
            │   └── SKILL.md
            ├── ict-smart-money/
            │   └── SKILL.md
            └── ... (165 total)
```

Layout follows the [Claude Code plugin marketplace spec](https://code.claude.com/docs/en/plugin-marketplaces).

---

## Local Development

Test a change without publishing:

```shell
claude --plugin-dir ./plugins/tradecraft
```

Edit any `plugins/tradecraft/skills/<name>/SKILL.md`, then inside Claude run `/reload-plugins` to pick up changes.

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
