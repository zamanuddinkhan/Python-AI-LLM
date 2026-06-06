# WAP To Check Greater among From Three Values

x=int(input("Enter X's Value: "))
y=int(input("Enter Y's Value: "))
z=int(input("Enter Z's Value: "))

if(x>=y and x>=z):
    print("X is Greatest")
    
elif(y>=x and y>=z):
    print("Y is Greatest")
    
else:
    print("Z is Greatest")