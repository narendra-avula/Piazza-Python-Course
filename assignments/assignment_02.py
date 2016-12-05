__author__ = 'Kalyan'

notes = '''
Fill up each of this methods so that it does what it is intended to do. Use
only the standard data types we have seen so far and builtin functions.

builtin functions: http://docs.python.org/2/library/functions.html

Do not use any control flow statements (if, for...) in this assignment.
Assume that inputs are valid and of expected type, so no checking required.

use constants from string module (string.XXXX) as required.
'''

from placeholders import *

import string

def get_lower_to_upper_dict():
    """
    returns a dict which contains a mapping from lower case letters to upper case letters
    Hint: see the constants in the string module, and the zip builtin function
    """
    lower_to_upper_dict = {}
    for i in range(1,27):
        lower_to_upper_dict[ string.lowercase[i-1] ] = string.uppercase[i-1]
    return lower_to_upper_dict

def get_digit_to_string_dict():
    """
    return a dict which maps every digit to its string representation.
    Hint: same as above.
    """
    digit_to_string_dict = {}
    for i in range(0,10):
        digit_to_string_dict[i] = string.lowercase[i]
    return digit_to_string_dict

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___

def test_lower_to_upper_dict():
    lower_to_upper = get_lower_to_upper_dict()
    assert 26 == len(lower_to_upper)
    for x in lower_to_upper:
        y = lower_to_upper[x]
        assert 1 == len(x)
        assert x.islower()
        assert 1 == len(y)
        assert y.isupper()
        assert x.upper() == y


def test_digit_to_string_dict():
    digit_to_string = get_digit_to_string_dict()
    assert 10 == len(digit_to_string)
    for x in range(0,10):
        assert x in digit_to_string
        assert digit_to_string[x] == str(digit_to_string[x])