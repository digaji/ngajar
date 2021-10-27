# Scopes

# A variable is only available from inside the region that it is created
# This is what's called a variable's scope

# Local scope
def hello():
    x = "Hello"
    print(x)

# hello()

# Global scope
x = "Nihao"

def nihao():
    print(x)

# nihao()
# print(x)
# Will work because x is global variable

y = "Sawadikap"

def sawadikap():
    y = "Namaste"
    print(y)

# sawadikap()
# print(y)

def bonjour():
    global z
    z = "Bonjour"
    print(z)

# bonjour()
# print(z)

a = "Konnichiwa"

def my_func():
    global a
    a = "Xin Chao"
    print(a)

my_func()
print(a)
