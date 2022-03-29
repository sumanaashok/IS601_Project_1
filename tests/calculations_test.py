"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Summation, Difference, Product, Divide


def test_multiplication_instance():
    """Testing the Calculator multiply"""
    # Arranging for AAA testing
    num_list = [2, 3]
    # Act for AAA testing
    calculation = Product.create(num_list)
    # Assert for AAA testing
    assert isinstance(calculation, Product)


def test_division_instance():
    """Testing the Calculator divide"""
    num_list = [2, 3]
    calculation = Divide.create(num_list)
    assert isinstance(calculation, Divide)


def test_subtraction_instance():
    """Testing the Calculator Subtract"""
    num_list = [2, 3]
    calculation = Difference.create(num_list)
    assert isinstance(calculation, Difference)


def test_addition_instance():
    """Testing the Calculator add"""
    num_list = [2, 3]
    calculation = Summation.create(num_list)
    assert isinstance(calculation, Summation)


def test_add_get_result_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    num_list = [2, 3]
    calculation = Summation.create(num_list)
    assert calculation.calculate_res() == 5


def test_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    num_list = [2, 3]
    calculation = Difference.create(num_list)
    assert calculation.calculate_res() == -5


def test_multiply_get_result_method():
    """Testing the Calculator Subtract"""
    num_list = [2, 3]
    calculation = Product.create(num_list)
    assert calculation.calculate_res() == 6


def test_divide_get_result_method():
    """Testing the Calculator Subtract"""
    num_list = [2, 4]
    calculation = Divide.create(num_list)
    assert calculation.calculate_res() == 0.125
