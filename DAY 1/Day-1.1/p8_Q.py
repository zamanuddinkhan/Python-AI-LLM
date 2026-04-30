#Exchange the value of two variable without using third variable

a,b = 2,3
print("a=",a, " ,b=",b)

# using '+' and '-'

# a = a+b
# b = a-b
# a = a-b


# direct
# a,b = b,a

#Exchange the value of two variable without using third variable and + , -
# using bit wise operator : XOR

a = a^b
b = a^b
a = a^b

print("a=",a, " ,b=",b)