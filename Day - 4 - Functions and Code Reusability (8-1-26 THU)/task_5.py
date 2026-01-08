# Task 5: Menu-Driven Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(x, y))
elif choice == 2:
    print("Result:", subtract(x, y))
elif choice == 3:
    print("Result:", multiply(x, y))
elif choice == 4:
    print("Result:", divide(x, y))
else:
    print("Invalid choice")
