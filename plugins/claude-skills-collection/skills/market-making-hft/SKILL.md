---
name: market-making-hft
description: "Market making and high-frequency trading: quote generation, inventory management, order book analysis, latency tracking, microstructure signals, spoofing detection, optimal execution (TWAP/VWAP), Avellaneda-Stoikov model, order flow toxicity, market impact estimation. USE FOR: market making, market maker, HFT, high frequency, order book, bid ask, spread, inventory, spoofing, microstructure, latency, TWAP, VWAP, order flow, toxicity, tick data, limit order."
related_skills:
  - execution-algo-trading
  - liquidity-analysis
  - tick-data-storage
tags:
  - trading
  - execution
  - market-making
  - hft
  - inventory
  - quote-generation
skill_level: expert
kind: reference
category: trading/execution
status: active
---
> **Skill:** Market Making Hft  |  **Domain:** trading  |  **Category:** execution  |  **Level:** expert
> **Tags:** `trading`, `execution`, `market-making`, `hft`, `inventory`, `quote-generation`



---

## Market Making Core Engine

# Market Making Core Engine

## Overview
Complete market making strategy implementation covering quote generation with inventory
skew, volatility adjustment, and multiple market making models (basic, Avellaneda-Stoikov,
grid-based). Designed for both crypto exchanges and forex/CFD markets.

## Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                  Market Making Engine                          │
├──────────────┬──────────────┬─────────────┬──────────────────┤
│ Quote        │ Inventory    │ Volatility  │ Avellaneda-      │
│ Generator    │ Manager      │ Estimator   │ Stoikov Model    │
└──────────────┴──────────────┴─────────────┴──────────────────┘
```

```python
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone, timedelta
import math
from enum import Enum


# ═════════════════════════════════════════════════════════════
# CORE DATA TYPES
# ═════════════════════════════════════════════════════════════

@dataclass
class Quote:
    """A two-sided market quote (bid and ask)."""
    bid_price: float
    ask_price: float
    bid_size: float
    ask_size: float
    mid_price: float
    spread: float
    spread_bps: float  # Spread in basis points
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    
    @property
    def is_valid(self) -> bool:
        return (
            self.bid_price > 0
            and self.ask_price > self.bid_price
            and self.bid_size > 0
            and self.ask_size > 0
        )


@dataclass
class OrderBookLevel:
    """A single level in the order book."""
    price: float
    volume: float
    order_count: int = 0
    side: str = ""  # "bid" or "ask"


@dataclass
class OrderBook:
    """Complete order book snapshot."""
    bids: List[OrderBookLevel]
    asks: List[OrderBookLevel]
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    exchange: str = ""
    symbol: str = ""
    
    @property
    def best_bid(self) -> Optional[float]:
        return self.bids[0].price if self.bids else None
    
    @property
    def best_ask(self) -> Optional[float]:
        return self.asks[0].price if self.asks else None
    
    @property
    def mid_price(self) -> Optional[float]:
        if self.best_bid and self.best_ask:
            return (self.best_bid + self.best_ask) / 2
        return None
    
    @property
    def spread(self) -> Optional[float]:
        if self.best_bid and self.best_ask:
            return self.best_ask - self.best_bid
        return None
    
    @property
    def spread_bps(self) -> Optional[float]:
        if self.mid_price and self.spread:
            return self.spread / self.mid_price * 10000
        return None


@dataclass
class InventoryState:
    """Current inventory position."""
    quantity: float = 0.0
    avg_entry_price: float = 0.0
    max_quantity: float = 1.0
    unrealized_pnl: float = 0.0
    realized_pnl: float = 0.0
    trades_count: int = 0
    
    @property
    def utilization(self) -> float:
        """Inventory utilization: -1 (max short) to +1 (max long)."""
        if self.max_quantity == 0:
            return 0.0
        return self.quantity / self.max_quantity
    
    @property
    def is_flat(self) -> bool:
        return abs(self.quantity) < 1e-10


# ═════════════════════════════════════════════════════════════
# BASIC MARKET MAKER
# ═════════════════════════════════════════════════════════════

