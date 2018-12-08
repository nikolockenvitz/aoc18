# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile().split()
file = [ int(x) for x in file ]

# Implementation
def part1n2(ix=0):
    numberOfChilds = file[ix]
    numberOfMetadata = file[ix+1]
    sumMetadata = 0

    ix += 2
    value = 0
    values = [None]
    # childs
    for i in range(numberOfChilds):
        [ix, curSum, curValue] = part1n2(ix)
        sumMetadata += curSum
        values.append(curValue)
    # own metadata
    for i in range(ix, ix+numberOfMetadata):
        sumMetadata += file[i]
        if(numberOfChilds != 0 and
           file[i] >= 1 and file[i] < len(values)):
            value += values[file[i]]
    ix += numberOfMetadata
    if(numberOfChilds == 0):
        value = sumMetadata

    return [ix, sumMetadata, value]

# Processing
[ix, result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
