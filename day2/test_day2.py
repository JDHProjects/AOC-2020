from day2.day2 import lineParse, getValidPasswordsPart1, getValidPasswordsPart2

testData = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

def test_lineParse():
    assert lineParse(testData[0]) == [1,3,'a',"abcde"]

def test_getValidPasswordsPart1():
    assert len(getValidPasswordsPart1(testData)) == 2

def test_getValidPasswordsPart2():
    assert len(getValidPasswordsPart2(testData)) == 1