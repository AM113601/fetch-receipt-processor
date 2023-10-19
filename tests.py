import os
import json
from rules import *

test_data = [
    os.path.join("tests", "test1.json"),
    os.path.join("tests", "test2.json"),
]

def readFile(path):
    with open(path, 'r') as file:
        file_data = json.load(file)
    return file_data

data0 = readFile(test_data[0])
data1 = readFile(test_data[1])

# Checks the retailers name.
def test1():
    if rule1(data0, 1) != 6: 
        print("Rule 1 doesn't pass for test1.json.")
        return False
    if rule1(data1, 2) != 28: 
        print("Rule 1 doesn't pass for test2.json.")
        return False
    return True    

# Checks the total calculation round dollar
def test2():
    total0 = float(data0["total"])
    total1 = float(data1["total"])
    if rule2(total0, 50) != 0:
        print("Rule 2 doesn't pass for test1.json.")
        return False
    if rule2(total1, 75) != 75:
        print("Rule 2 doesn't pass for test2.json.")
        return False
    return True

# Checks the total calculation % 0.25
def test3():
    total0 = float(data0["total"])
    total1 = float(data1["total"])
    if rule3(total0, 50) != 0:
        print("Rule 3 doesn't pass for test1.json.")
        return False
    if rule3(total1, 75) != 75:
        print("Rule 3 doesn't pass for test2.json.")
        return False
    return True

# Checks number of items on receipt
def test4():
    if rule4(data0, 5) != 10: 
        print("Rule 4 doesn't pass for test1.json.")
        return False
    if rule4(data1, 6) != 12: 
        print("Rule 4 doesn't pass for test2.json.")
        return False
    return True  

# Checks length of item
def test5():
    if rule5(data0) != 6: 
        print("Rule 5 doesn't pass for test1.json.")
        return False
    if rule5(data1) != 0: 
        print("Rule 5 doesn't pass for test2.json.")
        return False
    return True  

# Checks purchase date odd
def test6():
    if rule6(data0, 6) != 6: 
        print("Rule 6 doesn't pass for test1.json.")
        return False
    if rule6(data1, 6) != 0: 
        print("Rule 6 doesn't pass for test2.json.")
        return False
    return True  

# Checks purchase time
def test7():
    if rule7(data0, 0) != 0: 
        print("Rule 7 doesn't pass for test1.json.")
        return False
    if rule7(data1, 10) != 10: 
        print("Rule 7 doesn't pass for test2.json.")
        return False
    return True  

def run_all():
    passed = 0
    tests = [
        test1, 
        test2,
        test3, 
        test4,
        test5,
        test6,
        test7,
    ]
    for test in tests:
        if test():
            passed += 1

    print("Passed " + str(passed) + " out of " + str(len(tests)) + " tests.")

# Run file
if __name__ == '__main__':
    run_all()