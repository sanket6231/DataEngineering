from matplotlib import pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language")
plt.yticks(x_pos, x)
plt.barh(x, popularity, color=(0.4, 0.6, 0.9, 1.0))
plt.show()
