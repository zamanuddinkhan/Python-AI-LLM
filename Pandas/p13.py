import pandas as pd

alphabets = list("abcdefghijklmnopqrstuvwxyz")

s = pd.Series(data = alphabets, index = alphabets)

s = s.add_prefix("Label_")

print(s)
print(s.get("Label_a"))
