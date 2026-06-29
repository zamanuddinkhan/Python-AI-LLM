"""
Create a new file "practice.txt" using python. Add the following data in it:
Hi everyone
I am Learning File I/O
using C
I like programming in C.
"""
f = open("Python Fundamentals\File Handling\practice.txt", "w")
f.write("Hi everyone\nI am Learning File I/O\nusing C\nI like programming in C.")
f.close()

# Que:1 WAF that replace all occurrences of "C" with "Python" in practice.txt.
f = open("Python Fundamentals\File Handling\practice.txt","r")
data = f.read()
new_data = data.replace("C","Python")
print(new_data)
f.close()

f = open("Python Fundamentals\File Handling\practice.txt","w")
f.write(new_data)
f.close()

# Search if the word "learning" exists in the file or not.
word = "Learning"
f = open("Python Fundamentals\File Handling\practice.txt","r")
data = f.read()
if(data.find(word) !=-1):
    print("Found")
else:
    print("Not Found")
f.close()