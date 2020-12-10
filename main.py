
from common.common import loadData

from day1.day1 import addToTwo, addToThree
print("day 1 part 1 = "+str(addToTwo(loadData("day1", parseInt=True))))
print("day 1 part 2 = "+str(addToThree(loadData("day1", parseInt=True))))

from day2.day2 import getValidPasswordsPart1, getValidPasswordsPart2
print("day 2 part 1 = "+str(len(getValidPasswordsPart1(loadData("day2")))))
print("day 2 part 2 = "+str(len(getValidPasswordsPart2(loadData("day2")))))

from day3.day3 import getTreeCount, multiSlope
print("day 3 part 1 = "+str(getTreeCount(loadData("day3"),3,1)))
print("day 3 part 2 = "+str(multiSlope(loadData("day3"),[[1,1],[3,1],[5,1],[7,1],[1,2]])))

from day4.day4 import checkPassports, strictCheckPassports
print("day 4 part 1 = "+str(len(checkPassports(loadData("day4", splitChar="\n\n")))))
print("day 4 part 2 = "+str(len(strictCheckPassports(loadData("day4", splitChar="\n\n")))))

from day5.day5 import findHighestBoardingPass, missingBoardingPass
print("day 5 part 1 = "+str(findHighestBoardingPass(loadData("day5"))))
print("day 5 part 2 = "+str(missingBoardingPass(loadData("day5"))))

from day6.day6 import sumAnswers, sumUnanimousAnswers
print("day 5 part 1 = "+str(sumAnswers(loadData("day6", splitChar="\n\n"))))
print("day 5 part 2 = "+str(sumUnanimousAnswers(loadData("day6", splitChar="\n\n"))))

from day7.day7 import countBags, generateRules, bagsInBags
print("day 7 part 1 = "+str(countBags(generateRules(loadData("day7")),"shiny gold")))
print("day 7 part 1 = "+str(bagsInBags(generateRules(loadData("day7")),"shiny gold")))

from day8.day8 import runInfiniteProgram, instructionList, fixProgram
print("day 8 part 1 = "+str(runInfiniteProgram(instructionList(loadData("day8")))))
print("day 8 part 2 = "+str(fixProgram(instructionList(loadData("day8")))))

from day9.day9 import findIncorrectNum, findValFromRange
print("day 9 part 1 = "+str(findIncorrectNum(loadData("day9", parseInt=True),25)))
print("day 9 part 2 = "+str(findValFromRange(loadData("day9", parseInt=True),findIncorrectNum(loadData("day9", parseInt=True),25))))

from day10.day10 import calculateJoltage, calculateDistinctJoltages
print("day 10 part 1 = "+str(calculateJoltage(loadData("day10", parseInt=True))))
print("day 10 part 2 = "+str(calculateDistinctJoltages(loadData("day10", parseInt=True))))