from Course_Input import *
from Professor_Input import *
from Course_Assignment import *
from Fitness import *
from Graph_Creator import *

Final_Assignment=[]
Final_Assignment_Score=99999

for i in range(1000):
    Course_Assignment()
    if FitnessScore(courselist)<Final_Assignment_Score:
        Final_Assignment=courselist

f = open("output.txt", 'w',encoding="utf-8")

for course in Final_Assignment:
    f.write("Course " + repr(course.getName()) + " is assigned to ")
    for prof in course.profsTakingCourse:    
        f.write(repr(prof.getName()))
    f.writelines("\n")
f.close()

Graph_Creator(courselist,professorList)