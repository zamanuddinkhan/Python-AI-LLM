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

"""
2. Class Methods: A class method works with class variables (variables shared by all objects).
It does not work with individual object data.
Example:
"""
class Bank:
    bank = "HDFC"

    @classmethod
    def show_bank(cls):
        print(cls.bank)

Bank.show_bank()

# @classmethod tells Python this is a class method.
# cls refers to the class itself (just like self refers to an object).
