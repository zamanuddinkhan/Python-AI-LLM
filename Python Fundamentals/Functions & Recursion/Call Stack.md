# Call Stack in Python

## What is a Call Stack?

A **call stack** is a data structure used by Python to keep track of function calls during program execution.

Whenever a function is called:

1. A new **stack frame** is added to the top of the call stack.
2. The function executes.
3. When the function finishes, its stack frame is removed.
4. Control returns to the function below it.

---

## Example

```python
def greet():
    print("Hello")

def welcome():
    greet()

welcome()
```

### Call Stack Execution

```text
Start
  │
  ▼
welcome()
  │
  ▼
greet()
  │
  ▼
print("Hello")
  │
  ▼
greet() ends
  │
  ▼
welcome() ends
```

---

## Call Stack in Recursion

Consider the following recursive function:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(3))
```

### Call Stack Growth

```text
factorial(3)
    ↓
factorial(2)
    ↓
factorial(1)
    ↓
factorial(0)
```

At this point, the call stack looks like:

```text
Top
┌──────────────┐
│ factorial(0)│
├──────────────┤
│ factorial(1)│
├──────────────┤
│ factorial(2)│
├──────────────┤
│ factorial(3)│
└──────────────┘
Bottom
```

---