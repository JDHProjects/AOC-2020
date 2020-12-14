from day14.day14 import parseLine, maskNum, initialize

testData = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0","mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\nmem[8] = 11\nmem[7] = 101\nmem[8] = 0"]

def test_parseLine():
    assert parseLine(testData[0],[],[]) == ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",["mem[8]","mem[7]"], [0,101])

def test_maskNum():
    assert maskNum("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11) == 73

def test_initialize1():
    assert initialize([testData[0]]) == 165

def test_initialize2():
    assert initialize(testData) == 165
