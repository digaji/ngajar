# Open multiple files

with open("hihi.txt", "r", encoding="utf-8") as file:
    with open("hehe.txt", "w", encoding="utf-8") as new:
        print(file.read())
        print(new.read())
