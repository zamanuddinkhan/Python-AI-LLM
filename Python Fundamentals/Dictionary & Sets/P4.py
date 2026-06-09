# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can Take Help of build-in data types)

s = {9, (9.0,)}
print(type(s))
print(s,"\n")

"""
In Python, 9 == 9.0 evaluates to True.
Since sets store only unique elements, {9, 9.0} would contain only one value.
By storing 9.0 inside a tuple, it becomes a different object/type,
allowing both values to exist separately in the set.
"""

# OR
s = {9, "9.0"}
print(type(s))
print(s,"\n")

# OR
s = {
    ("float" , 9.0),
    ("int" , 9),
}
print(type(s))
print(s)