# Task 4: Remove Duplicate Values While Preserving Order

data = [1, 3, 5, 3, 1, 6, 7, 5]

unique_data = []
seen = set()

for item in data:
    if item not in seen:
        unique_data.append(item)
        seen.add(item)

print("Original list:", data)
print("List after removing duplicates:", unique_data)
