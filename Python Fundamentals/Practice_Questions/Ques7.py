'''
Q7. Ask the user for a temperature in Celsius (string input).
Convert it to float, then calculate and print temperature in Fahrenheit.

Conversion formula: Fahrenheit = (Celsius * (9/5)) + 32
'''

temperature = input("Enter Temperature in Celsius: ")
Celsius = float(temperature)

Fahrenheit = (Celsius * (9/5)) + 32
print("Celsius To Fahrenheit:", Fahrenheit)