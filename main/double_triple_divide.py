"""
Program:               double_triple_divide.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-09-01

Uses a decorator and function to double a dividend, triple a divisor, and return the quotient.
"""

import functools


# Decorator
def double_and_triple(function):
    """
    Doubles dividend and triples divisor for divide function.

    :param function: divide function
    :return: divide function wrapper's result
    """

    # Preserve information of the original function.
    @functools.wraps(function)
    def wrapper_double_and_triple(number_to_double, number_to_triple):
        """
        Wrapper function for divide function

        :param number_to_double: dividend to be doubled
        :param number_to_triple:  divisor to be tripled
        :return: quotient of doubled dividend and tripled divisor
        """

        # Print message of arithmetic being performed on the dividend and divisor.
        print(f'Doubling {str(number_to_double)} and tripling {str(number_to_triple)}')
        # Double dividend.
        number_to_double *= 2
        # Triple divisor.
        number_to_triple *= 3
        # Print message of error if divisor is zero.
        if number_to_triple == 0:
            print('Cannot divide by zero')
        else:
            # Return quotient.
            return function(number_to_double, number_to_triple)
    # Return wrapper function's returned value.
    return wrapper_double_and_triple


@double_and_triple
def divide(dividend, divisor):
    """
    Divide dividend and divisor. Return integer result.

    :param dividend: dividend to be divided.
    :param divisor: divisor to divide by
    :return: quotient of division result
    """

    # Get division result.
    quotient = int(dividend / divisor)
    # Return quotient.
    return quotient


if __name__ == '__main__':
    # Print two working examples.
    print(f'{str(divide(12, 2))}')
    print(f'{str(divide(36, 4))}')
    # Print divide by zero error.
    print(f'{str(divide(2, 0))}')
