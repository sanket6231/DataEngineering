from matplotlib import pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
bar_colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'black']
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language")
plt.bar(x, popularity, color=bar_colors)
plt.grid()
plt.show()
