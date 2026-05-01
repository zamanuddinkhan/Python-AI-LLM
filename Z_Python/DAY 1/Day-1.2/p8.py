#Annonymous or lambda function

s = lambda n:n*n
print("The Square of 4 is: ",s(4))
print("The Square of 4 is: ",s(5))

s = lambda a,b:a+b
print("The Sum of 10,20 is:",s(10,20))
print("The Sum of 100,200 is:",s(100,200))

s = lambda a,b:a if a>b else b
print("The biggest of 10,20 is: ",s(10,20))
print("The biggest of 10,20 is: ",s(200,100))