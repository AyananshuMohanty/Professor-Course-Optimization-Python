import random
import numpy as np
from Course_Type import *
from Course_Input import *
from Professor_Input import *


POPULATION_SIZE = 100
GENERATIONS = 200
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
MIN_FITNESS_SCORE = 1  # Ensure fitness score is at least 1

def generate_individual():
    individual = {}
    courses = list(d.values()) 
    for professor in professorList:
        individual[professor] = random.sample(courses, len(courses))
    return individual

def generate_population(size):
    return [generate_individual() for _ in range(size)]

def fitness(individual):
    score = 0
    for professor, courses in individual.items():
        for course in courses:
            if course in list(professor.Priority_Order_FDCDC.values()) or course in list(professor.Priority_Order_HDCDC.values()) or \
               course in list(professor.Priority_Order_FDELC.values()) or course in list(professor.Priority_Order_HDELC.values()):
                score += 1
            if professor.coursesRemaining < 1:
                score -= 100  # Penalize if professor exceeds their course capacity
    return max(score, MIN_FITNESS_SCORE)  

def selection(population):
    fitness_scores = [fitness(ind) for ind in population]
    print(f"Fitness scores: {fitness_scores}")  
    selected = random.choices(population, weights=fitness_scores, k=len(population))
    return selected

def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1.copy(), parent2.copy()
    
    crossover_point = random.randint(0, len(professorList) - 1)
    child1, child2 = {}, {}
    for i, professor in enumerate(professorList):
        if i <= crossover_point:
            child1[professor] = parent1[professor]
            child2[professor] = parent2[professor]
        else:
            child1[professor] = parent2[professor]
            child2[professor] = parent1[professor]
    return child1, child2


def mutate(individual):
    if random.random() < MUTATION_RATE:
        professor = random.choice(professorList)
        random.shuffle(individual[professor])
    return individual

def genetic_algorithm():
    population = generate_population(POPULATION_SIZE)
    for generation in range(GENERATIONS):
        population = selection(population)
        new_population = []
        for i in range(0, len(population), 2):
            parent1, parent2 = population[i], population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        population = new_population
        best_individual = max(population, key=fitness)
        print(f'Generation {generation + 1} Best Fitness: {fitness(best_individual)}')
    return best_individual


best_assignment = genetic_algorithm()

for professor, courses in best_assignment.items():
    print(f"Professor: {professor.name}")
    for course in courses:
        print(f"  Assigned Course: {course.name}")
