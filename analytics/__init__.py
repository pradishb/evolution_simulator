"Histogram"
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

plt.subplot2grid((2,2),(0,0))
x = [0, 0, 0, 1, 1.6, 1, 1, 1, 2, 2, 2.9, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 8, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11]
plt.hist(x, edgecolor='black')
plt.ylim((0, 10)) #sets y limits

plt.xlabel('Fitness Value')
plt.ylabel('Number of species')

# plot
plt.subplot2grid((2,2),(1,0))
sample_data = [11, 12, 14, 20, 5, 10, 33, 4, 15, 6, 9, 1, 2, 0, -5]
plt.xticks(np.arange(0, len(sample_data), 1), range(1, len(sample_data)+1))
plt.plot(sample_data)
plt.ylabel('Median Fitness')
plt.xlabel('Generation')

# stackedplot
plt.subplot2grid((2,2),(0,1),rowspan=2)
x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

y = np.vstack([y1, y2, y3])

labels = ["Fibonacci ", "Evens", "Odds"]

plt.stackplot(x, y1, y2, y3, labels=labels)
plt.legend(loc='upper left')

plt.show()