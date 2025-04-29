# Genetic Algorithm for 0-1 Knapsack Problem

This project implements a **Genetic Algorithm (GA)** to solve the classic **0-1 Knapsack Problem**, as part of the "Artificial Intelligence" lab assignment at BSDM. It demonstrates two selection techniques—**Elitism** and **Roulette Wheel Selection**—and uses standard GA components such as crossover and mutation, all without relying on NumPy.

---

## 🧠 Problem Description

The **0-1 Knapsack Problem** is a combinatorial optimization problem where you're given a set of items, each with a weight and a value. The objective is to determine the most valuable subset of items to include in a knapsack without exceeding the weight limit.

**Goal**: Maximize the total value without exceeding the knapsack's weight capacity.

---

## 🔬 Genetic Algorithm Components

### ✅ Chromosome Representation
Each chromosome is represented as a binary list (`0` or `1`), indicating whether an item is included (`1`) or not (`0`) in the knapsack.

### 📈 Fitness Function
Calculates the total value of selected items if the weight limit is not exceeded. Overweight solutions are penalized with a fitness of `0`.

### 🎯 Selection Methods
- **Elitism**: Selects the top-performing individuals directly.
- **Roulette Wheel**: Selects individuals probabilistically based on relative fitness.

### 🔀 Crossover
Single-point crossover is used to generate two offspring from two parents.

### 🧬 Mutation
Each gene has a small probability (defined by `mutation_rate`) to flip, introducing genetic diversity.

---

## 📁 File Structure

```
genetic-algorithm-knapsack/
├── genetic.py       # Main implementation of the genetic algorithm
├── test.txt         # Input file containing knapsack items
└── README.md        # Project documentation
```

---

## 📥 Input Format (`test.txt`)

The first line contains:
```
<number_of_items> <weight_limit>
```

Each subsequent line represents an item:
```
<value> <weight>
```

**Example:**
```
5 10
60 2
100 3
120 4
80 5
30 1
```

---

## 🚀 How to Run

1. Make sure you are using **Python 3.6+**
2. Ensure the `test.txt` file is in the same directory as `genetic.py`
3. Run the program:
```bash
python genetic.py
```

---

## ⚙️ Configuration

Inside the `__main__` section of `genetic.py`, you can configure:

- `population_size` — Number of chromosomes per generation
- `mutation_rate` — Likelihood of mutation per gene
- `generation` — Number of generations for evolution

```python
ga = GeneticAlgorithm(weight_limit, knapsack, population_size=20, mutation_rate=0.2)

for generation in range(50):
    ga.evolve()
```

---

## 🧪 Sample Output

```
Best solution found:
Items: ['item2', 'item3', 'item5'], Total Value: 250
Fitness of best solution: 250
```

---

## 📚 Concepts Practiced

- Genetic Algorithms
- Heuristic Search
- Fitness-Based Optimization
- Selection, Crossover, and Mutation
- Penalty Handling in Constraints

---

## ❌ No External Libraries

This implementation **does not use NumPy** or any third-party libraries—only Python's standard library.

---

## 🧑‍💻 Author

**Muqnit Ur Rehman**  
**Department Of Data Science(PUCIT)**
---


