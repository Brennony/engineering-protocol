# Brennon York  |  Calculator v1.0  |  8/5/2026

# Calculator v1.1: I abstracted more and made more appealing functions


# This Build is finally getting somewhere!
# Eventually I want to make a GUI for this calculator, but for now this is a good start
# Improvement Ideas:
#   1. Build an Instructions Portion
#   2. Build a GUI
#   3. Implement Multi-Operation Capabilities
#   4. Make a Calculation History Feature
#   5. Release Calculus Capabilities


# Defining Functions
def getFunction():
    print("=====================================")
    print("Available Functions:")
    print("1. Operation")
    print("2. Quit")
    print("=====================================\n")
    while True:
        function = input("Select a function: ")
        try:
            if function not in ("1", "2"):
                print("Please select a valid function.")
            else:
                break
        except ValueError:
            print("Please select a valid function.")
    return int(function)

def doOperation():
# Calculating (Eventually I want to make this process more streamlined)
# IDEA: Initialize operations as functions once there are more complicated functions
    # Getting Valid Operation
    operation = getOperator()

    # Getting Valid Numbers (On a later day, we can add multi-operation functionality)
    num1, num2 = getVariables(2)

    # Division by zero?
    if operation in ('/', '%'):
        num2 = zeroDivision(num2)

    # Calculation
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2 
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        answer = num1 / num2
    elif operation == '%':
        answer = num1 % num2
    else:
        answer = num1 ** num2
    # Print Results
    print(f"{num1} {operation} {num2} = {answer}")
    print("")

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
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print(f"Please enter valid a real number (1.0, 5.2, etc) for number {i + 1}: ")
    return numbers    

def zeroDivision(num2):
    while True:
        if num2 == 0:
            try:
                num2 = float(input(f"Please enter a non-zero number for division: "))
                if num2 != 0:
                    return float(num2)   
            except ValueError:
                print(f"Please enter a number for division: ")
        else:
            return float(num2)

# Full Calculator
print("=====================================")
print("=====  PYTHON CALCULATOR V1.0  ======")
print("=====================================")

while True:
    answer = getFunction()
    if answer == 1:
        doOperation()
    else:
        break 