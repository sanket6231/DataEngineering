import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

# df = pd.read_csv('titanic.csv')
df = sb.load_dataset('titanic')
sb.set()
sb.barplot(x="sex", y="survived", hue="class", data=df)
plt.show()
