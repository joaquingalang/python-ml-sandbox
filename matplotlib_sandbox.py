import matplotlib.pyplot as plt

# Line Chart

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, color='red', linestyle='--', label='Data Line')
plt.xlabel("Alphabet")
plt.xticks([1, 2, 3, 4, 5], ['A', 'B', 'C', 'D', 'E'])
plt.ylabel("Frequency")
plt.yticks([10, 20, 30, 40], ['Low', 'Medium', 'High', 'Very High'])
plt.show()

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.scatter(x, y, color='green', s=50, marker='o')
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7]
plt.hist(data, bins=5, color='orange', alpha=0.7, edgecolor='black')
plt.show()