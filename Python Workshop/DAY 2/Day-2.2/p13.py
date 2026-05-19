#set ->unordered collection of unique items
'''
A set is a collection of unique, unordered, and unindexed elements.  -> immutable
It automatically removes duplicates and is written using { } (curly brackets).
insertion order is not preserved unlike tuple 
no slicing
ambiguity
'''
s = {1,2,3,3,4}
print(s)
lst = [10,10,20,10,30]

print(set(lst))
