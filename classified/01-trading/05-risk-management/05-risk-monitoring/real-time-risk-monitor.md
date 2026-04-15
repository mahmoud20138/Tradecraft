---
id: real-time-risk-monitor
name: real-time-risk-monitor
description: "Real-time portfolio risk monitoring with live metrics (drawdown, exposure, correlation, VaR), configurable alert thresholds, kill switches for emergency stops, and ASCII dashboard display. Use for risk monitor, live risk, kill switch, exposure alert, real-time drawdown, or any live risk monitoring."
title: "Real-Time Risk Monitor"
domain: trading/risk-and-portfolio
level: expert
version: 1
depends_on: [drawdown-playbook, correlation-crisis, trading-brain]
unlocks: [multi-strategy-orchestration]
tags: [monitoring, real-time, alerts, kill-switch, exposure, live]
status: active
created: "2025-01-15"
updated: "2025-01-15"
context_cost: medium
load_priority: 0.75
kind: tool
category: trading/risk
---
> **Skill:** Real-Time Risk Monitor  |  **Domain:** trading/risk-and-portfolio  |  **Category:** risk  |  **Level:** expert
> **Tags:** `monitoring`, `real-time`, `alerts`, `kill-switch`, `exposure`, `live`

# Real-Time Risk Monitor

## 1. Architecture
```
┌─────────────────────────────────────────────┐
│ RISK MONITOR                                │
├─────────────────────────────────────────────┤
│                                             │
│ Data Layer                                  │
│ ├── MT5 account state (positions, balance)  │
│ ├── Market data feed (prices, spreads)      │
│ ├── Volatility feed (VIX, ATR)             │
│ └── Correlation matrix (rolling)            │
│                                             │
│ Computation Layer                           │
│ ├── Real-time P&L per position             │
│ ├── Portfolio exposure by:                  │
│ │   ├── Asset class                         │
│ │   ├── Direction (net long/short)          │
│ │   ├── Correlation cluster                 │
│ │   └── Strategy                            │
│ ├── Drawdown tracker (peak-to-current)     │
│ ├── Daily/weekly/monthly P&L vs limits     │
│ └── Margin utilization                      │
│                                             │
│ Alert Layer                                 │
│ ├── Threshold alerts (configurable)        │
│ ├── Anomaly detection (unusual patterns)   │
│ └── Kill switches (automated position exit) │
│                                             │
│ Output Layer                                │
│ ├── Dashboard (real-time display)          │
│ ├── Notifications (Telegram/email/SMS)     │
│ └── Logging (all state changes)            │
│                                             │
└─────────────────────────────────────────────┘
```

## 2. Core Metrics (Real-Time)

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class RiskSnapshot:
    timestamp: datetime

    # Account
    balance: float
    equity: float
    margin_used: float
    free_margin: float
    margin_level_pct: float  # equity / margin × 100

    # Exposure
    num_open_positions: int
    total_exposure_usd: float
    net_direction: float       # +1 = fully long, -1 = fully short
    gross_exposure_pct: float  # total_exposure / equity

    # P&L
    unrealized_pnl: float
    realized_pnl_today: float
    realized_pnl_week: float
    realized_pnl_month: float

    # Drawdown
    equity_peak: float
    current_drawdown_pct: float  # (peak - equity) / peak
    drawdown_duration_hours: float
    drawdown_level: int  # 0=normal, 1=caution, 2=warning, 3=critical, 4=emergency

    # Risk
    total_risk_pct: float      # sum of all position risk / equity
    largest_position_risk_pct: float
    correlation_cluster_risk: float

    # Volatility context
    current_vix: float
    avg_position_atr_pct: float

