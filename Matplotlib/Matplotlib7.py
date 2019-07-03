from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1, 2, 3, 4, 5]
y = [4, 5, 1, 3, 2]

x1 = [4, 5, 6, 2, 1]
y1 = [1, 5, 7, 3, 2]

x2 = [2, 6, 8, 5, 9]
y2 = [5, 3, 2, 6, 1]

plt.title('Sample plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x, y, 'g', label="line 1", linewidth=1, linestyle='dotted')
plt.plot(x1, y1, 'b', label="line 2", linewidth=3, linestyle='solid')
plt.plot(x2, y2, 'c', label="line 3", linewidth=5, linestyle='dashed')
plt.legend()
plt.show()
