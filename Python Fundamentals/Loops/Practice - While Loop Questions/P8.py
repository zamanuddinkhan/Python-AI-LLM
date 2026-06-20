# Que:8 WAP to find the sum of first n numbers.

n = int(input("Enter Number: "))
num = n  # Store original value
sum = 0

while n >= 1:
    sum = sum + n
    n = n - 1

print("Sum of", num,"number is: ", sum)