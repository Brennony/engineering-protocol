# Brennon York  |  Calculator v1.3.2  |  8/22/2026

# 1.3.2 - Fully wired all Algebra functions and accounted for Edge-cases

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
            variables = getBasicVar(1 if operation in SINGLE_VARIABLE else 2)
            if not sortBasic(variables, operation):
                doBasic(operation, variables)

        elif choice == 2:
            operation = getAlgebra()
            variables = getAlgebraVar(operation)
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
ALGEBRA_SPECS = {
    "slope":      {"points": 2, "numbers": 0},
    "midpoint":   {"points": 2, "numbers": 0},
    "distance":   {"points": 2, "numbers": 0},
    "quad":       {"points": 0, "numbers": 3},
    "xIntercept": {"points": 0, "numbers": 2},
    "yIntercept": {"points": 1, "numbers": 1}
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
    print("- Midpoint (midpoint)")
    print("- Distance (distance)")
    print("- Quadratics (quad)")
    print("- xIntercept (xIntercept)")
    print("- yIntercept (yIntercept)")
    print("=====================================\n")

    while True:
        operation = input("Select an operation: ").strip()

        if operation in ALGEBRA_SPECS:
            return operation

        print("Please select a valid operation.")


# Variable Input

def getBasicVar(amount):
    numbers = []
    
    for i in range(amount):
        numbers.append(
            getNumber(f"Enter number {i + 1}: ")
        )

    return numbers


def getAlgebraVar(operation):
    numbers = []
    spec = ALGEBRA_SPECS[operation]

    for i in range(spec["points"]):
        x = getNumber(f"Enter a number for x{i + 1}: ")
        y = getNumber(f"Enter a number for y{i + 1}: ")
        numbers.append([x,y])
    
    for i in range(spec["numbers"]):
        numbers.append(
            getNumber(f"Enter Number {i+1}: ")
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
            print("The quadratic is invalid because 'a' cannot be 0.")
            print("=====================================\n")
            return True

    elif operation == "xIntercept":
        if variables[0] == 0:
            print("=====================================")
            print("There is no xIntercept because 'a' cannot be 0.")
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

    ALGEBRA_OPS = {
        "slope": algebra_helpers.slope,
        "midpoint": algebra_helpers.midpoint,
        "distance": algebra_helpers.distance
    }

    function = ALGEBRA_OPS.get(operation)

    if function is None:

        if operation == "quad":
            a, b, c = variables
            answer1, answer2 = algebra_helpers.quadratic(
                a, b, c
            )
            answers = [answer1, answer2]

        elif operation == "xIntercept":
            a, b = variables
            answer = algebra_helpers.xIntercept(
                a, b
            )
            answers = [answer]

        elif operation == "yIntercept":
            x1, y1 = variables[0]
            a = variables[1]
            answer = algebra_helpers.yIntercept(
                x1, y1, a
            )
            answers = [answer]

    else:
        x1, y1 = variables[0]
        x2, y2 = variables[1]
        if operation in ("distance","slope"):
            answer = function(x1,y1,x2,y2)
            answers = [answer]
        else:
            answer1, answer2 = function(x1,y1,x2,y2)
            answers = [answer1, answer2]

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

    # Will handle edge cases tomorrow

    print("=====================================")

    if operation == "slope":
        x1, y1 = variables[0]
        x2, y2 = variables[1]

        print(
            f"The slope of ({x1}, {y1}) and "
            f"({x2}, {y2}) = {answers[0]}"
        )

    elif operation == "midpoint":
        x1, y1 = variables[0]
        x2, y2 = variables[1]

        print(
            f"The midpoint of ({x1}, {y1}) and "
            f"({x2}, {y2}) = ({answers[0]}, {answers[1]})"
        )

    elif operation == "distance":
        x1, y1 = variables[0]
        x2, y2 = variables[1]

        print(
            f"The distance between ({x1}, {y1}) and "
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

    elif operation == "xIntercept":
        a, b = variables

        if answers is not None:
            print(f"The xIntercept of {a} and {b} is: ")
            print(f"{answers[0]}")

    else:
        x1, y1 = variables[0]
        a = variables[1]

        print(
            f"The yIntercept of ({x1}, {y1}) and "
            f"{a} = {answers[0]}"
        )


    print("=====================================\n")


# Run Program

if __name__ == "__main__":
    main()