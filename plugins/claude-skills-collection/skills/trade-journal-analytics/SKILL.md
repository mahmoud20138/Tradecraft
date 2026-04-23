---
name: trade-journal-analytics
description: "Complete trade journalling system: trade logging, performance analytics, streak analysis, drawdown tracking, tag drill-down, and report generation. USE FOR: trade journal, log trade, performance report, win rate, expectancy, R-multiple, drawdown, equity curve, streak, P&L, SQN, profit factor, trade analytics, journal, session breakdown."
related_skills:
  - risk-and-portfolio
  - risk-and-portfolio
  - backtesting-sim
tags:
  - trading
  - infrastructure
  - journal
  - analytics
  - performance
  - review
skill_level: beginner
kind: reference
category: trading/psychology
status: active
---
> **Skill:** Trade Journal Analytics  |  **Domain:** trading  |  **Category:** infrastructure  |  **Level:** beginner
> **Tags:** `trading`, `infrastructure`, `journal`, `analytics`, `performance`, `review`


---

## Trade Journal & Analytics Skill

### Overview
A full-featured trade journalling and performance analysis system. Handles every step from
logging individual trades to generating publication-quality HTML/Markdown reports.
Built on pandas for fast aggregation and uses no external report dependencies.

### Python Module
`xtrading/skills/trade_journal.py`

### Stack
- **pandas** — DataFrame aggregation, groupby, pivot tables
- **numpy** — Equity curve, cumulative P&L, drawdown series
- **dataclasses** — Typed immutable `TradeRecord` structure
- **json / pathlib** — JSON persistence and cross-platform file paths
- **statistics** — Pure-Python mean/stdev for small samples

---

## 1. TradeRecord — Single Trade Data Structure

```python
from datetime import datetime
from xtrading.skills.trade_journal import TradeRecord

trade = TradeRecord(
    trade_id="T001",
    symbol="EURUSD",
    direction="long",
    entry_price=1.1000,
    exit_price=1.1050,
    quantity=1.0,              # lots
    entry_time=datetime(2025, 3, 10, 9, 0),
    exit_time=datetime(2025, 3, 10, 11, 30),
    stop_loss=1.0970,
    take_profit=1.1060,
    gross_pnl=500.0,
    commission=3.5,
    swap=0.0,
    risk_amount=300.0,
    r_multiple=1.65,           # net_pnl / risk_amount
    setup_tag="OB_pullback",
    session_tag="London",
    timeframe="H1",
    market_condition="trending",
    notes="Clean OB retest, strong momentum",
)

# Auto-computed fields:
# trade.net_pnl         → 496.5  (gross - commission - swap)
# trade.outcome         → "win"  (net_pnl > 0)
# trade.duration_minutes → 150
# trade.day_of_week     → "Mon"
# trade.hour_of_day     → 9
```

### TradeRecord Fields Reference

| Field | Type | Description |
|-------|------|-------------|
| `trade_id` | `str` | Unique identifier (required) |
| `symbol` | `str` | Instrument (e.g. "EURUSD") |
| `direction` | `"long"\|"short"` | Trade direction |
| `entry_price` | `float` | Entry fill price |
| `exit_price` | `float` | Exit fill price |
| `quantity` | `float` | Lots / shares / contracts |
| `gross_pnl` | `float` | P&L before costs |
| `commission` | `float` | Total broker commission |
| `swap` | `float` | Overnight swap/rollover cost |
| `net_pnl` | `float` | Auto-computed if left 0.0 |
| `risk_amount` | `float` | Dollar risk per trade |
| `r_multiple` | `float` | `net_pnl / risk_amount` |
| `mae` | `float` | Max Adverse Excursion (price) |
| `mfe` | `float` | Max Favorable Excursion (price) |
| `setup_tag` | `str` | Setup label (e.g. "FVG_fill") |
| `session_tag` | `str` | Session (e.g. "London") |
| `outcome` | `"win"\|"loss"\|"breakeven"\|"open"` | Auto-detected from net_pnl |

---

## 2. TradeJournal — CRUD and Persistence

