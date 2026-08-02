# Brennon York  |  Calculator v1.0  |  7/31/2026

# This Build is finally getting somewhere!
# Eventually I want to make a GUI for this calculator, but for now this is a good start
# Improvement Ideas:
#   1. Build an Instructions Portion
#   2. Build a GUI
#   3. Implement Multi-Operation Capabilities
#   4. Make a Calculation History Feature
#   5. Release Calculus Capabilities


# Defining Functions
def getOperator():
    while True:
        operation = input("Enter operation (+, -, *, /, %, **): ")
        if operation not in ('+', '-', '*', '/', '%', '**'):
            operation = input("Please select a valid operation (+, -, *, /, %, **): ")
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
    # Defining Variables
    again = '' 
    answer = 0
    operation = ''

    # Getting Valid Operation
    operation = getOperator()

    # Getting Valid Numbers (On a later day, we can add multi-operation functionality)
    num1, num2 = getVariables(2)

    # Division by zero?
    if operation in ('/', '%'):
        num2 = zeroDivision(num2)


    # Calculating (Eventually I want to make this process more streamlined)
    # IDEA: Initialize operations as functions once there are more complicated functions
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

    # Start Again?
    again = input("Calculate Again (y/n)?: ").lower()
    while True:
        if again not in ('y', 'n'):
            again = input("Enter Valid Answer (y/n): ").lower()
        else:
            break
    if again == 'n':
        break