def demo(*args, **kwargs):
    print("args = ", args)
    print("kwargs = ", kwargs)

demo(1, 2, 3, name = "Srishti", age = "19")

'''
Sometimes we don’t know how many arguments a function will receive.
To handle unlimited inputs:

Use *args → for positional arguments

Use **kwargs → for keyword arguments'''