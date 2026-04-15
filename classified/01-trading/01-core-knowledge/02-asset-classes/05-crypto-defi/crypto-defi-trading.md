---
name: crypto-defi-trading
description: "Crypto and DeFi trading: DEX analysis (Uniswap, SushiSwap, Curve), on-chain analytics, MEV detection, impermanent loss, yield farming metrics, DeFi risk analysis, token metrics, liquidity pool analysis, whale tracking, exchange netflow. USE FOR: crypto, defi, dex, uniswap, sushiswap, curve, impermanent loss, yield farming, on-chain, whale, MEV, arbitrage, liquidity pool, token, exchange flow, gas, NFT."
related_skills:
  - liquidity-analysis
  - ict-smart-money
  - technical-analysis
  - risk-and-portfolio
tags:
  - trading
  - asset-class
  - crypto
  - defi
  - dex
  - mev
  - yield-farming
  - bitcoin
skill_level: advanced
kind: reference
category: trading/asset-classes
status: active
---
> **Skill:** Crypto Defi Trading  |  **Domain:** trading  |  **Category:** asset-class  |  **Level:** advanced
> **Tags:** `trading`, `asset-class`, `crypto`, `defi`, `dex`, `mev`, `yield-farming`, `bitcoin`



---

## DEX Analysis Engine

# DEX Analysis Engine

## Overview
Complete decentralized exchange analysis covering Uniswap V2/V3, SushiSwap, Curve, and
other AMM protocols. Analyzes pool states, liquidity distributions, price impact, and
optimal routing across DEXes.

## Architecture

```
┌───────────────────────────────────────────────────────────┐
│                    DEX Analysis Engine                      │
├──────────────┬──────────────┬──────────────┬──────────────┤
│ Pool State   │ Liquidity    │ Price Impact │ Cross-DEX    │
│ Analyzer     │ Distribution │ Calculator   │ Router       │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

```python
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timezone
import math


# ═════════════════════════════════════════════════════════════
# CORE DATA TYPES
# ═════════════════════════════════════════════════════════════

@dataclass
class Token:
    """Represents an ERC-20 token."""
    address: str
    symbol: str
    decimals: int = 18
    name: str = ""
    
    def format_amount(self, raw_amount: int) -> float:
        """Convert raw token amount to human-readable."""
        return raw_amount / (10 ** self.decimals)
    
    def to_raw(self, amount: float) -> int:
        """Convert human-readable amount to raw."""
        return int(amount * (10 ** self.decimals))


@dataclass
class PoolState:
    """State of an AMM liquidity pool."""
    pool_address: str
    token_0: Token
    token_1: Token
    reserve_0: float
    reserve_1: float
    fee_tier: float  # e.g., 0.003 for 0.3%
    total_liquidity: float
    price: float  # token_1 per token_0
    volume_24h: float = 0.0
    fee_revenue_24h: float = 0.0
    tvl_usd: float = 0.0
    tick_current: Optional[int] = None  # Uniswap V3
    sqrt_price_x96: Optional[int] = None  # Uniswap V3
    
    @property
    def fee_apr(self) -> float:
        """Annualized fee APR based on 24h volume."""
        if self.tvl_usd == 0:
            return 0.0
        daily_fee_rate = self.fee_revenue_24h / self.tvl_usd
        return daily_fee_rate * 365 * 100
    
    @property
    def volume_to_tvl(self) -> float:
        """Volume/TVL ratio — higher = more capital efficient."""
        if self.tvl_usd == 0:
            return 0.0
        return self.volume_24h / self.tvl_usd


@dataclass
class LiquidityPosition:
    """A liquidity provider's position."""
    pool_address: str
    owner: str
    liquidity: float
    token_0_amount: float
    token_1_amount: float
    lower_tick: Optional[int] = None  # V3 range
    upper_tick: Optional[int] = None  # V3 range
    fees_earned_0: float = 0.0
    fees_earned_1: float = 0.0
    opened_at: Optional[datetime] = None
    
    @property
    def is_in_range(self) -> bool:
        """Check if a V3 position is currently in range (needs current tick)."""
        if self.lower_tick is None or self.upper_tick is None:
            return True  # V2 positions are always in range
        # Caller must check against current tick
        return True


# ═════════════════════════════════════════════════════════════
# UNISWAP V2 ANALYZER
# ═════════════════════════════════════════════════════════════

class UniswapV2Analyzer:
    """
    Uniswap V2 constant product AMM analyzer.
    
    Core formula: x * y = k
    Price: p = y / x
    Output amount: dy = (y * dx * (1 - fee)) / (x + dx * (1 - fee))
    """
    
    @staticmethod
    def get_price(reserve_0: float, reserve_1: float) -> float:
        """Calculate spot price (token1 per token0)."""
        if reserve_0 == 0:
            return 0.0
        return reserve_1 / reserve_0
    
    @staticmethod
    def get_output_amount(
        amount_in: float,
        reserve_in: float,
        reserve_out: float,
        fee: float = 0.003,
    ) -> float:
        """
        Calculate output amount for a swap.
        
        Args:
            amount_in: Amount of input token
            reserve_in: Reserve of input token
            reserve_out: Reserve of output token
            fee: Fee tier (e.g., 0.003 for 0.3%)
        """
        if reserve_in == 0 or reserve_out == 0:
            return 0.0
        amount_in_with_fee = amount_in * (1 - fee)
        numerator = amount_in_with_fee * reserve_out
        denominator = reserve_in + amount_in_with_fee
        return numerator / denominator
    
    @staticmethod
    def get_price_impact(
        amount_in: float,
        reserve_in: float,
        reserve_out: float,
        fee: float = 0.003,
    ) -> float:
        """
        Calculate price impact of a trade as a percentage.
        
        Returns:
            Price impact as a decimal (e.g., 0.02 = 2% impact)
        """
        if reserve_in == 0 or reserve_out == 0:
            return 1.0
        spot_price = reserve_out / reserve_in
        output = UniswapV2Analyzer.get_output_amount(
            amount_in, reserve_in, reserve_out, fee
        )
        if amount_in == 0:
            return 0.0
        exec_price = output / amount_in
        impact = 1 - (exec_price / spot_price)
        return abs(impact)
    
    @staticmethod
    def get_k(reserve_0: float, reserve_1: float) -> float:
        """Calculate the constant product k."""
        return reserve_0 * reserve_1
    
    @staticmethod
    def optimal_liquidity(
        amount_0: float,
        reserve_0: float,
        reserve_1: float,
    ) -> Tuple[float, float]:
        """
        Calculate optimal token amounts for adding liquidity.
        
        Given an amount of token0, returns the required amount of token1
        to maintain the pool ratio.
        """
        if reserve_0 == 0:
            return amount_0, 0.0
        amount_1 = amount_0 * reserve_1 / reserve_0
        return amount_0, amount_1
    
    @staticmethod
    def lp_share(
        liquidity_added: float,
        total_liquidity: float,
    ) -> float:
        """Calculate LP share percentage."""
        total = total_liquidity + liquidity_added
        if total == 0:
            return 0.0
        return liquidity_added / total


