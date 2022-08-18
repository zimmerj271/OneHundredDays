def f1(func):
    def wrapper_function():
        print("Started")
        func()
        print("Ended")
    return wrapper_function

def f2():
    print("Hello")

# Note that f2 returns a function, so this declaration will
# return nothing since it needs to be treated like a function.
f1(f2)

# Adding parenthesis makes the appropriate function call and
# will call wrapper_function as defined within function f1
f1(f2)()

# Python treats f1(f2) as an object, so it can be stored as a variable
f = f1(f2)
f()

# A decorator allows for a shortcut to pass f2 to f1 without the nested
# function call and/or storing it as a variable
@f1
def f3():
    print("Using a decorator")
f3()

# To pass parameters to a function that uses a decorator, need to declare
# *args and/or **kwargs within the wrapper_function
def my_decorator(func):
    def my_wrapper(*args, **kwargs):
        print("Started")
        func_val = func(*args, **kwargs)  # to correctly return value, save function to variable
        print("Ended")
        return func_val  # return the function call at the end to pass the output of the decorator
    return my_wrapper

@my_decorator
def add(a, b=3):
    return a + b

val = add(2)
print(val)

# timer decorator example
# This is a common method of testing how long an alogirthm takes to run
import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")
    return wrapper

@timer
def run():
    time.sleep(2)

run()

# Using a decorator inside a class
def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print("run")

t = Test()
t.decorated_method()
