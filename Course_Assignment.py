import random
import copy
from Course_Type import *
from Course_Input import *
from Professor_Input import *

def Course_Assignment():
    CDCList=[]
    ELCList=[]
    UnassignedProfessor=copy.deepcopy(professorList)
    for course in [*d.values()]: #gets list of values in dictionary
        if ((course.getCourseType()==Course_Type(1).name) or (course.getCourseType()==Course_Type(2).name)):
            local_course = copy.deepcopy(course) #creates a local copy of each CDC course
            CDCList.append(local_course)       
    for course in [*d.values()]:
        if ((course.getCourseType()==Course_Type(3).name) or (course.getCourseType()==Course_Type(4).name)):
            local_course = copy.deepcopy(course) #creates a local copy of each ELC course
            ELCList.append(local_course)
    for course in CDCList:
        UnassignedProfessorsWithCourseInPriorityList=[]
        for professor in UnassignedProfessor:
            if (professor.coursesRemaining>0 and ((course.getCourseCode() in list((professor.Priority_Order_FDCDC).values())) or (course.getCourseCode() in list((professor.Priority_Order_HDCDC).values())))):
                UnassignedProfessorsWithCourseInPriorityList.append(professor)
        Assigned=False
        while UnassignedProfessorsWithCourseInPriorityList and Assigned==False:   #loops until a professor is assigned to this course
            PickProfessor=random.choice(UnassignedProfessorsWithCourseInPriorityList) #chooses one of the professors who have this course in their priority list
            UnassignedProfessorsWithCourseInPriorityList.remove(PickProfessor)            
            if UnassignedProfessorsWithCourseInPriorityList:
                if PickProfessor.coursesRemaining==0.5:
                    PotentialCandidates=[]
                    for professor2 in UnassignedProfessorsWithCourseInPriorityList:
                        if ((professor2.coursesRemaining==0.5) or (professor2.coursesRemaining==1.5)) :
                            PotentialCandidates.append(professor2)
                    if PotentialCandidates:
                        PickProfessor2=random.choice(PotentialCandidates)
                        PickProfessor.coursesRemaining-=0.5
                        PickProfessor2.coursesRemaining-=0.5
                        course.addProfTakingCourse(PickProfessor)
                        course.addProfTakingCourse(PickProfessor2)
                        if PickProfessor2.coursesRemaining==0:
                            UnassignedProfessor.remove(PickProfessor2)                                
                        UnassignedProfessor.remove(PickProfessor)
                        Assigned=True
                
                elif PickProfessor.coursesRemaining==1:
                    PickProfessor.coursesRemaining-=1
                    course.addProfTakingCourse(PickProfessor)
                    UnassignedProfessor.remove(PickProfessor)
                    Assigned=True
                
                elif PickProfessor.coursesRemaining==1.5:
                    PotentialCandidates=[]
                    for professor2 in UnassignedProfessorsWithCourseInPriorityList:
                        if ((professor2.coursesRemaining==0.5) or (professor2.coursesRemaining==1.5)):
                            PotentialCandidates.append(professor2)
                    if PotentialCandidates:
                        PickProfessor2=random.choice(PotentialCandidates)
                        PickProfessor.coursesRemaining-=0.5
                        PickProfessor2.coursesRemaining-=0.5
                        course.addProfTakingCourse(PickProfessor)
                        course.addProfTakingCourse(PickProfessor2)
                        if PickProfessor2.coursesRemaining==0:
                            UnassignedProfessor.remove(PickProfessor2)                            
                        Assigned=True
                    else:
                        PickProfessor.coursesRemaining-=1
                        course.addProfTakingCourse(PickProfessor)
                        Assigned=True
            else:
                if PickProfessor.coursesRemaining==0.5:
                    UnassignedProfessorsWithCourseInPriorityList.remove(PickProfessor)
                elif PickProfessor.coursesRemaining==1:
                    PickProfessor.coursesRemaining-=1
                    course.addProfTakingCourse(PickProfessor)
                    UnassignedProfessor.remove(PickProfessor)
                    Assigned=True
                else:
                    PickProfessor.coursesRemaining-=1
                    course.addProfTakingCourse(PickProfessor)
                    Assigned=True
                        
    
    for course in ELCList:
        UnassignedProfessorsWithCourseInPriorityList=[]
        for professor in UnassignedProfessor:
            if (professor.coursesRemaining>0 and ((course.getCourseCode() in list((professor.Priority_Order_FDELC).values())) or (course.getCourseCode() in list((professor.Priority_Order_HDELC).values())))):
                UnassignedProfessorsWithCourseInPriorityList.append(professor)
        numberOf0_5Profs=0
        numberOf1Profs=0
        numberOf1_5Profs=0
        for prof in UnassignedProfessorsWithCourseInPriorityList:
            if prof.coursesRemaining==0.5:
                numberOf0_5Profs+=1
            elif prof.coursesRemaining==1:
                numberOf1Profs+=1
            elif prof.coursesRemaining==1.5:
                numberOf1_5Profs+=1
        Assigned=False
        if ((numberOf0_5Profs<2) and (numberOf1Profs==0) and (numberOf1_5Profs==0)): #checks if it is possible to assign elective
            Assigned=True
        
        if UnassignedProfessorsWithCourseInPriorityList:
            while Assigned==False:   #loops until a professor is assigned to this course
                PickProfessor=random.choice(UnassignedProfessorsWithCourseInPriorityList) #chooses one of the professors who have this course in their priority list
                UnassignedProfessorsWithCourseInPriorityList.remove(PickProfessor)
                
                if UnassignedProfessorsWithCourseInPriorityList:
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
    CDCList.extend(ELCList)
    return CDCList