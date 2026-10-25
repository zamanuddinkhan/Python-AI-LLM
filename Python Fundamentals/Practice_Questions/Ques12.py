# Q2. Given a list of integers compute the average of all numbers in the list.

# Method 1: Without Loop

list = [1, 2, 3, 4, 5, 6]
total = list[0] + list[1] + list[2] + list[3] + list[4] + list[5]
avg = total / 6
print("Average of", list, "is", avg)

# Method 2: With Loop

numbers = [0, 1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total = total + num

avg = total / len(numbers)

print("Average of", numbers, "is", avg)

# Method 3: Using Build-in Function

numbers = [0, 1, 2]
avg = sum(numbers) / len(numbers)
print("Average of", numbers, "is", avg)