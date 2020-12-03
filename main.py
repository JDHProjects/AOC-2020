
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
