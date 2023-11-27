import pandas as pd
import numpy as np
from Course import Course
df = pd.read_csv("CourseList.csv")
df["Name"] = df["Name"].astype(str)
df["CourseNo"] = df["CourseNo"].astype(str)
df["CourseType"] = df["CourseType"].astype(np.int64)
d = {}  #empty dictionary to map course codes to courses
numberOfCourses=df["Name"].count()
courselist = []
for i in range(0,numberOfCourses):
    course = Course(df.iloc[i]["Name"], df.iloc[i]["CourseNo"], df.iloc[i]["CourseType"])
    courselist.append(course)
    d[course.getCourseCode()] = course

# print(courselist)
# print(d["MUP"])
print(d.keys())