"""
for variable in iterable:
    # code to execute

variable → takes each value from the iterable one by one
iterable → something you can loop over (like a list, string, range)
Indented code block runs for each value
"""
#Looping over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    print(fruit, end=" ")

#Looping over a range(start, stop, step)
for i in range(1,10,2):
    print(i)