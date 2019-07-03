from matplotlib import pyplot as plt
import numpy as np

x = np.array(np.random.rand(1, 100))
y = np.array(np.random.rand(1, 100))

plt.scatter(x, y, color='red')
plt.title('Scatter Plot')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
