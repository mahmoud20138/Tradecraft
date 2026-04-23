# Tradecraft — Commands Reference

Every skill in Tradecraft is invoked as `/tradecraft:<skill-name>`. Total: **169** skills across **6** domains (plus 12 currently uncategorized).

To install, see **[INSTALL.md](INSTALL.md)**.

## Table of Contents

- [Parameterized commands](#parameterized-commands) — skills that accept arguments
  - [`/tradecraft:fetch-quotes`](#tradecraftfetch-quotes)
  - [`/tradecraft:pair-analyze`](#tradecraftpair-analyze)
  - [`/tradecraft:analyze-gold`](#tradecraftanalyze-gold)
  - [`/tradecraft:analyze-us30`](#tradecraftanalyze-us30)
  - [`/tradecraft:master-trading-workflow`](#tradecraftmaster-trading-workflow)
  - [`/tradecraft:xtrading-analyze`](#tradecraftxtrading-analyze)
  - [`/tradecraft:analyze`](#tradecraftanalyze)
- [All skills by domain](#all-skills-by-domain)
  - [Trading](#trading) (104)
  - [AI Development](#ai-development) (7)
  - [Software Engineering](#software-engineering) (20)
  - [Claude Code Platform](#claude-code-platform) (20)
  - [Data Acquisition](#data-acquisition) (4)
  - [Domain Specific](#domain-specific) (2)
  - [Uncategorized](#uncategorized) (12)

---

## Parameterized commands

These seven commands accept positional arguments. Run them as:

```text
/tradecraft:<skill-name> [arg1] [arg2] ...
```

All other skills in this plugin load as knowledge context — just invoke by name (no arguments).

### `/tradecraft:fetch-quotes`

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

### `/tradecraft:pair-analyze`

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

### `/tradecraft:analyze-gold`

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

### `/tradecraft:analyze-us30`

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

### `/tradecraft:master-trading-workflow`

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

### `/tradecraft:xtrading-analyze`

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

### `/tradecraft:analyze`

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

---

## All skills by domain

The knowledge skills below take no arguments — invoke by name and they load as context for Claude. Descriptions come directly from each skill's YAML frontmatter.

### Trading

104 skill(s)

| Command | Description |
|---|---|
| `/tradecraft:ai-signal-aggregator` | ML-powered signal aggregation across ALL strategy skills — combines signals from every strategy using weighted voting, random forest meta-learner, and confidence calibration. THE MASTER SIGNAL COMBINER. Use for "combine all signals", "aggregate strategies", "meta strategy", "AI signal", "ensemble signal", "which signal to follow", "best signal now", "combine everything", "master signal", "AI recommendation", or any request to synthesize signals from multiple skills. This is the intelligence l... |
| `/tradecraft:ai-trading-crew` | AI Trading Crew — 50-agent AutoGen system for US stock analysis. 8 specialized teams (Technical, Fundamental, Macro, Sentiment, Quant, Risk, Execution, Strategy) reporting to a Head Coach supervisor. Risk team has veto power. Devil's Advocate agent f |
| `/tradecraft:alternative-data-integrator` | Alternative data sources for trading signals — Google Trends, web traffic, search volume, shipping/supply chain data, satellite imagery proxies, and economic nowcasting. Use this skill whenever the user asks about "alternative data", "Google Trends trading", "search trends", "web traffic signals", "nowcasting", "satellite data trading", "shipping index", "Baltic Dry", "unusual data sources", "non-traditional indicators", "big data trading signals", or any request to incorporate non-standard d... |
| `/tradecraft:analyze` | Instant full trading analysis — just type a symbol. Auto-detects asset class, timeframe, and runs the complete 18-phase master workflow. Use for ANY ticker/symbol like "EURUSD", "AAPL", "BTCUSD", "XAUUSD", "SPY", "NQ", "ES". This is THE one-command entry point. |
| `/tradecraft:analyze-gold` | Pre-configured combination command for gold (XAUUSD) analysis. Runs the full pair-analyze pipeline tuned for gold's volatility profile, session behavior, and dollar sensitivity. USE FOR - analyze gold, analyze XAUUSD, gold setup, trade gold, gold analysis, XAUUSD plan. |
| `/tradecraft:analyze-us30` | Pre-configured combination command for US30 (Dow Jones Industrial Average CFD) analysis. Runs the full pair-analyze pipeline tuned for US30's session-driven flow, earnings sensitivity, and Fed-rate reactivity. USE FOR - analyze US30, analyze Dow, analyze Dow Jones, US30 setup, trade US30, DJ30 plan. |
| `/tradecraft:asian-session-scalper` | Tokyo session low-volatility scalping setups — range-bound strategies for the quietest session. Use for "Asian scalp", "Tokyo session trade", "Asian range", "night scalping", "low vol scalp", "Asian session strategy", or any Tokyo-session-specific trading. Works with session-profiler. |
| `/tradecraft:backtest-report-generator` | Generates publication-quality backtest reports with equity curves, Monte Carlo simulations, tearsheets, and comprehensive risk analysis. Use this skill whenever the user asks to "generate a backtest report", "create tearsheet", "equity curve", "Monte Carlo simulation", "strategy report", "performance tearsheet", "backtest results", "drawdown analysis", "strategy statistics", "risk report", "publish backtest", "PDF report", "HTML report", or any request to visualize and document strategy backt... |
| `/tradecraft:backtesting-sim` | Backtesting and simulation: vectorized backtesting, paper trading simulation, strategy A/B testing, automated strategy building, natural language to strategy, and trading plan generation. USE FOR: backtest, backtesting, paper trading, simulation, strategy builder, A/B test strategies, natural language strategy, trading plan, equity curve, drawdown analysis, walk-forward, Monte Carlo simulation, performance metrics, Sharpe, Sortino, Calmar, win rate, profit factor, expectancy, strategy validat... |
| `/tradecraft:borsellino-10-commandments` | Lewis Borsellino's 10 Commandments of Trading — the discipline framework from the largest S&P pit trader in Chicago history ($4.7M in one day, 10% of S&P volume, 20 years without a losing year). Covers trading for success vs money, discipline, knowing yourself, killing ego, avoiding hope/prayer, letting profits run, knowing when to trade, loving losers, the 3-loss circuit breaker, and the unbreakable rule. Source: Words of Rizdom podcast (March 2026, Arabic dubbed). Use this skill for "Borsel... |
| `/tradecraft:breakout-strategy-engine` | Pre-built breakout strategy templates — volatility squeeze detection, range breakout, momentum breakout with confirmation filters. Use this skill whenever the user asks about "breakout strategy", "Bollinger squeeze", "range breakout", "momentum breakout", "volatility expansion", "ATR breakout", "Donchian breakout", "breakout confirmation", "false breakout filter", "squeeze momentum", "compression breakout", or any breakout-based trade setup. Works with market-regime-classifier, mt5-chart-brow... |
| `/tradecraft:capitulation-mean-reversion` | Lance Breitstein's $100M+ capitulation mean reversion framework — 7-variable checklist, slope analysis for waterfalls, "Right Side of the V" entry method, multi-variable mental rubric scoring, and prior-bar-highs/lows trailing system. Covers the complete decision framework from scanning to entry to trade management. Source: Chart Fanatics interview (Market Wizard, Trillium's top trader 2020-2021). Use this skill for "capitulation trade", "Lance Breitstein", "Breitstein strategy", "right side ... |
| `/tradecraft:chart-vision` | Complete chart vision pipeline — render charts, preprocess images, detect candlestick patterns, detect classical chart patterns, detect trendlines and S/R levels, and annotate results back onto charts. Use this skill for ANY chart image task: "render a chart", "create chart image", "screenshot chart", "generate candlestick chart", "draw chart with indicators", "produce chart for analysis", "make a chart PNG", "render OHLCV", "chart to image", "visual chart output", "clean chart image", "prepr... |
| `/tradecraft:correlation-crisis` | Correlation breakdown during crises, tail risk measurement (VaR, CVaR, fat tails), regime-dependent correlation matrices, hedging strategies by volatility regime, and stress testing protocols. Use for correlation crisis, tail risk, VaR, CVaR, hedging strategy, stress test, or any correlation/tail-risk analysis. |
| `/tradecraft:correlation-regime-switcher` | Automatically switches strategy sets when correlation regimes change. Use this skill whenever the user asks about "correlation regime change", "adaptive strategy switching", "when correlations break", "regime-based strategy selection", "correlation breakdown trading", "dynamic strategy switching", "auto-switch strategy", or any question about adapting to changing inter-market relationships. Works with pair-correlation-engine and market-regime-classifier. |
| `/tradecraft:cross-asset-arbitrage-engine` | Statistical arbitrage, triangular arbitrage, basis trades, and convergence detection across instruments. Use this skill whenever the user asks about "arbitrage", "stat arb", "pairs trading", "triangular arbitrage", "convergence trade", "mean reversion pair", "cointegration", "basis trade", "spread trading", "relative value", "mispricing detection", or any cross-asset relative value strategy. Works with pair-correlation-engine and mt5-chart-browser. |
| `/tradecraft:cross-asset-relationships` | Cross-asset and quantitative analysis: pair correlations, correlation heatmaps, currency strength, cross-timeframe divergence, intermarket analysis, market breadth, carry trades, swap rates, risk premia, and multi-pair baskets. USE FOR: correlation, currency strength, intermarket, market breadth, carry trade, swap rate, risk premia, basket, pair trading, cross asset, quant. |
| `/tradecraft:crypto-defi-trading` | Crypto and DeFi trading: DEX analysis (Uniswap, SushiSwap, Curve), on-chain analytics, MEV detection, impermanent loss, yield farming metrics, DeFi risk analysis, token metrics, liquidity pool analysis, whale tracking, exchange netflow. USE FOR: crypto, defi, dex, uniswap, sushiswap, curve, impermanent loss, yield farming, on-chain, whale, MEV, arbitrage, liquidity pool, token, exchange flow, gas, NFT. |
| `/tradecraft:dan-zanger-breakout-strategy` | Dan Zanger's complete breakout trading strategy - the system that turned $10,775 into $42 million in 23 months. Chart pattern breakouts with volume confirmation and strict risk management. |
| `/tradecraft:discord-webhook` | Send trading alerts, signals, and analysis summaries to Discord via webhook. Integrates with realtime-alert-pipeline, trading-brain, and trade-journal-analytics. |
| `/tradecraft:drawdown-playbook` | Drawdown taxonomy, tiered response protocols (caution to emergency), equity curve health analysis, recovery mathematics, and pre-drawdown preparation. Use for drawdown, equity curve, max drawdown, recovery protocol, drawdown management, or any drawdown-related analysis. |
| `/tradecraft:economic-calendar` | Economic calendar data: high-impact event detection, news avoidance windows, pre-event volatility expansion, post-event fade, event-driven trade setup. USE FOR: economic calendar, economic events, news events, NFP, CPI, FOMC, GDP, PMI, retail sales, high impact news, news avoidance, pre-news, post-news, event risk, news trading, data release, central bank, interest rate decision. |
| `/tradecraft:economic-indicator-tracker` | Track leading, lagging, and coincident economic indicators systematically. Use for "economic indicators", "leading indicator", "lagging indicator", "PMI tracker", "GDP tracker", "jobs data", "inflation tracker", "economic cycle", "recession indicator", "expansion indicator", "economic health", or any systematic macro indicator tracking. Works with macro-economic-dashboard. |
| `/tradecraft:elliott-wave-engine` | Elliott Wave counting and forecasting — impulse waves, corrective patterns, wave degree. Use for "Elliott Wave", "wave count", "impulse wave", "corrective wave", "wave 3", "wave 5", "ABC correction", "wave analysis", "Fibonacci wave", "wave degree", or any Elliott Wave analysis. Works with fibonacci-strategy-engine for price targets and chart-pattern-scanner. |
| `/tradecraft:equities-trading` | Equities and stock CFD trading: NYSE/NASDAQ sessions, stock-specific mechanics, earnings impact, sector rotation, index correlation, gap trading, opening range. USE FOR: stocks, equities, stock CFD, NYSE, NASDAQ, earnings, sector rotation, index correlation, opening range breakout, ORB, gap and go, pre-market, after-hours, stock screener, TSLAm, AAPLm, MSFTm, NVDAm, AMZNm, GOOGm, METAm, JPMm, BAm. |
| `/tradecraft:execution-algo-trading` | Institutional execution algorithms: TWAP, VWAP, Implementation Shortfall, POV, Iceberg orders, slippage analysis, market impact, and TCA. USE FOR: execution, TWAP, VWAP, implementation shortfall, slippage, market impact, TCA, iceberg order, POV, algo execution, transaction cost. |
| `/tradecraft:fetch-quotes` | Cascading market-data fetcher. Prefers yfinance (free, no credentials) and falls back to a local MT5 terminal when available for broker-exact pricing. Returns OHLCV bars plus a latest quote as JSON, optionally with a PNG chart. USE FOR - get quotes, get data, fetch bars, live data, market data, price data, get chart, quotes for XAUUSD, quotes for US30, any symbol data. |
| `/tradecraft:fibonacci-harmonic-wave` | Fibonacci retracement/extension levels, harmonic pattern detection (Gartley, Butterfly, Bat, Crab, Cypher, Shark), and Elliott Wave counting with Python engines. Use for Fibonacci levels, harmonic pattern, Elliott Wave, wave count, XABCD pattern, or any combined Fibonacci/harmonic/wave analysis. |
| `/tradecraft:forex-trading` | Forex market specifics: major/minor/exotic pairs, currency pair mechanics, pip values, lot sizes, swap/rollover, session overlaps, carry trades, central bank impact. USE FOR: forex pairs, currency pairs, pip value, lot size, major pairs, minor pairs, exotic pairs, forex session, carry trade, swap rates, rollover, central bank, forex spread, forex leverage, currency risk, forex broker, forex liquidity. |
| `/tradecraft:freqtrade-bot` | Freqtrade — open-source Python crypto trading bot. Backtesting, hyperopt (ML parameter optimization), FreqAI (self-training adaptive strategies), Telegram + WebUI control. Supports Binance, Kraken, Bybit, OKX, Gate.io (spot + futures). SQLite trade h |
| `/tradecraft:futures-trading` | Futures markets: contract specs, margin, rollover dates, commodity futures, index futures, interest rate futures, contango/backwardation, basis risk. USE FOR: futures contract, futures margin, rollover, expiry, contango, backwardation, commodity futures, crude oil futures, gold futures, ES futures, NQ futures, S&P futures, Nasdaq futures, treasury futures, basis risk, futures spread, USOILm, XAUUSDm futures. |
| `/tradecraft:gap-trading-strategy` | Gap trading — opening gaps, gap fill probability, gap-and-go, fade the gap. Use for "gap trading", "opening gap", "gap fill", "gap and go", "fade the gap", "Sunday gap", "weekend gap", "gap statistics", "gap probability", or any gap-based trading. Works with session-profiler. |
| `/tradecraft:gold-orb-ea` | GOLD_ORB — MQL5 Expert Advisor for XAUUSD 1H Opening Range Breakout. Identifies opening range (first 1H candle after 1:02 AM server time), confirms consolidation (min 3 candles), then trades breakouts. Buy signal on resistance break, sell on support |
| `/tradecraft:grid-trading-engine` | Systematic grid trading — place buy/sell orders at fixed intervals across a price range. Use for "grid trading", "grid bot", "grid strategy", "buy the dips grid", "DCA grid", "range grid", "grid order placement", or any systematic interval-based order strategy. Works with market-regime-classifier (best in RANGING regimes) and risk-and-portfolio. |
| `/tradecraft:harmonic-pattern-engine` | Harmonic pattern detection — Gartley, Butterfly, Bat, Crab, Cypher, Shark with Fibonacci ratio validation. Use for "harmonic pattern", "Gartley", "Butterfly pattern", "Bat pattern", "Crab pattern", "Cypher", "XABCD", "harmonic trading", "Scott Carney", or any harmonic analysis. Works with fibonacci-strategy-engine and chart-pattern-scanner. |
| `/tradecraft:hurst-exponent-dynamics-crisis-prediction` | Mark Vogel's Oxford ISF Conference research on rolling-window Hurst exponent dynamics of wavelet-denoised S&P 500 returns (2000-2020). Covers the chaos analysis framework, cascadic wavelet denoising, recurrence quantification analysis, multifractal DFA spectra, rolling-window bootstrapping, momentum crash prediction via fractal-trend-to-mean-reversion regime shifts, and continuous wavelet transform heatmaps for crisis detection. Contradicts Mandelbrot's long-memory interpretation -- shows H>0... |
| `/tradecraft:ict-smart-money` | ICT (Inner Circle Trader) Smart Money Concepts — full methodology reference by Michael J. Huddleston. Covers market structure (BOS/CHoCH/MSS), order blocks, smart money traps, supply/demand zones, Wyckoff method, institutional behavior, order flow delta analysis, power of 3, AMD accumulation manipulation distribution, PD arrays, killzones, silver bullet, judas swing, optimal trade entry OTE, liquidity BSL SSL, fair value gap FVG, inverse FVG IFVG, CISD change in state of delivery, breaker blo... |
| `/tradecraft:ict-trading-tool` | Automated MT5 trading tool using ICT Smart Money Concepts. Scans 21 instruments, scores setups (0-12), generates charts, executes and monitors trades. Use for ICT scanner, MT5 automated trading, scan for ICT setups, or any automated ICT execution. |
| `/tradecraft:institutional-timeline` | Central bank policy tracking, COT positioning analysis, FX intervention detection, and event timeline linking with causal chain analysis. Use for central bank, COT report, institutional flow, FX intervention, policy divergence, event timeline, or any institutional behavior monitoring. |
| `/tradecraft:jdub-price-action-strategy` | Jdub Trades' 3-step price action framework: Direction, Location, Execution. Three-bar confirmation entry pattern (lead, reaction, confirmation candle). Key POIs: old highs/lows, PDH/PDL, opening print/previous day close. Two-timeframe rule for entry alignment. 9:30 AM NY open M5 scalping variant. 1-minute Opening Range Break & Retest scalping (no bias needed). USE FOR: Jdub Trades strategy, three bar entry, three bar confirmation, direction location execution, PDH PDL trading, opening print t... |
| `/tradecraft:liquidity-analysis` | Advanced liquidity analysis: pool identification, institutional flow detection, DOM/orderbook reading, volume concentration mapping, dark pool activity, micro-structure signals, real-time liquidity monitoring, slippage modeling, session liquidity patterns, tick data interpretation. USE FOR: liquidity pool, liquidity analysis, order flow imbalance, DOM depth of market, institutional accumulation, block trade detection, dark pools, spread widening, volume clusters, VWAP analysis, liquidity dens... |
| `/tradecraft:macro-economic-dashboard` | Macro economic inter-market analysis dashboard — DXY, VIX, yield curves, bond spreads, commodity flows, and cross-asset correlations. Use this skill whenever the user asks about "DXY", "dollar index", "VIX", "volatility index", "yield curve", "bond yields", "10-year", "2-10 spread", "yield inversion", "risk on risk off", "inter-market", "commodity flows", "gold vs dollar", "oil vs CAD", "equities vs forex", "macro overview", "big picture", "cross-asset", "safe havens", or any macro-level inte... |
| `/tradecraft:market-breadth-analyzer` | Market breadth — how many pairs trending vs ranging, overall market health, breadth divergence. Use for "market breadth, breadth scan, market health, how many trending, broad market, pairs trending", or any related query. Works with trading-brain and relevant analysis/strategy skills. |
| `/tradecraft:market-data-ingestion` | Market data ingestion pipelines: OHLCV data fetching from MT5, yfinance, Alpha Vantage, data cleaning, normalization, missing bar handling, multi-symbol batch fetching. USE FOR: market data, OHLCV, fetch data, download data, historical data, MT5 data, yfinance, Alpha Vantage, data pipeline, data ingestion, price data, candle data, bar data, multi-symbol, batch fetch, data cleaning, normalize prices. |
| `/tradecraft:market-impact-model` | Estimate your own orders' market impact and optimize execution for larger accounts. Use this skill whenever the user asks about "market impact", "slippage model", "order impact", "large order execution", "TWAP", "VWAP execution", "implementation shortfall", "transaction cost analysis", "TCA", "optimal execution speed", "Almgren-Chriss", or any question about executing larger positions without moving the market. Works with execution-algo-trading and market-microstructure-analyzer. |
| `/tradecraft:market-intelligence` | Complete market intelligence layer — macro analysis, regime classification, news impact, sentiment, institutional behavior, event timelines, pair correlations, and trading fundamentals. Includes NLP sentiment scoring, news straddle strategies, COT positioning, seasonality analysis, contrarian sentiment composites, economic indicator tracking, and event timeline linking. MACRO & INTERMARKET: "DXY", "dollar index", "VIX", "volatility index", "yield curve", "bond yields", "10-year", "2-10 spread... |
| `/tradecraft:market-making-hft` | Market making and high-frequency trading: quote generation, inventory management, order book analysis, latency tracking, microstructure signals, spoofing detection, optimal execution (TWAP/VWAP), Avellaneda-Stoikov model, order flow toxicity, market impact estimation. USE FOR: market making, market maker, HFT, high frequency, order book, bid ask, spread, inventory, spoofing, microstructure, latency, TWAP, VWAP, order flow, toxicity, tick data, limit order. |
| `/tradecraft:market-regime-classifier` | ML-powered market regime classification — trending, ranging, volatile, quiet. Automatically adapts strategy selection based on detected regime. Use this skill whenever the user asks "is the market trending", "what regime are we in", "ranging or trending", "market conditions", "volatility regime", "classify market state", "adapt strategy", "regime change", "market phase", "consolidation or breakout", "trending market detection", or any question about current market conditions and which strateg... |
| `/tradecraft:market-structure-bos-choch` | Market structure analysis — Break of Structure (BOS), Change of Character (CHoCH), premium/ discount, market structure shifts, and candle-close swing validation (Jonathan Jarvis method). Use for "BOS", "break of structure", "CHoCH", "change of character", "market structure shift", "MSS", "structure break", "higher high higher low", "lower high lower low", "internal structure", "swing structure", "valid high", "valid low", "candle close validation", "mechanical structure", "Norfolk FX", or any... |
| `/tradecraft:markets` | Entry-point live-market scan. Returns current quote, H1/H4 regime, session state, and watch levels for a default watchlist (gold, US30, US500, US100, EURUSD, GBPUSD, BTCUSD, ETHUSD) — or any custom list. Uses the free yfinance path by default, MT5 if available. USE FOR - scan markets, what's moving, market overview, current prices, what's on the watchlist, show me the markets. |
| `/tradecraft:master-trading-workflow` | Master 18-phase trading workflow — the definitive skill sequence for any trade. Covers infrastructure through automation. Use for "trading workflow", "full process", "trade checklist", "how to trade", "complete trading plan", "master plan", "what skills to run", "trade from scratch". |
| `/tradecraft:mean-reversion-engine` | Mean reversion strategy templates — Bollinger bounce, RSI extreme fade, Z-score reversion with regime guard. Use this skill for "mean reversion", "fade the move", "RSI overbought oversold", "Bollinger bounce", "reversion to mean", "Z-score trade", "oversold bounce", "overbought fade", "rubber band strategy", "range trading strategy", or any reversion setup. Works with market-regime-classifier (ONLY use in ranging regimes) and risk-and-portfolio. |
| `/tradecraft:ml-trading` | Machine learning for trading — supervised classification/regression (XGBoost, LSTM), feature engineering, unsupervised regime detection (K-Means, HMM), reinforcement learning (PPO), NLP sentiment, and time-series cross-validation. Use for ML trading, machine learning, feature engineering, XGBoost, LSTM, or any ML-based trading model development. |
| `/tradecraft:mt5-chart-browser` | MT5 chart browser, pair scanner, indicator engine, and GPU-accelerated chart image analysis. Use this skill whenever the user asks to open MT5, browse pairs, view charts, apply indicators, screenshot charts, analyze chart images, read candlestick patterns from screenshots, scan multiple pairs visually, or perform any visual/technical analysis on MT5 charts. Also trigger when the user says "open MT5", "show me EURUSD", "what does the chart look like", "analyze this chart", "scan all pairs", "a... |
| `/tradecraft:mt5-integration` | MT5 integration: chart browser, EA code generation, GPU chart analysis, multi-account management, pair scanning, OHLCV data engine, indicator engine, and MQL5 development. USE FOR: mt5, metatrader, EA, expert advisor, MQL5, chart browser, multi-account, pair scanner, screener, mt5 chart, indicator, OHLCV, GPU analysis, chart image, pattern recognition. |
| `/tradecraft:mtf-confluence-scorer` | Scores multi-timeframe alignment and outputs confluence heat maps. Use this skill whenever the user asks about "multi-timeframe analysis", "MTF confluence", "timeframe alignment", "higher timeframe bias", "are timeframes aligned", "confluence score", "top-down analysis", "HTF/LTF alignment", "which timeframes agree", "heat map", or any question about whether multiple timeframes support the same directional bias. Works with mt5-chart-browser for data and trading-brain for trade decisions. |
| `/tradecraft:multi-pair-basket-trader` | Trade currency baskets instead of individual pairs — USD basket, EUR basket, risk-on basket. Use for "basket trade", "currency basket", "trade USD strength", "sell EUR basket", "multi pair trade", "basket execution", "currency index trade", or any basket-based approach. Works with synthetic-pair-constructor and pair-correlation-engine. |
| `/tradecraft:multi-strategy-orchestration` | Pipeline for running multiple trading strategies simultaneously. Signal arbitration, conflict resolution, capital allocation per strategy, risk aggregation, and regime switchover logic. The brain that coordinates all strategy agents. USE FOR: multi-strategy, strategy orchestration, signal conflict, strategy pipeline, run multiple strategies, strategy coordination, risk aggregation, portfolio heat, regime switchover, strategy agent, trading pipeline, strategy conflict resolution, how to combin... |
| `/tradecraft:news-intelligence` | Multi-source news intelligence gathering, cross-domain analysis, and skill routing for comprehensive situational awareness. Use this skill whenever the user asks "what's happening", "news today", "catch me up", "morning brief", "market news", "what's affecting gold/forex/USD", "AI news", "scan the news", "what should I know", or any request for current events awareness. Also trigger when user asks about market impact of events, cross-domain connections, or wants to understand how news in one ... |
| `/tradecraft:news-straddle-strategy` | News trading strategies — pre-news straddle, spike fade, news momentum riding, and event volatility strategies. Use for "news trading", "straddle NFP", "trade the news", "news spike", "fade the spike", "news momentum", "event trading", "FOMC trade", "NFP strategy", "high impact news trade", or any news-event-based trading strategy. Works with market-news-impact and risk-calendar-trade-filter. |
| `/tradecraft:notion-sync` | Sync trade journal entries, analysis notes, and skill outputs to Notion. Bidirectional — read watchlists from Notion, write trade logs back. |
| `/tradecraft:openalice-trading-agent` | OpenAlice — experimental file-driven autonomous AI trading agent running locally. "Your research desk, quant team, trading floor, and risk manager on your laptop 24/7." Uses "Trading-as-Git" workflow (stage → commit → push to execute). Natively integ |
| `/tradecraft:options-trading` | Full options trading: Black-Scholes pricing, Greeks, IV surface, multi-leg strategies, and option screening. USE FOR: options, black-scholes, greeks, delta, gamma, theta, vega, implied volatility, iron condor, straddle, strangle, call, put, option chain. |
| `/tradecraft:pair-analyze` | Parametric combination command that runs a full multi-skill trading analysis for any symbol. Composes regime classification, structure (ICT/SMC), liquidity, entry refinement, risk sizing, and an execution plan. USE FOR - analyze pair, analyze symbol, pair analysis, full setup, combination analysis, trade plan, what should I trade, run full analysis. |
| `/tradecraft:pair-scanner-screener` | Scan all available pairs for specific technical conditions — overbought, oversold, breakout, squeeze, divergence, pattern match. Use for "scan all pairs", "screener", "find setups", "which pairs have RSI oversold", "scan for breakouts", "find squeeze setups", "market scan", "pair filter", "setup scanner", "opportunity finder", or any multi-pair screening. Works with mt5-chart-browser for data and all strategy/indicator skills for conditions. |
| `/tradecraft:poc-bounce-strategy` | Complete Volume Profile POC (Point of Control) bounce trading strategy with level detection, confluence scoring, multi-timeframe analysis, and trade management. Use whenever the user asks about "POC bounce", "point of control", "volume profile strategy", "volume profile levels", "POC trading", "naked POC", "virgin POC", "value area bounce", "VAH VAL", "HVN LVN", "volume nodes", "session POC", "profile shape", "80% rule", "value area fill", "where did institutions trade", "fair value volume", ... |
| `/tradecraft:polymarket-prediction-agents` | AI agent framework for autonomous trading on Polymarket prediction markets. Connects LLMs to Polymarket's DEX via Gamma API, supports RAG with Chroma DB, integrates news/betting/web-search data sources. Uses py-clob-client for on-chain order executio |
| `/tradecraft:portfolio-optimization` | Modern portfolio construction: Markowitz MVO, Risk Parity, Black-Litterman, Hierarchical Risk Parity (HRP), Kelly Criterion, VaR/CVaR tail risk, and portfolio analytics. USE FOR: portfolio optimization, Markowitz, efficient frontier, risk parity, Black-Litterman, HRP, Kelly criterion, VaR, CVaR, max Sharpe, minimum variance, covariance, portfolio weights, asset allocation, tail risk, diversification. |
| `/tradecraft:price-action` | Pure price action analysis: candlestick patterns & statistics, chart pattern recognition, harmonic patterns, Elliott Wave theory, and trendline/S&R detection. USE FOR: price action trading, candlestick pattern identification, candle pattern analysis, chart pattern recognition, harmonic patterns ABCD Gartley Butterfly Bat Crab, Elliott Wave count, trendline drawing, support resistance levels, head and shoulders, double top double bottom, engulfing candle, pin bar, doji, hammer, shooting star, ... |
| `/tradecraft:quant-ml-trading` | Complete quantitative and ML-powered trading toolkit — strategy validation, genetic optimization, decay monitoring, reinforcement learning, signal aggregation, data science pipelines, and statistical/quant foundations. Use this skill for: "generate a backtest report", "create tearsheet", "equity curve", "Monte Carlo simulation", "strategy report", "performance tearsheet", "backtest results", "drawdown analysis", "strategy statistics", "risk report", "publish backtest", "PDF report", "HTML rep... |
| `/tradecraft:real-time-risk-monitor` | Real-time portfolio risk monitoring with live metrics (drawdown, exposure, correlation, VaR), configurable alert thresholds, kill switches for emergency stops, and ASCII dashboard display. Use for risk monitor, live risk, kill switch, exposure alert, real-time drawdown, or any live risk monitoring. |
| `/tradecraft:realtime-alert-pipeline` | Condition monitoring, multi-trigger alerts, and notification pipeline for trading signals. Use this skill whenever the user asks about "set an alert", "price alert", "notify me when", "trigger alert", "condition monitoring", "signal pipeline", "push notification trading", "alert system", "watchlist alerts", "multi-condition trigger", "composite alert", or any request to set up automated monitoring and alerting. Works with mt5-chart-browser for data and all analysis skills for condition genera... |
| `/tradecraft:recommendations` | Entry-point ranked-setup feed. Runs the full pair-analyze pipeline against a watchlist and returns the top N highest-grade trade setups right now, sorted by confidence × R:R, with one-line rationale and a copy-pasteable trade plan. USE FOR - what should I trade, recommend trades, best setups, top picks, ranked opportunities, where's the edge. |
| `/tradecraft:risk-and-portfolio` | Complete trading risk management, portfolio construction, performance tracking, and quantitative stress testing — all in one skill. The safety layer for all trading decisions. RISK MANAGEMENT: "risk management", "position sizing", "lot size calculation", "stop loss placement", "drawdown management", "Kelly criterion", "ATR-based sizing", "fixed percentage risk model", "risk-reward analysis", "profit factor", "expectancy", "trading psychology", "trade-psychology-coach biases", "loss aversion",... |
| `/tradecraft:risk-calendar-trade-filter` | Determines when NOT to trade by mapping event blackout zones, session quality windows, and risk filters. Use this skill whenever the user asks "should I trade today", "is it safe to trade", "any events to avoid", "blackout zones", "when not to trade", "trade filter", "event risk", "news blackout", "rollover time", "low liquidity", "end of month", "NFP week", "FOMC week", or any question about trading timing safety. This is a pre-trade safety gate that should be checked before any entry. Works... |
| `/tradecraft:risk-of-ruin` | Risk of Ruin formula, Kelly Criterion (full and fractional), Monte Carlo survival simulation, and position sizing models (fixed fractional, volatility-adjusted, fixed ratio). Use for risk of ruin, Kelly criterion, Monte Carlo, position sizing, bankroll management, or any ruin/sizing calculation. |
| `/tradecraft:session-profiler` | Statistical analysis of trading sessions — London, New York, Tokyo, and their overlaps. Use this skill whenever the user asks about "best time to trade", "session analysis", "London session", "New York session", "Tokyo session", "Asian session", "session overlap", "session open patterns", "London open", "NY open", "session statistics", "when is the market most active", "session volatility", "what session are we in", "killzone", "ICT killzone", or any question about trading session behavior, t... |
| `/tradecraft:session-scalping` | Session-based and short-term strategies: Asian session scalping, session breakouts, scalping frameworks, breakout strategies, gap trading, grid trading, end-of-day, and swing trading. Opening Range Break & Retest (ORB) — NY session M5/M1/M15 first candle strategy. USE FOR: Asian session, London session, New York session, Tokyo session, scalping, scalp trade, M1 strategy, session breakout, London breakout, Asian range breakout, NY reversal, gap trading, opening gap, gap fill, gap and go, Sunda... |
| `/tradecraft:smart-money-trap-detector` | Detect fake breakouts, stop hunts, liquidity grabs, and institutional traps. Use for "fake breakout", "trap", "stop hunt", "liquidity grab", "bull trap", "bear trap", "false break", "smart money trap", "institutional trap", "fakeout", or any trap/fake-out detection. Works with liquidity-order-flow-mapper and market-structure-bos-choch. |
| `/tradecraft:smc-beginner-pro-guide` | Smart Risk's SMC beginner-to-pro framework: 5 core concepts — market direction (mitigation-based control), liquidity (stop hunting + grab patterns), supply & demand zones (3-candle rule, 3 marking methods), order blocks (FVG-based), and top-down analysis (Weekly > Daily > 4H > 1H step-by-step with live EURUSD example). USE FOR: SMC beginner guide, smart money concepts basics, market direction mitigation, liquidity grab pattern, supply demand zone marking, order block identification, top down ... |
| `/tradecraft:social-sentiment-scraper` | Scrapes and analyzes social media sentiment from Twitter/X, Reddit, TradingView, and market sentiment indicators like Fear & Greed Index and retail positioning. Use this skill whenever the user asks about "market sentiment", "what are traders saying", "Twitter sentiment", "Reddit WallStreetBets", "retail positioning", "Fear and Greed Index", "crowd sentiment", "contrarian signal", "social media trading", "TradingView ideas", "bullish or bearish crowd", "retail long/short ratio", "IG client se... |
| `/tradecraft:spread-slippage-cost-analyzer` | Measure real execution costs, compare brokers, detect hidden fees and spread widening. Use this skill for "spread analysis", "slippage", "execution cost", "broker comparison", "hidden fees", "spread widening", "cost of trading", "true spread", "execution quality", "tick cost analysis", "best broker", or any question about trading costs. Works with mt5-chart-browser for tick data and trade-journal-performance for actual execution data. |
| `/tradecraft:statistics-timeseries` | Statistical analysis and time series modeling for trading: regime detection, probability modeling, edge validation, correlation modeling, distribution analysis, hypothesis testing, ARIMA models, stationarity testing, autocorrelation analysis. USE FOR: regime detection, edge validation, win rate analysis, expectancy, probability of profit, distribution analysis, normal distribution, fat tails, Sharpe ratio calculation, statistical significance, hypothesis testing, Monte Carlo simulation, corre... |
| `/tradecraft:strategies` | Entry-point strategy selector. Lists the available trading strategies with a one-line when-to-use for each, plus a deep-dive drill-down by name. Routes to the right specialist skill (ICT/SMC, breakout, scalping, swing, trend-following, mean-reversion). USE FOR - which strategy, what strategies, strategy selector, strategy list, how should I trade, pick a strategy, ICT or SMC, breakout or trend. |
| `/tradecraft:strategy-genetic-optimizer` | Evolutionary algorithm engine that breeds, mutates, and evolves trading strategies automatically. Use this skill whenever the user asks to "optimize strategy", "evolve parameters", "genetic algorithm", "breed strategies", "parameter optimization", "auto-optimize", "find best parameters", "evolutionary search", "mutation", "crossover", "fitness function", "population-based optimization", or any request to automatically discover optimal strategy configurations. Works with quant-trading-pipeline... |
| `/tradecraft:strategy-selection` | Meta-skill for selecting the optimal trading strategy based on current market conditions, session timing, volatility regime, and asset class. Routes to the correct strategy skill. USE FOR: which strategy to use, what setup for this market, strategy for current conditions, best approach right now, market regime detection, should I scalp or swing, trending or ranging. |
| `/tradecraft:strategy-validation` | End-to-end strategy validation — backtest tearsheet (Sharpe, Sortino, Calmar, VaR), walk-forward optimization, Monte Carlo stress testing, parameter sensitivity heatmaps, and strategy A/B testing. Use for validate strategy, backtest report, walk-forward, Monte Carlo test, parameter sensitivity, or any strategy validation. |
| `/tradecraft:synthetic-pair-constructor` | Build custom synthetic instruments from weighted pair combinations. Use this skill whenever the user asks about "synthetic pair", "basket construction", "custom index", "weighted basket", "create a currency basket", "DXY replica", "synthetic instrument", "pair basket", "composite instrument", "trade a basket", or any request to construct custom tradeable instruments from multiple pairs. Works with pair-correlation-engine and portfolio-optimizer. |
| `/tradecraft:technical-analysis` | Complete technical analysis knowledge base covering candlestick patterns, chart patterns, technical indicators, support/resistance, Fibonacci levels, pivot points, and supply/demand zones. Includes Python strategy engines for Fibonacci retracement/extension, Ichimoku cloud signals, MA ribbons, pivot point strategies, momentum/ROC, divergences (regular and hidden), Heikin-Ashi candles, Renko bricks, volume profile (POC/VAH/VAL), trend following systems, and mean reversion setups. Trigger when ... |
| `/tradecraft:telegram-bot` | Send trading alerts and psychology nudges to Telegram. Mobile notifications for trade setups, risk warnings, and trade-psychology-coach messages. |
| `/tradecraft:tensortrade-rl` | TensorTrade — composable RL framework for building and training reinforcement learning trading agents. Modular TradingEnv with Observer, ActionScheme, RewardScheme, Portfolio, Exchange components. Integrates Ray RLlib for distributed training. Python |
| `/tradecraft:tick-data-storage` | Tick data collection and storage: real-time tick capture from MT5, efficient storage formats (Parquet, HDF5), tick aggregation to OHLCV, bid/ask spread tracking. USE FOR: tick data, real-time data, live data feed, data storage, Parquet, HDF5, tick aggregation, bid ask spread, L1 data, time and sales, trade tape, high frequency data, MT5 ticks, save data, data archive, historical ticks. |
| `/tradecraft:trade-copier-signal-broadcaster` | Format and distribute trading signals to MT5 copiers, Telegram bots, Discord bots, and webhook endpoints. Use this skill whenever the user asks about "trade copier", "signal service", "broadcast signals", "Telegram trading bot", "Discord signals", "webhook alerts", "copy trading", "signal distribution", "format trade signal", "MT5 copier", "send signal to Telegram", "signal channel", or any request to distribute trading signals to external systems. Works with realtime-alert-pipeline and execu... |
| `/tradecraft:trade-journal-analytics` | Complete trade journalling system: trade logging, performance analytics, streak analysis, drawdown tracking, tag drill-down, and report generation. USE FOR: trade journal, log trade, performance report, win rate, expectancy, R-multiple, drawdown, equity curve, streak, P&L, SQN, profit factor, trade analytics, journal, session breakdown. |
| `/tradecraft:trade-psychology-coach` | Trading psychology monitoring — tilt detection, emotional state tracking, trade-psychology-coach bias alerts, discipline scoring, and behavioral pattern recognition. Use for "trading psychology", "am I tilted", "revenge trading", "emotional trading", "discipline check", "trading mindset", "fear of missing out", "FOMO", "trading emotions", "overtrading detection", "psychology check", or any trading psychology question. Works with trade-journal-performance and drawdown-playbook. |
| `/tradecraft:trading-agents-llm` | Multi-agent LLM trading framework that mirrors real-world trading firm dynamics. Specialized agents (Fundamentals, Sentiment, News, Technical analysts + Researcher debate + Trader + Risk Manager) collaborate to analyze markets and make trading decisi |
| `/tradecraft:trading-brain` | Master Trading Brain — the TOP-LEVEL orchestrator implementing the 7-layer autonomous trading architecture. This is the PRIMARY entry point for ALL trading tasks. USE THIS SKILL FIRST FOR: "analyze the market", "what should I trade", "full analysis", "trade setup", "scan the market", "brain mode", "orchestrate", "coordinate all skills", "master plan", "big picture", "run all analyses", "what's happening in markets", "EURUSD analysis", "liquidity trap", "should I go long", "entry signal", "tra... |
| `/tradecraft:trading-fundamentals` | Core trading knowledge covering market structure, order types, asset classes, timeframes, risk management, position sizing, trading psychology, and journaling. USE FOR: explain market structure, what is a market order, types of orders, limit order vs stop order, iceberg order, TWAP VWAP orders, asset classes, scalping vs day trading vs swing trading vs position trading, risk management rules, position sizing, Kelly criterion, ATR position sizing, fixed percent risk, risk reward ratio, drawdow... |
| `/tradecraft:trading-gym-rl-env` | TradingGym — OpenAI Gym-style RL trading environment toolkit for tick and OHLC data. Supports training, backtesting, and (planned) live trading via IB API. 3-action discrete space (hold/buy/sell), configurable observation window, fee-adjusted rewards |
| `/tradecraft:trading-plan-builder` | Structured pre-market routine, watchlist generation, daily preparation checklist, and trading plan templates. Use this skill for "trading plan", "pre-market routine", "daily prep", "watchlist", "what should I focus on today", "morning routine", "prepare for trading", "daily checklist", "plan my trading day", "what pairs to watch", or any trading preparation. Works with all analysis skills to auto-generate the daily plan. |
| `/tradecraft:volatility-surface-analyzer` | Implied volatility, vol smile, term structure, and vol arbitrage signal analysis. Use this skill whenever the user asks about "implied volatility", "vol smile", "volatility surface", "term structure", "vol skew", "IV rank", "IV percentile", "volatility arbitrage", "realized vs implied", "volatility cone", "variance risk premium", "vol crush", "straddle pricing", or any options/ volatility-related analysis. Works with macro-economic-dashboard for VIX context. |
| `/tradecraft:volume-analysis` | Volume Profile (POC, VAH, VAL, HVN, LVN), Order Flow & Delta analysis, and Wyckoff accumulation/distribution detection with Python engines. Use for volume profile, order flow, delta divergence, Wyckoff, POC level, or any volume-based trading analysis. |
| `/tradecraft:xtrading-analyze` | Full multi-strategy market analysis using the 6-layer autonomous trading AI. Fetches live MT5 data, generates charts, then runs the complete analysis pipeline through multi-agent system, trade-psychology-coach layer, trading brain, and super skills. USE FOR: analyze markets, market analysis, xtrading, analyze gold, analyze XAUUSD, analyze US100, analyze US30, analyze US500, run analysis, trading report, full analysis, full market scan, multi-timeframe analysis, generate trading report, check ... |
| `/tradecraft:zone-refinement-sniper-entry` | Supply & Demand zone refinement strategy for sniper entries — drop timeframes to find smaller zones inside larger zones, dramatically amplifying R:R (1.9R to 6.25R on same trade). Covers extreme zone selection, standard confirmation for non-extreme zones, the two-steps-down rule to avoid over-refinement, and multi-timeframe zone mapping. Source: JeaFx (802K views). Use this skill for "sniper entry", "zone refinement", "refine zone", "supply demand entry", "tight stop loss", "maximize risk rew... |

### AI Development

7 skill(s)

| Command | Description |
|---|---|
| `/tradecraft:agent-development` | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins. |
| `/tradecraft:ai-agent-builder` | Expert guide for building AI-powered coding agents that produce professional-quality output. Trigger whenever the user asks to build an AI agent, coding assistant, automation pipeline, tool-using LLM system, or says "agent", "agentic", "tool use", "function calling", "LLM pipeline", "AI workflow", "coding bot", or "autonomous AI". Covers agent architecture, tool design, skill loading, prompt engineering, context management, evaluation loops, and multi-step orchestration using the Claude API o... |
| `/tradecraft:few-shot-quality-prompting` | Master guide for crafting prompts that make AI models produce professional-quality code and UI consistently. Trigger whenever the user asks about prompt engineering, improving AI output quality, building system prompts, few-shot examples, making AI write better code, prompt optimization, or says "how to prompt", "better results", "improve output", "stop getting slop". Covers system prompt architecture, few-shot patterns, negative examples, chain-of-thought, output formatting, and evaluation-d... |
| `/tradecraft:mcp-integration` | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration. |
| `/tradecraft:openspec` | OpenSpec — lightweight fluid spec framework for AI-assisted development. USE FOR: "openspec", "opsx", "/opsx:propose", "propose feature", "spec before coding", "iterative spec", "brownfield spec", "AI spec framework", "change proposal", "design before implement", "fluid specs", "spec folder", "openspec init". Lighter alternative to spec-kit: no rigid phases, works on existing projects. |
| `/tradecraft:spec-kit` | GitHub Spec Kit — Spec-Driven Development with AI coding agents. Structures AI coding by creating living spec artifacts before implementation. USE FOR: "spec kit", "spec-driven", "specify init", "write a spec", "create constitution", "spec before coding", "structured AI coding", "spec driven development", "speckit", "/speckit", "constitution.md", "plan before coding", "fix AI coding", "make AI follow specs", "spec then implement", "structured prompting", "define requirements first", "tasks br... |
| `/tradecraft:transformers-js` | Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. Supports NLP (text classification, translation, summarization), computer vision (image classification, object detection), audio (speech recognition, audio classification), and multimodal tasks. Works in Node.js and browsers (with WebGPU/WASM) using pre-trained models from Hugging Face Hub. |

### Software Engineering

20 skill(s)

| Command | Description |
|---|---|
| `/tradecraft:agentic-storage` | Agentic storage architecture — persistent memory for AI agents using MCP, immutable versioning, sandboxing, and intent validation. Covers the stateless problem in LLM agents, RAG limitations (read-only), MCP protocol (JSON-RPC, resources, tools), storage safety layers, and agent file system design. Source: IBM Technology (Martin Keen), March 2026. Use this skill for "agentic storage", "agent memory", "persistent agent state", "MCP storage", "agent file system", "agent hard drive", "stateless ... |
| `/tradecraft:code-review` | Reviews code changes using CodeRabbit AI. Use when user asks for code review, PR feedback, code quality checks, security issues, or wants autonomous fix-review cycles. |
| `/tradecraft:debug-failing-test` | Debug a failing test using an iterative logging approach, then clean up and document the learning. |
| `/tradecraft:e2b-sandboxes` | E2B open-source cloud sandboxes for executing AI-generated code securely. USE FOR: run code in sandbox, e2b, code interpreter, execute AI code, secure code execution, isolated environment, AI coding agent execution, run untrusted code, cloud sandbox, code execution API, python sandbox cloud, AI agent code runner, safe code execution, jupyter sandbox. |
| `/tradecraft:elite-ui-design` | Generates production-grade, visually stunning UI code that rivals top design studios. Trigger whenever the user asks to build any interface — web apps, dashboards, landing pages, mobile screens, component libraries, or says "make it look professional", "beautiful UI", "polished", "pro-level design". Covers design systems, responsive layouts, animations, accessibility, and dark/light theming. Produces complete runnable code, never mockups or pseudocode. |
| `/tradecraft:frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics. |
| `/tradecraft:git-phase-restore` | Autonomous Git-based project phase restoration. Uses Git history (commits, tags, branches, diffs, semantic messages) to identify and restore any development phase automatically. Trigger for: "restore to when X worked", "go back to before Y broke", "show project phases", "undo the last feature", "roll back to [phase]", "find when this bug was introduced", "restore to [tag/commit/date]", "time travel", "git timeline", "diff between phases", "what changed since X", or any variation of wanting to... |
| `/tradecraft:github-actions-trigger` | Trigger GitHub Actions workflows from Claude Code. Auto-run tests, deploy, or validate when skills like run-pre-commit-checks complete. |
| `/tradecraft:httpie-cli` | HTTPie — human-friendly CLI HTTP client for APIs, debugging, testing and scripting. USE FOR: "httpie", "http cli", "api testing", "http request terminal", "curl alternative", "test API from command line", "send HTTP request", "REST client CLI", "debug API", "http post json cli", "download file cli", "http auth cli", "http session", "http proxy". |
| `/tradecraft:interactive-coding-challenges` | 120+ interactive coding challenges in Jupyter Notebooks covering data structures, algorithms, system design and OOP for interview prep. USE FOR: coding challenges, algorithm practice, data structures interview, leetcode style problems, DSA practice, array problems, linked list, graph algorithms, dynamic programming, sorting algorithms, bit manipulation, system design interview, OOP design, big-O complexity, technical interview prep. |
| `/tradecraft:ip-rotation` | Rotate IP addresses when sessions are rate-limited or blocked by YouTube or other services. USE FOR: ip rotation, rate limit, proxy, tor, blocked, 429 error, youtube block. |
| `/tradecraft:playground` | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic. |
| `/tradecraft:pro-code-architecture` | Produces senior-engineer-level code architecture across any language or platform. Trigger whenever the user asks to build a feature, module, service, or full app — or says "clean code", "scalable", "production-grade", "professional architecture", "refactor", or "best practices". Covers SOLID, design patterns, error handling, testing strategy, API design, and modular composition. Enforces clean boundaries, type safety, and separation of concerns. Works across Python, Kotlin, TypeScript, and an... |
| `/tradecraft:programmatic-drawing` | Expert skill for generating visual art, diagrams, illustrations, charts, and drawings programmatically using SVG, HTML Canvas, p5.js, Three.js, Mermaid, and D3. Trigger whenever the user asks to draw, illustrate, visualize, diagram, create art, generate graphics, make a flowchart, render shapes, animate visuals, create infographics, or produce any kind of visual output through code. Also trigger for data visualization, generative art, interactive graphics, and technical diagrams. |
| `/tradecraft:python-manager-discovery` | Environment manager-specific discovery patterns and known issues. Use when working on or reviewing environment discovery code for conda, poetry, pipenv, pyenv, or venv. |
| `/tradecraft:run-e2e-tests` | Run E2E tests to verify complete user workflows like environment discovery, creation, and selection. Use this before releases or after major changes. |
| `/tradecraft:run-integration-tests` | Run integration tests to verify that extension components work together correctly. Use this after modifying component interactions or event handling. |
| `/tradecraft:run-pre-commit-checks` | Run the mandatory pre-commit checks before committing code. Includes lint, type checking, and unit tests. MUST be run before every commit. |
| `/tradecraft:run-smoke-tests` | Run smoke tests to verify extension functionality in a real VS Code environment. Use this when checking if basic features work after changes. |
| `/tradecraft:system-design-academy` | Real-world system design case studies from 40+ major tech companies + 114 concepts. USE FOR: system design, design Twitter, design YouTube, design Uber, design Netflix, design WhatsApp, design Slack, design Instagram, URL shortener, payment system, distributed systems, scalability, microservices, caching patterns, consistent hashing, rate limiting, system design interview, architecture patterns, database scaling. |

### Claude Code Platform

20 skill(s)

| Command | Description |
|---|---|
| `/tradecraft:claude-automation-recommender` | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use. |
| `/tradecraft:claude-md-improver` | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates. Also use when the user mentions "CLAUDE.md maintenance" or "project memory optimization". |
| `/tradecraft:command-development` | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code. |
| `/tradecraft:context-memory` | Persist and recall state between skill invocations. Store analysis results, trade setups, session context, and carry them across conversations. |
| `/tradecraft:generate-snapshot` | Generate a codebase health snapshot for technical debt tracking and planning. Analyzes git history, code complexity, debt markers, and dependencies to identify hotspots and refactoring priorities. |
| `/tradecraft:hook-development` | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks", "use ${CLAUDE_PLUGIN_ROOT}", "set up event-driven automation", "block dangerous commands", or mentions hook events (PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification). Provides comprehensive guidance for creating and implementing Claude Code plugin hooks with focus on adva... |
| `/tradecraft:plugin-settings` | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state files", "read YAML frontmatter", "per-project plugin settings", or wants to make plugin behavior configurable. Documents the .claude/plugin-name.local.md pattern for storing plugin-specific configuration with YAML frontmatter and markdown content. |
| `/tradecraft:plugin-structure` | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plugin.json", "use ${CLAUDE_PLUGIN_ROOT}", "add commands/agents/skills/hooks", "configure auto-discovery", or needs guidance on plugin directory layout, manifest configuration, component organization, file naming conventions, or Claude Code plugin architecture best practices. |
| `/tradecraft:search` | Entry-point skill discovery. Given a keyword or task description, returns the shortest list of Tradecraft skills that match, with direct invocation recipes. No keyword = show the 5 main entry points. USE FOR - find skill, which skill, how do I, search skills, list skills, what can this do, find command. |
| `/tradecraft:skill-analytics` | Track which skills you use most, success rates, token usage, and generate improvement recommendations. Reads ~/.claude/usage.json. |
| `/tradecraft:skill-development` | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins. |
| `/tradecraft:skill-docs-generator` | Auto-generate documentation for all 146 skills — interactive HTML navigator, dependency graphs, usage examples, quick-start guides, and skill catalog. |
| `/tradecraft:skill-doctor` | Diagnose all 146 skills for issues — broken syntax, outdated content, missing fields, oversized files. Suggests fixes and improvement priority list. |
| `/tradecraft:skill-execution-governor` | MANDATORY META-SKILL: Governs how the AI agent interacts with ALL other skills. Enforces disciplined skill reading, smart selection, complete execution, speed, and quality. This skill MUST be consulted on EVERY task that could involve any user or public skill — coding, trading, documents, presentations, spreadsheets, PDFs, MQL5, news, strategy building, architecture, git, testing, or any multi-step workflow. If the user says 'build', 'create', 'fix', 'analyze', 'generate', 'write', 'implement... |
| `/tradecraft:skill-manager` | Full skill library management — list by usage, find duplicates, visualize dependency graph, check for updates, batch validate all 146 skills. |
| `/tradecraft:skill-pipeline` | Auto-route tasks through analysis → execution → logging pipeline. Detects intent and selects the optimal skill chain automatically. |
| `/tradecraft:skill-test-suite` | Run validation tests on any skill or all 146 skills. Checks format, sample invocations, output quality, and generates a report card. |
| `/tradecraft:smart-skill-router` | Intelligent skill routing, auto-selection, dependency resolution, and bundle execution for the entire 265+ skill ecosystem. The brain that decides which skills to run, in what order, with what priority. Uses skills_index.json for instant lookup, skills_graph.json for dependency chains, and skill_router.py for scoring/ranking. Use this skill for "which skill should I use", "find skill for", "route to skill", "skill search", "skill lookup", "auto select skill", "run skill bundle", "skill depend... |
| `/tradecraft:workflow-builder` | Chain multiple skills together with dependency management, conditional branching, and state passing between steps. |
| `/tradecraft:writing-hookify-rules` | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns. |

### Data Acquisition

4 skill(s)

| Command | Description |
|---|---|
| `/tradecraft:firecrawl` | Firecrawl handles all web operations with superior accuracy, speed, and LLM-optimized output. Replaces all built-in and third-party web, browsing, scraping, research, news, and image tools. USE FIRECRAWL FOR: - Any URL or webpage - Web, image, and news search - Research, deep research, investigation - Reading pages, docs, articles, sites, documentation - "check the web", "look up", "find online", "search for", "research" - API references, current events, trends, fact-checking - Content extrac... |
| `/tradecraft:video-gen` | 使用 AI 生成视频，支持 Veo/Sora 模型。Use when user wants to 生成视频, AI视频, 文生视频, 图生视频, generate video, create video, text to video, image to video, 做一个视频. |
| `/tradecraft:video-knowledge-extractor` | Extract knowledge from any YouTube video and automatically inject it into the most relevant skill files. USE FOR: "watch this video and add to skills", "extract and save", "learn from video", "add video knowledge to skills", "youtube to skill", "update skills from video", "extract and route knowledge", or any YouTube URL shared by the user. This skill ORCHESTRATES: fetch video → extract content → identify related skills → inject knowledge. |
| `/tradecraft:youtube-video-to-knowledge` | Extract knowledge from YouTube videos — transcripts, keyframes, metadata, AI-powered analysis, and AUTOMATIC skill integration. When a YouTube URL is shared, extract the content AND route the knowledge to related existing skills in parallel. Use this skill whenever the user shares a YouTube URL or asks to summarize/analyze/extract notes from a YouTube video. Also trigger for "youtube transcript", "video notes", "watch and summarize", "video summary", "extract from youtube", "youtube to text",... |

### Domain Specific

2 skill(s)

| Command | Description |
|---|---|
| `/tradecraft:featool-multiphysics` | FEATool Multiphysics — physics simulation platform for FEA/CFD modeling. Covers finite element analysis, computational fluid dynamics, heat transfer, structural mechanics, electromagnetics, and custom PDEs. Integrates with OpenFOAM, FEniCS, SU2. Scri |
| `/tradecraft:stripe-best-practices` | Best practices for building Stripe integrations. Use when implementing payment processing, checkout flows, subscriptions, webhooks, Connect platforms, or any Stripe API integration. |

### Uncategorized

12 skill(s)

| Command | Description |
|---|---|
| `/tradecraft:autohedge-swarm` | _(no description)_ |
| `/tradecraft:brain-ecosystem-mcp` | _(no description)_ |
| `/tradecraft:build-your-own-x` | _(no description)_ |
| `/tradecraft:cow-protocol-sdk` | _(no description)_ |
| `/tradecraft:deepagents-langchain` | _(no description)_ |
| `/tradecraft:fundamental-analysis` | _(no description)_ |
| `/tradecraft:gitnexus-codebase-intelligence` | _(no description)_ |
| `/tradecraft:hedgequantx-prop-trading` | _(no description)_ |
| `/tradecraft:ritmex-crypto-agent` | _(no description)_ |
| `/tradecraft:smc-python-library` | _(no description)_ |
| `/tradecraft:stocksight-sentiment` | _(no description)_ |
| `/tradecraft:trading-autopilot` | _(no description)_ |

## Notes

12 skill file(s) have incomplete or malformed YAML frontmatter. They currently show under *Uncategorized* above; their descriptions may be blank until the frontmatter is fixed.
