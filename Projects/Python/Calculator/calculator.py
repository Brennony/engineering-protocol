# Brennon York  |  Calculator v1.4  |  8/29/2026


# 1.4 - Calculator 1.4: Completed with Basic Functions, Trig Functions, and Algebra Functions. Also contains history reader/caller and constants.
# Next version: 1.5 will be focused on handling Calculus. Future 2.0 will be built into a GUI. 



from math import pi, e, tau, isclose
import math_helpers
import algebra_helpers
import trig_helpers



# Main Program

def main():
    print("=====  PYTHON CALCULATOR V1.4  ======\n")

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

        elif choice == 3:
            operation = getTrig()
            mode = SETTINGS["angle_mode"]
            variables = getTrigVar(mode)
            if not sortTrig():     # False for now
                doTrig(operation, variables, mode)


        elif choice == 4:
            getSettings()



# Constants Dictionary

CONSTANTS = {
    "pi": pi,
    "e": e,
    "tau": tau
}
DISPLAY_NAMES = {
    3.141592653589793: "π",
    2.718281828459045: "e",
    6.283185307179586: "τ"
}


# Settings Dictionary

SETTINGS = {
    "angle_mode": "radians"
}

# History

HISTORY = []
LAST_ANSWER = None


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
TRIG_SPECS = {
    "sin",
    "cos",
    "tan",
    "sec",
    "csc",
    "cot",
    "arcsin",
    "arccos",
    "arctan"
}


# Function Selection

def getFunction():
    print("=====================================")
    print("Available Functions:")
    print("0. Quit Program")
    print("1. Basic Operations")
    print("2. Algebraic Operations")
    print("3. Trigonometry Operations")
    print("4. Settings")
    print("=====================================\n")

    while True:
        function = input("Select a function: ")

        if function in ("0", "1", "2",  "3", "4"):
            return int(function)

        print("Please select a valid function.")


# Settings Select

def getSettings():
    global SETTINGS

    while True:
        mode = SETTINGS["angle_mode"]
        print("=====================================")
        print("0. Quit")
        print(f"1. Radians/Degrees: {mode}")
        print("2. History")
        print("=====================================\n")
        Option = input("Select a valid option: ")
        if Option == "1":
            if SETTINGS["angle_mode"] == "radians":
                SETTINGS["angle_mode"] = "degrees"
            else:
                SETTINGS["angle_mode"] = "radians"
        elif Option == "0":
            break
        else:
            printHistory()
          
    

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
    return checkGetOps(BASIC_OPERATIONS)


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
    return checkGetOps(ALGEBRA_SPECS)

# Trigonometry Operations

def getTrig():
    print("=====================================")
    print("Operations:")
    print("- Sine (sin)")
    print("- Cosine (cos)")
    print("- Tangent (tan)")
    print("- Secant (sec)")
    print("- Cosecant (csc)")
    print("- Cotangent (cot)")
    print("- Arc Sine (arcsin)")
    print("- Arc Cosine (arccos)")
    print("- Arc Tangent (arctan)")
    print("=====================================\n")
    return checkGetOps(TRIG_SPECS)


# Check Operations

def checkGetOps(Dict):
    while True:
        operation = input("Select an operation: ").strip()
        if operation in Dict:
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


def getTrigVar(mode):
    numbers = []
    numbers.append(
        getNumber(f"Enter a number in {mode}: ")
    )
    return numbers


def getNumber(prompt):
    while True:
        try:
            raw = input(prompt).strip().lower()
            if raw in CONSTANTS:
                return CONSTANTS[raw]
            if raw == "ans":
                if LAST_ANSWER is not None:
                    return LAST_ANSWER
                print("No previous answer available.")
                continue
            return float(raw)
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


def sortTrig():
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

    addLast(answer)
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

    if operation == "quad" and answer1 is not None and answer2 is not None:
        choice = input("Which answer to save as 'ans'? (1 or 2): ").strip()
        addLast(answer2 if choice == "2" else answer1)
    else:
        addLast(answers[0])
    printAlgebra(operation, variables, answers)


# Trigonometry Calculations

def doTrig(operation, variables, mode):
    operations = {
            "sin": trig_helpers.sine,
            "cos": trig_helpers.cosine,
            "tan": trig_helpers.tang,
            "sec": trig_helpers.sec,
            "csc": trig_helpers.csc,
            "cot": trig_helpers.cot,
            "arcsin": trig_helpers.arcsin,
            "arccos": trig_helpers.arccos,
            "arctan": trig_helpers.arctan
        }
    
    if mode == "degrees":
        variables[0] = trig_helpers.degRads(variables[0])
    
    function = operations.get(operation)
    if function is None:
        return
    answer = function(variables[0])

    addLast(answer)
    printTrig(operation, variables, answer)


