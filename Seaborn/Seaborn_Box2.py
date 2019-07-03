import pandas as pd
import io
import requests
import seaborn as sb
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

sb.set()
sb.boxplot(x="day", y="tip", data=df)
plt.show()
