def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# NOTE: python functions are known as 'first-class objects', which can be passed around as arguments
# eg int/string/float etc

# in the calculate function we define parameters which take a function and ints/floats
# this is an example of a function being used as an object which is passed as a parameter to another function
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(multiply, 3, 5)
print(result)

# Nested functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

# Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function  # return a reference to nested_function, suppress '()'

inner_function = outer_function()  # stores reference to nested_function() as a variable
inner_function()  # activate the referenced function by adding '()'

# Python decorator function
# a decorator function is a function that wraps another function and gives it additional functionality
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_hello()
say_bye()
say_greeting()

# can also pass decorator as reference
decorated_function = delay_decorator(say_greeting)
decorated_function()