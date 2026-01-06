# Conditional statement

marks = int(input("Enter marks: "))

if marks >= 75:
    grade = "Distinction"
elif marks >= 60:
    grade = "First Class"
elif marks >= 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Result:", grade)
