# MARKSHEET

Physics=int(input("Enter Physics Number: "))
Chemistry=int(input("Enter Chemistry Number: "))
Maths=int(input("Enter Maths Number: "))
English=int(input("Enter English Number: "))
Hindi=int(input("Enter Hindi Number: "))

Total = Physics + Chemistry + Maths + English + Hindi
Average = Total / 5

if(Average >= 90):
    print('Grade "A+"')
elif(Average >= 80):
    print('Grade "A"')
elif(Average >= 70):
    print('Grade "B"')
elif(Average >= 60): 
    print('Grade "C"')
elif(Average >= 50):
    print('Grade "D"')
elif(Average >= 40):
    print('Grade "E"')
else:
    print("FAIL")