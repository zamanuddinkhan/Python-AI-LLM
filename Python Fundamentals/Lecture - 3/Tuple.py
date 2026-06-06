# Tuple in Python

# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))
print("First Element:", my_tuple[0])

# Empty Tuple
empty_tuple = ()
print("\nEmpty Tuple:", empty_tuple)

# Single-Element Tuple
# A comma (,) is mandatory for a tuple with only one element.

tup1 = (1,)
tup2 = ("Zaman",)
tup3 = (2.0,)

print("\nSingle-Element Tuples:")
print(tup1, tup2, tup3)

print(type(tup1))
print(type(tup2))
print(type(tup3))

# Without Comma
# Python treats these as normal data types, not tuples.

value1 = (1)
value2 = ("Zaman")
value3 = (2.0)

print("\nWithout Comma:")
print(value1, value2, value3)

print(type(value1))   # int
print(type(value2))   # str
print(type(value3))   # float

# Multiple Elements
# Trailing comma is optional.

tuple_a = (1, 2, 3, 4,)
tuple_b = (1, 2, 3, 4)

print("\nTuple A:", tuple_a)
print("Type:", type(tuple_a))

print("\nTuple B:", tuple_b)
print("Type:", type(tuple_b))

# Tuple Slicing
print("\nSlicing Example:")
print(tuple_a[:-1])   # Returns all elements except the last one

# Tuple Immutability
# Tuples are immutable, meaning their values cannot be changed after creation.

# tuple_a[0] = 101   # Error: 'tuple' object does not support item assignment

print("\nTuples are immutable (cannot be modified).")