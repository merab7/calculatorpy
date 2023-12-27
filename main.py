import sys

def mult(a, b):
    return a * b

def add(a, b):
    return a + b

def sub(a, b):
    return a / b 

def min(a, b):
    return a - b

def calculate(a, b, operation):
    if operation == "*":
        return mult(a, b)
    elif operation == "+":
        return add(a, b)
    elif operation == "/":
        return sub(a, b)
    else:
        return min(a, b)

while True:
    first = input("What's the first number?: ")
    try:
        first = float(first)
    except ValueError:
        print("Please enter a valid integer value.")
        continue  # Restart the loop if input is invalid

    second = input("What's the next number?: ")
    try:
        second = float(second)
    except ValueError:
        print("Please enter a valid integer value.")
        continue  # Restart the loop if input is invalid

    operation = input("Choose an operation (+, -, *, /): ")
    if operation not in ["+", "-", "*", "/"]:
        print("Please enter a valid operator.")
        continue  # Restart the loop if input is invalid

    result = calculate(first, second, operation)
    print(f"{first} {operation} {second} = {result}")

    choice = input("Type y to continue calculating, n to start a new calculation, or x to exit: ")
    if choice.lower() == "x":
        sys.exit()
    elif choice.lower() == "n":
        continue
    elif choice.lower() == "y":
        while True:
            second = input("What's the next number?: ")
            try:
                second = int(second)
            except ValueError:
                print("Please enter a valid integer value.")
                continue

            operation = input("Choose an operation (+, -, *, /): ")
            if operation not in ["+", "-", "*", "/"]:
                print("Please enter a valid operator.")
                continue

            next_result = calculate(result, second, operation)
            print(f"{result} {operation} {second} = {next_result}")
            result = next_result

            choice = input("Type y to continue calculating, n to start a new calculation, or x to exit: ")
            if choice.lower() == "x":
                sys.exit()
            elif choice.lower() == "n":
                break  # Break out of the inner loop to start a new calculation
    else:
        print("Invalid choice. Exiting.")
        sys.exit()
