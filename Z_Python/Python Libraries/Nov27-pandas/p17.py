'''consider the series
Sunny 1000
Bunny 2000
Chinny 4500
Pinny 6000
dtype: int64
Select al values whee salary is in between 2500 to 5000'''

import pandas as pd


# s = pd.Series(data = {'Sunny' : 1000, "Bunny" : 2000, "Chinny": 4500, "Pinny": 6000}, dtype = int)
s = pd.Series( data = [1000, 2000, 4500, 6000], index = ["Sunny", "Bunny", "Chinny", "Pinny"], dtype = int)

# def  salary(s):
#     return [True if i > 2500 and i < 5000 else False for i in range(s.size)]

# print(s[salary])
# print(s)