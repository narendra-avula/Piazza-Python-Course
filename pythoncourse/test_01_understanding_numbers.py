__author__ = 'Narendra'

from placeholders import *

# For most of these tests use the interpreter to fill up the blanks.
# type(object) -> returns the object's type.

def test_numbers_types():
    assert 'int' == type(7).__name__
    assert 'float' == type(7.5).__name__
    assert 'long' == type(10L).__name__

def test_numbers_int_arithmetic_operations():
    assert 30 == 10 + 20
    assert 200 == 10 * 20
    assert 32 == 2 ** 5
    assert -10 == 10 - 20
    assert 2 == 7/3

def test_numbers_string_to_int():
    """hint: execute  print int.__doc__ to find out what int(..) does"""
    assert 255 == int("FF", 16)
    assert 63 == int("77", 8)

def test_numbers_int_to_string():
    assert '012' == oct(10)
    assert '0x64' == hex(100)
    assert '0b11111111' == bin(255)

def test_numbers_long():
    """Long is not the long in c"""
    assert 1606938044258990275541962092341162602522202993782792835301376L == 2 ** 200


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = __;




