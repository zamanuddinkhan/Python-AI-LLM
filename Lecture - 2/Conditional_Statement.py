# IF-ELIF[ELSE-IF]-ELSE

# Greater From Two Values
a=int(input("Enter A's Value: "))
b=int(input("Enter B's Value: "))

if(a>b):
    print("A is Greater") # Indentation
    
elif(a<b):
    print("B is Greater")

else:
    print("Both are Equal")
    
# VOTE Eligibility
age=int(input("Enter Your Age: "))

if(age>=18):
    print("Can Vote")
    
else:
    print("Cannot Vote")