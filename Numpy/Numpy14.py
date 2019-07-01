import numpy as np

input_array1 = list(map(int, input('Enter 1d array1 : ').split()))
input_array2 = list(map(int, input('Enter 1d array2 : ').split()))
array1 = np.array(input_array1)
array2 = np.array(input_array2)
print('array1 : ', array1)
print('array2 : ', array2)

array3 = np.setxor1d(array2, array1)
print(array3)
