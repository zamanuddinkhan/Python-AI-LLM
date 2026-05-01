import pandas as pd
import numpy as np

s1 = pd.Series(data = [10,20,30,40,60], index = ['A', 'B', 'C', 'D', 'E'])
s2 = pd.Series(data = [10,20,30,40,50], index = ['C', 'D', 'E', 'F', 'G'])

print(s1.sub(s2))
print(s1.sub(s2, fill_value=0))
print(s1.mul(s2))
print(s1.mul(s2, fill_value=0))
print(s1.div(s2))
print(s1.div(s2, fill_value=0))