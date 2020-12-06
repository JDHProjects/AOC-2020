def boardingPassParse(lineToParse):
    row = binaryToInt(lineToParse[:7], "B", "F")
    col = binaryToInt(lineToParse[7:], "R", "L")
    return [row, col]

def binaryToInt(pattern, oneChar="1", zeroChar="0"):
    return int(pattern.replace(oneChar,"1").replace(zeroChar,"0"),2)

def findHighestBoardingPass(inData):
    return boardingPassesToSeatIDList(inData)[-1]

def boardingPassesToSeatIDList(inData):
    seatIDs = []
    for line in inData:
        rowCol = boardingPassParse(line)
        seatIDs.append(rowCol[0]*8 + rowCol[1])
    seatIDs.sort()
    return seatIDs

def missingBoardingPass(inData):
    seatIDs = boardingPassesToSeatIDList(inData)
    for i in range(1,len(seatIDs)-1):
        currentSeatID= seatIDs[i-1] +1
        if(currentSeatID != seatIDs[i]):
            return currentSeatID 
