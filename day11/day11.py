from copy import deepcopy

def inputToList(inData):
    return list(map(list,inData))

def stabilizeSeats(layoutOne,part2=False):
    layoutTwo = checkAllSeats(layoutOne,part2)
    flipflop = False
    while (layoutOne != layoutTwo):
        if(flipflop):
            layoutTwo = checkAllSeats(layoutOne,part2)
        else:
            layoutOne = checkAllSeats(layoutTwo,part2)
        flipflop = not flipflop
    return layoutOne

def countOccupied(layout):
    count = 0
    for y in range(0,len(layout)):
        for x in range(0,len(layout[y])):
            if(layout[y][x] == "#"):
                count += 1
    return count

def checkAllSeats(layout,part2=False):
    newLayout = []
    for y in range(0,len(layout)):
        newLayoutRow = []
        for x in range(0,len(layout[y])):
            if(part2):
                current = checkFarSeat(layout,x,y)
            else:
                current = checkSeat(layout,x,y)
            if(layout[y][x] != "."):
                if (current):
                    newLayoutRow.append("#")
                else:
                    newLayoutRow.append("L")
            else:
                newLayoutRow.append(".")
        newLayout.append(newLayoutRow)
    return newLayout

def checkSeat(layout, x, y):
    chairCount = 0
    if(x>0):
        if(y>0):
            chairCount += 1 if layout[y-1][x-1] == "#" else 0
        chairCount += 1 if layout[y][x-1] == "#" else 0
        if(y<len(layout)-1):
            chairCount += 1 if layout[y+1][x-1] == "#" else 0

    if(y>0):
        chairCount += 1 if layout[y-1][x] == "#" else 0
    if(y<len(layout)-1):
        chairCount += 1 if layout[y+1][x] == "#" else 0

    if(x<len(layout[y])-1):
        if(y>0):
            chairCount += 1 if layout[y-1][x+1] == "#" else 0
        chairCount += 1 if layout[y][x+1] == "#" else 0
        if(y<len(layout)-1):
            chairCount += 1 if layout[y+1][x+1] == "#" else 0

    if(layout[y][x] == "L" and chairCount == 0):
        return True
    elif(layout[y][x] == "#" and chairCount < 4):
        return True
    return False

def checkFarSeat(layout, x, y):
    chairCount = 0

    chairCount += checkAdj(layout,x,y,1,0)
    chairCount += checkAdj(layout,x,y,-1,0)
    chairCount += checkAdj(layout,x,y,0,1)
    chairCount += checkAdj(layout,x,y,0,-1)

    chairCount += checkAdj(layout,x,y,1,1)
    chairCount += checkAdj(layout,x,y,1,-1)
    chairCount += checkAdj(layout,x,y,-1,1)
    chairCount += checkAdj(layout,x,y,-1,-1)
   
    if(layout[y][x] == "L" and chairCount == 0):
        return True
    elif(layout[y][x] == "#" and chairCount < 5):
        return True
    return False

def checkAdj(layout, x, y, incX, incY):
    if (y + incY < 0 or y + incY >= len(layout)):
        return 0 
    elif (x + incX < 0 or x + incX >= len(layout[y])):
        return 0
    current = layout[y+incY][x+incX]
    if(current == "L"):
        return 0
    elif(current == "#"):
        return 1

    return checkAdj(layout, x+incX, y+incY, incX, incY)
