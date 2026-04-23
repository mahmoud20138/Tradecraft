---
name: cow-protocol-sdk
description: CoW Protocol SDK — TypeScript monorepo for intent-based DEX trading with MEV protection. Coincidence of Wants (CoW): batch auction matching, solver network finds optimal routes. Order types: market, limit, TWAP (composable). 14 packages covering trad
kind: reference
category: trading/asset-classes
status: active
tags: [asset-classes, cow, protocol, sdk, trading, typescript]
related_skills: [crypto-defi-trading, equities-trading, forex-trading, futures-trading]
---

# cow-protocol-sdk

USE FOR:
  - "CoW Protocol / CoW Swap integration"
  - "MEV-protected DeFi trading"
  - "intent-based DEX order"
  - "TWAP on-chain order"
  - "limit order on DEX (crypto)"
  - "cross-chain swap / bridge"
  - "batch auction solver trading"
  - "TypeScript DeFi trading SDK"
tags: [CoW-Protocol, DeFi, DEX, MEV-protection, TWAP, limit-order, intent-based, Ethereum, TypeScript, solver, batch-auction]
kind: sdk
category: crypto-defi-trading

---

## What Is CoW Protocol?

Intent-based trading protocol with MEV protection via batch auctions and solver network.

- Repo: https://github.com/cowprotocol/cow-sdk
- Docs: docs.cow.fi
- Interface: swap.cow.fi (CoW Swap)
- Model: **Coincidence of Wants** — direct peer-to-peer matching when possible

### How CoW Works

```
User submits signed intent (not on-chain tx)
         ↓
Solver network competes to find best execution:
  Option A: CoW match   → peer-to-peer, no AMM needed (best price)
  Option B: AMM route   → Uniswap/Curve/etc. (fallback)
  Option C: Aggregator  → 1inch/Paraswap route
         ↓
Best solver wins batch auction → executes on-chain
User gets guaranteed price or better (surplus → user)
```

**MEV Protection**: Orders are signed intents, not on-chain txs → front-running impossible.
**Surplus**: Any price improvement beyond quoted amount goes back to the user.

---

## Supported Networks

Ethereum · BNB Chain · Gnosis Chain · Polygon · Base · Arbitrum One · Avalanche · Linea · Ink · Sepolia (testnet)

---

## Package Architecture (14 packages)

| Package | Purpose |
|---------|---------|
| `@cowprotocol/cow-sdk` | Main entry point (re-exports all) |
| `@cowprotocol/sdk-trading` | High-level: quote → sign → post |
| `@cowprotocol/sdk-order-book` | OrderBook API client (get/post orders) |
| `@cowprotocol/sdk-order-signing` | Cryptographic signing utilities |
| `@cowprotocol/sdk-composable` | Programmatic orders: TWAP, conditional |
| `@cowprotocol/sdk-bridging` | Cross-chain token transfers |
| `@cowprotocol/sdk-cow-shed` | Account abstraction support |
| `@cowprotocol/sdk-viem-adapter` | Viem provider adapter |
| `@cowprotocol/sdk-ethers-v6-adapter` | Ethers v6 adapter |
| `@cowprotocol/sdk-ethers-v5-adapter` | Ethers v5 adapter |
| `@cowprotocol/sdk-app-data` | Order metadata / app data |
| `@cowprotocol/sdk-config` | Chain/environment config |
| `@cowprotocol/sdk-contracts-ts` | Type-safe contract ABIs |
| `@cowprotocol/sdk-subgraph` | GraphQL subgraph queries |

---

## Installation

```bash
npm install @cowprotocol/cow-sdk
# or
pnpm add @cowprotocol/cow-sdk
```

---

## Core Usage: Quote → Sign → Post

