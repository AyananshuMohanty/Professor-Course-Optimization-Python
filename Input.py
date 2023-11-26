import pandas as pd
import numpy as np
from Course import Course
df = pd.read_csv("coursedata.csv")
df['Name'] = df['Name'].astype(str)
df['CourseNo'] = df['CourseNo'].astype(str)
df['CourseType'] = df['CourseType'].astype(np.int64)
print(df.iloc[0]["Name"])
print(df["Name"].dtype)
courselist = []
for i in range(0,2):
    course = Course(df.iloc[i]["Name"], df.iloc[i]["CourseNo"], df.iloc[i]["CourseType"])
    courselist.append(course)

print(courselist)
