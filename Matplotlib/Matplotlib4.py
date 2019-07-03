from matplotlib import pyplot as plt
import pandas as pd

csv_data = pd.read_csv('Matplotlib/fdata.csv', sep=',', parse_dates=False, index_col=0)
print(csv_data)
csv_data.plot()
plt.show()
