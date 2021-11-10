# Error Handling

# print("Hello" + 15) # Will error out the program

# Way to handle error
try:        # Statement to try and execute
    print("Hello" + 15)
except:     # Statement to do when an error happens
    print("Hello", 15)
finally:    # Statement to do regardless of the outcome from the try and except
    print("Done")

# Figuring out what error occurs
try:
    print("Hi" + 15)
except Exception as e:
    print(type(e))
    print(e)

try:
    print(5 / 0)
except Exception as e:
    print(type(e))

try:
    divide_by = eval(input("Input something to divide 5 by: "))
    print(5 / divide_by)
except ZeroDivisionError:   # Handle when ZeroDivisionError is raised
    print("Cannot divide with 0!!!!")
except TypeError:           # Handle when TypeError is raised
    print("Enter an integer!!!")
finally:
    print("Done")

try:
    divide_by = eval(input("Input something to divide 5 by: "))
    print(5 / divide_by)
except (ZeroDivisionError, TypeError):   # Handle when ZeroDivisionError and/or TypeError is raised
    print("Cannot!!!!")
finally:
    print("Done")

# Testing
x = eval(input("Input a number greater than 10: "))

try:
    assert x > 10
except Exception as e:
    print(type(e))
else:   # Only get executed if no errors were raised
    print(f"The value of x: {x} is greater than 10")