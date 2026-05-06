# Immutability Concept
#Immutability allows Python to reuse objects, but only for certain types and ranges.
"""Immutable objects: int, float, string, tuple, frozenset.
You cannot change their value once created.
So when you assign the same value to two variables, Python can reuse the same object in memory.

Small integer caching (interning)
Python pre-allocates small integers (usually from -5 to 256) and reuses them.
Larger integers
Python does not automatically cache large integers.

Strings (interning)
Python may also intern strings, especially short strings or identifiers.
But for long strings or dynamically created strings, separate objects may exist even if values are equal."""

a=200
b=200
# c=200
c=300
d=200

e = 200000
f = 200000
print(id(e)==id(f)) # Usually False, different objects in memory

print("A= ",a)
print("B= ",b)
print("C= ",c)
print("D= ",d)

print("E= ",e)
print("F= ",f)

print("A= ",id(a))
print("B= ",id(b))
print("C= ",id(c))
print("D= ",id(d))

print("F= ",id(f))
print("E= ",id(e))

str1 = "srishti"
str2 = "srishti"
print(id(str1)==id(str2))