# Brennon York  |  Calculator v1.3  |  8/19/2026

# Massive updates to Calculator Program! Version 1.3 is complete! 
# -Fully testing for available functions 
# -Added Algebra functions and Basic functions
# -Easier-to-use terminal interface 
# -Cleaner code in general

# Next up, Trignometric functions, basic Calculus capabilities, and then build Calculator v1.4 will be finished!



import math_helpers
import algebra_helpers


# Main Program

def main():
    print("=====  PYTHON CALCULATOR V1.3  ======\n")

    while True:
        choice = getFunction()

        if choice == 0:
            print("Thanks for using my calculator!")
            break

        if choice == 1:
            operation = getBasic()
            variables = getVariables(1 if operation in SINGLE_VARIABLE else 2,
                                      choice,
                                      operation)

            if not sortBasic(variables, operation):
                doBasic(operation, variables)

        elif choice == 2:
            operation = getAlgebra()

            amount = 2 if operation == "slope" else 3
            variables = getVariables(amount, choice, operation)

            if not sortAlgebra(variables, operation):
                doAlgebra(operation, variables)


# Operation Definitions

SINGLE_VARIABLE = {
    "sqrt",
    "flr",
    "ceil",
    "abs"
}
BASIC_OPERATIONS = {
    "+",
    "-",
    "*",
    "/",
    "%",
    "**",
    "log",
    "sqrt",
    "root",
    "flr",
    "ceil",
    "abs"
}
ALGEBRA_OPERATIONS = {
    "slope",
    "quad"
}


# Function Selection

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


# Basic Operations

def getBasic():
    print("=====================================")
    print("Operations:")
    print("- Add (+)")
    print("- Subtract (-)")
    print("- Multiplication (*)")
    print("- Divide (/)")
    print("- Remainder (%)")
    print("- Power (**)")
    print("- Logarithm (log)")
    print("- Square Root (sqrt)")
    print("- Nth Root (root)")
    print("- Floor (flr)")
    print("- Ceil (ceil)")
    print("- Absolute Value (abs)")
    print("=====================================\n")

    while True:
        operation = input("Select an operation: ").strip()

        if operation in BASIC_OPERATIONS:
            return operation

        print("Please select a valid operation.")


# Algebra Operations

def getAlgebra():
    print("=====================================")
    print("Operations:")
    print("- Slope (slope)")
    print("- Quadratics (quad)")
    print("=====================================\n")

    while True:
        operation = input("Select an operation: ").strip()

        if operation in ALGEBRA_OPERATIONS:
            return operation

        print("Please select a valid operation.")


# Variable Input

def getVariables(amount, choice, operation):
    numbers = []

    if choice == 1:
        for i in range(amount):
            numbers.append(
                getNumber(f"Enter number {i + 1}: ")
            )

    elif choice == 2:

        if operation == "slope":
            for i in range(amount):
                x = getNumber(f"Enter number for x{i + 1}: ")
                y = getNumber(f"Enter number for y{i + 1}: ")

                numbers.append([x, y])

        elif operation == "quad":
            for variable in ("a", "b", "c"):
                numbers.append(
                    getNumber(f"Enter number for variable {variable}: ")
                )

    return numbers


def getNumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# Basic Validation

def sortBasic(variables, operation):

    if operation in ("/", "%"):
        variables[1] = getNonZero(
            variables[1],
            "Please enter a non-zero number for division: "
        )

    elif operation == "sqrt":
        variables[0] = getNonNegative(
            variables[0],
            "Please enter a non-negative number for sqrt: "
        )

    elif operation == "log":
        variables[0] = getPositive(
            variables[0],
            "Please enter a positive number for the logarithm: "
        )

        variables[1] = getLogBase(variables[1])

    return False


def getNonZero(number, prompt):
    while number == 0:
        number = getNumber(prompt)

    return number


def getNonNegative(number, prompt):
    while number < 0:
        number = getNumber(prompt)

    return number


def getPositive(number, prompt):
    while number <= 0:
        number = getNumber(prompt)

    return number


def getLogBase(base):
    while base <= 0 or base == 1:
        base = getNumber(
            "Please enter a valid log base (> 0 and != 1): "
        )

    return base


# Algebra Validation

def sortAlgebra(variables, operation):

    if operation == "slope":
        x1 = variables[0][0]
        x2 = variables[1][0]

        if x1 == x2:
            print("=====================================")
            print("The slope is undefined.")
            print("=====================================\n")
            return True

    elif operation == "quad":
        if variables[0] == 0:
            print("=====================================")
            print("The quadratic is invalid because a cannot be 0.")
            print("=====================================\n")
            return True

    return False


# Basic Calculations

def doBasic(operation, variables):

    operations = {
        "+": math_helpers.addition,
        "-": math_helpers.subtraction,
        "*": math_helpers.multiplication,
        "/": math_helpers.division,
        "%": math_helpers.remainder,
        "**": math_helpers.power,
        "log": math_helpers.logarithm,
        "root": math_helpers.nthroot,
        "sqrt": math_helpers.sqrtRoot,
        "flr": math_helpers.flr,
        "ceil": math_helpers.ceiling,
        "abs": math_helpers.absVal
    }

    function = operations.get(operation)

    if function is None:
        return

    answer = function(*variables)

    printBasic(operation, variables, answer)


# Algebra Calculations

def doAlgebra(operation, variables):

    if operation == "slope":
        x1, y1 = variables[0]
        x2, y2 = variables[1]

        answer = algebra_helpers.slope(
            x1, y1, x2, y2
        )

        answers = [answer]

    elif operation == "quad":
        a, b, c = variables

        answer1, answer2 = algebra_helpers.quadratic(
            a, b, c
        )

        answers = [answer1, answer2]

    else:
        return

    printAlgebra(operation, variables, answers)


# Basic Output

def printBasic(operation, variables, answer):

    print("=====================================")

    if operation == "sqrt":
        print(f"sqrt value of {variables[0]} is {answer}")

    elif operation == "abs":
        print(f"Absolute value of {variables[0]} is {answer}")

    elif operation == "flr":
        print(f"{variables[0]} floored is {answer}")

    elif operation == "ceil":
        print(f"{variables[0]} ceiled is {answer}")

    elif operation == "root":
        print(
            f"The {variables[1]}th root of "
            f"{variables[0]} = {answer}"
        )

    elif operation == "log":
        print(
            f"The log base {variables[1]} "
            f"of {variables[0]} = {answer}"
        )

    else:
        print(
            f"{variables[0]} {operation} "
            f"{variables[1]} = {answer}"
        )

    print("=====================================\n")


# Algebra Output

def printAlgebra(operation, variables, answers):

    print("=====================================")

    if operation == "slope":

        x1, y1 = variables[0]
        x2, y2 = variables[1]

        print(
            f"The slope of ({x1}, {y1}) and "
            f"({x2}, {y2}) = {answers[0]}"
        )

    elif operation == "quad":

        a, b, c = variables
        answer1, answer2 = answers

        if answer1 is not None and answer2 is not None:
            print(
                f"The roots of "
                f"{a}x^2 + {b}x + {c} = 0:"
            )
            print(f"  x₁ = {answer1}")
            print(f"  x₂ = {answer2}")

        else:
            print("The quadratic has no real roots.")

    print("=====================================\n")


# Run Program

if __name__ == "__main__":
    main()