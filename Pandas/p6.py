import pandas as pd
lt = [10,20,30,40]

# sr = pd.Series(lt, copy = False)
sr = pd.Series(lt, copy = True)
sr.iloc[0]=999
print(lt)
print(sr)