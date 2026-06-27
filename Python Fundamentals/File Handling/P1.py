"""
Create a new file "practice.txt" using python. Add the following data in it:
Hi everyone
I am Learning File I/O
using C
I like programming in C.

Que:1 WAF that replace all occurrences of "C" with "Python" in above file.
Search if the word "learning" exists in the file or not.
"""
f = open("Python Fundamentals\File Handling\practice.txt","a+")
data = f.write("Hi everyone\nI am Learning File I/O\nusing C\nI like programming in C.")
f.close()