# ═════════════════════════════════════════════════════════════
# UNISWAP V3 CONCENTRATED LIQUIDITY ANALYZER
# ═════════════════════════════════════════════════════════════

class UniswapV3Analyzer:
    """
    Uniswap V3 concentrated liquidity analyzer.
    
    V3 uses ticks and concentrated positions. Liquidity is provided
    within price ranges instead of across the full curve.
    """
    
    TICK_BASE = 1.0001
    MIN_TICK = -887272
    MAX_TICK = 887272
    Q96 = 2 ** 96
    
    @staticmethod
    def tick_to_price(tick: int) -> float:
        """Convert a tick to a price."""
        return UniswapV3Analyzer.TICK_BASE ** tick
    
    @staticmethod
    def price_to_tick(price: float) -> int:
        """Convert a price to the nearest tick."""
        if price <= 0:
            return UniswapV3Analyzer.MIN_TICK
        return int(math.log(price) / math.log(UniswapV3Analyzer.TICK_BASE))
    
    @staticmethod
    def sqrt_price_x96_to_price(sqrt_price_x96: int, decimals_0: int = 18, decimals_1: int = 18) -> float:
        """Convert sqrtPriceX96 to human-readable price."""
        price = (sqrt_price_x96 / UniswapV3Analyzer.Q96) ** 2
        return price * (10 ** (decimals_0 - decimals_1))
    
    @staticmethod
    def liquidity_for_amounts(
        sqrt_price_current: float,
        sqrt_price_lower: float,
        sqrt_price_upper: float,
        amount_0: float,
        amount_1: float,
    ) -> float:
        """
        Calculate liquidity for given token amounts and price range.
        
        Based on the Uniswap V3 whitepaper formulas.
        """
        if sqrt_price_current <= sqrt_price_lower:
            # Below range — all in token0
            if amount_0 == 0:
                return 0.0
            return amount_0 * sqrt_price_lower * sqrt_price_upper / (sqrt_price_upper - sqrt_price_lower)
        elif sqrt_price_current >= sqrt_price_upper:
            # Above range — all in token1
            if amount_1 == 0:
                return 0.0
            return amount_1 / (sqrt_price_upper - sqrt_price_lower)
        else:
            # In range — need both tokens
            liq_0 = amount_0 * sqrt_price_current * sqrt_price_upper / (sqrt_price_upper - sqrt_price_current)
            liq_1 = amount_1 / (sqrt_price_current - sqrt_price_lower)
            return min(liq_0, liq_1)
    
    @staticmethod
    def amounts_for_liquidity(
        liquidity: float,
        sqrt_price_current: float,
        sqrt_price_lower: float,
        sqrt_price_upper: float,
    ) -> Tuple[float, float]:
        """Calculate token amounts for a given liquidity and price range."""
        if sqrt_price_current <= sqrt_price_lower:
            amount_0 = liquidity * (sqrt_price_upper - sqrt_price_lower) / (sqrt_price_lower * sqrt_price_upper)
            amount_1 = 0.0
        elif sqrt_price_current >= sqrt_price_upper:
            amount_0 = 0.0
            amount_1 = liquidity * (sqrt_price_upper - sqrt_price_lower)
        else:
            amount_0 = liquidity * (sqrt_price_upper - sqrt_price_current) / (sqrt_price_current * sqrt_price_upper)
            amount_1 = liquidity * (sqrt_price_current - sqrt_price_lower)
        return amount_0, amount_1
    
    @staticmethod
    def fee_growth_in_range(
        fee_growth_global_0: float,
        fee_growth_global_1: float,
        fee_growth_outside_lower_0: float,
        fee_growth_outside_lower_1: float,
        fee_growth_outside_upper_0: float,
        fee_growth_outside_upper_1: float,
        tick_current: int,
        tick_lower: int,
        tick_upper: int,
    ) -> Tuple[float, float]:
        """Calculate accumulated fees within a position's range."""
        if tick_current >= tick_lower:
            fee_below_0 = fee_growth_outside_lower_0
            fee_below_1 = fee_growth_outside_lower_1
        else:
            fee_below_0 = fee_growth_global_0 - fee_growth_outside_lower_0
            fee_below_1 = fee_growth_global_1 - fee_growth_outside_lower_1
        
        if tick_current < tick_upper:
            fee_above_0 = fee_growth_outside_upper_0
            fee_above_1 = fee_growth_outside_upper_1
        else:
            fee_above_0 = fee_growth_global_0 - fee_growth_outside_upper_0
            fee_above_1 = fee_growth_global_1 - fee_growth_outside_upper_1
        
        fee_in_range_0 = fee_growth_global_0 - fee_below_0 - fee_above_0
        fee_in_range_1 = fee_growth_global_1 - fee_below_1 - fee_above_1
        
        return fee_in_range_0, fee_in_range_1
    
    @staticmethod
    def capital_efficiency(
        tick_lower: int,
        tick_upper: int,
    ) -> float:
        """
        Calculate capital efficiency multiplier vs V2 full range.
        
        Narrower ranges = higher efficiency but more IL risk.
        """
        price_lower = UniswapV3Analyzer.tick_to_price(tick_lower)
        price_upper = UniswapV3Analyzer.tick_to_price(tick_upper)
        if price_lower <= 0 or price_upper <= price_lower:
            return 1.0
        sqrt_lower = math.sqrt(price_lower)
        sqrt_upper = math.sqrt(price_upper)
        # Full range efficiency relative to concentrated position
        return 1.0 / (1.0 - sqrt_lower / sqrt_upper)
