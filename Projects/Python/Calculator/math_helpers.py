# Brennon York  |  Math Helpers v1.3  |  8/29/2026

from math import sqrt, floor, ceil, log


# -- Basic Calculator Functions --

# Functions with One Variable:

def sqrtRoot(num1):
    if num1 < 0:
        return None
    return sqrt(num1)

def flr(num1):
    return floor(num1)

def ceiling(num1):
    return ceil(num1)

def absVal(num1):
    return abs(num1)


# Functions with Two or More Variables:

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2

def remainder(num1, num2):
    if num2 == 0:
        return None
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

def nthroot(num1, num2):
    if num2 == 0:
        return None
    return num1 ** (1 / num2)

def logarithm(num1, num2):
    if num1 <= 0 or num2 <= 0 or num2 == 1:
        return None
    return log(num1, num2)