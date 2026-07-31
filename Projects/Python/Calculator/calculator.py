# Brennon York  |  Calculator Alpha Prototype  |  7/31/2026

while True:
    again = 'y' 
    # Variables
    operation = input("Enter operation (+, -, *, /, %): ")
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    answer = 0

    # Getting Valid Operation
    while True:
        if operation not in ('+', '-', '*', '/', '%'):
            operation = input("Please select a valid operation (+, -, *, /, %): ")
        else:
            break

        # Getting Valid Numbers
        # IDK HOW TO DO THIS YET

    # Getting Valid Denominator
    if operation in ('/', '%'):
        while True:
            if num2 == 0:
                num2 = float(input("Enter a non-zero number for the denominator: "))
            else:
                break

    # Calculating
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2 
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        answer = num1 / num2
    else:
        answer = num1 % num2

    # Print Results
    print(f"{num1} {operation} {num2} = {answer}")
    print("")

    # Start Again?
    again = input("Calculate Again (y/n)?: ").lower()
    while True:
        if again not in ('y', 'n'):
            again = input("Enter Valid Answer (y/n): ")
        else:
            break
    if again == 'n':
        break