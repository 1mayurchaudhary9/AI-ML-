from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.optimize import linear_sum_assignment
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

# 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

for k in [2, 3, 4]:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)

    model.fit(X_train)

    train_labels = model.labels_
    test_labels = model.predict(X_test)

    # Match cluster labels with actual class labels
    cost = np.zeros((k, 3), dtype=int)

    for i in range(k):
        for j in range(3):
            cost[i, j] = np.sum(
                (test_labels == i) & (y_test == j)
            )

    rows, cols = linear_sum_assignment(-cost)

    mapping = {r: c for r, c in zip(rows, cols)}
    predicted = np.array([mapping.get(label, 0) for label in test_labels])

    accuracy = accuracy_score(y_test, predicted)

    print("K =", k)
    print("Distance Measure = Euclidean")
    print("Accuracy =", accuracy)
    print()