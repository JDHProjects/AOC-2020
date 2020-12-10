def calculateJoltage(inData):
    oneCount = 0    
    threeCount = 0
    inData.append(0)
    inData.append(max(inData)+3)
    inData.sort()
    for i in range(0,len(inData)-1):
        diff = inData[i+1] - inData[i]
        if (diff == 1):
            oneCount += 1
        elif (diff == 3):
            threeCount += 1

    return oneCount * threeCount

def calculateDistinctJoltages(inData):
    inData.append(0)
    inData.append(max(inData)+3)
    inData.sort()
    total = 1
    multiList = []
    for i in range(0,len(inData)-2):
        if (inData[i+2] - inData[i] <= 3):
            if (multiList == []):
                multiList+=inData[i:i+3]
            else:
                multiList.append(inData[i+2])
        else:
            if (multiList != []):
                total = total * calculateJoltageGroups(multiList)
                multiList = []
    return total

def calculateJoltageGroups(joltageGroup):
    multiplier = 1
    for i in range(0, len(joltageGroup)-2):
        if(joltageGroup[i+2] - joltageGroup[i] <= 3):
            multiplier = multiplier * 2
            if(joltageGroup[i+2] - joltageGroup[0] > 3 ):
                multiplier -= 1
    return multiplier