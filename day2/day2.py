def lineParse(inString):
    stringList = inString.split(":")
    infoList = stringList[0].split(" ")
    rangeList = infoList[0].split("-")
    
    lower = int(rangeList[0])
    upper = int(rangeList[1])
    character = infoList[1]
    password = stringList[1].strip()

    return [lower,upper,character,password]


def getValidPasswordsPart1(inData):
    validPasswords = []
    for i in inData:
        line = lineParse(i)
        charCount = line[3].count(line[2])
        if(charCount >= line[0] and charCount <= line[1]):
            validPasswords.append(line[3])
    return validPasswords

def getValidPasswordsPart2(inData):
    validPasswords = []
    for i in inData:
        line = lineParse(i)

        if(bool(line[2] == line[3][line[0]-1]) ^ bool(line[2] == line[3][line[1]-1])):
            validPasswords.append(line[3])
    return validPasswords

