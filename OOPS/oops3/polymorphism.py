class Animal:

    def make_sound(self) -> None:
        print("Animal speaking")


class Dog(Animal):

    def make_sound(self) -> None:
        print("Barking ...")


class Cat(Animal):

    def make_sound(self) -> None:
        print("Meu-ing ...")

class Human(Animal):
    pass


def main_polymorphism():
    dog = Dog()
    dog.make_sound()
    cat = Cat()
    cat.make_sound()
    hu = Human()
    hu.make_sound()

