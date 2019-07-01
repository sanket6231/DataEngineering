import numpy as np

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
array = np.array(list1)
print('List to array : ', array)

tuple1 = (8, 4, 6, 1, 2, 3)
array2 = np.array(tuple1)
array2 = array2.reshape(2, 3)
print('Tuple to array : ', array2)
