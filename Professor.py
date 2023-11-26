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