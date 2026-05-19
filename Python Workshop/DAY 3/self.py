class Student:
    def __init__(self,sname,rollno,mob):
        self.sname=sname
        self.rollno=rollno
        self.mob=mob
        
    def show(self):
        print("Student Name= ",self.sname)
        print("Roll No= ",self.rollno)
        print("Mobile No= ",self.mob)

d1=Student("raj",23233,9806877639)
d2=Student("Zaman",23233,9806877639)
d3=Student("Kunal",23233,9806877639)
d1.show()
d2.show()
d3.show()