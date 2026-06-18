# While Loop: Runs as long as the condition is True.
# Used when we don't know beforehand how many times the loop will execute.

"""
--> Flow of a While Loop:
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


--> Parts of a While Loop
i = 1          # Initialization

while i <= 5:  # Condition
    print(i)   # Loop Body
    i += 1     # Updation

Part	           Purpose
Initialization	-  Starting value
Condition	    -  Decides whether loop continues
Loop Body	    -  Statements executed repeatedly
Updation	    -  Changes variable value
"""

# Infinite Loop
# while True:
#     print("Hello World")

# Specific Number of Times
count = 1  # count is a loop control variable (iterator)
while count <= 5:  # Each complete execution is called an iteration
    print("Hello World")
    count += 1

# Print "Zamanuddin Khan" from 1 to 1000
i = 1
print("\nSequence of 1 to 1000")
while i <= 1000:
    print("Zamanuddin Khan", i)
    i += 1

# Print Numbers from 1 to 5
i = 1
print("\nSequence")
while i <= 5:
    print(i)
    i += 1


# While with Else: Print Numbers from 5 to 1
i = 5
print("\nReverse")
while i >= 1:
    print(i)
    i -= 1
else:
    print("Loop Completed")

# Break and Continue In While Loop
# Break → Immediately exits the loop.

i = 1
print("Using Break")
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# Continue → Skips the current iteration and moves to the next one.

i = 0
print("Using Continue")
while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)

# Infinite Loop Example
# i = 5
# while i < 6:
#     print(i)
#     i -= 1
# print("Loop Ended")