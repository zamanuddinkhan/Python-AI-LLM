# Que:6.1 WAP convert USD to INR.

usd = int(input("Enter USD amount: "))

def usd_to_inr(usd):
    n = usd * 95
    print(usd,"USD =",n,"INR")

usd_to_inr(usd)

# Que:6.1 WAP convert INR to USD.

inr = int(input("Enter INR amount: "))

def inr_to_usd(inr):
    usd = inr / 95
    print(inr,"INR =",usd,"USD")

inr_to_usd(inr)