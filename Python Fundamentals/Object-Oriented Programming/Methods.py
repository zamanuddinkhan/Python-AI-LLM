"""
Methods: Methods are functions that belong to an object or a class.
They are used to perform operations on that object.

Types of Methods:
1. Instance Methods: Work with object (instance) data. Take self as the first parameter.
Example:
"""
class Student:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("Name:",self.name)

s = Student("Zaman")
s.display()
