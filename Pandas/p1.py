# Series -> 1D array of data. it can hold data of any type: string, integer, float etc
# Execution of series is fast as compare to list -> useful for bulk data
# Executoion speed , process of handling data

import pandas as pd
lst = ['indore', 'pune', 'bhopal']
sr = pd.Series(lst)

print(type(sr))
print(sr)