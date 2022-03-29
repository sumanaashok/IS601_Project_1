"""History of calculations Class"""
from calculator.calculations import Summation, Difference, Product, Divide


class Calculations:
    """Calculations class manages the history of calculations"""
    hist = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clearing_history_calculations():
        """clear the history of calculations"""
        Calculations.hist.clear()
        return True

    @staticmethod
    def count_hist():
        """get number of items in history"""
        return len(Calculations.hist)

    @staticmethod
    def last_calculation_object():
        """get last calculation as object"""
        return Calculations.hist[-1]

    @staticmethod
    def last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.last_calculation_object()
        return calculation.calculate_res()

    @staticmethod
    def first_calculation():
        """get first calculation"""
        return Calculations.hist[0]

    @staticmethod
    def fetch_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.hist[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return Calculations.hist.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Summation.create(values))
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Difference.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Product.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Divide.create(values))
        return True