```python
from xtrading.skills.trade_journal import TradeJournal

# Create journal (optional JSON persistence)
journal = TradeJournal(
    journal_path="my_journal.json",
    account_name="Prop Account",
    initial_balance=50_000.0,
)

# Add trades
journal.add_trade(trade)          # returns trade_id

# Update a field
journal.update_trade("T001", notes="Updated note", r_multiple=1.70)

# Retrieve
t = journal.get_trade("T001")

# Delete
journal.delete_trade("T001")     # returns True if found

# Querying with filters
trades = journal.get_trades(
    symbol="EURUSD",
    setup_tag="OB_pullback",
    session_tag="London",
    from_date=date(2025, 1, 1),
    to_date=date(2025, 3, 31),
    direction="long",
    outcome="win",
    min_r=1.0,                    # only trades with R ≥ 1.0
)

# Convert to DataFrame for custom analysis
df = journal.to_dataframe()

# Export to CSV
journal.export_csv("journal_export.csv")

# Persistence is automatic — every add/update/delete saves to JSON
len(journal)   # → 42 trades
repr(journal)  # → "TradeJournal(account='Prop Account', trades=42)"
```

### File Persistence Format
The JSON file structure allows portable sharing between machines:
```json
{
  "account": "Prop Account",
  "initial_balance": 50000.0,
  "trades": [
    {
      "trade_id": "T001",
      "entry_time": "2025-03-10T09:00:00",
      "exit_time": "2025-03-10T11:30:00",
      ...
    }
  ]
}
```

---

## 3. PerformanceAnalytics — Trading Statistics

```python
from xtrading.skills.trade_journal import PerformanceAnalytics

analytics = PerformanceAnalytics(journal.get_trades())

# Individual metrics
wr     = analytics.win_rate()          # 0.623  (62.3%)
exp    = analytics.expectancy()        # +0.42R per trade
pf     = analytics.profit_factor()    # 2.15
sharpe = analytics.sharpe_ratio()     # 1.34 (annualised)
sortino = analytics.sortino_ratio()   # 1.89 (downside only)
sqn    = analytics.sqn()             # 2.87 (> 2 = good)
dur    = analytics.avg_trade_duration()  # 142.5 minutes

# Full report (all metrics in one call)
report = analytics.full_report()
# {
#   "n_trades": 50,   "n_wins": 31,   "n_losses": 18,
#   "win_rate": 0.62, "win_rate_pct": 62.0,
#   "expectancy_r": 0.42,
#   "profit_factor": 2.15,
#   "avg_win_r": 1.85,   "avg_loss_r": 1.12,
#   "best_trade_r": 4.20, "worst_trade_r": -2.10,
#   "total_net_pnl": 8420.0,
#   "sharpe_ratio": 1.34,  "sortino_ratio": 1.89,
#   "sqn": 2.87,
#   "max_drawdown_pct": 8.2,
#   "calmar_ratio": 5.1,
#   "avg_duration_min": 142.5,
#   "total_commission": 175.0,
# }
```

### Metric Interpretation Guide

| Metric | Poor | Acceptable | Good | Excellent |
|--------|------|------------|------|-----------|
| Win Rate | < 35% | 35–45% | 45–65% | > 65% |
| Expectancy | < 0 | 0–0.2R | 0.2–0.5R | > 0.5R |
| Profit Factor | < 1.0 | 1.0–1.5 | 1.5–2.0 | > 2.0 |
| SQN | < 1.6 | 1.6–2.0 | 2.0–3.0 | > 3.0 |
| Sharpe | < 0.5 | 0.5–1.0 | 1.0–2.0 | > 2.0 |
| Max Drawdown | > 25% | 15–25% | 8–15% | < 8% |

### Key Formulas

```
Expectancy   = WR × Avg_Win_R − (1−WR) × Avg_Loss_R
Profit Factor = Gross_Profit / Gross_Loss
SQN          = (Expectancy / StdDev_R) × √(n_trades)
Sharpe       = (Daily_PnL_mean − rf/252) / Daily_PnL_std × √252
Sortino      = (Daily_PnL_mean − rf/252) / Downside_Std × √252
Calmar       = Annualised_Return / Max_Drawdown_pct
```

