# LIST IN PYTHON

# Without using a list, we need separate variables
marks1 = 10.1
marks2 = 220.2
marks3 = 130.3
marks4 = 1.4
marks5 = 20

# Using a list, we can store multiple values in a single variable
marks = [10.1, 220.2, 130.3, 1.4, 20]

# Print the complete list
print("Marks List:", marks)

# Print the data type of marks
print("Data Type:", type(marks))

# Print the number of elements in the list
print("Length of List:", len(marks))

# Accessing elements using indexing
# Index starts from 0 in Python
print("Element at index 1:", marks[1])
print("Element at index 4:", marks[4])

# Lists can store different data types together
student = ["Zaman", 20, "Indore"]

print("Student Details:", student)

# Accessing individual elements
print("Student Name:", student[0])
print("Student Age:", student[1])
print("Student City:", student[2])

# Lists are mutable (values can be changed)
student[0] = "Zamanuddin"
print("Updated Student Name:", student[0])

# Adding a new element
student.append("B.Tech")
print("After Append:", student)

# Removing an element
student.remove("Indore")
print("After Remove:", student)

# Negative indexing
print("Last Element:", student[-1])

# Slicing
print("First Two Elements:", student[:2])

# Numeric list operations
numbers = [5, 2, 8, 1]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)