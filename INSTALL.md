# Tradecraft — Install Manual

Step-by-step install for the Tradecraft Claude Code plugin (165 AI skills for trading, AI development, software engineering, and more).

---

## Platform support

| Component | Windows | macOS | Linux |
|---|---|---|---|
| The plugin itself (marketplace add + install) | ✅ | ✅ | ✅ |
| The 161 pure-markdown knowledge skills | ✅ | ✅ | ✅ |
| `/tradecraft:fetch-quotes` — free path (yfinance) | ✅ | ✅ | ✅ |
| `/tradecraft:fetch-quotes` — MT5 path | ✅ | ❌ (`MetaTrader5` PyPI package publishes Windows wheels only) | ❌ |
| `/tradecraft:pair-analyze`, `analyze-gold`, `analyze-us30` | ✅ | ✅ | ✅ (use free source by default) |
| Skills hardcoded to the author's local paths: `ict-trading-tool`, `xtrading-analyze`, `smart-skill-router` | ⚠️ Adapt paths | ❌ | ❌ |
| Skills that need Windows + a running MT5 terminal: `gold-orb-ea`, `mt5-integration`, `mt5-chart-browser`, `realtime-alert-pipeline` | ✅ (with MT5) | ❌ | ❌ |
| Data Acquisition skills (`firecrawl`, `video-gen`, `video-knowledge-extractor`, `youtube-video-to-knowledge`) | ⚠️ External tooling/APIs required (Firecrawl MCP, ffmpeg, YouTube API) | ⚠️ Same | ⚠️ Same |

The default install works out of the box on all three operating systems. Only the MT5 upgrade path and a handful of skills that assume specific local tools require extra setup.

> **Skill-count math.** Total = **165**. Of those, **161** are pure-markdown knowledge skills (row 2). The remaining **4** are script-backed commands with arguments: `fetch-quotes`, `pair-analyze`, `analyze-gold`, `analyze-us30`.

---

## Prerequisites

| Requirement | Why | How to check |
|---|---|---|
| **Claude Code CLI** | Runs the plugin | `claude --version` |
| **Python 3.9+** | Needed for `/tradecraft:fetch-quotes` (market data) | `python --version` (Windows) or `python3 --version` (macOS / Linux) |
| **`pip`** | Install the three Python deps | `pip --version` or `pip3 --version` |
| **Git** | Claude Code clones the marketplace over HTTPS | `git --version` |

> **Note on `python` vs `python3`.** On Windows the Python launcher installs as `python`; on macOS and most Linux distributions `python` either doesn't exist or points at Python 2, and you should use `python3`. This manual writes `python` (Windows) everywhere — substitute `python3` on macOS / Linux. Or, simpler, `python -m pip` and `python3 -m pip` both work universally when invoked through the interpreter that's actually on your `PATH`.

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

Pick the snippet that matches your shell:

**bash / zsh / Git Bash / WSL (macOS, Linux, Windows-with-Git-Bash)**

```shell
pip install -r "${CLAUDE_PLUGIN_ROOT}/scripts/requirements.txt"
```

**Windows PowerShell**

```powershell
pip install -r "$env:CLAUDE_PLUGIN_ROOT\scripts\requirements.txt"
```

**Windows cmd.exe**

```cmd
pip install -r "%CLAUDE_PLUGIN_ROOT%\scripts\requirements.txt"
```

That installs:
- **yfinance** — free market data (no account, no API key)
- **pandas** — OHLCV data wrangling
- **matplotlib** (optional) — chart rendering for the `--chart` flag

If `${CLAUDE_PLUGIN_ROOT}` doesn't resolve in your shell, substitute the full path Claude Code reports when you run `/plugin list` — typically `~/.claude/plugins/cache/tradecraft/tradecraft/<version>/scripts/requirements.txt` on macOS/Linux or `%USERPROFILE%\.claude\plugins\cache\tradecraft\tradecraft\<version>\scripts\requirements.txt` on Windows.

---

## 4. (Optional) Broker-exact pricing via local MT5

Skip this section unless you have a MetaTrader 5 broker account and want your OWN broker's tick data instead of Yahoo's delayed public feed.

**Windows only** — the `MetaTrader5` PyPI package is Windows-only (it IPCs into a running desktop MT5 terminal). On macOS / Linux this step fails cleanly and the plugin keeps using the free path.

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

For the 161 knowledge skills (no shell commands, just instructions for Claude):

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
| `ERROR: Could not find a version that satisfies the requirement MetaTrader5` / `No matching distribution found for MetaTrader5` | The `MetaTrader5` PyPI package publishes only Windows wheels; you are on macOS or Linux | The MT5 path is not available on your OS. Stay on the free yfinance path — everything else in the plugin works. |
| `${CLAUDE_PLUGIN_ROOT}: command not found` or similar from your shell | You are in PowerShell or cmd.exe, not bash | Use the PowerShell form `$env:CLAUDE_PLUGIN_ROOT` or the cmd form `%CLAUDE_PLUGIN_ROOT%` from Step 3. |
| `python: command not found` (macOS / Linux) | The binary is named `python3` on your OS | Replace `python` with `python3` in all commands, or `python -m pip` with `python3 -m pip`. |

For bugs and feature requests: <https://github.com/mahmoud20138/Tradecraft/issues>

---

## What's next

- **[COMMANDS.md](COMMANDS.md)** — full reference of all 165 skills, grouped by domain
- **[README.md](README.md)** — high-level overview and quick install
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — how to add or edit skills
