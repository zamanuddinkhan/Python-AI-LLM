'''
Q1 Write a program that asks the user for their name and age, then prints a sentence like: 
Hello Zamanuddin Khan, you are 21 years old
'''

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

# Print the greeting using commas to separate the values
# print("Hello", name, "you are", age, "years old")

# Print the greeting using an f-string to insert variables directly into the sentence
print(f"Hello {name}, you are {age} years old")