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
records = {}
mini = None
maxi = None
for line in file:
    line = line.split("] ")
    timestamp = int("".join(re.findall("\d+", line[0])))
    records[timestamp] = line[1]

    if(mini == None): mini = timestamp
    else: mini = min(timestamp, mini)
    if(maxi == None): maxi = timestamp
    else: maxi = max(timestamp, maxi)

curTime = mini
guards = {}
awake = False
curGuard = None
while(curTime <= maxi):
    if(curTime in records):
        if(records[curTime][:5] == "Guard"):
            curGuard = re.findall("\d+", records[curTime])[0]
            awake = True
            if(curGuard not in guards.keys()):
                guards[curGuard] = [0]*60
        elif(records[curTime][:5] == "wakes"):
            awake = True
        elif(records[curTime][:5] == "falls"):
            awake = False
    if(curTime % 10000 < 60):
        if(not awake):
            guards[curGuard][curTime%10000] += 1
    curTime += 1

def part1():
    maxi = [None, None]
    for guard in guards.keys():
        if(maxi[0] == None or maxi[0] < sum(guards[guard])):
            maxi = [sum(guards[guard]), guard]

    t = guards[maxi[1]]
    for i in range(len(t)):
        if(t[i] == max(t)):
            return i * int(maxi[1])

def part2():
    maxi = [None, None]
    for guard in guards.keys():
        curMax = max(guards[guard])
        if(maxi[0] == None or maxi[0] < curMax):
            maxi = [curMax, guard]

    for i in range(60):
        if(guards[maxi[1]][i] == maxi[0]):
            return i * int(maxi[1])

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
