from Animal import *


class HHStudent(Animal):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def print_score(self):
        print("%s,%s" % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name = name

    def set_score(self,score):
        self.__score = score

    def run(self):
        print("humans is running")
