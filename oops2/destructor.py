class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

    def __del__(self):
        print("Destructor invoked")


def maindestructor():
    s1 = Student("John", 20)
    s1.display()
    # del s1
    s2 = Student("Jimmy", 23)
    s2.display()
    print(s2.name)
    print(s1.name)  # this won't work after 'del  s1' line being executed
