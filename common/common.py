def loadData(folder, parseInt=False):
    with open(folder+"/input.txt", "r") as file:
        values = file.read().splitlines()
    if parseInt:
        valuesInt = []
        for i in values:
            valuesInt.append(int(i))
        return valuesInt
    return values