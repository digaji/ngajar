# Dictionary Use Cases

import time
import random

# Quick Look Up
my_list = ["apple", "banana", "cherry", "strawberry"]

my_dict = {
    "fruit1": "apple",
    "fruit2": "banana",
    "fruit3": "cherry",
    "fruit4": "strawberry"
}

# start = time.perf_counter()
# my_list[3]
# print(f"The list took {time.perf_counter() - start} to finish")

# start = time.perf_counter()
# my_dict["fruit3"]
# print(f"The dictionary took {time.perf_counter() - start} to finish")

# List is still faster

long_list = random.sample(range(1000000 + 1), 1000000)

long_dict = {x: x for x in random.sample(range(1000000 + 1), 1000000)}

def find_in_list(lst, number):
    if number in lst:
        return True
    else:
        return False

def find_in_dict(dct, number):
    if number in dct.keys():
        return True
    else:
        return False

start = time.perf_counter()
find_in_list(long_list, 999999)
print(f"The list took {time.perf_counter() - start} to finish")

start = time.perf_counter()
find_in_dict(long_dict, 999999)
print(f"The dictionary took {time.perf_counter() - start} to finish")