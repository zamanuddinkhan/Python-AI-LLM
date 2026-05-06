import pandas as pd
import numpy as np

r = np.array([1,2])
ser = pd.Series(r, copy = True)
# ser = pd.Series(r, copy = False)
ser.iloc[0] = 999


print(r)
print(ser)