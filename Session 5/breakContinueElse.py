# break statement

x = 1

while x < 10:
    print(x)
    if x > 5:
        break
    x += 2

# while x < 10, keep printing x but break when it's greater than 5
# break exits the loop

# continue statement
x = 1

while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)

# if x reaches 5, the current iteration of the loop ends and the next iteration starts (so print(x) is not reached)
# continue exits the current iteration of the loop

# else statement
x = 0

while x < 5:
    print(x)
    x += 1
else:
    print("While loop is done!")
    print("x is now greater than 5")

# else after while -> Runs once the condition for the while loop isn't true anymore