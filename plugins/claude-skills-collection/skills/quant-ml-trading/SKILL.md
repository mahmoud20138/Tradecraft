---
name: quant-ml-trading
description: >
  Complete quantitative and ML-powered trading toolkit — strategy validation, genetic
  optimization, decay monitoring, reinforcement learning, signal aggregation, data science
  pipelines, and statistical/quant foundations.
  Use this skill for: "generate a backtest report", "create tearsheet", "equity curve",
  "Monte Carlo simulation", "strategy report", "performance tearsheet", "backtest results",
  "drawdown analysis", "strategy statistics", "risk report", "publish backtest", "PDF report",
  "HTML report", "walk-forward", "out of sample validation", "rolling optimization", "WFO",
  "anchored walk forward", "parameter stability", "robustness test", "rolling backtest",
  "adaptive optimization", "parameter reoptimization", "stress test", "bootstrap simulation",
  "worst case scenario", "parameter sensitivity", "confidence interval", "ruin probability",
  "survival analysis", "tail risk", "heatmap", "parameter sweep", "optimization surface",
  "3D surface", "parameter landscape", "which parameters matter", "robust parameters",
  "sensitivity analysis", "parameter grid search", "A/B test strategies", "compare
  strategies", "which strategy is better", "statistical comparison", "strategy comparison",
  "head to head", "variant testing", "significance test", "optimize strategy",
  "evolve parameters", "genetic algorithm", "breed strategies", "parameter optimization",
  "auto-optimize", "find best parameters", "evolutionary search", "mutation", "crossover",
  "fitness function", "population-based optimization", "is my strategy still working",
  "strategy decay", "alpha decay", "edge erosion", "performance degradation",
  "parameter drift", "when to retire a strategy", "strategy health check", "is the edge
  gone", "strategy monitoring", "live vs backtest divergence", "reinforcement learning
  trading", "RL agent", "deep Q-network trading", "PPO trading", "train an agent",
  "learn from replay", "reward function trading", "AI agent that learns to trade",
  "gym trading environment", "state space market", "action space trading", "combine all
  signals", "aggregate strategies", "meta strategy", "AI signal", "ensemble signal",
  "which signal to follow", "best signal now", "combine everything", "master signal",
  "AI recommendation",
  "backtesting framework", "walk-forward analysis", "overfitting prevention",
  "survivorship bias", "look-ahead bias", "performance metrics", "Sharpe", "Sortino",
  "Calmar", "Information Ratio", "win rate", "profit factor", "expectancy", "R-multiple",
  "SQN", "ARIMA models", "GARCH volatility", "regression analysis", "Fama-French factors",
  "machine learning trading", "random forest", "XGBoost", "LSTM",
  "feature engineering for trading", "market regime detection", "NLP sentiment analysis",
  "algorithmic execution", "TWAP", "VWAP", "implementation shortfall", "factor investing",
  "value", "momentum", "size", "quality", "low volatility", "statistical arbitrage",
  "cointegration", "mean reversion statistics", "Z-score trading",
  "analyze trading data", "build ML models on price data", "feature engineering on market data",
  "store retrieve analysis results", "run data science on my pairs",
  "find patterns in the data", "statistical analysis of EURUSD", "cluster market regimes",
  "anomaly detection on price", "store my analysis", "retrieve past analysis",
  "data pipeline", "machine learning on forex data", "train a model", "feature importance",
  "large-scale data processing", "ETL", "persistent result storage",
  "data science pipeline", "data cleaning", "data validation", "OHLCV cleaning",
  or any strategy validation, genetic optimization, decay detection, RL trading,
  ML signal aggregation, quantitative analysis, or data science task applied to trading.
related_skills:
  - ml-trading
  - backtesting-sim
  - statistics-timeseries
  - backtesting-sim
tags:
  - trading
  - quant
  - machine-learning
  - genetic
  - reinforcement-learning
  - signals
