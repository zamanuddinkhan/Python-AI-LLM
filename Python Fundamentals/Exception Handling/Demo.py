try:
    x = float(input("Enter Numerator: "))
    y = float(input("Enter Denominator: "))
    Div = x / y

except ZeroDivisionError:
    print("You Cannot Divide a Number with 0")

except ValueError:
    print("Invalid Input! Please Enter Numeric Values.")

else:
    print(f"Division of {x} by {y} is {Div}")   

finally:
    print("---- Program Completed ----")