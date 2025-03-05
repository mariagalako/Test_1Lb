import pytest
from Howework import (
    polindrome,
    back_string,
    vowels,
    remove_duplicates
)

def test_summation():
    """Testing Summation function"""
    assert palindrome("malayalam") == "malayalam"
    assert palindrome("deed") == "deed"
    assert palindrome("level") == "level"

def test_subtraction():
    """
    Testing Subtraction function
    """
    assert back_string("ASD") == "DSA"
    assert back_string("kill") == "llik"
    assert back_string("nuul") == "luun"

def test_multiplication():
    """
    Testing Multiplication function
    """
    assert vowels("ааффыыв") == 4
    assert vowels("аЁфук") == 3
    assert vowels("ккккукуку") == 3

def test_Division():
    """
    Testing Division function
    """
    assert remove_duplicates("hello world") == "helo wrd"
    assert remove_duplicates("he knows English") == "he knowsEgli"
    assert remove_duplicates("wooedd") == "woed"
