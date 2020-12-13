def parseBuses(inData):
    buses = []
    for bus in inData[1].split(","):
        if bus != "x":
            buses.append(int(bus))
    return (int(inData[0]), buses)

def getNextBus(time, buses):
    arrival = []
    for bus in buses:
        arrival.append(bus - (time % bus))
    return (buses[arrival.index(min(arrival))],min(arrival))