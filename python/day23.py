# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

bots = []
for line in file:
    cur = [int(x) for x in line.split("<")[1].split(">")[0].split(",")]
    cur.append(int(line.split("r=")[1]))
    bots.append(cur)

# Implementation
def part1():
    maxi = [None, None, None, None] # x, y, z, radius
    for bot in bots:
        if(maxi[3] == None or bot[3] > maxi[3]):
            maxi = aoc.copyList(bot)

    result = 0
    for bot in bots:
        d = abs(maxi[0] - bot[0]) + abs(maxi[1] - bot[1]) + abs(maxi[2] - bot[2])
        if(d <= maxi[3]):
            result += 1
    return result
        
def part2():
    maxi = [None, 0,0,0] # number of bots, x, y, z
    for bot1 in bots:
        numberOfBots = 0
        for bot2 in bots:
            d = abs(bot1[0] - bot2[0]) + abs(bot1[1] - bot2[1]) + abs(bot1[2] - bot2[2])
            if(d <= bot2[3]):
                numberOfBots += 1
        if(maxi[0] == None or numberOfBots > maxi[0]):
            maxi = [numberOfBots, bot1[0], bot1[1], bot1[2], abs(bot1[0])+abs(bot1[1])+abs(bot1[2])]

    size = 10000
    stepsize = size//10
    while(1):
        foundBetterSolution = False
        for dx in range(-size,size+1,stepsize):
            for dy in range(-size,size+1,stepsize):
                for dz in range(-size,size+1,stepsize):
                    numberOfBots = 0
                    for bot in bots:
                        d = abs(maxi[1]+dx - bot[0]) + abs(maxi[2]+dy - bot[1]) + abs(maxi[3]+dz - bot[2])
                        if(d <= bot[3]):
                            numberOfBots += 1
                    distanceToOrigin = abs(maxi[1]+dx) + abs(maxi[2]+dy) + abs(maxi[3]+dz)
                    if(numberOfBots > maxi[0] or (numberOfBots == maxi[0] and distanceToOrigin < maxi[4])):
                        foundBetterSolution = True
                        maxi = [numberOfBots, maxi[1]+dx, maxi[2]+dy, maxi[3]+dz, distanceToOrigin]
        if(not foundBetterSolution):
            if(stepsize == 1): break
            size = size//10
            stepsize = size//10
    return maxi[4]

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
