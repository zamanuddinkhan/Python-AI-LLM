# Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.

integer1 = int(input("Enter First Integer Number: "))
integer2 = int(input("Enter Second Integer Number: "))
float1 = float(input("Enter Float Number: "))

# Way 1 - Implicit Type Conversion
avg = (integer1 + integer2 + float1) / 3
print("Average: ", avg)

print(type(avg))
print(type(integer1))
print(type(integer2))
print(type(float1))

# Way 2 - Explicit Type Casting
i1 = float(integer1)
i2 = float(integer2)

# float1 is already a float, so no conversion is needed
avg = (i1 + i2 + float1) / 3
print("Average: ", avg)

print(type(avg))
print(type(i1))
print(type(i2))
print(type(float1))