import numpy as np

array = np.ones(9)
array = array.reshape(3, 3)
array = np.insert(array, 0, 0, 1)
array = np.insert(array, 0, 0, 0)
array = np.insert(array, len(array), 0, 1)
array = np.insert(array, len(array), 0, 0)
print(array)
