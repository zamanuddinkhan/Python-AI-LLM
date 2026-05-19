#Variable Length Argument
def Sum(*n):
    sum = 0
    for i in n:
        sum = sum + i
    return sum

print(Sum())
print(Sum(10))
print(Sum(10,20))
print(Sum(10,20,30))
print(Sum(10,20,30,40))
print(Sum(10,20,30,40,50))
print(Sum(10,20,30,40,50,60))