import pandas as pd
from Course_Input import *
class Professor:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.Priority_Order_FDCDC={}    #Dictionary(Priority,Course)
        self.Priority_Order_HDCDC={}    #Dictionary(Priority,Course)
        self.Priority_Order_FDELC={}    #Dictionary(Priority,Course)
        self.Priority_Order_HDELC={}    #Dictionary(Priority,Course)

    def getName(self):
        return self.name

    def getID(self):
        return self.ID
    
    def getFDCDCPriority(self, x):
        return self.Priority_Order_FDCDC[x]
    
    def getHDCDCPriority(self, x):
        return self.Priority_Order_HDCDC[x]
    
    def getFDELCPriority(self, x):
        return self.Priority_Order_FDELC[x]
    
    def getHDELCPriority(self, x):
        return self.Priority_Order_HDELC[x]

    def setPriority(self, priorityList):
        courseCodes = priorityList
        courseCodes = courseCodes.astype(str)
        count=0
        for i in courseCodes:
            if count<5:
                if i!="nan":    #if case for when professor has not filled an input
                    print(i)
                    self.Priority_Order_FDCDC[count+1]=d[i]
            elif count<10:
                if i!="nan":    #if case for when professor has not filled an input
                    print(i)
                    self.Priority_Order_HDCDC[count-4]=d[i]
            elif count<13:
                if i!="nan":    #if case for when professor has not filled an input
                    print(i)
                    self.Priority_Order_FDELC[count-9]=d[i]
            elif count<16:
                if i!="nan":    #if case for when professor has not filled an input
                    print(i)
                    self.Priority_Order_HDELC[count-12]=d[i]
            count+=1
            