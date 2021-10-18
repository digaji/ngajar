# Strings
my_string = "  woah dude, JUST take it slow"
# print("my_string has the content {}".format(my_string))

print(my_string[-1])
print(my_string[::-1])

# Methods
print(my_string.capitalize())
# First character uppercased, the rest lowercased

print(my_string.upper())
# All characters uppercased

print(my_string.casefold())
# All characters returned as lowercased

print(my_string.replace("woah", "yo"))
# Replace old value with new value

print(my_string.center(50))
print(my_string.center(50, "!"))
# Can specify the padding characters

print(my_string.islower())
print(my_string.isupper())
# Checks all characters in a string and returns boolean

print(my_string.split())
# Splits the string's character into list elements
print(my_string.split(","))
# Can specify the separator

print(my_string.strip())
# Remove any leading or trailing whitespaces

# There are still a lot of string methods out there

print("my_string content = {}".format(my_string))
print(f"my_string content = {my_string}")