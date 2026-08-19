#  Brennon York  |  Test Algebra Helpers v1.1  |  8/19/2026

from calculator import sortAlgebra
import algebra_helpers

# Slope Tests
def test_slope():
    assert algebra_helpers.slope(4,4,5,5) == 1
    assert algebra_helpers.slope(-3,3,-5,5) == -1

def test_horizontalSlope():
    assert algebra_helpers.slope(1,5,3,5) == 0

def test_undefinedSlope():
    assert sortAlgebra(2, 2, "slope") is True


# Quad Tests
def test_realQuads():
    assert algebra_helpers.quadratic(1,3,2) == (-1.0,-2.0)
    assert algebra_helpers.quadratic(1,5,4) == (-1.0,-4.0)

def test_negativeB():
    assert algebra_helpers.quadratic(1,-10,9) == (9.0,1.0)

def test_noRootsQuads():
    assert algebra_helpers.quadratic(1,0,1) == (None,None)

def test_repeatRootsQuads():
    assert algebra_helpers.quadratic(1,2,1) == (-1.0, -1.0)

def test_invalidQuads():
    assert sortAlgebra(0,1, "quad") is True