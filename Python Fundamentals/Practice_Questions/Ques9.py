'''
Q9. Ask the user for Principal (P), Rate (R), and Time (T).
Convert all to float and calculate Simple Interest:
SI = (P * R * T) / 100
'''

# Take input from the user
Principal = input("Enter Principal: ")
Rate = input("Enter Rate: ")
Time = input("Enter Time: ")

# Convert inputs to float
P = float(Principal)
R = float(Rate)
T = float(Time)

# Print the data types
print("Principal Type:", type(P))
print("Rate Type:", type(R))
print("Time Type:", type(T))

# Calculate Simple Interest
SI = (P * R * T) / 100

# Print the Simple Interest and its data type
print("Simple Interest:", SI)
print("SI Type:", type(SI))