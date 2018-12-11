# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
serialNumber = int(aoc.getFile())

# Implementation
def part1n2():
    cells = []
    maxi = [0, -1, -1] # max totalpower, x, y
    for y in range(300):
        cells.append([])
        for x in range(300):
            xcoord = x + 1
            ycoord = y + 1
            rackid = xcoord + 10
            powerlevel = rackid * ycoord
            powerlevel+= serialNumber
            powerlevel*= rackid
            powerlevel = (powerlevel%1000)//100
            powerlevel-= 5
            cells[y].append(powerlevel)
            if(y > 2 and x > 2):
                totalpower = 0
                for dx in range(3):
                    for dy in range(3):
                        totalpower += cells[y-dy][x-dx]
                if(totalpower > maxi[0]):
                    maxi = [totalpower, x-1, y-1]
    result1 = str(maxi[1]) + "," + str(maxi[2])

    maxi = [0, -1, -1, 0] # max totalpower, x, y, square-size
    for y in range(300):
        for x in range(300):
            totalpower = 0
            for size in range(1,301-max(x,y)):
                for dy in range(size):
                    totalpower += cells[y+dy][x+size-1]
                for dx in range(size-1):
                    totalpower += cells[y+size-1][x+dx]
                if(totalpower > maxi[0]):
                    maxi = [totalpower, x+1, y+1, size]
    
    result2 = "{},{},{}".format(maxi[1],maxi[2],maxi[3])
    return [result1, result2]

# Processing
[result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
