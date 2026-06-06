"""WAP to count the Number of Students with the "A" Grade in the Tuple: ("C", "D", "A", "A","B", "B", "A") 
store this values in the list & sort them from "A" To "D"."""

Tup = ("C", "D", "A", "A", "B", "B", "A")
print("Number of Students with Grade A:", Tup.count("A"))

# Convert Tuple to List
# The list() function is used to create a list or convert other data types into a list.

ls = list(Tup)
ls.sort()
print("Sorted List:", ls)