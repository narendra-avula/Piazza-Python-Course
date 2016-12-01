__author__ = 'Narendra'

from placeholders import *

# This lesson introduces the basic assert statement in python

def test_assert_true():
    #throws assertion error
    assert True  #This should be True -- replace ___ with True.

def test_assert_true_with_message():
    assert True, "This should be True, fix this"

def test_assert_equality():
    assert 7 == 2 + 5   #replace __ with the expected value

#Fill in __ in the statements below to make the asserts succeed
def test_make_assert_true_1():
    assert 8 > 7, "Fill in a value greater than 7"

#you can use the interpreter to find the value of 2**30
def test_make_assert_true_2():
    assert 10737418255 > 2**30, "Fill in value greater than 2**30"

def test_make_assert_true_3():
    s1 = "Hello, World"
    s2 = "Hello, World"
    assert s1 == s2

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = __;

