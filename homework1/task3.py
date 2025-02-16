"""Homewok 1 Task 3"""

def valueCheck (value):
    if value < 0: #check if value is less than zero --> negative
        return "Negative"
    elif value > 0: # check if value is greater than zero --> positive
        return "Positive"
    elif value == 0: #check if value is zero 
        return "Zero"

def firstTenPrimeNum(value):
    num = 2 #start at the value 2 (first prime greater than 1)
    for _ in range(value): # iterate as many times as value (number of prime numbers we want)
        while any(num % i == 0 for i in range(2, int(num ** 0.5) + 1)): #calculate if its a prime
            num += 1
        print(num, end=" ") #print if a prime
        num += 1

def sumNumbers(value): # sum the numbers from 1 to the value given
    i = 1
    total = 0
    while i <= value:
        total = total + i
        i+=1
    return total
def test_valueCheck_zero():# test zero in value check
    assert valueCheck(0) == "Zero"

def test_valueCheck_negative(): #test negative in value check 
    assert valueCheck(-2) == "Negative"

def test_valueCheck_positive(): # test positive in value check
    assert valueCheck(4) == "Positive"

def test_firstTenPrimeNum(capfd): # test if the output is the first 10 prime numbers
    firstTenPrimeNum(10)
    out, err = capfd.readouterr()
    assert out == "2 3 5 7 11 13 17 19 23 29 "

def test_sumNumbers(): # test if the return value of sumNumbers is the sum of the numbers from 1 to the value chosen
    assert sumNumbers(100) == 5050