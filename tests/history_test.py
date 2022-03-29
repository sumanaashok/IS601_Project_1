"""Testing the Calculator"""
import pytest
from calculator.history import Calculations as History
from calculator.calculations import Summation


@pytest.fixture
def history_clear():
    """a function that will run each time you pass it to a test"""
    # pylint: disable=redefined-outer-name
    History.clearing_history_calculations()


@pytest.fixture
def addition_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = [2, 3]
    addition = Summation(values)
    History.add_calculation(addition)


def testing_add_calculation_to_history(history_clear, addition_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_hist() == 1


def testing_clear_calculation_from_history(history_clear, addition_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_hist() == 1
    History.clearing_history_calculations()
    assert History.count_hist() == 0
    assert History.clearing_history_calculations() == True


def testing_get_calculation(history_clear, addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.fetch_calculation(0).calculate_res() == 5


def testing_get_calc_last_result_value(history_clear, addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.last_calculation_result_value() == 5


def testing_get_first_calculation(history_clear, addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.first_calculation().calculate_res() == 5


def testing_history_count(history_clear, addition_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.count_hist() == 1


def testing_get_calc_last_result_object(history_clear, addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(History.last_calculation_object(), Summation)


def test_add_addition_calculation(history_clear, addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.add_addition_calculation
