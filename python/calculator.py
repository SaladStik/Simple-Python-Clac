num1, num2, operators = 0, 0, ["+", "-", "*", "/"]  # ^ Initialize variables and list of valid operators
while True:
    if num1 == 0:
        # * Prompt for the first number until a valid numeric input is provided
        while not (num1 := input("Enter first number: ")).isnumeric():
            print("Invalid input")
    # * Prompt for a valid operation until one of the valid operators is provided
    while (operation := input("Enter operation(+,-,*,/): ")) not in operators:
        print("Invalid operation")
    # * Prompt for the second number until a valid numeric input is provided
    while not (num2 := input("Enter second number: ")).isnumeric():
        print("Invalid input")
    try:
        # ^ Perform the calculation using eval and update num1 with the result
        num1 = eval(f"{num1}{operation}{num2}")
        print(f"The result is: {num1}") # * Show user the result
    except ZeroDivisionError:
        # * Handle division by zero error
        print("Division by zero not allowed!")
        continue
    # * Check if the user wants to continue or exit the loop
    if input("Do you want to continue(y/n): ").lower() == "n":
        break
    # * Check if the user wants to reset the calculator
    if input("Do you want to reset the calculator(y/n): ").lower() == "y":
        num1, num2 = 0, 0  # ^ Reset the numbers