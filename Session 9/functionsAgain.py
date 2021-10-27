# Functions

def triple(number1):
    return number1 * 3

# print(triple(3))

# Keyword arguments
def greet(name, msg):
    print("Hello", name + "! " + msg)

# # greet("Walbert", "Wow you're so cool!")

# # Keyword arguments in order
# greet(name="Walbert", msg="Wow you're so cool!")

# # Keyword arguments out of order
# greet(msg="Wow you're so cool!", name="Walbert")

# # Mix
# greet("Walbert", msg="Wow you're so cool!")

# *args
# When you don't know the number of arguments that will be passed in

def hello(*names):
    for name in names:
        print("Hello", name)

# hello("Filbert", "Reyhan", "Alvin", "Dio")

def my_sum(*integers):
    result = 0
    for integer in integers:
        result += integer
    return result

# print(my_sum(1, 2, 3, 4, 5))

# **kwargs

def my_func(**name):
    print("Their first name is " + name["fName"])

my_func(lName = "Jeremy", fName = "Jason")