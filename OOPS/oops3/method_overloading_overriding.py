class A:
    def do_something(self, arg: str) -> None:
        print("printing from parent with string parameter")

    def do_something(self, arg: int) -> None:
        print("printing from parent with integer parameter")


class B(A):
    def do_something(self, arg: int) -> None:
        print("printing from parent with integer parameter")

    def do_something(self, arg: str) -> None:
        print("printing from child with string parameter")


def main_overloading_overriding():
    a = A()
    b = B()
    a.do_something("test")
    a.do_something(12)
    b.do_something("test123")
    b.do_something(15)
