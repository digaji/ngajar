#%%
# No. 1
import time

def delay(message, jeda):
    time.sleep(jeda)
    print(message)

delay("This is message", 5)

#%%
# No. 2
def diamond(height):
    for i in range(height):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))   # Use + 1 because index only counts until height-1
    for i in range(height - 2, -1, -1):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))

diamond(eval(input("Type the height that you want: ")))

# More "efficient"
def diamond1(height):
    for i in list(range(height)) + list(range(height - 2, -1, -1)):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))

diamond1(eval(input("Type the height: ")))

#%%
# No. 3
def emirpChecker(number):
    # Get reversed version of inputted number
    reversed = int(str(number)[::-1])

    # If number and reversed greater than 1 and if the number doesn't equal to itself reversed
    if number > 1 and reversed > 1 and number != reversed:
        # Check if number == NOT prime (can be divided by 2 until number - 1)
        for i in range(2, number):
            if (number % i == 0):
                print("False!")
                return False
        # Check if reversed == NOT prime (can be divided by 2 until number - 1)
        for i in range(2, reversed):
            if (reversed % i == 0):
                print("False!")
                return False
        print(f"{number} {reversed}")
        return True
    else:
        print("False!")
        return False

emirpChecker(13)
emirpChecker(347)
emirpChecker(5)

# %%
