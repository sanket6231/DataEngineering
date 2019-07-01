import numpy as np

array = np.ones(36)
array = array.reshape(6, 6)
for i in range(1, len(array) - 1):
    for j in range(1, len(array[i]) - 1):
        array[i][j] = 0
print(array)
