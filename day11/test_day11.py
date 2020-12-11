from day11 import inputToList, checkSeat, checkAllSeats, stabilizeSeats, countOccupied, checkFarSeat

testData = ["L.LL.LL.LL"
           ,"LLLLLLL.LL"
           ,"L.L.L..L.."
           ,"LLLL.LL.LL"
           ,"L.LL.LL.LL"
           ,"L.LLLLL.LL"
           ,"..L.L....."
           ,"LLLLLLLLLL"
           ,"L.LLLLLL.L"
           ,"L.LLLLL.LL"]

testOutput = ["#.##.##.##"
             ,"#######.##"
             ,"#.#.#..#.."
             ,"####.##.##"
             ,"#.##.##.##"
             ,"#.#####.##"
             ,"..#.#....."
             ,"##########"
             ,"#.######.#"
             ,"#.#####.##"]

testData2 = [".......#.",
               "...#.....",
               ".#.......",
               ".........",
               "..#L....#",
               "....#....",
               ".........",
               "#........",
               "...#....."]


def test_inputToList():
    assert inputToList(testData) == [["L",".","L","L",".","L","L",".","L","L"],
                                      ["L","L","L","L","L","L","L",".","L","L"],
                                      ["L",".","L",".","L",".",".","L",".","."],
                                      ["L","L","L","L",".","L","L",".","L","L"],
                                      ["L",".","L","L",".","L","L",".","L","L"],
                                      ["L",".","L","L","L","L","L",".","L","L"],
                                      [".",".","L",".","L",".",".",".",".","."],
                                      ["L","L","L","L","L","L","L","L","L","L"],
                                      ["L",".","L","L","L","L","L","L",".","L"],
                                      ["L",".","L","L","L","L","L",".","L","L"]]

def test_checkSeat1():
    assert checkSeat(inputToList(testData),2,3) == True

def test_checkSeat2():
    assert checkSeat(inputToList(testData),3,2) == False

def test_checkSeat3():
    assert checkSeat(inputToList(testData),0,0) == True

def test_checkSeat4():
    assert checkSeat(inputToList(testData),1,0) == False

def test_checkAllSeats():
    assert checkAllSeats(inputToList(testData)) == inputToList(testOutput)

def test_stabilizeSeats():
    assert countOccupied(stabilizeSeats(inputToList(testData))) == 37

def test_checkFarSeat():
    assert checkFarSeat(inputToList(testData2),3,4) == False
    
def test_stabilizeSeatsPart2():
    assert countOccupied(stabilizeSeats(inputToList(testData),part2=True)) == 26