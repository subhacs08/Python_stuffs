class Person:
    def __init__(self, name=None):
        if name is None:
            print("Default Constructor called")
        else:
            print(f"Parameterised constructor called with parameter value {name}")
            self.name = name

    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")


def mainconstructor() -> None:
    m = Person()
    m.method()
    f = Person("Ravinaa")
    f.method()