```


---

## Impermanent Loss Calculator

# Impermanent Loss Calculator

```python
class ImpermanentLossCalculator:
    """
    Complete impermanent loss analysis for AMM liquidity provision.
    
    Covers:
    - Standard IL formula for V2 constant product AMMs
    - V3 concentrated liquidity IL
    - IL with fee compensation
    - Break-even analysis
    - Multi-asset IL
    - IL hedging strategies
    """
    
    @staticmethod
    def v2_impermanent_loss(price_ratio: float) -> float:
        """
        Calculate impermanent loss for Uniswap V2 (constant product).
        
        Args:
            price_ratio: Current price / initial price (e.g., 1.5 = 50% increase)
        
        Returns:
            IL as a negative decimal (e.g., -0.0566 = -5.66% loss vs HODL)
        """
        if price_ratio <= 0:
            return -1.0
        sqrt_ratio = math.sqrt(price_ratio)
        il = 2 * sqrt_ratio / (1 + price_ratio) - 1
        return il
    
    @staticmethod
    def v2_il_percentage(price_ratio: float) -> float:
        """IL as a positive percentage (convenience)."""
        return abs(ImpermanentLossCalculator.v2_impermanent_loss(price_ratio)) * 100
    
    @staticmethod
    def v3_impermanent_loss(
        price_initial: float,
        price_current: float,
        price_lower: float,
        price_upper: float,
    ) -> float:
        """
        Calculate impermanent loss for Uniswap V3 concentrated position.
        
        Concentrated liquidity amplifies both fees earned AND impermanent loss.
        IL can be significantly worse than V2 for narrow ranges.
        
        Args:
            price_initial: Price when position was opened
            price_current: Current price
            price_lower: Lower bound of liquidity range
            price_upper: Upper bound of liquidity range
        """
        if price_current <= 0 or price_initial <= 0:
            return -1.0
        
        # Clamp prices to range
        p0 = max(min(price_initial, price_upper), price_lower)
        p1 = max(min(price_current, price_upper), price_lower)
        
        sqrt_p0 = math.sqrt(p0)
        sqrt_p1 = math.sqrt(p1)
        sqrt_pa = math.sqrt(price_lower)
        sqrt_pb = math.sqrt(price_upper)
        
        # Value at current price
        if price_current <= price_lower:
            # All in token0
            value_current = sqrt_pb - sqrt_pa
        elif price_current >= price_upper:
            # All in token1
            value_current = (sqrt_pb - sqrt_pa) * price_current / sqrt_pb
        else:
            value_current = (sqrt_p1 - sqrt_pa) * sqrt_p1 + (sqrt_pb - sqrt_p1)
        
        # Value if just held
        if price_initial <= price_lower:
            value_hodl = (sqrt_pb - sqrt_pa) * price_current / price_initial
        elif price_initial >= price_upper:
            value_hodl = (sqrt_pb - sqrt_pa)
        else:
            value_hodl_token0 = (sqrt_pb - sqrt_p0) * price_current / price_initial
            value_hodl_token1 = (sqrt_p0 - sqrt_pa) * sqrt_p0
            value_hodl = value_hodl_token0 + value_hodl_token1
        
        if value_hodl == 0:
            return 0.0
        
        return (value_current - value_hodl) / value_hodl
    
    @staticmethod
    def il_with_fees(
        price_ratio: float,
        fee_tier: float,
        volume_to_tvl_daily: float,
        days: int,
    ) -> dict:
        """
        Calculate net IL after fee compensation.
        
        Args:
            price_ratio: Current price / initial price
            fee_tier: Pool fee tier (e.g., 0.003)
            volume_to_tvl_daily: Daily volume/TVL ratio
            days: Number of days position has been open
        
        Returns:
            Dict with il, fees_earned, net_pnl (all as percentages)
        """
        il_pct = ImpermanentLossCalculator.v2_il_percentage(price_ratio)
        daily_fee_yield = fee_tier * volume_to_tvl_daily * 100
        total_fees = daily_fee_yield * days
        net_pnl = total_fees - il_pct
        
        return {
            "impermanent_loss_pct": round(il_pct, 4),
            "fees_earned_pct": round(total_fees, 4),
            "net_pnl_pct": round(net_pnl, 4),
            "days_to_breakeven": round(il_pct / daily_fee_yield, 1) if daily_fee_yield > 0 else float("inf"),
            "daily_fee_yield_pct": round(daily_fee_yield, 4),
            "annualized_fee_yield_pct": round(daily_fee_yield * 365, 2),
            "compensated": net_pnl >= 0,
        }
    
    @staticmethod
    def il_table(price_changes: List[float] = None) -> pd.DataFrame:
        """
        Generate an IL reference table for common price changes.
        
        Returns DataFrame with columns: price_change_pct, price_ratio, il_pct
        """
        if price_changes is None:
            price_changes = [-90, -80, -70, -60, -50, -40, -30, -25, -20, -15, -10, -5,
                             0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100,
                             150, 200, 300, 400, 500]
        rows = []
        for pct in price_changes:
            ratio = 1 + pct / 100
            if ratio <= 0:
                continue
            il = ImpermanentLossCalculator.v2_il_percentage(ratio)
            rows.append({
                "price_change_pct": pct,
                "price_ratio": round(ratio, 2),
                "il_pct": round(il, 4),
            })
        return pd.DataFrame(rows)
    
    @staticmethod
    def breakeven_volume(
        price_ratio: float,
        fee_tier: float,
        tvl: float,
        days: int,
    ) -> float:
        """
        Calculate the daily volume needed to offset IL with fees.
        
        Returns required daily volume in USD.
        """
        il_pct = ImpermanentLossCalculator.v2_il_percentage(price_ratio) / 100
        il_usd = il_pct * tvl
        if days == 0 or fee_tier == 0:
            return float("inf")
        required_daily_fees = il_usd / days
        required_daily_volume = required_daily_fees / fee_tier
        return required_daily_volume