skill_level: expert
kind: reference
category: trading/quant
status: active
---
> **Skill:** Quant Ml Trading  |  **Domain:** trading  |  **Category:** quantitative  |  **Level:** expert
> **Tags:** `trading`, `quant`, `machine-learning`, `genetic`, `reinforcement-learning`, `signals`


# Quant & ML Trading — Complete Toolkit

## Overview
Five powerful tools for quantitative strategy work:

1. **Strategy Validation** — backtest tearsheets, walk-forward OOS, Monte Carlo, sensitivity, A/B testing
2. **Genetic Optimizer** — evolve strategy parameters using evolutionary algorithms
3. **Decay Monitor** — detect when a live strategy is losing its edge
4. **RL Trade Agent** — reinforcement learning agent (DQN) that learns to trade from market replay
5. **AI Signal Aggregator** — combine signals from all strategies using weighted voting + ML meta-model

## Reference Files

| File | Contents |
|------|----------|
| `references/strategy-validation.md` | Tearsheet, walk-forward WFO, Monte Carlo, sensitivity heatmaps, A/B testing |
| `references/genetic-optimizer.md` | Gene encoding, fitness functions, GA engine, anti-overfitting safeguards |
| `references/tensortrade-rl.md` | Strategy decay monitor (CUSUM, rolling Sharpe, live vs backtest) + RL trading environment + DQN agent |
| `references/ai-signal-aggregator.md` | Weighted voting, ML meta-learner, confidence calibration, trade decision engine |
| `references/quantitative-trading.md` | Quant workflow diagram, performance metrics table, pitfalls table, key formulas (Sharpe/Kelly/Z-score/IR/Expectancy) |
| `references/statistics-timeseries.md` | Descriptive stats, return distributions, stationarity (ADF/KPSS), ARIMA models, GARCH volatility, regression, Fama-French factors, cointegration |
| `references/ml-trading.md` | Supervised learning (XGBoost/LSTM/RF configs), feature engineering, regime detection (K-Means/HMM/GMM), RL, NLP sentiment, model validation |
| `references/backtesting-execution.md` | 10 backtesting rules, walk-forward, Monte Carlo, detailed performance metrics, 8 pitfalls, TWAP/VWAP/IS execution, factor strategies |
| `references/data-science-pipeline.md` | DataPipeline (OHLCV clean/validate/resample), FeatureEngine, StatisticalAnalysis, ModelFactory, TradingDataStore (persistent storage) |

## Quick Decision Guide

```
Strategy tearsheet / backtest report / Monte Carlo?
  → Load references/strategy-validation.md

Parameter optimization / genetic algorithm / evolve strategy?
  → Load references/genetic-optimizer.md

Strategy decay / live vs backtest divergence / RL agent?
  → Load references/tensortrade-rl.md

Combine signals / meta-model / AI signal aggregation?
  → Load references/ai-signal-aggregator.md

Quant workflow / performance metrics / key formulas?
  → Load references/quantitative-trading.md

Stats / time series / ARIMA / GARCH / regression / Fama-French?
  → Load references/statistics-timeseries.md

ML models / feature engineering / regime detection / NLP?
  → Load references/ml-trading.md

Backtesting rules / execution algos / factor strategies (detail)?
  → Load references/backtesting-execution.md

Data cleaning / feature pipeline / anomaly detection / persistent storage / ETL?
  → Load references/data-science-pipeline.md

Multiple topics?
  → Load all relevant reference files
```

## Anti-Overfitting Rules (ALL skills)
1. Always use walk-forward OOS — never optimize on all available data
2. Monte Carlo bootstrap required before any live deployment
3. GA/RL results MUST be validated on unseen temporal data
4. Meta-model must be re-trained monthly with rolling walk-forward
5. Live vs backtest Sharpe gap > 0.5 = pause the strategy immediately
---

---

## Related Skills

- [Ai Pattern Recognition](../ml-trading.md)
- [Backtesting Sim](../backtesting-sim.md)
- [Statistical Analysis](../statistics-timeseries.md)
- [Algorithmic Strategies](../backtesting-sim.md)
