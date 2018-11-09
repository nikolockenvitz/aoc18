# Import and Setup
import os
import re

from aoc import *
DAY = int(re.findall("\d+", os.path.basename(__file__))[0])
aoc = AOC(DAY)

# Initialization
resultA = None
resultB = None

# Input
file = aoc.getFile()

# Implementation
def part1():
    result = 0
    return result

def part2():
    result = 0
    return result

# Processing
resultA = part1()
resultB = part2()

# Output
aoc.output(resultA, resultB)
