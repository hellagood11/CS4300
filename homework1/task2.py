"""Homework 1 Task 2"""
import pytest

#create methods to be tested for int, float, string, and bool
def intAddition():
    return 3 + 3

def floatAddition():
    return 2.2 + 4.2

def stringAddition():
    return "AA" + "BB"

def booleanMethod():
    return (4 == 5)

#create methods to test the data types that the above methods return
def test_intAddition():
    assert isinstance(intAddition(), int)

def test_floatAddition():
    assert isinstance(floatAddition(), float)

def test_stringAddition():
    assert isinstance(stringAddition(), str)

def test_boolean():
    assert isinstance(booleanMethod(), bool)