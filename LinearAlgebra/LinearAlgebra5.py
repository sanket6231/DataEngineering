import numpy as np

x = np.array([12, 7, 3, 4, 5, 6, 7, 8, 9], 'i')
x.resize(3, 3)
print('X = ', x)
print('\n')

inv_x = np.linalg.inv(x)
print('Inverse of matrix X is -> ', '\n', inv_x)
