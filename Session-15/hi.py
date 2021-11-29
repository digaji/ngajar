from hello import Person


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


class Dog(Animal):
    def __init__(self, weight):
        super().__init__(4, weight, 30)


cat = Animal(4, 5, 3)

aric = Person("Aric", 20, 35)

# print(cat.get_legs())

# print(cat.get_legs())

# print(cat.legs)
