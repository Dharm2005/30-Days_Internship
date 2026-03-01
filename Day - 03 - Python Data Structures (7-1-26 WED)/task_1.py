# Task 1: Find Unique Elements and Their Frequency

numbers = [2, 4, 2, 5, 6, 4, 2, 6, 7, 5]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of elements:")
for key, value in frequency.items():
    print(key, ":", value)
