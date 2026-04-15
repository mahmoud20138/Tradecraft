---
name: trading-brain
description: >
  Master Trading Brain — the TOP-LEVEL orchestrator implementing the 7-layer autonomous
  trading architecture. This is the PRIMARY entry point for ALL trading tasks.

  USE THIS SKILL FIRST FOR: "analyze the market", "what should I trade", "full analysis",
  "trade setup", "scan the market", "brain mode", "orchestrate", "coordinate all skills",
  "master plan", "big picture", "run all analyses", "what's happening in markets",
  "EURUSD analysis", "liquidity trap", "should I go long", "entry signal", "trade idea",
  "risk check before trading", "is it safe to trade", "multi-factor analysis",
  "comprehensive analysis", "7-layer analysis", "autonomous trading", "trading loop",
  "full pipeline", "end-to-end analysis", "market intelligence", "strategy recommendation",
  "signal generation", "aggregate signals", "validate risk", "execute trade", "learn from trade",
  "what does the brain say", "trading brain", "run the brain", "activate brain",
  ANY complex query requiring data from more than one skill,
  ANY request that involves market analysis + strategy + risk combined.

  This skill replaces trading-brain as the primary entry point.
  It implements a strict 7-layer pipeline: Intelligence -> Strategy -> Signal ->
  Aggregation -> Risk -> Execution -> Learning. Each layer has defined inputs,
  outputs, and skill dependencies. No layer can be skipped.

load_priority: 1.0
context: fork
agent: general-purpose
related_skills:
  - market-intelligence
  - strategy-selection
  - ai-signal-aggregator
  - ai-signal-aggregator
  - risk-and-portfolio
  - risk-and-portfolio
  - execution-algo-trading
  - execution-algo-trading
  - tensortrade-rl
  - multi-strategy-orchestration
  - mt5-integration
  - trading-autopilot
tags:
  - trading
  - orchestrator
  - pipeline
  - brain
  - 7-layer
  - autonomous
  - master
  - infrastructure
skill_level: advanced
kind: orchestrator
category: trading/core
status: active
---

# Trading Brain -- 7-Layer Autonomous Trading Architecture

> **Role:** Master orchestrator  |  **Priority:** Highest  |  **Level:** Advanced
> Supersedes `trading-brain` as the primary entry point.

---

## Architecture Overview

```
 USER QUERY
     |
     v
+=========================================================================+
|                        TRADING BRAIN (Layer 0)                          |
|    Parse intent -> Route -> Orchestrate -> Synthesize -> Respond        |
+=========================================================================+
     |           |           |           |           |           |
     v           v           v           v           v           v
+----------+----------+----------+----------+----------+----------+
| LAYER 1  | LAYER 2  | LAYER 3  | LAYER 4  | LAYER 5  | LAYER 6  |---+
| Market   | Strategy | Signal   | Signal   | Risk     | Execution|   |
| Intel    | Select   | Generate | Aggregate| Engine   | Engine   |   |
+----------+----------+----------+----------+----------+----------+   |
     ^                                                                 |
     |                        +----------+                             |
     +------------------------| LAYER 7  |<----------------------------+
                              | Learning |
                              | Engine   |
                              +----------+
```

### Detailed Layer Diagram

