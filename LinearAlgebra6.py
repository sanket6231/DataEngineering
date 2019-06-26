# program to find transpose matrix of matrix Y in problem 1

import numpy as np

# Using numpy
y = np.array([5, 8, 1, 6, 7, 3, 4, 5, 9], 'i')
y.resize(3, 3)
print('Y = ', y)
print('\n')

z = y.T
print('Transpose of matrix Y ->  ', z)

# without using numpy
x = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
print(x)

for i in range(len(x)):
    for j in range(len(x[0])):
        x[i][j] = x[j][i]

print(x)
