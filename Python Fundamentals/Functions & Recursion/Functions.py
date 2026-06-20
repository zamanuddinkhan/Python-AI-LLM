"""
Function: It is a block of statements that performs a specific task.
Syntax: def function_name(parameter1, parameter2):
            # Code Block
            return value

--> Way to call Function:
function_name(argument1, argument2)
"""

def greet():
    print("Good Morning")

greet()

# With Return

print("\nWith Return")
# Function Definition
def calc_total(a,b): # Parameters
    total = a + b
    print("total:",total)
    return total

n = calc_total(110,28) # Function Call; [here 110 and 28 are Arguments]
print(n)


# Without Return: If we do not return anything then python automatically returns None.

print("\nWithout Return")
def calc_total(a,b):
    total = a + b
    print("total:",total)

n = calc_total(110,28)
print(n)

"""
Flow Diagram:

                Function Call
                       │
           ┌───────────┴───────────┐
           │                       │
      With Return            Without Return
           │                       │
      return value            No return
           │                       │
       n = 138                n = None
           │                       │
     print(n) → 138         print(n) → None
"""