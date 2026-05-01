import pandas as pd

dt = {'a' : 1000, 'b' : 2000, 'c' : 3000}

sr = pd.Series(data = dt, index = ['x','y','z'])
# sr = pd.Series(data = dt, index = ['a', 'b','c'])

print(sr)
print(type(sr))


'''If it can change → not hashable ->mutable
 If it cannot change → hashablec-> immutable'''