class RiskMonitor:
    def __init__(self, config: RiskConfig):
        self.config = config
        self.peak_equity = config.starting_balance
        self.alerts_sent: list[Alert] = []

    def compute_snapshot(self, account, positions, market_data) -> RiskSnapshot:
        equity = account.equity

        # Track peak
        if equity > self.peak_equity:
            self.peak_equity = equity

        dd_pct = (self.peak_equity - equity) / self.peak_equity

        # Compute exposure
        total_exposure = sum(abs(p.volume * p.current_price) for p in positions)
        net_exposure = sum(
            p.volume * p.current_price * (1 if p.type == 'buy' else -1)
            for p in positions
        )

        # Compute total risk
        total_risk = sum(
            abs(p.current_price - p.sl) * p.volume / equity
            for p in positions if p.sl
        )

        # Drawdown level
        dd_level = self._classify_drawdown(dd_pct)

        return RiskSnapshot(
            timestamp=datetime.now(),
            balance=account.balance,
            equity=equity,
            margin_used=account.margin,
            free_margin=account.free_margin,
            margin_level_pct=account.margin_level,
            num_open_positions=len(positions),
            total_exposure_usd=total_exposure,
            net_direction=net_exposure / total_exposure if total_exposure else 0,
            gross_exposure_pct=total_exposure / equity * 100,
            unrealized_pnl=sum(p.profit for p in positions),
            realized_pnl_today=self._get_realized_pnl('today'),
            realized_pnl_week=self._get_realized_pnl('week'),
            realized_pnl_month=self._get_realized_pnl('month'),
            equity_peak=self.peak_equity,
            current_drawdown_pct=dd_pct * 100,
            drawdown_duration_hours=self._dd_duration(),
            drawdown_level=dd_level,
            total_risk_pct=total_risk * 100,
            largest_position_risk_pct=max(
                abs(p.current_price - p.sl) * p.volume / equity * 100
                for p in positions if p.sl
            ) if positions else 0,
            correlation_cluster_risk=self._compute_cluster_risk(positions),
            current_vix=market_data.get('VIX', 0),
            avg_position_atr_pct=self._avg_atr_pct(positions, market_data),
        )
```

## 3. Alert Thresholds
```yaml
# risk-config.yaml

thresholds:
  # Drawdown levels (matches drawdown-playbook)
  drawdown:
    caution: 3.0      # % — reduce size 25%
    warning: 5.0       # % — reduce size 50%
    critical: 10.0     # % — minimum size only
    emergency: 15.0    # % — KILL SWITCH

  # Daily limits
  daily:
    max_loss: 4.0      # % of account
    max_trades: 10
    max_loss_streak: 5  # consecutive losses

  # Exposure limits
  exposure:
    max_gross: 300     # % (3:1 leverage max)
    max_single_position: 2.0  # % risk per position
    max_total_risk: 6.0      # % total open risk
    max_correlated: 4.0      # % risk in correlated cluster
    min_margin_level: 200    # % — below = too leveraged

  # Volatility adjustments
  volatility:
    vix_reduce_25: 25    # At VIX > 25, reduce size 25%
    vix_reduce_50: 35    # At VIX > 35, reduce size 50%
    vix_stop: 45         # At VIX > 45, no new positions

kill_switches:
  margin_level_below: 150   # Auto-close largest loser
  drawdown_above: 15.0      # Auto-close ALL positions
  daily_loss_above: 5.0     # Auto-close ALL, lock for day
