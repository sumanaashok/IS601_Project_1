"""Testing the Calculator"""
# From specifies the namespace
from calculator import CalculatorMain


def num_list():
    """Arranging for AAA Testing"""
    return 1.0, 2


def testing_add_method():
    """Testing the Calculator"""
    # Act for AAA testing

    result = CalculatorMain.add(num_list())

    # Assert for AAA testing
    assert result == 3


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    assert CalculatorMain.subtract(num_list()) == -3


def test_calculator_multiply_method():
    """Testing the Calculator multiply"""
    assert CalculatorMain.multiply(num_list()) == 2


def test_calculator_divide_method():
    """Testing the Calculator divide"""
    assert CalculatorMain.divide(num_list()) == 0.5
