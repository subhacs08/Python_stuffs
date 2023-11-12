class Parent:
    def __init__(self, name):
        self._name = name

    def printname(self):
        print("Inside parent class's printname method")
        print("from Parent .. " + self._name)


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def printname(self):
        print("Inside Child class printname method")
        print("from child .. " + self._name)
        print("Calling printname method from Parent class")
        # both the below 2 lines works equivalent in nature
        super(Child, self).printname()
        super().printname()


def mainsuper():
    p = Parent("Base_Class")
    p.printname()
    c = Child("Inherited_Class")
    c.printname()

