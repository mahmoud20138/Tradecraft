---
name: strategy-genetic-optimizer
description: >
  Evolutionary algorithm engine that breeds, mutates, and evolves trading strategies automatically.
  Use this skill whenever the user asks to "optimize strategy", "evolve parameters", "genetic
  algorithm", "breed strategies", "parameter optimization", "auto-optimize", "find best parameters",
  "evolutionary search", "mutation", "crossover", "fitness function", "population-based optimization",
  or any request to automatically discover optimal strategy configurations. Works with
  quant-trading-pipeline for backtesting and walk-forward-optimizer for validation.
kind: engine
category: trading/quant
status: active
tags: [backtesting, genetic, optimizer, quant, strategy, trading]
related_skills: [backtesting-sim, backtest-report-generator, hurst-exponent-dynamics-crisis-prediction, ml-trading, quant-ml-trading]
---

# Strategy Genetic Optimizer

## Overview
Uses evolutionary algorithms (GA) to search the parameter space of trading strategies.
Breeds top performers, mutates for exploration, and applies selection pressure via
risk-adjusted fitness functions. Prevents overfitting through walk-forward validation
and population diversity enforcement.

---

## 1. Gene Encoding & Strategy Genome

```python
import numpy as np
import pandas as pd
from dataclasses import dataclass, field
from typing import Callable, Optional
import random, copy

@dataclass
class Gene:
    """Single parameter with its valid range."""
    name: str
    min_val: float
    max_val: float
    step: float = 1.0
    gene_type: str = "float"  # float, int, bool, choice
    choices: list = field(default_factory=list)

    def random_value(self):
        if self.gene_type == "bool": return random.choice([True, False])
        if self.gene_type == "choice": return random.choice(self.choices)
        if self.gene_type == "int": return random.randint(int(self.min_val), int(self.max_val))
        val = random.uniform(self.min_val, self.max_val)
        return round(val / self.step) * self.step

    def mutate(self, value, mutation_strength: float = 0.2):
        if self.gene_type == "bool": return not value
        if self.gene_type == "choice": return random.choice(self.choices)
        range_size = self.max_val - self.min_val
        delta = random.gauss(0, range_size * mutation_strength)
        new_val = np.clip(value + delta, self.min_val, self.max_val)
        if self.gene_type == "int": return int(round(new_val))
        return round(new_val / self.step) * self.step

@dataclass
class Genome:
    """Complete strategy parameter set."""
    genes: dict  # {gene_name: value}
    fitness: float = 0.0
    generation: int = 0
    id: str = ""

# Example: MA crossover strategy genome definition
MA_CROSSOVER_GENES = [
    Gene("fast_period", 5, 50, 1, "int"),
    Gene("slow_period", 20, 200, 1, "int"),
    Gene("rsi_filter", 0, 100, 1, "int"),
    Gene("atr_stop_mult", 1.0, 5.0, 0.1, "float"),
    Gene("atr_tp_mult", 1.0, 8.0, 0.1, "float"),
    Gene("use_volume_filter", 0, 1, 1, "bool"),
    Gene("entry_type", 0, 0, 0, "choice", choices=["market", "limit_pullback", "stop_entry"])]
```

---

## 2. Fitness Functions (Risk-Adjusted)

```python
def fitness_sharpe_dd(returns: pd.Series, max_dd_threshold: float = -0.20) -> float:
    """Sharpe ratio penalized by drawdown. Primary fitness function."""
    if len(returns) < 30 or returns.std() == 0: return -999
    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
    equity = (1 + returns).cumprod()
    dd = (equity / equity.cummax() - 1).min()
    if dd < max_dd_threshold: return sharpe + (dd - max_dd_threshold) * 10  # Heavy penalty
    return sharpe

def fitness_expectancy(trades: pd.DataFrame) -> float:
    """Expectancy * frequency. Rewards consistent edges."""
    if trades.empty: return -999
    wins = trades[trades["pnl"] > 0]
    losses = trades[trades["pnl"] <= 0]
    wr = len(wins) / len(trades)
    avg_w = wins["pnl"].mean() if len(wins) > 0 else 0
    avg_l = abs(losses["pnl"].mean()) if len(losses) > 0 else 1
    expectancy = wr * avg_w - (1 - wr) * avg_l
    frequency = len(trades) / 252  # trades per year
    return expectancy * np.sqrt(frequency)

def fitness_sortino_calmar(returns: pd.Series) -> float:
    """Combined Sortino + Calmar for downside-focused optimization."""
    if len(returns) < 30: return -999
    downside = returns[returns < 0].std() * np.sqrt(252)
    sortino = returns.mean() * 252 / max(downside, 1e-10)
    equity = (1 + returns).cumprod()
    max_dd = abs((equity / equity.cummax() - 1).min())
    calmar = returns.mean() * 252 / max(max_dd, 1e-10)
    return (sortino + calmar) / 2
```

---

## 3. Genetic Algorithm Engine