```typescript
import { TradingSdk, SupportedChainId, OrderKind } from "@cowprotocol/cow-sdk"
import { createWalletClient, http } from "viem"
import { privateKeyToAccount } from "viem/accounts"
import { mainnet } from "viem/chains"

// Setup
const account = privateKeyToAccount("0x...")
const walletClient = createWalletClient({ account, chain: mainnet, transport: http() })

const sdk = new TradingSdk({
  chainId: SupportedChainId.MAINNET,
  signer: walletClient,
})

// 1. Get quote
const quote = await sdk.getQuote({
  kind: OrderKind.SELL,
  sellToken: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", // WETH
  buyToken:  "0x6B175474E89094C44Da98b954EedeAC495271d0F", // DAI
  amount: "1000000000000000000", // 1 WETH (18 decimals)
})

console.log(`Quote: sell 1 WETH → get ${quote.buyAmount} DAI`)

// 2. Post order (sign + submit in one step)
const orderId = await sdk.postSwapOrder({
  ...quote,
  slippageBps: 50, // 0.5% slippage tolerance
})

console.log(`Order posted: ${orderId}`)
// Track at: https://explorer.cow.fi/orders/${orderId}
```

---

## Order Types

### Market Order (Swap)
```typescript
// Execute immediately at best available price
const orderId = await sdk.postSwapOrder({
  kind: OrderKind.SELL,
  sellToken: WETH,
  buyToken: DAI,
  amount: parseEther("1"),
  slippageBps: 50,
})
```

### Limit Order
```typescript
// Execute only when price reaches target
const orderId = await sdk.postLimitOrder({
  kind: OrderKind.SELL,
  sellToken: WETH,
  buyToken: DAI,
  sellAmount: parseEther("1"),
  buyAmount: parseUnits("3200", 18), // Only fill if 1 WETH ≥ 3200 DAI
  validTo: Math.floor(Date.now() / 1000) + 86400, // expires in 24h
})
```

### TWAP (Time-Weighted Average Price)
```typescript
import { buildTWAPOrder } from "@cowprotocol/sdk-composable"

// Split 10 WETH into 10 parts over 24 hours
const twapOrder = buildTWAPOrder({
  sellToken: WETH,
  buyToken: DAI,
  totalSellAmount: parseEther("10"),
  numberOfParts: 10,
  timeBetweenParts: 2 * 60 * 60, // every 2 hours
  span: 0,                         // execute anytime within each window
})

const orderId = await sdk.postComposableOrder(twapOrder)
```

---

## OrderBook API (Direct)

```typescript
import { OrderBookApi, SupportedChainId } from "@cowprotocol/cow-sdk"

const orderBook = new OrderBookApi({ chainId: SupportedChainId.MAINNET })

// Get all open orders for a wallet
const orders = await orderBook.getOrders({ owner: "0x..." })

// Get order status
const order = await orderBook.getOrder(orderId)
console.log(order.status) // "open" | "fulfilled" | "cancelled" | "expired"

// Cancel an order
await orderBook.cancelOrder(orderId, signature)
```

---

## Cross-Chain Bridging

```typescript
import { BridgingSdk } from "@cowprotocol/sdk-bridging"

const bridge = new BridgingSdk({ chainId: SupportedChainId.MAINNET })

// Bridge USDC from Ethereum → Arbitrum
const bridgeOrder = await bridge.postBridgeOrder({
  sellToken: USDC_MAINNET,
  buyToken: USDC_ARBITRUM,
  amount: parseUnits("1000", 6),
  targetChainId: SupportedChainId.ARBITRUM_ONE,
})
```

---

## Key Advantages Over Standard DEX Aggregators

| Feature | CoW Protocol | 1inch / Paraswap |
|---------|-------------|-----------------|
| MEV Protection | ✓ (signed intents) | ✗ (on-chain txs) |
| Surplus to user | ✓ (price improvement) | ✗ (keeper keeps it) |
| Peer-to-peer matching | ✓ (CoW mechanism) | ✗ |
| TWAP orders | ✓ (composable) | Limited |
| Limit orders | ✓ | ✓ |
| Gas costs | Lower (batched) | Standard |


---
