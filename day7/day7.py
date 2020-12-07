import re
def bagParse(lineToParse):
    bagsList = [["",0]]
    bagRegex = re.compile(r'\d+\D+bag')
    lineList = lineToParse.split("contain")
    
    bagsList[0][0] = lineList[0].replace(" bags ","")
    containedBags = bagRegex.findall(lineList[1])

    count = 0
    for bag in containedBags:
        count += int(bag[0])
        bagsList.append([bag[1:].replace(" bag", "").strip(" "),int(bag[0])])
    bagsList[0][1] = count
    return bagsList

def generateRules(inData):
    rules = []
    for line in inData:
        parsed = bagParse(line)
        rules.append(parsed)
    return rules

def simplifyRules(rules):
    simpleRules = []
    for rule in rules:
        simpleRule = []
        for bag in rule:
            simpleRule.append(bag[0])
        simpleRules.append(simpleRule)
    return simpleRules

def countBagsReccur(rules, bag):
    acceptedRules = set()
    for rule in rules:
        if (len(rule) > 1):
            if (bag in rule[1:]):
                acceptedRules.add(rules.index(rule))
                acceptedRules.update(countBagsReccur(rules, rule[0]))

    return acceptedRules

def countBags(rules, bag):
    return len(countBagsReccur(simplifyRules(rules), bag))

def bagsInBagsReccur(rules, bag):
    count = 1
    for rule in rules:
        if (bag == rule[0][0]):
            if (len(rule) > 1):
                for i in range(1,len(rule)):
                    bagCount = bagsInBagsReccur(rules, rule[i][0])
                    count+= rule[i][1] * bagCount
            else:
                return 1

    return count
    
def bagsInBags(rules, bag):
    return bagsInBagsReccur(rules, bag) -1