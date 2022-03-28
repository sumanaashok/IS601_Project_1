"""Calculation, Addition, Subtraction ,Multiplication and  Division Classes """
from calculator.operations import Add, Sub, Mul, Div


class Calculator:
    """ The Base abstract class for calculation"""

    num_list = []

    # pylint: disable=too-few-public-methods
    def __init__(self, num_list):
        """constructor for calculation class"""
        self.num_list = num_list
        self.values_list = Calculator.float_conversion(num_list)

    @classmethod
    def create(cls, num_list):
        return cls(num_list)

    @staticmethod
    def float_conversion(num_list):
        list_float = []
        for num in num_list:
            list_float.append(float(num))
        return list_float


class Summation(Calculator):
    """addition class"""

    def calculate_res(self):
        """returns addition results"""
        sum_values = 0.0
        for num in self.values_list:
            sum_values = Add.add(num, sum_values)
        return sum_values


class Difference(Calculator):
    """subtraction class"""

    def calculate_res(self):
        """returns the subtraction results"""
        diff_values = 0.0
        for value in self.values_list:
            diff_values = Sub.sub(diff_values, value)
        return diff_values


class Product(Calculator):
    """multiplication class"""

    def calculate_res(self):
        """returns multiplication results"""
        prod_values = 1.0
        for value in self.values_list:
            prod_values = Mul.mul(prod_values, value)
        return prod_values


class Divide(Calculator):
    """division class"""

    def calculate_res(self):
        """returns multiplication results"""
        div_values = 1.0
        for value in self.values_list:
            div_values = Div.div(div_values, value)
        return div_values
