# Functions

A function is a block of reusable code that performs a specific task.

Instead of writing the same code again and again, you can put it inside a function and call it whenever needed.

# Why Use Functions?

* Reuse code
* Reduce repetition
* Make programs easier to read and maintain
* Break large problems into smaller parts

# Syntax

```python
def function_name():
    # code block
```

## Example

```python
def greet():
    print("Hello!")

greet()
```

# Flow of a Function

```text
Start
  ↓
Define Function
  ↓
Call Function
  ↓
Execute Function Body
  ↓
Return to Caller
  ↓
End
```

# Function with Parameters

Parameters allow you to pass data into a function.

```python
def greet(name):
    print("Hello", name)

greet("Zaman")
```

**Note:** Here, `name` is a parameter.

# Function with Return Value

A function can return a result using `return`.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

# Types of Functions

| Type                   | Description                                                |
| ---------------------- | ---------------------------------------------------------- |
| Built-in Functions     | Already provided by Python (`print()`, `len()`, `input()`) |
| User-defined Functions | Created by the programmer using `def`                      |

## Built-in Function Example

```python
name = "Python"
print(len(name))
```

## User-defined Function Example

```python
def square(n):
    return n * n

print(square(5))
```

# Visual Diagram

```text
                Function
                    │
        ┌───────────┴───────────┐
        │                       │
   Built-in                User-defined
        │                       │
  print(), len()         def my_func()
        │
        └──── Parameters ──── Return Value
```

# Key Points

* Functions are defined using the `def` keyword.
* A function runs only when it is called.
* Parameters receive input values.
* `return` sends a value back to the caller.
* Functions help make code reusable and organized.

# Types of Functions in Python

There are **two main types of functions** in Python:

## 1. Built-in Functions

These functions are available by default in Python.

### Common Built-in Functions

* `print()`
* `input()`
* `len()`
* `type()`
* `abs()`
* `sum()`
* `max()`
* `min()`

---

## 2. User-defined Functions

These functions are created by the programmer using the `def` keyword.

### Example

```python
def greet():
    print("Good Morning")

greet()
```

### Example with Parameters

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

# Default Parameter in Python

A **default parameter** is a parameter that has a predefined value. If no argument is passed for that parameter when calling the function, the default value is used.

---

## Way 1: All Parameters Have Default Values

```python
def calc_prod(a=1, b=2):
    print(a * b)
    return a * b

calc_prod()
```

---

## Way 2: Mandatory Parameter Followed by a Default Parameter

```python
def calc_prod(a, b=2):
    print(a * b)
    return a * b

calc_prod(1)
```

---

## Not Possible

A non-default parameter cannot follow a default parameter.

```python
def calc_prod(a=2, b):
    print(a * b)
    return a * b

calc_prod(1)
```

---

## Correct Way

Place all mandatory parameters before default parameters.

```python
def calc_prod(b, a=2):
    print(a * b)
    return a * b

calc_prod(1)
```

---

## Rule

```python
def function_name(mandatory_parameters, default_parameter=value):
    pass
```

---

## Important Points

- Default parameters have predefined values.
- If no argument is passed, the default value is used.
- Mandatory (non-default) parameters must come before default parameters.
- A non-default parameter cannot follow a default parameter.