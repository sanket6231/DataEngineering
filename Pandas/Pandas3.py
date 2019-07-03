import pandas as pd
series1 = pd.Series([2, 4, 6, 8, 10])
series2 = pd.Series([1, 3, 5, 7, 9])

series = series1 + series2
print("Add two Series:")
print(series)

print("Subtract two Series:")
series = series1 - series2
print(series)

print("Multiply two Series:")
series = series1 * series2
print(series)

print("Divide Series1 by Series2:")
series = series1 / series2
print(series)
