import pandas as pd
import numpy as np
from Professor import Professor
df = pd.read_csv("ProfessorList.csv")
print(df)
df['Name'] = df['Name'].astype(str)
df['ID'] = df['ID'].astype(str)
print(df.iloc[0]["Name"])
print(df["Name"].dtype)
numberOfProfessors=df['Name'].count()
professorList = []
for i in range(0,numberOfProfessors):
    professor = Professor(df.iloc[i]["Name"], df.iloc[i]["ID"])
    professorList.append(professor)

print(professorList)
