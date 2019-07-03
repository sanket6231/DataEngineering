from matplotlib import pyplot as plt
import numpy as np

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(marks_range, math_marks, label='Maths')
plt.scatter(marks_range, science_marks, label='Science')
plt.title('Scatter Plot for comparision between maths and science marks')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
