import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = [
    ["Sunny","Hot","High",False,"No"],
    ["Sunny","Hot","High",True,"No"],
    ["Overcast","Hot","High",False,"Yes"],
    ["Rainy","Mild","High",False,"Yes"],
    ["Rainy","Cool","Normal",False,"Yes"],
    ["Rainy","Cool","Normal",True,"No"],
    ["Overcast","Cool","Normal",True,"Yes"],
    ["Sunny","Mild","High",False,"No"],
    ["Sunny","Cool","Normal",False,"Yes"],
    ["Rainy","Mild","Normal",False,"Yes"],
    ["Sunny","Mild","Normal",True,"Yes"],
    ["Overcast","Mild","High",True,"Yes"],
    ["Overcast","Hot","Normal",False,"Yes"],
    ["Rainy","Mild","High",True,"No"]
]

df = pd.DataFrame(data,columns=["Outlook","Temp","Humidity","Windy","Play"])

X = pd.get_dummies(df.drop("Play", axis=1))
y = df["Play"]

# Random 10 training + remaining 4 testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=10, random_state=10
)

for depth in [1, 2, 3, 4]:

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=depth,
        random_state=10
    )

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print("Max Depth =", depth)
    print("Accuracy =", accuracy)
    print()