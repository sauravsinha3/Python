def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (ADD/SUB/MUL/DIV): ")

    if choice in ('ADD', 'SUB', 'MUL', 'DIV'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'ADD':
            print("Result:", add(num1, num2))
        elif choice == 'SUB':
            print("Result:", subtract(num1, num2))
        elif choice == 'MUL':
            print("Result:", multiply(num1, num2))
        elif choice == 'DIV':
            print("Result:", divide(num1, num2))
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")
