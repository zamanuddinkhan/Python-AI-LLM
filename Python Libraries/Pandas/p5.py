import pandas as pd

student = dict(name="Srishti", age=18, branch="CSE")

print(student)

sr = pd.Series(student)

print(sr)
print(type(sr))


'''A one-dimensional data structure
Like a column in Excel or a table
Stores data + index (labels)'''