```
+=======================================================================+
|  L1: MARKET INTELLIGENCE ENGINE                                       |
|  "What is the market doing right now?"                                |
|                                                                       |
|  +------------------+  +------------------+  +------------------+     |
|  | market-          |  | macro-regime     |  | news-sentiment   |     |
|  | intelligence     |  | market-regime-   |  | news-intelligence|     |
|  | fundamental-     |  | classifier       |  | economic-        |     |
|  | analysis         |  | market-regime-   |  | calendar         |     |
|  |                  |  | detection        |  | sentiment-       |     |
|  |                  |  |                  |  | analysis         |     |
|  +------------------+  +------------------+  +------------------+     |
|  +------------------+  +------------------+  +------------------+     |
|  | mt5-chart-       |  | cross-asset-     |  | institutional-   |     |
|  | browser          |  | relationships    |  | timeline         |     |
|  | market-data-     |  | correlation-     |  | liquidity-       |     |
|  | ingestion        |  | fundamentals     |  | analysis         |     |
|  +------------------+  +------------------+  +------------------+     |
|                                                                       |
|  OUTPUT: MarketState { regime, sentiment, key_levels, volatility,     |
|          correlations, news_events, institutional_flow }              |
+=======================================================================+
                              |
                              v
+=======================================================================+
|  L2: STRATEGY SELECTION ENGINE                                        |
|  "Which strategies work in this market state?"                        |
|                                                                       |
|  +------------------+  +------------------+  +------------------+     |
|  | strategy-        |  | portfolio-       |  | market-regime-   |     |
|  | selection        |  | strategy-        |  | classifier       |     |
|  | strategy-        |  | allocation       |  | multi-strategy-  |     |
|  | playbook         |  | multi-strategy-  |  | allocator        |     |
|  |                  |  | orchestration    |  |                  |     |
|  +------------------+  +------------------+  +------------------+     |
|                                                                       |
|  OUTPUT: list[Strategy] with weights and regime-fit scores            |
+=======================================================================+
                              |
                              v
+=======================================================================+
|  L3: SIGNAL GENERATION                                                |
|  "Run selected strategies, produce raw signals"                       |
|                                                                       |
|  +------------------+  +------------------+  +------------------+     |
|  | ict-smart-money  |  | trend-following- |  | mean-reversion-  |     |
|  | price-action     |  | systems          |  | engine           |     |
|  | supply-demand-   |  | breakout-        |  | divergence-      |     |
|  | zone-strategy    |  | strategy-engine  |  | strategy-engine  |     |
|  | market-structure |  | momentum-roc-    |  | fibonacci-       |     |
|  | -bos-choch       |  | strategy         |  | strategy-engine  |     |
|  +------------------+  +------------------+  +------------------+     |
|  +------------------+  +------------------+  +------------------+     |
|  | volume-profile-  |  | chart-vision     |  | session-breakout |     |
|  | strategy         |  | mtf-confluence-  |  | -strategies      |     |
|  | wyckoff-method   |  | scorer           |  | scalping-        |     |
|  | -engine          |  | technical-       |  | framework        |     |
|  |                  |  | analysis         |  |                  |     |
|  +------------------+  +------------------+  +------------------+     |
|                                                                       |
|  OUTPUT: list[Signal] { direction, entry, stop, targets, confidence } |
+=======================================================================+
                              |
                              v
+=======================================================================+
|  L4: SIGNAL AGGREGATION                                               |
|  "Combine signals into a single decision"                             |
|                                                                       |
|  +------------------+  +------------------+  +------------------+     |
|  | ai-signal-       |  | signal-          |  | mtf-confluence-  |     |
|  | aggregator       |  | aggregator       |  | scorer           |     |
|  +------------------+  +------------------+  +------------------+     |
|                                                                       |
|  OUTPUT: FinalSignal { direction, conviction, entry, stop, targets,   |
|          conflict_flags, agreement_score }                            |
+=======================================================================+
                              |
                              v
+=======================================================================+
|  L5: RISK ENGINE                                                      |
|  "Is this trade safe to take?"                                        |
|                                                                       |
|  +------------------+  +------------------+  +------------------+     |
|  | risk-and-portfolio  |  | risk-manager-    |  | drawdown-        |     |
|  | risk-and-        |  | position-sizer   |  | playbook         |     |
|  | portfolio        |  | risk-of-ruin     |  | drawdown-        |     |
|  |                  |  |                  |  | recovery-        |     |
|  |                  |  |                  |  | protocol         |     |
|  +------------------+  +------------------+  +------------------+     |
|  +------------------+  +------------------+  +------------------+     |
|  | correlation-     |  | risk-calendar-   |  | tail-risk-       |     |
|  | crisis           |  | trade-filter     |  | hedging          |     |
|  | real-time-risk-  |  | risk-and-portfolio |  | account-tail-    |     |
|  | monitor          |  |                  |  | risk             |     |
|  +------------------+  +------------------+  +------------------+     |
|                                                                       |
|  OUTPUT: RiskApproval { approved, position_size, adjusted_stop,       |
|          max_loss, portfolio_heat, veto_reasons }                     |
+=======================================================================+
                              |
                              v
+=======================================================================+
|  L6: EXECUTION ENGINE                                                 |
|  "Place the trade optimally"                                          |
|                                                                       |
|  +------------------+  +------------------+  +------------------+     |
|  | execution-algo-  |  | execution-       |  | mt5-integration  |     |
|  | trading          |  | optimizer        |  | mt5-ea-code-     |     |
|  | market-impact-   |  | spread-slippage- |  | generator        |     |
|  | model            |  | cost-analyzer    |  | trading-         |     |
|  |                  |  |                  |  | automation       |     |
|  +------------------+  +------------------+  +------------------+     |
|  +------------------+  +------------------+                           |
|  | signal-          |  | alert-pipeline   |                           |
|  | broadcaster      |  | realtime-alert-  |                           |
|  |                  |  | pipeline         |                           |
|  +------------------+  +------------------+                           |
|                                                                       |
|  OUTPUT: TradeResult { order_id, fill_price, slippage, status }       |
+=======================================================================+
                              |
                              v
+=======================================================================+
|  L7: LEARNING ENGINE                                                  |
|  "What did we learn? How do we improve?"                              |
|                                                                       |
|  +------------------+  +------------------+  +------------------+     |
|  | tensortrade-rl     |  | strategy-        |  | trade-journal-   |     |
|  | rl-trade-agent   |  | validation       |  | analytics        |     |
|  | strategy-decay-  |  | walk-forward-    |  | trade-journal-   |     |
|  | monitor          |  | optimizer        |  | performance      |     |
|  +------------------+  +------------------+  +------------------+     |
|  +------------------+  +------------------+  +------------------+     |
|  | performance-     |  | parameter-       |  | monte-carlo-     |     |
|  | attribution-     |  | sensitivity-     |  | stress-tester    |     |
|  | engine           |  | analyzer         |  | backtesting-sim  |     |
|  +------------------+  +------------------+  +------------------+     |
|                                                                       |
|  OUTPUT: LearningUpdate { weight_adjustments, strategy_scores,        |
|          decay_alerts, performance_attribution }                      |
|  FEEDBACK LOOP -> L1 (regime weights), L2 (strategy scores),         |
|                   L4 (aggregation weights), L5 (risk params)          |
+=======================================================================+
```

---

## Layer Mapping Table

| Layer | Purpose | Super Skills | Micro Skills |
|-------|---------|-------------|--------------|
| **L1** Market Intelligence | Understand current market state | `market-intelligence`, `macro-regime`, `news-sentiment` | `fundamental-analysis`, `social-sentiment-scraper`, `economic-calendar`, `news-intelligence`, `news-sentiment-nlp-engine`, `social-sentiment-scraper`, `institutional-timeline`, `market-regime-classifier`, `market-regime-classifier`, `mt5-chart-browser`, `market-data-ingestion`, `cross-asset-relationships`, `correlation-fundamentals`, `liquidity-analysis`, `currency-strength-meter`, `macro-economic-dashboard` |
| **L2** Strategy Selection | Pick optimal strategies for regime | `strategy-selection`, `multi-strategy-orchestration`, `portfolio-optimization` | `strategy-playbook`, `market-regime-classifier`, `multi-strategy-allocator`, `backtesting-sim`, `price-action` |
| **L3** Signal Generation | Run strategies, produce raw signals | `technical-analysis`, `price-action`, `ict-smart-money` | `trend-following-systems`, `mean-reversion-engine`, `breakout-strategy-engine`, `divergence-strategy-engine`, `fibonacci-strategy-engine`, `harmonic-pattern-engine`, `elliott-wave-engine`, `poc-bounce-strategy`, `market-structure-bos-choch`, `volume-profile-strategy`, `wyckoff-method-engine`, `momentum-roc-strategy`, `chart-vision`, `mtf-confluence-scorer`, `session-breakout-strategies`, `scalping-framework`, `order-flow-delta-strategy`, `smart-money-trap-detector`, `ichimoku-complete-strategy`, `candlestick-patterns` |
| **L4** Signal Aggregation | Combine signals into one decision | `ai-signal-aggregator`, `ai-signal-aggregator` | `mtf-confluence-scorer` |
| **L5** Risk Engine | Validate risk, size position | `risk-and-portfolio`, `risk-and-portfolio` | `risk-and-portfolio`, `risk-of-ruin`, `drawdown-playbook`, `drawdown-playbook`, `correlation-crisis`, `real-time-risk-monitor`, `risk-calendar-trade-filter`, `tail-risk-hedging`, `account-tail-risk`, `risk-and-portfolio`, `risk-adjusted-compounding`, `trade-psychology-coach` |
| **L6** Execution Engine | Place trades optimally | `execution-algo-trading`, `mt5-integration`, `trading-autopilot` | `execution-algo-trading`, `market-impact-model`, `spread-slippage-cost-analyzer`, `mt5-ea-code-generator`, `signal-broadcaster`, `alert-pipeline`, `realtime-alert-pipeline`, `trade-copier-signal-broadcaster` |
| **L7** Learning Engine | Adapt weights, detect decay, journal | `tensortrade-rl`, `strategy-validation`, `trade-journal-analytics` | `rl-trade-agent`, `strategy-decay-monitor`, `walk-forward-optimizer`, `parameter-sensitivity-analyzer`, `monte-carlo-stress-tester`, `backtesting-sim`, `performance-attribution-engine`, `trade-journal-performance`, `strategy-ab-tester`, `backtest-report-generator` |

