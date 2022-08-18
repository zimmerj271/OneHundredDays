# Abstract classes prevent a user from creating an object of that class
# and compels the user to override any abstract methods in a child class.
# At minimum, each child class must include an implementation of the abstract methods,
# defined in the parent class, or an error will occur.

# Python does not have abstract classes implemented by default.
# To create an abstract class, you must import from the 'abc' library

from abc import ABC, abstractmethod


class Vehicle(ABC):  # abstract class inherits from class ABC in library abc

    @abstractmethod  # to create an abstract method, must use the @abstractmethod decorator
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def move(self):
        pass


class Car(Vehicle):

    # Because the go method is defined as an abstract method in the Vehicle
    # class, it is required to be implemented in the Car class since it is
    # a child class of the Vehicle class.
    def go(self):
        print("Car is going")

    def stop(self):
        print("Car is stopping")


class Motorcycle(Vehicle):

    def go(self):
        print("Motorcycle is going")

    def stop(self):
        print("Motorcycle is stopping")

# since Vehicle is an abstract class,
# instantiating a Vehicle object with throw an error
# vehicle = Vehicle()

car = Car()
car.go()
car.stop()

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

# Not an abstract method, so not required to be implemented for each child class.
# The child classes inherit this method from the parent class per OOP.
car.move()
