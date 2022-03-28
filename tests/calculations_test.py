"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculations import Summation, Difference, Product, Divide


def test_calculation_multiplication_instance():
    """Testing the Calculator multiply"""
    # Arranging for AAA testing
    num_list = [1, 2]
    # Act for AAA testing
    calculation = Product.create(num_list)
    # Assert for AAA testing
    assert isinstance(calculation, Product)


def test_calculation_division_instance():
    """Testing the Calculator divide"""
    num_list = [1, 2]
    calculation = Divide.create(num_list)
    assert isinstance(calculation, Divide)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    num_list = [1, 2]
    calculation = Difference.create(num_list)
    assert isinstance(calculation, Difference)


def test_calculation_addition_instance():
    """Testing the Calculator add"""
    num_list = [1, 2]
    calculation = Summation.create(num_list)
    assert isinstance(calculation, Summation)


def test_calculation_add_get_result_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    num_list = [1, 2]
    calculation = Summation.create(num_list)
    assert calculation.calculate_res() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    num_list = [1, 2]
    calculation = Difference.create(num_list)
    assert calculation.calculate_res() == -3


def test_calculation_multiply_get_result_method():
    """Testing the Calculator Subtract"""
    num_list = [1, 2]
    calculation = Product.create(num_list)
    assert calculation.calculate_res() == 2


def test_calculation_divide_get_result_method():
    """Testing the Calculator Subtract"""
    num_list = [1, 2]
    calculation = Divide.create(num_list)
    assert calculation.calculate_res() == 0.5
