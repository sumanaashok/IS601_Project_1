"""Testing the calculator operations """

from calculator.operations import Add, Sub, Mul, Div


def testing_operations_add():
    """Testing the Calculator"""
    assert Add.add(2, 3) == 5


def testing_operations_subtract():
    """Testing the Calculator"""
    assert Sub.sub(3, 2) == 1


def testing_operations_multiply():
    """Testing the Calculator"""
    assert Mul.mul(3, 2) == 6


def testing_operations_divide():
    """Testing the Calculator"""
    assert Div.div(1, 1) == 1


def testing_operations_divide_by_zero():
    """Testing the Divide By Zero operation"""
    try:
        Div.div(25, 0)
    except ZeroDivisionError:
        assert True
