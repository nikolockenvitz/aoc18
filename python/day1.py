# Import and Setup
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
    frequency = 0
    for line in file:
        frequency += int(line)
    return frequency

def part2():
    lineIndex = 0
    currentFrequency = 0
    frequencies = {}
    while(1):
        currentFrequency += int(file[lineIndex%len(file)])
        if(currentFrequency in frequencies.keys()):
            return currentFrequency
        frequencies[currentFrequency] = True
        lineIndex += 1

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
