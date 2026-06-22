"""
Recursion: Recursion is a programming technique where a function calls itself 
to solve a problem by breaking it into smaller subproblems.
"""
# Factorial
def factorial(n):
    if n == 0:      # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

n = int(input("Enter Number: "))
print("Factorial of",n, "is:",factorial(n))

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("\nEnter Number: "))
print("Fibonacci of",n, "is:",fibonacci(n))

# Sum of N Number
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

n = int(input("\nEnter Number: "))
print("Sum of",n, "Number is:",recursive_sum(n))