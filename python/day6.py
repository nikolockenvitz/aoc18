# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

maxi = 0
for i in range(len(file)):
    file[i] = file[i].split(", ")
    file[i][0] = int(file[i][0])
    file[i][1] = int(file[i][1])
    maxi = max(maxi, file[i][0], file[i][1])

# Implementation + Processing
result2 = 0

grid = []
n = maxi+1
for y in range(n):
    grid.append([])
    for x in range(n):
        mini = [None, None] # distance, point
        totaldistance = 0

        for i in range(len(file)):
            distance = abs(x - file[i][0]) + abs(y - file[i][1])
            if(mini[0] == None or mini[0] > distance):
                mini = [distance, i]
            elif(mini[0] == distance):
                mini = [distance, [mini[1]] + [i]]

            totaldistance += distance

        if(type(mini[1]) == list):
            mini[1] = None
        grid[y].append(mini[1])

        if(totaldistance < 10000):
            result2 += 1

points = []
for i in range(len(file)):
    points.append(0)

for y in range(n):
    for x in range(n):
        point = grid[y][x]
        if(point == None):
            continue
        if(y == 0 or x == 0 or y == n-1 or x == n-1):
            # points at the edge are infinite
            points[point] = None
            continue
        if(points[point] != None):
            points[point] += 1

for distance in points:
    if(distance == None): continue
    if(result1 == None or result1 < distance):
        result1 = distance

# Output
aoc.output(result1, result2)
