"""
This is Object Oriented approach. The same task has been in object oriented manner.
"""
class Student:
    # Declaration of the below attribute explicitly in class is OPTIONAL under object oriented approach.
    # name: str
    # age: int
    # gender: str

    def __init__(self, name:str, age:int, gender:str):
        self.name = name
        self.age = age
        self.gender = gender

    def print_student(self):
        print(self.name)
        print(self.age)
        print(self.gender)

def objectOriented_main():
    student2 = Student(name="Kavita", age= 16, gender="Female")
    student2.print_student()

