# Que:6 WAP convert USD to INR or INR to USD.

def usd_to_inr():
    usd = int(input("Enter USD amount: "))
    n = usd * 95
    print(usd,"USD =",n,"INR")

def inr_to_usd():
    inr = int(input("Enter INR amount: "))
    usd = inr / 95
    print(inr,"INR =",usd,"USD")

while True:
    print("\n======== Currency Converter ========")
    print("1. USD to INR")
    print("2. INR to USD")
    print("3. Exit")

    n = int(input("Enter Choice (1-3): "))

    if n == 1:
        usd_to_inr()

    elif n == 2:
        inr_to_usd()
    
    elif n == 3:
        print("Exit successfully.")
        break

    else:
        print("Invalid choice. Try again.")