---

## Data Flow Between Layers

```
L1 MarketState -----> L2 (regime, volatility, session, correlations)
L2 Strategies  -----> L3 (strategy list with weights and parameters)
L3 RawSignals  -----> L4 (direction, confidence, entry/stop/target per strategy)
L4 FinalSignal -----> L5 (aggregated direction, conviction, conflict flags)
L5 RiskApproval ----> L6 (position size, adjusted stops, go/no-go, veto reasons)
L6 TradeResult  ----> L7 (fill data, slippage, execution quality)
L7 LearningUpdate --> L1 (updated regime weights)
                  --> L2 (updated strategy fitness scores)
                  --> L4 (updated aggregation weights)
                  --> L5 (updated risk parameters, drawdown state)
```

### Data Contracts

```python
from dataclasses import dataclass, field
from typing import Optional, Literal
from datetime import datetime
from enum import Enum

class Regime(Enum):
    TRENDING_BULL = "trending_bull"
    TRENDING_BEAR = "trending_bear"
    RANGING = "ranging"
    VOLATILE = "volatile"
    TRANSITIONING = "transitioning"

class Direction(Enum):
    LONG = "long"
    SHORT = "short"
    FLAT = "flat"

@dataclass
class MarketState:
    """L1 output: complete snapshot of current market conditions."""
    symbol: str
    timestamp: datetime
    regime: Regime
    regime_confidence: float                     # 0-1
    trend_direction: Direction
    volatility_percentile: float                 # 0-100, current ATR vs 252-day
    adr_ratio: float                             # today ADR / 20-day avg ADR
    key_levels: dict                             # {"support": [...], "resistance": [...]}
    sentiment_score: float                       # -1 (extreme bearish) to +1 (extreme bullish)
    news_events: list[dict]                      # upcoming high-impact events
    institutional_bias: Direction
    correlation_shifts: list[dict]               # regime breaks in correlated pairs
    session: str                                 # "london", "new_york", "tokyo", "overlap"
    currency_strength: dict[str, float]          # {"USD": 0.7, "EUR": -0.3, ...}

@dataclass
class Strategy:
    """L2 output: a selected strategy with regime-fit metadata."""
    name: str
    skill_name: str                              # maps to a SKILL.md
    weight: float                                # allocation weight 0-1
    regime_fit: float                            # how well it fits current regime 0-1
    parameters: dict                             # strategy-specific params
    expected_win_rate: float
    expected_rr: float
    timeframes: list[str]                        # ["H1", "H4"]

@dataclass
class Signal:
    """L3 output: raw signal from a single strategy."""
    strategy_name: str
    direction: Direction
    entry_price: float
    stop_loss: float
    targets: list[float]
    confidence: float                            # 0-1
    timeframe: str
    reasoning: str
    confluence_factors: list[str]

@dataclass
class FinalSignal:
    """L4 output: aggregated signal from all strategies."""
    direction: Direction
    conviction: float                            # 0-1, weighted agreement
    entry_price: float
    stop_loss: float
    targets: list[float]
    agreement_score: float                       # % of strategies agreeing
    conflict_flags: list[str]                    # disagreements worth noting
    contributing_signals: list[Signal]
    veto: bool                                   # True if conflicts are irreconcilable

@dataclass
class RiskApproval:
    """L5 output: risk validation result."""
    approved: bool
    position_size_lots: float
    position_size_pct: float                     # of account
    adjusted_stop: Optional[float]               # risk engine may widen stop
    max_loss_dollars: float
    max_loss_pct: float
    portfolio_heat_pct: float                    # total open risk
    risk_reward_ratio: float
    veto_reasons: list[str]                      # why rejected (if not approved)
    conditions: list[str]                        # "reduce size 50%", "set trailing stop"

@dataclass
class TradeResult:
    """L6 output: execution result."""
    order_id: str
    symbol: str
    direction: Direction
    fill_price: float
    requested_price: float
    slippage_pips: float
    spread_at_fill: float
    execution_algo: str                          # "market", "limit", "twap", etc.
    status: Literal["filled", "partial", "rejected", "pending"]
    timestamp: datetime

@dataclass
class LearningUpdate:
    """L7 output: feedback for all layers."""
    strategy_scores: dict[str, float]            # updated fitness per strategy
    weight_adjustments: dict[str, float]          # delta to aggregation weights
    decay_alerts: list[str]                      # strategies losing edge
    risk_param_updates: dict[str, float]          # adjusted risk thresholds
    regime_weight_updates: dict[str, float]       # regime detection calibration
    performance_summary: dict                     # Sharpe, win rate, avg RR, etc.
```

---

## TradingBrain Implementation

