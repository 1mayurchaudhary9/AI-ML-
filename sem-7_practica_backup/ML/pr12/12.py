import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import tensorflow as tf

# NumPy
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)
print("Mean:", np.mean(arr))

# Pandas
data = pd.DataFrame({
    "Age": [20, 21, 22, 23, 24],
    "Marks": [65, 70, 75, 80, 85]
})
print("\nPandas DataFrame:")
print(data)

# Scikit-learn
X = data[["Age"]]
y = data["Marks"]

model = LinearRegression()
model.fit(X, y)

print("\nScikit-learn Prediction:", model.predict([[25]])[0])

# TensorFlow
tensor = tf.constant([1, 2, 3, 4, 5])
print("\nTensorFlow Tensor:", tensor)
print("TensorFlow Mean:", tf.reduce_mean(tensor).numpy())