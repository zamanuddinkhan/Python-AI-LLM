"""
Q4. The user enters a string containing a number (e.g., "45"). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.
"""

num = input("Enter Number: ")
print(num, type(num))


integer = int(num)
print(integer, type(integer))

float1 = float(integer)
print(float1, type(float1))

string = str(float1)
print(string, type(string))