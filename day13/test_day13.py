from day13.day13 import parseBuses, getNextBus, parseAllBuses

testData = ["939",
            "7,13,x,x,59,x,31,19"]

def test_parseBuses():
    assert parseBuses(testData) == (939,[7,13,59,31,19])

def test_getNextBus():
    (timestamp, buses) = parseBuses(testData)
    assert getNextBus(timestamp,buses) == (59,5)
