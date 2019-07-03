from matplotlib import pyplot as plt

x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language")
plt.bar(x, popularity, color=(0.4, 0.6, 0.9, 1.0))
plt.grid()
plt.show()
