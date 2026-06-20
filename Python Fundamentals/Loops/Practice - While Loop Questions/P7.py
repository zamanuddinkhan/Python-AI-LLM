# 1. Using While - Continue Print Odd Numbers

i = 1
print("Odd Numbers")
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1

# 2. Using While - Continue Print Even Numbers

i = 1
print("\nEven Numbers")
while i <= 10:
    if(i % 2 != 0):
        i = i + 1
        continue
    print(i)
    i = i + 1