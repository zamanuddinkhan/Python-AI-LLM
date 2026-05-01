class Outer:
    def __init__(self):
        print("Outer class object creation")

    class Inner:  # Move Inner class definition to class level, not inside __init__
        def __init__(self):
            print("Inner class object creation")

        def m1(self):
            print("Inner class method m1")

            class SubInner:
                def __init__(self):
                    print("SubInner class object creation")

                def m2(self):
                    print("SubInner class method m2")

            # Create a SubInner object inside m1 if you want
            self.sub = SubInner()

# Object creation and method calls
ob = Outer()
i = ob.Inner()    # Accessing nested class
i.m1()            # Calls method m1 and creates SubInner inside it
i.sub.m2()        # Calling SubInner method