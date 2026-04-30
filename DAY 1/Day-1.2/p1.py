def sum_sub(a,b):
    x = a+b
    y = a-b
    return x,y

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c,d = sum_sub(a,b)
print("Sum =",c)
print("Sub =",d)