from day9 import findIncorrectNum, findValFromRange

testData = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]


def test_findIncorrectNum():
    assert findIncorrectNum(testData, 5) == 127

def test_findValFromRange():
    assert findValFromRange(testData, 127) == 62