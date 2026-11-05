# Python Exception Handling

## 📌 Introduction

Exception Handling in Python is a mechanism used to handle runtime errors so that a program does not terminate unexpectedly.

It allows developers to detect errors and handle them properly using specific keywords such as `try`, `except`, `else`, and `finally`.

**Example:** If a user enters a string instead of a number while performing division, Python raises a `ValueError`. Exception handling allows us to manage this situation without crashing the program.

---

## 🎯 Why Exception Handling?

Exception handling is important because it:

- Prevents unexpected program termination.
- Helps manage runtime errors.
- Makes programs more reliable and stable.
- Provides meaningful error messages.
- Separates error-handling code from normal program logic.
- Improves user experience.

---

## 🧠 Types of Errors in Python

Python errors can generally be classified into three categories:

### 1. Syntax Errors

Syntax errors occur when Python rules or syntax are not followed.

```python
print("Hello World"
```

**Output:**
```text
SyntaxError: '(' was never closed
```

### 2. Runtime Errors

Runtime errors occur while the program is executing.

```python
a = 10
b = 0

print(a / b)
```

**Output:**
```text
ZeroDivisionError: division by zero
```

### 3. Logical Errors

Logical errors occur when a program executes successfully but produces an incorrect result due to incorrect logic.

```python
length = 10
width = 5

area = length + width  # Incorrect logic
print(area)
```

**Output:**
```text
15
```

The correct formula for area is `length * width`.

---

## 🔑 Keywords Used in Exception Handling

Python provides five important keywords for exception handling.

| Keyword | Description |
|---|---|
| `try` | Contains code that may generate an exception. |
| `except` | Handles the exception if it occurs. |
| `else` | Executes when no exception occurs in the try block. |
| `finally` | Executes whether an exception occurs or not. |
| `raise` | Manually generates an exception. |

---

## 1. try Block

The `try` block contains code that might generate an exception.

```python
try:
    result = 10 / 2
    print(result)
```

The code inside the try block is monitored for exceptions.

## 2. except Block

The `except` block handles exceptions raised inside the try block.

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

**Output:**
```text
Cannot divide by zero.
```

## 3. else Block

The `else` block executes only when no exception occurs in the try block.

```python
try:
    num = 10 / 2

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", num)
```

**Output:**
```text
Result: 5.0
```

## 4. finally Block

The `finally` block always executes, regardless of whether an exception occurs.

It is commonly used for cleanup operations, such as closing files or releasing resources.

```python
try:
    print("Program is running.")

except Exception:
    print("An error occurred.")

finally:
    print("Execution completed.")
```

**Output:**
```text
Program is running.
Execution completed.
```

## 5. raise Keyword

The `raise` keyword is used to manually generate an exception.

```python
age = 15

if age < 18:
    raise ValueError("You must be 18 or older.")

print("Access granted.")
```

**Output:**
```text
ValueError: You must be 18 or older.
```

---

## 🔄 Complete Exception Handling Structure

```python
try:
    # Code that may generate an exception

except ExceptionType:
    # Handle the exception

else:
    # Execute if no exception occurs

finally:
    # Always execute
```

**Note:** The `else` and `finally` blocks are optional.

---

## 📚 Common Built-in Exceptions in Python

Python provides several built-in exceptions.

| Exception | Description |
|---|---|
| `ZeroDivisionError` | Raised when dividing a number by zero. |
| `ValueError` | Raised when a value has an inappropriate type or format for an operation. |
| `TypeError` | Raised when an operation is applied to an incompatible type. |
| `NameError` | Raised when a variable is not defined. |
| `IndexError` | Raised when a sequence index is out of range. |
| `KeyError` | Raised when a dictionary key does not exist. |
| `FileNotFoundError` | Raised when a requested file does not exist. |
| `AttributeError` | Raised when an object does not have the requested attribute. |
| `ImportError` | Raised when an import cannot be completed. |
| `ModuleNotFoundError` | Raised when the requested module cannot be found. |
| `IndentationError` | Raised when indentation is incorrect. |
| `OverflowError` | Raised when a numerical operation exceeds the allowed range. |
| `RuntimeError` | Raised when an error does not fit another category. |
| `MemoryError` | Raised when an operation runs out of memory. |

---

## 💻 Practical Examples

### Example 1: Handling ZeroDivisionError

```python
try:
    a = 10
    b = 0

    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
```

### Example 2: Handling ValueError

```python
try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Error: Please enter a valid integer.")
```

### Example 3: Handling Multiple Exceptions

```python
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
```

### Example 4: Using Multiple Exceptions in One Block

```python
try:
    num = int("Hello")

except (ValueError, TypeError):
    print("An invalid value or type was provided.")
```

### Example 5: Using finally

```python
try:
    file = open("example.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File does not exist.")

finally:
    print("File operation completed.")
```

### Example 6: Custom Exception

Python allows developers to create their own exceptions using classes.

```python
class InvalidAgeError(Exception):
    pass


age = 15

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Eligible")

except InvalidAgeError as e:
    print("Error:", e)
```

**Output:**
```text
Error: Age must be 18 or above.
```

---

## 🏗️ Exception Hierarchy in Python

Python exceptions follow a hierarchical structure.

```text
BaseException
    |
    |-- SystemExit
    |-- KeyboardInterrupt
    |-- GeneratorExit
    |
    |-- Exception
          |
          |-- ArithmeticError
          |     |-- ZeroDivisionError
          |     |-- OverflowError
          |
          |-- LookupError
          |     |-- IndexError
          |     |-- KeyError
          |
          |-- ValueError
          |-- TypeError
          |-- NameError
          |-- RuntimeError
          |-- OSError
                |-- FileNotFoundError
```

**Note:** This is a simplified hierarchy showing some common exceptions, not the complete Python exception hierarchy.

---

## ⭐ Best Practices

Follow these practices when writing exception-handling code:

1. Use specific exceptions instead of catching every exception.
2. Avoid using empty `except` blocks.
3. Keep the `try` block as small as possible.
4. Provide meaningful error messages.
5. Use `finally` for cleanup operations when necessary.
6. Use custom exceptions when application-specific errors need to be represented.
7. Avoid using exceptions for normal program flow.
8. Use `with` statements for managing files and other supported resources.
9. Do not silently ignore exceptions.
10. Log unexpected errors when developing larger applications.

### Good Practice

```python
try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid integer.")
```

### Bad Practice

```python
try:
    num = int(input("Enter a number: "))

except:
    pass
```

The bad example hides errors and makes debugging difficult.

---

## 🔗 References

- [Python Official Documentation – Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Official Documentation – Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

---