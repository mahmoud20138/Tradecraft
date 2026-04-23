---
name: fundamental-analysis
description: Complete fundamental analysis knowledge base for evaluating stocks, companies, and markets. Covers financial statement analysis (income statement, balance sheet, cash flow), valuation ratios (P/E, P/B, EV/EBITDA, PEG), valuation methods (DCF, comps, DDM), profitability/liquidity/leverage/efficiency ratios, macroeconomic analysis, central bank policy, intermarket relationships, industry analysis (Porter's Five Forces), and economic moats. Trigger when analyzing company fundamentals, financial ratios, stock valuation, earnings reports, economic indicators, or business quality. USE FOR: P/E ratio, P/B ratio, EV/EBITDA, PEG ratio, DCF analysis, discounted cash flow, comparable company analysis, dividend discount model, income statement analysis, balance sheet analysis, cash flow analysis, free cash flow, ROE, ROA, ROIC, DuPont analysis, gross margin, operating margin, net margin, current ratio, quick ratio, debt-to-equity, interest coverage, asset turnover, inventory turnover, cash conversion cycle, WACC calculation, terminal value, economic indicators, GDP, CPI, PMI, yield curve, Fed policy, intermarket analysis, Porter's Five Forces, economic moats, sector analysis, earnings analysis, financial statement red flags. DO NOT USE FOR: technical chart analysis (use technical-analysis), specific trading strategies (use trading-strategies-playbook), options analysis (use options-trading).
related_skills:
  - market-intelligence
  - equities-trading
  - cross-asset-relationships
tags:
  - trading
  - research
  - fundamental
  - financials
  - valuation
  - moat
skill_level: intermediate
kind: reference
category: trading/analysis
status: active
---
> **Skill:** Fundamental Analysis  |  **Domain:** trading  |  **Category:** research  |  **Level:** intermediate
> **Tags:** `trading`, `research`, `fundamental`, `financials`, `valuation`, `moat`


# Fundamental Analysis

## Reference Files

Load these when needed — do not pre-load all of them:

| File | Load When |
|------|-----------|
| [references/financial-statements.md](references/financial-statements.md) | Analyzing income statement, balance sheet, cash flow, FCF, working capital, red flags |
| [references/valuation-methods.md](references/valuation-methods.md) | Computing or comparing valuation ratios, running DCF, comps, DDM, profitability/liquidity/leverage/efficiency ratios |
| [references/macro-industry.md](references/macro-industry.md) | Economic indicators, central bank policy, intermarket analysis, Porter's Five Forces, economic moats |

---

## Quick Ratio Reference

### Valuation Ratios

| Ratio | Undervalued | Fair | Expensive | Notes |
|-------|-------------|------|-----------|-------|
| P/E (trailing) | < 10 | 10–20 | > 30 | Compare to sector & growth rate |
| P/E (forward) | < 12 | 12–18 | > 25 | More predictive than trailing |
| PEG | < 1.0 | ~1.0 | > 1.5 | P/E ÷ EPS growth rate |
| P/S | < 1.0 | 1–3 | > 5 | Sector-dependent; SaaS can be 8–20× |
| P/B | < 1.0 | 1–3 | > 5 | Banks/financials: fair at 1–2× |
| EV/EBITDA | < 8 | 8–12 | > 15 | Best for capital-intensive businesses |
| EV/Revenue | < 1 | 1–3 | > 5 | Pre-profit companies |

### Profitability Ratios

| Ratio | Poor | Good | Excellent | Notes |
|-------|------|------|-----------|-------|
| ROE | < 10% | 15–20% | > 20% | Beware high leverage inflating ROE |
| ROA | < 2% | 5–8% | > 10% | Banks: 1–2% is normal |
| ROIC | < WACC | WACC+5% | > 15% | Value creation only if ROIC > WACC |
| Gross Margin | Sector low | 40%+ (tech) | 60%+ | Highly sector-specific |
| Operating Margin | < 5% | 10–20% | > 25% | Sector-adjusted |
| Net Margin | < 3% | 8–15% | > 20% | Sector-adjusted |

### Liquidity & Leverage Ratios

| Ratio | Weak | Acceptable | Strong | Notes |
|-------|------|------------|--------|-------|
| Current Ratio | < 1.0 | 1.5–2.0 | > 2.5 | < 1 = liquidity risk |
| Quick Ratio | < 0.7 | 1.0–1.5 | > 2.0 | Excludes inventory |
| Cash Ratio | < 0.3 | 0.5–1.0 | > 1.0 | Most conservative |
| Debt/Equity | > 2.0 | 0.5–1.5 | < 0.5 | Sector-adjusted |
| Debt/EBITDA | > 4× | 2–3× | < 2× | > 5× = distress risk |
| Interest Coverage | < 2× | 3–5× | > 5× | < 1.5× = danger zone |

### Efficiency Ratios

| Ratio | Poor | Good | Excellent |
|-------|------|------|-----------|
| Asset Turnover | < 0.5 | 0.8–1.5 | > 1.5 |
| Inventory Turnover | < 4 | 6–12 | > 15 |
| DSO (Days Sales Outstanding) | > 60 | 30–45 | < 30 |
| CCC (Cash Conversion Cycle) | > 90 days | 30–60 | < 30 (or negative) |

---

## Financial Statement Structure Overview

```
Income Statement       →  Profitability (what was earned)
Balance Sheet          →  Financial position (what is owned/owed)
Cash Flow Statement    →  Liquidity (actual cash movement)

Key linkages:
  Net Income (IS) → Retained Earnings (BS) → Operating CF (CFS)
  CapEx (CFS)     → PP&E change (BS)
  D&A  (IS)       → Added back in Operating CF (CFS)
  FCF = CFO - CapEx  (the purest measure of cash generation)
```

---

## Valuation Method Selection Guide

| Situation | Best Method | Why |
|-----------|-------------|-----|
| Stable, predictable FCF | DCF | Intrinsic value based on fundamentals |
| Profitable, comparable peers exist | Comps (EV/EBITDA, P/E) | Market-derived, fast |
| Dividend-paying, mature company | DDM (Gordon Growth) | Dividend stream = value |
| Pre-profit high-growth | EV/Revenue, EV/ARR | No earnings yet |
| Asset-heavy (banks, real estate) | P/B, P/TBV, P/FFO | Assets = value driver |
| Acquisition / M&A context | EV/EBITDA + DCF | Enterprise-level view |
| Cyclical industry | EV/EBITDA on normalized earnings | Avoid peak/trough distortions |

> **Rule**: Always triangulate — use 2–3 methods and compare implied price ranges.

---

## Red Flags Checklist

### Earnings Quality
- [] Revenue growing faster than cash from operations
- [] Accounts receivable growing faster than revenue (channel stuffing)
- [] Gross margin declining while revenue rises
- [] Frequent non-recurring "one-time" charges
- [] Auditor changes or going-concern opinion
- [] Earnings beat only due to tax rate or share count changes

### Balance Sheet
- [] Goodwill > 30% of total assets (acquisition risk)
- [] Inventory buildup without revenue growth
- [] Rising short-term debt to fund operations
- [] Pension obligations understated (check footnotes)

### Cash Flow
- [] Persistent CFO < Net Income (low earnings quality)
- [] FCF negative for 3+ years without clear growth investment story
- [] Heavy reliance on asset sales in investing CF
- [] Dividends paid from debt, not earnings

---

## Analytical Workflow

1. **Screen** → Use ratio table above to flag outliers
2. **Understand the business** → Revenue model, customers, competitive position
3. **Read financial statements** → See `references/financial-statements.md`
4. **Compute ratios** → See `references/valuation-methods.md`
5. **Value the company** → DCF + comps + sector-specific multiples
6. **Assess macro/industry** → See `references/macro-industry.md`
7. **Form a view** → Bull/base/bear scenario with margin of safety

---

## Related Skills

- [Market Intelligence](../market-intelligence.md)
- [Equities Trading](../equities-trading.md)
- [Cross Asset Relationships](../cross-asset-relationships.md)



---
