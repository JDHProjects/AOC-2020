from day8.day8 import lineParse, instructionList, runInfiniteProgram, runProgram, fixProgram

testData = ["nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6"]
        
testData2 = ["nop +0",
             "acc +1",
             "jmp +4",
             "acc +3",
             "jmp -3",
             "acc -99",
             "acc +1",
             "nop -4",
             "acc +6"]
 
def test_lineParse1():
    assert lineParse(testData[0]) == ["nop",0]

def test_lineParse2():
    assert lineParse(testData[1]) == ["acc",1]

def test_lineParse3():
    assert lineParse(testData[2]) == ["jmp",4]

def test_lineParse4():
    assert lineParse(testData[3]) == ["acc",3]

def test_lineParse5():
    assert lineParse(testData[4]) == ["jmp",-3]

def test_instructionList():
    assert instructionList(testData) == [["nop", 0],
                                        ["acc", 1],
                                        ["jmp", 4],
                                        ["acc", 3],
                                        ["jmp", -3],
                                        ["acc", -99],
                                        ["acc", 1],
                                        ["jmp", -4],
                                        ["acc", 6]]

def test_runInfiniteProgram():
    assert runInfiniteProgram(instructionList(testData)) == 5

def test_runProgram1():
    assert runProgram(instructionList(testData)) == False

def test_runProgram2():
    assert runProgram(instructionList(testData2)) == 8

def test_fixProgram():
    assert fixProgram(instructionList(testData)) == 8