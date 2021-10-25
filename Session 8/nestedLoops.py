# Nested Loops

my_list = [1, 2, 3, "apple", "apple", 1]
my_tuple = (3, 4, 5, "pineapple")

# # Regular for loops
# for element in my_list:
#     print(element)

# # While loop equivalent
# x = 0
# while x < len(my_list):
#     print(my_list[x])
#     x += 1

# Going through two things
n = 1
for element in my_list:
    print(f"{n} iterations")
    print(element)
    print("Going inside my_tuple")

    for thing in my_tuple:
        print(thing)

    print("\n")
    n += 1

print("Done!")