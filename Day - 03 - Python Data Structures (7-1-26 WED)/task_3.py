# Task 3: Student Marks Analysis Using Dictionary

students = {
    "Dharm": 78,
    "Azim": 34,
    "Vedant": 56,
    "Ronak": 89,
    "Dharmit": 42
}

for name, marks in students.items():
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"
    print(name, ":", marks, "-", result)
