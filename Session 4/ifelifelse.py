a = 5

# if a == 5: # Checks for boolean in front of if before running
#     print(a)
# elif a == 6: # Gets checked if any ifs or elifs above it doesn't run
#     print(7)
# else: # Always runs as long as nothing is run above it
#     print("Wow")

# if a > 8:
#     print(a)
# elif a == 7:
#     print(a)
# elif a == 5:
#     pass
# elif a == 8:
#     pass
# else:
#     print("Wow")

if a > 8:
    print(a)
else:
    if a > 10:
        print(f"a is {a}")
    else:
        print(f"a is actually {a}")
