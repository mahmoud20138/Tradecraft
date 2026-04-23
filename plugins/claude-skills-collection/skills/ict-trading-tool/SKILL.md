---
name: ict-trading-tool
description: "Automated MT5 trading tool using ICT Smart Money Concepts. Scans 21 instruments, scores setups (0-12), generates charts, executes and monitors trades. Use for ICT scanner, MT5 automated trading, scan for ICT setups, or any automated ICT execution."
kind: tool
category: trading/strategies
status: active
tags: [ict, mt5, smart-money, strategies, tool, trading]
related_skills: [ict-smart-money, liquidity-analysis, smc-beginner-pro-guide, market-structure-bos-choch, smart-money-trap-detector]
---

# ICT Trading Tool — MT5 Automated Scanner

Automated MT5 trading tool using ICT (Inner Circle Trader) Smart Money Concepts.
Scans 21 instruments, scores setups (0-12), generates charts, executes and monitors trades.

**Tool root:** `C:\Users\Mamoud\Desktop\ICT-Trading-Tool`
**Config:** `C:\Users\Mamoud\Desktop\ICT-Trading-Tool\config.json`
**MT5 broker:** Exness (suffix `m` on all symbols)

---

## Available Commands

Run all commands from `C:\Users\Mamoud\Desktop\ICT-Trading-Tool`:

```bash
python main.py account                          # Check balance, equity, session, positions
python main.py scan --symbols SYM1 SYM2 ...    # Scan specific symbols (space-separated)
python main.py quick                            # Quick scan of 8 key instruments
python main.py charts                           # Generate H4 charts for top setups
python main.py report                           # Generate HTML/text report
python main.py full                             # Full pipeline (scan + charts + report)
python main.py trade --symbol SYM --action BUY/SELL --sl PRICE --tp PRICE
python main.py monitor                          # Live position monitor (runs until closed)
python main.py close --ticket TICKET_NUMBER     # Close a specific position
python main.py close-all                        # Emergency: close all open positions
```

---

## How to Run from Claude Code

Use the Bash tool with the working directory set:

```bash
cd C:\Users\Mamoud\Desktop\ICT-Trading-Tool && python main.py account
cd C:\Users\Mamoud\Desktop\ICT-Trading-Tool && python main.py quick
cd C:\Users\Mamoud\Desktop\ICT-Trading-Tool && python main.py scan --symbols EURUSDm GBPUSDm XAUUSDm
```

Claude Code executable: `C:\Users\Mamoud\.local\bin\claude.exe`
OpenCode executable: `C:\Users\Mamoud\AppData\Roaming\npm\opencode.cmd`

---

## Parallel Sub-Agents (Full Scan)

For full 21-symbol scan, spawn 3 parallel claude-sonnet-coder agents:

| Agent | Symbols | Focus |
|-------|---------|-------|
| Agent 1 | USTECm US30m US500m XAUUSDm BTCUSDm ETHUSDm | NY session |
| Agent 2 | EURUSDm GBPUSDm USDJPYm USDCHFm AUDUSDm USDCADm NZDUSDm EURGBPm | London + NY |
| Agent 3 | AAPLm MSFTm AMZNm GOOGLm TSLAm NVDAm METAm | NY open only |

See `prompts/agent_instructions.md` for sub-agent task template.

---

## Prompt Templates

| File | Usage | Command |
|------|-------|---------|
| `prompts/full_scan.md` | Full 21-symbol scan with sub-agents | `claude -p prompts/full_scan.md` |
| `prompts/quick_scan.md` | Quick 8-symbol scan, no sub-agents | `claude -p prompts/quick_scan.md` |
| `prompts/monitor_only.md` | Check account + start monitor | `claude -p prompts/monitor_only.md` |
| `prompts/agent_instructions.md` | Sub-agent task boilerplate | Used internally by orchestrator |

All prompt files use `--dangerously-skip-permissions` flag.

---

## Config Key Settings

```json
{
  "mt5": { "suffix": "m" },
  "risk": {
    "max_risk_per_trade_pct": 1.0,
    "max_daily_loss_pct": 3.0,
    "max_concurrent_positions": 2,
    "max_trades_per_day": 3,
    "min_score_to_trade": 5,
    "full_risk_score": 8,
    "min_rr_ratio": 1.0
  },
  "llm": {
    "orchestrator_model": "claude-opus-4-6",
    "subagent_model": "claude-sonnet-coder"
  }
}
```

---

## Risk Management Rules

| Rule | Value |
|------|-------|
| Max risk per trade | 1.0% (0.5% if score 5-7) |
| Max concurrent positions | 2 |
| Max daily loss | 3% (auto-close all positions) |
| Max trades per day | 3 |
| Min confluence score | 5 (half risk), 8 (full risk) |
| Min RR ratio | 1:1 |
| Correlated groups count as | 1 trade combined |

**Daily loss protocol:** 2% warning → 3% auto-close → stop trading for day

---

## Symbol List (21 instruments, all with 'm' suffix)

```
Indices   : USTECm  US30m   US500m
Commodity : XAUUSDm
Crypto    : BTCUSDm ETHUSDm
Forex Maj : EURUSDm GBPUSDm USDJPYm USDCHFm AUDUSDm USDCADm
Forex Min : NZDUSDm EURGBPm
Stocks    : AAPLm   MSFTm   AMZNm   GOOGLm  TSLAm   NVDAm   METAm
```

Quick scan (8 instruments): `XAUUSDm USTECm EURUSDm GBPUSDm BTCUSDm US30m USDJPYm AAPLm`

---

## ICT Confluence Scoring

| Factor | Points | Hard Req? |
|--------|--------|-----------|
| HTF Bias (D1+H4 aligned) | +2 | YES |
| Killzone active | +2 | YES |
| Liquidity sweep confirmed | +2 | YES |
| MSS/CHoCH confirmed | +2 | YES |
| FVG at entry | +1 | No |
| Order Block at entry | +1 | No |
| OTE zone (62-79% Fib) | +1 | No |
| Premium/Discount correct | +1 | No |
| SMT Divergence | +1 | No |
| NWOG alignment | +1 | No |

Score 10-12: Full risk | Score 8-9: Full risk | Score 5-7: Half risk | <5: No trade

---

## Python Coding Rules

1. **Paths:** `os.path.join(TOOL_ROOT, "charts")` — never hardcoded backslashes
2. **Strings:** `.format()` only — no f-strings (MT5 Python 3.6 compat)
3. **Output:** ASCII-only — no Unicode, no emoji in any print/log output
4. **MT5 import:** always wrapped in `try/except ImportError` with `MT5_AVAILABLE` flag

---

## Output Directories

```
charts/    -- H4 chart images: {SYMBOL}_H4_{YYYYMMDD_HHMM}.png
reports/   -- Scan reports: report_{YYYYMMDD_HHMM}.html + .txt
logs/      -- Monitor logs: monitor_{YYYYMMDD}.log
```

---

## Core Modules

```
core/scanner.py          -- ICT setup scoring and detection
core/account.py          -- MT5 account info, balance, positions
core/chart_generator.py  -- H4 chart image rendering
core/report_generator.py -- HTML + text report generation
core/trade_executor.py   -- Trade placement and management
core/trade_monitor.py    -- Live position monitoring loop
```

---

*ICT-Trading-Tool v1.0 | MT5 + Claude Code + OpenCode | Exness broker*
