from matplotlib import pyplot as plt
import numpy as np

x = np.array(np.random.rand(1, 100))
y = np.array(np.random.rand(1, 100))
sizes = np.array(np.random.rand(1, 100))*100
colors = np.array(np.random.rand(1, 100))
plt.scatter(x, y, s=sizes, c=colors)
plt.title('Scatter Plot')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
