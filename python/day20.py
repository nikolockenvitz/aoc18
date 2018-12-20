# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile()

area = {}
def a(x,y):
    if((x,y) in area):
        return area[(x,y)]
    return "#"

def show():
    mx, my = [None, None], [None, None]
    for k in area:
        if(mx[0] == None or mx[0] > k[0]): mx[0] = k[0]
        if(mx[1] == None or mx[1] < k[0]): mx[1] = k[0]
        if(my[0] == None or my[0] > k[1]): my[0] = k[1]
        if(my[1] == None or my[1] < k[1]): my[1] = k[1]
    for y in range(my[0],my[1]+1):
        line = ""
        for x in range(mx[0],mx[1]+1):
            line += a(x,y)
        print(line)

# Implementation
def move(direction, coords):
    cnew = []
    if(direction == "N"):
        for c in range(len(coords)):
            area[(coords[c][0],coords[c][1]-1)] = "-"
            area[(coords[c][0],coords[c][1]-2)] = "."
            cnew.append((coords[c][0],coords[c][1]-2))
    elif(direction == "E"):
        for c in range(len(coords)):
            area[(coords[c][0]+1,coords[c][1])] = "|"
            area[(coords[c][0]+2,coords[c][1])] = "."
            cnew.append((coords[c][0]+2,coords[c][1]))
    elif(direction == "S"):
        for c in range(len(coords)):
            area[(coords[c][0],coords[c][1]+1)] = "-"
            area[(coords[c][0],coords[c][1]+2)] = "."
            cnew.append((coords[c][0],coords[c][1]+2))
    elif(direction == "W"):
        for c in range(len(coords)):
            area[(coords[c][0]-1,coords[c][1])] = "|"
            area[(coords[c][0]-2,coords[c][1])] = "."
            cnew.append((coords[c][0]-2,coords[c][1]))
    return cnew

def r(coords, i):
    cur = aoc.copyList(coords)
    rv = []
    i += 1
    while(i < len(file)-1):
        if(file[i] == ")"):
            for c in cur:
                rv.append(c)
            break
        elif(file[i] == "("):
            [i, cur] = r(cur,i)
        elif(file[i] == "|"):
            for c in cur:
                if(c not in rv):
                    rv.append(c)
            cur = aoc.copyList(coords)
        else:
            cur = move(file[i], cur)
        i += 1
    return [i, rv]

def part1():
    coords = [(0,0)]
    area[coords[0]] = "X"
    i = 1
    while(i < len(file)-1):
        el = file[i]
        if(el == "("):
            [i, coords] = r(coords,i)
        else:
            coords = move(el, coords)
        i += 1

    # BFS
    area[(0,0)] = ["X",0]
    queue = [(0,0)]
    i = 0
    while(i < len(queue)):
        (x,y) = queue[i]
        for d in [[0,-1], [1,0], [0,1], [-1,0]]:
            if(a(x+d[0], y+d[1]) in "-|"):
                if(type(a(x+2*d[0],y+2*d[1])) == str):
                    area[(x+2*d[0],y+2*d[1])] = [area[(x+2*d[0],y+2*d[1])], area[(x,y)][1]+1]
                    queue.append((x+2*d[0], y+2*d[1]))
                else:
                    area[(x+2*d[0],y+2*d[1])] = [area[(x+2*d[0],y+2*d[1])], min(area[(x,y)][1]+1,area[(x+2*d[0],y+2*d[1])][1])]                
        i += 1
    return area[queue[-1]][1]

def part2():
    result = 0
    for k in area:
        if(len(area[k]) > 1):
            if(area[k][1] >= 1000):
                result += 1
    return result

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
