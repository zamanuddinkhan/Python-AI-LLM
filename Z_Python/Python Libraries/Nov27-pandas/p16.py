# Write a program for which it selects every 7th value

import pandas as pd

s = pd.Series([i for i in range(100)])
def  seventh_selection(s):
    return [True if i % 7 == 0 else False for i in range(s.size)]

print(s[seventh_selection])
# print(s)