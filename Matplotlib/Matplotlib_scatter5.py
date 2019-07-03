from matplotlib import pyplot as plt

weights1 = [30, 60, 90, 20, 50, 30, 70, 55, 64, 96]
weights2 = [45, 32, 86, 75, 66, 19, 20, 85, 49, 73]
weights3 = [31, 86, 74, 23, 61, 58, 10, 5, 43, 9]

heights1 = [110, 50, 60, 70, 30, 111, 99, 46, 88, 64]
heights2 = [50, 111, 65, 38, 77, 49, 35, 120, 95, 100]
heights3 = [150, 64, 10, 80, 30, 62, 80, 18, 37, 46]

plt.scatter(weights1, heights1, label='Group 1', marker='*', color='red', s=10)
plt.scatter(weights2, heights2, label='Group 2', marker='*', color='blue', s=20)
plt.scatter(weights3, heights3, label='Group 3', marker='*', color='green', s=30)

plt.title('Scatter plot to show comparision between weights and heights of 3 groups')
plt.xlabel('Weights')
plt.ylabel('Heights')
plt.legend()
plt.show()
