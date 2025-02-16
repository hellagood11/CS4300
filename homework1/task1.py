"""Homework One Task One"""
import pytest
def main():
    return "Hello World!"

def test_main():
    assert main() == "Hello World!"

if __name__ == "__main__":
    print(main())