```


---

## On-Chain Analytics

# On-Chain Analytics

```python
class OnChainAnalytics:
    """
    On-chain data analysis for trading intelligence.
    
    Tracks:
    - Exchange netflow (bullish/bearish indicator)
    - Whale activity and accumulation
    - Network health metrics
    - Active address trends
    - Token holder distribution
    - Smart money flows
    """
    
    @staticmethod
    def exchange_netflow(
        inflow_usd: float,
        outflow_usd: float,
    ) -> dict:
        """
        Analyze exchange netflow.
        
        Positive netflow (more inflow) = bearish (coins moving to exchange to sell)
        Negative netflow (more outflow) = bullish (coins leaving exchange = accumulation)
        
        Args:
            inflow_usd: Total USD value flowing INTO exchanges
            outflow_usd: Total USD value flowing OUT of exchanges
        """
        netflow = inflow_usd - outflow_usd
        total_flow = inflow_usd + outflow_usd
        
        if total_flow == 0:
            bias = "neutral"
            strength = 0.0
        else:
            ratio = netflow / total_flow
            if ratio > 0.1:
                bias = "strongly_bearish"
                strength = min(abs(ratio) * 5, 1.0)
            elif ratio > 0.03:
                bias = "bearish"
                strength = min(abs(ratio) * 5, 1.0)
            elif ratio < -0.1:
                bias = "strongly_bullish"
                strength = min(abs(ratio) * 5, 1.0)
            elif ratio < -0.03:
                bias = "bullish"
                strength = min(abs(ratio) * 5, 1.0)
            else:
                bias = "neutral"
                strength = 0.2
        
        return {
            "netflow_usd": round(netflow, 2),
            "inflow_usd": round(inflow_usd, 2),
            "outflow_usd": round(outflow_usd, 2),
            "netflow_ratio": round(netflow / total_flow, 4) if total_flow > 0 else 0,
            "bias": bias,
            "strength": round(strength, 2),
            "interpretation": (
                "Coins flowing TO exchanges — sell pressure likely"
                if netflow > 0
                else "Coins flowing FROM exchanges — accumulation signal"
            ),
        }
    
    @staticmethod
    def whale_activity_score(
        transactions: List[dict],
        min_usd: float = 1_000_000,
    ) -> dict:
        """
        Analyze whale transaction activity.
        
        Args:
            transactions: List of dicts with keys: from, to, value_usd, is_exchange_deposit, 
                         is_exchange_withdrawal, timestamp
            min_usd: Minimum USD value to count as whale transaction
        
        Returns:
            Dict with whale metrics and directional bias
        """
        whale_txs = [tx for tx in transactions if tx.get("value_usd", 0) >= min_usd]
        
        if not whale_txs:
            return {
                "whale_tx_count": 0,
                "total_whale_volume": 0,
                "exchange_deposits": 0,
                "exchange_withdrawals": 0,
                "bias": "neutral",
                "score": 0.0,
            }
        
        total_volume = sum(tx.get("value_usd", 0) for tx in whale_txs)
        deposits = sum(
            tx.get("value_usd", 0)
            for tx in whale_txs
            if tx.get("is_exchange_deposit", False)
        )
        withdrawals = sum(
            tx.get("value_usd", 0)
            for tx in whale_txs
            if tx.get("is_exchange_withdrawal", False)
        )
        
        # Score: -1 (bearish) to +1 (bullish)
        if deposits + withdrawals > 0:
            score = (withdrawals - deposits) / (deposits + withdrawals)
        else:
            score = 0.0
        
        if score > 0.3:
            bias = "bullish"
        elif score < -0.3:
            bias = "bearish"
        else:
            bias = "neutral"
        
        return {
            "whale_tx_count": len(whale_txs),
            "total_whale_volume": round(total_volume, 2),
            "exchange_deposits": round(deposits, 2),
            "exchange_withdrawals": round(withdrawals, 2),
            "net_whale_flow": round(withdrawals - deposits, 2),
            "bias": bias,
            "score": round(score, 3),
        }
    
    @staticmethod
    def holder_distribution(
        holders: List[dict],
    ) -> dict:
        """
        Analyze token holder distribution (concentration risk).
        
        Args:
            holders: List of dicts with keys: address, balance, balance_usd
        
        Returns:
            Gini coefficient, top holder concentration, distribution tiers
        """
        if not holders:
            return {"error": "No holder data"}
        
        balances = sorted([h.get("balance", 0) for h in holders], reverse=True)
        total = sum(balances)
        
        if total == 0:
            return {"error": "Zero total balance"}
        
        n = len(balances)
        
        # Gini coefficient
        cumulative = np.cumsum(sorted(balances))
        gini = 1 - 2 * np.sum(cumulative) / (n * total) + 1 / n
        
        # Top holder concentration
        top_1_pct = balances[0] / total if n >= 1 else 0
        top_10_pct = sum(balances[:10]) / total if n >= 10 else sum(balances) / total
        top_50_pct = sum(balances[:50]) / total if n >= 50 else sum(balances) / total
        
        # Distribution tiers
        whale_threshold = total * 0.01  # 1% of supply
        shark_threshold = total * 0.001  # 0.1%
        
        whales = sum(1 for b in balances if b >= whale_threshold)
        sharks = sum(1 for b in balances if shark_threshold <= b < whale_threshold)
        fish = sum(1 for b in balances if b < shark_threshold)
        
        # Risk assessment
        if top_10_pct > 0.8:
            concentration_risk = "EXTREME"
        elif top_10_pct > 0.6:
            concentration_risk = "HIGH"
        elif top_10_pct > 0.4:
            concentration_risk = "MODERATE"
        else:
            concentration_risk = "LOW"
        
        return {
            "total_holders": n,
            "gini_coefficient": round(gini, 4),
            "top_1_holder_pct": round(top_1_pct * 100, 2),
            "top_10_holders_pct": round(top_10_pct * 100, 2),
            "top_50_holders_pct": round(top_50_pct * 100, 2),
            "whales": whales,
            "sharks": sharks,
            "fish": fish,
            "concentration_risk": concentration_risk,
        }
    
    @staticmethod
    def network_health(
        active_addresses_24h: int,
        active_addresses_7d_avg: int,
        transactions_24h: int,
        transactions_7d_avg: int,
        hash_rate_current: float = 0,
        hash_rate_7d_avg: float = 0,
    ) -> dict:
        """
        Assess network health based on on-chain activity.
        
        Growing activity = bullish fundamental backdrop.
        Declining activity = bearish fundamental backdrop.
        """
        addr_growth = (
            (active_addresses_24h / active_addresses_7d_avg - 1) * 100
            if active_addresses_7d_avg > 0
            else 0
        )
        tx_growth = (
            (transactions_24h / transactions_7d_avg - 1) * 100
            if transactions_7d_avg > 0
            else 0
        )
        hash_growth = (
            (hash_rate_current / hash_rate_7d_avg - 1) * 100
            if hash_rate_7d_avg > 0
            else 0
        )
        
        # Composite score (-100 to +100)
        score = (addr_growth * 0.4 + tx_growth * 0.4 + hash_growth * 0.2)
        score = max(min(score, 100), -100)
        
        if score > 15:
            health = "STRONG"
        elif score > 5:
            health = "HEALTHY"
        elif score > -5:
            health = "NEUTRAL"
        elif score > -15:
            health = "WEAK"
        else:
            health = "DECLINING"
        
        return {
            "active_addresses_24h": active_addresses_24h,
            "address_growth_pct": round(addr_growth, 2),
            "transactions_24h": transactions_24h,
            "tx_growth_pct": round(tx_growth, 2),
            "hash_rate_growth_pct": round(hash_growth, 2),
            "composite_score": round(score, 2),
            "health": health,
        }
