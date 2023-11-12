class Student:

    # The first parameter need not be 'self',it can be anything --which eventually will point to the
    # instance of the current object fow which it has been called
    def display(instance, name):
        print(name)

def mainreftoself():
    s = Student()
    s.display("Johnny")
    Student.display(s, "James") # This is just another way of calling the method. Here 's' is nothing but the reference of the class Student

