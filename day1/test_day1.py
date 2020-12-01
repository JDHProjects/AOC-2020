from day1 import addToTwo, addToThree

testData = [1721,979,366,299,675,1456]

def test_addToTwo():
    assert addToTwo(testData) == 514579

def test_addToThree():
    assert addToThree(testData) == 241861950