```


---

## MEV Detection & Analysis

# MEV Detection & Analysis

```python
class MEVDetector:
    """
    Maximal Extractable Value (MEV) opportunity detection and analysis.
    
    Covers:
    - Sandwich attack detection on pending transactions
    - Cross-DEX arbitrage opportunity detection
    - Liquidation opportunity scanning
    - Backrunning opportunity detection
    - Gas price optimization
    - MEV protection strategies
    """
    
    @staticmethod
    def detect_sandwich_opportunity(
        pending_tx_amount: float,
        pool_reserve_in: float,
        pool_reserve_out: float,
        fee: float = 0.003,
        gas_cost_usd: float = 5.0,
    ) -> dict:
        """
        Detect if a pending transaction is vulnerable to a sandwich attack.
        
        A sandwich attack front-runs a victim's swap (buying before them to push
        price up), then back-runs (selling after them at the higher price).
        
        Args:
            pending_tx_amount: Amount the victim is swapping
            pool_reserve_in: Pool reserve of input token
            pool_reserve_out: Pool reserve of output token
            fee: Pool fee tier
            gas_cost_usd: Estimated gas cost for the sandwich (2 txs)
        """
        # Calculate price impact of victim's trade
        victim_output = UniswapV2Analyzer.get_output_amount(
            pending_tx_amount, pool_reserve_in, pool_reserve_out, fee
        )
        victim_impact = UniswapV2Analyzer.get_price_impact(
            pending_tx_amount, pool_reserve_in, pool_reserve_out, fee
        )
        
        if victim_impact < 0.001:
            return {
                "opportunity": False,
                "reason": "Price impact too small to sandwich",
                "victim_impact_pct": round(victim_impact * 100, 4),
            }
        
        # Optimal frontrun size (simplified): roughly equal to victim trade
        frontrun_amount = pending_tx_amount * 0.5
        
        # Step 1: Frontrun — buy before victim
        frontrun_output = UniswapV2Analyzer.get_output_amount(
            frontrun_amount, pool_reserve_in, pool_reserve_out, fee
        )
        
        # Updated reserves after frontrun
        new_reserve_in = pool_reserve_in + frontrun_amount
        new_reserve_out = pool_reserve_out - frontrun_output
        
        # Step 2: Victim trades (at worse price)
        victim_output_after = UniswapV2Analyzer.get_output_amount(
            pending_tx_amount, new_reserve_in, new_reserve_out, fee
        )
        
        # Updated reserves after victim
        new_reserve_in_2 = new_reserve_in + pending_tx_amount
        new_reserve_out_2 = new_reserve_out - victim_output_after
        
        # Step 3: Backrun — sell the frontrun tokens
        backrun_output = UniswapV2Analyzer.get_output_amount(
            frontrun_output, new_reserve_out_2, new_reserve_in_2, fee
        )
        
        profit = backrun_output - frontrun_amount - gas_cost_usd
        
        return {
            "opportunity": profit > 0,
            "estimated_profit_usd": round(profit, 2),
            "frontrun_amount": round(frontrun_amount, 4),
            "victim_impact_pct": round(victim_impact * 100, 4),
            "victim_extra_slippage_pct": round(
                (1 - victim_output_after / victim_output) * 100, 4
            ),
            "gas_cost_usd": gas_cost_usd,
            "profit_after_gas": round(profit, 2),
            "warning": "MEV exploitation is ethically controversial. Use for defense/awareness only.",
        }
    
    @staticmethod
    def detect_cross_dex_arbitrage(
        dex_prices: Dict[str, float],
        trade_size_usd: float = 10000,
        gas_cost_usd: float = 10.0,
    ) -> List[dict]:
        """
        Detect cross-DEX arbitrage opportunities.
        
        Args:
            dex_prices: Dict of DEX name → price for the same pair
            trade_size_usd: Size of arbitrage trade
            gas_cost_usd: Total gas cost for the round trip
        
        Returns:
            List of arbitrage opportunities sorted by profit
        """
        opportunities = []
        dex_list = list(dex_prices.items())
        
        for i, (dex_buy, price_buy) in enumerate(dex_list):
            for j, (dex_sell, price_sell) in enumerate(dex_list):
                if i == j:
                    continue
                
                # Buy low, sell high
                if price_sell > price_buy:
                    spread_pct = (price_sell - price_buy) / price_buy * 100
                    tokens_bought = trade_size_usd / price_buy
                    revenue = tokens_bought * price_sell
                    profit = revenue - trade_size_usd - gas_cost_usd
                    
                    if profit > 0:
                        opportunities.append({
                            "buy_dex": dex_buy,
                            "sell_dex": dex_sell,
                            "buy_price": round(price_buy, 6),
                            "sell_price": round(price_sell, 6),
                            "spread_pct": round(spread_pct, 4),
                            "trade_size_usd": trade_size_usd,
                            "estimated_profit_usd": round(profit, 2),
                            "profit_pct": round(profit / trade_size_usd * 100, 4),
                            "gas_cost_usd": gas_cost_usd,
                        })
        
        return sorted(opportunities, key=lambda x: x["estimated_profit_usd"], reverse=True)
    
    @staticmethod
    def detect_liquidation_opportunities(
        positions: List[dict],
        current_prices: Dict[str, float],
    ) -> List[dict]:
        """
        Detect DeFi lending positions approaching liquidation.
        
        Args:
            positions: List of dicts with keys: owner, collateral_token, collateral_amount,
                      debt_token, debt_amount, liquidation_threshold, collateral_price_at_open
            current_prices: Dict of token → current price
        """
        opportunities = []
        
        for pos in positions:
            collateral_token = pos.get("collateral_token", "")
            debt_token = pos.get("debt_token", "")
            current_collateral_price = current_prices.get(collateral_token, 0)
            current_debt_price = current_prices.get(debt_token, 1)
            
            if current_collateral_price == 0:
                continue
            
            collateral_value = pos.get("collateral_amount", 0) * current_collateral_price
            debt_value = pos.get("debt_amount", 0) * current_debt_price
            liq_threshold = pos.get("liquidation_threshold", 0.8)
            
            if collateral_value == 0:
                continue
            
            health_factor = (collateral_value * liq_threshold) / debt_value if debt_value > 0 else float("inf")
            ltv = debt_value / collateral_value
            
            # Distance to liquidation (price drop needed)
            liq_price = (debt_value / (pos.get("collateral_amount", 1) * liq_threshold))
            distance_to_liq = (current_collateral_price - liq_price) / current_collateral_price
            
            if health_factor < 1.1:  # Within 10% of liquidation
                # Liquidation bonus (typically 5-10%)
                liq_bonus_pct = 0.05
                profit = collateral_value * liq_bonus_pct - debt_value * 0.01  # Approximate gas
                
                opportunities.append({
                    "owner": pos.get("owner", "unknown"),
                    "collateral_token": collateral_token,
                    "debt_token": debt_token,
                    "collateral_value_usd": round(collateral_value, 2),
                    "debt_value_usd": round(debt_value, 2),
                    "health_factor": round(health_factor, 4),
                    "ltv": round(ltv * 100, 2),
                    "distance_to_liq_pct": round(distance_to_liq * 100, 2),
                    "estimated_profit_usd": round(profit, 2),
                    "urgency": "IMMINENT" if health_factor < 1.01 else "APPROACHING",
                })
        
        return sorted(opportunities, key=lambda x: x["health_factor"])


