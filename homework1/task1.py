"""Homework One Task One"""
import pytest

#created one main method that returns hello world 
def printHelloWorld():
    print("Hello World!")

#makes sure that the main method returns the string that it is supposed to 
def test_HelloWorld(capfd):
    printHelloWorld()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"

