# Loops: They are used to execute a block of code repeatedly.

There are two main kinds of loops in Python:

1. while: Runs as long as a condition is True.
   (Used when you don't know how many times to iterate)

Syntax:
while condition:
    # code block


2. for: Used when you know how many times to iterate
   or when looping through a collection.

Syntax:
for variable in sequence:
    # code block


--> range() Function: Generates a sequence of numbers.
   Commonly used with for loops.

Syntax:
for variable in range(start, stop, step):
    # code block


# There is no do-while loop in Python.
    It can be simulated using a while True loop with a break.

Syntax:
while True:
    # code block

    if condition:
        break


# Loop Control Statements

1. break: Stops the loop immediately.

Syntax:
for/while condition:
    if condition:
        break


2. continue: Skips the current iteration and moves to the next iteration.

Syntax:
for/while condition:
    if condition:
        continue


3. pass: Placeholder statement that does nothing.

Syntax:
for/while condition:
    pass


# Nested Loops: A loop inside another loop.

Syntax:
for variable1 in sequence1:
    for variable2 in sequence2:
        # code block


else with Loops:
The else block runs if the loop finishes normally
(without encountering a break statement).

Syntax:
for/while condition:
    # code block
else:
    # code block


Infinite Loop: A loop that runs forever until it is stopped manually
or terminated using a break statement.

Syntax:
while True:
    # code block


# Visual Diagram

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