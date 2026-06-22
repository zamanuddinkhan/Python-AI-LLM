"""
A recurrence relation is an equation that defines a sequence using one or more of its previous terms.

In simple words, the current value depends on previous value(s).

General Form
T(n) = f(T(n-1), T(n-2), ..., n)

where:

T(n) is the current term.
Previous terms such as T(n-1) and T(n-2) are used to calculate it.
A base case is required to stop the recursion.
"""

# Factorial
def factorial(n):
    if (n == 0 or n == 1):
        return 1 
    return factorial(n-1) * n

n = int(input("Enter Number: "))
print("Factorial of", n, "is:", factorial(n))