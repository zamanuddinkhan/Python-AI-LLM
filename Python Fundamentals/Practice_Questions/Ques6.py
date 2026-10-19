# Write a program to swap values of two numbers entered by the user.

val1 = int(input("Enter First Value: "))
val2 = int(input("Enter Second Value: "))

# Method 1 - Using a third variable
swap = val1
val1 = val2
val2 = swap

print("\nMethod 1 - Using Third Variable")
print("First Value:", val1)
print("Second Value:", val2)


# Method 2 - Using addition and subtraction without a third variable
val1 = val1 + val2
val2 = val1 - val2
val1 = val1 - val2

print("\nMethod 2 - Using Addition and Subtraction")
print("First Value:", val1)
print("Second Value:", val2)

# Method 3 - Using multiplication and division without a third variable
if val1 != 0 and val2 != 0:
    val1 = val1 * val2
    val2 = val1 / val2
    val1 = val1 / val2

    print("\nMethod 3 - Using Multiplication and Division")
    print("First Value:", val1)
    print("Second Value:", val2)
else:
    print("\nMethod 3 cannot be used when either value is zero.")

# Method 4 - Using Python's tuple unpacking [BEST ONE]
val1, val2 = val2, val1

print("\nMethod 4 - Using Tuple Unpacking")
print("First Value:", val1)
print("Second Value:", val2)

# Method 5 - Using XOR
val1 = int(val1) ^ int(val2)
val2 = int(val1) ^ int(val2)
val1 = int(val1) ^ int(val2)

print("\nMethod 5 - Using XOR")
print("First Value:", val1)
print("Second Value:", val2)