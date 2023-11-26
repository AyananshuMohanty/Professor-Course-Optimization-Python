import pandas as pd
from Course_Type import *
class Course:
    def __init__(self, course_name, course_code, course_type):
        self.course_name = course_name
        self.course_code = course_code
        self.course_type = course_type

    def getName(self):
        return self.course_name

    def getCourseCode(self):
        return self.course_code

    def getCourseType(self):
        return Course_Type(self.course_type).name
    
