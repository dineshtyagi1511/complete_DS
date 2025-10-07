"""Why Error Handling?
To prevent your program from crashing, you 
use try–except blocks."""

"""try:
    # Code that may cause an error
except:
    # Code to handle the error"""
## basic 
try:
    print(10/0)
except Exception as e:
    print("Error name :" ,e)

"""else block

Runs only if no exception occurs inside try."""


"""finally block

Runs always, no matter if there’s an error or not — 
usually used for cleanup (like closing files or connections)."""

try:
    print(10/1)
except Exception as e :
    print("Exception:", e)
else:
    print("code runs Succesfully")
finally:
    print("M to chalunga ")

"""The raise Keyword:

Used to manually raise an exception."""

def Division(a,b):
    if b==0:
        raise ZeroDivisionError("can't divide by zero")
    return a/b

try:
    print(Division(10,0)) 
except Exception as e:
    print("Error:",e)
    
"""Custom Exceptions

You can create your own error types by inheriting 
from Python’s built-in Exception class."""

class NegativeNumberError(Exception):
    """Raised when a number is negative"""
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed!")
    else:
        print("Number is valid")

try:
    check_number(-5)
except NegativeNumberError as e:
    print("Error:", e)

    

