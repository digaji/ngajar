# Tuples

my_tuple = (1, 2, 3, "apple", 1, 2, 2)
# Ordered + indexed + immutable + allow duplicates

# print(len(my_tuple))

# print(my_tuple[0])

# my_tuple[0] = 3
# ^ This will error out

# Methods
x = my_tuple.count(2)
print(x)
# Counts how manny times a value appears in my_tuple

y = my_tuple.index(2)
print(y)
# Returns the first occurence of the value specified in my_tuple

# Only 2 methods :)
print(my_tuple)