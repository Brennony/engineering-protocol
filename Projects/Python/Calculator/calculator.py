# Brennon York  |  Calculator v1.2  |  8/5/2026

# Calculator v1.2: Created a helper script for calculating.

# This Build is finally getting somewhere!
# Eventually I want to make a GUI for this calculator, but for now this is a good start
# Improvement Ideas:
#   1. Build an Instructions Portion
#   2. Build a GUI
#   3. Implement Multi-Operation Capabilities
#   4. Make a Calculation History Feature
#   5. Release Calculus Capabilities

import math_helpers


# Defining Functions
def main():
    print("=====  PYTHON CALCULATOR V1.0  ======\n")
    while True:
        choice = getFunction()
        if choice == 1:
            operation = getOperator()
            variables = getVariables(2)
            if operation in ("/", "%"):
                variables[1] = zeroDivision(variables[1])
            doOperation(operation, variables)
        elif choice == 2:
            print("Thanks for using my calculator!")
            break

def getFunction():
    print("=====================================")
    print("Available Functions:")
    print("1. Operation")
    print("2. Quit")
    print("=====================================\n")
    while True:
        function = input("Select a function: ")
        if function in ("1", "2"):
            return int(function)
        print("Please select a valid function.")

def getOperator():
    while True:
        operation = input("Enter operation (+, -, *, /, %, **): ")
        if operation not in ('+', '-', '*', '/', '%', '**'):
            print("Please select a valid operation.")
        else:
            return operation

def getVariables(amount):
    numbers = []
    for i in range(amount):
        while True:
            try:
                number = float(input(f"Enter number {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print(f"Please enter a valid number for number {i + 1}.")
    return numbers 

def zeroDivision(number):
    while number == 0:
        try:
            number = float(input("Please enter a non-zero number for division: "))
        except ValueError:
            print("Please enter a valid number.")
    return number

def doOperation(operation, variables):
    num1 = variables[0]
    num2 = variables[1]
    if operation == "+":
        answer = math_helpers.addition(num1, num2)
    elif operation == "-":
        answer = math_helpers.subtraction(num1, num2)
    elif operation == "*":
        answer = math_helpers.multiplication(num1, num2)
    elif operation == "/":
        answer = math_helpers.division(num1, num2)
    elif operation == "%":
        answer = math_helpers.remainder(num1, num2)
    elif operation == "**":
        answer = math_helpers.power(num1, num2)
    else:
        return
    print("=====================================")
    print(f"{num1} {operation} {num2} = {answer}")
    print("=====================================\n")


# Performing Main
main()