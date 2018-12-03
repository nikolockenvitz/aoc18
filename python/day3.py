# Import and Setup
import re

from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

# Implementation
def part1():
    result = 0
    square = []
    n = 1000
    for y in range(n):
        square.append([])
        for x in range(n):
            square[y].append(0)

    for line in file:
        cur = re.findall("\d+", line)
        x = int(cur[1])
        y = int(cur[2])
        dx = int(cur[3])
        dy = int(cur[4])
        for ix in range(x, x+dx):
            for iy in range(y, y+dy):
                square[iy][ix] += 1

    for y in range(n):
        for x in range(n):
            if(square[y][x] > 1):
                result += 1

    return result

def part2():
    result = []
    for line in file:
        result.append(int(re.findall("\d+", line)[0]))

    square = []
    n = 1000
    for y in range(n):
        square.append([])
        for x in range(n):
            square[y].append([])

    for line in file:
        cur = re.findall("\d+", line)
        x = int(cur[1])
        y = int(cur[2])
        dx = int(cur[3])
        dy = int(cur[4])
        for ix in range(x, x+dx):
            for iy in range(y, y+dy):
                square[iy][ix].append(int(cur[0]))
                if(len(square[iy][ix]) > 1):
                    for element in square[iy][ix]:
                        if element in result:
                            result.remove(element)

    return result[0]

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
