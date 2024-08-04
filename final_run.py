import subprocess
import importlib
import sys
from Course_Input import *
from Professor_Input import *
from Course_Assignment import *
from Fitness import *
from Graph_Creator import *

# Initialize the best fitness score and final assignment
best_fitness_score = 0
best_courselist = []

# Function to reload the module and access variables
def reload_module(module_name):
    if module_name in sys.modules:
        del sys.modules[module_name]
    return importlib.import_module(module_name)

for i in range(10):
    # Run the script
    subprocess.run(['python', 'Final_Assignment.py'])
    
    # Import the script and reload the module
    assignment_module = reload_module('Final_Assignment')
    
    # Access the fitness score and courselist variables
    fitness_score = assignment_module.best_fitness_score
    courselist = assignment_module.best_courselist
    
    # Check if the current run is better than the previous best
    if fitness_score > best_fitness_score:
        best_fitness_score = fitness_score
        print(f"New best score: {best_fitness_score}")
        best_courselist = courselist

# Print the best fitness score and corresponding courselist
f = open("output.txt", 'w',encoding="utf-8")
for course in best_courselist:
    f.write("Course " + repr(course.getName()) + " is assigned to ")
    for prof in course.profsTakingCourse:    
        f.write(repr(prof.getName()))
    f.writelines("\n")
f.close()
Graph_Creator(courselist,professorList)