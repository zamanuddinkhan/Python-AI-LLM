"""
Que1 : Create Student class that takes name & marks of 3 subjects as arguments in constructor.
then create a method to print the average.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        average = (self.marks[0] + self.marks[1] + self.marks[2]) / 3
        print("Name:", self.name)
        print("Average:", average)
        
s = Student("Zaman",[92,90,80])
s.avg()