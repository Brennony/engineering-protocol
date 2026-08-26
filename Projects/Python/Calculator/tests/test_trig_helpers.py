# Brennon York  |  Test Trigonometry Helpers v1  |  8/24/2026

import trig_helpers
from math import pi, isclose

def test_sin():
    assert trig_helpers.sine(0) == 0

def test_cos():
    assert isclose(trig_helpers.cosine(pi/2), 0, abs_tol=1e-9) 

def test_tan():
    assert isclose(trig_helpers.tang(pi), 0, abs_tol=1e-9)
    assert trig_helpers.tang(pi/2) is None

def test_asin():
    assert trig_helpers.arcsin(1) == pi/2
    assert trig_helpers.arcsin(40) is None

def test_acos():
    assert trig_helpers.arccos(1) == 0
    assert trig_helpers.arccos(40) is None

def test_atan():
    assert trig_helpers.arctan(0) == 0

def test_csc():
    assert isclose(trig_helpers.csc(pi/2), 1, abs_tol=1e-9)
    assert trig_helpers.csc(pi) is None

def test_sec():
    assert isclose(trig_helpers.sec(pi), -1, abs_tol=1e-9)
    assert trig_helpers.sec(pi/2) is None

def test_cot():
    assert isclose(trig_helpers.tang(pi/2), 0, abs_tol=1e-9)
    assert trig_helpers.cot(0) is None