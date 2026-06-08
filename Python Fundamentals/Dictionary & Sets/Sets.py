# Sets: It is a well definied collection of objects i.e. Unordered items. Each elements in the set must be Unique and Immutable.

collection = {1,2,3,3,3,4,4,5,5,"Hello"} # Repeated Values Stored once
print(collection)
print(type(collection))
print(len(collection), "\n")

# Methods In Set

collection.add(10)
print("After Add: ", collection)

collection.remove(10)
print("After Remove: ", collection)

collection.pop() # Removes a random element
print("After Pop: " ,collection)

copy = collection.copy() # Copy() creates a shallow copy of the original one
print("After Copy: " ,copy)
copy.clear()
print(copy)
print(collection, "\n")

a = {1,2,3}
b = {3,4,5,6}

print("Union:", a.union(b)) # All unique elements

print("Intersection:", a.intersection(b)) # Common elements

print("Difference:", a.difference(b)) # Elements in A but not in B

a.update(b) # Adds B's elements into A
print("After Update: " ,a)

# Way to define Empty Set
empty_collection = set()
print("\n", empty_collection)
print(type(empty_collection))