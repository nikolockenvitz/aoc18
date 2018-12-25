# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

constellations = []
for line in file:
    constellations.append([[int(x) for x in line.split(",")]])

# Implementation
def distance(a, b):
    result = 0
    for i in range(4):
        result += abs(a[i] - b[i])
    return result

def part1():
    def mergeConstellations():
        for i in range(len(constellations)-1):
            for j in range(i+1,len(constellations)):
                for ki in range(len(constellations[i])):
                    for kj in range(len(constellations[j])):
                        if(distance(constellations[i][ki], constellations[j][kj]) <= 3):
                            constellations[i] += aoc.copyList(constellations[j])
                            del constellations[j]
                            return True
        return False

    while(1):
        if(mergeConstellations() == False): break
    return len(constellations)

def part2():
    result = 0
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
