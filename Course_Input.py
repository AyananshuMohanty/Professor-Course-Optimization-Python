import pandas as pd
import numpy as np
from Course import Course

d={}
courselist = []
def Take_Course_Input():
    d1 = {}  #empty dictionary to map course codes to courses, key being course code and the course obect mapped to it
    courselist1 = [] #list of all courses
    df = pd.read_csv("Course_List.csv")
    df["Name"] = df["Name"].astype(str)
    df["CourseNo"] = df["CourseNo"].astype(str)
    df["CourseType"] = df["CourseType"].astype(np.int64)
    numberOfCourses=df["Name"].count()
    for i in range(0,numberOfCourses):
        course = Course(df.iloc[i]["Name"], df.iloc[i]["CourseNo"], df.iloc[i]["CourseType"])
        courselist1.append(course)
        d1[course.getCourseCode()] = course
    return d1,courselist1

d,courselist=Take_Course_Input()  