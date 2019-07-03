from matplotlib import pyplot as plt

x = list()
y = list()
with open('Matplotlib/test.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        x.append(int(line.split(' ')[0]))
        y.append(int(line.split(' ')[1]))

print(x)
print(y)
plt.title('Sample plot from text')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.plot(x, y)
plt.show()
