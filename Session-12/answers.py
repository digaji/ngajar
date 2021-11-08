# No. 1

my_prog = {
    "Go": "A statically typed, compiled programming language designed at Google",
    "Java": "A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible",
    "C++": "A general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language",
    "Kotlin": "a cross-platform, statically typed, general-purpose programming language with type inference",
    "Swift": "A general-purpose, multi-paradigm, compiled programming language developed by Apple Inc. and the open-source community"
}

sequence = ["C++", "Java", "Kotlin", "Go", "Swift"]

for key in sequence:
    print(key + "\n" + my_prog.get(key))
    if key != sequence[-1]:
        print()

# No. 2

cars = {
    "JJ": ["Golf", "Camry", "LFA"],
    "Nicklas": ["Innova", "Panther", "Fortuner"],
    "Vincent": ["Yaris", "Jazz", "Polo"],
    "Gardyan": ["320i", "E300", "Freed"],
    "Coki": ["Wraith", "Dawn", "991"]
}

for key in cars.keys():
    print(key, "likes these cars:")
    for element in cars.get(key):
        print("-", element)
    print()