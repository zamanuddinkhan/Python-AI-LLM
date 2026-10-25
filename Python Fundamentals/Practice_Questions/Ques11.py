'''
Q11. Ask the user for a string and check whether it is a palindrome or not.
A palindrome is a string which is same when we read it forward & backward. 
Eg - "madam", "racecar" etc.

[Hint - A palindrome string is equal to the reversed version of the string. We can
use a loop to reverse the string manually. ]
'''
# Method 1:
str = input("Enter String: ")
if (str == str[::-1]):
    print("Palindrome String")
else:
    print("Not a Palindrome String")

# Method 2:
string = input("Enter String: ")
reverse = ""

for char in string:
    reverse = char + reverse

if string == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")