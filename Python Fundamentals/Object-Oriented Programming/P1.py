"""
Que1 : Create Student class that takes name & marks of 3 subjects as arguments in constructor.
then create a method to print the average.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        average = sum(self.marks) / len(self.marks)
        print("Name:", self.name)
        print("Average:", average)
        
s = Student("Zaman",[92,90,80])
s.avg()

# We can change attribute value as well
s.name = "Zamanuddin"
s.avg()