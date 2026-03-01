# Task 2: Find Second Largest Element in a List

numbers = [10, 45, 23, 67, 89, 45, 67]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]
print("Second largest number:", second_largest)
