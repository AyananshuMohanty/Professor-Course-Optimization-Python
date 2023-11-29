import pandas as pd
import numpy as np
from Professor import Professor
df = pd.read_csv("File_Input.csv")
# print(df)
df['Name'] = df['Name'].astype(str)
df['ID'] = df['ID'].astype(str)
df['x'] = df['x'].astype(np.float64)
# print(df.iloc[1:2,1])
# print(df.iloc[1:2,1].dtype)
numberOfProfessors=df['Name'].count()
# print(numberOfProfessors)
professorList = []
for i in range(0,numberOfProfessors):
    professor = Professor(df.iloc[i]["Name"], df.iloc[i]["ID"])
    professorList.append(professor)
    print(professor.getName())
    professor.setPriority(df.iloc[i, 2:19])
    x = df.iloc[i]['x']
    professor.setCoursesRemaining(x)
    
professorListInitial = professorList