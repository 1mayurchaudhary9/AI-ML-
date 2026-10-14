import numpy as np

X1 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5,1, 2, 3, 4, 2, 5, 1, 3, 2, 1,2, 1, 1, 1, 2]

X2 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5,1, 2, 3, 4, 2, 5, 1, 3, 2, 1,2, 1, 1, 1, 2000]

X3 = [1, 2, 3, 10, 20, 30,100, 200, 300, 1000, 2000, 3000]

for name, data in {"X1": X1, "X2": X2, "X3": X3}.items():
    print(name)
    print("Standard Deviation:", np.std(data))
    print("Variance:", np.var(data))