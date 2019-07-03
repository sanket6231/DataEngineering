import pandas as pd

series = pd.Series([10, 20, 30, 40, 50])
print('Series : ', series)
print('Series converted to list : ')
print(series.tolist())
print(type(series.tolist()))
