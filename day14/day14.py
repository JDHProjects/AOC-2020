def parseLine(inData,memPos,memVal):
    lines = inData.split("\n")
    bitmask = lines[0][7:]
    for line in lines[1:]:
        posVal = line.split(" = ")
        if(posVal[0] in memPos):
            memVal[memPos.index(posVal[0])] = maskNum(bitmask,int(posVal[1]))
        else:
            memPos.append(posVal[0])
            memVal.append(maskNum(bitmask,int(posVal[1])))
    return bitmask, memPos, memVal

def maskNum(mask, num):
    binary = bin(num)[2:]
    binary = ((len(mask)-len(binary)) * "0") + binary
    masked = ""
    for i in range(0,len(mask)):
        if(mask[i] == "X"):
            masked += binary[i]
        else:
            masked += mask[i]
    return int(masked,2)

def initialize(inData):
    total = 0
    memPos = []
    memVal = []
    for line in inData:
        (bitmask, memPos, memVal) = parseLine(line, memPos, memVal)
    for val in memVal:
        total += val
    return total