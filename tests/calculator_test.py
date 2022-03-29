"""Testing the Calculator"""
# From specifies the namespace
from calculator import CalculatorMain


def num_list():
    """Arranging for AAA Testing"""
    return 2.0, 3


def testing_add_method():
    """Testing the Calculator"""
    # Act for AAA testing

    result = CalculatorMain.add(num_list())

    # Assert for AAA testing
    assert result == 5


def testing_subtract_method():
    """Testing the Calculator Subtract"""
    assert CalculatorMain.subtract(num_list()) == -5


def testing_multiply_method():
    """Testing the Calculator multiply"""
    assert CalculatorMain.multiply(num_list()) == 6


def testing_divide_method():
    """Testing the Calculator divide"""
    assert CalculatorMain.divide(num_list()) == 0.16666666666666666