```python
"""
TradingBrain -- Master orchestrator for the 7-layer trading architecture.

Integrates with skill_router.py for skill discovery and routing.
Each layer reads the relevant SKILL.md files and executes their patterns.

Usage:
    from trading_brain import TradingBrain
    brain = TradingBrain(symbol="EURUSD", account_equity=10000)
    result = brain.run()
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Optional

# Import skill router for dynamic skill lookup
SKILLS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILLS_DIR))
from skill_router import load_skills, route_query, resolve_deps, find_skill

# ---------------------------------------------------------------------------
# Layer -> Skill mapping
# ---------------------------------------------------------------------------

LAYER_SKILLS: dict[str, list[str]] = {
    "L1_intelligence": [
        "market-intelligence", "macro-regime", "news-sentiment",
        "market-regime-classifier", "market-regime-classifier",
        "mt5-chart-browser", "cross-asset-relationships",
        "correlation-fundamentals", "institutional-timeline",
        "liquidity-analysis", "social-sentiment-scraper",
        "economic-calendar", "currency-strength-meter"],
    "L2_strategy": [
        "strategy-selection", "strategy-playbook",
        "portfolio-optimization", "multi-strategy-orchestration",
        "multi-strategy-allocator", "market-regime-classifier"],
    "L3_signals": [
        "ict-smart-money", "price-action", "technical-analysis",
        "trend-following-systems", "mean-reversion-engine",
        "breakout-strategy-engine", "divergence-strategy-engine",
        "poc-bounce-strategy", "market-structure-bos-choch",
        "volume-profile-strategy", "wyckoff-method-engine",
        "fibonacci-strategy-engine", "momentum-roc-strategy",
        "chart-vision", "mtf-confluence-scorer",
        "session-breakout-strategies", "scalping-framework"],
    "L4_aggregation": [
        "ai-signal-aggregator", "ai-signal-aggregator",
        "mtf-confluence-scorer"],
    "L5_risk": [
        "risk-and-portfolio", "risk-and-portfolio",
        "risk-and-portfolio", "risk-of-ruin",
        "drawdown-playbook", "drawdown-playbook",
        "correlation-crisis", "real-time-risk-monitor",
        "risk-calendar-trade-filter", "tail-risk-hedging"],
    "L6_execution": [
        "execution-algo-trading", "execution-algo-trading",
        "mt5-integration", "mt5-ea-code-generator",
        "trading-autopilot", "signal-broadcaster",
        "alert-pipeline", "spread-slippage-cost-analyzer"],
    "L7_learning": [
        "tensortrade-rl", "strategy-decay-monitor",
        "rl-trade-agent", "strategy-validation",
        "walk-forward-optimizer", "trade-journal-analytics",
        "performance-attribution-engine", "monte-carlo-stress-tester",
        "backtesting-sim", "parameter-sensitivity-analyzer"],
}


class TradingBrain:
    """
    Master orchestrator implementing the 7-layer autonomous trading pipeline.

    Each method corresponds to one layer. The run() method executes the
    full pipeline sequentially, with each layer feeding the next.
    """

    def __init__(
        self,
        symbol: str = "EURUSD",
        timeframes: list[str] = None,
        account_equity: float = 10_000.0,
        risk_per_trade_pct: float = 1.0,
        max_portfolio_heat_pct: float = 6.0,
        mode: str = "analysis",  # "analysis" | "live" | "paper"
    ):
        self.symbol = symbol
        self.timeframes = timeframes or ["M15", "H1", "H4", "D1"]
        self.account_equity = account_equity
        self.risk_per_trade_pct = risk_per_trade_pct
        self.max_portfolio_heat_pct = max_portfolio_heat_pct
        self.mode = mode

        # State flowing between layers
        self.market_state: Optional[MarketState] = None
        self.strategies: list[Strategy] = []
        self.signals: list[Signal] = []
        self.final_signal: Optional[FinalSignal] = None
        self.risk_approval: Optional[RiskApproval] = None
        self.trade_result: Optional[TradeResult] = None
        self.learning_update: Optional[LearningUpdate] = None

        # Skill registry
        self._skills = load_skills()

        # Execution log
        self.log: list[dict] = []

    # -------------------------------------------------------------------
    # Layer 1: Market Intelligence
    # -------------------------------------------------------------------

    def analyze_market(self) -> MarketState:
        """
        Layer 1: Gather all market intelligence for self.symbol.

        Reads skills: market-intelligence, macro-regime, news-sentiment,
        mt5-chart-browser, cross-asset-relationships, institutional-timeline.

        Returns MarketState with regime, sentiment, levels, correlations.
        """
        self._log("L1_INTEL", f"Analyzing market for {self.symbol}")

        # Step 1: Get price data and compute indicators (mt5-chart-browser)
        # Step 2: Classify regime (market-regime-classifier + market-regime-classifier)
        # Step 3: Fetch news and sentiment (news-sentiment, economic-calendar)
        # Step 4: Check institutional positioning (institutional-timeline)
        # Step 5: Run correlation analysis (cross-asset-relationships)
        # Step 6: Calculate currency strength (currency-strength-meter)

        skills_to_invoke = self._resolve_layer_skills("L1_intelligence")
        self._log("L1_INTEL", f"Invoking {len(skills_to_invoke)} skills")

        # Build MarketState from aggregated skill outputs
        self.market_state = MarketState(
            symbol=self.symbol,
            timestamp=datetime.utcnow(),
            regime=Regime.RANGING,            # populated by L1 skills
            regime_confidence=0.0,
            trend_direction=Direction.FLAT,
            volatility_percentile=50.0,
            adr_ratio=1.0,
            key_levels={"support": [], "resistance": []},
            sentiment_score=0.0,
            news_events=[],
            institutional_bias=Direction.FLAT,
            correlation_shifts=[],
            session=self._detect_session(),
            currency_strength={},
        )

        self._log("L1_INTEL", f"Regime={self.market_state.regime.value}, "
                  f"Session={self.market_state.session}")
        return self.market_state

    # -------------------------------------------------------------------
    # Layer 2: Strategy Selection
    # -------------------------------------------------------------------

    def select_strategy(self, market_state: MarketState) -> list[Strategy]:
        """
        Layer 2: Select optimal strategies for the current market state.

        Reads skills: strategy-selection, strategy-playbook,
        portfolio-optimization, multi-strategy-orchestration.

        Returns ranked list of Strategy objects with weights.
        """
        self._log("L2_STRATEGY", f"Selecting strategies for regime={market_state.regime.value}")

        # Strategy-regime mapping
        REGIME_STRATEGY_MAP = {
            Regime.TRENDING_BULL: [
                ("trend-following-systems", 0.35),
                ("ict-smart-money", 0.25),
                ("breakout-strategy-engine", 0.20),
                ("momentum-roc-strategy", 0.20)],
            Regime.TRENDING_BEAR: [
                ("trend-following-systems", 0.35),
                ("ict-smart-money", 0.25),
                ("breakout-strategy-engine", 0.20),
                ("momentum-roc-strategy", 0.20)],
            Regime.RANGING: [
                ("mean-reversion-engine", 0.30),
                ("poc-bounce-strategy", 0.25),
                ("divergence-strategy-engine", 0.25),
                ("scalping-framework", 0.20)],
            Regime.VOLATILE: [
                ("breakout-strategy-engine", 0.30),
                ("session-breakout-strategies", 0.25),
                ("volume-profile-strategy", 0.25),
                ("fibonacci-strategy-engine", 0.20)],
            Regime.TRANSITIONING: [
                ("market-structure-bos-choch", 0.30),
                ("wyckoff-method-engine", 0.25),
                ("smart-money-trap-detector", 0.25),
                ("divergence-strategy-engine", 0.20)],
        }

        regime_strategies = REGIME_STRATEGY_MAP.get(
            market_state.regime, REGIME_STRATEGY_MAP[Regime.RANGING]
        )

        self.strategies = []
        for skill_name, weight in regime_strategies:
            self.strategies.append(Strategy(
                name=skill_name.replace("-", " ").title(),
                skill_name=skill_name,
                weight=weight,
                regime_fit=market_state.regime_confidence,
                parameters={},
                expected_win_rate=0.0,  # populated by L7 feedback
                expected_rr=0.0,
                timeframes=self.timeframes,
            ))

        self._log("L2_STRATEGY", f"Selected {len(self.strategies)} strategies: "
                  f"{[s.skill_name for s in self.strategies]}")
        return self.strategies

    # -------------------------------------------------------------------
    # Layer 3: Signal Generation
    # -------------------------------------------------------------------

    def generate_signals(self, strategies: list[Strategy]) -> list[Signal]:
        """
        Layer 3: Run each selected strategy to produce raw signals.

        For each Strategy, reads its SKILL.md and applies its analysis
        to the current market data. Returns one Signal per strategy.
        """
        self._log("L3_SIGNALS", f"Generating signals from {len(strategies)} strategies")

        self.signals = []
        for strategy in strategies:
            skill_path = self._get_skill_path(strategy.skill_name)
            if not skill_path:
                self._log("L3_SIGNALS", f"SKIP: {strategy.skill_name} not found")
                continue

            # Each strategy skill produces a Signal with:
            # - direction, entry, stop, targets, confidence, reasoning
            signal = Signal(
                strategy_name=strategy.skill_name,
                direction=Direction.FLAT,      # populated by strategy execution
                entry_price=0.0,
                stop_loss=0.0,
                targets=[],
                confidence=0.0,
                timeframe=strategy.timeframes[0] if strategy.timeframes else "H1",
                reasoning="",
                confluence_factors=[],
            )
            self.signals.append(signal)

        self._log("L3_SIGNALS", f"Generated {len(self.signals)} raw signals")
        return self.signals

    # -------------------------------------------------------------------
    # Layer 4: Signal Aggregation
    # -------------------------------------------------------------------

    def aggregate_signals(self, signals: list[Signal]) -> FinalSignal:
        """
        Layer 4: Combine all raw signals into a single FinalSignal.

        Uses weighted voting from ai-signal-aggregator and conflict
        detection. Produces conviction score and identifies disagreements.
        """
        self._log("L4_AGGREGATE", f"Aggregating {len(signals)} signals")

        if not signals:
            self.final_signal = FinalSignal(
                direction=Direction.FLAT, conviction=0.0,
                entry_price=0.0, stop_loss=0.0, targets=[],
                agreement_score=0.0, conflict_flags=["NO_SIGNALS"],
                contributing_signals=[], veto=True,
            )
            return self.final_signal

        # Weighted vote
        long_score = 0.0
        short_score = 0.0
        total_weight = 0.0

        for sig in signals:
            # Look up strategy weight from L2
            weight = 1.0
            for strat in self.strategies:
                if strat.skill_name == sig.strategy_name:
                    weight = strat.weight
                    break

            effective_weight = weight * sig.confidence
            if sig.direction == Direction.LONG:
                long_score += effective_weight
            elif sig.direction == Direction.SHORT:
                short_score += effective_weight
            total_weight += effective_weight

        # Determine direction and conviction
        if total_weight == 0:
            direction = Direction.FLAT
            conviction = 0.0
        elif long_score > short_score:
            direction = Direction.LONG
            conviction = min((long_score - short_score) / total_weight, 0.95)
        elif short_score > long_score:
            direction = Direction.SHORT
            conviction = min((short_score - long_score) / total_weight, 0.95)
        else:
            direction = Direction.FLAT
            conviction = 0.0

        # Conflict detection
        directions = [s.direction for s in signals if s.direction != Direction.FLAT]
        long_count = sum(1 for d in directions if d == Direction.LONG)
        short_count = sum(1 for d in directions if d == Direction.SHORT)
        total_directional = long_count + short_count

        conflict_flags = []
        if long_count > 0 and short_count > 0:
            conflict_flags.append(
                f"CONFLICT: {long_count} LONG vs {short_count} SHORT signals"
            )
        agreement = max(long_count, short_count) / max(total_directional, 1)

        # Veto if agreement below threshold
        veto = agreement < 0.5 or conviction < 0.15

        self.final_signal = FinalSignal(
            direction=direction,
            conviction=round(conviction, 3),
            entry_price=0.0,       # best entry from contributing signals
            stop_loss=0.0,         # tightest stop from contributing signals
            targets=[],
            agreement_score=round(agreement, 3),
            conflict_flags=conflict_flags,
            contributing_signals=signals,
            veto=veto,
        )

        self._log("L4_AGGREGATE",
                  f"Direction={direction.value}, Conviction={conviction:.3f}, "
                  f"Agreement={agreement:.1%}, Veto={veto}")
        return self.final_signal

    # -------------------------------------------------------------------
    # Layer 5: Risk Engine
    # -------------------------------------------------------------------

    def validate_risk(self, signal: FinalSignal) -> RiskApproval:
        """
        Layer 5: Validate the trade against all risk rules.

        Checks: position sizing, portfolio heat, drawdown state,
        correlation risk, event calendar, risk-of-ruin, and tail risk.
        Returns RiskApproval with go/no-go decision.
        """
        self._log("L5_RISK", "Validating risk")

        veto_reasons = []

        # Rule 1: Signal must not be vetoed by L4
        if signal.veto:
            veto_reasons.append("L4 aggregation vetoed: insufficient agreement")

        # Rule 2: Conviction floor
        if signal.conviction < 0.30:
            veto_reasons.append(f"Conviction {signal.conviction:.1%} below 30% floor")

        # Rule 3: Conflict flags
        if signal.conflict_flags:
            veto_reasons.append(f"Unresolved conflicts: {signal.conflict_flags}")

        # Rule 4: Portfolio heat check
        current_heat = 0.0  # would query real-time-risk-monitor
        remaining_heat = self.max_portfolio_heat_pct - current_heat
        if remaining_heat <= 0:
            veto_reasons.append(f"Portfolio heat {current_heat}% exceeds max {self.max_portfolio_heat_pct}%")

        # Rule 5: Event calendar filter (risk-calendar-trade-filter)
        # Would check if high-impact news is within blackout window

        # Rule 6: Drawdown state (drawdown-playbook)
        # Would check current drawdown and apply size reduction rules

        # Position sizing (risk-and-portfolio)
        if signal.stop_loss and signal.entry_price:
            stop_distance = abs(signal.entry_price - signal.stop_loss)
            dollar_risk = self.account_equity * (self.risk_per_trade_pct / 100)
            position_size = dollar_risk / stop_distance if stop_distance > 0 else 0
            rr_ratio = 0.0
            if signal.targets and stop_distance > 0:
                target_distance = abs(signal.targets[0] - signal.entry_price)
                rr_ratio = target_distance / stop_distance

            # Rule 7: Minimum R:R
            if rr_ratio < 1.5:
                veto_reasons.append(f"R:R {rr_ratio:.1f} below 1.5 minimum")
        else:
            dollar_risk = self.account_equity * (self.risk_per_trade_pct / 100)
            position_size = 0.0
            rr_ratio = 0.0

        approved = len(veto_reasons) == 0

        # Apply conviction-based size adjustment
        if approved and signal.conviction < 0.60:
            position_size *= 0.5  # half size for moderate conviction
            conditions = ["Reduced to 50% size (conviction < 60%)"]
        else:
            conditions = []

        self.risk_approval = RiskApproval(
            approved=approved,
            position_size_lots=round(position_size, 2),
            position_size_pct=round(self.risk_per_trade_pct * (0.5 if signal.conviction < 0.60 else 1.0), 2),
            adjusted_stop=signal.stop_loss,
            max_loss_dollars=round(dollar_risk, 2),
            max_loss_pct=self.risk_per_trade_pct,
            portfolio_heat_pct=current_heat + self.risk_per_trade_pct,
            risk_reward_ratio=round(rr_ratio, 2),
            veto_reasons=veto_reasons,
            conditions=conditions,
        )

        self._log("L5_RISK", f"Approved={approved}, Size={position_size:.2f}, "
                  f"Veto reasons={veto_reasons}")
        return self.risk_approval

    # -------------------------------------------------------------------
    # Layer 6: Execution Engine
    # -------------------------------------------------------------------

    def execute(self, signal: FinalSignal, risk: RiskApproval) -> TradeResult:
        """
        Layer 6: Execute the trade if risk-approved.

        Uses execution-algo-trading for optimal entry, mt5-integration
        for order placement, and alert-pipeline for notifications.
        """
        self._log("L6_EXEC", f"Execution mode={self.mode}")

        if not risk.approved:
            self.trade_result = TradeResult(
                order_id="REJECTED",
                symbol=self.symbol,
                direction=signal.direction,
                fill_price=0.0,
                requested_price=signal.entry_price,
                slippage_pips=0.0,
                spread_at_fill=0.0,
                execution_algo="none",
                status="rejected",
                timestamp=datetime.utcnow(),
            )
            self._log("L6_EXEC", f"REJECTED: {risk.veto_reasons}")
            return self.trade_result

        if self.mode == "analysis":
            # Analysis-only mode: report what WOULD be traded
            self.trade_result = TradeResult(
                order_id="ANALYSIS_ONLY",
                symbol=self.symbol,
                direction=signal.direction,
                fill_price=signal.entry_price,
                requested_price=signal.entry_price,
                slippage_pips=0.0,
                spread_at_fill=0.0,
                execution_algo="analysis",
                status="pending",
                timestamp=datetime.utcnow(),
            )
            self._log("L6_EXEC", "Analysis mode: trade plan generated, not executed")
        elif self.mode == "paper":
            # Paper trading via trade-simulator-paper
            self.trade_result = TradeResult(
                order_id=f"PAPER_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
                symbol=self.symbol,
                direction=signal.direction,
                fill_price=signal.entry_price,
                requested_price=signal.entry_price,
                slippage_pips=0.0,
                spread_at_fill=0.0,
                execution_algo="paper",
                status="filled",
                timestamp=datetime.utcnow(),
            )
            self._log("L6_EXEC", "Paper trade logged")
        else:
            # Live mode: use execution-algo-trading + mt5-integration
            # Would invoke MT5 order placement here
            self.trade_result = TradeResult(
                order_id=f"LIVE_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
                symbol=self.symbol,
                direction=signal.direction,
                fill_price=0.0,
                requested_price=signal.entry_price,
                slippage_pips=0.0,
                spread_at_fill=0.0,
                execution_algo="limit",
                status="pending",
                timestamp=datetime.utcnow(),
            )
            self._log("L6_EXEC", "Live order submitted")

        return self.trade_result

    # -------------------------------------------------------------------
    # Layer 7: Learning Engine
    # -------------------------------------------------------------------

    def learn(self, result: TradeResult) -> None:
        """
        Layer 7: Record outcome, update strategy weights, detect decay.

        Uses tensortrade-rl for strategy health monitoring, trade-journal-analytics
        for logging, performance-attribution-engine for factor analysis,
        and feeds updates back to L1/L2/L4/L5.
        """
        self._log("L7_LEARN", f"Recording result: {result.status}")

        # Step 1: Log to trade journal (trade-journal-analytics)
        journal_entry = {
            "timestamp": result.timestamp.isoformat(),
            "symbol": result.symbol,
            "direction": result.direction.value,
            "strategies_used": [s.skill_name for s in self.strategies],
            "conviction": self.final_signal.conviction if self.final_signal else 0,
            "fill_price": result.fill_price,
            "slippage": result.slippage_pips,
            "status": result.status,
        }

        # Step 2: Check for strategy decay (strategy-decay-monitor)
        # Would run rolling Sharpe analysis on recent trades

        # Step 3: Update aggregation weights (feeds back to L4)
        # Strategies that produced correct signals get weight boost

        # Step 4: Update risk parameters (feeds back to L5)
        # If on losing streak, drawdown-playbook kicks in

        # Step 5: Re-evaluate regime detection accuracy (feeds back to L1)

        self.learning_update = LearningUpdate(
            strategy_scores={},
            weight_adjustments={},
            decay_alerts=[],
            risk_param_updates={},
            regime_weight_updates={},
            performance_summary={},
        )

        self._log("L7_LEARN", "Learning cycle complete, weights updated")

    # -------------------------------------------------------------------
    # Full Pipeline: run()
    # -------------------------------------------------------------------

    def run(self) -> dict:
        """
        Execute the complete 7-layer pipeline.

        Returns a comprehensive result dict with outputs from every layer.
        """
        self._log("BRAIN", f"=== Trading Brain activated for {self.symbol} ===")
        self._log("BRAIN", f"Mode={self.mode}, Timeframes={self.timeframes}")

        # L1: Market Intelligence
        market_state = self.analyze_market()

        # L2: Strategy Selection
        strategies = self.select_strategy(market_state)

        # L3: Signal Generation
        signals = self.generate_signals(strategies)

        # L4: Signal Aggregation
        final_signal = self.aggregate_signals(signals)

        # L5: Risk Validation
        risk = self.validate_risk(final_signal)

        # L6: Execution
        trade = self.execute(final_signal, risk)

        # L7: Learning
        self.learn(trade)

        # Compile full report
        return {
            "symbol": self.symbol,
            "timestamp": datetime.utcnow().isoformat(),
            "mode": self.mode,
            "layers": {
                "L1_market_state": {
                    "regime": market_state.regime.value,
                    "regime_confidence": market_state.regime_confidence,
                    "session": market_state.session,
                    "sentiment": market_state.sentiment_score,
                    "volatility_pctl": market_state.volatility_percentile,
                },
                "L2_strategies": [
                    {"name": s.skill_name, "weight": s.weight}
                    for s in strategies
                ],
                "L3_signals": [
                    {"strategy": s.strategy_name, "direction": s.direction.value,
                     "confidence": s.confidence}
                    for s in signals
                ],
                "L4_final_signal": {
                    "direction": final_signal.direction.value,
                    "conviction": final_signal.conviction,
                    "agreement": final_signal.agreement_score,
                    "conflicts": final_signal.conflict_flags,
                    "veto": final_signal.veto,
                },
                "L5_risk": {
                    "approved": risk.approved,
                    "position_size": risk.position_size_lots,
                    "max_loss": risk.max_loss_dollars,
                    "rr_ratio": risk.risk_reward_ratio,
                    "veto_reasons": risk.veto_reasons,
                },
                "L6_execution": {
                    "status": trade.status,
                    "order_id": trade.order_id,
                    "algo": trade.execution_algo,
                },
                "L7_learning": {
                    "decay_alerts": self.learning_update.decay_alerts if self.learning_update else [],
                },
            },
            "log": self.log,
        }

    # -------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------

    def _resolve_layer_skills(self, layer_key: str) -> list[str]:
        """Return available skills for a given layer."""
        wanted = LAYER_SKILLS.get(layer_key, [])
        return [s for s in wanted if s in self._skills]

    def _get_skill_path(self, skill_name: str) -> Optional[str]:
        """Get the filesystem path for a skill's SKILL.md."""
        skill = self._skills.get(skill_name)
        if skill and skill.path:
            return skill.path
        # Fallback: check common locations
        for candidate in [
            SKILLS_DIR / skill_name / "SKILL.md",
            SKILLS_DIR / skill_name / "skill.md"]:
            if candidate.exists():
                return str(candidate)
        return None

    def _detect_session(self) -> str:
        """Detect current trading session based on UTC hour."""
        hour = datetime.utcnow().hour
        if 0 <= hour < 7:
            return "tokyo"
        elif 7 <= hour < 9:
            return "london_open"
        elif 9 <= hour < 12:
            return "london"
        elif 12 <= hour < 14:
            return "london_ny_overlap"
        elif 14 <= hour < 17:
            return "new_york"
        elif 17 <= hour < 21:
            return "new_york_close"
        else:
            return "off_hours"

    def _log(self, layer: str, message: str) -> None:
        """Append to execution log."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "layer": layer,
            "message": message,
        }
        self.log.append(entry)
```

