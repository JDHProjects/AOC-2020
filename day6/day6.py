def groupParse(lineToParse):
    questionID = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    answers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0, len(questionID)):
        if (questionID[i] in lineToParse):
            answers[i] = 1
    return answers

def groupUnanimousParse(lineToParse):
    questionID = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    answers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    numInGroup = len(lineToParse.split("\n"))
    for i in range(0, len(questionID)):
        qTotal = lineToParse.count(questionID[i])
        answers[i] = 1 if qTotal == numInGroup else 0
    return answers

def sumAnswers(inData):
    total = 0
    for line in inData:
        total += sum(groupParse(line))
    return total

def sumUnanimousAnswers(inData):
    total = 0
    for line in inData:
        total += sum(groupUnanimousParse(line))
    return total