class BasicMarketMaker:
    """
    Simple symmetric market maker with inventory skew.
    
    Generates two-sided quotes around mid price with:
    - Base spread (configurable target)
    - Inventory skew (widen spread away from inventory direction)
    - Volatility adjustment (wider spread in high vol)
    - Order size scaling (reduce size at inventory limits)
    """
    
    def __init__(
        self,
        spread_target_bps: float = 10.0,
        max_inventory: float = 1.0,
        skew_factor: float = 0.5,
        vol_multiplier: float = 2.0,
        base_order_size: float = 0.1,
    ):
        """
        Args:
            spread_target_bps: Target spread in basis points
            max_inventory: Maximum position size (in base currency units)
            skew_factor: How aggressively to skew quotes (0-1)
            vol_multiplier: How much volatility widens spread
            base_order_size: Default order size
        """
        self.spread_target_bps = spread_target_bps
        self.max_inventory = max_inventory
        self.skew_factor = skew_factor
        self.vol_multiplier = vol_multiplier
        self.base_order_size = base_order_size
        self.inventory = InventoryState(max_quantity=max_inventory)
    
    def generate_quote(
        self,
        mid_price: float,
        volatility: float = 0.0,
        order_book_imbalance: float = 0.0,
    ) -> Quote:
        """
        Generate a two-sided quote.
        
        Args:
            mid_price: Current mid-market price
            volatility: Annualized volatility (e.g., 0.2 = 20%)
            order_book_imbalance: -1 (ask heavy) to +1 (bid heavy)
        
        Returns:
            Quote with bid/ask prices and sizes
        """
        # Base half-spread
        half_spread_bps = self.spread_target_bps / 2
        half_spread = mid_price * half_spread_bps / 10000
        
        # Inventory skew: shift quotes to reduce inventory
        inventory_ratio = self.inventory.utilization
        inventory_skew = inventory_ratio * half_spread * self.skew_factor
        
        # Volatility adjustment
        vol_adjustment = volatility * mid_price * self.vol_multiplier / 10000
        
        # Order book imbalance adjustment (lean into imbalance)
        imbalance_adj = order_book_imbalance * half_spread * 0.3
        
        # Calculate prices
        bid = mid_price - half_spread - inventory_skew - vol_adjustment + imbalance_adj
        ask = mid_price + half_spread - inventory_skew + vol_adjustment + imbalance_adj
        
        # Size scaling based on inventory
        bid_size_scale = max(0.1, 1 - max(0, inventory_ratio))
        ask_size_scale = max(0.1, 1 + min(0, inventory_ratio))
        
        bid_size = self.base_order_size * bid_size_scale
        ask_size = self.base_order_size * ask_size_scale
        
        spread = ask - bid
        spread_bps = spread / mid_price * 10000 if mid_price > 0 else 0
        
        return Quote(
            bid_price=round(bid, 8),
            ask_price=round(ask, 8),
            bid_size=round(bid_size, 8),
            ask_size=round(ask_size, 8),
            mid_price=mid_price,
            spread=round(spread, 8),
            spread_bps=round(spread_bps, 2),
        )
    
    def on_fill(
        self,
        side: str,
        price: float,
        quantity: float,
    ) -> None:
        """Process a trade fill and update inventory."""
        if side == "buy":
            new_qty = self.inventory.quantity + quantity
            # Update average price
            if self.inventory.quantity >= 0:
                total_cost = (
                    self.inventory.avg_entry_price * self.inventory.quantity
                    + price * quantity
                )
                self.inventory.avg_entry_price = (
                    total_cost / new_qty if new_qty > 0 else price
                )
            self.inventory.quantity = new_qty
        elif side == "sell":
            # Realize PnL on sells
            if self.inventory.quantity > 0:
                pnl = (price - self.inventory.avg_entry_price) * min(quantity, self.inventory.quantity)
                self.inventory.realized_pnl += pnl
            self.inventory.quantity -= quantity
        
        self.inventory.trades_count += 1
    
    def update_unrealized_pnl(self, current_price: float) -> float:
        """Update and return unrealized PnL."""
        if self.inventory.quantity == 0:
            self.inventory.unrealized_pnl = 0.0
        else:
            self.inventory.unrealized_pnl = (
                (current_price - self.inventory.avg_entry_price)
                * self.inventory.quantity
            )
        return self.inventory.unrealized_pnl


# ═════════════════════════════════════════════════════════════
# AVELLANEDA-STOIKOV MODEL
# ═════════════════════════════════════════════════════════════

