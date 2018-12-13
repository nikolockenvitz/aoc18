# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

track = []
for y in range(len(file)):
    track.append([])
    for x in range(len(file[y])):
        track[y].append([file[y][x]])

numCarts = 0
for y in range(len(track)):
    for x in range(len(track[y])):
        if(track[y][x][0] == "<"):
            track[y][x] = ["-","<",0,-1]
            numCarts += 1
        elif(track[y][x][0] == "^"):
            track[y][x] = ["|","^",0,-1]
            numCarts += 1
        elif(track[y][x][0] == ">"):
            track[y][x] = ["-",">",0,-1]
            numCarts += 1
        elif(track[y][x][0] == "v"):
            track[y][x] = ["|","v",0,-1]
            numCarts += 1

# Implementation
def show(t):
    for line in t:
        p = ""
        for el in line:
            if(len(el) > 1):
                p += el[1]
            else:
                p += el[0]
        print(p)

def part1n2():
    global numCarts
    tick = 0
    result1 = ""
    while(1):
        for y in range(len(track)):
            for x in range(len(track[y])):
                if(len(track[y][x]) > 1 and track[y][x][3] != tick):
                    cart = track[y][x][1]
                    if(cart == "^"):
                        if(len(track[y-1][x]) > 1):
                            if(result1 == ""):
                                result1 = "{},{}".format(x,y-1)
                            track[y][x] = track[y][x][:1]
                            track[y-1][x] = track[y-1][x][:1]
                            numCarts -= 2
                            continue
                        if(track[y-1][x][0] == "|"):
                            track[y-1][x].append("^")
                        elif(track[y-1][x][0] == "/"):
                            track[y-1][x].append(">")
                        elif(track[y-1][x][0] == "\\"):
                            track[y-1][x].append("<")
                        elif(track[y-1][x][0] == "+"):
                            if(track[y][x][2] == 0):
                                track[y-1][x].append("<")
                            elif(track[y][x][2] == 1):
                                track[y-1][x].append("^")
                            elif(track[y][x][2] == 2):
                                track[y-1][x].append(">")
                            track[y][x][2] = (track[y][x][2]+1)%3
                        track[y-1][x].append(track[y][x][2])
                        track[y-1][x].append(tick)
                        track[y][x] = track[y][x][:1]

                    elif(cart == ">"):
                        if(len(track[y][x+1]) > 1):
                            if(result1 == ""):
                                result1 = "{},{}".format(x+1,y)
                            track[y][x] = track[y][x][:1]
                            track[y][x+1] = track[y][x+1][:1]
                            numCarts -= 2
                            continue
                        if(track[y][x+1][0] == "-"):
                            track[y][x+1].append(">")
                        elif(track[y][x+1][0] == "/"):
                            track[y][x+1].append("^")
                        elif(track[y][x+1][0] == "\\"):
                            track[y][x+1].append("v")
                        elif(track[y][x+1][0] == "+"):
                            if(track[y][x][2] == 0):
                                track[y][x+1].append("^")
                            elif(track[y][x][2] == 1):
                                track[y][x+1].append(">")
                            elif(track[y][x][2] == 2):
                                track[y][x+1].append("v")
                            track[y][x][2] = (track[y][x][2]+1)%3
                        track[y][x+1].append(track[y][x][2])
                        track[y][x+1].append(tick)
                        track[y][x] = track[y][x][:1]

                    elif(cart == "v"):
                        if(len(track[y+1][x]) > 1):
                            if(result1 == ""):
                                result1 = "{},{}".format(x,y+1)
                            track[y][x] = track[y][x][:1]
                            track[y+1][x] = track[y+1][x][:1]
                            numCarts -= 2
                            continue
                        if(track[y+1][x][0] == "|"):
                            track[y+1][x].append("v")
                        elif(track[y+1][x][0] == "/"):
                            track[y+1][x].append("<")
                        elif(track[y+1][x][0] == "\\"):
                            track[y+1][x].append(">")
                        elif(track[y+1][x][0] == "+"):
                            if(track[y][x][2] == 0):
                                track[y+1][x].append(">")
                            elif(track[y][x][2] == 1):
                                track[y+1][x].append("v")
                            elif(track[y][x][2] == 2):
                                track[y+1][x].append("<")
                            track[y][x][2] = (track[y][x][2]+1)%3
                        track[y+1][x].append(track[y][x][2])
                        track[y+1][x].append(tick)
                        track[y][x] = track[y][x][:1]

                    elif(cart == "<"):
                        if(len(track[y][x-1]) > 1):
                            if(result1 == ""):
                                result1 = "{},{}".format(x-1,y)
                            track[y][x] = track[y][x][:1]
                            track[y][x-1] = track[y][x-1][:1]
                            numCarts -= 2
                            continue
                        if(track[y][x-1][0] == "-"):
                            track[y][x-1].append("<")
                        elif(track[y][x-1][0] == "/"):
                            track[y][x-1].append("v")
                        elif(track[y][x-1][0] == "\\"):
                            track[y][x-1].append("^")
                        elif(track[y][x-1][0] == "+"):
                            if(track[y][x][2] == 0):
                                track[y][x-1].append("v")
                            elif(track[y][x][2] == 1):
                                track[y][x-1].append("<")
                            elif(track[y][x][2] == 2):
                                track[y][x-1].append("^")
                            track[y][x][2] = (track[y][x][2]+1)%3
                        track[y][x-1].append(track[y][x][2])
                        track[y][x-1].append(tick)
                        track[y][x] = track[y][x][:1]
        tick += 1
        if(numCarts == 1):
            result2 = ""
            for y in range(len(track)):
                for x in range(len(track[y])):
                    if(len(track[y][x])>1):
                        result2 = "{},{}".format(x,y)
                        return [result1, result2]

# Processing
[result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
