# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile()

# Implementation
def part1(polymer):
    i = 0
    while(1):
        if(i > len(polymer) - 2):
            return len(polymer)

        if(polymer[i].lower() == polymer[i+1].lower() and
           polymer[i] != polymer[i+1]):
            polymer = polymer[:i] + polymer[i+2:]
            i = max(0, i-1)
        else:
            i += 1

def part2(polymer):
    mini = None
    for unit in "abcdefghijklmnopqrstuvwxyz":
        curPolymer = polymer
        i = 0
        while(1):
            if(i > len(curPolymer) - 1):
                break
            if(curPolymer[i].lower() == unit):
                curPolymer = curPolymer[:i] + curPolymer[i+1:]
            else:
                i += 1

        length = part1(curPolymer)
        if(mini == None or mini > length):
            mini = length
        
    return mini

# Processing
result1 = part1(file)
result2 = part2(file)

# Output
aoc.output(result1, result2)