class AvellanedaStoikovMM:
    """
    Avellaneda-Stoikov optimal market making model.
    
    From "High-frequency trading in a limit order book" (2008).
    Provides theoretically optimal quotes given risk aversion,
    volatility, and time horizon.
    
    Key formula:
      reservation_price = s - q * gamma * sigma^2 * (T - t)
      optimal_spread = gamma * sigma^2 * (T - t) + 2/gamma * ln(1 + gamma/kappa)
    
    Where:
      s = mid price
      q = inventory
      gamma = risk aversion parameter
      sigma = volatility
      T - t = time remaining
      kappa = order arrival rate
    """
    
    def __init__(
        self,
        gamma: float = 0.1,
        kappa: float = 1.5,
        sigma: float = 0.02,
        time_horizon_seconds: float = 3600,
        max_inventory: float = 1.0,
        tick_size: float = 0.01,
    ):
        """
        Args:
            gamma: Risk aversion (higher = more risk-averse, tighter inventory)
            kappa: Order arrival intensity (higher = more frequent fills expected)
            sigma: Volatility per second (annualized_vol / sqrt(252 * 24 * 3600))
            time_horizon_seconds: Trading session length in seconds
            max_inventory: Maximum inventory limit
            tick_size: Minimum price increment
        """
        self.gamma = gamma
        self.kappa = kappa
        self.sigma = sigma
        self.time_horizon = time_horizon_seconds
        self.max_inventory = max_inventory
        self.tick_size = tick_size
        self.inventory = 0.0
        self._start_time = datetime.now(timezone.utc)
    
    def reservation_price(
        self,
        mid_price: float,
        time_remaining: Optional[float] = None,
    ) -> float:
        """
        Calculate the reservation price (indifference price).
        
        The price at which the market maker is indifferent between holding
        and not holding one more unit, given their current inventory.
        """
        if time_remaining is None:
            elapsed = (datetime.now(timezone.utc) - self._start_time).total_seconds()
            time_remaining = max(0.001, self.time_horizon - elapsed)
        
        # r = s - q * gamma * sigma^2 * tau
        return mid_price - self.inventory * self.gamma * self.sigma ** 2 * time_remaining
    
    def optimal_spread(
        self,
        time_remaining: Optional[float] = None,
    ) -> float:
        """
        Calculate the optimal spread (ask - bid).
        
        Wider spread when:
        - Higher risk aversion (gamma)
        - Higher volatility (sigma)
        - More time remaining (tau)
        - Lower order arrival rate (kappa)
        """
        if time_remaining is None:
            elapsed = (datetime.now(timezone.utc) - self._start_time).total_seconds()
            time_remaining = max(0.001, self.time_horizon - elapsed)
        
        # delta = gamma * sigma^2 * tau + 2/gamma * ln(1 + gamma/kappa)
        spread = (
            self.gamma * self.sigma ** 2 * time_remaining
            + (2 / self.gamma) * math.log(1 + self.gamma / self.kappa)
        )
        
        # Round to tick size
        return max(spread, self.tick_size * 2)
    
    def generate_quote(
        self,
        mid_price: float,
        time_remaining: Optional[float] = None,
    ) -> Quote:
        """Generate optimal quotes using Avellaneda-Stoikov model."""
        r = self.reservation_price(mid_price, time_remaining)
        spread = self.optimal_spread(time_remaining)
        
        bid = r - spread / 2
        ask = r + spread / 2
        
        # Round to tick size
        bid = math.floor(bid / self.tick_size) * self.tick_size
        ask = math.ceil(ask / self.tick_size) * self.tick_size
        
        # Size based on inventory proximity to limit
        inv_ratio = abs(self.inventory) / self.max_inventory if self.max_inventory > 0 else 0
        base_size = 1.0 - inv_ratio * 0.8  # Reduce size near limits
        
        # Favor reducing inventory side
        if self.inventory > 0:
            ask_size = base_size * 1.5
            bid_size = base_size * 0.5
        elif self.inventory < 0:
            bid_size = base_size * 1.5
            ask_size = base_size * 0.5
        else:
            bid_size = base_size
            ask_size = base_size
        
        return Quote(
            bid_price=round(bid, 8),
            ask_price=round(ask, 8),
            bid_size=round(max(0.01, bid_size), 4),
            ask_size=round(max(0.01, ask_size), 4),
            mid_price=mid_price,
            spread=round(ask - bid, 8),
            spread_bps=round((ask - bid) / mid_price * 10000, 2) if mid_price > 0 else 0,
        )
    
    def on_fill(self, side: str, quantity: float) -> None:
        """Update inventory on fill."""
        if side == "buy":
            self.inventory += quantity
        elif side == "sell":
            self.inventory -= quantity
    
    def reset_session(self) -> None:
        """Reset for a new trading session."""
        self._start_time = datetime.now(timezone.utc)
        self.inventory = 0.0
