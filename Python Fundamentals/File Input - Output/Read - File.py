# Read the entire file

# f = open("Python Fundamentals\File Input - Output\demo.txt", "r")
# or
f = open(r"Python Fundamentals\File Input - Output\demo.txt", "rt")

data = f.read()
print("Entire file content:")
print(data)
print("Data type:", type(data))

f.close()

# OR (Better Way)
# Use a raw string (r"...") to avoid escape sequence issues in file paths.
# Also, use the 'with' statement so the file is closed automatically.
with open(r"Python Fundamentals\File Input - Output\demo.txt", "rt") as f:
    data = f.read()
    print("\nEntire file content using 'with':")
    print(data)
    print("Data type:", type(data))

# Ways to Read a File

# Read specific characters
f = open(r"Python Fundamentals\File Input - Output\demo.txt", "rt")

data = f.read(5)  # Reads the first 5 characters from the file.
print("\nFirst 5 characters:")
print(data)
print("Data type:", type(data))

f.close()

# Read one line at a time
f = open(r"Python Fundamentals\File Input - Output\demo.txt", "rt")

data = f.readline()  # Reads the first line.
print("\nFirst line:")
print(data)
print("Data type:", type(data))

f.close()

# Use read() and readline() together
f = open(r"Python Fundamentals\File Input - Output\demo.txt", "rt")

data = f.read()
print("\nEntire file content:")
print(data)

line = f.readline()
print("\nOutput of readline() after read():")
print(line)  # Returns an empty string because read() has already read the entire file.

f.close()