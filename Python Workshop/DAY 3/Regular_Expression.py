#Regular Expression for Mobile number
import re
n = input("Enter Mobile Number: ")
m=re.match("[7-9][0-9]{9}",n)
#[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
#[7-9]\d{9}
if m!=None:
    print("Valid Mobile Number")
    
else:
    print("Invalid Mobile Number")