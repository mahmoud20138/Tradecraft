# Data Model: Auto-Trading AI Agent System

## Entity Relationship Diagram

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│  MarketData │───▶│    OHLCV     │───▶│  Indicator  │    │  Regime     │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
       │                   │                                     │
       │                   ▼                                     ▼
       │            ┌──────────────┐                      ┌─────────────┐
       └───────────▶│   Strategy   │◀─────────────────────│   Signal    │
                    └──────────────┘                      └─────────────┘
                           │                                     │
                           ▼                                     ▼
                    ┌──────────────┐                      ┌─────────────┐
                    │SignalAggreg. │─── VALIDATED ───────▶│ RiskFilter  │
                    └──────────────┘                      └─────────────┘
                                                              │
                                                              ▼
                                                       ┌─────────────┐
                                                       │    Trade    │
                                                       └─────────────┘
                                                              │
                                         ┌────────────────────┼────────────────┐
                                         ▼                    ▼                ▼
                                  ┌─────────────┐    ┌─────────────┐  ┌───────────┐
                                  │  Position   │    │ TradeLog    │  │  PnL      │
                                  └─────────────┘    └─────────────┘  └───────────┘
```

## Core Entities

### 1. MarketData (Tick)

```python
@dataclass
class Tick:
    """Single price tick from market"""
    symbol: str
    timestamp: datetime
    bid: float
    ask: float
    volume: int

    # Redis TTL: 60 seconds (hot data only)
    # PostgreSQL: Append-only for historical analysis
