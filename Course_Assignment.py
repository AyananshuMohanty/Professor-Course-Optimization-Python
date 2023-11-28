import random
from Course_Type import *
from Course_Input import *
from Professor_Input import *

CDCList=[]
ELCList=[]
UnassignedProfessor=professorList
for course in [*d.values()]: #gets list of values in dictionary
    if ((course.getCourseType()==Course_Type(1).name) or (course.getCourseType()==Course_Type(3).name)):
        CDCList.append(course)
        
for course in [*d.values()]:
    if ((course.getCourseType()==Course_Type(2).name) or (course.getCourseType()==Course_Type(4).name)):
        ELCList.append(course)

for course in CDCList:
    UnassignedProfessorsWithCourseInPriorityList=[]
    for professor in UnassignedProfessor:
        if ((course in list((professor.Priority_Order_FDCDC).values())) or (course in list((professor.Priority_Order_HDCDC).values()))):
            UnassignedProfessorsWithCourseInPriorityList.append(professor)
    Assigned=False
    print(UnassignedProfessorsWithCourseInPriorityList)
    
    if len(UnassignedProfessorsWithCourseInPriorityList)!=0:
        while Assigned==False:   #loops until a professor is assigned to this course
            PickProfessor=random.choice(UnassignedProfessorsWithCourseInPriorityList) #chooses one of the professors who have this course in their priority list
            UnassignedProfessorsWithCourseInPriorityList.remove(PickProfessor)
            
            if len(UnassignedProfessorsWithCourseInPriorityList)!=0:
                if PickProfessor.coursesRemaining==0.5:
                    PotentialCandidates=[]
                    for professor2 in UnassignedProfessorsWithCourseInPriorityList:
                        if ((professor2.coursesRemaining==0.5) or (professor2.coursesRemaining==1.5)) :
                            PotentialCandidates.append(professor2)
                    if len(PotentialCandidates)!=0:
                        PickProfessor2=random.choice(PotentialCandidates)
                        PickProfessor.coursesRemaining-=0.5
                        PickProfessor2.coursesRemaining-=0.5
                        course.addProfTakingCourse(PickProfessor)
                        course.addProfTakingCourse(PickProfessor2)
                        UnassignedProfessor.remove(PickProfessor2)
                        Assigned=True
                    else:
                        Assigned=False
                
                elif PickProfessor.coursesRemaining==1:
                    PickProfessor.coursesRemaining-=1
                    course.addProfTakingCourse(PickProfessor)
                    Assigned=True
                
                elif PickProfessor.coursesRemaining==1.5:
                    PotentialCandidates=[]
                    for professor2 in UnassignedProfessorsWithCourseInPriorityList:
                        if ((professor2.coursesRemaining==0.5) or (professor2.coursesRemaining==1.5)) :
                            PotentialCandidates.append(professor2)
                    if len(PotentialCandidates)!=0:
                        PickProfessor2=random.choice(PotentialCandidates)
                        PickProfessor.coursesRemaining-=0.5
                        PickProfessor2.coursesRemaining-=0.5
                        course.addProfTakingCourse(PickProfessor)
                        course.addProfTakingCourse(PickProfessor2)
                        UnassignedProfessor.remove(PickProfessor2)
                        Assigned=True
                    else:
                        PickProfessor.coursesRemaining-=1
                        course.addProfTakingCourse(PickProfessor)
                        Assigned=True
            else:
                if PickProfessor.coursesRemaining==0.5:
                    Assigned=False
                elif PickProfessor.coursesRemaining==1:
                    PickProfessor.coursesRemaining-=1
                    course.addProfTakingCourse(PickProfessor)
                    Assigned=True
                elif PickProfessor.coursesRemaining==1.5:
                    PickProfessor.coursesRemaining-=1
                    course.addProfTakingCourse(PickProfessor)
                    Assigned=True
                