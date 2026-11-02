'''
Q3. Input two lists of integers from the user. Merge them into one list and sort the result.

Eg - list1 = [1, 2, 7] , list2 = [2, 4, 5]
result = [1, 2, 3, 4, 5, 7]
'''

# The split() function breaks a string into smaller parts and returns them as a list.
# The map() function applies a function to every item in an iterable, such as a list.

list1 = list(map(int, input("Enter numbers for List 1: ").split()))
list2 = list(map(int, input("Enter numbers for List 2: ").split()))
result = list1 + list2
result.sort()
print("Result =", result)
