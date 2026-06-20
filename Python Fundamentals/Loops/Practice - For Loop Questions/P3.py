# Que:3 WAP to find the Factorial of first n numbers.

n = int(input("Enter Number: "))
fac = 1
for i in range(1, n + 1):
    fac = fac * i
print("Factorial of", n, "is", fac)