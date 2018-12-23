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
    result = 0
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
