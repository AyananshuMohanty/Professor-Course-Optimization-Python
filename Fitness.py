from Course_Input import *

def FitnessScore(courseList):
    score=0
    for course in courseList:
        for professor in course.profsTakingCourse:
            for key,value in professor.Priority_Order_FDCDC.items():
                if value==course:
                    sum+=key
            for key,value in professor.Priority_Order_HDCDC.items():
                if value==course:
                    sum+=key
            for key,value in professor.Priority_Order_FDELC.items():
                if value==course:
                    sum+=key
            for key,value in professor.Priority_Order_HDELC.items():
                if value==course:
                    sum+=key
    return score
        