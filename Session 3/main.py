# x = 5
# print(x)

# # strings
# # int, floats
# # lists, tuples, dict, sets
# # booleans

# print(type(x))

# x = 5

# print("The value of x is " + str(x))

# a = 5
# b = 10

# # print("The value of a is {} and b is {}".format(a, b))

# print(f"The value of a is {a} and b is {b}")

# x = input("Enter a number: ")
# print(x)

# x = int(x)

# print(type(x))

# x = eval(input("Enter a number: "))

# print(x)
# print(type(x))

# x = "5"

# print(type(int(x)))

# if and elif

# x = eval(input("Enter a number [1 - 4]: "))

# if x == 3:
#     print("X is equal to 3")
# elif x == 4:
#     print("X is equal to 4")
# elif x < 1 or x > 4:
#     print(f"X is beyond the range. X is {x}")
# else:
#     print(f"X is either 1 or 2. X is actually {x}")

"""
Write a program that reads the three edges of a triangle and computes the perimeter if the
input is valid. The input is valid if the sum of every pair of two edges is greater than the
remaining edge. Otherwise (i.e. else) print a message stating that the input is invalid and the
perimeter cannot be calculated. (Note: This question does NOT require further input
validation.)
"""
# Alvin
# edge1 = float(input("Enter a length for edge1:"))
# edge2 = float(input("Enter a length for edge2:"))
# edge3 = float(input("Enter a length for edge3:"))

# if edge1 + edge2 >= edge3:
#     print("The perimeter is", edge1 + edge2 + edge3)
# elif edge1 + edge3 >= edge2:
#     print("The perimeter is", edge1+edge2+edge3)
# elif edge2 + edge3 >= edge1:
#     print("The perimeter is", edge1 + edge2 + edge3)
# else:
#     print("invalid")

# Steph
# a = float(input("Enter first edge: "))
# b = float(input("Enter second edge: "))
# c = float(input("Enter third edge: "))

# if a + b >= c and b + c >= a and a + c >= b:
#     print("The parameter is ", a + b + c)
# else:
#     print("Edges are not valid")

# for i in range(1, 10):
#     print(i)

# i = 1
# while i <= 10:
#     i *= 2
#     print(i)

# x = [1, 2, 3]
# x.append(4)

# print(x)

# x = (1, 1, 2, 3)

# print(x)
# print(type(x))

# myList = [1, 1, 2, 3]
# myList.append("Apple")
# myList.insert(0, 8)
# myList.insert(2, 5)

# print(myList)