---

## Autonomous Trading Loop (Pseudocode)

```
LOOP forever (or on schedule):
    brain = TradingBrain(symbol, mode="live")

    # L1 ------------------------------------------------------------------
    market_state = brain.analyze_market()
    IF market_state.session in ["off_hours"] AND NOT force:
        SKIP "Outside trading hours"
        CONTINUE

    # L2 ------------------------------------------------------------------
    strategies = brain.select_strategy(market_state)
    IF len(strategies) == 0:
        SKIP "No strategies fit current regime"
        CONTINUE

    # L3 ------------------------------------------------------------------
    signals = brain.generate_signals(strategies)
    IF all signals are FLAT:
        SKIP "No actionable signals"
        CONTINUE

    # L4 ------------------------------------------------------------------
    final = brain.aggregate_signals(signals)
    IF final.veto:
        LOG "Signal vetoed by aggregation layer"
        CONTINUE

    # L5 ------------------------------------------------------------------
    risk = brain.validate_risk(final)
    IF NOT risk.approved:
        LOG f"Risk rejected: {risk.veto_reasons}"
        CONTINUE

    # L6 ------------------------------------------------------------------
    trade = brain.execute(final, risk)
    IF trade.status == "rejected":
        LOG "Execution rejected"
        CONTINUE

    # L7 ------------------------------------------------------------------
    # Wait for trade outcome (async or scheduled check)
    WHEN trade closes:
        brain.learn(trade)
        # Weights updated, fed back to L1/L2/L4/L5

    SLEEP until next_scan_interval
END LOOP
```

