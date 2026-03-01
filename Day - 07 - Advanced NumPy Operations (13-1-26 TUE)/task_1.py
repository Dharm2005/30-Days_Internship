# Task 1: Advanced Indexing and Boolean Masking

import numpy as np

data = np.array([12, 45, 23, 67, 89, 34, 56])

filtered_data = data[data > 40]

print("Original data:", data)
print("Values greater than 40:", filtered_data)