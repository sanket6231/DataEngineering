from matplotlib import pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
bar_colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'black']

explode = [0.1, 0, 0, 0, 0, 0]

plt.pie(popuratity, explode=explode, labels=languages, colors=bar_colors, autopct='%1.1f%%')
plt.title('Popularity of Programming Language')
plt.show()
