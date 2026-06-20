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