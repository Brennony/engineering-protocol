# Brennon York  |  Algebra Helpers v1.2  |  8/16/2026

# Algebra
from math_helpers import sqrtRoot

def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def quadratic(a, b, c):
    try:
        disc = sqrtRoot((b**2) - 4*a*c)
    except ValueError:
        return None, None
    else:
        quad1 = ((-b + disc)/(2*a))
        quad2 = ((-b - disc)/(2*a))
        return quad1, quad2