# Task 3: Read and Display CSV Data Using Python

import csv

try:
    with open("./CSV_Files/data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found.")