```

**Schema (PostgreSQL):**
```sql
CREATE TABLE ticks (
    id BIGSERIAL PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    timestamp TIMESTAMPTZ NOT NULL,
    bid DECIMAL(18,8) NOT NULL,
    ask DECIMAL(18,8) NOT NULL,
    volume INTEGER NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_ticks_symbol_time ON ticks(symbol, timestamp DESC);
```

### 2. OHLCV Bar

```python
@dataclass
class OHLCVBar:
    """Open-High-Low-Close-Volume bar"""
    symbol: str
    timeframe: str  # 'M1', 'M5', 'M15', 'M30', 'H1', 'H4', 'D1', 'W1', 'MN1'
    open_time: datetime
    close_time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

    # Redis: Cached for common timeframes (1-hour TTL)
    # PostgreSQL: Permanent storage
```

**Schema (PostgreSQL):**
```sql
CREATE TABLE ohlcv_bars (
    id BIGSERIAL PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    timeframe VARCHAR(5) NOT NULL,
    open_time TIMESTAMPTZ NOT NULL,
    close_time TIMESTAMPTZ NOT NULL,
    open DECIMAL(18,8) NOT NULL,
    high DECIMAL(18,8) NOT NULL,
    low DECIMAL(18,8) NOT NULL,
    close DECIMAL(18,8) NOT NULL,
    volume BIGINT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(symbol, timeframe, open_time)
);

CREATE INDEX idx_ohlcv_symbol_tf_time ON ohlcv_bars(symbol, timeframe, open_time DESC);
```

### 3. MarketState

```python
@dataclass
class MarketState:
    """Complete snapshot of market conditions at a point in time"""
    timestamp: datetime
    symbol: str
    bid: float
    ask: float
    spread: float
    mid_price: float

    # Regime classification
    regime: RegimeType  # Enum: TRENDING, RANGING, VOLATILE
    regime_confidence: float  # 0.0 to 1.0

    # Volatility metrics
    atr: float  # Average True Range
    volatility_percent: float  # ATR as % of price

    # Technical indicators (latest values)
    rsi: Optional[float] = None
    macd: Optional[float] = None
    macd_signal: Optional[float] = None
    bb_upper: Optional[float] = None
    bb_middle: Optional[float] = None
    bb_lower: Optional[float] = None

    # Liquidity assessment
    liquidity_score: float  # 0.0 to 1.0
    spread_pips: float

    # Risk assessment
    news_risk: NewsRiskLevel  # Enum: NONE, LOW, MEDIUM, HIGH
    session_active: bool  # Is trading session active?

    # Event metadata
    event_id: str  # Correlation ID for this state
```

**RegimeType Enum:**
```python
class RegimeType(Enum):
    TRENDING = "trending"      # Strong directional movement
    RANGING = "ranging"        # Sideways, bounded
    VOLATILE = "volatile"      # High volatility, choppy
```

### 3b. SkillInvocation (Agent Transparency Log)

```python
@dataclass
class SkillInvocation:
    """Logged for EVERY skill call — full agent transparency"""
    id: str  # UUID
    timestamp: datetime
    agent_name: str          # HEAD_TRADER, WORLD_INTEL, TECHNICIAN, STRATEGIST, RISK_OFFICER, EXECUTOR, DEVILS_ADVOCATE, MODE_SELECTOR
    skill_name: str          # e.g. "technical-analysis"
    input_summary: str       # e.g. "XAUUSD H1 last 200 bars"
    output_summary: str      # e.g. "RSI=72, MACD bearish cross, regime=TRENDING"
    confidence: float        # Agent's confidence in this output (0.0–1.0)
    duration_ms: int         # How long the skill took
    mode_context: str        # BULLET / BLITZ / RAPID / SHARED
    trade_setup_id: Optional[str] = None  # Links to a proposed trade setup
```

### 3c. AgentVote (Trade Decision Audit)

```python
class AgentVoteType(Enum):
    AGREE = "agree"
    DISAGREE = "disagree"
    ABSTAIN = "abstain"

@dataclass
class AgentVote:
    """Each agent's vote on a proposed trade — visible collaboration"""
    trade_setup_id: str
    agent_name: str
    vote: AgentVoteType
    reasoning: str           # Why this agent voted this way
    skills_consulted: list[str]  # Which skills informed the vote
    confidence: float
    timestamp: datetime

@dataclass
class TradeDecision:
    """Final decision after all agents vote"""
    trade_setup_id: str
    votes: list[AgentVote]   # All 5 specialist votes
    agree_count: int         # How many agreed
    devils_advocate_overruled: bool  # Was Devil's Advocate overruled?
    head_trader_decision: str  # EXECUTE / PASS / HALF_SIZE
    mode: str                # BULLET / BLITZ / RAPID
    timestamp: datetime

class TradingIntensity(Enum):
    BULLET = "bullet"    # Tick/M1, 1-60s hold, 0.5-3 pip TP
    BLITZ = "blitz"      # M1/M5, 30s-15min hold, 3-15 pip TP
    RAPID = "rapid"      # M15+, 15min-4h+ hold, 15-100+ pip TP
```

### 4. TradingSignal

```python
@dataclass
class TradingSignal:
    """Generated trading signal from a strategy"""
    id: str  # UUID
    timestamp: datetime
    symbol: str

    # Signal source
    strategy_name: str
    strategy_version: str

    # Signal details
    direction: Direction  # Enum: LONG, SHORT
    entry_price: float
    stop_loss: float
    take_profit: float

    # Signal metadata
    confidence: float  # 0.0 to 1.0
    regime_required: RegimeType  # Regime this signal works in
    timeframe: str  # Timeframe used for analysis

    # Rationale
    rationale: str  # Human-readable explanation
    conditions_met: List[str]  # Conditions that triggered signal

    # Lifecycle
    status: SignalStatus  # Enum: PENDING, VALIDATED, REJECTED, EXPIRED, FILLED
    created_at: datetime
    validated_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None  # Signal expiration time

    # Game mode (Bullet/Blitz/Rapid — None if non-mode-specific strategy)
    intensity_mode: Optional[TradingIntensity] = None

    # Linked entities
    trade_id: Optional[str] = None  # If this signal became a trade
```

**Schema (PostgreSQL):**
```sql
CREATE TYPE direction_enum AS ENUM ('LONG', 'SHORT');
CREATE TYPE signal_status_enum AS ENUM ('PENDING', 'VALIDATED', 'REJECTED', 'EXPIRED', 'FILLED');

CREATE TABLE signals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    strategy_name VARCHAR(100) NOT NULL,
    strategy_version VARCHAR(20) NOT NULL,
    direction direction_enum NOT NULL,
    entry_price DECIMAL(18,8) NOT NULL,
    stop_loss DECIMAL(18,8) NOT NULL,
    take_profit DECIMAL(18,8) NOT NULL,
    confidence DECIMAL(5,4) NOT NULL,
    regime_required VARCHAR(20) NOT NULL,
    timeframe VARCHAR(5) NOT NULL,
    rationale TEXT NOT NULL,
    conditions_met JSONB,
    status signal_status_enum DEFAULT 'PENDING',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    validated_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    trade_id UUID,
    intensity_mode VARCHAR(20)
);

