# Tradecraft — Install Manual

Step-by-step install for the Tradecraft Claude Code plugin (165 AI skills for trading, AI development, software engineering, and more).

---

## Prerequisites

| Requirement | Why | How to check |
|---|---|---|
| **Claude Code CLI** | Runs the plugin | `claude --version` |
| **Python 3.9+** | Needed for `/tradecraft:fetch-quotes` (market data) | `python --version` |
| **`pip`** | Install the three Python deps | `pip --version` |
| **Git** | Claude Code clones the marketplace over HTTPS | `git --version` |

Claude Code install guide: <https://code.claude.com/docs/en/quickstart>

You do **not** need a broker account, MT5, Yahoo account, or any API key for the free-path defaults.

---

## 1. Add the marketplace

Run this inside any Claude Code session:

```shell
/plugin marketplace add https://github.com/mahmoud20138/Tradecraft.git
```

> **Why the full HTTPS URL, not `mahmoud20138/Tradecraft`?** The shorthand form sometimes resolves to SSH (`git@github.com:...`), which fails on machines without GitHub's SSH host key in `~/.ssh/known_hosts`. The HTTPS URL avoids the issue entirely — no SSH, no credentials, public repo. If your environment is SSH-ready you can use the shorthand; otherwise stick with HTTPS.

(Old URL `https://github.com/mahmoud20138/Claude-Skills-Collection.git` still works — GitHub auto-redirects from the prior name.)

You should see a confirmation that the `tradecraft` marketplace was added. Verify with:

```shell
/plugin marketplace list
```

---

## 2. Install the plugin

```shell
/plugin install tradecraft@tradecraft
```

The first word is the plugin name; the part after `@` is the marketplace name — both are `tradecraft`.

Verify with:

```shell
/plugin list
/help
```

`/help` should now show entries under `tradecraft:` — 165 of them.

---

## 3. Install the Python deps (free-path data)

Only required if you want `/tradecraft:fetch-quotes` or any of the `analyze-*` combination skills to actually pull live data.

```shell
pip install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"
```

That installs:
- **yfinance** — free market data (no account, no API key)
- **pandas** — OHLCV data wrangling
- **matplotlib** (optional) — chart rendering for the `--chart` flag

If `${CLAUDE_PLUGIN_ROOT}` doesn't resolve in your shell, substitute the full path Claude Code reports when you run `/plugin list` (typically `~/.claude/plugins/cache/tradecraft/tradecraft/<version>/scripts/requirements.txt`).

---

## 4. (Optional) Broker-exact pricing via local MT5

Skip this section unless you have a MetaTrader 5 broker account and want your OWN broker's tick data instead of Yahoo's delayed public feed.

Windows only:

```shell
pip install MetaTrader5
```

Then launch MT5 on the same machine and log into your broker. After that, any command run with `--source auto` (the default) will prefer MT5 over yfinance automatically.

Test:

```shell
/tradecraft:fetch-quotes XAUUSD H1 1 mt5
```

You should see `"source": "mt5"` in the JSON response. If MT5 isn't running, this invocation errors out (exit code 2) — that's intentional: `mt5` mode is strict. Use `auto` or `free` for silent fallback.

---

## 5. First invocations

Verify end-to-end with the free path:

```shell
/tradecraft:fetch-quotes XAUUSD H1 50 free
```

Expected: JSON with `"source": "yfinance"`, `"broker_symbol": "GC=F"`, 50 bars, a `latest` block, and a `note` explaining the Yahoo data caveats.

Then try a combination command:

```shell
/tradecraft:analyze-gold H1 standard
/tradecraft:analyze-us30 H4 conservative
/tradecraft:pair-analyze EURUSD M15 scalp
```

Each runs the full pipeline: data fetch → regime → fundamentals gate → ICT/SMC structure → liquidity → entry refinement → risk sizing → JSON trade plan.

For the 164+ knowledge skills (no shell commands, just instructions for Claude):

```shell
/tradecraft:trading-fundamentals
/tradecraft:ict-smart-money
/tradecraft:mcp-integration
# ... see COMMANDS.md for the full list
```

---

## 6. Updating

When the plugin changes:

```shell
/plugin marketplace update
/plugin update tradecraft@tradecraft
/reload-plugins
```

Or to reload after editing a skill locally (dev loop):

```shell
/reload-plugins
```

---

## 7. Uninstall

```shell
/plugin uninstall tradecraft@tradecraft
/plugin marketplace remove tradecraft
```

(Removing a marketplace also uninstalls all plugins installed from it.)

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `/help` doesn't show `tradecraft:` skills | Marketplace added but plugin not installed | Run `/plugin install tradecraft@tradecraft`, then `/reload-plugins` |
| `"source": "yfinance"` when you expected `"mt5"` | MT5 not running, not logged in, or `MetaTrader5` lib missing | Launch MT5 and log in; `pip install MetaTrader5`; re-run with `--source auto` |
| `fetch_quotes.py` — `ModuleNotFoundError: yfinance` | Step 3 skipped | `pip install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"` |
| Exit code 2 from `fetch-quotes --source mt5` | `mt5` mode is strict (by design) | Use `auto` if you want silent fallback to yfinance |
| Exit code 4 ("no data from any source") | Ticker doesn't exist at either feed | Double-check the symbol; try a broker variant like `XAUUSDm` or the yfinance form like `GC=F` |
| `/plugin validate .` fails | Local dev edit broke frontmatter | Run `claude plugin validate .` from the repo root; fix the flagged YAML |
| Old slash prefix `/claude-skills-collection:` no longer works | Plugin was renamed to `tradecraft` | Use `/tradecraft:<skill>` — run `/plugin marketplace update` to pick up the rename |
| `Failed to clone marketplace repository: SSH host key is not in your known_hosts file` | Claude Code tried SSH (`git@github.com`) but your `~/.ssh/known_hosts` has no GitHub entry | Use the explicit HTTPS URL: `/plugin marketplace add https://github.com/mahmoud20138/Tradecraft.git`. Or, to keep using the shorthand, run `ssh-keyscan -t rsa,ecdsa,ed25519 github.com >> ~/.ssh/known_hosts` once. |

For bugs and feature requests: <https://github.com/mahmoud20138/Tradecraft/issues>

---

## What's next

- **[COMMANDS.md](COMMANDS.md)** — full reference of all 165 skills, grouped by domain
- **[README.md](README.md)** — high-level overview and quick install
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — how to add or edit skills
