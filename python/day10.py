# Import and Setup
from time import sleep
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

# Implementation
def part1n2():
    points = []
    for line in file:
        point = [0,0,0,0]
        point[0] = int(line.split("position=<")[1].split(",")[0])
        point[1] = int(line.split(", ")[1].split(">")[0])
        point[2] = int(line.split("velocity=<")[1].split(",")[0])
        point[3] = int(line.split(", ")[2].split(">")[0])
        points.append(point)

    seconds = 0
    while(1):
        d = {}
        for i in range(len(points)):
            points[i][0] += points[i][2]
            points[i][1] += points[i][3]
            d[(points[i][0],points[i][1])] = 1
        seconds += 1

        for i in range(len(points)):
            if((points[i][0],points[i][1]+1) in d.keys() and
               (points[i][0],points[i][1]+2) in d.keys() and
               (points[i][0],points[i][1]+3) in d.keys() and
               (points[i][0],points[i][1]+4) in d.keys() and
               (points[i][0],points[i][1]+5) in d.keys() and
               (points[i][0],points[i][1]+6) in d.keys() and
               (points[i][0],points[i][1]+7) in d.keys()):
                for y in range(-4,12):
                    line = ""
                    for x in range(-20,60):
                        cur = (points[i][0]+x,points[i][1]+y)
                        if(cur in d.keys()):
                            line += "#"
                        else:
                            line += "."
                    print(line)
                return ["please read text above", seconds]

# Processing
[result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
