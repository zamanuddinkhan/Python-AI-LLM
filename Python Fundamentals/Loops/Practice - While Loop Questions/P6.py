# Que:6 Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

t = (1,4,9,16,25,36,49,64,81,100)
n = int(input("Enter Number: "))
i = 0

while i < 10:
    if t[i] == n:
        print("Number Exists:", t[i])
        break
    i += 1
else:
    print("Number Not Exist")