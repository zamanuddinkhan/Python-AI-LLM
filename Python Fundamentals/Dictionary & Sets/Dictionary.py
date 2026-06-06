"""
Dictionary: A built-in data type used to store data in KEY : VALUE pairs.

Properties:
1. Ordered (Python 3.7+)
2. Mutable (Changeable)
3. Keys must be unique
4. Duplicate values are allowed
5. Dictionary keys must be Immutable.
6. Therefore, List, Set, and Dictionary cannot be used as keys.
7. Values can be of any data type.
8. Keys are case-sensitive.
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

# We can change values in a dictionary. The previous value is overwritten by the new value.
student["Pi"] = 3
print("\nAfter changing Pi, the value is:", student["Pi"])

# We can also create an empty dictionary.
null_dict = {}
print("\n", type(null_dict))
null_dict["Location"] = "Bangalore"
print(null_dict)

# Nested Dictionary

nested_student = {
    "name": "Karan",
    "subjects": {
        "Maths": 88,
        "Physics": 90,
        "Chemistry": 77
    }
}

print("\n", nested_student)

# Access all subject marks
print("\nAll Subjects Marks:", nested_student["subjects"])

# Access Maths marks only
print("Maths Marks:", nested_student["subjects"]["Maths"])

# Methods in Dictionary

print("\nAll Keys:", nested_student.keys())  # Returns all keys

# By Type Casting
print("\nBy Type Casting:", list(nested_student.keys()))  # Converts keys to a list

print("\nAll Values:", nested_student.values())  # Returns all values

print("\nAll Items:", nested_student.items())  # Returns all (key, value) pairs as tuples
pairs = list(nested_student.items())
print(pairs[0]) # Access Individually

# print(student["name2"]) # Return ERROR
print("\n", nested_student.get("name2")) # Return None, Because after this if code is correct then it can run

print("\nName:", nested_student.get("name"))  # Returns the value of the specified key

nested_student.update({"City": "Indore"})  # Adds or updates key-value pairs

print("\nUpdated Dictionary:", nested_student)