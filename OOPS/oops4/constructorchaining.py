class A:
    def __init__(self):
        print("Inside class A's init method")


class B(A):
    def __init__(self):
        super().__init__()  # need to do this explicitly in python, chaining does not happen automatically in python
        print("Inside class B's init method")


class C(B):
    def __init__(self):
        super().__init__()  # need to do this explicitly in python, chaining does not happen automatically in python
        print("Inside class C's init method")


def main_constructorchaining():
    print("Initializing A class's init method")
    a = A()
    print("Initializing B class's init method")
    b = B()
    print("Initializing C class's init method")
    c = C()