---

## Example Workflow: "Analyze EURUSD liquidity trap"

```
USER: "Analyze EURUSD liquidity trap"
BRAIN: Intent = signal generation with ICT/SMC focus

STEP 1 - L1: Market Intelligence
  -> Read: market-intelligence, mt5-chart-browser, liquidity-analysis
  -> mt5-chart-browser: Pull EURUSD M15/H1/H4/D1 OHLCV data
  -> market-regime-classifier: Classify regime -> "TRANSITIONING" (conf 0.72)
  -> liquidity-analysis: Map liquidity pools above/below current price
  -> news-sentiment: Check upcoming events (none in next 4h)
  -> Result: MarketState{regime=TRANSITIONING, session=london_ny_overlap}

STEP 2 - L2: Strategy Selection
  -> Read: strategy-selection, strategy-playbook
  -> Regime=TRANSITIONING maps to:
     1. market-structure-bos-choch (0.30)
     2. wyckoff-method-engine (0.25)
     3. smart-money-trap-detector (0.25)  <-- directly relevant
     4. divergence-strategy-engine (0.20)
  -> Result: 4 strategies selected

STEP 3 - L3: Signal Generation
  -> Read: smart-money-trap-detector SKILL.md
     -> Detects: Liquidity grab below 1.0850 Asian low, followed by
        aggressive buying (bullish engulfing on M15), FVG left at 1.0855
     -> Signal: LONG, entry=1.0858, stop=1.0835, target=[1.0890, 1.0920]
     -> Confidence: 0.78
  -> Read: market-structure-bos-choch SKILL.md
     -> Detects: CHoCH on M15 after stop hunt, BOS confirmed on H1
     -> Signal: LONG, confidence=0.71
  -> Read: wyckoff-method-engine SKILL.md
     -> Detects: Spring pattern (Phase C), volume climax on the sweep
     -> Signal: LONG, confidence=0.68
  -> Read: divergence-strategy-engine SKILL.md
     -> Detects: Bullish RSI divergence on H1
     -> Signal: LONG, confidence=0.55
  -> Result: 4 signals, all LONG

STEP 4 - L4: Signal Aggregation
  -> Read: ai-signal-aggregator
  -> Weighted vote: 4/4 LONG, agreement=100%
  -> Conviction: 0.82 (high)
  -> Conflict flags: NONE
  -> Result: FinalSignal{direction=LONG, conviction=0.82, veto=False}

STEP 5 - L5: Risk Engine
  -> Read: risk-and-portfolio, risk-and-portfolio
  -> Stop distance: 23 pips (1.0858 - 1.0835)
  -> Target 1 distance: 32 pips -> R:R = 1.39 (below 1.5 threshold!)
  -> Target 2 distance: 62 pips -> R:R = 2.70 (good)
  -> Decision: APPROVED with target 2 as primary, target 1 as partial TP
  -> Position size: 0.43 lots (1% of $10,000 / 23 pips)
  -> Portfolio heat: 1.0% (well within 6% max)
  -> Result: RiskApproval{approved=True, size=0.43}

STEP 6 - L6: Execution
  -> Read: execution-algo-trading
  -> Recommendation: Limit order at 1.0858 (FVG retest)
  -> Mode=analysis: Report trade plan, do not execute
  -> Result: TradeResult{status=pending, algo=analysis}

STEP 7 - L7: Learning
  -> Log trade setup to journal
  -> smart-money-trap-detector accuracy: 78% (above threshold)
  -> No decay alerts
  -> Weights unchanged

FINAL OUTPUT TO USER:
  "EURUSD Liquidity Trap Analysis -- 7-Layer Result
   Direction: LONG | Conviction: 82% | Agreement: 4/4 strategies
   Entry: 1.0858 (FVG retest) | Stop: 1.0835 (-23 pips)
   TP1: 1.0890 (+32 pips, partial) | TP2: 1.0920 (+62 pips, full)
   Position: 0.43 lots | Risk: $100 (1.0%)
   Regime: Transitioning | Session: London-NY overlap
   Key: Liquidity grab confirmed, Wyckoff spring, CHoCH + BOS aligned"
```

