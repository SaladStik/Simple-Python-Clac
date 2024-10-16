# This is a simple calculator that performs basic arithmetic operations
# ^ Initialize the first and second numbers to 0
num1 = 0
num2 = 0

# ^ List of valid operators
operators = ["+", "-", "*", "/"]

# ^ Start an infinite loop for the calculator
while True:
    # * If num1 is 0, prompt the user to enter the first number
    if num1 == 0:
        while True:
            num1 = input("Enter first number: ")
            if not num1.isnumeric():
                print("Invalid input")  # ^ Validate input
            else:
                num1 = int(num1)  # ^ Convert input to integer
                break

    # * Prompt the user to enter a valid operation
    while True:
        operation = input("Enter operation(+,-,*,/): ")
        if operation in operators:
            break
        else:
            print("Invalid operation")  # ^ Validate operation

    # * Prompt the user to enter the second number
    while True:
        num2 = input("Enter second number: ")
        if not num2.isnumeric():
            print("Invalid input")  # ^ Validate input
        else:
            num2 = int(num2)  # ^ Convert input to integer
            break

    # ^ Perform the operation based on the user input
    match operation:
        case "+":
            num1 = num1 + num2
        case "-":
            num1 = num1 - num2
        case "*":
            num1 = num1 * num2
        case "/":
            if num2 == 0:
                print("Division by zero is not allowed")  # ^ Handle division by zero
                continue
            num1 = num1 / num2

    # * Print the result of the operation
    print(f"The result is: {num1}")

    # * Ask the user if they want to continue
    if input("Do you want to continue(y/n): ").lower() == "n":
        break

    # * Ask the user if they want to reset the calculator
    if input("Do you want to reset the calculator(y/n): ").lower() == "y":
        num1 = 0
        num2 = 0