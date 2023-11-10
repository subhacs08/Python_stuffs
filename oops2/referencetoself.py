class Student:

    def display(self, name):
        print(name)

def mainreferencetoself():
    s = Student()
    s.display("Johnny")
    Student.display(s, "James") # This is just another way of calling the method. Here 's' is nothing but the reference of the class Student

