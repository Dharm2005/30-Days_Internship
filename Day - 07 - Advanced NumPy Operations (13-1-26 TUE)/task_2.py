# Task 2: 2D Array Indexing and Slicing

import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Second row:", matrix[1])
print("First column:", matrix[:, 0])
print("Sub-matrix:\n", matrix[0:2, 1:3])