```


---

## Order Book Analyzer

# Order Book Analyzer

```python
class OrderBookAnalyzer:
    """
    Deep order book analysis for microstructure intelligence.
    
    Provides:
    - Order flow imbalance (directional predictor)
    - Book depth analysis
    - Spoofing detection
    - Support/resistance from order clusters
    - VWAP calculation from book
    - Liquidity heatmap generation
    """
    
    @staticmethod
    def order_flow_imbalance(
        bid_levels: List[OrderBookLevel],
        ask_levels: List[OrderBookLevel],
        depth: int = 10,
        weighted: bool = True,
    ) -> float:
        """
        Calculate order flow imbalance (OFI).
        
        A directional signal: positive = buy pressure, negative = sell pressure.
        
        Args:
            bid_levels: List of bid levels (best to worst)
            ask_levels: List of ask levels (best to worst)
            depth: Number of levels to consider
            weighted: If True, weight levels by inverse distance from mid
        
        Returns:
            Imbalance from -1 (all sell) to +1 (all buy)
        """
        bids = bid_levels[:depth]
        asks = ask_levels[:depth]
        
        if not bids or not asks:
            return 0.0
        
        if weighted:
            mid = (bids[0].price + asks[0].price) / 2 if bids and asks else 0
            if mid == 0:
                return 0.0
            
            bid_vol = sum(
                level.volume / (1 + abs(level.price - mid) / mid * 100)
                for level in bids
            )
            ask_vol = sum(
                level.volume / (1 + abs(level.price - mid) / mid * 100)
                for level in asks
            )
        else:
            bid_vol = sum(level.volume for level in bids)
            ask_vol = sum(level.volume for level in asks)
        
        total = bid_vol + ask_vol
        if total == 0:
            return 0.0
        
        return (bid_vol - ask_vol) / total
    
    @staticmethod
    def book_depth_profile(
        bid_levels: List[OrderBookLevel],
        ask_levels: List[OrderBookLevel],
        pct_range: float = 1.0,
    ) -> dict:
        """
        Analyze order book depth within a percentage range of mid price.
        
        Args:
            pct_range: Percentage of mid price to include (e.g., 1.0 = ±1%)
        """
        if not bid_levels or not ask_levels:
            return {"error": "Empty order book"}
        
        mid = (bid_levels[0].price + ask_levels[0].price) / 2
        lower = mid * (1 - pct_range / 100)
        upper = mid * (1 + pct_range / 100)
        
        bids_in_range = [l for l in bid_levels if l.price >= lower]
        asks_in_range = [l for l in ask_levels if l.price <= upper]
        
        bid_depth = sum(l.volume * l.price for l in bids_in_range)
        ask_depth = sum(l.volume * l.price for l in asks_in_range)
        
        # Find large walls (levels > 3x average)
        all_volumes = [l.volume for l in bids_in_range + asks_in_range]
        avg_vol = np.mean(all_volumes) if all_volumes else 0
        
        bid_walls = [
            {"price": l.price, "volume": l.volume, "usd_value": l.volume * l.price}
            for l in bids_in_range
            if l.volume > avg_vol * 3
        ]
        ask_walls = [
            {"price": l.price, "volume": l.volume, "usd_value": l.volume * l.price}
            for l in asks_in_range
            if l.volume > avg_vol * 3
        ]
        
        return {
            "mid_price": round(mid, 8),
            "bid_depth_usd": round(bid_depth, 2),
            "ask_depth_usd": round(ask_depth, 2),
            "depth_ratio": round(bid_depth / ask_depth, 4) if ask_depth > 0 else float("inf"),
            "bid_levels_count": len(bids_in_range),
            "ask_levels_count": len(asks_in_range),
            "bid_walls": bid_walls[:5],
            "ask_walls": ask_walls[:5],
            "imbalance": round(
                (bid_depth - ask_depth) / (bid_depth + ask_depth), 4
            ) if (bid_depth + ask_depth) > 0 else 0,
        }
    
    @staticmethod
    def detect_spoofing(
        order_updates: List[dict],
        threshold_cancel_ratio: float = 0.9,
        min_size_multiple: float = 3.0,
        window_seconds: float = 60.0,
    ) -> List[dict]:
        """
        Detect potential spoofing activity in order book updates.
        
        Spoofing indicators:
        - Large orders placed then quickly cancelled (>90% cancel rate)
        - Orders significantly larger than average
        - Rapid placement/cancellation cycles
        
        Args:
            order_updates: List of dicts with keys: order_id, action (place/cancel/fill),
                          price, volume, timestamp, side
            threshold_cancel_ratio: Min cancel/place ratio to flag
            min_size_multiple: Min multiple of average size to flag
        """
        if not order_updates:
            return []
        
        # Group by order ID
        orders: Dict[str, List[dict]] = {}
        for update in order_updates:
            oid = update.get("order_id", "")
            if oid not in orders:
                orders[oid] = []
            orders[oid].append(update)
        
        # Calculate average order size
        all_volumes = [
            u.get("volume", 0)
            for u in order_updates
            if u.get("action") == "place"
        ]
        avg_volume = np.mean(all_volumes) if all_volumes else 0
        
        suspects = []
        for oid, updates in orders.items():
            placed = [u for u in updates if u.get("action") == "place"]
            cancelled = [u for u in updates if u.get("action") == "cancel"]
            filled = [u for u in updates if u.get("action") == "fill"]
            
            if not placed:
                continue
            
            volume = placed[0].get("volume", 0)
            is_large = volume > avg_volume * min_size_multiple if avg_volume > 0 else False
            
            # Check if quickly cancelled
            if cancelled and placed:
                place_time = placed[0].get("timestamp")
                cancel_time = cancelled[0].get("timestamp")
                if place_time and cancel_time:
                    lifetime = (cancel_time - place_time).total_seconds()
                else:
                    lifetime = window_seconds
            else:
                lifetime = None
            
            # Flag as suspicious
            cancel_ratio = len(cancelled) / len(placed) if placed else 0
            
            if (
                is_large
                and cancel_ratio >= threshold_cancel_ratio
                and not filled
                and lifetime is not None
                and lifetime < window_seconds
            ):
                suspects.append({
                    "order_id": oid,
                    "side": placed[0].get("side", "unknown"),
                    "price": placed[0].get("price", 0),
                    "volume": volume,
                    "volume_multiple": round(volume / avg_volume, 1) if avg_volume > 0 else 0,
                    "lifetime_seconds": round(lifetime, 2) if lifetime else None,
                    "cancel_ratio": round(cancel_ratio, 2),
                    "confidence": min(1.0, (volume / avg_volume / 5 + cancel_ratio) / 2) if avg_volume > 0 else 0.5,
                })
        
        return sorted(suspects, key=lambda x: x.get("confidence", 0), reverse=True)
    
    @staticmethod
    def vwap_from_book(
        levels: List[OrderBookLevel],
        target_volume: float,
    ) -> Optional[float]:
        """
        Calculate VWAP for executing a target volume through the book.
        
        This gives the expected average execution price for a market order
        of the given size.
        """
        if not levels or target_volume <= 0:
            return None
        
        remaining = target_volume
        total_cost = 0.0
        
        for level in levels:
            fill = min(remaining, level.volume)
            total_cost += fill * level.price
            remaining -= fill
            if remaining <= 0:
                break
        
        filled_volume = target_volume - remaining
        if filled_volume == 0:
            return None
        
        return total_cost / filled_volume
    
    @staticmethod
    def market_impact_estimate(
        levels: List[OrderBookLevel],
        order_size: float,
    ) -> dict:
        """
        Estimate market impact of a market order.
        
        Returns:
            Dict with vwap, slippage, price levels consumed, etc.
        """
        if not levels:
            return {"error": "Empty book"}
        
        best_price = levels[0].price
        vwap = OrderBookAnalyzer.vwap_from_book(levels, order_size)
        
        if vwap is None:
            return {
                "error": "Insufficient liquidity",
                "available_volume": sum(l.volume for l in levels),
                "requested_volume": order_size,
            }
        
        slippage = abs(vwap - best_price)
        slippage_bps = slippage / best_price * 10000 if best_price > 0 else 0
        
        # Count levels consumed
        remaining = order_size
        levels_consumed = 0
        for level in levels:
            remaining -= level.volume
            levels_consumed += 1
            if remaining <= 0:
                break
        
        return {
            "best_price": round(best_price, 8),
            "vwap": round(vwap, 8),
            "slippage": round(slippage, 8),
            "slippage_bps": round(slippage_bps, 2),
            "levels_consumed": levels_consumed,
            "total_levels": len(levels),
            "order_size": order_size,
        }
