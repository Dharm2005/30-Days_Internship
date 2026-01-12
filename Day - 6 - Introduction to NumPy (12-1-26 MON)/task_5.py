# Task 5: Performance Comparison – Python List vs NumPy Array

import numpy as np
import time

# Python List
py_list = list(range(1000000))
start = time.time()
py_result = [x * 2 for x in py_list]
print(f"Python list time : {time.time() - start}")

# Numpy array
np_array = np.array(range(1000000))
start = time.time()
np_result = np_array * 2
print(f"Numpy array time : {time.time() - start}")