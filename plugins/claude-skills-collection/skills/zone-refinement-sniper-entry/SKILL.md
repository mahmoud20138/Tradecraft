---
name: zone-refinement-sniper-entry
description: >
  Supply & Demand zone refinement strategy for sniper entries — drop timeframes to find
  smaller zones inside larger zones, dramatically amplifying R:R (1.9R to 6.25R on same trade).
  Covers extreme zone selection, standard confirmation for non-extreme zones, the two-steps-down
  rule to avoid over-refinement, and multi-timeframe zone mapping. Source: JeaFx (802K views).
  Use this skill for "sniper entry", "zone refinement", "refine zone", "supply demand entry",
  "tight stop loss", "maximize risk reward", "amplify R:R", "extreme zone", "buy limit zone",
  "sell limit zone", "supply demand refinement", "lower timeframe entry", "MTF zone",
  "drop timeframe for entry", "precise entry", "pinpoint entry", "perfect entry",
  "zone inside zone", "nested zone", "refined supply demand".
  Works with poc-bounce-strategy, price-action, mtf-confluence-scorer,
  ict-smart-money, session-breakout-strategies.
related_skills:
  - poc-bounce-strategy
  - price-action
  - mtf-confluence-scorer
  - ict-smart-money
  - market-structure-bos-choch
tags:
  - supply-demand
  - sniper-entry
  - zone-refinement
  - risk-reward
  - multi-timeframe
  - price-action
category: trading/strategies
priority: 9
skill_level: intermediate
kind: reference
status: active
---

# Zone Refinement — Sniper Entry Strategy

> **Source:** JeaFx — "The PERFECT ENTRY Strategy That Will 10x Your Results" (802K+ views).
> Supply & demand zone refinement to dramatically amplify R:R on the same trade.

## Core Concept

Take the same trade setup but get a **massively better entry** by refining your zone
to a lower timeframe. Same direction, same target — but tighter stop loss and bigger R:R.

```
WITHOUT REFINEMENT:              WITH REFINEMENT:

4H Zone Entry ────┐              1H Refined Entry ──┐
                  │ 1.9R                             │ 6.25R
     Target ──────┘              Target ─────────────┘

Same trade. 3x better R:R.
```

---

## Supply & Demand Basics (Quick Review)

### Demand Zone (Buy Zone)
- Area of **consolidation before a strong upward move**
- The **last candle before the impulse** away
- Shows where **institutional buying** previously occurred
- Seen as a **discount price** — future buying expected on retest

```
         ┌──── Impulse up
    ─────┤
    █████│ ← Last candle before impulse = DEMAND ZONE
    ─────┘
```

### Supply Zone (Sell Zone)
- Area of **consolidation before a strong downward move**
- The **last candle before the impulse** down
- Shows where **institutional selling** previously occurred
- Seen as a **premium price** — future selling expected on retest

```
    ─────┐
    █████│ ← Last candle before impulse = SUPPLY ZONE
    ─────┤
         └──── Impulse down
```

**Rule:** Use the **last candle before the impulse** to mark zones.
Look for sideways candles with wicks either side, little movement, just before a large push.

---

## Zone Refinement Strategy

### Step 1: Identify Zone on Higher Timeframe

Start on your analysis timeframe (e.g., 4H) and mark the supply/demand zone.

**Example (4H supply zone):**
- Entry at zone = 1.9R trade
- Acceptable, but not a sniper entry

### Step 2: Drop to Lower Timeframe

Go inside the higher timeframe zone by dropping down one level:

| Analysis TF | Refinement TF 1 | Refinement TF 2 (max) |
|------------|----------------|----------------------|
| Daily | 4H | 1H |
| 4H | 1H | 30M |
| 1H | 30M | 15M |
| 30M | 15M | 5M |

### Step 3: Find Smaller Zones Inside

On the lower timeframe, you'll see more candles. Identify smaller supply/demand zones
**inside** the larger zone.

```
4H ZONE (large):
┌──────────────────────────┐
│                          │
│  1H zones inside:        │
│  ┌────┐                  │
│  │ Z1 │ (top zone)       │
│  └────┘                  │
│           ┌────┐         │
│           │ Z2 │ (extreme│
│           └────┘  zone)  │
└──────────────────────────┘
```

### Step 4: Select the Extreme Zone

The **extreme zone** = the furthest zone from current price in the leg of price movement.

- For **buying**: the LOWEST zone in the bullish leg
- For **selling**: the HIGHEST zone in the bearish leg

**Why the extreme zone?**
1. **Best R:R** — tightest entry = most profit potential
2. **Safest** — if you place at a non-extreme zone, you can be RIGHT about direction but still get stopped out when price reaches for the extreme

### Step 5: Place Your Order

- **Extreme zone** → Place **limit order** directly (buy limit / sell limit)
- **Non-extreme zones** → Use **standard confirmation** (see below)

---

## R:R Amplification Example (Real Trade)

**Setup:** NZDJPY 4H — trend shift (BOS), looking for pullback buy

