"""Homework 1 Task 7"""
import pytest
import numpy as np

"""Our specific task it to use numpy to do array multiplication and we will test that the output is another numpy array and not a regular array"""
#do array multiplication using numpy
def arrayMultiplication():
    array1 = np.array([1,2,3])
    array2 = np.array([3,2,1])
    array3 = array1 * array2
    return array3

# test that the return was a numpy array 
def test_arrayMultiplication():
    assert isinstance(arrayMultiplication(), np.ndarray)