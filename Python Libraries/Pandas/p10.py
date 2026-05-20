import pandas as pd

lst = [10,20,30,0,50,1,0,70]
sr = pd.Series(data = lst, dtype = bool)

print(sr)

print(type(sr))