import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import euclidean

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [1, 3, 5, 7, 9, 7, 5, 3, 1, 0]

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [1, 3, 5, 7, 9, 7, 5, 3, 1, 0]

print("Cosine Similarity (A, B):", cosine_similarity([A], [B])[0][0])
print("Cosine Similarity (X, Y):", cosine_similarity([X], [Y])[0][0])

print("Euclidean Distance (A, B):", euclidean(A, B))
print("Euclidean Distance (X, Y):", euclidean(X, Y))