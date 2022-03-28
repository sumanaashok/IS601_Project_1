""" This is the Calculator Class"""
from calculator.calculations import Summation, Difference, Product, Divide


class CalculatorMain:
    """ This is the default result property"""

    @staticmethod
    def add(num_list):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Summation.create(num_list)
        return calculation.calculate_res()

    @staticmethod
    def subtract(num_list):
        """ This is the subtract method"""
        calculation = Difference.create(num_list)
        return calculation.calculate_res()

    @staticmethod
    def multiply(num_list):
        """ This is the multiplication method"""
        calculation = Product.create(num_list)
        return calculation.calculate_res()

    @staticmethod
    def divide(num_list):
        """ This is the division method"""
        calculation = Divide.create(num_list)
        return calculation.calculate_res()
