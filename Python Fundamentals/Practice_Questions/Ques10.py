'''
Q10. Take a decimal number as input (like 45.78) and output its:
• Integer part - 45
• Fractional part - .78
'''

decimal = float(input("Enter Decimal Number: "))

# Print the integer part
print("Integer Part:", int(decimal))

# Calculate and print the fractional part, rounded to 2 decimal places
print("Fractional Part:", round(decimal - int(decimal), 2))