| Method | Entry | R:R | Return per 1% Risk |
|--------|-------|-----|---------------------|
| 4H zone (no refinement) | Top of 4H demand | 3.08R | 3.08% |
| 1H extreme zone (refined) | Bottom 1H demand | 5.58R | 5.58% |
| 30M zone (two-step refined) | 30M demand inside 1H | 6.0R | 6.0% |

**Same trade, same target, same direction** — but refinement doubled the profit.

---

## Handling Multiple Zones (Zone Selection)

When you drop timeframes, you often find **multiple zones** inside the larger zone.

### Decision Framework

```
Multiple zones found inside larger zone:

Zone 1 (top, closer to price):
  → Use STANDARD CONFIRMATION before entering
  → Wait for structure shift on LTF agreeing with HTF direction

Zone 2 (bottom, extreme):
  → Place LIMIT ORDER directly
  → Best R:R + safest position
```

### Standard Confirmation (for Non-Extreme Zones)

When price reaches a non-extreme zone, confirm before entering:

1. Watch for price to enter the zone
2. Look for **lower timeframe structure shift** in your trade direction
3. Specifically: a **break of structure** (BOS) — new higher high in a buy scenario

```
LTF Structure Before:     LTF Structure After Confirmation:

  LH                         HH ← NEW HIGH (confirms zone strength)
   \                        /
    LL                     HL ← HIGHER LOW
     \                    /
      LH               LL
       \              /
        LL          LH
                   /
                 LL

BEARISH structure → Shift to BULLISH = CONFIRMED
```

**What this shows:** The demand zone is seeing an influx of buying strong enough
to reshape the trend. Now safe to place buy limit on the next pullback.

---

## The Two-Steps-Down Rule (Avoid Over-Refinement)

### The Problem

Going too deep (e.g., 4H → 5M) finds tiny zones at the absolute extreme that
**rarely get hit**. On paper it looks amazing (25R), but the trade is missed most of the time.

### The Rule

> **Maximum two steps down from your analysis timeframe.**

| Analysis TF | Step 1 (good) | Step 2 (max) | Too Far |
|------------|---------------|-------------|---------|
| Daily | 4H | 1H | 30M, 15M, 5M |
| 4H | 1H | 30M | 15M, 5M, 1M |
| 1H | 30M | 15M | 5M, 1M |
| 30M | 15M | 5M | 1M |

### Reality Check

- **One step down** is usually enough to secure a sniper entry
- Going from 3R to 5.5R by dropping one TF = excellent
- Going from 5.5R to 25R by dropping three more TFs = trade gets missed
- Don't get greedy — 5-6R is a healthy, profitable trade

---

## Complete Workflow

```
1. IDENTIFY SETUP (HTF)
   └── Mark supply/demand zone on analysis TF (e.g., 4H)
   └── Confirm trend direction (BOS, market structure)
   └── Set target (recent swing high/low)

2. REFINE ZONE (drop 1-2 TFs)
   └── Go to 1H (or next lower TF)
   └── Find smaller zones INSIDE the HTF zone
   └── Identify the EXTREME zone (furthest from price)

3. CHOOSE ENTRY METHOD
   └── Extreme zone → LIMIT ORDER (direct placement)
   └── Non-extreme zone → STANDARD CONFIRMATION (wait for LTF BOS)

4. SET POSITION
   └── Entry: top of refined zone (for buys) / bottom (for sells)
   └── Stop: below entire move low (for buys) / above move high (for sells)
   └── Target: HTF swing point (same as original trade)

5. EXECUTE
   └── Place limit order at extreme zone
   └── Monitor non-extreme zones for confirmation entries
   └── Let it play out — don't move stops
```

---

## Quick Reference Card

```
ZONE REFINEMENT CHECKLIST:
[] HTF zone marked (last candle before impulse)
[] Trend direction confirmed (BOS on HTF)
[] Dropped 1-2 timeframes (not more!)
[] Found refined zones inside HTF zone
[] Identified EXTREME zone (furthest from price)
[] Entry type selected:
    - Extreme → limit order
    - Non-extreme → standard confirmation
[] Stop below/above the move extreme
[] Target at HTF swing point
[] R:R calculated (should be significantly better than HTF zone entry)

OVER-REFINEMENT WARNING:
  4H → 1H → 30M = OK (two steps)
  4H → 5M = TOO FAR (trade will be missed)

R:R AMPLIFICATION GUIDE:
  No refinement:   ~2-3R typical
  One step down:   ~4-6R typical
  Two steps down:  ~5-8R typical
  Over-refined:    ~15-25R on paper, rarely hit
```

---

## Integration with Super Skills

| Super Skill | How It Integrates |
|-------------|------------------|
| `market-structure-intelligence` | Confirm BOS/CHoCH for trade direction before refining |
| `liquidity-analysis` | Check for liquidity below extreme zone (stop hunts) |
| `price-action-engine` | Validate candle patterns at refined zone |
| `multi-timeframe-signal-engine` | Score confluence across HTF and refined TF |
| `risk-and-portfolio` | Calculate lot size based on refined stop distance |
| `ict-smart-money` | Combine with OBs, FVGs for additional confluence |


---