# ═════════════════════════════════════════════════════════════
# GAS OPTIMIZER
# ═════════════════════════════════════════════════════════════

class GasOptimizer:
    """Gas price analysis and optimization for transaction timing."""
    
    @staticmethod
    def analyze_gas_history(
        gas_prices: List[dict],
    ) -> dict:
        """
        Analyze historical gas prices to find optimal trading windows.
        
        Args:
            gas_prices: List of dicts with keys: timestamp, gas_gwei, block_number
        """
        if not gas_prices:
            return {"error": "No gas data"}
        
        prices = [g.get("gas_gwei", 0) for g in gas_prices]
        
        # Hourly averages
        hourly = {}
        for g in gas_prices:
            ts = g.get("timestamp")
            if ts and hasattr(ts, "hour"):
                hour = ts.hour
                if hour not in hourly:
                    hourly[hour] = []
                hourly[hour].append(g.get("gas_gwei", 0))
        
        hourly_avg = {h: round(np.mean(v), 1) for h, v in hourly.items()}
        cheapest_hour = min(hourly_avg, key=hourly_avg.get) if hourly_avg else 0
        
        return {
            "current_gwei": round(prices[-1] if prices else 0, 1),
            "avg_gwei": round(np.mean(prices), 1),
            "median_gwei": round(np.median(prices), 1),
            "min_gwei": round(min(prices), 1),
            "max_gwei": round(max(prices), 1),
            "p25_gwei": round(np.percentile(prices, 25), 1),
            "p75_gwei": round(np.percentile(prices, 75), 1),
            "cheapest_hour_utc": cheapest_hour,
            "cheapest_hour_avg_gwei": hourly_avg.get(cheapest_hour, 0),
            "hourly_averages": hourly_avg,
            "recommendation": (
                f"Best time to transact: ~{cheapest_hour}:00 UTC "
                f"(avg {hourly_avg.get(cheapest_hour, 0)} gwei)"
            ),
        }
    
    @staticmethod
    def estimate_cost(
        gas_limit: int,
        gas_price_gwei: float,
        eth_price_usd: float,
    ) -> dict:
        """Estimate transaction cost in USD."""
        gas_cost_eth = gas_limit * gas_price_gwei * 1e-9
        gas_cost_usd = gas_cost_eth * eth_price_usd
        return {
            "gas_limit": gas_limit,
            "gas_price_gwei": gas_price_gwei,
            "cost_eth": round(gas_cost_eth, 6),
            "cost_usd": round(gas_cost_usd, 2),
        }
