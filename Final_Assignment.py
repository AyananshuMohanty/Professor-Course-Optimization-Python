from Course_Input import *
from Professor_Input import *
from Course_Assignment import *
from Fitness import *
from Graph_Creator import *

Final_Assignment=[]
Final_Assignment_Score=99999

for i in range(2):
    Course_Assignment()
    if FitnessScore(courselist)<Final_Assignment_Score:
        Final_Assignment=courselist

for course in Final_Assignment:
    print("Course " + course.getName() + " is assigned to ", end = " ")
    print(course.profsTakingCourse)

Graph_Creator(courselist,professorList)