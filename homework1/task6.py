"""Homework 1 Task 6"""
import pytest

# Expected word count from the given text file in a dictionary
expected_counts = {
    'task6_read_me.txt': 104  # Manually counted word count from counting editor in browser
}

# opens the file and counts the words that are in it. Stores the file name and read as the variable file
def count_words(filename):
    """Reads a file and returns the word count."""
    with open(filename, 'r') as file:
        return len(file.read().split())

# Metaprogramming: Generate test functions dynamically
def generate_test_case(filename, expected_count):
    def test_func():
        assert count_words(filename) == expected_count
    return test_func

# Dynamically create test functions
for filename, expected_count in expected_counts.items(): # take file name and expected word count from the dictionary
    test_name = f'test_word_count_{filename.replace(".", "_")}' # create a new test name by appending the file name to test word count and replacing the . with _ 
    globals()[test_name] = generate_test_case(filename, expected_count) # needs to be a global so that it can be accessed by pytest
