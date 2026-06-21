# Que:5 WAP to find the factorial of n. (n is the parameter)

n = int(input("Enter Number: "))

def fact(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
    print("Factorial of",n,"is",fac)

fact(n)