

# Default argument:if argument to the function is empty ...default value will be set to the variable

def myfunction(x, y=50):
    print("x: ", x)
    print("y: ", y)

myfunction(10)


# Keyword Argument:passing arguments by using parameter names

def function1(lname,fname):
    print(fname,lname)

function1(lname="tarun",fname="amaraneni")


# Positional Arguments: values are assigned to parameters based on their order in the function call.

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("Case-2:")
nameAge(27, "Olivia")



# Arbitrary Arguments: allow functions to accept multiple values. This is done using two special symbols:

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')