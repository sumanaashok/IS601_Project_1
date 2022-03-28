""" The 4 basic Operation Classes"""


class Add:
    """ This class is used for addition of 2 numbers"""

    # pylint: disable=redefined-outer-name
    @staticmethod
    def add(num1, num2):
        """This method does the addition operation"""
        add_res = num1 + num2
        return add_res


class Sub:
    """ This class is used for subtraction of 2 numbers"""

    # pylint: disable=redefined-outer-name
    @staticmethod
    def sub(num1, num2):
        """This method does the subtraction operation"""
        sub_res = num1 - num2
        return sub_res


class Mul:
    """ This class is used for multiplication of 2 numbers"""

    # pylint: disable=redefined-outer-name
    @staticmethod
    def mul(num1, num2):
        """This method does the multiplication operation"""
        mul_res = num1 * num2
        return mul_res


class Div:
    """ This class is used for division of 2 numbers"""

    # pylint: disable=redefined-outer-name
    @staticmethod
    def div(num1, num2):
        """This method does the multiplication operation"""
        div_res = num1 / num2
        return div_res
