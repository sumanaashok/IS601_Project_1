"""Testing the calculator operations """

from calculator.operations import Add, Sub, Mul, Div


def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Add.add(1, 1) == 2


def test_calculator_operations_subtract():
    """Testing the Calculator"""
    assert Sub.sub(1, 1) == 0


def test_calculator_operations_multiply():
    """Testing the Calculator"""
    assert Mul.mul(1, 1) == 1


def test_calculator_operations_divide():
    """Testing the Calculator"""
    assert Div.div(1, 1) == 1
