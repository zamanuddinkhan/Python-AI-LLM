# Que:3 From a file containing numbers separated by comma, print the count of even numbers.

count = 0
with open("Python Fundamentals\File Handling\practice.txt","r") as f:
    data = f.read()
    print(data)
    
    n = data.split(",")
    for val in n:
        if(int(val)% 2 == 0):
            count += 1
print(count)