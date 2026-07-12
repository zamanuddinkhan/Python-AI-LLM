"""
Encapsulation: Wrapping data (variables) and methods (functions) into a single unit (class) 
and restricting direct access to the data.

Access Modifier	    Syntax	  Meaning
Public	            name	  Accessible from anywhere
Protected	        _name	  Intended for internal use (by convention)
Private	            __name	  Name-mangled to discourage direct access

Example:
"""

class Account:
    def __init__(self):
        self.account_no = 12345      # Public
        self._owner = "Zaman"        # Protected
        self.__balance = 1000        # Private

    def deposit(self, amount):       # Public method
        self.__balance += amount

    def show_details(self):          # Public method
        print("Account Number:", self.account_no)   # Public attribute
        print("Owner:", self._owner)                # Protected attribute
        print("Balance:", self.__balance)           # Private attribute


# Create object
acc = Account()

# Accessing public attribute
print("Account Number:", acc.account_no)

# Accessing protected attribute (possible, but not recommended)
print("Owner:", acc._owner)

# Accessing private attribute directly (Not Allowed)
# print(acc.__balance)   # AttributeError

# Accessing private attribute using public methods
acc.deposit(500)
acc.show_details()