import matplotlib.pyplot as plt
import numpy as np
import statistics

X = [1, 3, 2, 4, 5, 6, 4, 3, 2, 4, 5, 3, 1, 2, 3, 2, 3, 1, 4]

mean = np.mean(X)
median = np.median(X)
mode = statistics.mode(X)

plt.hist(X, bins=6, edgecolor="black")

plt.axvline(mean, label="Mean")
plt.axvline(median, label="Median")
plt.axvline(mode, label="Mode")

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.show()