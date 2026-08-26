# Brennon York  |  Trigonometry Helpers v1  |  8/24/2026

import math

# -- Trig Functions -- 


## Convert degrees to radians

def degRads(x):
    radians = x * (math.pi / 180)
    return radians

## One Variable Trig

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tang(x):
    if math.isclose(cosine(x), 0, abs_tol=1e-9):
        return None
    return math.tan(x)

def csc(x):
    if math.isclose(sine(x), 0, abs_tol=1e-9):
        return None
    return (1/sine(x))

def sec(x):
    if math.isclose(cosine(x), 0, abs_tol=1e-9):
        return None
    return (1/cosine(x))

def cot(x):
    t = tang(x)
    if t is None or t == 0:
        return None
    return (1/t)

def arcsin(x):
    if -1 > x or 1 < x:
        return None
    return math.asin(x)

def arccos(x):
    if -1 > x or 1 < x:
        return None
    return math.acos(x)

def arctan(x):
    return math.atan(x)