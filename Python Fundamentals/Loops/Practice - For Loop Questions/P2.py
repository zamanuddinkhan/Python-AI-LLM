# Que:2 Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

tp = (1,4,9,16,25,36,49,64,81,100)
n = int(input("Enter Number: "))

for i in range(len(tp)):
    if tp[i] == n:
        print("Number Exists at idx:", i)
        break
else:
    print("Number does not exist")