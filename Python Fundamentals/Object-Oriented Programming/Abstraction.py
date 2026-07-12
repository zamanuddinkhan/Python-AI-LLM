# Abstraction: Hiding the implementation details and showing only the essential functionality to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        # Internal implementation is hidden from the user.
        self.clutch = True
        self.acc = True
        print("Car Starting.....")

c = Car()
c.start()

"""
Abstract Class:
A class that contains one or more abstract methods.
It cannot be instantiated (you cannot create its object directly).

Abstract Method:
A method declared using @abstractmethod that has no implementation in the abstract class.
Every child class must override it.
"""

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    # Abstract Method
    @abstractmethod
    def sound(self):
        pass


# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

d = Dog()
d.sound()

# a = Animal()   # ❌ Error: Cannot create an object of an abstract class.