---

## 4. StreakAnalyser — Win/Loss Streak Detection

```python
from xtrading.skills.trade_journal import StreakAnalyser

streaks = StreakAnalyser(journal.get_trades())

# Current active streak
current = streaks.current_streak()
# {"streak": 4, "type": "win", "message": "4-trade WIN streak"}

# Maximum streaks in history
maxima = streaks.max_streaks()
# {
#   "max_win_streak": 8,
#   "max_loss_streak": 5,
#   "current": {"streak": 4, "type": "win", "message": "..."}
# }

# Distribution of streak lengths
dist = streaks.streak_distribution()
# {
#   "win_streaks":  {1: 12, 2: 8, 3: 4, 4: 2, 8: 1},
#   "loss_streaks": {1: 10, 2: 5, 3: 2, 5: 1},
#   "avg_win_streak": 1.9,
#   "avg_loss_streak": 1.7,
# }

# Revenge trading detection (performance after losing trades)
after_loss = streaks.after_loss_performance()
# {
#   "n_after_loss": 18,
#   "avg_r_after_loss": -0.15,
#   "revenge_trading_risk": True,   # True when avg < -0.3R
#   "trades_after_loss": [-1.2, 0.8, -0.9, ...]
# }
```

**Revenge Trading Alert**: `revenge_trading_risk=True` indicates the trader is
taking on poor quality trades after losses (avg R < −0.3 in the next trade).

---

## 5. DrawdownTracker — Equity Curve & Drawdown Analysis

```python
from xtrading.skills.trade_journal import DrawdownTracker

dd = DrawdownTracker(journal.get_trades(), initial_balance=50_000.0)

# Build equity curve (pd.Series indexed by datetime)
equity = dd.equity_curve()
# 2025-01-02    50000.0
# 2025-01-03    50450.0
# ...

# Full drawdown statistics
result = dd.calculate()
# {
#   "max_drawdown": 4200.0,             # in dollars
#   "max_drawdown_pct": 8.2,            # % from peak
#   "max_drawdown_duration_days": 12,   # days to recovery
#   "current_drawdown_pct": 1.5,        # current DD from peak
#   "peak_equity": 58400.0,
#   "current_equity": 57524.0,
#   "total_return_pct": 15.05,
# }

# Monthly P&L breakdown
monthly = dd.monthly_pnl()
#           net_pnl  n_trades  avg_pnl
# 2025-01   1842.00        18   102.33
# 2025-02   2315.00        22   105.23
# 2025-03    763.00        10    76.30
```

---

## 6. TagAnalytics — Drill-Down by Any Dimension

```python
from xtrading.skills.trade_journal import TagAnalytics

tag = TagAnalytics(journal.get_trades())

# Performance by any field
by_setup = tag.by_tag("setup_tag")
#    setup_tag     n_trades  win_rate  expectancy  profit_factor  avg_r  total_pnl
# 0  OB_pullback         18     0.722       0.845           3.12   1.25    4215.0
# 1  FVG_fill            12     0.583       0.320           1.85   0.72    2100.0
# 2  BOS_entry            8     0.500       0.125           1.42   0.55     800.0

by_session = tag.by_tag("session_tag")
by_symbol  = tag.by_tag("symbol")
by_dow     = tag.by_tag("day_of_week")
by_tf      = tag.by_tag("timeframe")
by_market  = tag.by_tag("market_condition")

# Top setups with at least N trades
top_setups = tag.best_setups(min_trades=5)

# Session performance as list of dicts
sessions = tag.session_breakdown()
# [{"session_tag": "London", "n_trades": 22, "win_rate": 0.68, ...},
#  {"session_tag": "NewYork", "n_trades": 18, "win_rate": 0.61, ...}]

# Heatmap: average R by hour and day of week
heatmap = tag.time_of_day_heatmap()
#        Mon   Tue   Wed   Thu   Fri
# hour
# 7     0.82  1.20  0.45  0.91  0.33
# 8     1.42  0.98  1.15  0.72  0.88
# 9     1.85  1.32  1.60  1.45  1.10
# 10    0.65  0.72  0.80  0.55  0.42
```

