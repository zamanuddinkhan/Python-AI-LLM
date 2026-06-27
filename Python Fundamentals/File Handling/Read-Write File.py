# 1. Read and Write without erasing existing data

f = open(r"Python Fundamentals\File Handling\demo.txt", "r+")
f.write("Hii")      # Overwrites data from the current position
f.seek(0)           # Move the file pointer to the beginning
print(f.read())     # Read the entire file
f.close()

# 2. Erase existing data and then Read and Write

f = open(r"Python Fundamentals\File Handling\demo.txt", "w+")
f.write("Empty File")    # Writes new content after deleting old content
f.seek(0)                # Move the file pointer to the beginning
print(f.read())          # Read the new content
f.close()