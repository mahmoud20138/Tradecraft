# Tradecraft

> **5 entry-point commands** on top of **169 curated AI skills** — trading, AI development, software engineering, Claude Code platform, data acquisition, and more. You don't need to remember 169 names: start with one of the 5, let it route you in.

[![Skills](https://img.shields.io/badge/skills-169-blue?style=for-the-badge)](COMMANDS.md)
[![Domains](https://img.shields.io/badge/domains-6-green?style=for-the-badge)](COMMANDS.md)
[![Plugin](https://img.shields.io/badge/claude_code-plugin-2dd4bf?style=for-the-badge)](https://code.claude.com/docs/en/plugins)
[![License](https://img.shields.io/badge/license-MIT-informational?style=for-the-badge)](LICENSE)

**📖 [Install manual](INSTALL.md) · [Full command reference](COMMANDS.md) · [Contributing](CONTRIBUTING.md)**

---

## Quick Install

Inside Claude Code:

```shell
/plugin marketplace add https://github.com/mahmoud20138/Tradecraft.git
/plugin install tradecraft@tradecraft
```

> The full HTTPS URL is recommended because the `owner/repo` shorthand can resolve to SSH on some machines and fail if GitHub isn't in `~/.ssh/known_hosts`. See [INSTALL.md](INSTALL.md) for the full setup.

**Works on Windows, macOS, and Linux.** The default free data path is cross-platform (yfinance, no credentials). The optional MT5 upgrade path is Windows-only (MetaQuotes ships the `MetaTrader5` Python package for Windows only). See the [platform support matrix](INSTALL.md#platform-support) for details.

For live market data on the `fetch-quotes` / `analyze-*` combination skills (free path, no account, no API key):

```shell
pip install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"
```

## The 5 entry points

Start here. These five commands cover the full collection:

| Command | What it does |
|---|---|
| `/tradecraft:analyze <SYMBOL>` | One-shot deep analysis for any ticker — regime, structure, entry, SL/TP, JSON plan |
| `/tradecraft:search [keyword]` | Find the right specialist skill by keyword; no arg shows the 5-entry-point menu |
| `/tradecraft:markets [watchlist]` | Live watchlist snapshot (last, H4 bias, ATR, session) via free yfinance path |
| `/tradecraft:recommendations [watchlist] [N]` | Top N ranked trade setups across the watchlist right now |
| `/tradecraft:strategies [name] [symbol]` | Strategy selector and deep-dive (ICT, SMC, breakout, scalp, swing, trend) |

### Examples

```shell
/tradecraft:analyze XAUUSD                             # one-shot gold analysis
/tradecraft:search risk sizing                         # find skills matching "risk sizing"
/tradecraft:markets                                    # scan default watchlist
/tradecraft:recommendations XAUUSD,US30,EURUSD 3       # top 3 setups from those 3 symbols
/tradecraft:strategies ict XAUUSD                      # ICT deep-dive tuned for gold
```

### Power users: direct skill invocation

All **169 skills** are still directly invokable as `/tradecraft:<skill-name>` — the 5 entry points are an ergonomic layer, nothing is hidden. See the full list in [COMMANDS.md](COMMANDS.md), grouped by domain with per-skill descriptions.

Each skill is also model-invocable — Claude will auto-select the right one based on your task context. Run `/help` to browse under the `tradecraft:` namespace. Full step-by-step setup (including optional MT5 for broker-exact prices) is in **[INSTALL.md](INSTALL.md)**.

---

## What's Inside

| Domain | Skills | Examples |
|---|---:|---|
| **Trading** | 104 | `trading-fundamentals`, `ict-smart-money`, `analyze`, `markets`, `recommendations`, `strategies`, `pair-analyze`, `analyze-gold`, `analyze-us30` |
| **AI Development** | 7 | `agent-development`, `mcp-integration`, `ai-agent-builder`, `few-shot-quality-prompting` |
| **Software Engineering** | 20 | `pro-code-architecture`, `elite-ui-design`, `system-design-academy`, `debug-failing-test` |
| **Claude Code Platform** | 20 | `search`, `plugin-structure`, `hook-development`, `skill-development`, `command-development` |
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
            └── ... (169 total)
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
