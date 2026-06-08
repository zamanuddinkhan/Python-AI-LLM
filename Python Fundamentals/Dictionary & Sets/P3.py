# WAP to Enter marks of 3 subjects from the user and store them in a dictionary. Start with empty dictionary & add one by one.
# Use Subject name as key & marks as value.

marks_dictionary = {}
marks_dictionary["Maths"] = int(input("Enter Marks of Maths: "))
marks_dictionary["Science"] = int(input("Enter Marks of Science: "))
marks_dictionary["English"] = int(input("Enter Marks of English: "))

print(marks_dictionary)
print(type(marks_dictionary))

# OR

# Using Update Method

marks_dictionary = {}

marks_dictionary.update({"Maths": int(input("Enter Marks of Maths: "))})
marks_dictionary.update({"Science": int(input("Enter Marks of Science: "))})
marks_dictionary.update({"English": int(input("Enter Marks of English: "))})

print(marks_dictionary)
print(type(marks_dictionary))