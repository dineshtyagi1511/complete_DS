print("Function")
"""The def keyword is used to define a function in Python.
A function is a reusable block of code that performs a specific
       task."""

"""
def function_name(parameters):
    # code block
    return value  # optional
"""


print("##################3")

"""*args (Positional Arguments)
*args allows a function to accept any number of
 positional arguments (non-keyword arguments).

Inside the function, args is a tuple containing 
all passed values."""

print("*args")
def add_numbers(*args):
    total =0 
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))   
print(add_numbers(4, 5))     


"""**kwargs (Keyword Arguments)
**kwargs allows a function to accept any number 
of keyword arguments (key=value pairs).

Inside the function, kwargs is a dictionary containing
 all passed key-value pairs."""

print("**Kwargs")

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Dinesh", age=26)

print("########")
def user_info(role, **kwargs):
    print(f"Role: {role}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info("Developer", name="Dinesh", age=26)



print("#####################")

print("Lambda function ")
"""
What is a Lambda Function?

A lambda function is a small anonymous function.

It can have any number of arguments, but only one expression.

The expression is evaluated and returned automatically."""


print("Syntax:","lambda arguments: expression")

square = lambda x: x**2
print(square(5))  

