# Brennon York  |  Test Math Helpers v1.1  |  8/19/2026

import math_helpers


# =========================
# One Variable Tests
# =========================

def test_sqrtRoot():
    assert math_helpers.sqrtRoot(4) == 2
    assert math_helpers.sqrtRoot(25) == 5

def test_sqrtRoot_negative():
    assert math_helpers.sqrtRoot(-1) is None

def test_flr():
    assert math_helpers.flr(30.8) == 30
    assert math_helpers.flr(-30.8) == -31

def test_ceiling():
    assert math_helpers.ceiling(30.2) == 31
    assert math_helpers.ceiling(-30.2) == -30

def test_absVal():
    assert math_helpers.absVal(-4) == 4
    assert math_helpers.absVal(4) == 4


# =========================
# Two Variable Tests
# =========================

def test_addition():
    assert math_helpers.addition(2, 3) == 5
    assert math_helpers.addition(-2, 3) == 1

def test_subtraction():
    assert math_helpers.subtraction(5, 3) == 2
    assert math_helpers.subtraction(3, 5) == -2

def test_multiplication():
    assert math_helpers.multiplication(4, 5) == 20
    assert math_helpers.multiplication(-4, 5) == -20

def test_division():
    assert math_helpers.division(5, 2) == 2.5
    assert math_helpers.division(10, 2) == 5

def test_division_zero():
    assert math_helpers.division(5, 0) is None

def test_remainder():
    assert math_helpers.remainder(10, 3) == 1
    assert math_helpers.remainder(15, 5) == 0

def test_remainder_zero():
    assert math_helpers.remainder(5, 0) is None

def test_power():
    assert math_helpers.power(3, 3) == 27
    assert math_helpers.power(2, 4) == 16

def test_nthroot():
    assert math_helpers.nthroot(8, 3) == 2
    assert math_helpers.nthroot(16, 2) == 4

def test_nthroot_zero():
    assert math_helpers.nthroot(8, 0) is None


# =========================
# Logarithm Tests
# =========================

def test_log():
    assert math_helpers.logarithm(1, 10) == 0
    assert math_helpers.logarithm(100, 10) == 2

def test_log_invalid_number():
    assert math_helpers.logarithm(0, 10) is None
    assert math_helpers.logarithm(-5, 10) is None

def test_log_invalid_base():
    assert math_helpers.logarithm(10, 0) is None
    assert math_helpers.logarithm(10, 1) is None
    assert math_helpers.logarithm(10, -2) is None