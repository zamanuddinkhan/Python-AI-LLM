# Que:3 Print the Multiplication Table of a number n.

n = int(input("Enter Number: "))
i = 1
while i <= 10:
    t = n * i
    print(n, "x", i, "=", t)
    i = i + 1