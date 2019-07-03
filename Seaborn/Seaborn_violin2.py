import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

# df = pd.read_csv('titanic.csv')
df = sb.load_dataset('iris')
sb.set()
sb.violinplot(x="species", y="sepal_length", data=df)
plt.show()
