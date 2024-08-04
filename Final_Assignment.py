from Course_Input import *
from Professor_Input import *
from Course_Assignment import *
from Fitness import *
from Graph_Creator import *

Final_Assignment=[]
Final_Assignment_Score=0

for i in range(1):
    Current_Assignment=Course_Assignment()
    Current_Fitness_Score=FitnessScore(Current_Assignment)
    print(Current_Fitness_Score)
    if Current_Fitness_Score>Final_Assignment_Score:
        Final_Assignment_Score=Current_Fitness_Score
        Final_Assignment=Current_Assignment
f = open("output.txt", 'w',encoding="utf-8")
for course in Final_Assignment:
    f.write("Course " + repr(course.getName()) + " is assigned to ")
    for prof in course.profsTakingCourse:    
        f.write(repr(prof.getName()))
    f.writelines("\n")
f.close()
best_fitness_score = Final_Assignment_Score
best_courselist = Final_Assignment
Graph_Creator(Final_Assignment,professorList)