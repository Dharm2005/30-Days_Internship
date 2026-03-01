# Task 3: Function-Based Student Result System

def calculate_total(marks):
    return sum(marks)

def get_result(total):
    if total >= 200:
        return "Distinction"
    elif total >= 150:
        return "Pass"
    else:
        return "Fail"

student_marks = [65, 72, 55, 60]
total_marks = calculate_total(student_marks)
result = get_result(total_marks)

print("Total Marks:", total_marks)
print("Result:", result)
