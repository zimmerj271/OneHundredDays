def add(*args):  # NOTE that *args can be called whatever you want.  *numbers for example.
    # The '*' is what indicates we are passing unlimited positional arguments.  *args is the standard nomenclature
    arg_sum = 0
    for n in args:
        arg_sum += n
    print(arg_sum)

def demo(**kwargs): # **kwargs will return parameters as a dictionary
    print(kwargs)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
demo(add=5, multiply=3)
calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") # use to avoid error.  get() will return None if "model" is not included in kw
        self.color = kw.get("color")
        self.seat = kw.get("seat")

my_car = Car(make="Honda", model="Civic")
print(my_car.make, my_car.model)