```


---

## Latency Tracker & Execution Monitor

# Latency Tracker & Execution Monitor

```python
class LatencyTracker:
    """
    Track and analyze execution latency for HFT operations.
    
    Monitors:
    - Order submission to acknowledgement latency
    - Market data feed latency
    - Round-trip latency
    - Latency distribution (percentiles)
    - Latency anomaly detection
    """
    
    def __init__(self, max_samples: int = 10000):
        self._measurements: List[float] = []
        self._max_samples = max_samples
        self._labels: Dict[str, List[float]] = {}
    
    def record(
        self,
        latency_seconds: float,
        label: str = "default",
    ) -> None:
        """Record a latency measurement."""
        self._measurements.append(latency_seconds)
        if len(self._measurements) > self._max_samples:
            self._measurements = self._measurements[-self._max_samples:]
        
        if label not in self._labels:
            self._labels[label] = []
        self._labels[label].append(latency_seconds)
        if len(self._labels[label]) > self._max_samples:
            self._labels[label] = self._labels[label][-self._max_samples:]
    
    def record_timestamps(
        self,
        sent_time: float,
        received_time: float,
        label: str = "default",
    ) -> float:
        """Record latency from two timestamps. Returns latency."""
        latency = received_time - sent_time
        self.record(latency, label)
        return latency
    
    def stats(self, label: Optional[str] = None) -> dict:
        """
        Get latency statistics.
        
        Returns percentiles, mean, std, min, max in milliseconds.
        """
        measurements = self._labels.get(label, self._measurements) if label else self._measurements
        
        if not measurements:
            return {"error": "No measurements recorded"}
        
        arr = np.array(measurements) * 1000  # Convert to ms
        
        return {
            "label": label or "all",
            "count": len(measurements),
            "mean_ms": round(float(np.mean(arr)), 3),
            "std_ms": round(float(np.std(arr)), 3),
            "min_ms": round(float(np.min(arr)), 3),
            "max_ms": round(float(np.max(arr)), 3),
            "p50_ms": round(float(np.percentile(arr, 50)), 3),
            "p90_ms": round(float(np.percentile(arr, 90)), 3),
            "p95_ms": round(float(np.percentile(arr, 95)), 3),
            "p99_ms": round(float(np.percentile(arr, 99)), 3),
            "p999_ms": round(float(np.percentile(arr, 99.9)), 3),
        }
    
    def detect_anomalies(
        self,
        label: Optional[str] = None,
        threshold_std: float = 3.0,
    ) -> List[dict]:
        """Detect latency anomalies (values beyond threshold standard deviations)."""
        measurements = self._labels.get(label, self._measurements) if label else self._measurements
        
        if len(measurements) < 10:
            return []
        
        arr = np.array(measurements)
        mean = np.mean(arr)
        std = np.std(arr)
        
        if std == 0:
            return []
        
        anomalies = []
        for i, val in enumerate(measurements):
            z_score = (val - mean) / std
            if abs(z_score) > threshold_std:
                anomalies.append({
                    "index": i,
                    "latency_ms": round(val * 1000, 3),
                    "z_score": round(z_score, 2),
                    "severity": "HIGH" if abs(z_score) > 5 else "MODERATE",
                })
        
        return anomalies
    
    def jitter(self, label: Optional[str] = None) -> dict:
        """Calculate jitter (variation in latency)."""
        measurements = self._labels.get(label, self._measurements) if label else self._measurements
        
        if len(measurements) < 2:
            return {"error": "Need at least 2 measurements"}
        
        diffs = np.diff(np.array(measurements)) * 1000  # ms
        
        return {
            "mean_jitter_ms": round(float(np.mean(np.abs(diffs))), 3),
            "max_jitter_ms": round(float(np.max(np.abs(diffs))), 3),
            "std_jitter_ms": round(float(np.std(diffs)), 3),
        }


