def FitnessScore(localCourseList):
    score=0
    for course in localCourseList:
        for professor in course.profsTakingCourse:
            for key,value in professor.Priority_Order_FDCDC.items():
                if value==course.getCourseCode():
                    score+=abs(100-key)
            for key,value in professor.Priority_Order_HDCDC.items():
                if value==course.getCourseCode():
                    score+=abs(100-key)
            for key,value in professor.Priority_Order_FDELC.items():
                if value==course.getCourseCode():
                    score+=abs(100-key)
            for key,value in professor.Priority_Order_HDELC.items():
                if value==course.getCourseCode():
                    score+=abs(100-key)
    return score
        