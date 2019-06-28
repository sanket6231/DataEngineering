# program to multiply matrices in problem 1

import numpy as np

x = np.array([12, 7, 3, 4, 5, 6, 7, 8, 9], 'i')
x.resize(3, 3)
print('X = ', x)
print('\n')

y = np.array([5, 8, 1, 6, 7, 3, 4, 5, 9], 'i')
y.resize(3, 3)
print('Y = ', y)
print('\n')

z = x*y
print('X * Y = ', z)
