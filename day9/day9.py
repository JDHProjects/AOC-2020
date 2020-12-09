def findIncorrectNum(inData, preamble):
    for i in range(preamble, len(inData)):
        if(not sumValInPreamble(inData[i-preamble:i],inData[i])):
            return inData[i]
    return -1

def sumValInPreamble(preamble, val):
    for i in range(0,len(preamble)):
        current = preamble[i]
        preamble[i] = "null"
        if(preamble.count(val-current) > 0):
            return True
        preamble[i] = current
    return False

def findValFromRange(inData, val): 
    for i in range(0, len(inData)):
        contList = []
        offset = 0
        while (sum(contList) < val):
            contList.append(inData[i+offset])
            if(sum(contList) == val):
                return max(contList) + min(contList)
            else:
                offset += 1