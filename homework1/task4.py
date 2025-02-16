"""Homework 1 Task 4"""
import pytest

def calculate_discount(price, discount):
    newPrice = 0
    if isinstance(discount, int):
        discount = (100-discount) * .01 # calculate new price with discount
        newPrice = round(price * discount,2) # round to two decimals 
    elif isinstance(discount, float):
        newPrice = round(price - (price * discount),2) #round the price to two decimals
    else:
        return -1 # if the input is not a float or int return error 
    return newPrice

# test the discount calculation with integers
def test_int_calculate_discount():
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(200, 55) == 90

# test the discount calculation with floating point 
def test_float_calculate_discount():
    assert calculate_discount(100, .20) == 80
    assert calculate_discount(200, .55) == 90