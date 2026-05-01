#To Change Line using print() or "\n" 
print("Hello World")
print("Welcome to Python Programming Language")

# Single Line Comment

'''
This is Multi-Line Comment
'''
"""
Hello....!
"""
# For Multiple Line Shortcut Key CTRL + /

a=10
b=20
print("Sum is", a+b)
print() #To Change Line

#Type Casting - Manually Change one data type into another
a = "10"
c = int(a)
b = 20
print(c+b, "\n") #To Change Line ["\n"]

#Take Input From User
name = input("Enter Your Name: ")
print("Welcome" , name)
print(type(name), "\n") 

pi = input("Enter Value of Pi: ")
print("Pi" , pi)
print(type(pi), "\n") #By Default type is str always because we do not write manually

# For Specific Type of data use Type Casting
n = int(input("Enter Number: "))
print(type(n),"\n", n)

n1 = float(input("Enter Number: "))
print(type(n1),"\n", n1, "\n")

name = input("Enter Name: ")
age = int(input("Enter Age: "))
marks =float(input("Enter Marks:"))

print(type(name), type(age), type(marks))
print(name)
print(age)
print(marks)