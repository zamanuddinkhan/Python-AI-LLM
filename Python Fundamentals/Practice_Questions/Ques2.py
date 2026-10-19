# Q2. Take two numbers and print their sum, difference, product, and quotient.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

total = num1 + num2
print("\nSum of Two Numbers: ", total)

difference = num1 - num2
print("Difference of Two Numbers: ", difference)

product = num1 * num2
print("Product of Two Numbers: ", product)

if num2 != 0:
    quotient = num1 / num2
    print("Quotient of Two Numbers: ",quotient)
else:
    print("Quotient cannot be calculated because the second number is 0.")