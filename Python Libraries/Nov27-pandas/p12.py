import pandas as pd

alphabets = list('abcdefghijklmnopqrstuvwxyz')
indexes = [10, 12, 15]

sr = pd.Series(
    data=[alphabets[i] for i in indexes],   # data parameter
    index=["10th", "12th", "15th"],         # index parameter
    name="Selected Letters",                # name parameter
    copy=True                               # copy parameter
)

print(sr)
