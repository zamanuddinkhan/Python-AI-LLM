"""
Class Attribute:
A class attribute is a variable that belongs to the class and is shared by all objects of that class.

Syntax:
"""
class ClassName:
    class_attribute = "value"

"""
Instance Attribute: An instance attribute is a variable that belongs to an object.
Each object has its own copy of the attribute.

Syntax:
"""
class ClassName:
    def __init__(self, parameter):
        self.instance_attribute = parameter

# Priority: Instance Attribute > Class Attribute

# Example:
class Student:
    college_name = "ABC College"
    name = "anonymous"      # Class attribute

    def __init__(self, name, marks):
        self.name = name    # Instance attribute > Class attribute
        self.marks = marks
        print("Adding new student in Database...")

s1 = Student("Karan", 97)
print(s1.name)