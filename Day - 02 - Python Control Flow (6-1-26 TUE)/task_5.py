# Task 5: Count Positive, Negative, and Zero Values

numbers = [5, -3, 0, 12, -7, 0, 8]

positive = negative = zero = 0

for n in numbers:
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
