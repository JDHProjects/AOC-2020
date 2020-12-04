import re

def dictParse(lineToParse):
    valDict = {"byr":"","iyr":"","eyr":"","hgt":"","hcl":"","ecl":"","pid":"","cid":""}
    keyval = lineToParse.replace("\n"," ").split(" ")
    for pair in keyval:
        splitPair = pair.split(":")
        if (splitPair[0] in valDict):
            valDict[splitPair[0]]=splitPair[1]
    return valDict

def checkPassports(inData):
    validPassports = []
    for line in inData:
        lineDict = dictParse(line)
        valid = True
        for key, val in lineDict.items():
            if(val == "" and key != "cid"):
                valid = False
        if(valid):
            validPassports.append(lineDict)
    return validPassports

def strictCheckPassports(inData):
    hcl = re.compile('#[a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9][a-f0-9]')
    ecl = ["amb","blu","brn","gry","grn","hzl","oth"]
    pid = re.compile('\\d\\d\\d\\d\\d\\d\\d\\d\\d')
    validPassports = []
    for line in inData:
        lineDict = dictParse(line)
        valid = True
        try:
            for key, val in lineDict.items():
                if(key == "byr" and (int(val)<1920 or int(val)>2002)):
                    valid = False
                elif(key == "iyr" and (int(val)<2010 or int(val)>2020)):
                    valid = False
                elif(key == "eyr" and (int(val)<2020 or int(val)>2030)):
                    valid = False
                elif(key == "hgt"):
                    unit = val[-2:]
                    value = val[:-2]
                    if(unit == "cm" and (int(value)<150 or int(value)>193)):
                        valid = False
                    elif(unit == "in" and (int(value)<59 or int(value)>76)):
                        valid = False
                    elif (unit != "cm" and unit != "in"):
                        valid = False
                elif(key == "hcl" and (hcl.match(val) == None or len(val) != 7)):
                    valid = False
                elif(key == "ecl" and val not in ecl):
                    valid = False
                elif(key == "pid" and (pid.match(val) == None or len(val) != 9)):
                    valid = False
        except:
            valid = False


        if(valid):
            validPassports.append(lineDict)
    return validPassports