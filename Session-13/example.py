# Try to open a file that doesn't exist

filename = input("Enter a filename: ")

try:
    assert open(filename, "r")
except FileNotFoundError:
    print("File doesn't exist! Creating a new file...")
    with open(filename, "w") as f:
        f.write("Look I'm a new file!")
finally:
    with open(filename, "r") as f:
        print(f.read())

# Send through zoom private chat and we see the first 3 answers :)

# * --------------------------------------------------------------- * #

# filename = input("Enter a filename: ")

# try:
#     assert open(filename, "r")
# except:
#     print("File doesn't exist")
#     file = open("{}".format(filename),"w")
#     file.write("I'm a new file")
#     file.close()
# finally:
#     with open(filename, 'r') as f:
#         print(f.read())
# ^ Closest attempt, forgot to close() so can't print(f.read()) :(