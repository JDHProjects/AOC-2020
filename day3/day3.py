def getTreeCount(inData, x, y):
    treeCount = 0
    xOffset = 0
    for i in range(0,len(inData),y):     
        if(xOffset >= len(inData[i])):
            xOffset -= len(inData[i]) 

        if(inData[i][xOffset] == "#"):
            treeCount += 1
        xOffset += x
    return treeCount

def multiSlope(inData, slopeList):
    total = 1
    for slope in slopeList:
        total = total * getTreeCount(inData,slope[0],slope[1])
    return total