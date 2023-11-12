class Student:
    def __init__(self, name):
        self.__name = name

    # Getter method
    @property
    def name(self):
        return self.__name

    # Setter method
    @name.setter
    def name(self, new_name):
        self.__name = new_name


def maingettersetter():
    stu = Student("John")
    print(stu.name)
    stu.name = "James"
    print(stu.name)