```

## 4. Kill Switch Implementation
```python
class KillSwitch:
    """Automated position closure for extreme scenarios."""

    def __init__(self, mt5_connection, config: dict):
        self.mt5 = mt5_connection
        self.config = config
        self.triggered = False
        self.trigger_log: list = []

    def evaluate(self, snapshot: RiskSnapshot) -> list[Action]:
        actions = []

        # Kill Switch 1: Margin crisis
        if snapshot.margin_level_pct < self.config['margin_level_below']:
            actions.append(Action(
                type='CLOSE_LARGEST_LOSER',
                reason=f'Margin level {snapshot.margin_level_pct:.0f}% < {self.config["margin_level_below"]}%',
                severity='CRITICAL'
            ))

        # Kill Switch 2: Emergency drawdown
        if snapshot.current_drawdown_pct > self.config['drawdown_above']:
            actions.append(Action(
                type='CLOSE_ALL',
                reason=f'Drawdown {snapshot.current_drawdown_pct:.1f}% > {self.config["drawdown_above"]}%',
                severity='EMERGENCY'
            ))

        # Kill Switch 3: Daily loss limit
        daily_loss_pct = abs(min(0, snapshot.realized_pnl_today)) / snapshot.equity_peak * 100
        if daily_loss_pct > self.config['daily_loss_above']:
            actions.append(Action(
                type='CLOSE_ALL_AND_LOCK',
                reason=f'Daily loss {daily_loss_pct:.1f}% > {self.config["daily_loss_above"]}%',
                severity='CRITICAL',
                lock_duration_hours=24
            ))

        # Execute actions
        for action in actions:
            self._execute(action)
            self._notify(action)
            self.trigger_log.append((datetime.now(), action))

        return actions

    def _execute(self, action: Action):
        if action.type == 'CLOSE_ALL':
            positions = self.mt5.positions_get()
            for pos in positions:
                self.mt5.close_position(pos.ticket)
            self.triggered = True

        elif action.type == 'CLOSE_LARGEST_LOSER':
            positions = self.mt5.positions_get()
            worst = min(positions, key=lambda p: p.profit)
            self.mt5.close_position(worst.ticket)

        elif action.type == 'CLOSE_ALL_AND_LOCK':
            self._execute(Action(type='CLOSE_ALL'))
            self._set_trading_lock(action.lock_duration_hours)
```

## 5. Dashboard Display

```
╔══════════════════════════════════════════════════════════╗
║  RISK MONITOR                          2025-01-15 14:32 ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  ACCOUNT          DRAWDOWN           EXPOSURE            ║
║  Balance: $52,340  Current: 2.1%     Gross: 142%        ║
║  Equity:  $51,890  Peak: $53,000     Net Long: 67%      ║
║  Margin:  $12,400  Duration: 3.2h    Positions: 4       ║
║  Free:    $39,490  Level: NORMAL     Corr Risk: 3.1%    ║
║                                                          ║
║  P&L TODAY         LIMITS                                ║
║  Realized: -$340   Daily: 34% of limit                   ║
║  Unreal:   -$450   Weekly: 21% of limit                  ║
║  Total:    -$790   Monthly: 12% of limit                 ║
║                                                          ║
║  POSITIONS                                               ║
║  EURUSD  BUY  0.5L  +$120  Risk: 0.8%                  ║
║  GBPUSD  BUY  0.3L  -$280  Risk: 1.2%                  ║
║  USDJPY  SELL 0.4L  -$190  Risk: 0.7%                  ║
║  XAUUSD  BUY  0.1L  -$100  Risk: 0.4%                  ║
║                                    Total: 3.1%          ║
║                                                          ║
║  VIX: 18.2 (Normal)    Spread Alert: None                ║
║  Kill Switch: ARMED    Last Trigger: Never               ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

## 6. Monitoring Loop
```python
import asyncio

async def risk_monitoring_loop(
    monitor: RiskMonitor,
    kill_switch: KillSwitch,
    notifier: Notifier,
    interval_seconds: int = 5
):
    """Main monitoring loop. Runs continuously during trading hours."""

    while is_trading_hours():
        try:
            # Get current state
            account = mt5.account_info()
            positions = mt5.positions_get()
            market_data = get_market_data()

            # Compute risk snapshot
            snapshot = monitor.compute_snapshot(account, positions, market_data)

            # Check kill switches (highest priority)
            kill_actions = kill_switch.evaluate(snapshot)

            # Check alerts
            alerts = monitor.check_thresholds(snapshot)
            for alert in alerts:
                if not monitor.recently_alerted(alert):
                    await notifier.send(alert)

            # Log snapshot
            monitor.log_snapshot(snapshot)

            # Broadcast to dashboard
            await dashboard.update(snapshot)

        except Exception as e:
            await notifier.send(Alert(
                level='ERROR',
                message=f'Risk monitor error: {e}',
            ))

        await asyncio.sleep(interval_seconds)
```

---

## Related Skills

- [Drawdown Playbook](drawdown-playbook.md)
- [Correlation Crisis](correlation-crisis.md)
- [Risk And Portfolio](risk-and-portfolio.md)
- [Trading Brain Orchestrator](../trading-infrastructure/trading-brain.md)
- [Multi-Strategy Orchestration](../meta/multi-strategy-orchestration.md)
