import pandas as pd

alphabets = list('abcdefghizklmnopqrstuvwxyz')

sr = pd.Series(
    # data = alphabets[:3],
    data = alphabets[::5],
    # data = alphabets[:3],
    # index = ['1', '2', '3']
)

print(sr)
