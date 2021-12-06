class Person:
    # Class variable
    __num_of_ppl = 0

    # Regular methods
    def __init__(self, name):
        # Instance variable
        self.__name = name
        Person.add_ppl()
        # self.__greeting()

    def get_name(self):
        self.__greeting()
        return self.__name

    # Class method
    @classmethod
    def get_num(cls):
        return cls.__num_of_ppl

    @classmethod
    def add_ppl(cls):
        cls.__num_of_ppl += 1

    # Static method
    @staticmethod
    def return_name(x):
        return f"name {x}"

    # Regular method
    def __greeting(self):
        print(f"My name is {self.__name}")


p1 = Person("hugo")
print(p1.get_name())
# print(p1.get_num())

p2 = Person("nicklas")
# print(Person.get_num())
print(p1.return_name("Hello"))
# print(p1.get_name())
# print(p2.get_name())

# print(p1.get_num())

