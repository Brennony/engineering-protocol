# Brennon York  |  Calculator v1.2.4  |  8/16/2026

# Calculator v1.2.4: __name__ == "__main__" functionality, added testing for helpers.

# This Build is finally getting somewhere!
# Eventually I want to make a GUI for this calculator, but for now this is a good start
# Improvement Ideas:
#   1. Build an Instructions Portion
#   2. Build a GUI
#   3. Implement Multi-Operation Capabilities
#   4. Make a Calculation History Feature
#   5. Release Calculus Capabilities

import math_helpers
import algebra_helpers

# Defining Functions
def main():
    print("=====  PYTHON CALCULATOR V1.2.1  ======\n")
    while True:
        choice = getFunction()
        if choice == 0:
            print("Thanks for using my calculator!")
            break
        elif choice == 1:
            operation = getBasic()
            if operation in ("sqrt", "flr", "ceil", "abs"):
                variables = getVariables(1, choice, operation)
                if operation == "sqrt":
                    variables[0] = sortBasic(variables[0], operation)
            else:
                variables = getVariables(2, choice, operation)
                if operation in ("/", "%"):
                    variables[1] = sortBasic(variables[1], operation)
            doOperation(operation, variables)
        elif choice == 2:
            operation = getAlgebra()
            if operation == "slope":
                variables = getVariables(2, choice, operation)
                undef = sortAlgebra(variables[0][0], variables[1][0], operation)
                if undef:
                    print("=====================================")
                    print("The slope is undefined.")
                    print("=====================================\n")
                    continue
            elif operation == "quad":
                variables = getVariables(3, choice, operation)
                undef = sortAlgebra(variables[0], None, operation)
                if undef:
                    print("=====================================")
                    print("The quadratic is invalid.")
                    print("=====================================\n")
                    continue
            doAlgebra(operation, variables)

def getFunction():
    print("=====================================")
    print("Available Functions:")
    print("0. Quit Program")
    print("1. Basic Operations")
    print("2. Algebraic Operations")
    print("=====================================\n")
    while True:
        function = input("Select a function: ")
        if function in ("0", "1", "2"):
            return int(function)
        print("Please select a valid function.")

def getBasic():
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

def getAlgebra():
    while True:
        print("=====================================")
        print("Operations:")
        print("-Slope (slope)")
        print("-Quadratics (quad)")
        print("=====================================\n")
        operation = input("Select an operation: ").strip()
        if operation not in ("slope", "quad"):
            print("Please select a valid operation.")
        else:
            return operation

def getVariables(amount, choice, operation):
    numbers = []
    if choice == 1:
        for i in range(amount):
            while True:
                try:
                    number = float(input(f"Enter number {i + 1}: "))
                    numbers.append(number)
                    break
                except ValueError:
                    print(f"Please enter a valid number for number {i + 1}.")
        return numbers 
    elif choice == 2:
        if operation == "slope":
            for i in range(amount):
                point = []
                for j in range(2):
                    while True:
                        try:
                            if j == 0:
                                number = float(input(f"Enter number for x{i+1}: "))
                            else:
                                number = float(input(f"Enter number for y{i+1}: "))
                            point.append(number)
                            break
                        except ValueError:
                            print("Please enter a valid number.")

                numbers.append(point)
            return numbers
        elif operation == "quad":
            for i in range(ord('a'), ord('c') + 1):
                while True:
                    try:
                        number = float(input(f"Enter number for variable {chr(i)}: "))
                        numbers.append(number)
                        break
                    except ValueError:
                        print("Please enter a valid number.")
            return numbers

def sortBasic(number, operation):
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

def sortAlgebra(num1, num2, operation):
    if operation == "slope":
        if num1 == num2:
            return True
        else:
            return False
    else:
        if num1 == 0:
            return True
        else:
            return False

def doOperation(operation, variables):
    print("=====================================")
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
        if operation in ('flr', 'ceil'):
            print(f"{num1} {operation}'d is {answer}")
        elif operation in ('sqrt', 'abs'):
            print(f"{operation} value of {num1} is {answer}")
        else:
            return
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
        if operation in ('+', '-', '*', '/', '%', '**'):
            print(f"{num1} {operation} {num2} = {answer}")
        else:
            print(f"The {num2}th Root of {num1} = {answer}")
    print("=====================================\n")

def doAlgebra(operation, variables):
    print("=====================================")
    if operation == "slope":
        x1 = variables[0][0]
        y1 = variables[0][1]
        x2 = variables[1][0]
        y2 = variables[1][1]
        answer = algebra_helpers.slope(x1,y1,x2,y2)
        if answer is None:
            print("The slope is undefined.")
        else:
            print(f"The slope of ({x1}, {y1}) and ({x2}, {y2}) = {answer}")
    if operation == "quad":
        a = variables[0]
        b = variables[1]
        c = variables[2]
        answer1, answer2 = algebra_helpers.quadratic(a,b,c)
        if answer1 is not None and answer2 is not None:
            print(f"The roots of {a}x^2 + {b}x + {c} = 0: ")
            print(f"  {answer1}, {answer2}  ")
        elif answer1 == "zero":
            print("Zero Division is impossible.")
        else:
            print("The quadratic is undefined.")
    print("=====================================\n")

# Performing Main
if __name__ == "__main__":
    main()