# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

state = file[0].split(": ")[1]
notes = file[2:]

pots = {}
for i in range(len(state)):
    if(state[i] == "#"):
        pots[i] = "#"

rules = {}
for line in notes:
    line = line.split(" => ")
    rules[line[0]] = line[1]

# Implementation
def part1n2(pots, generations):
    h = {}
    mini = -2
    maxi = 102
    for generation in range(1,generations+1):
        new = {}
        nmini = 0
        nmaxi = 0
        for i in range(mini-2,maxi+3):
            neighbors = ""
            for j in [-2,-1,0,1,2]:
                if((i+j) in pots.keys()):
                    neighbors += "#"
                else:
                    neighbors += "."
            r = rules[neighbors]
            if(r == "#"):
                nmini = min(mini,i)
                nmaxi = max(maxi,i)
                new[i] = "#"
        pots = new
        mini = nmini
        maxi = nmaxi
    result = sum(pots.keys())
    return result

# Processing
result1 = part1n2(pots, 20)
# after some time the sum increases linear
result2 = 2000000001684 #part1n2(pots, 50*10**9)

# Output
aoc.output(result1, result2)
