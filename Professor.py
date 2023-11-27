import pandas as pd
from Course_Input import *
class Professor:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.Priority_Order = {}

    def getName(self):
        return self.name

    def getID(self):
        return self.ID
    
    def getPriority(self, x):
        return self.Priority_Order[x]

    def addPriority(self, Priority, Course):
        self.Priority_Order[Priority] = Course

    def setPriority(self, priorityList):
        Priority  = 0
        self.Priorty_Order = []
        coursenames = priorityList
        coursenames = coursenames.astype(str)
        # print(coursenames.iloc[0:1])
        for i in coursenames:
            if i!="None":
                self.Priority_Order[Priority] = d[i]
                Priority = Priority + 1
            