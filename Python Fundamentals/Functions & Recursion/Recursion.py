"""
Recursion: Recursion is a programming technique where a function calls itself 
to solve a problem by breaking it into smaller subproblems.
"""

def factorial(n):
    if n == 0:      # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)

print(recursive_sum(5))