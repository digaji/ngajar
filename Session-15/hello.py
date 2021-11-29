# Class

# Blueprint
class Person:
    # Initialize
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f"Person: {name} created!")

    def greet(self):
        print(f"Hi! My name is {self.name}")
        print(f"I'm {self.age} years old!")

    def __str__(self):
        return (
            f"My name is {self.name}. I'm {self.age}. And I make {self.salary} dollars!"
        )


# me = Person("JJ", 19, 50)

# print(me)

# Get the attributes
# print(me.name)
# print(me.age)
# print(me.salary)

# Call the method
# me.greet()

# student = Person("Student", 18, 0)

# print(student.age)

# # Changing property value
# student.age = 20

# print(student.age)
