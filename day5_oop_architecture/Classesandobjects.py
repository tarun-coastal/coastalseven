
class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house



        
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self,house):
        if house not in ["gnt","hyd"]:
            raise ValueError("wrong")
        self._house =house

    def __str__(self):
        return f"{self.name} is from {self.house}"


def get_student():
    name=input("name? ")
    house=input("house? ")
    return Student(name,house)


def main():
    student=get_student()
    student.house="a"
    print(f"{student.name} is from {student.house}")
    print(student)

main()

# class methods
import random

class Hat:
    houses=["guntur","amaravati","pedakurapadu","hyderabad"]

    @classmethod
    def sort(cls,name):
        print(f"{name} is from {random.choice(cls.houses)}")




Hat.sort("harry")