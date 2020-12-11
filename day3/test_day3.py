from day3.day3 import getTreeCount, multiSlope

testData = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]

def test_getTreeCount():
    assert getTreeCount(testData, 3, 1) == 7

def test_multiSlope():
    assert multiSlope(testData, [[1,1],[3,1],[5,1],[7,1],[1,2]]) == 336