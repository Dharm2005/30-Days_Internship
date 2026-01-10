# Task 1: Clean a List Using List Comprehension

data = [10, -5, 0, 25, "NA", None, 40, -2]

cleaned_data = [x for x in data if isinstance(x, int) and x > 0]

print("Cleaned data:", cleaned_data)
