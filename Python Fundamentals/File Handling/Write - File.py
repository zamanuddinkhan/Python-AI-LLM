# To Create a file
f = open("sample.txt","w")
f.close()

# Writing to a File

# 1. Overwrite the existing file and write new content
f = open(r"Python Fujjndamentals\File Handling\demo.txt", "w")
f.write("I am Zaman")
f.close()


# 2. Append content to the end of the existing file
f = open(r"Python Fundamentals\File Handling\demo.txt", "a")
f.write("\nI belongs to Indore")
f.close()