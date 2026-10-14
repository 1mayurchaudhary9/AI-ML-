from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()

X = iris.data
y = iris.target

# Overall mean
overall_mean = np.mean(X, axis=0)

# Within-class scatter
within_class_scatter = 0

for c in np.unique(y):
    Xc = X[y == c]
    class_mean = np.mean(Xc, axis=0)
    within_class_scatter += np.sum((Xc - class_mean) ** 2)

# Between-class scatter
between_class_scatter = 0

for c in np.unique(y):
    Xc = X[y == c]
    class_mean = np.mean(Xc, axis=0)
    n = len(Xc)
    between_class_scatter += n * np.sum((class_mean - overall_mean) ** 2)

# Total scatter
total_scatter = np.sum((X - overall_mean) ** 2)

print("Within Class Scatter:", within_class_scatter)
print("Between Class Scatter:", between_class_scatter)
print("Total Scatter:", total_scatter)