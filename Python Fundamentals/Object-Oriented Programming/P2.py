"""
Que2 : Create Account class with 2 Attributes - Balance & Account Number.
Create methods for debit, credit and printing the balance.
"""

class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc_no = acc

    def debit(self, amount):
        self.bal -= amount
        print("Rs.",amount,"was debited")
        print("Total Balance: ",self.get_bal())

    def credit(self, amount):
        self.bal += amount
        print("Rs.",amount,"was creadited")
        print("Total Balance: ",self.get_bal())

    def get_bal(self):
        return self.bal

acc1 = Account(1020, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(90500)
acc1.debit(15000)