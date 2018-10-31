from Course_Class import *

class School:
    def __init__ (self, location):
        self.__location = location
        self.__courses = []

    def setLocation(self, location):
        self.__location = location

    def getLocation(self):
        return self.__location

    def addCourse(self, course):
        if not isinstance(course, Course):
            raise TypeError("Add course operaion cannot be performed" + 
            "because this is not a Course Type")

        self.__courses.append(course)

    def getCourses(self):
        return self.__courses      