```


---

## Yield Farming Analyzer

# Yield Farming Analyzer

```python
class YieldFarmingAnalyzer:
    """
    DeFi yield farming analysis and comparison.
    
    Covers:
    - APY/APR calculation with compounding
    - Farming strategy comparison
    - Risk-adjusted yield analysis
    - Auto-compound optimization
    - Farming P&L tracking
    """
    
    @staticmethod
    def calculate_apy(
        apr: float,
        compounds_per_year: int = 365,
    ) -> float:
        """
        Convert APR to APY with compounding.
        
        APY = (1 + APR/n)^n - 1
        
        Args:
            apr: Annual Percentage Rate as decimal (e.g., 0.5 = 50%)
            compounds_per_year: Number of compounding periods
        """
        if compounds_per_year == 0:
            return apr
        return (1 + apr / compounds_per_year) ** compounds_per_year - 1
    
    @staticmethod
    def calculate_apr(
        daily_reward_usd: float,
        total_staked_usd: float,
    ) -> float:
        """Calculate APR from daily rewards."""
        if total_staked_usd == 0:
            return 0.0
        return (daily_reward_usd * 365) / total_staked_usd
    
    @staticmethod
    def compare_farms(
        farms: List[dict],
    ) -> pd.DataFrame:
        """
        Compare yield farming opportunities.
        
        Args:
            farms: List of dicts with keys: name, apr, tvl_usd, token_reward,
                   il_risk (low/medium/high), smart_contract_risk (low/medium/high),
                   chain, protocol
        """
        rows = []
        for farm in farms:
            apr = farm.get("apr", 0)
            apy = YieldFarmingAnalyzer.calculate_apy(apr / 100) * 100
            
            # Risk score (1-10, lower is better)
            il_scores = {"low": 2, "medium": 5, "high": 8}
            sc_scores = {"low": 1, "medium": 4, "high": 7}
            il_risk = il_scores.get(farm.get("il_risk", "medium"), 5)
            sc_risk = sc_scores.get(farm.get("smart_contract_risk", "medium"), 4)
            risk_score = (il_risk + sc_risk) / 2
            
            # Risk-adjusted yield: APR / risk_score
            risk_adjusted = apr / risk_score if risk_score > 0 else 0
            
            rows.append({
                "name": farm.get("name", ""),
                "protocol": farm.get("protocol", ""),
                "chain": farm.get("chain", ""),
                "apr_pct": round(apr, 2),
                "apy_pct": round(apy, 2),
                "tvl_usd": farm.get("tvl_usd", 0),
                "reward_token": farm.get("token_reward", ""),
                "il_risk": farm.get("il_risk", "medium"),
                "sc_risk": farm.get("smart_contract_risk", "medium"),
                "risk_score": round(risk_score, 1),
                "risk_adjusted_yield": round(risk_adjusted, 2),
            })
        
        df = pd.DataFrame(rows)
        return df.sort_values("risk_adjusted_yield", ascending=False).reset_index(drop=True)
    
    @staticmethod
    def optimal_compound_frequency(
        apr: float,
        gas_cost_usd: float,
        position_size_usd: float,
    ) -> dict:
        """
        Calculate the optimal compounding frequency.
        
        More frequent compounding increases APY but costs more gas.
        Find the sweet spot that maximizes net yield.
        """
        best_freq = 1
        best_net_yield = 0
        results = []
        
        for freq in [1, 2, 4, 7, 14, 30, 90, 182, 365]:
            compounds_per_year = 365 / freq
            apy = YieldFarmingAnalyzer.calculate_apy(apr, int(compounds_per_year))
            total_gas_cost = gas_cost_usd * compounds_per_year
            gross_yield = position_size_usd * apy
            net_yield = gross_yield - total_gas_cost
            net_apy = net_yield / position_size_usd if position_size_usd > 0 else 0
            
            results.append({
                "compound_every_days": freq,
                "compounds_per_year": int(compounds_per_year),
                "gross_apy_pct": round(apy * 100, 2),
                "gas_cost_annual": round(total_gas_cost, 2),
                "net_yield_usd": round(net_yield, 2),
                "net_apy_pct": round(net_apy * 100, 2),
            })
            
            if net_yield > best_net_yield:
                best_net_yield = net_yield
                best_freq = freq
        
        return {
            "optimal_frequency_days": best_freq,
            "optimal_net_apy_pct": round(best_net_yield / position_size_usd * 100, 2) if position_size_usd > 0 else 0,
            "all_frequencies": results,
        }
