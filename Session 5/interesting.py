import random

my_list = [1, 2, 3, "apple", "bird"]
count = 1

while 2 in my_list:
    print(f"2 is still in my_list! It's been {count} iterations")
    count += 1
    my_list.pop(random.randrange(len(my_list)))

# Pops an element from my_list from a random range within the length of my_list

# Difference between randrange and randint -> randint includes the upper range but randrange doesn't