# Format Operations

def formatNum(value):
    if not isinstance(value, float):
        return value
    if isclose(value, 0, abs_tol=1e-9):
        return 0
    rounded = round(value)
    if isclose(value, rounded, rel_tol=1e-9):
        return rounded
    for const, symbol in DISPLAY_NAMES.items():
        if isclose(value, const, rel_tol=1e-9):
            return symbol
    return value


# Basic Output

def printBasic(operation, variables, answer):
    if operation == "sqrt":
        result = f"sqrt({formatNum(variables[0])}) = {formatNum(answer)}"
    elif operation == "abs":
        result = f"abs({formatNum(variables[0])}) = {formatNum(answer)}"
    elif operation == "flr":
        result = f"floor({formatNum(variables[0])}) = {formatNum(answer)}"
    elif operation == "ceil":
        result = f"ceil({formatNum(variables[0])}) = {formatNum(answer)}"
    elif operation == "root":
        result = f"{formatNum(variables[1])}th root of {formatNum(variables[0])} = {formatNum(answer)}"
    elif operation == "log":
        result = f"log base {formatNum(variables[1])} of {formatNum(variables[0])} = {formatNum(answer)}"
    else:
        result = f"{formatNum(variables[0])} {operation} {formatNum(variables[1])} = {formatNum(answer)}"

    print(f"=====================================\n{result}\n=====================================\n")
    addHistory(result)


def printAlgebra(operation, variables, answers):
    if operation == "slope":
        x1, y1 = variables[0]
        x2, y2 = variables[1]
        result = f"slope({formatNum(x1)}, {formatNum(y1)}, {formatNum(x2)}, {formatNum(y2)}) = {formatNum(answers[0])}"

    elif operation == "midpoint":
        x1, y1 = variables[0]
        x2, y2 = variables[1]
        result = f"midpoint({formatNum(x1)}, {formatNum(y1)}, {formatNum(x2)}, {formatNum(y2)}) = ({formatNum(answers[0])}, {formatNum(answers[1])})"

    elif operation == "distance":
        x1, y1 = variables[0]
        x2, y2 = variables[1]
        result = f"distance({formatNum(x1)}, {formatNum(y1)}, {formatNum(x2)}, {formatNum(y2)}) = {formatNum(answers[0])}"

    elif operation == "quad":
        a, b, c = variables
        answer1, answer2 = answers
        if answer1 is not None and answer2 is not None:
            result = f"{formatNum(a)}x^2 + {formatNum(b)}x + {formatNum(c)} = 0: x₁={formatNum(answer1)}, x₂={formatNum(answer2)}"
        else:
            result = f"{formatNum(a)}x^2 + {formatNum(b)}x + {formatNum(c)} = 0: no real roots"

    elif operation == "xIntercept":
        a, b = variables
        result = f"xIntercept({formatNum(a)}, {formatNum(b)}) = {formatNum(answers[0])}"

    else:
        x1, y1 = variables[0]
        a = variables[1]
        result = f"yIntercept({formatNum(x1)}, {formatNum(y1)}, slope={formatNum(a)}) = {formatNum(answers[0])}"

    print(f"=====================================\n{result}\n=====================================\n")
    addHistory(result)


def printTrig(operation, variables, answer):
    if answer is None:
        result = f"{operation}({formatNum(variables[0])}) = undefined"
    else:
        result = f"{operation}({formatNum(variables[0])}) = {formatNum(answer)}"

    print(f"=====================================\n{result}\n=====================================\n")
    addHistory(result)


# Add History

def addHistory(hisentry):
    if len(HISTORY) >= 100:
        HISTORY.pop(0)
    HISTORY.append(f"Entry {len(HISTORY)+1}: {hisentry}")


# Print History

def printHistory():
    print("\n===============History===============")
    try:
        HISTORY[0]
    except IndexError:
        print("       There is no history yet       ")
    else: 
        print(*HISTORY, sep='\n')
    print("=====================================\n")

def addLast(answer):
    global LAST_ANSWER
    LAST_ANSWER = answer

# Run Program

if __name__ == "__main__":
    main()