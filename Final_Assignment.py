from Course_Input import *
from Professor_Input import *
from Course_Assignment import *
from Fitness import *

Final_Assignment=[]
Final_Assignment_Score=99999

for i in range(10000):
    Course_Assignment()
    if FitnessScore()>Final_Assignment_Score:
        Final_Assignment=courselist

for course in Final_Assignment:
    print("Course " + course.getName() + " is assigned to " + course.profsTakingCourse)