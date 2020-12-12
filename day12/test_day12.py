from day12.day12 import getManhattanDistance, moveObject, moveBoatThroughPath, rotateObject

testData = ["F10",
            "N3",
            "F7",
            "R90",
            "F11"]

def test_moveObject1():
    assert moveObject(testData[0],"E", 0, 0, 0, 0) == ("E",10,0,10,0)

def test_moveObject2():
    assert moveObject(testData[1],"E", 10, 0, 10, 0) == ("E",10,3,10,3)

def test_moveObject3():
    assert moveObject("L90","E", 0, 0, 0, 0) == ("N",0,0,0,0)

def test_moveObject4():
    assert moveObject("L180","E", 0, 0, 0, 0) == ("W",0,0,0,0)

def test_moveObject5():
    assert moveObject("L270","E", 0, 0, 0, 0) == ("S",0,0,0,0)

def test_moveObject6():
    assert moveObject("L360","E", 0, 0, 0, 0) == ("E",0,0,0,0)

def test_moveObject7():
    assert moveObject("R90","E", 0, 0, 0, 0) == ("S",0,0,0,0)

def test_moveObject8():
    assert moveObject("R180","E", 0, 0, 0, 0) == ("W",0,0,0,0)

def test_moveObject9():
    assert moveObject("R270","E", 0, 0, 0, 0) == ("N",0,0,0,0)

def test_moveObject10():
    assert moveObject("R360","E", 0, 0, 0, 0) == ("E",0,0,0,0)

def test_moveBoatThroughPath():
    assert moveBoatThroughPath(testData,0,0,0,0) == (17, -8)

def test_getManhattanDistance():
    (x, y) = moveBoatThroughPath(testData,0,0,0,0)
    assert getManhattanDistance(0,0,x,y) == 25

def test_rotateObject1():
    assert rotateObject("E",90,10,4,0,0) == ("S",4,-10)

def test_rotateObject2():
    assert rotateObject("E",180,10,4,0,0) == ("W",-10,-4)

def test_rotateObject3():
    assert rotateObject("E",270,10,4,0,0) == ("N",-4,10)

def test_rotateObject4():
    assert rotateObject("E",-90,10,4,0,0) == ("N",-4,10)

def test_rotateObject5():
    assert rotateObject("E",-180,10,4,0,0) == ("W",-10,-4)

def test_rotateObject6():
    assert rotateObject("E",-270,10,4,0,0) == ("S",4,-10)

def test_rotateObject7():
    assert rotateObject("N",90,-3,8,0,0) == ("E",8,3)

def test_rotateObject8():
    assert rotateObject("W",180,-8,-3,0,0) == ("E",8,3)

def test_moveObject11():
    assert moveObject("F10","E", 10, 1, 0, 0) == ("E",110,11,100,10)

def test_moveObject12():
    assert moveObject("N3","E", 10, 1, 0, 0) == ("E",10,4,0,0)

def test_moveObject13():
    assert moveObject("W5","E", 10, 1, 0, 0) == ("E",5,1,0,0)

def test_moveObject14():
    assert moveObject("F5","N", 45, 45, 50, 50) == ("W",20,20,25,25)

def test_moveObject15():
    assert moveObject("F5","N", -5, -5, 0, 0) == ("W",-30,-30,-25,-25)

def test_moveBoatThroughPath2():
    assert moveBoatThroughPath(testData,10,1,0,0) == (214, -72)