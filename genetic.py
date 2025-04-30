import random

class Chromosome:    
    def __init__(self, genes=None, knapsack=None, weight_limit=0):
        self.knapsack = knapsack
        self.weight_limit = weight_limit
        self.genes = genes if genes is not None else [random.randint(0, 1) for _ in range(len(knapsack))]
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        total_weight = 0
        total_value = 0
        items = list(self.knapsack.values())  # Convert knapsack values to a list
        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                value, weight = items[i]  # Access the value and weight by index
                total_weight += weight
                total_value += value
        if total_weight > self.weight_limit:
            return 0  # Penalize overweight solutions
        return total_value
    
    def __str__(self):  
        items = list(self.knapsack.keys())
        selected_items = [items[i] for i in range(len(self.genes)) if self.genes[i] == 1]
        return f"Items: {selected_items}, Total Value: {self.fitness}"


class GeneticAlgorithm:
    def __init__(self, weight_limit, knapsack, population_size, mutation_rate):
        self.weight_limit = weight_limit
        self.knapsack = knapsack
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        return [
            Chromosome(knapsack=self.knapsack, weight_limit=self.weight_limit)
            for _ in range(self.population_size)
        ]

    def selection(self, method):
        sorted_pop = sorted(self.population, key=lambda c: c.fitness, reverse=True)

        if method == "elitism":
            return sorted_pop[:self.population_size]

        elif method == "roulette":
            fitness_sum = sum(c.fitness for c in sorted_pop)
            if fitness_sum == 0:
                return random.choices(self.population, k=self.population_size)
            probabilities = [c.fitness / fitness_sum for c in sorted_pop]
            return random.choices(sorted_pop, weights=probabilities, k=self.population_size)


    def crossover(self, parent1, parent2):
        point = random.randint(1, len(parent1.genes) - 1)
        child1_genes = parent1.genes[:point] + parent2.genes[point:]
        child2_genes = parent2.genes[:point] + parent1.genes[point:]
        return (
            Chromosome(child1_genes, self.knapsack, self.weight_limit),
            Chromosome(child2_genes, self.knapsack, self.weight_limit)
        )

    def mutation(self, chromosome):
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                chromosome.genes[i] = 1 - chromosome.genes[i]
        chromosome.fitness = chromosome.calculate_fitness()

    def evolve(self):
        selected = self.selection(method="elitism")
        new_population = []
        for i in range(0, self.population_size, 2):
            parent1 = selected[i]
            parent2 = selected[i + 1 if i + 1 < self.population_size else 0]
            child1, child2 = self.crossover(parent1, parent2)
            self.mutation(child1)
            self.mutation(child2)
            new_population.extend([child1, child2])
        self.population = new_population[:self.population_size]

    def get_solution(self):
        return max(self.population, key=lambda c: c.fitness)


def build_knapsack(file_path):
    knapsack = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n, weight_limit = map(int, lines[0].split())
        for idx, line in enumerate(lines[1:n+1]):
            value, weight = map(int, line.strip().split())
            knapsack[f"item{idx+1}"] = (value, weight)
    return weight_limit, knapsack


if __name__ == "__main__":
    # Load the input from file
    weight_limit, knapsack = build_knapsack("tests.txt")

    # Create and run the genetic algorithm
    ga = GeneticAlgorithm(weight_limit, knapsack, population_size=20, mutation_rate=0.2)
    
    for generation in range(50):
        ga.evolve()

    # Output best solution
    best_solution = ga.get_solution()
    print("Best solution found:")
    print(best_solution)
    print("Fitness of best solution:", best_solution.fitness)