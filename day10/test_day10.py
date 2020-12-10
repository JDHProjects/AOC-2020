from day10 import calculateJoltage, calculateDistinctJoltages, calculateJoltageGroups

testData = [16,10,15,5,1,11,7,19,6,12,4]

testData2 = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]

testData3 = [17,11,16,5,1,12,8,20,6,13,4]

testData4 = [1,4,5,6,7,8]

testData5 = [4,5,6]

testData6 = [4,5,6,7]

testData7 = [4,5,6,8]

testData8 = [1,4,5,6,9,12]

def test_calculateJoltage():
    assert calculateJoltage(testData.copy()) == 35

def test_calculateDistinctJoltages():
    assert calculateDistinctJoltages(testData.copy()) == 8

def test_calculateDistinctJoltages2():
    assert calculateDistinctJoltages(testData2.copy()) == 19208

def test_calculateDistinctJoltages3():
    assert calculateDistinctJoltages(testData3.copy()) == 6

def test_calculateDistinctJoltages4():
    assert calculateDistinctJoltages(testData8.copy()) == 2

def test_calculateJoltageGroups1():
        assert calculateJoltageGroups(testData5.copy()) == 2

def test_calculateJoltageGroups2():
        assert calculateJoltageGroups(testData6.copy()) == 4
    
def test_calculateJoltageGroups3():
        assert calculateJoltageGroups(testData7.copy()) == 3
