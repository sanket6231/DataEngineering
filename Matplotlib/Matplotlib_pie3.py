from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('Matplotlib/medal.csv')
country_data = data["country"]
medal_data = data["gold_medal"]
bar_colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'black']

explode = [0.1, 0, 0, 0, 0]

plt.pie(medal_data, explode=explode, labels=country_data, colors=bar_colors, autopct='%1.1f%%')
plt.title('Gold Medal data')
plt.show()
