from person import Person
from comp.something import something


class Animal:
    def __init__(self, legs, weight, lifespan):
        self.__legs = legs
        self.__weight = weight
        self.__lifespan = lifespan

    def make_sound(self):
        return "No sound"

    # Getters
    def get_legs(self):
        return self.__legs

    def get_weight(self):
        return self.__weight

    def get_lifespan(self):
        return self.__lifespan

    # Setters
    def set_legs(self, new_legs):
        self.__legs = new_legs

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def set_lifespan(self, new_lifespan):
        if new_lifespan < 1:
            return f"New lifespan of {new_lifespan} doesn't make sense"
        self.__lifespan = new_lifespan

    # Method
    def will_live(self, age=None):
        if age == None:
            return f"This animal will live until {self.__lifespan} years old"
        else:
            return self.will_live() + f" But, this one has lived for {age} years"


class Dog(Animal):
    def __init__(self, weight):
        # To inherit from superclass
        super().__init__(4, weight, 30)

    # Overriding a method
    def make_sound(self):
        return "Bark"

    def make_sound(self, integer):
        return "Bark " * integer


class Fish(Animal):
    def __init__(self, weight, lifespan):
        super().__init__(0, weight, lifespan)

    # Overriding
    def make_sound(self):
        return "Glug, glug"


if __name__ == "__main__":
    cat = Animal(4, 5, 3)
    bro = Dog(20)
    nemo = Fish(3, 5)

    # print(cat._Animal__legs)
    # print(cat.make_sound())
    print(bro.make_sound())
    print(bro.make_sound(5))
    # print(nemo.make_sound())

    # print(cat.will_live(2))
    # print(bro.will_live(15))
    # print(nemo.will_live(10))
