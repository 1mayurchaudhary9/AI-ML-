import matplotlib.pyplot as plt
import numpy as np

X = [1, 3, 2, 4, 56, 4, 3, 2, 4, 5, 3, 1, 2, 3, 2, 3, 1, 4]

sd = np.std(X)
variance = np.var(X)

print("Standard Deviation:", sd)
print("Variance:", variance)

plt.hist(X, bins=6, edgecolor="black")

plt.axvline(sd, label=f"Standard Deviation = {sd:.2f}")
plt.axvline(variance, label=f"Variance = {variance:.2f}")

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.show()