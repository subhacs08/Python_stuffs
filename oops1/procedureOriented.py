"""
This is a demonstration of procedure oriented usage of class in python
In this example class Student has been used as STRUCT is used in JAVA. There is no concept of STRUCT
in Python, dataclass decorated Student class enables us to use the same
"""
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    gender: str

def print_student(stu: Student):
    print(stu.name)
    print(stu.age)
    print(stu.gender)

def procedureOriented_main():
    student1 = Student(name="John", age=18, gender="Male")
    print_student(student1)
