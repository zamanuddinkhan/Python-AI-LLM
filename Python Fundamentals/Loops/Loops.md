# Loops

Loops are used to execute a block of code repeatedly.

There are two main kinds of loops in Python:

## 1. while Loop

A `while` loop executes a block of code as long as a condition is `True`.

**Used when you don't know how many times to iterate.**

### Syntax

```python
while condition:
    # code block
```

### Flow of a While Loop

```text
Start
  ↓
Initialize Variable
  ↓
Check Condition
  ↓
True ? ── No ──→ Exit
  ↓ Yes
Execute Body
  ↓
Update Variable
  ↓
Back to Condition
```

---

## 2. for Loop

A `for` loop is used to iterate (repeat) over a sequence such as a list, tuple, string, range, or other iterable objects.

**Used when you know how many times to iterate or when looping through a collection.**

### Syntax

```python
for variable in sequence:
    # code block
```

### Flow of a For Loop

```text
Start
  ↓
Get Sequence
  ↓
Take First Element
  ↓
Execute Loop Body
  ↓
Next Element Available?
  ├─ Yes → Repeat Loop
  └─ No  → Exit
  ↓
End
```

---

# range() Function

The `range()` function generates a sequence of numbers.

It is commonly used with `for` loops.

### Syntax

```python
for variable in range(start, stop, step):
    # code block
```

### Examples

| Statement | Output |
|------------|---------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(1, 10, 2)` | 1, 3, 5, 7, 9 |
| `range(10, 0, -1)` | 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 |

---

# do-while Simulation

There is no `do-while` loop in Python.

It can be simulated using a `while True` loop with a `break` statement.

### Syntax

```python
while True:
    # code block

    if condition:
        break
```

---

# Loop Control Statements

## 1. break

Stops the loop immediately.

### Syntax

```python
for/while condition:
    if condition:
        break
```

---

## 2. continue

Skips the current iteration and moves to the next iteration.

### Syntax

```python
for/while condition:
    if condition:
        continue
```

---

## 3. pass

A placeholder statement that does nothing.

### Syntax

```python
for/while condition:
    pass
```

### Use of pass

Without `pass`, Python gives an error because blocks cannot be empty.

❌ Incorrect

```python
if True:
```

✅ Correct

```python
if True:
    pass
```

---

# Nested Loops

A nested loop is a loop inside another loop.

### Syntax

```python
for variable1 in sequence1:
    for variable2 in sequence2:
        # code block
```

---

# else with Loops

The `else` block runs if the loop finishes normally (without encountering a `break` statement).

### Syntax

```python
for/while condition:
    # code block
else:
    # code block
```

---

# Infinite Loop

An infinite loop runs forever until it is stopped manually or terminated using a `break` statement.

### Syntax

```python
while True:
    # code block
```

---

# Visual Diagram

```text
                +------------------+
                |      Loops       |
                +------------------+
                         |
          +--------------+--------------+
          |                             |
     +---------+                  +---------+
     |  while  |                  |   for   |
     +---------+                  +---------+
          |                             |
          |                        range()
          |
          +-----------------------------+
                        |
                 Control Statements
                        |
          +-------------+-------------+
          |             |             |
        break       continue        pass
          |
      Nested Loops
          |
      else with Loops
          |
      Infinite Loop
          |
    do-while Simulation
```