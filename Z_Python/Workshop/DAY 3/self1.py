class Employee:
    def __init__(self,ename,eid,loc,mob):
        self.ename=ename
        self.eid=eid
        self.mob=mob
        self.loc=loc
        
    def show(self):
        print("Employee Name= ",self.ename)
        print("Employee ID= ",self.eid)
        print("Location= ",self.loc)
        print("Mobile Number= ",self.mob)
        print()

d1=Employee("Raj",23233,9806877639,"Indore")
d2=Employee("Zaman",23233,9806877639,"Bhopal")
d3=Employee("Kunal",23233,9806877639,"Ujjain")

d1.show()
d2.show()
d3.show()

# Delete one property
# del d1.ename
# Delete the whole Object
# del d1