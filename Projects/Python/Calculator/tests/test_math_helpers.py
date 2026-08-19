#  Brennon York  |  Test Math Helpers v1.0  |  8/18/2026

import math_helpers

# Test One Variable
def test_sqrtRoot():
    assert math_helpers.sqrtRoot(4) == 2

def test_flr():
    assert math_helpers.flr(30.8) == 30

def test_ceiling():
    assert math_helpers.ceiling(30.2) == 31

def test_absVal():
    assert math_helpers.absVal(-4) == 4


# Test Two Variables
def test_addition():
    assert math_helpers.addition(2,3) == 5

def test_subtraction():
    assert math_helpers.subtraction(5,3) == 2

def test_multiplication():
    assert math_helpers.multiplication(4,5) == 20

def test_division():
    assert math_helpers.division(5,2) == 2.5

def test_remainder():
    assert math_helpers.remainder(10,3) == 1

def test_power():
    assert math_helpers.power(3,3) == 27

def test_nthroot():
    assert math_helpers.nthroot(8,3) == 2

