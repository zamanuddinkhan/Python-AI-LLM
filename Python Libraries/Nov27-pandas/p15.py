import pandas as pd

s = pd.Series([i for i in range(20)])
def  odd_selection(s):
    return [True if i % 2 == 1 else False for i in range(s.size)]

print(s[odd_selection])
print(s)