```python
class GeneticOptimizer:
    """Core evolutionary optimization engine."""

    def __init__(self, gene_defs: list[Gene], fitness_fn: Callable,
                 population_size: int = 50, elite_pct: float = 0.1,
                 mutation_rate: float = 0.15, crossover_rate: float = 0.7):
        self.gene_defs = {g.name: g for g in gene_defs}
        self.fitness_fn = fitness_fn
        self.pop_size = population_size
        self.elite_pct = elite_pct
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = []
        self.history = []

    def initialize_population(self) -> list[Genome]:
        self.population = []
        for i in range(self.pop_size):
            genes = {name: gene.random_value() for name, gene in self.gene_defs.items()}
            self.population.append(Genome(genes=genes, id=f"gen0_{i}"))
        return self.population

    def evaluate(self, strategy_runner: Callable, data: pd.DataFrame):
        """Evaluate all genomes. strategy_runner(data, params) -> returns Series."""
        for genome in self.population:
            try:
                returns = strategy_runner(data, genome.genes)
                genome.fitness = self.fitness_fn(returns)
            except Exception:
                genome.fitness = -999
        self.population.sort(key=lambda g: g.fitness, reverse=True)

    def select_parents(self) -> tuple[Genome, Genome]:
        """Tournament selection."""
        def tournament(k=3):
            contestants = random.sample(self.population, min(k, len(self.population)))
            return max(contestants, key=lambda g: g.fitness)
        return tournament(), tournament()

    def crossover(self, parent_a: Genome, parent_b: Genome) -> Genome:
        """Uniform crossover — each gene randomly from either parent."""
        child_genes = {}
        for name in self.gene_defs:
            child_genes[name] = parent_a.genes[name] if random.random() < 0.5 else parent_b.genes[name]
        return Genome(genes=child_genes)

    def mutate(self, genome: Genome, strength: float = 0.2) -> Genome:
        mutated = copy.deepcopy(genome)
        for name, gene_def in self.gene_defs.items():
            if random.random() < self.mutation_rate:
                mutated.genes[name] = gene_def.mutate(mutated.genes[name], strength)
        return mutated

    def evolve_generation(self, strategy_runner: Callable, data: pd.DataFrame, gen_num: int) -> dict:
        """One full generation: evaluate → select → breed → mutate."""
        self.evaluate(strategy_runner, data)
        n_elite = max(int(self.pop_size * self.elite_pct), 1)
        elites = [copy.deepcopy(g) for g in self.population[:n_elite]]

        new_pop = list(elites)
        while len(new_pop) < self.pop_size:
            p1, p2 = self.select_parents()
            child = self.crossover(p1, p2) if random.random() < self.crossover_rate else copy.deepcopy(p1)
            child = self.mutate(child)
            child.generation = gen_num
            child.id = f"gen{gen_num}_{len(new_pop)}"
            new_pop.append(child)

        self.population = new_pop
        best = self.population[0]
        gen_stats = {
            "generation": gen_num, "best_fitness": round(best.fitness, 4),
            "best_params": best.genes, "avg_fitness": round(np.mean([g.fitness for g in self.population]), 4),
            "diversity": self._population_diversity(),
        }
        self.history.append(gen_stats)
        return gen_stats

    def run(self, strategy_runner: Callable, data: pd.DataFrame, n_generations: int = 30) -> dict:
        """Full optimization run."""
        self.initialize_population()
        for gen in range(n_generations):
            stats = self.evolve_generation(strategy_runner, data, gen)
            print(f"Gen {gen}: best={stats['best_fitness']:.4f} avg={stats['avg_fitness']:.4f} div={stats['diversity']:.3f}")
            if stats["diversity"] < 0.05:
                print("WARNING: Population converged — injecting random individuals")
                for i in range(self.pop_size // 4):
                    genes = {name: gene.random_value() for name, gene in self.gene_defs.items()}
                    self.population[-(i+1)] = Genome(genes=genes, generation=gen, id=f"random_{gen}_{i}")

        self.evaluate(strategy_runner, data)
        return {
            "best_genome": self.population[0],
            "top_5": [(g.genes, round(g.fitness, 4)) for g in self.population[:5]],
            "history": self.history,
            "WARNING": "Validate with walk-forward OOS before live deployment. GA results overfit easily.",
        }

    def _population_diversity(self) -> float:
        """Measure population diversity (0=identical, 1=maximum spread)."""
        if len(self.population) < 2: return 0
        diversities = []
        for name, gene_def in self.gene_defs.items():
            vals = [g.genes[name] for g in self.population if isinstance(g.genes[name], (int, float))]
            if vals and (gene_def.max_val - gene_def.min_val) > 0:
                diversities.append(np.std(vals) / (gene_def.max_val - gene_def.min_val))
        return np.mean(diversities) if diversities else 0
```

---

## Anti-Overfitting Safeguards
1. **Always split data**: optimize on 60%, validate on 40% OOS
2. **Diversity enforcement**: inject randoms when population converges
3. **Penalize complexity**: fewer parameters = better (Occam's razor)
4. **Walk-forward validation**: use walk-forward-optimizer skill on best genomes
5. **Multiple fitness functions**: rank by Sharpe AND Sortino AND Calmar — not just one
