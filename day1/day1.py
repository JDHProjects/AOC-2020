def addToTwo(inData):
    for i in inData:
        for j in inData:
            if j + i == 2020:
                return j*i

def addToThree(inData):
    for i in inData:
        for j in inData:
            for k in inData:
                if j + i + k == 2020:
                    return j*i*k