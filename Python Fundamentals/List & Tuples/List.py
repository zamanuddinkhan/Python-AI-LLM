# LIST IN PYTHON

# Without using a list, we need separate variables
marks1 = 10.1
marks2 = 220.2
marks3 = 130.3
marks4 = 1.4
marks5 = 20

# Using a list, we can store multiple values in a single variable
marks = [10.1, 220.2, 130.3, 1.4, 20]

# Displaying a list
print("Marks List:", marks)

# Data type of a list
print("Data Type:", type(marks))

# Length of a list
print("Length of List:", len(marks))

# Accessing elements using indexing
print("Element at index 1:", marks[1])
print("Element at index 4:", marks[4])

# Heterogeneous list (different data types in one list)
student = ["Zaman", 20, "Indore"]
print("Student Details:", student)

# Accessing individual elements
print("Student Name:", student[0])
print("Student Age:", student[1])
print("Student City:", student[2])

# Mutability of list
student[0] = "Zamanuddin"
print("Updated Student Name:", student[0])

# Append method
# Adds an element at the end of the list
student.append("B.Tech")
print("After Append:", student)

# Remove method
# Removes a specified element
student.remove("Indore")
print("After Remove:", student)

# Negative indexing
print("Last Element:", student[-1])

# List slicing
# Syntax: List_Name[start:end]
# End index is not included
print("First Two Elements:", student[:2])

# Numeric list operations
numbers = [5, 2, 8, 1]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Sort method
# Sorts the list in ascending order
numbers.sort()
print("Sorted List In Asc:", numbers)

# Sorts the list in Descending order
numbers.sort(reverse = True)
print("Sorted List In Desc:", numbers)

# sort() modifies the original list and returns None
print("Return Value of sort():", numbers.sort())

# Reverse method
# Reverses the order of elements
numbers.reverse()
print("Reversed List:", numbers)

# For loop with list
print("Elements of Marks List:")
for mark in marks:
    print(mark)

# Membership operator
print("Is 20 Present?", 20 in marks)

# Insert method
# Inserts an element at a specified position
student.insert(1, "Mr.")
print("After Insert:", student)

# Pop method
# Removes and returns the last element
removed_item = student.pop()
print("Removed Item:", removed_item)
print("After Pop:", student)

# Count method
# Counts occurrences of an element
sample = [1, 2, 2, 3, 2, 4]
print("Count of 2:", sample.count(2))

# Index method
# Returns the index of an element
print("Index of 20:", student.index(20))

# Copy method
# Creates a copy of the list
new_student = student.copy()
print("Copied List:", new_student)

# Clear method
# Removes all elements from the list
temp = [10, 20, 30]
temp.clear()
print("After Clear:", temp)