# Que: Write a program for normal, function, and recursive function to calculate the sum of first n natural numbers.

# 1. Normal Method
n = int(input("Enter Number: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum of Natural Numbers (Normal):", sum)


# 2. Using Function (Non-Recursive)
def nn(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum

n = int(input("\nEnter Number (Function): "))
print("Sum of Natural Numbers (Function):", nn(n))


# 3. Using Recursion Function
def nn_recursive(n):
    if n == 0:   # Base case
        return 0
    return n + nn_recursive(n - 1)

n = int(input("\nEnter Number (Recursion): "))
print("Sum of Natural Numbers (Recursion):", nn_recursive(n))

"""
🔁 How It Works (Call Stack)

For nn(5):

nn(5)
= 5 + nn(4)
= 5 + 4 + nn(3)
= 5 + 4 + 3 + nn(2)
= 5 + 4 + 3 + 2 + nn(1)
= 5 + 4 + 3 + 2 + 1 + nn(0)
= 15
"""