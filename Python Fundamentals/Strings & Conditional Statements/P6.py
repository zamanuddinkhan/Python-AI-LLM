# WAP To Check whether Given Number is Palindrome or not by using String Slicing
num = input("Enter a Number: ")

if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")