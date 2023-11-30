import pandas as pd
import numpy as np
from Course_Input import *
from Professor import *

professorList = []
def Take_File_Input():
    professorList = []
    df = pd.read_csv("File_Input.csv")
    df['Name'] = df['Name'].astype(str)
    df['ID'] = df['ID'].astype(str)
    df['x'] = df['x'].astype(np.float64)
    
    numberOfProfessors=df['Name'].count()

    for i in range(0,numberOfProfessors):
        professor = Professor(df.iloc[i]["Name"], df.iloc[i]["ID"],df.iloc[i]['x'])
        professorList.append(professor)
        professor.setPriority(df.iloc[i, 2:19])
    return professorList
professorList=Take_File_Input()      