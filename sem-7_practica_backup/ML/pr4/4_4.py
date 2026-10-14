import matplotlib.pyplot as plt
import numpy as np

A = np.array([1, 2])
B = np.array([3, 4])

# Cosine Similarity
cosine = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

# Euclidean Distance
distance = np.linalg.norm(A - B)

print("Cosine Similarity:", cosine)
print("Euclidean Distance:", distance)

# Cosine Similarity diagram
plt.figure()
plt.quiver(0, 0, A[0], A[1], angles="xy", scale_units="xy", scale=1, label="A")
plt.quiver(0, 0, B[0], B[1], angles="xy", scale_units="xy", scale=1, label="B")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cosine Similarity")
plt.grid()
plt.legend()
plt.axis("equal")
plt.show()

# Euclidean Distance diagram
plt.figure()
plt.plot([A[0], B[0]], [A[1], B[1]], marker="o")
plt.text(A[0], A[1], " A")
plt.text(B[0], B[1], " B")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Euclidean Distance")
plt.grid()
plt.axis("equal")
plt.show()