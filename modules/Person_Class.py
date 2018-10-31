import uuid
from Person_Class import *
from School_Class import *

class Person:
    def __init__(self, name, role):
        self._name = name
        self.__id = self.gernerateId()
        self.__role = role
        self.__school = None
        self.__courses = []

    @staticmethod
    def gernerateId():
        return uuid.uuid4()

    def getName(self):
        return self._name

    def getId(self):
        return self.__id

    def registerSchool(self, school):
        if not isinstance(school, School):
            raise TypeError("Cannot register school. Arg must be a school type")

        self.__school = school

    def enrollCourse(self, course):
        if not isinstance(course, Course):
            raise TypeError(self.__class__.__name__ + " Add course operaion cannot be performed" + 
            "Arg must be a Course Type")

        self.__courses.append(course)

    def quitCourse(self, course):
        if not isinstance(course, Course):
            raise TypeError(self.__class__.__name__ + " Quit course operaion cannot be performed" + 
            "Arg must be a Course Type")

        if course not in self.__courses:
            print("Cannot quit course because you are not enrolled in it")

        self.__courses.pop(course)      