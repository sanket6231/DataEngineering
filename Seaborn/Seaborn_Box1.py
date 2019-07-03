import pandas as pd
import io
import requests
import seaborn as sb
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

sb.set()
sb.boxplot(x="continent", y="lifeExp", data=df)
plt.show()
