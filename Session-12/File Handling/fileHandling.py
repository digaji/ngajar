# File Handling

with open("hehe.txt", "r") as f:
    print(f.read())

print("Yes")
print(f.read())
# ^ Cannot because file is already closed