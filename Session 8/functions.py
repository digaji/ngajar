# Functions

def my_func():
    print("Hello my func")

# my_func()

# def new_func(name):
#     print("Hello " + str(name))

# Type hinting

def new_func(name: str):
    print("Hello " + name)

# new_func(5)

# The number of parameters and arguments that you pass in matters
def another_func(fName, lName):
    print(fName + " - " + lName)

# another_func("woah", "bruh")

def compare(number1: int, number2: int):
    if number1 < number2:
        print(f"The 2nd number, {number2}, is greater!")
    else:
        print(f"The 1st number, {number1}, is greater!")

# x = compare(1, 2)
# print(x)

def complete_func(number1: int, number2: int) -> str:
    """Compares and prints which of the 2 numbers passed in is greater
    """
    if number1 < number2:
        return f"The 2nd number, {number2}, is greater!"
    else:
        return f"The 1st number, {number1}, is greater!"

x = complete_func(1, 2)
print(x)