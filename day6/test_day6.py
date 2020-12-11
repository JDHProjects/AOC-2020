from day6.day6 import groupParse, groupUnanimousParse, sumAnswers, sumUnanimousAnswers
testData = ["abc","a\nb\nc","ab\nac","a\na\na\na","b"]

def test_groupParse1():
    assert groupParse(testData[0]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupParse2():
    assert groupParse(testData[1]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupParse3():
    assert groupParse(testData[2]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupParse4():
    assert groupParse(testData[3]) == [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupParse5():
    assert groupParse(testData[4]) == [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupUnanimousParse1():
    assert groupUnanimousParse(testData[0]) == [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupUnanimousParse2():
    assert groupUnanimousParse(testData[1]) == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupUnanimousParse3():
    assert groupUnanimousParse(testData[2]) == [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupUnanimousParse4():
    assert groupUnanimousParse(testData[3]) == [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_groupUnanimousParse5():
    assert groupUnanimousParse(testData[4]) == [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def test_sumAnswers():
    assert sumAnswers(testData) == 11

def test_sumUnanimousAnswers():
    assert sumUnanimousAnswers(testData) == 6