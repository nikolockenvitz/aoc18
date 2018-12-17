# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

mx, my = [None, None], [None, None] # min, max
ground = {}
for line in file:
    line = line.split(", ")
    if(line[0][0] == "x"):
        x = int(line[0].split("=")[1])
        for y in range(int(line[1].split("=")[1].split(".")[0]), int(line[1].split("..")[1])+1):
            ground[(x,y)] = "#"
            if(my[0] == None or my[0] > y): my[0] = y
            if(my[1] == None or my[1] < y): my[1] = y
        if(mx[0] == None or mx[0] > x): mx[0] = x
        if(mx[1] == None or mx[1] < x): mx[1] = x
            
    else:
        y = int(line[0].split("=")[1])
        for x in range(int(line[1].split("=")[1].split(".")[0]), int(line[1].split("..")[1])+1):
            ground[(x,y)] = "#"
            if(mx[0] == None or mx[0] > x): mx[0] = x
            if(mx[1] == None or mx[1] < x): mx[1] = x
        if(my[0] == None or my[0] > y): my[0] = y
        if(my[1] == None or my[1] < y): my[1] = y
mx = [mx[0]-1, mx[1]+1]

def show(spring=[500,0]):
    for y in range(min(my[0],spring[1]),max(my[1],spring[1])+1):
        line = ""
        for x in range(min(mx[0],spring[0]), max(mx[1],spring[0])+1):
            if(x == spring[0] and y == spring[1]):
                line += "+"
            elif((x,y) in ground):
                line += ground[(x,y)]
            else:
                line += "."
        print(line)

def g(x,y):
    if(x == 500 and y == 0):
        return "+"
    if((x,y) in ground):
        return ground[(x,y)]
    return "."

# Implementation
def fillRow(x,y):
    left = x
    while(1):
        left -= 1
        if(g(left,y) == "#"): break
        if(g(left,y+1) in "|."): break

    right = x
    while(1):
        right += 1
        if(g(right,y) == "#"): break
        if(g(right,y+1) in "|."): break

    if(g(left,y) == "#" and g(right,y) == "#"):
        # fill with ~
        for cx in range(left+1,right):
            ground[(cx,y)] = "~"
    else:
        # fill with |
        for cx in range(left+1,right):
            ground[(cx,y)] = "|"
    return [left if g(left,y) != "#" else None,
            right if g(right,y) != "#" else None]

def createWater():
    spring = [500, 0]
    x = spring[0]
    y = spring[1]+1
    springs = []
    while(1):
        if([x,y] in springs):
            springs.remove([x,y])
        if(g(x,y) == "."):
            ground[(x,y)] = "|"
            y += 1
            if(y > my[1]):
                if(springs == []): break
                [x,y] = springs[0]
                springs = springs[1:]
        elif(g(x,y) in "#~"):
            while(1):
                y -= 1
                rv = fillRow(x,y)
                if(rv[0] != None):
                    springs.append([rv[0],y])
                if(rv[1] != None):
                    springs.append([rv[1],y])
                if(rv[0] != None or rv[1] != None):
                    break

            if(springs == []): break
            [x,y] = springs[0]
            springs = springs[1:]
        elif(g(x,y) in "|"):
            if(springs == []): break
            [x,y] = springs[0]
            springs = springs[1:]

def countWater():
    result1 = 0
    result2 = 0
    for key in ground.keys():
        if(my[0] <= key[1] <= my[1]):
            if(ground[key] == "~"):
                result1 += 1
                result2 += 1
            if(ground[key] == "|"):
                result1 += 1
    return [result1, result2]

# Processing
createWater()
[result1, result2] = countWater()

# Output
aoc.output(result1, result2)
