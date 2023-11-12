"""
Python support method overriding/run time polymorphism/late binding
"""


class A:

    def do_something(self, hello):
        print("called with param at Parent")


class B(A):

    def do_something(self, hello):
        print("called with param at Child")


def main_runtimepolymorphism():
    a = A()
    b = B()
    a.do_something("some_value")  # this outputs "called with param at Parent"
    b.do_something("test")  # this outputs "called with param at Child"
