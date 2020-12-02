
from common.common import loadData

from day1.day1 import addToTwo, addToThree
print("day 1 part 1 = "+str(addToTwo(loadData("day1", parseInt=True))))
print("day 1 part 2 = "+str(addToThree(loadData("day1", parseInt=True))))

from day2.day2 import getValidPasswordsPart1, getValidPasswordsPart2
print("day 2 part 1 = "+str(len(getValidPasswordsPart1(loadData("day2")))))
print("day 2 part 2 = "+str(len(getValidPasswordsPart2(loadData("day2")))))
