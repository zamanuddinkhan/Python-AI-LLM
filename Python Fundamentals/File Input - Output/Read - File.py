# Read the entire file

# f = open("Python Fundamentals\File Input - Output\demo.txt", "r")
# or
f = open("Python Fundamentals\File Input - Output\demo.txt", "rt")
data = f.read()
print(data)
print(type(data))
f.close()

# OR (Better Way)
# Use a raw string (r"...") to avoid escape sequence issues in file paths.
# Also, use the 'with' statement so the file is closed automatically.
with open(r"Python Fundamentals\File Input - Output\demo.txt", "rt") as f:
    data = f.read()
    print("\n",data)
    print(type(data))

# If i want to read specific characters
f = open(r"Python Fundamentals\File Input - Output\demo.txt", "rt")
data = f.read(5) # The read(n) method reads the first n characters from the file.
print("\n",data)
print(type(data))
f.close()