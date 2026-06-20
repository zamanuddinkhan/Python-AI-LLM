# Que:3 Print Multiplication Table of the Number n.

n = int(input("Enter Number: "))
for i in range(1,11):
    t = n * i
    print(n,"*",i,"=",t)