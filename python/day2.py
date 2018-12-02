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
    letter2Times = 0
    letter3Times = 0
    for line in file:
        cur2 = False
        cur3 = False
        for letter in line:
            n = line.count(letter)
            if(n == 2):
                cur2 = True
            elif(n == 3):
                cur3 = True
            if(cur2 and cur3):
                break
        if(cur2):
            letter2Times += 1
        if(cur3):
            letter3Times += 1
    checksum = letter2Times * letter3Times
    return checksum

def part2():
    for i in range(len(file)-1):
        for j in range(i+1, len(file)):
            # compare file[i] and file[j]
            diff = 0
            for k in range(len(file[i])):
                if(file[i][k] != file[j][k]):
                    diff += 1
                    if(diff > 1): break
            if(diff == 1):
                result = ""
                for k in range(len(file[i])):
                    if(file[i][k] == file[j][k]):
                        result += file[i][k]
                return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
