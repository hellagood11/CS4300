"""Homework 1 task 5"""
import pytest

# list of favorite books tuple as title, author
favoriteBookList =[
    ("The Martian", "Andy Weir"),
    ("1984", "George Orwell"),
    ("The Giver", "Lois Lowry"),
    ("Hatchet", "Gary Paulsen"),
    ("Artemis Fowl", "Eoin Colfer")
]

#Create student database from a dictionary
studentDatabase = {
    "Jim": "0001",
    "John": "0002",
    "Sam": "0003",
    "Sarah": "0004",
    "Thomas": "0005"
}
# print the first three books using list slicing
print(favoriteBookList[:3]) 

#function to get the first three books in the list
def getFirstThreeBooks():
    return favoriteBookList[:3]

#function to get the ID based on a name from a student ID
def getStudentID(name):
    return studentDatabase.get(name)

# pytest to test if the first three books were what they were supposed to be
def test_bookList():
    expectedOutput = [
        ("The Martian", "Andy Weir"),
        ("1984", "George Orwell"),
        ("The Giver", "Lois Lowry")
    ]
    assert expectedOutput == getFirstThreeBooks()

# test to make sure the database is set up correctly
def test_Database():
    assert getStudentID("Jim") == "0001"
    assert getStudentID("John") == "0002"
    assert getStudentID("Sam") == "0003"
    assert getStudentID("Sarah") == "0004"
    assert getStudentID("Thomas") == "0005"