```


---

## DeFi Risk Analyzer

# DeFi Risk Analyzer

```python
class DeFiRiskAnalyzer:
    """
    Comprehensive DeFi protocol and position risk analysis.
    
    Evaluates:
    - Smart contract risk (audit status, age, TVL)
    - Liquidity risk (depth, concentration)
    - Oracle risk (price feed reliability)
    - Governance risk (centralization, admin keys)
    - Market risk (volatility, correlation)
    - Composability risk (dependency chains)
    """
    
    @staticmethod
    def protocol_risk_score(
        has_audit: bool = False,
        audit_firms: int = 0,
        age_days: int = 0,
        tvl_usd: float = 0,
        bug_bounty_usd: float = 0,
        has_timelock: bool = False,
        has_multisig: bool = False,
        is_upgradeable: bool = True,
        has_admin_key: bool = True,
        fork_of: str = "",
        open_source: bool = True,
    ) -> dict:
        """
        Calculate a comprehensive protocol risk score (0-100, lower = safer).
        """
        score = 50  # Start at medium risk
        factors = []
        
        # Audit status (up to -20)
        if has_audit:
            score -= 10
            factors.append("Audited (-10)")
            if audit_firms >= 2:
                score -= 5
                factors.append("Multiple audits (-5)")
            if audit_firms >= 3:
                score -= 5
                factors.append("3+ audit firms (-5)")
        else:
            score += 15
            factors.append("No audit (+15)")
        
        # Age (up to -15)
        if age_days > 365:
            score -= 15
            factors.append("1+ year old (-15)")
        elif age_days > 180:
            score -= 10
            factors.append("6+ months old (-10)")
        elif age_days > 90:
            score -= 5
            factors.append("3+ months old (-5)")
        else:
            score += 10
            factors.append("Very new protocol (+10)")
        
        # TVL
        if tvl_usd > 1_000_000_000:
            score -= 10
            factors.append("$1B+ TVL (-10)")
        elif tvl_usd > 100_000_000:
            score -= 5
            factors.append("$100M+ TVL (-5)")
        elif tvl_usd < 1_000_000:
            score += 10
            factors.append("Low TVL (<$1M) (+10)")
        
        # Bug bounty
        if bug_bounty_usd > 1_000_000:
            score -= 5
            factors.append("Large bug bounty (-5)")
        elif bug_bounty_usd > 0:
            score -= 2
            factors.append("Has bug bounty (-2)")
        
        # Governance
        if has_timelock:
            score -= 5
            factors.append("Timelock (-5)")
        if has_multisig:
            score -= 5
            factors.append("Multisig (-5)")
        if not is_upgradeable:
            score -= 5
            factors.append("Immutable (-5)")
        if has_admin_key:
            score += 10
            factors.append("Admin key (+10)")
        if not open_source:
            score += 15
            factors.append("Closed source (+15)")
        
        # Clamp
        score = max(0, min(100, score))
        
        if score < 25:
            risk_level = "LOW"
        elif score < 50:
            risk_level = "MODERATE"
        elif score < 75:
            risk_level = "HIGH"
        else:
            risk_level = "EXTREME"
        
        return {
            "risk_score": score,
            "risk_level": risk_level,
            "factors": factors,
            "recommendation": (
                "Acceptable for large allocations"
                if score < 25
                else "Use with caution, limit exposure"
                if score < 50
                else "High risk — small allocations only"
                if score < 75
                else "Extreme risk — avoid or use minimal amounts"
            ),
        }
    
    @staticmethod
    def position_risk_assessment(
        position_value_usd: float,
        portfolio_total_usd: float,
        protocol_risk_score: int,
        il_risk_pct: float,
        token_volatility_30d: float,
        is_stablecoin_pair: bool = False,
    ) -> dict:
        """
        Assess risk for a specific DeFi position.
        """
        # Concentration risk
        allocation_pct = (
            position_value_usd / portfolio_total_usd * 100
            if portfolio_total_usd > 0
            else 100
        )
        
        # Max recommended allocation based on protocol risk
        if protocol_risk_score < 25:
            max_allocation = 30
        elif protocol_risk_score < 50:
            max_allocation = 15
        elif protocol_risk_score < 75:
            max_allocation = 5
        else:
            max_allocation = 2
        
        # Adjust for stablecoin pairs (lower risk)
        if is_stablecoin_pair:
            max_allocation = min(max_allocation * 2, 50)
        
        # Risk-adjusted expected loss
        expected_il = il_risk_pct / 100
        protocol_loss_prob = protocol_risk_score / 100 * 0.1  # Simplified
        expected_loss = position_value_usd * (expected_il + protocol_loss_prob)
        
        warnings = []
        if allocation_pct > max_allocation:
            warnings.append(
                f"Position too large: {allocation_pct:.1f}% vs recommended max {max_allocation}%"
            )
        if token_volatility_30d > 1.0:
            warnings.append(f"High token volatility: {token_volatility_30d:.0%} (30d)")
        if protocol_risk_score > 60:
            warnings.append("High protocol risk — consider reducing exposure")
        
        return {
            "position_value_usd": round(position_value_usd, 2),
            "allocation_pct": round(allocation_pct, 2),
            "max_recommended_allocation_pct": max_allocation,
            "protocol_risk_score": protocol_risk_score,
            "expected_il_pct": round(il_risk_pct, 2),
            "expected_loss_usd": round(expected_loss, 2),
            "token_volatility_30d": round(token_volatility_30d * 100, 1),
            "warnings": warnings,
            "within_limits": len(warnings) == 0,
        }
```

## SMC Application to Crypto — Beginner to Intermediate (Smart Risk)
*Source: video_037 — How to Trade Crypto Coins for Beginners*
- **BTC dominance rule:** Always check BTC D1 bias before trading any altcoin; alts amplify BTC moves (typical beta: ALT moves ~3x BTC % move)
- **SMT Divergence for crypto:** If BTC makes new high but ETH doesn't → BTC likely reverses; use at HTF POIs
- **Market cap tier rules:** Large cap (BTC/ETH) = SMC works cleanly; mid cap (SOL/BNB/ADA) = SMC works with some manipulation noise; small cap (<$500M) = insufficient liquidity for reliable SMC; micro cap = skip SMC, use only as speculative position
- **Volatility adjustments:** Use 1.5x ATR minimum for stops; target 3:1+ RR to compensate; wider OB zones expected
- **Session timing:** London open (08:00–10:00 UTC) and NY open (13:00–16:00 UTC) = highest quality crypto setups; avoid Asian session entries
- **Meme coin rule:** Position size = 1-2% max; enter only during early accumulation (unknown stage); never chase momentum
- **Weekend warning:** Lower volume weekends → erratic behavior → reduce position size or avoid entries entirely

## BTC Dominance Technical Setup & Altcoin Rotation (Smart Risk)
*Source: video_079 — How to Start Trading Crypto the Right Way*
- **Altcoin season signal:** BTC at/near ATH + BTC.D (Bitcoin Dominance) making D1 BOS downward = early altcoin season confirmed; capital rotating from BTC to altcoins
- **BTC.D technical reading:** Open BTC.D on TradingView; bearish BOS on D1 + bearish FVG on BTC.D = further dominance decline → alts outperform
- **Sequential rotation order:** Large-cap alts first (ETH, SOL, BNB) → once trend confirmed → mid-cap alts; never jump to micro-caps first
- **Entry timing in bull run:** Do NOT FOMO buy after 50-100% pump; wait for first meaningful pullback to H4/D1 FVG in discount zone; same SMC entry mechanics apply
- **Risk management in bull run:** 0.5-1% per altcoin; max 3% total crypto exposure; diversify across 3-5 alts
- **Exit signal for altcoin season:** BTC.D reverses (starts rising again) + BTC D1 shows LH → rotate back to BTC or cash; alts stop making new ATHs before BTC peaks

---

## Related Skills

- [Liquidity Analysis](../liquidity-analysis.md)
- [Ict Smart Money](../ict-smart-money.md)
- [Technical Analysis](../technical-analysis.md)
- [Risk And Portfolio](../risk-and-portfolio.md)
