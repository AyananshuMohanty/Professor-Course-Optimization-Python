import pandas as pd
import numpy as np
from Course import Course
df = pd.read_csv("Course_List.csv")
df["Name"] = df["Name"].astype(str)
df["CourseNo"] = df["CourseNo"].astype(str)
df["CourseType"] = df["CourseType"].astype(np.int64)
d = {}  #empty dictionary to map course codes to courses, key being course code and the course obect mapped to it
numberOfCourses=df["Name"].count()
courselist = [] #list of all courses
for i in range(0,numberOfCourses):
    course = Course(df.iloc[i]["Name"], df.iloc[i]["CourseNo"], df.iloc[i]["CourseType"])
    courselist.append(course)
    d[course.getCourseCode()] = course

courseListInitial = courselist
# for course in courselist:
#     print(type(course.getCourseType()))
# print(d["MUP"])
# for key in d.keys():
#     print(d[key])