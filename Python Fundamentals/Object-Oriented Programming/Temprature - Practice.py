# Que: Using @staticmethod write a conversion for all three Celsius, Fahrenheit and Kelvin.

"""
Conversion	Formula:
Celsius     →     Fahrenheit     F = (C * 9/5) + 32
Fahrenheit  →     Celsius	     C = (F - 32) * 5/9
Celsius     →     Kelvin	     K = C + 273.15
Kelvin      →     Celsius	     C = K - 273.15
Fahrenheit  →     Kelvin	     K = (F - 32) * 5/9 + 273.15
Kelvin      →     Fahrenheit	 F = (K - 273.15) * 9/5 + 32
"""

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return (f - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return (k - 273.15) * 9/5 + 32

print("Celsius to Fahrenheit:", Temperature.celsius_to_fahrenheit(30))
print("Fahrenheit to Celsius:", Temperature.fahrenheit_to_celsius(86))
print("Celsius to Kelvin:", Temperature.celsius_to_kelvin(30))
print("Kelvin to Celsius:", Temperature.kelvin_to_celsius(303.15))
print("Fahrenheit to Kelvin:", Temperature.fahrenheit_to_kelvin(86))
print("Kelvin to Fahrenheit:", Temperature.kelvin_to_fahrenheit(303.15))