CREATE INDEX idx_signals_symbol_status ON signals(symbol, status);
CREATE INDEX idx_signals_created ON signals(created_at DESC);
```

### 5. Trade

```python
@dataclass
class Trade:
    """Executed trade (filled order)"""
    id: str  # UUID
    signal_id: str  # Originating signal

    # Trade details
    symbol: str
    direction: Direction
    entry_price: float
    quantity: float  # Position size in lots/units

    # Risk levels
    stop_loss: float
    take_profit: float
    risk_amount: float  # Dollar amount at risk
    risk_percent: float  # % of account equity

    # Timestamps
    submitted_at: datetime
    filled_at: datetime
    exit_price: Optional[float] = None
    exited_at: Optional[datetime] = None

    # Status
    status: TradeStatus  # Enum: PENDING, OPEN, CLOSED, CANCELLED

    # P&L
    entry_value: float  # Total position value at entry
    exit_value: Optional[float] = None
    pnl: Optional[float] = None  # Realized P&L
    pnl_percent: Optional[float] = None

    # Exit reason
    exit_reason: Optional[ExitReason] = None  # Enum: SL, TP, MANUAL, SIGNAL, EXPIRY

    # Metadata
    broker_order_id: Optional[str] = None
    commission: float = 0.0
    swap: float = 0.0
```

**Schema (PostgreSQL):**
```sql
CREATE TYPE trade_status_enum AS ENUM ('PENDING', 'OPEN', 'CLOSED', 'CANCELLED');
CREATE TYPE exit_reason_enum AS ENUM ('SL', 'TP', 'MANUAL', 'SIGNAL', 'EXPIRY');

