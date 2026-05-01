import pandas as pd

# Create a Series
lst = [10, 20, 30]
s = pd.Series(lst)

# Boolean mask
mask = [True, False, True]

# Correct usage:
print(s)            # full series
print(s[mask])      # boolean indexing
print(s.loc[mask])  # loc with boolean mask
print(s.iloc[mask]) # iloc with boolean mask
print(s.get(0))     # using get()
