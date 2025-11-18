history = []

def add(x, y):
    result = x + y
    history.append(f"{x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    history.append(f"{x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    history.append(f"{x} * {y} = {result}")
    return result

def divide(x, y):
    if y == 0:
        history.append(f"{x} / {y} = Error (division by zero)")
        return "Error: Division by zero"
    result = x / y
    history.append(f"{x} / {y} = {result}")
    return result

def show_history():
    print("\nCalculation History:")
    for entry in history:
        print(entry)

def calculator():
    while True:
        print("\nOptions:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Show History\n6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '6':
            print("Goodbye!")
            break
        elif choice == '5':
            show_history()
        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please select a valid option.")

calculator()