# ═════════════════════════════════════════════════════════════
# OPTIMAL EXECUTION ALGORITHMS
# ═════════════════════════════════════════════════════════════

class OptimalExecution:
    """
    Optimal execution algorithms for minimizing market impact.
    
    Implements:
    - TWAP (Time-Weighted Average Price)
    - VWAP (Volume-Weighted Average Price)
    - Implementation Shortfall minimization
    """
    
    @staticmethod
    def twap_schedule(
        total_quantity: float,
        duration_minutes: int,
        interval_minutes: int = 1,
    ) -> List[dict]:
        """
        Generate a TWAP execution schedule.
        
        Splits the total quantity into equal slices over time.
        
        Args:
            total_quantity: Total quantity to execute
            duration_minutes: Total execution window
            interval_minutes: Time between child orders
        """
        n_slices = max(1, duration_minutes // interval_minutes)
        slice_qty = total_quantity / n_slices
        
        schedule = []
        for i in range(n_slices):
            schedule.append({
                "slice": i + 1,
                "time_offset_minutes": i * interval_minutes,
                "quantity": round(slice_qty, 8),
                "cumulative_quantity": round(slice_qty * (i + 1), 8),
                "pct_complete": round((i + 1) / n_slices * 100, 1),
            })
        
        return schedule
    
    @staticmethod
    def vwap_schedule(
        total_quantity: float,
        volume_profile: List[float],
        duration_minutes: int,
    ) -> List[dict]:
        """
        Generate a VWAP execution schedule.
        
        Distributes quantity proportional to historical volume profile.
        
        Args:
            total_quantity: Total quantity to execute
            volume_profile: Historical volume for each time bucket (normalized)
            duration_minutes: Total execution window
        """
        if not volume_profile:
            return OptimalExecution.twap_schedule(total_quantity, duration_minutes)
        
        total_volume = sum(volume_profile)
        if total_volume == 0:
            return OptimalExecution.twap_schedule(total_quantity, duration_minutes)
        
        interval = duration_minutes / len(volume_profile)
        schedule = []
        cumulative = 0.0
        
        for i, vol in enumerate(volume_profile):
            weight = vol / total_volume
            qty = total_quantity * weight
            cumulative += qty
            
            schedule.append({
                "slice": i + 1,
                "time_offset_minutes": round(i * interval, 1),
                "quantity": round(qty, 8),
                "cumulative_quantity": round(cumulative, 8),
                "volume_weight": round(weight, 4),
                "pct_complete": round(cumulative / total_quantity * 100, 1),
            })
        
        return schedule
    
    @staticmethod
    def implementation_shortfall(
        decision_price: float,
        execution_prices: List[float],
        execution_quantities: List[float],
        side: str = "buy",
    ) -> dict:
        """
        Calculate implementation shortfall.
        
        Measures the cost of delayed/imperfect execution vs the decision price.
        
        Args:
            decision_price: Price at time of decision
            execution_prices: List of fill prices
            execution_quantities: List of fill quantities
            side: "buy" or "sell"
        """
        if not execution_prices or not execution_quantities:
            return {"error": "No executions"}
        
        total_qty = sum(execution_quantities)
        if total_qty == 0:
            return {"error": "Zero total quantity"}
        
        avg_exec_price = (
            sum(p * q for p, q in zip(execution_prices, execution_quantities))
            / total_qty
        )
        
        if side == "buy":
            shortfall = (avg_exec_price - decision_price) * total_qty
            shortfall_bps = (avg_exec_price / decision_price - 1) * 10000
        else:
            shortfall = (decision_price - avg_exec_price) * total_qty
            shortfall_bps = (1 - avg_exec_price / decision_price) * 10000
        
        return {
            "decision_price": round(decision_price, 8),
            "avg_execution_price": round(avg_exec_price, 8),
            "total_quantity": round(total_qty, 8),
            "shortfall_usd": round(shortfall, 2),
            "shortfall_bps": round(shortfall_bps, 2),
            "num_fills": len(execution_prices),
            "slippage_direction": "adverse" if shortfall > 0 else "favorable",
        }
```


---

## Order Flow Toxicity (VPIN)

# Order Flow Toxicity (VPIN)

```python
class OrderFlowToxicity:
    """
    Volume-Synchronized Probability of Informed Trading (VPIN).
    
    Measures the proportion of "toxic" (informed) order flow. High VPIN
    indicates adverse selection risk for market makers.
    
    Based on Easley, Lopez de Prado, and O'Hara (2012).
    """
    
    @staticmethod
    def calculate_vpin(
        trades: List[dict],
        bucket_volume: float,
        n_buckets: int = 50,
    ) -> dict:
        """
        Calculate VPIN from trade data.
        
        Args:
            trades: List of dicts with keys: price, volume, timestamp
            bucket_volume: Volume per bucket (e.g., average daily volume / 50)
            n_buckets: Number of buckets for the rolling window
        
        Returns:
            Dict with VPIN value and toxicity assessment
        """
        if not trades or bucket_volume <= 0:
            return {"error": "Invalid input"}
        
        # Classify trades as buy/sell using tick rule
        classified = OrderFlowToxicity._classify_trades(trades)
        
        # Create volume buckets
        buckets = []
        current_buy = 0.0
        current_sell = 0.0
        current_total = 0.0
        
        for trade in classified:
            vol = trade["volume"]
            if trade["side"] == "buy":
                current_buy += vol
            else:
                current_sell += vol
            current_total += vol
            
            while current_total >= bucket_volume:
                overflow = current_total - bucket_volume
                
                # Proportionally reduce
                if current_total > 0:
                    factor = bucket_volume / (current_total)
                else:
                    factor = 1.0
                
                buckets.append({
                    "buy_volume": current_buy * factor,
                    "sell_volume": current_sell * factor,
                    "total_volume": bucket_volume,
                    "order_imbalance": abs(current_buy * factor - current_sell * factor),
                })
                
                # Carry overflow
                current_buy = current_buy * (1 - factor)
                current_sell = current_sell * (1 - factor)
                current_total = overflow
        
        if len(buckets) < n_buckets:
            return {
                "vpin": 0.0,
                "warning": f"Only {len(buckets)} buckets (need {n_buckets})",
                "toxicity": "UNKNOWN",
            }
        
        # Calculate VPIN over rolling window
        recent_buckets = buckets[-n_buckets:]
        total_imbalance = sum(b["order_imbalance"] for b in recent_buckets)
        total_volume = sum(b["total_volume"] for b in recent_buckets)
        
        vpin = total_imbalance / total_volume if total_volume > 0 else 0
        
        # Toxicity assessment
        if vpin > 0.7:
            toxicity = "EXTREME"
            action = "Widen spreads significantly or stop quoting"
        elif vpin > 0.5:
            toxicity = "HIGH"
            action = "Widen spreads and reduce position sizes"
        elif vpin > 0.3:
            toxicity = "ELEVATED"
            action = "Monitor closely, slight spread widening"
        else:
            toxicity = "NORMAL"
            action = "Standard market making parameters"
        
        return {
            "vpin": round(vpin, 4),
            "toxicity": toxicity,
            "action": action,
            "n_buckets_used": n_buckets,
            "total_buckets_available": len(buckets),
        }
    
    @staticmethod
    def _classify_trades(trades: List[dict]) -> List[dict]:
        """Classify trades as buy/sell using the tick rule."""
        classified = []
        prev_price = trades[0]["price"] if trades else 0
        
        for trade in trades:
            price = trade["price"]
            if price > prev_price:
                side = "buy"
            elif price < prev_price:
                side = "sell"
            else:
                side = classified[-1]["side"] if classified else "buy"
            
            classified.append({
                **trade,
                "side": side,
            })
            prev_price = price
        
        return classified
    
    @staticmethod
    def kyle_lambda(
        price_changes: List[float],
        volume_changes: List[float],
    ) -> dict:
        """
        Estimate Kyle's lambda (price impact coefficient).
        
        Lambda measures how much prices move per unit of order flow.
        Higher lambda = lower liquidity / higher informed trading.
        
        Uses simple OLS regression: delta_price = lambda * signed_volume + epsilon
        """
        if len(price_changes) != len(volume_changes) or len(price_changes) < 10:
            return {"error": "Need at least 10 matching observations"}
        
        x = np.array(volume_changes)
        y = np.array(price_changes)
        
        # OLS: lambda = Cov(y, x) / Var(x)
        cov = np.cov(y, x)[0, 1]
        var_x = np.var(x)
        
        if var_x == 0:
            return {"error": "Zero variance in volume"}
        
        lambda_coeff = cov / var_x
        
        # R-squared
        y_pred = lambda_coeff * x
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        
        return {
            "kyle_lambda": round(lambda_coeff, 8),
            "r_squared": round(r_squared, 4),
            "interpretation": (
                "High price impact per unit volume — low liquidity"
                if abs(lambda_coeff) > np.std(y) / np.std(x)
                else "Normal price impact — adequate liquidity"
            ),
            "n_observations": len(price_changes),
        }
```


---

## HFT Risk Manager

# HFT Risk Manager

```python
class HFTRiskManager:
    """
    Real-time risk management for high-frequency market making.
    
    Monitors:
    - Position limits
    - Loss limits (daily, per-trade)
    - Inventory age
    - Quote sanity checks
    - Kill switch triggers
    """
    
    def __init__(
        self,
        max_position: float = 10.0,
        max_daily_loss: float = 1000.0,
        max_trade_loss: float = 100.0,
        max_inventory_age_seconds: float = 300.0,
        max_spread_bps: float = 100.0,
        min_spread_bps: float = 0.5,
    ):
        self.max_position = max_position
        self.max_daily_loss = max_daily_loss
        self.max_trade_loss = max_trade_loss
        self.max_inventory_age_seconds = max_inventory_age_seconds
        self.max_spread_bps = max_spread_bps
        self.min_spread_bps = min_spread_bps
        
        self._daily_pnl = 0.0
        self._current_position = 0.0
        self._position_opened_at: Optional[datetime] = None
        self._kill_switch = False
        self._warnings: List[str] = []
    
    def check_quote(self, quote: Quote, mid_price: float) -> dict:
        """
        Validate a quote before submission.
        
        Returns dict with approved flag and any warnings/rejections.
        """
        issues = []
        
        if self._kill_switch:
            return {"approved": False, "reason": "KILL SWITCH ACTIVE", "issues": ["Kill switch triggered"]}
        
        # Spread sanity
        if quote.spread_bps > self.max_spread_bps:
            issues.append(f"Spread too wide: {quote.spread_bps:.1f} bps > {self.max_spread_bps}")
        if quote.spread_bps < self.min_spread_bps:
            issues.append(f"Spread too tight: {quote.spread_bps:.1f} bps < {self.min_spread_bps}")
        
        # Price sanity (quotes shouldn't be too far from mid)
        bid_deviation = abs(quote.bid_price - mid_price) / mid_price * 10000
        ask_deviation = abs(quote.ask_price - mid_price) / mid_price * 10000
        if bid_deviation > 200 or ask_deviation > 200:
            issues.append(f"Quote too far from mid: bid={bid_deviation:.0f}bps, ask={ask_deviation:.0f}bps")
        
        # Negative spread (crossed market)
        if quote.ask_price <= quote.bid_price:
            issues.append("Crossed market: ask <= bid")
        
        # Position limit
        if abs(self._current_position + quote.bid_size) > self.max_position:
            issues.append(f"Would exceed position limit: {abs(self._current_position + quote.bid_size):.2f} > {self.max_position}")
        
        # Daily loss limit
        if self._daily_pnl <= -self.max_daily_loss:
            issues.append(f"Daily loss limit reached: {self._daily_pnl:.2f}")
            self._kill_switch = True
        
        approved = len(issues) == 0
        return {
            "approved": approved,
            "issues": issues,
            "quote": {
                "bid": quote.bid_price,
                "ask": quote.ask_price,
                "spread_bps": quote.spread_bps,
            },
        }
    
    def on_fill(self, side: str, price: float, quantity: float, pnl: float = 0.0) -> dict:
        """
        Process a fill and update risk state.
        
        Returns risk status after the fill.
        """
        if side == "buy":
            self._current_position += quantity
        else:
            self._current_position -= quantity
        
        self._daily_pnl += pnl
        
        if self._position_opened_at is None and self._current_position != 0:
            self._position_opened_at = datetime.now(timezone.utc)
        elif self._current_position == 0:
            self._position_opened_at = None
        
        # Check limits
        warnings = []
        if abs(self._current_position) > self.max_position * 0.8:
            warnings.append(f"Position at {abs(self._current_position) / self.max_position:.0%} of limit")
        if self._daily_pnl < -self.max_daily_loss * 0.8:
            warnings.append(f"Daily PnL at {self._daily_pnl:.2f} ({abs(self._daily_pnl / self.max_daily_loss):.0%} of limit)")
        if abs(pnl) > self.max_trade_loss:
            warnings.append(f"Trade loss {pnl:.2f} exceeds limit {self.max_trade_loss}")
        
        return {
            "position": round(self._current_position, 8),
            "daily_pnl": round(self._daily_pnl, 2),
            "kill_switch": self._kill_switch,
            "warnings": warnings,
        }
    
    def check_inventory_age(self) -> Optional[str]:
        """Check if inventory has been held too long."""
        if self._position_opened_at is None or self._current_position == 0:
            return None
        
        age = (datetime.now(timezone.utc) - self._position_opened_at).total_seconds()
        if age > self.max_inventory_age_seconds:
            return (
                f"Inventory age {age:.0f}s exceeds limit "
                f"{self.max_inventory_age_seconds:.0f}s — consider unwinding"
            )
        return None
    
    def trigger_kill_switch(self, reason: str = "manual") -> None:
        """Activate kill switch — reject all new quotes."""
        self._kill_switch = True
        self._warnings.append(f"Kill switch triggered: {reason}")
    
    def reset_kill_switch(self) -> None:
        """Deactivate kill switch."""
        self._kill_switch = False
    
    def reset_daily(self) -> None:
        """Reset daily counters (call at start of new trading day)."""
        self._daily_pnl = 0.0
        self._kill_switch = False
        self._warnings.clear()
    
    @property
    def status(self) -> dict:
        return {
            "position": round(self._current_position, 8),
            "position_pct": round(abs(self._current_position) / self.max_position * 100, 1) if self.max_position > 0 else 0,
            "daily_pnl": round(self._daily_pnl, 2),
            "daily_pnl_pct_of_limit": round(abs(self._daily_pnl) / self.max_daily_loss * 100, 1) if self.max_daily_loss > 0 else 0,
            "kill_switch": self._kill_switch,
            "inventory_age": self.check_inventory_age(),
            "warnings": list(self._warnings),
        }
```

---

## Related Skills

- [Execution Algo Trading](../execution-algo-trading.md)
- [Market Microstructure](../market-microstructure.md)
- [Liquidity Analysis](../liquidity-analysis.md)
- [Tick Data Storage](../tick-data-storage.md)
