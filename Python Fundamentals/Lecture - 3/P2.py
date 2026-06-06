# Write a Program to check if a List cotains a Palindrome of elements. HINT: Use Copy() Method
# A palindrome number is a number that remains the same when its digits are reversed. Ex: 121, 111, 12455421

Number = [1,2,3,2,1]
Copied_Number = Number.copy()
Copied_Number.reverse()

if Copied_Number == Number:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")


# OR By using Slicing

Number = [1,2,3,2,1]

if Number == Number[::-1]:
    print("\nPalindrome Number")
else:
    print("\nNot Palindrome Number")