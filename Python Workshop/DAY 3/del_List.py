import time
class Test:
    def __init__(self):
        print("Constructor Execution")
    def __del__(self):
        print("Destructor Execution")
        
list=[Test(), Test(), Test()]
del list
time.sleep(5)
print("End of Application")