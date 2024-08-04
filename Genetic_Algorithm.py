from Course_Input import *
from Professor_Input import *
from Course_Assignment import *
from Fitness import *
from Graph_Creator import *

POPULATION_SIZE = 100
GENERATIONS = 200
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
MIN_FITNESS_SCORE = 1

def generate_individual():
    individual = Course_Assignment()
    return individual

def generate_population(size):
    return [generate_individual() for _ in range(size)]

def fitness(individual):
    score = FitnessScore(individual)
    return max(score, MIN_FITNESS_SCORE)

def selection(population):
    fitness_scores = [fitness(ind) for ind in population]
    selected = random.choices(population, weights=fitness_scores, k=len(population))
    return selected

def crossover(parent1, parent2):
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)
    for i in range(len(parent1)):
        if random.random() > 0.5:
            child1[i] = copy.deepcopy(parent2[i])
            child2[i] = copy.deepcopy(parent1[i])
    return child1, child2

def mutate(individual):
    if random.random() < MUTATION_RATE:
        return Course_Assignment()

def genetic_algorithm():
    population = generate_population(POPULATION_SIZE)
    for generation in range(GENERATIONS):
        population = selection(population)
        new_population = []
        for i in range(0, len(population), 2):
            parent1, parent2 = population[i], population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    best_individual = max(population, key=fitness)
    return best_individual

Best_Assignment = genetic_algorithm()
print("Fitness score of the best assignment is ",FitnessScore(Best_Assignment))
Graph_Creator(Best_Assignment,professorList)
f = open("output.txt", 'w',encoding="utf-8")
for course in Best_Assignment:
    f.write("Course " + repr(course.getName()) + " is assigned to ")
    for prof in course.profsTakingCourse:    
        f.write(repr(prof.getName()))
    f.writelines("\n")
f.close()