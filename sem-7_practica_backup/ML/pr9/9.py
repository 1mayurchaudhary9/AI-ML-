from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

iris = load_iris()

X = iris.data
y = iris.target

X = StandardScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=7
)

models = [
    ((3,), "sgd"),
    ((5,), "sgd"),
    ((5, 3), "sgd"),
    ((10, 5), "sgd")
]

for arch, function in models:

    model = MLPClassifier(
        hidden_layer_sizes=arch,
        solver=function,
        max_iter=1000,
        random_state=7
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Architecture:", arch)
    print("Training Function:", function)
    print("Accuracy:", accuracy)
    print()