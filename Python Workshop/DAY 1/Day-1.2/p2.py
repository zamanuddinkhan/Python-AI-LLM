#basic calculator

def calcy(a,b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return sum,sub,mul,div

    
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# sum,sub,mul,div = calcy(a,b)
# print("The results are: ")
# print("Sum =",sum)
# print("Sub =",sub)
# print("Multiply =",mul)
# print("Divide =",div)

t = calcy(a,b)
print("The results are: ")
for i in t:
    print(i)