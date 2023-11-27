from Professor_Input import *
from Course_Input import *
class Solution:
    def assignFirstCDCPriority(self):
        for prof in professorList:            
            for course in prof.Priority_Order_FDCDC+prof.Priority_Order_HDCDC:
                if(course.noOfProfsTakingCourse<2):
                    break 
                
            prof.addCourseTaken(course) #need to subtract 1 or 0.5 from the prof too, need to add a field to prof
            course.addProfTakingCourse(prof)
            if(course.noOfProfsTakingCourse==1):
                prof.coursesRemaining -= 1
            elif(course.noOfProfsTakingCourse==2):
                prof.coursesRemaining -= 0.5
                course.profsTakingCourse[0].coursesRemaining += 0.5
                # def sortProfessors(self): will create this after updating input file, add x1,x2,x3 as fields
                
    def unassigned(self, list):
        for i in list:
            if(i.getCourseType()==1|i.getCourseType()==3):
                if(i.noOfProfsTakingCourse==0):
                    return True
        
        return False
                    
                            
    def assignCourses(self):
        self.assignFirstCDCPriority()
        while self.unassigned(courselist):
            print('zzz')
            
            
            
        