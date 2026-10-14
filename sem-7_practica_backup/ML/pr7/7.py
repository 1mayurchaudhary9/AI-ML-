from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
y = iris.target

k_values = [1, 3, 5, 7]
accuracies = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(model, X, y, cv=10)
    accuracy = scores.mean()
    accuracies.append(accuracy)

    print("K =", k)
    print("Accuracy =", accuracy)

plt.plot(k_values, accuracies, marker="o")

plt.xlabel("Value of K")
plt.ylabel("Accuracy")
plt.title("KNN: K vs Accuracy")
plt.grid()
plt.show()