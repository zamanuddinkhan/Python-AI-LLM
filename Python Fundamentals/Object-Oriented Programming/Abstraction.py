# Abstraction: Hiding the implementation details and showing only the essential functionality to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        # Internal implementation is hidden from the user.
        self.clutch = True
        self.acc = True
        print("Car Starting.....")

c = Car()
c.start()
