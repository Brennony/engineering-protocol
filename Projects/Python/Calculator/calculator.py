# Brennon York  |  Calculator v1.2.1  |  8/14/2026

# Calculator v1.2.1: Updated Helper Script and Calculator Functionality.

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
        if choice == 0:
            print("Thanks for using my calculator!")
            break
        else:
            operation = getOperator()
            if operation in ("sqrt", "flr", "ceil", "abs"):
                variables = getVariables(1)
                if operation == "sqrt":
                    variables[0] = sortInput(variables[0], operation)
            else:
                variables = getVariables(2)
                if operation in ("/", "%"):
                    variables[1] = sortInput(variables[1], operation)
            doOperation(operation, variables)

def getFunction():
    print("=====================================")
    print("Available Functions:")
    print("0. Quit Program")
    print("1. Basic Operations")
    print("=====================================\n")
    while True:
        function = input("Select a function: ")
        if function in ("0", "1"):
            return int(function)
        print("Please select a valid function.")

def getOperator():
    while True:
        print("=====================================")
        print("Operations:")
        print("-Add (+)")
        print("-Subtract (-)")
        print("-Multiplication (*)")
        print("-Divide (/)")
        print("-Remainder (%)")
        print("-Power (**)")
        print("-Square Root (sqrt)")
        print("-Nth Root (root)")
        print("-Floor (flr)")
        print("-Ceil (ceil)")
        print("-Absolute Value (abs)")
        print("=====================================\n")
        operation = input("Select an operation: ").strip()
        if operation not in ('+', '-', '*', '/', '%', '**', 'sqrt', 'root', 'flr',
                             'ceil', 'abs'):
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

def sortInput(number, operation):
    if operation in ("/", "%"):
        while number == 0:
            try:
                number = float(input("Please enter a non-zero number for division: "))
            except ValueError:
                print("Please enter a valid number.")
    elif operation == "sqrt":
        while number < 0:
            try:
                number = float(input("Please enter a non-negative number for sqrt: "))
            except ValueError:
                print("Please enter a valid number.")
    return number

def doOperation(operation, variables):
    if len(variables) == 1:
        num1 = variables[0]
        if operation == "sqrt":
            answer = math_helpers.sqrtRoot(num1)
        elif operation == "flr":
            answer = math_helpers.flr(num1)
        elif operation == "ceil":
            answer = math_helpers.ceiling(num1)
        elif operation == "abs":
            answer = math_helpers.absVal(num1)
        else:
            return
        print("=====================================")
        if operation in ('flr', 'ceil'):
            print(f"{num1} {operation}'d is {answer}")
        elif operation in ('sqrt', 'abs'):
            print(f"{operation} value of {num1} is {answer}")
        else:
            return
        print("=====================================\n")
    else: 
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
        elif operation == "root":
            answer = math_helpers.nthroot(num1, num2)
        else:
            return
        print("=====================================")
        if operation in ('+', '-', '*', '/', '%', '**'):
            print(f"{num1} {operation} {num2} = {answer}")
        else:
            print(f"The {num2}th Root of {num1} = {answer}")
        print("=====================================\n")

# Performing Main
main()