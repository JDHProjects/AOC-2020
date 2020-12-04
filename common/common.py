def loadData(folder, parseInt=False, splitChar="\n"):
    with open(folder+"/input.txt", "r") as file:
        values = file.read().split(splitChar)
    while("" in values):
        values.remove("")
    if parseInt:
        valuesInt = []
        for i in values:
            valuesInt.append(int(i))
        return valuesInt
    return values