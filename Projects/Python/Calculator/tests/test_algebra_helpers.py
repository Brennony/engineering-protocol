#  Brennon York  |  Test Algebra Helpers v1.0  |  8/18/2026

from calculator import sortAlgebra
import algebra_helpers

# Tests
def test_slope():
    assert algebra_helpers.slope(4,4,5,5) == 1
    assert algebra_helpers.slope(-3,3,-5,5) == -1

def test_horizontalslope():
    assert algebra_helpers.slope(1,5,3,5) == 0

def test_undefinedslope():
    assert sortAlgebra(2, 2, "slope") is True