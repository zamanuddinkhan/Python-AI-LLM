str = "Zamanuddin Khan"
print(str[0:15]) # Slicing from index 0 to 14.
print(str[0:len(str)]) # Slicing from index 0 to the length of the string (entire string).
print(str[:])    # Slicing the entire string.
print(str[::])   # Slicing the entire string with default step.
print(str[:5])   # Slicing from the beginning to index 4.
print(str[5:])   # Slicing from index 5 to the end.
print(str[-5:])  # Slicing the last 5 characters.
print(str[:-5])  # Slicing from the beginning to the length of the string minus 5.
print(str[::2])  # Slicing with a step of 2 (every second character).
print(str[2::])  # Slicing from index 2 to the end with a step of 1 (default).
print(str[::-1]) # Slicing with a step of -1 (reversing the string).
print(str[-1::]) # Slicing from the last character to the end with a step of 1 (default).
print(str[1:10:2]) # Slicing from index 1 to 9 with a step of 2.
print(str[10:1:-1]) # Slicing from index 10 to 2 in reverse order.
print(str[1:5][::-1]) # Slicing from index 1 to 4 and then reversing that slice.
print(str[10:1]) # Slicing from index 10 to 2 with a step of 1 (default), but since the start index is greater than the end index, it will return an empty string.
print(str[::-2]) # Slicing with a step of -2 (every second character in reverse order).