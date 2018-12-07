# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

dep = []
for y in range(26):
    dep.append([])
    for x in range(26):
        dep[y].append(0)

for line in file:
    line = line.split()
    origin = ord(line[1])-65
    destination = ord(line[7])-65
    dep[destination][origin] = 1

# Implementation
def part1(dep):
    result = ""
    while(1):
        for i in range(len(dep)):
            if(sum(dep[i]) == 0 and chr(i+65) not in result):
                result += chr(i+65)
                for j in range(len(dep)):
                    dep[j][i] = 0
                break
        if(len(result) == len(dep)):
            return result

def part2(dep):
    workers = [[None,0], [None,0], [None,0], [None,0], [None,0]]
    result = ""
    inprog = []
    seconds = 0
    while(1):
        new = False
        # assign step to a worker
        for i in range(len(dep)):
            if(sum(dep[i]) == 0 and
               chr(i+65) not in inprog and
               chr(i+65) not in result):
                for w in range(len(workers)):
                    if(workers[w][0] == None):
                        workers[w][0] = chr(i+65)
                        workers[w][1] = i+61
                        inprog.append(chr(i+65))
                        new = True
                        break
                break
        if(not new):
            # count up seconds
            seconds += 1
            for w in range(len(workers)):
                if(workers[w][0] == None): continue
                workers[w][1] -= 1
                if(workers[w][1] == 0):
                    # done
                    for j in range(len(dep)):
                        dep[j][ord(workers[w][0])-65] = 0
                    result += workers[w][0]
                    inprog.remove(workers[w][0])
                    workers[w] = [None, 0]
            
        if(len(result) == len(dep)):
            return seconds

# Processing
result1 = part1(aoc.copyList(dep))
result2 = part2(aoc.copyList(dep))

# Output
aoc.output(result1, result2)
