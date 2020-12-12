allDirs = ["N","E","S","W"]
dirChange = [[0,1],[1,0],[0,-1],[-1,0]]
waypointOrient = [[-1,1],[1,1],[1,-1],[-1,-1]]

def getNewDir(degree,current):
    return allDirs[int((allDirs.index(current)+degree)%4)]

def getManhattanDistance(x1, y1, x2, y2):
    return abs(abs(x1)-abs(x2)+abs(y1)-abs(y2))

def moveObject(comVal,direction,x,y,originX,originY):
    command = comVal[0]
    value = int(comVal[1:])
    if(command == "L"):
        return rotateObject(direction,-value,x,y,originX,originY)+(originX,originY)
    if(command == "R"):
        
        return rotateObject(direction,value,x,y,originX,originY)+(originX,originY)
    if (x == originX and y == originY):
        if(command == "F"):
            newDir = direction
        else:
            newDir = command
        dirMultiplier = dirChange[allDirs.index(newDir)]
        newX = x + (value * dirMultiplier[0])
        newY = y + (value * dirMultiplier[1])
        return (direction, newX, newY, newX, newY)
    else:
        if(command == "F"):
            xDiff = x - originX
            yDiff = y - originY
            newX = x + (value * xDiff)
            newY = y + (value * yDiff)

            return (checkDir(xDiff,yDiff,direction), newX, newY, newX-xDiff, newY-yDiff)
        else:
            newDir = command
            dirMultiplier = dirChange[allDirs.index(newDir)]
            newX = x + (value * dirMultiplier[0])
            newY = y + (value * dirMultiplier[1])
            return (checkDir(newX-originX,newY-originY,direction), newX, newY, originX, originY)

def checkDir(xDiff, yDiff, direction):
    if(xDiff>=0 and yDiff>=0 and direction != "E"):
        return "E"
    if(xDiff>=0 and yDiff<0 and direction != "S"):
        return "S"
    if(xDiff<0 and yDiff<0 and direction != "W"):
        return "W"
    if(xDiff<0 and yDiff>=0 and direction != "N"):
        return "N"
    return direction

def rotateObject(direction, degree, x, y, originX, originY):
    value = degree / 90

    x = abs(x - originX)
    y = abs(y - originY)
    
    if((value % 2) != 0):
        x, y = y, x

    newDirection = getNewDir(value,direction)

    orient = waypointOrient[allDirs.index(newDirection)]
    return (newDirection, x * orient[0] + originX, y * orient[1] + originY)

def moveBoatThroughPath(path,x,y,originX,originY,noWaypoint=True):
    direction = "E"
    for move in path:
        (direction,x,y,originX,originY) = moveObject(move, direction, x, y, originX, originY)
    return (originX,originY)



