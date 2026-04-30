#Regular Expression for Mail ID
import re
s = input("Enter Mail ID: ")
m=re.match("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m!=None:
    print("Valid Mail ID")
    
else:
    print("Invalid Mail ID")