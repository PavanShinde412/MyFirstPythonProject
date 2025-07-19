# calculator.py

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

# Main Program
print("Simple Calculator")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Select operation: 1.Add  2.Subtract  3.Multiply  4.Divide")
choice = int(input("Enter choice (1-4): "))

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
