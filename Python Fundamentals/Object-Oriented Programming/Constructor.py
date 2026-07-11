"""
A constructor is a special method that is automatically called when an object is created.
It is used to initialize (assign values to) the object's attributes.

In Python, the constructor is named __init__().
"""

class Student:

    def __init__(self, fullname):
        self.name = fullname
        print("Adding new student")

s1 = Student("Karan")
print(s1.name)

s2 = Student("Arjun")
print(s2.name)

"""
Self: Self is a reference to the current object that is using the class. 
It allows each object to store and access its own data.
"""