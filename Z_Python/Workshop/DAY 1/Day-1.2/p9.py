# Nested Functions -> declare a function inside another function

def outer():
    print("Outer function started")

    def inner():
        print("inner function execution")
    
    print("Outer function calling inner function")

    inner()

outer()