# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()
depth = int(file[0].split(": ")[1])
target = [int(x) for x in file[1].split(": ")[1].split(",")]

cave = {} # (x,y): erosion level

# Implementation
def getGeologicIndex(x,y):
    if(x == 0 and y == 0):
        return 0
    if(x == target[0] and y == target[1]):
        return 0
    if(y == 0):
        return x * 16807
    if(x == 0):
        return y * 48271
    return cave[(x-1,y)] * cave[(x,y-1)]

def getErosionLevel(x,y):
    return (getGeologicIndex(x,y) + depth) % 20183

def part1():
    for y in range(target[1]+1000):
        for x in range(target[0]+1000):
            cave[(x,y)] = getErosionLevel(x,y)

    riskLevel = 0
    for y in range(target[1]+1):
        for x in range(target[0]+1):
            riskLevel += cave[(x,y)] % 3
    return riskLevel

class QueueElement:
    def __init__(self, x, y, tool, distance):
        self.x = x
        self.y = y
        self.tool = tool
        self.distance = distance
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.first = None

    def insert(self, x, y, tool, distance):
        new = QueueElement(x,y,tool,distance)
        if(self.first == None):
            self.first = new
        elif(new.distance < self.first.distance):
            new.next = self.first
            self.first = new
        else:
            cur = self.first
            while(1):
                if(new.distance < cur.distance): break
                last = cur
                if(cur.next == None):
                    cur.next = new
                    return
                if(cur.x == new.x and
                   cur.y == new.y and
                   cur.tool == new.tool):
                    return
                cur = cur.next
            new.next = cur
            last.next = new

    def extractMin(self):
        if(self.first == None): return None
        cur = self.first
        self.first = self.first.next
        return [cur.x, cur.y, cur.tool, cur.distance]

def getPossibleRegions(x,y,tool,distance):
    regions = []
    for d in [[0,-1], [-1,0], [1,0], [0,1]]:
        if(x+d[0] < 0 or y+d[1] < 0): continue
        t = cave[(x+d[0], y+d[1])] % 3
        if((t == 0 and tool == "neither") or
           (t == 1 and tool == "torch") or
           (t == 2 and tool == "climbing gear")):
            continue
        regions.append((x+d[0], y+d[1], tool, distance+1))
    for newtool in ["neither","torch","climbing gear"]:
        if(tool == newtool): continue
        t = cave[(x, y)] % 3
        if((t == 0 and newtool == "neither") or
           (t == 1 and newtool == "torch") or
           (t == 2 and newtool == "climbing gear")):
            continue
        regions.append((x, y, newtool, distance+7))
    return regions


def part2():
    d = { (x,y,"torch"): 0 }
    q = PriorityQueue()
    for r in getPossibleRegions(0,0,"torch",0):
        if((r[0],r[1],r[2]) not in d):
            q.insert(r[0],r[1],r[2],r[3])

    while(1):
        while(1):
            cur = q.extractMin()
            if(cur == None): return
            if((cur[0],cur[1],cur[2]) not in d):
                d[(cur[0],cur[1],cur[2])] = cur[3]
                if(cur[0] == target[0] and
                   cur[1] == target[1] and
                   cur[2] == "torch"):
                    return cur[3]
                break

        for r in getPossibleRegions(cur[0],cur[1],cur[2],cur[3]):
            if((r[0],r[1],r[2]) not in d):
                q.insert(r[0],r[1],r[2],r[3])

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
