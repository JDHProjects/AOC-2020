from day5.day5 import boardingPassParse, binaryToInt, findHighestBoardingPass
testData = ["BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]

def test_boardingPassParse():
    assert boardingPassParse(testData[0]) == [70,7]

def test_binaryToInt():
    assert binaryToInt(testData[0][:7], "B","F") == 70

def test_findHighestBoardingPass():
    assert findHighestBoardingPass(testData) == 820
