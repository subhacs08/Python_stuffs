class CompileTimePolymorphism:
    """
    Python being interpreted language, the interpreter scans the code line by line. With this,
    given multiple version of a method, the latest version replaces the previous version and only
    the latest version of the method remains alive in the memory.

    In the current case, the do_something() method with parameter 'hello' gets loaded in the memory
    and the one without any parameter does not exist anymore in the memory.

    So whenever we call the method without any parameter E.g do_something() ---> this triggers the
    earlier version of the method call where no parameter has been passed. And as discussed above this version of the
    signature does not exist in the memory and hence the compiler throws error
    TypeError: CompileTimePolymorphism.do_something() missing 1 required positional argument: 'hello'
    indicating to call do_something() with passing a parameter irrespective of number of call being made.

    In summary, Python does not support method overloading/compile time polymorphism/early binding
    """

    def do_something(self):
        print("called without param")
        return 0

    def do_something(self, hello):
        print("called with param")
        return ""


def main_compiletimepolymorphism():
    ctp = CompileTimePolymorphism()
    ctp.do_something("")
    ctp.do_something("test")
