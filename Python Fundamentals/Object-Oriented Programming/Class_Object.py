# Class → Class is a Blueprint for creating objects. Always Initialize ClassName with Capital Letter.
# Syntax: 
class ClassName:
    pass

# Object → Real thing created from the blueprint.
# Syntax: 
object_name = ClassName()

class Student:
    Course = "B.Tech"
    Branch = "CSE"

s1 = Student()
print(s1.Branch)
print(s1.Course)