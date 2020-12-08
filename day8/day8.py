from copy import deepcopy
def lineParse(lineToParse):
    splitList = lineToParse.split(" ")
    return [splitList[0], int(splitList[1])]

def instructionList(inData):
    instructions = []
    for line in inData:
        instructions.append(lineParse(line))
    return instructions

def runInfiniteProgram(instructions):
    pc = 0
    acc = 0
    while(instructions[pc][0] != "rep"):
        current = instructions[pc]
        if (current[0] == "acc"):
            acc += current[1]
        if (current[0] == "jmp"):
            pc += current[1]
        else:
            pc += 1
        current[0] = "rep"
    return acc
    
def runProgram(instructions):
    pc = 0
    acc = 0
    while(pc < len(instructions)):
        current = instructions[pc]
        if (current[0] == "rep"):
            return False
        if (current[0] == "acc"):
            acc += current[1]
        if (current[0] == "jmp"):
            pc += current[1]
        else:
            pc += 1
        current[0] = "rep"
    return acc

def fixProgram(instructions):
    jmpLoc = [index for index, value in enumerate(instructions) if value[0] == "jmp"]
    for i in jmpLoc:
        changedInstructions = deepcopy(instructions)
        changedInstructions[i][0] = "nop"
        output = runProgram(changedInstructions)
        if(output != False):
            return output
    return False