### Drillable Tag Fields

| Tag Field | Purpose |
|-----------|---------|
| `setup_tag` | ICT model, pattern type |
| `session_tag` | London / NewYork / Asian |
| `symbol` | Per-instrument performance |
| `timeframe` | H1 / H4 / D1 |
| `direction` | Long vs Short bias |
| `day_of_week` | Best trading days |
| `market_condition` | Trending vs Ranging |

---

## 7. JournalReporter — Report Generation

```python
from xtrading.skills.trade_journal import JournalReporter

reporter = JournalReporter(journal)

# Console text summary
print(reporter.text_summary())
# ============================================================
#   TRADING PERFORMANCE REPORT — Prop Account
# ============================================================
#   Trades     : 50 total  (31W / 18L)
#   Win Rate   : 62.0%
#   Expectancy : +0.42R per trade
#   Profit Fac : 2.15
#   Total P&L  : $8,420.00
#   Avg Win    : +1.85R  |  Avg Loss: 1.12R
#   Best Trade : +4.20R  |  Worst: -2.10R
#   SQN        : 2.87
#   Sharpe     : 1.34
#   Max DD     : 8.2%
#   Current DD : 1.5%
#   Max W Str  : 8 | Max L Str: 5
#   Current    : 4-trade WIN streak
# ============================================================

# Markdown report (for Obsidian, Notion, GitHub)
md = reporter.markdown_report()
# Includes: Summary stats table + Performance by Setup table

# Self-contained HTML report (dark theme, no dependencies)
html = reporter.html_report()
with open("report.html", "w") as f:
    f.write(html)

# Report on a subset of trades
london_trades = journal.get_trades(session_tag="London")
print(reporter.text_summary(london_trades))
```

---

## Full Workflow Example

```python
from datetime import datetime, date
from xtrading.skills.trade_journal import (
    TradeRecord, TradeJournal, PerformanceAnalytics,
    StreakAnalyser, DrawdownTracker, TagAnalytics, JournalReporter,
)

# 1. Create / load journal
journal = TradeJournal("journal.json", "My Prop Account", 100_000)

# 2. Log trades
for trade_data in my_trade_source:
    journal.add_trade(TradeRecord(**trade_data))

# 3. Analyse all trades
analytics = PerformanceAnalytics(journal.get_trades())
report = analytics.full_report()

# 4. Check for patterns
streaks = StreakAnalyser(journal.get_trades())
if streaks.after_loss_performance().get("revenge_trading_risk"):
    print("⚠️ Revenge trading detected — consider a break rule")

# 5. Drawdown check
dd = DrawdownTracker(journal.get_trades(), journal.initial_balance).calculate()
if dd["current_drawdown_pct"] > 10:
    print(f"⛔ Max daily loss approaching: {dd['current_drawdown_pct']:.1f}% DD")

# 6. Find your best setups
tag = TagAnalytics(journal.get_trades())
print(tag.best_setups(min_trades=5).to_string())

# 7. Generate reports
reporter = JournalReporter(journal)
print(reporter.text_summary())
html = reporter.html_report()
```

---

## Usage Conventions

1. **R-multiples** — always set `risk_amount` for meaningful `r_multiple` values
2. **outcome** — auto-detected from `net_pnl`; explicitly set `"open"` for live trades
3. **session_tag** — use consistent labels: `"London"`, `"NewYork"`, `"Asian"`, `"Overlap"`
4. **Sharpe/Sortino** — require ≥ 5 closed trades; meaningful only at ≥ 20
5. **SQN benchmark** — > 2.0 good, > 3.0 excellent, > 5.0 exceptional (Van Tharp)
6. **Persistence** — auto-saves on every CRUD operation when `journal_path` is set
7. **Filtering** — combine `get_trades()` filters then pass subset to any analyser class

---

## Related Skills

- [Risk Performance](../risk-and-portfolio.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
- [Backtesting Sim](../backtesting-sim.md)
