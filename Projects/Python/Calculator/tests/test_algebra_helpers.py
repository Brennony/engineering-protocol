# Brennon York  |  Test Algebra Helpers v1.2  |  8/19/2026

import algebra_helpers


# =========================
# Slope Tests
# =========================

def test_slope():
    assert algebra_helpers.slope(4, 4, 5, 5) == 1
    assert algebra_helpers.slope(-3, 3, -5, 5) == -1

def test_horizontalSlope():
    assert algebra_helpers.slope(1, 5, 3, 5) == 0

def test_undefinedSlope():
    assert algebra_helpers.slope(2, 2, 2, 5) is None


# =========================
# Midpoint Tests
# =========================

def test_midpoint():
    assert algebra_helpers.midpoint(0, 0, 4, 4) == (2, 2)
    assert algebra_helpers.midpoint(1, 3, 5, 7) == (3, 5)


# =========================
# Distance Tests
# =========================

def test_distance():
    assert algebra_helpers.distance(0, 0, 3, 4) == 5
    assert algebra_helpers.distance(1, 1, 4, 5) == 5


# =========================
# Intercept Tests
# =========================

def test_yIntercept():
    assert algebra_helpers.yIntercept(2, 5, 3) == -1
    assert algebra_helpers.yIntercept(1, 4, 2) == 2

def test_xIntercept():
    assert algebra_helpers.xIntercept(2, 4) == -2
    assert algebra_helpers.xIntercept(5, 10) == -2

def test_xIntercept_invalid():
    assert algebra_helpers.xIntercept(0, 5) is None


# =========================
# Quadratic Tests
# =========================

def test_realQuads():
    assert algebra_helpers.quadratic(1, 3, 2) == (-1.0, -2.0)
    assert algebra_helpers.quadratic(1, 5, 4) == (-1.0, -4.0)

def test_negativeB():
    assert algebra_helpers.quadratic(1, -10, 9) == (9.0, 1.0)

def test_noRootsQuads():
    assert algebra_helpers.quadratic(1, 0, 1) == (None, None)

def test_repeatRootsQuads():
    assert algebra_helpers.quadratic(1, 2, 1) == (-1.0, -1.0)

def test_invalidQuads():
    assert algebra_helpers.quadratic(0, 1, 1) == (None, None)