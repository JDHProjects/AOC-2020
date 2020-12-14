
import os, sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from common.common import loadData


from day1.day1 import addToTwo, addToThree
def test_day_1_1():
    print(addToTwo(loadData("day1", parseInt=True)))
def test_day_1_2():
    print(addToThree(loadData("day1", parseInt=True)))

from day2.day2 import getValidPasswordsPart1, getValidPasswordsPart2
def test_day_2_1():
    print(len(getValidPasswordsPart1(loadData("day2"))))
def test_day_2_2():
    print(len(getValidPasswordsPart2(loadData("day2"))))

from day3.day3 import getTreeCount, multiSlope
def test_day_3_1():
    print(getTreeCount(loadData("day3"),3,1))
def test_day_3_2():
    print(multiSlope(loadData("day3"),[[1,1],[3,1],[5,1],[7,1],[1,2]]))

from day4.day4 import checkPassports, strictCheckPassports
def test_day_4_1():
    print(len(checkPassports(loadData("day4", splitChar="\n\n"))))
def test_day_4_2():
    print(len(strictCheckPassports(loadData("day4", splitChar="\n\n"))))

from day5.day5 import findHighestBoardingPass, missingBoardingPass
def test_day_5_1():
    print(findHighestBoardingPass(loadData("day5")))
def test_day_5_2():
    print(missingBoardingPass(loadData("day5")))

from day6.day6 import sumAnswers, sumUnanimousAnswers
def test_day_6_1():
    print(sumAnswers(loadData("day6", splitChar="\n\n")))
def test_day_6_2():
    print(sumUnanimousAnswers(loadData("day6", splitChar="\n\n")))

from day7.day7 import countBags, generateRules, bagsInBags
def test_day_7_1():
    print(countBags(generateRules(loadData("day7")),"shiny gold"))
def test_day_7_2():
    print(bagsInBags(generateRules(loadData("day7")),"shiny gold"))

from day8.day8 import runInfiniteProgram, instructionList, fixProgram
def test_day_8_1():
    print(runInfiniteProgram(instructionList(loadData("day8"))))
def test_day_8_2():
    print(fixProgram(instructionList(loadData("day8"))))

from day9.day9 import findIncorrectNum, findValFromRange
def test_day_9_1():
    print(findIncorrectNum(loadData("day9", parseInt=True),25))
def test_day_9_2():
    print(findValFromRange(loadData("day9", parseInt=True),findIncorrectNum(loadData("day9", parseInt=True),25)))

from day10.day10 import calculateJoltage, calculateDistinctJoltages
def test_day_10_1():
    print(calculateJoltage(loadData("day10", parseInt=True)))
def test_day_10_2():
    print(calculateDistinctJoltages(loadData("day10", parseInt=True)))

from day11.day11 import inputToList, countOccupied, stabilizeSeats
def test_day_11_1():
    print(countOccupied(stabilizeSeats(inputToList(loadData("day11")))))
def test_day_11_2():
    print(countOccupied(stabilizeSeats(inputToList(loadData("day11")),part2=True)))

from day12.day12 import moveBoatThroughPath, getManhattanDistance
def test_day_12_1():
    (x, y) = moveBoatThroughPath(loadData("day12"),0,0,0,0)
    print(getManhattanDistance(0,0,x,y))
def test_day_12_2():
    (x, y) = moveBoatThroughPath(loadData("day12"),10,1,0,0)
    print(getManhattanDistance(0,0,x,y))


from day13.day13 import parseBuses, getNextBus
def test_day_13_1():
    (timestamp, buses) = parseBuses(loadData("day13"))
    (bus, wait) = getNextBus(timestamp,buses)
    print(bus * wait)
def test_day_13_2():
    print("come back to this :(")


from day14.day14 import initialize
def test_day_14_1():
    print(initialize(loadData("day14",splitChar="\n\n")))
def test_day_14_2():
    print("come back to this :(")