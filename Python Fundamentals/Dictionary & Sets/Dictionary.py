"""
Dictionary: A built-in data type used to store data in KEY : VALUE pairs.

Properties:
1. Ordered (Python 3.7+)
2. Mutable (Changeable)
3. Keys must be unique
4. Duplicate values are allowed
5. Dictionary keys must be Immutable.
6. Therefore, List, Set, and Dictionary cannot be used as keys.
"""

student = {
    "Name": "Zaman Khan",
    "Name": "Zamanuddin Khan", # Since the key "Name" appears twice, Python keeps only the last occurrence.
    "Age": 20,
    "Pi": 3.14,
    "Fruits": ["Apple", "Mango", "Banana"],
    "Numbers": (1, 2, 3, 4, 5),
    "Location": {"Indore", "Madhya Pradesh"},
    "Is_Indore": True, 
    True: "Yes", # Python considers True and 1 equal as dictionary keys
    1: "One", # # "Yes" is overwritten by "One"
    55: "Integer",
    3.14: "Float",
    "name": "String",
    (1, 2): "Tuple"
}

print(type(student))
print(student)

# To Access Individually
print(student["Name"])

# Convert Dictionary to List
print("\nFirst Item:", list(student.items())[0])

# Invalid keys: Because lists, sets, and dictionaries are mutable, Python does not allow them as dictionary keys.
# d = {
#     [1, 2]: "List",      # Error
#     {1, 2}: "Set",       # Error
#     {"a": 1}: "Dict"     # Error
# }

# We can change Values in Dictionary. Thus Previous value is overwrittern by New one.
student["Pi"] = 3
print("After Change Pi value is ", student["Pi"])