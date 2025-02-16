"""Homework One Task One"""
import pytest

#created one main method that returns hello world 
def main():
    return "Hello World!"

#makes sure that the main method returns the string that it is supposed to 
def test_main():
    assert main() == "Hello World!"

#prints the output of the main method
if __name__ == "__main__":
    print(main())