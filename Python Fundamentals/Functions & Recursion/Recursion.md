# What is Recursion in Python?

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it into smaller subproblems.

A recursive function typically has:

1. **Base Case** – Stops the recursion.
2. **Recursive Case** – Calls itself with a smaller or simpler input.

---

## Advantages of Recursion

✅ Makes code shorter and easier to understand for problems like:

* Tree Traversal
* Graph Algorithms
* Divide-and-Conquer Algorithms
* Backtracking (N-Queens, Sudoku, etc.)

---

## Disadvantages of Recursion

❌ Uses more memory due to the function call stack.

❌ Can cause a `RecursionError` if the recursion depth becomes too large.

```python
def infinite():
    return infinite()

infinite()  # RecursionError
```
---

## Conclusion

Recursion is a powerful programming technique where a function solves a problem by calling itself. It is particularly useful for problems that can be divided into smaller, similar subproblems. Every recursive function must have a base case to prevent infinite recursion.