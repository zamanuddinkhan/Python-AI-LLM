'''
Q11. Evaluate and print the result of the following expression:
x = 10 + 3 * 2 ** 2

Explain the output using operator precedence.
'''

# Evaluate the expression according to operator precedence
x = 10 + 3 * 2 ** 2

print("Result:", x)

'''
Explanation:
1. Exponentiation (**) has the highest priority.
   2 ** 2 = 4

2. Multiplication (*) comes next.
   3 * 4 = 12

3. Addition (+) comes last.
   10 + 12 = 22

Therefore, the final result is 22.
'''