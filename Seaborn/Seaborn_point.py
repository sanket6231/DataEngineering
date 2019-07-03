import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

# df = pd.read_csv('titanic.csv')
df = sb.load_dataset('titanic')
sb.set()
sb.pointplot(x="sex", y="survived", hue="embark_town", data=df)
plt.show()
