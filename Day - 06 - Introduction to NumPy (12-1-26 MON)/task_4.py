# Task 4: Indexing and Slicing in NumPy

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(f"Array : {arr}")
print(f"First Element : {arr[0]}")
print(f"Slice 1 to 4 : {arr[1:5]}")

arr[3] = 400
print(f"Modified Array : {arr}")