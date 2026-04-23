---
name: gold-orb-ea
description: GOLD_ORB — MQL5 Expert Advisor for XAUUSD 1H Opening Range Breakout. Identifies opening range (first 1H candle after 1:02 AM server time), confirms consolidation (min 3 candles), then trades breakouts. Buy signal on resistance break, sell on support 
kind: meta
category: trading/mt5
status: active
tags: [breakout, gold, mt5, orb, trading]
related_skills: [mt5-integration, mt5-chart-browser]
---

# gold-orb-ea

USE FOR:
  - "gold ORB EA / bot"
  - "XAUUSD opening range breakout MQL5"
  - "MT5 expert advisor for gold"
  - "ORB strategy for XAUUSD 1H"
  - "MQL5 EA with dynamic position sizing"
  - "build opening range breakout bot"
tags: [MQL5, MT5, EA, gold, XAUUSD, ORB, opening-range-breakout, price-action, 1H, hedging]
kind: tool
category: mt5-integration

---

## What Is GOLD_ORB?

MQL5 Expert Advisor for XAUUSD 1H Opening Range Breakout.
- Repo: https://github.com/yulz008/GOLD_ORB
- Platform: MetaTrader 5
- Symbol: XAUUSD (Gold)
- Timeframe: H1
- Broker requirement: **Hedging mode** (ICMarkets MT5 recommended)
- Purpose: Working EA + educational codebase for beginners

---

## Strategy Logic

### Phase 1 — Range Formation
```
Market open: 1:02 AM server time
First 1H candle → defines initial support (low) and resistance (high)
```

### Phase 2 — Range Confirmation
```
Wait for N consecutive candles to close WITHIN the range
Default N = 3 (user-adjustable)
Range becomes "final" only after consolidation confirmed
```

### Phase 3 — Signal Generation
```
Signal 11  → Price BREAKS ABOVE resistance  → BUY
Signal 10  → Price BREAKS BELOW support     → SELL
Signal 0   → No breakout                    → No trade
```

---

## Entry / Exit Parameters

| Parameter | Default |
|-----------|---------|
| Take Profit | 1,200 points |
| Stop Loss | 400 points |
| R:R Ratio | 3:1 |
| Max trades/day | 2 (1 long + 1 short independently) |
| Risk per trade | 1% of account balance |
| Max equity drawdown | 10% |

---

## MQL5 Class Architecture

```mql5
// Candle detection
class new_candle_check2 {
    bool IsNewCandle();  // Returns true on new H1 candle open
}

// Core strategy
class Open_Range_Breakout {
    int GetSignal();    // Returns: 11=BUY, 10=SELL, 0=NONE
    // Internally tracks: range high, range low, candle count
}

// Execution (built-in MQL5 classes)
CTrade  trade;          // Order send / modify / close
CTrailing trailing;     // Dynamic stop-loss trailing
```

---

## Full EA Structure (Educational Template)

```mql5
// OnInit — setup
int OnInit() {
    // Validate symbol, timeframe
    // Initialize ORB object
    // Set risk parameters
    return INIT_SUCCEEDED;
}

// OnTick — main logic
void OnTick() {
    if (!new_candle.IsNewCandle()) return;   // Only act on new H1 candle
    
    int signal = orb.GetSignal();
    
    if (signal == 11 && long_enabled && daily_buys < 1) {
        double lot = CalcLotSize(risk_pct, sl_points);
        trade.Buy(lot, _Symbol, 0, sl_price, tp_price, "GOLD_ORB_BUY");
        daily_buys++;
    }
    
    if (signal == 10 && short_enabled && daily_sells < 1) {
        double lot = CalcLotSize(risk_pct, sl_points);
        trade.Sell(lot, _Symbol, 0, sl_price, tp_price, "GOLD_ORB_SELL");
        daily_sells++;
    }
    
    // Check drawdown limit
    if (GetEquityDrawdown() > max_drawdown_pct) CloseAllPositions();
}
```

---

## Dynamic Position Sizing

```mql5
double CalcLotSize(double risk_pct, int sl_points) {
    double account_balance = AccountInfoDouble(ACCOUNT_BALANCE);
    double risk_amount = account_balance * risk_pct / 100.0;
    double tick_value = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_VALUE);
    double lot = risk_amount / (sl_points * tick_value);
    return NormalizeDouble(lot, 2);
}
```

---

## Risk Management Features

| Feature | Detail |
|---------|--------|
| Dynamic sizing | % of account balance per trade |
| Max drawdown | Hard stop at 10% equity loss |
| Daily trade limit | 1 long + 1 short max |
| Losing streak detection | Reduces size after N consecutive losses |
| Virtual simulation | Test without real orders |
| Independent long/short | Can disable either direction |

---

## Installation

```
1. Clone repo → copy folder to:
   C:\Users\[user]\AppData\Roaming\MetaQuotes\Terminal\[ID]\MQL5\Experts\GOLD_ORB\

2. Open MetaEditor → recompile .mq5 files

3. Open XAUUSD H1 chart in MT5

4. Drag EA from Navigator → attach to chart

5. Configure inputs:
   - Enable/disable long/short
   - Adjust risk_pct, max_drawdown_pct
   - Set candle consolidation threshold (default 3)
   - Enable trailing stop if desired
```

---

## ORB Strategy Notes for Gold (XAUUSD)

```
Gold ORB works well because:
- London open (2-3 AM NY time) creates sharp directional moves
- Asia session establishes clear range (low volatility consolidation)
- Breakout of Asia range at London/NY open = high-probability continuation

Optimal configuration for gold:
- Range period:  Asian session (22:00–02:00 server)
- Breakout time: London open (02:00–04:00 server)
- Filter:        Only trade if range width > 5 ATR (avoid false breakouts)
- Exit:          Trail stop after 1R achieved
```

---

## Adapting to Other Symbols

The framework is designed to be adapted:
```mql5
// Change symbol
input string TradingSymbol = "EURUSD";  // or "GBPJPY", "US30", etc.

// Adjust open time per symbol's market open
input string MarketOpenTime = "08:00";  // London for forex

// Adjust TP/SL to match symbol volatility (in points)
input int TakeProfit = 300;   // Tighter for forex vs gold
input int StopLoss   = 150;
```


---
