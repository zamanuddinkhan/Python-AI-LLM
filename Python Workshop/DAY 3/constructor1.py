class Test:
    def __init__(self,*a):
        sm=0
        for i in a:
            sm=sm+i
        print("Sum=",sm)
            
t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)
t5=Test(10,20,30,40)
t6=Test(10,20,30,40,50)