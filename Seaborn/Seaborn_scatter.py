import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

# df = pd.read_csv('titanic.csv')
df = sb.load_dataset('tips')
sb.set()
sb.scatterplot(x="day", y="total_bill", hue="sex", data=df)
plt.show()
