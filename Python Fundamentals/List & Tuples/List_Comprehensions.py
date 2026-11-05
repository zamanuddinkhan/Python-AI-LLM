
'''
LIST COMPREHENSIONS

List Comprehension is a short and simple way to create a new list from an existing iterable
(like a list, tuple, string, or range).

Instead of writing multiple lines using a for loop, we can create a list in just one line.

Syntax: [output for item in iterable if condition]
'''

# Example 1: Create a List of Numbers (1 to 5)

numbers = [i for i in range(1, 6)]
print(numbers)


# Example 2: Create a List of Even Numbers (1 to 10)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)


# Example 3: Create a List of Squares of Numbers (1 to 5)

squares = [x**2 for x in range(1, 6)]
print(squares)


# Example 4: Filter Names Starting with 'A'

names = ["Aman", "Rahul", "Ankit", "Rohit"]
result = [name for name in names if name.startswith("A")]
print(result)


# Example 5: Convert All Words into Uppercase

words = ["python", "java", "html"]
result = [word.upper() for word in words]
print(result)


# Example 6: Filter Numbers Greater Than 5

numbers = [2, 5, 8, 10, 3, 12]
result = [x for x in numbers if x > 5]
print(result)


# Example 7: Create a List of Odd Numbers (1 to 10)

odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(odd_numbers)


# Example 8: Create a List of Cubes of Numbers (1 to 5)

cubes = [x**3 for x in range(1, 6)]
print(cubes)


# Example 9: List Comprehension with if-else Condition

numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(result)


# Example 10: List Comprehension with Multiple Conditions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in numbers if x > 3 and x < 9]
print(result)


# Example 11: Nested List Comprehension (Flatten a Nested List)

nested_list = [[1, 2], [3, 4], [5, 6]]
result = [x for row in nested_list for x in row]
print(result)


# Example 12: Extract Words Having More Than 4 Characters

words = ["Python", "Java", "HTML", "Programming", "CSS"]
result = [word for word in words if len(word) > 4]
print(result)