CREATE TABLE trades (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    signal_id UUID NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    direction direction_enum NOT NULL,
    entry_price DECIMAL(18,8) NOT NULL,
    quantity DECIMAL(18,8) NOT NULL,
    stop_loss DECIMAL(18,8) NOT NULL,
    take_profit DECIMAL(18,8) NOT NULL,
    risk_amount DECIMAL(18,2) NOT NULL,
    risk_percent DECIMAL(5,2) NOT NULL,
    submitted_at TIMESTAMPTZ NOT NULL,
    filled_at TIMESTAMPTZ NOT NULL,
    exit_price DECIMAL(18,8),
    exited_at TIMESTAMPTZ,
    status trade_status_enum DEFAULT 'PENDING',
    entry_value DECIMAL(18,2) NOT NULL,
    exit_value DECIMAL(18,2),
    pnl DECIMAL(18,2),
    pnl_percent DECIMAL(8,4),
    exit_reason exit_reason_enum,
    broker_order_id VARCHAR(100),
    commission DECIMAL(18,2) DEFAULT 0,
    swap DECIMAL(18,2) DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_trades_symbol_status ON trades(symbol, status);
CREATE INDEX idx_trades_filled ON trades(filled_at DESC);
```

### 6. Position

```python
@dataclass
class Position:
    """Current open position (runtime state, not persisted)"""
    trade_id: str
    symbol: str
    direction: Direction
    quantity: float
    entry_price: float
    current_price: float

    # P&L (unrealized)
    unrealized_pnl: float
    unrealized_pnl_percent: float

    # Risk levels
    stop_loss: float
    take_profit: float

    # Duration
    entry_time: datetime
    duration: timedelta

    # Progress toward targets
    sl_distance_pips: float
    tp_distance_pips: float
    progress_percent: float  # 0% at entry, 100% at TP
```

**Note:** Positions are runtime state stored in Redis, not PostgreSQL.

### 7. Portfolio

```python
@dataclass
class Portfolio:
    """Overall portfolio state"""
    timestamp: datetime
    account_id: str

    # Account balances
    balance: float  # Current balance
    equity: float   # Balance + unrealized P&L
    margin: float   # Used margin
    free_margin: float
    margin_level: float  # %

    # Position summary
    open_positions: int
    long_exposure: float
    short_exposure: float
    net_exposure: float

    # Risk metrics
    total_risk: float  # Total amount at risk across all positions
    total_risk_percent: float  # % of account equity
    max_drawdown: float  # Current drawdown from peak
    peak_equity: float  # High water mark

    # Session stats
    session_trades: int
    session_pnl: float
    session_win_rate: float
```

**Redis Key Structure:**
```
portfolio:{account_id}:state → JSON serialized Portfolio
portfolio:{account_id}:positions → Hash of trade_id → Position
portfolio:{account_id}:signals → List of active signal IDs
```

### 8. StrategyConfig

```python
@dataclass
class StrategyConfig:
    """Configuration for a trading strategy"""
    name: str
    version: str
    enabled: bool

    # Regime filter
    allowed_regimes: List[RegimeType]

    # Risk parameters
    max_risk_per_trade: float  # % of account
    min_rr_ratio: float  # Min risk:reward (e.g., 1:2)

    # Signal parameters
    min_confidence: float  # Minimum confidence to trade
    signal_expiry_minutes: int  # How long signal is valid

    # Position limits
    max_positions_per_symbol: int
    max_total_positions: int

    # Strategy-specific parameters
    parameters: Dict[str, Any]  # Custom params per strategy
```

### 9. TradingIntensityConfig

```python
# TradingIntensity enum is defined in section 3c above (BULLET, BLITZ, RAPID)
# ScalpingIntensity is DEPRECATED — use TradingIntensity instead

@dataclass
class TradingIntensityConfig:
    """Configuration for a game mode (Bullet/Blitz/Rapid)"""
    mode: TradingIntensity
    enabled: bool

    # Timeframe
    analysis_tf: str       # e.g. 'M5' for SCALPING, 'M1' for MICRO, 'tick' for NANO/ULTRA
    entry_tf: str          # e.g. 'M1' for SCALPING, 'tick' for NANO/ULTRA

    # Hold duration
    min_hold_seconds: int  # Minimum hold time
    max_hold_seconds: int  # Auto-close if exceeded

    # Targets (in pips)
    tp_min: float          # Minimum take-profit
    tp_max: float          # Maximum take-profit
    sl_pips: float         # Fixed stop-loss distance

    # Risk (TP/SL define the mode; risk % is user-configurable in settings, NOT per mode)
    max_concurrent: int      # Max open positions for this mode

    # Spread guard
    max_spread_ratio: float  # Reject if spread > tp_min * this ratio (default 0.3)
    spread_pause_threshold: float  # Pause mode if spread exceeds this (pips)

    # Cooldown
    cooldown_seconds: int  # Min time between trades

    # Session filter
    allowed_sessions: List[str]  # e.g. ['london', 'ny', 'london_ny_overlap']
    session_hours_utc: Optional[str]  # e.g. '13:00-16:00' for BULLET

# Default configurations — 3 game modes
INTENSITY_MODES = {
    TradingIntensity.BULLET: TradingIntensityConfig(
        mode=TradingIntensity.BULLET, enabled=True,
        analysis_tf='M1', entry_tf='tick',
        min_hold_seconds=1, max_hold_seconds=60,
        tp_min=0.5, tp_max=3.0, sl_pips=2.0,
        max_concurrent=2,
        max_spread_ratio=0.3, spread_pause_threshold=1.5,
        cooldown_seconds=5,
        allowed_sessions=['london_ny_overlap'], session_hours_utc='13:00-16:00',
    ),
    TradingIntensity.BLITZ: TradingIntensityConfig(
        mode=TradingIntensity.BLITZ, enabled=True,
        analysis_tf='M5', entry_tf='M1',
        min_hold_seconds=30, max_hold_seconds=900,
        tp_min=3.0, tp_max=15.0, sl_pips=5.0,
        max_concurrent=3,
        max_spread_ratio=0.3, spread_pause_threshold=3.0,
        cooldown_seconds=15,
        allowed_sessions=['london', 'ny'], session_hours_utc=None,
    ),
    TradingIntensity.RAPID: TradingIntensityConfig(
        mode=TradingIntensity.RAPID, enabled=True,
        analysis_tf='H1', entry_tf='M15',
        min_hold_seconds=900, max_hold_seconds=14400,
        tp_min=15.0, tp_max=100.0, sl_pips=30.0,
        max_concurrent=5,
        max_spread_ratio=0.3, spread_pause_threshold=5.0,
        cooldown_seconds=60,
        allowed_sessions=['all'], session_hours_utc=None,
    ),
}
```

### 10. ConfluenceResult

```python
@dataclass
class ConfluenceResult:
    """Output of the weighted linear confluence scorer"""
    score: float  # 0.0–1.0 weighted sum
    take_trade: bool  # score >= 0.60
    position_size_multiplier: float  # 0.0, 0.25–1.0 based on score

    # Factor breakdown (for journaling/debugging)
    factor_contributions: Dict[str, Dict]  # {factor: {signal, weight, contribution}}

    # Gate results
    gates_passed: bool  # news_clear >= 0.5 AND spread_normal >= 0.5
    gate_details: Dict[str, bool]  # {gate_name: passed}

# Confluence weights (configurable, sum to 1.0)
CONFLUENCE_WEIGHTS = {
    'htf_trend':        0.20,  # Strongest predictor
    'regime_match':     0.15,
    'mtf_agreement':    0.12,
    'sr_proximity':     0.12,
    'volume_confirm':   0.10,
    'momentum_align':   0.08,
    'news_clear':       0.08,  # HARD GATE
    'session_quality':  0.05,
    'spread_normal':    0.05,  # HARD GATE
    'no_losing_streak': 0.05,
}

# Thresholds
MIN_CONFLUENCE = 0.60   # Below = no trade
SINGLE_STRATEGY_MIN_CONFLUENCE = 0.70  # Min for single-strategy trades (also needs confidence > 0.85)
FULL_SIZE_CONFLUENCE = 0.80  # Above = full position

# Game mode confluence weight overrides (faster modes de-weight HTF, boost momentum/spread)
INTENSITY_CONFLUENCE_WEIGHTS = {
    TradingIntensity.BULLET: {
        'htf_trend': 0.03, 'regime_match': 0.08, 'mtf_agreement': 0.02,
        'sr_proximity': 0.12, 'volume_confirm': 0.20, 'momentum_align': 0.28,
        'news_clear': 0.08, 'session_quality': 0.04, 'spread_normal': 0.12, 'no_losing_streak': 0.03,
    },
    TradingIntensity.BLITZ: {
        'htf_trend': 0.10, 'regime_match': 0.15, 'mtf_agreement': 0.08,
        'sr_proximity': 0.14, 'volume_confirm': 0.14, 'momentum_align': 0.14,
        'news_clear': 0.08, 'session_quality': 0.05, 'spread_normal': 0.07, 'no_losing_streak': 0.05,
    },
    TradingIntensity.RAPID: CONFLUENCE_WEIGHTS,  # Same as default (HTF-dominant)
}
```

### 10. AccountInfo (MT5 Bridge)

```python
@dataclass
class AccountInfo:
    """Account state from MT5 Bridge (GET /account)"""
    balance: float
    equity: float
    margin: float
    free_margin: float
    margin_level: float  # %
    currency: str  # e.g. 'USD'
    leverage: int
    server: str
    trade_allowed: bool
    timestamp: datetime
```

### 10. OrderRequest / OrderResult (MT5 Bridge)

```python
@dataclass
class OrderRequest:
    """Order submission to MT5 Bridge (POST /order)"""
    symbol: str
    direction: Direction  # LONG / SHORT
    order_type: str  # 'MARKET', 'LIMIT', 'STOP'
    volume: float  # Lot size
    price: Optional[float] = None  # Required for LIMIT/STOP
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    deviation: int = 20  # Max slippage in points
    magic: int = 0  # EA magic number for identification
    comment: str = ""

@dataclass
class OrderResult:
    """Order execution result from MT5 Bridge"""
    success: bool
    order_id: int  # MT5 order ticket
    volume: float  # Filled volume
    price: float  # Fill price
    bid: float
    ask: float
    comment: str
    request_id: int
    retcode: int  # MT5 return code
    retcode_description: str
    timestamp: datetime
```

### 11. CloseResult (MT5 Bridge)

```python
@dataclass
class CloseResult:
    """Position close result from MT5 Bridge (DELETE /position/{ticket})"""
    success: bool
    ticket: int  # Position ticket that was closed
    volume: float  # Closed volume
    price: float  # Close price
    pnl: float  # Realized P&L
    commission: float
    swap: float
    retcode: int
    retcode_description: str
    timestamp: datetime
```

---

## Data Flow

### Redis (Hot State)

| Key Pattern | Type | TTL | Purpose |
|-------------|------|-----|---------|
| `market:{symbol}:tick` | Hash | 60s | Latest tick |
| `market:{symbol}:state` | JSON | 300s | Current market state |
| `signals:pending` | List | - | Pending signals queue |
| `signal:{id}` | Hash | 1h | Signal details |
| `portfolio:state` | JSON | - | Portfolio snapshot |
| `trade:{id}` | Hash | - | Open trade state |
| `regime:{symbol}` | String | 3600s | Current regime |

### PostgreSQL (Cold Storage)

| Table | Retention | Purpose |
|-------|-----------|---------|
| `ticks` | 7 days | Raw data (compressed after) |
| `ohlcv_bars` | Permanent | Historical bars |
| `signals` | Permanent | Signal audit trail |
| `trades` | Permanent | Trade history |
| `system_events` | 90 days | System event log |
| `performance_metrics` | Permanent | Daily/hourly stats |

## Migration Strategy

| Phase | Action |
|-------|--------|
| 1 | Create all tables with indexes |
| 2 | Set up Redis connection pool |
| 3 | Implement state sync (Redis ← → PostgreSQL) |
| 4 | Add partitioning for `ticks` (daily) |
| 5 | Set up retention jobs (pg_cron) |

---

**Data Model Status:** Scalping modes added
**Version:** 4.0
**Date:** 2026-03-19
**Changes v4.0:**
- TradingIntensity enum (BULLET, BLITZ, RAPID) replaces ScalpingIntensity
- IntensityModeConfig dataclass (renamed from ScalpingModeConfig)
- INTENSITY_MODES default configurations dict (3 modes)
**Prior (v3.0):** ConfluenceResult, weights, thresholds
