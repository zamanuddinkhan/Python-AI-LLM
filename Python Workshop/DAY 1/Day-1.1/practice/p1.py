#Complex numbers a + bj , a-> Real part and b-> Imaginary part

a = 1 + 2j
b = 3 + 4j

add = a + b
print(add)

sub = a - b
print(sub)

product = a * b #(a+bi)∗(c+di)=(ac−bd)+(ad+bc)i
print(product)

div = a / b  # a+bi/c+di = (a+bi)(c-di)/(c^2+ d^2)
print(div)

print(a)
print(type(a))
print(a.real)  # 1.0
print(a.imag)  # 2.0
print(abs(a))  # magnitude √(1^2 + 2^2) = 2.23606797749979