# Task 4: Calculate Average from CSV Data

import csv

total = 0
count = 0

try:
    with open("./CSV_Files/numbers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                num = float(row[0])
                total += num
                count += 1
            except ValueError:
                continue
    print("Average:", total / count)
except FileNotFoundError:
    print("File not found.")
