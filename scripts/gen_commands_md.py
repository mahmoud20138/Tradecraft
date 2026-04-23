#!/usr/bin/env python3
"""
Regenerate COMMANDS.md with:
  1. Detailed sections for the 7 parameterized commands (syntax/options/examples).
  2. Per-domain tables listing every knowledge skill with its full description.

Invoked by hand: `python scripts/gen_commands_md.py` from the repo root.
Not part of the plugin runtime; not referenced by plugin.json or marketplace.json.
"""

import os
import re
import sys
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("need pyyaml: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = "plugins/tradecraft/skills"

CAT_LABEL = {
    "trading": "Trading",
    "ai": "AI Development",
    "dev": "Software Engineering",
    "platform": "Claude Code Platform",
    "data": "Data Acquisition",
    "domain": "Domain Specific",
    "uncategorized": "Uncategorized",
}
CAT_ORDER = ["trading", "ai", "dev", "platform", "data", "domain", "uncategorized"]


def scan_skills():
    skills = {}
    by_cat = defaultdict(list)
    issues = []
    for d in sorted(os.listdir(ROOT)):
        sp = os.path.join(ROOT, d, "SKILL.md")
        if not os.path.isfile(sp):
            continue
        try:
            with open(sp, encoding="utf-8") as f:
                text = f.read()
            m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
            if not m:
                issues.append((d, "no frontmatter"))
                skills[d] = {"desc": "", "cat": "uncategorized"}
                by_cat["uncategorized"].append(d)
                continue
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except Exception as e:
                issues.append((d, f"yaml: {e}"))
                fm = {}
            name = (fm.get("name") or d).strip()
            desc = re.sub(r"\s+", " ", (fm.get("description") or "").strip())
            cat_raw = fm.get("category") or "uncategorized"
            cat = str(cat_raw).split("/")[0] or "uncategorized"
            if cat not in CAT_LABEL:
                cat = "uncategorized"
            skills[name] = {"desc": desc, "cat": cat}
            by_cat[cat].append(name)
        except Exception as e:
            issues.append((d, str(e)))
    return skills, by_cat, issues


DETAILED_SECTIONS = {
    "fetch-quotes": r"""### `/tradecraft:fetch-quotes`

Cascading market-data fetcher. yfinance by default (free, no credentials), MT5 terminal when available (broker-exact). Returns OHLCV bars + latest quote as JSON, with optional PNG chart.

**Syntax**

```text
/tradecraft:fetch-quotes <SYMBOL> [TIMEFRAME] [BARS] [SOURCE] [CHART]
```

**Arguments**

| Arg | Required | Values | Default | Meaning |
|---|---|---|---|---|
| `SYMBOL` | yes | `XAUUSD`, `US30`, `EURUSD`, `BTCUSD`, ... | — | Any supported or pass-through ticker. Broker suffixes (`XAUUSDm`, `US30.cash`) auto-normalized. |
| `TIMEFRAME` | no | `M1 M5 M15 M30 H1 H4 D1 W1` | `H1` | Bar granularity. `H4` via `free` source is resampled from 1h bars. |
| `BARS` | no | integer | `200` | Number of bars to return. |
| `SOURCE` | no | `auto`, `free`, `mt5` | `auto` | `auto` = MT5 if available else yfinance; `free` = yfinance only (zero creds); `mt5` = strict, fails if terminal down. |
| `CHART` | no | `chart` or a path | — | Pass `chart` to render an auto-named PNG, or a full path. |

**Examples**

```shell
/tradecraft:fetch-quotes XAUUSD                  # H1, 200 bars, auto
/tradecraft:fetch-quotes US30 H4                 # H4, 200 bars, auto
/tradecraft:fetch-quotes EURUSD M15 100 free     # explicit free path
/tradecraft:fetch-quotes BTCUSD D1 300 auto chart
```
""",

    "pair-analyze": r"""### `/tradecraft:pair-analyze`

Parametric multi-skill trading analysis for any symbol. Runs: data fetch → regime → fundamentals gate → ICT/SMC structure → liquidity → entry refinement → risk sizing → JSON trade plan.

**Syntax**

```text
/tradecraft:pair-analyze <SYMBOL> [TIMEFRAME] [MODE]
```

**Arguments**

| Arg | Required | Values | Default | Meaning |
|---|---|---|---|---|
| `SYMBOL` | yes | Any broker-recognized ticker | — | e.g. `XAUUSD`, `US30`, `EURUSD`, `BTCUSD` |
| `TIMEFRAME` | no | `M5 M15 M30 H1 H4 D1` | `H1` | Analysis timeframe |
| `MODE` | no | `conservative`, `standard`, `aggressive`, `scalp`, `swing` | `standard` | Risk/R:R calibration |

**Mode calibration**

| Mode | Per-trade risk | Min R:R | Setup grade | Timeframes |
|---|---:|---:|---|---|
| conservative | 0.5% | 3.0 | A only | H4, D1 |
| standard | 1.0% | 2.0 | A, B | H1, H4 |
| aggressive | 2.0% | 1.5 | A, B, C | M15, H1 |
| scalp | 0.5% | 1.5 | A only | M5, M15 |
| swing | 1.0% | 3.0 | A, B | H4, D1 |

**Examples**

```shell
/tradecraft:pair-analyze XAUUSD H1 standard
/tradecraft:pair-analyze US30 H4 conservative
/tradecraft:pair-analyze EURUSD M15 scalp
/tradecraft:pair-analyze BTCUSD D1 swing
```
""",

    "analyze-gold": r"""### `/tradecraft:analyze-gold`

Pre-configured wrapper around `pair-analyze` for **XAUUSD** with gold-specific calibration (DXY correlation, 100 oz contract, London/NY session preference, 2.5-pt SL minimum).

**Syntax**

```text
/tradecraft:analyze-gold [TIMEFRAME] [MODE]
```

Symbol is locked to `XAUUSD`. Arguments are the same as `pair-analyze` except `SYMBOL` is omitted. Mode `aggressive` is capped at 1.5% risk (lower than generic pair-analyze 2.0%).

**Examples**

```shell
/tradecraft:analyze-gold                   # H1, standard
/tradecraft:analyze-gold H4 conservative
/tradecraft:analyze-gold M15 scalp
/tradecraft:analyze-gold D1 swing
```
""",

    "analyze-us30": r"""### `/tradecraft:analyze-us30`

Pre-configured wrapper around `pair-analyze` for **US30** (Dow Jones Industrial Average CFD) with index-specific calibration (SPX/VIX correlations, cash-session gating, 40-pt SL minimum, overnight gap awareness).

**Syntax**

```text
/tradecraft:analyze-us30 [TIMEFRAME] [MODE]
```

Symbol is locked to `US30`. Arguments are the same as `pair-analyze` except `SYMBOL` is omitted. Mode `aggressive` is capped at 1.5% risk. Position math assumes $1 per index-point per 1.0 lot (most retail CFDs); for $10/point brokers, adjust lot size proportionally (see skill body).

**Examples**

```shell
/tradecraft:analyze-us30                   # H1, standard
/tradecraft:analyze-us30 H4 conservative
/tradecraft:analyze-us30 M15 aggressive
/tradecraft:analyze-us30 D1 swing
```
""",

    "master-trading-workflow": r"""### `/tradecraft:master-trading-workflow`

The full 18-phase trading workflow — pre-market preparation through post-trade review. Use when you want the exhaustive end-to-end process. `pair-analyze` is its condensed form.

**Syntax**

```text
/tradecraft:master-trading-workflow <SYMBOL> <TIMEFRAME> [OPTIONS...]
```

**Options** (mix and match)

| Option | Meaning |
|---|---|
| `phase:<name>` | Start from a specific phase (assumes upstream done) |
| `morning-brief` | Phases 1–7 only (pre-market routine) |
| `review-only` | Phases 15–17 only (post-trade review) |
| `full-auto` | All 18 phases, autonomous execution |
| `conservative` | 0.5% risk, R:R min 3:1, A-grade only |
| `aggressive` | 2% risk, R:R min 1.5:1, A+B setups |

**Examples**

```shell
/tradecraft:master-trading-workflow EURUSD H4
/tradecraft:master-trading-workflow XAUUSD H1 phase:scan
/tradecraft:master-trading-workflow all-pairs morning-brief
/tradecraft:master-trading-workflow BTCUSD D1 review-only
```
""",

    "xtrading-analyze": r"""### `/tradecraft:xtrading-analyze`

Full multi-strategy scan using the 6-layer autonomous trading AI (multi-agent system, trade-psychology coach, trading brain, super skills). Assumes a local MT5 + Python pipeline for live data and chart generation.

**Syntax**

```text
/tradecraft:xtrading-analyze <SYMBOL-OR-LIST> [TIMEFRAME]
```

**Examples**

```shell
/tradecraft:xtrading-analyze XAUUSD
/tradecraft:xtrading-analyze XAUUSD,US30,US100 H1
/tradecraft:xtrading-analyze all
```
""",

    "analyze": r"""### `/tradecraft:analyze`

Instant full trading analysis for any ticker. Auto-detects asset class and timeframe, then runs the master workflow.

**Syntax**

```text
/tradecraft:analyze <SYMBOL>
```

**Examples**

```shell
/tradecraft:analyze EURUSD
/tradecraft:analyze AAPL
/tradecraft:analyze BTCUSD
/tradecraft:analyze XAUUSD
/tradecraft:analyze NQ
```
""",
}

PARAM_ORDER = [
    "fetch-quotes", "pair-analyze", "analyze-gold", "analyze-us30",
    "master-trading-workflow", "xtrading-analyze", "analyze",
]


def build_md(skills, by_cat, issues):
    total = sum(len(v) for v in by_cat.values())
    out = []

    out.append("# Tradecraft — Commands Reference")
    out.append("")
    out.append(
        f"Every skill in Tradecraft is invoked as `/tradecraft:<skill-name>`. "
        f"Total: **{total}** skills across **6** domains (plus {len(by_cat['uncategorized'])} currently uncategorized)."
    )
    out.append("")
    out.append("To install, see **[INSTALL.md](INSTALL.md)**.")
    out.append("")
    out.append("## Table of Contents")
    out.append("")
    out.append("- [Parameterized commands](#parameterized-commands) — skills that accept arguments")
    for key in PARAM_ORDER:
        anchor = f"tradecraft{key}"
        out.append(f"  - [`/tradecraft:{key}`](#{anchor})")
    out.append("- [All skills by domain](#all-skills-by-domain)")
    for cat in CAT_ORDER:
        if by_cat.get(cat):
            label = CAT_LABEL[cat]
            anchor = label.lower().replace(" ", "-")
            out.append(f"  - [{label}](#{anchor}) ({len(by_cat[cat])})")
    out.append("")
    out.append("---")
    out.append("")

    # Parameterized commands
    out.append("## Parameterized commands")
    out.append("")
    out.append("These seven commands accept positional arguments. Run them as:")
    out.append("")
    out.append("```text")
    out.append("/tradecraft:<skill-name> [arg1] [arg2] ...")
    out.append("```")
    out.append("")
    out.append("All other skills in this plugin load as knowledge context — just invoke by name (no arguments).")
    out.append("")
    for key in PARAM_ORDER:
        out.append(DETAILED_SECTIONS[key])
    out.append("---")
    out.append("")

    # Per-domain tables
    out.append("## All skills by domain")
    out.append("")
    out.append("The knowledge skills below take no arguments — invoke by name and they load as context for Claude. Descriptions come directly from each skill's YAML frontmatter.")
    out.append("")
    for cat in CAT_ORDER:
        names = by_cat.get(cat)
        if not names:
            continue
        label = CAT_LABEL[cat]
        out.append(f"### {label}")
        out.append("")
        out.append(f"{len(names)} skill(s)")
        out.append("")
        out.append("| Command | Description |")
        out.append("|---|---|")
        for name in sorted(names):
            desc = skills[name]["desc"]
            if len(desc) > 500:
                desc = desc[:497] + "..."
            desc_s = desc.replace("|", "\\|")
            out.append(f"| `/tradecraft:{name}` | {desc_s or '_(no description)_'} |")
        out.append("")

    if issues:
        out.append("## Notes")
        out.append("")
        out.append(
            f"{len(issues)} skill file(s) have incomplete or malformed YAML frontmatter. "
            "They currently show under *Uncategorized* above; their descriptions may be blank "
            "until the frontmatter is fixed."
        )
        out.append("")

    return "\n".join(out)


def main():
    skills, by_cat, issues = scan_skills()
    md = build_md(skills, by_cat, issues)
    with open("COMMANDS.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(md)
    total = sum(len(v) for v in by_cat.values())
    print(f"wrote COMMANDS.md  total={total}  categories={len([c for c in by_cat if by_cat[c]])}  issues={len(issues)}")


if __name__ == "__main__":
    main()
