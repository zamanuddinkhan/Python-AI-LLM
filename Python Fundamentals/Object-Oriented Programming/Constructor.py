"""
A constructor is a special method that is automatically called when an object is created.
It is used to initialize (assign values to) the object's attributes.

In Python, the constructor is named __init__().
"""

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student")

s1 = Student("Karan",81)
print(s1.name, s1.marks)

s2 = Student("Arjun",72)
print(s2.name,s1.marks)

"""
Self: Self is a reference to the current object that is using the class. 
It allows each object to store and access its own data.
"""