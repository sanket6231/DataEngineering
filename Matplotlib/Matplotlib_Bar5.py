from matplotlib import pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
bar_colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'black']
x_pos = [i for i, _ in enumerate(x)]

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color='b')

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language")
plt.bar(x, popularity, color=bar_colors)


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%f' % float(height),
        ha='center', va='bottom')


autolabel(rects1)
plt.grid()
plt.show()
