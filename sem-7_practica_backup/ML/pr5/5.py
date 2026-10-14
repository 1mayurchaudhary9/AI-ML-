import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([70, 80, 90, 100, 110, 120, 130, 140, 150, 160]).reshape(-1, 1)
Y = np.array([7, 7, 8, 9, 12, 12, 15, 14, 13, 17])

model = LinearRegression()
model.fit(X, Y)

w0 = model.intercept_
w1 = model.coef_[0]

# Predict Y for X = 210
prediction = model.predict([[210]])[0]

print("w0:", w0)
print("w1:", w1)
print("Y for X = 210:", prediction)

# Full best-fit line from 70 to 210
X_line = np.linspace(70, 210, 100).reshape(-1, 1)
Y_line = model.predict(X_line)

# Plot data points
plt.scatter(X, Y, label="Actual Data")

# Plot best-fit line
plt.plot(X_line, Y_line, label="Best Fit Line", color="red")

# Plot prediction
plt.scatter(210, prediction, label=f"Prediction (210, {prediction:.2f})")

plt.xlabel("Advertisement Amount")
plt.ylabel("Increase in Unit Sale")
plt.title("Simple Linear Regression")
plt.legend()
plt.grid()
plt.show()