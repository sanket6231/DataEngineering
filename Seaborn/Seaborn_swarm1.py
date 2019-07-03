import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

# df = pd.read_csv('titanic.csv')
df = sb.load_dataset('tips')
sb.set()
sb.swarmplot(x="size", y="total_bill", data=df)
plt.show()
