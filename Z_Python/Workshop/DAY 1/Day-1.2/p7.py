a = 10 #Global Variable

def f1():
    global a # inside a function global function is declared using "global" keyword
    a =777
    print(a)

def f2():
    print(a)

f1()
f2()