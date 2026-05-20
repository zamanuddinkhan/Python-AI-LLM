'''
types of parameters

data
index
dtype
name 
copy
'''

import pandas as pd

books_dict = {
    'Book-1' : 'Pyhton',
    10 : 20,
    10.5 : 20.6,
    'Book-3' : 'DataScience'
}

sr = pd.Series(data = books_dict)

sr.iloc[0] = 999

print(sr)