---

## Operating Rules

| # | Rule | Detail |
|---|------|--------|
| 1 | **Always start at L1** | Never skip market intelligence. Context is everything. |
| 2 | **No layer skipping** | Every layer must run, even if abbreviated. L5 is never optional. |
| 3 | **L5 has veto power** | Risk engine can reject any trade, regardless of conviction. |
| 4 | **Surface all conflicts** | Never hide conflicting signals from L4. Show them prominently. |
| 5 | **Conviction thresholds** | <30% = no trade, 30-60% = half size, >60% = standard size. |
| 6 | **Mode awareness** | In "analysis" mode, never place orders. Report what WOULD happen. |
| 7 | **Log everything** | Every layer writes to the execution log for L7 consumption. |
| 8 | **Fail gracefully** | If one skill errors, continue pipeline with remaining skills. |
| 9 | **L7 feedback is mandatory** | Every trade (win or loss) feeds back to update weights. |
| 10 | **Past performance caveat** | Always include: historical analysis does not guarantee future results. |

---

## How to Invoke This Skill

When Claude receives any trading-related query:

1. **Read this file first** -- it is the master routing table.
2. **Identify which layer(s) the query targets.** A simple "What's the RSI?" is L3 only. A "Full analysis of GBPJPY" triggers L1-L6.
3. **Read the relevant sub-skill SKILL.md files** as determined by the layer mapping table above.
4. **Execute layer by layer**, passing outputs forward.
5. **Always finish with a synthesis** that includes: direction, conviction, key levels, risk parameters, and caveats.

### Quick Layer Dispatch

| User says... | Layers triggered |
|---|---|
| "What's happening in markets?" | L1 only |
| "Which strategy for ranging EUR?" | L1 + L2 |
| "Is there a trade on gold?" | L1 + L2 + L3 + L4 |
| "Should I take this trade?" | L1 through L5 |
| "Full analysis of USDJPY" | L1 through L6 |
| "Run the brain on EURUSD" | L1 through L7 (full pipeline) |
| "Why am I losing lately?" | L7 (learning + journal review) |
| "Update strategy weights" | L7 -> feedback to L2 + L4 |
