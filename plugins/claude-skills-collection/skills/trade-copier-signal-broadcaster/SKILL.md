---
name: trade-copier-signal-broadcaster
description: >
  Format and distribute trading signals to MT5 copiers, Telegram bots, Discord bots, and
  webhook endpoints. Use this skill whenever the user asks about "trade copier", "signal
  service", "broadcast signals", "Telegram trading bot", "Discord signals", "webhook alerts",
  "copy trading", "signal distribution", "format trade signal", "MT5 copier", "send signal to
  Telegram", "signal channel", or any request to distribute trading signals to external systems.
  Works with realtime-alert-pipeline and execution-algo-trading.
kind: tool
category: trading/infrastructure
status: active
aliases: [signal-broadcaster]
tags: [alerts, broadcaster, copier, discord, hooks, infrastructure, mt5, signal]
related_skills: [discord-webhook, notion-sync, realtime-alert-pipeline, telegram-bot]
---

# Trade Copier & Signal Broadcaster

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import json

@dataclass
class TradeSignal:
    symbol: str
    direction: str              # "BUY" or "SELL"
    entry_price: float
    stop_loss: float
    take_profit: list[float]    # multiple TP levels
    lot_size: float
    confidence: float           # 0-1
    setup_type: str
    timeframe: str
    notes: str = ""
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.utcnow().isoformat()

class SignalFormatter:
    """Format signals for different distribution channels."""

    @staticmethod
    def telegram_format(signal: TradeSignal) -> str:
        emoji = "🟢" if signal.direction == "BUY" else "🔴"
        tp_lines = "\n".join([f"  TP{i+1}: {tp}" for i, tp in enumerate(signal.take_profit)])
        return f"""{emoji} *{signal.direction} {signal.symbol}*
━━━━━━━━━━━━━━━
📍 Entry: `{signal.entry_price}`
🛑 SL: `{signal.stop_loss}`
{tp_lines}
📊 Lots: `{signal.lot_size}`
⏱ TF: {signal.timeframe}
🎯 Setup: {signal.setup_type}
📈 Confidence: {signal.confidence*100:.0f}%
{f'📝 {signal.notes}' if signal.notes else ''}
⏰ {signal.timestamp[:16]}"""

    @staticmethod
    def discord_format(signal: TradeSignal) -> dict:
        return {
            "embeds": [{
                "title": f"{'🟢' if signal.direction == 'BUY' else '🔴'} {signal.direction} {signal.symbol}",
                "color": 0x00ff00 if signal.direction == "BUY" else 0xff0000,
                "fields": [
                    {"name": "Entry", "value": str(signal.entry_price), "inline": True},
                    {"name": "Stop Loss", "value": str(signal.stop_loss), "inline": True},
                    {"name": "Take Profit", "value": " / ".join(str(tp) for tp in signal.take_profit), "inline": True},
                    {"name": "Lots", "value": str(signal.lot_size), "inline": True},
                    {"name": "Confidence", "value": f"{signal.confidence*100:.0f}%", "inline": True},
                    {"name": "Setup", "value": signal.setup_type, "inline": True}],
                "timestamp": signal.timestamp,
            }]
        }

    @staticmethod
    def mt5_copier_format(signal: TradeSignal) -> str:
        """Format for standard MT5 trade copier protocol."""
        return (f"{signal.direction},{signal.symbol},{signal.entry_price},"
                f"{signal.stop_loss},{signal.take_profit[0] if signal.take_profit else 0},"
                f"{signal.lot_size}")

    @staticmethod
    def mql5_code(signal: TradeSignal) -> str:
        """Generate MQL5 code to execute the signal."""
        sl_points = abs(signal.entry_price - signal.stop_loss)
        tp_points = abs(signal.take_profit[0] - signal.entry_price) if signal.take_profit else 0
        fn = "Buy" if signal.direction == "BUY" else "Sell"
        return f"""#include <Trade\\Trade.mqh>
CTrade trade;
void ExecuteSignal() {{
   trade.{fn}({signal.lot_size}, "{signal.symbol}", 0, {signal.stop_loss}, {signal.take_profit[0] if signal.take_profit else 0}, "{signal.setup_type}");
}}"""

    @staticmethod
    def webhook_payload(signal: TradeSignal) -> dict:
        """Generic webhook JSON payload."""
        return {
            "action": signal.direction.lower(),
            "symbol": signal.symbol,
            "entry": signal.entry_price,
            "sl": signal.stop_loss,
            "tp": signal.take_profit,
            "size": signal.lot_size,
            "confidence": signal.confidence,
            "setup": signal.setup_type,
            "tf": signal.timeframe,
            "timestamp": signal.timestamp,
        }

class SignalBroadcaster:
    """Broadcast signals to multiple channels simultaneously."""

    @staticmethod
    def broadcast(signal: TradeSignal, channels: list[str]) -> dict:
        results = {}
        formatter = SignalFormatter
        for ch in channels:
            if ch == "telegram":
                results["telegram"] = formatter.telegram_format(signal)
            elif ch == "discord":
                results["discord"] = json.dumps(formatter.discord_format(signal))
            elif ch == "mt5_copier":
                results["mt5_copier"] = formatter.mt5_copier_format(signal)
            elif ch == "mql5":
                results["mql5"] = formatter.mql5_code(signal)
            elif ch == "webhook":
                results["webhook"] = json.dumps(formatter.webhook_payload(signal))
        return results
```
