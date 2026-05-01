import pandas as pd

name_lst = ['Sunny', 'Bunny', 'Chinny']

sr = pd.Series(data = name_lst, index = ['S', 'B', 'C'])

print(sr)

print(type(sr))