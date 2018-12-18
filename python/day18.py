# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

area = {}
height = len(file)
width = len(file[0])
for y in range(height):
    for x in range(width):
        area[(x,y)] = file[y][x]

# Implementation
def a(x,y):
    if((x,y) in area):
        return area[(x,y)]
    return "."

def resourceValues():
    trees, lumberyards = 0, 0
    for y in range(height):
        for x in range(width):
            if(a(x,y) == "|"): trees += 1
            if(a(x,y) == "#"): lumberyards += 1
    return trees * lumberyards

def count(x,y,acre):
    result = 0
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if(dy == 0 and dx == 0): continue
            if(a(x+dx,y+dy) == acre):
                result += 1
    return result

def part1n2(input1, input2):
    global area
    checksums = {}
    result1 = None
    i = 0
    while(i < input2):
        cur = {}
        checksum = ""
        for y in range(height):
            for x in range(width):
                acre = a(x,y)
                if(acre == "."):
                    if(count(x,y,"|") >= 3):
                        cur[(x,y)] = "|"
                    else:
                        cur[(x,y)] = "."
                elif(acre == "|"):
                    if(count(x,y,"#") >= 3):
                        cur[(x,y)] = "#"
                    else:
                        cur[(x,y)] = "|"
                else:
                    if(count(x,y,"#") >= 1 and
                       count(x,y,"|") >= 1):
                        cur[(x,y)] = "#"
                    else:
                        cur[(x,y)] = "."
                checksum += cur[(x,y)]
        area = cur
        
        checksum = aoc.hashSHA1(checksum)
        if(checksum in checksums):
            cycle = i - checksums[checksum]
            i = i + ((input2-i)//cycle)*cycle
        checksums[checksum] = i
        
        i += 1

        if(i == input1):
            result1 = resourceValues()
    return [result1, resourceValues()]

# Processing
[result1, result2] = part1n2(10, 10**9)

# Output
aoc.output(result1, result2)
