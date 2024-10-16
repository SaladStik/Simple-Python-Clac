num1 = 0
num2 = 0
operators = ["+", "-", "*", "/"]

while True:
    if num1 == 0:
        while True:
            num1 = input("Enter first number: ")
            if not num1.isnumeric():
                print("Invalid input")
            else:
                num1 = int(num1)
                break
    while True:
        operation = input("Enter operation(+,-,*,/): ")
        if operation in operators:
            break
        else:
            print("Invalid operation")
    while True:
            num2 = input("Enter second number: ")
            if not num2.isnumeric():
                print("Invalid input")
            else:
                num2 = int(num2)
                break
    match operation:
        case "+":
            num1 = num1 + num2
        case "-":
            num1 = num1 - num2
        case "*":
            num1 = num1 * num2
        case "/":
            if num2 == 0:
                print("Division by zero is not allowed")
                continue
            num1 = num1 / num2
    print(f"The result is: {num1}")
    if input("Do you want to continue(y/n): ").lower() == "n":
        break
    if input("Do you want to reset the calculator(y/n): ").lower() == "y":
        num1 = 0
        num2 = 0
    