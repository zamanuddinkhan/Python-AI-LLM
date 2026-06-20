"""
For Loop: A for loop is used to iterate (repeat) over a sequence.
          Such as a list, tuple, string, range, or other iterable objects.

Use: To iterate over sequences.
     No need to manually initialize or update a counter.

Syntax
for variable in sequence:
    # Code to execute
"""

print("List of Fruits: ")
list = ["Apple", "Banana", "Orange", "Grapes", "Litchi"]
for i in list:
    print(i)

print("\nWhole Number")
for i in range(3): # 3 not Included
    print(i)

print("\nNatural Number")
for i in range(1,5): # 1 Included
    print(i)

print("\nOdd Number")
for i in range(1,10,2): # Jump by every 2 value
    print(i)

print("\nIterate Through a String")
for i in "Python":
    print(i)

# For Loop with else: The else block executes when the loop finishes normally and not use "BREAK".

print("\nUsing Else")
for i in range(5):
    print(i)
else:
    print("Loop Completed")