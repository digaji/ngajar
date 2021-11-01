# Dictionary

my_dictionary = {"brand": "Onda", "model": "Accordian", "year": 2002}
# Ordered + unindexed + mutable + no duplicates
# Key:value pairs
# NOTE: Dictionaries are only ordered with python ver 3.7+

# print(my_dictionary)

# Access value from key
print(my_dictionary["brand"])

my_dictionary = {
    "brand": "Ponda",
    "model": ["Accordian", "Prv", "Pity", "Pivic"],
    "colour": ["Red", "White", "Pondation"]
}

# Methods
print(my_dictionary.keys())

print(my_dictionary.values())

print(my_dictionary.items())

# Remove according to key
x = my_dictionary.pop("colour")
print(x)
print(my_dictionary)

# Get values from keys
print(my_dictionary.get("model"))
print(my_dictionary.get("price"))
print(my_dictionary.get("price", 2000))

# Update dictionary
my_dictionary.update({"branch": "Jakarta"})
print(my_dictionary)

my_dictionary.update({"brand": "Donda"})
print(my_dictionary)