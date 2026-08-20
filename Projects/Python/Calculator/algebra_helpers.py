# Brennon York  |  Algebra Helpers v1.3  |  8/19/2026

from math_helpers import sqrtRoot


# -- Algebra Functions --

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return None
    return (y2 - y1) / (x2 - x1)

def midpoint(x1, y1, x2, y2):
    return (
        (x1 + x2) / 2,
        (y1 + y2) / 2
    )

def distance(x1, y1, x2, y2):
    return sqrtRoot(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

def yIntercept(x1, y1, slope):
    return y1 - slope * x1

def xIntercept(a, b):
    if a == 0:
        return None
    return -b / a

def quadratic(a, b, c):
    # A quadratic requires a != 0.
    if a == 0:
        return None, None
    discriminant = (b ** 2) - (4 * a * c)
    # Negative discriminant = no real roots.
    if discriminant < 0:
        return None, None
    disc = sqrtRoot(discriminant)
    quad1 = (-b + disc) / (2 * a)
    quad2 = (-b - disc) / (2 * a)
    return quad1, quad2