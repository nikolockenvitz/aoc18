# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

cave = {}
caveWidth = len(file[0])
caveHeight = len(file)
goblinHitPoints = 0
elfHitPoints = 0
for y in range(caveHeight):
    for x in range(caveWidth):
        cur = [file[y][x]]
        if(cur[0] == "."): continue
        if(cur[0] in "GE"):
            cur.append(200) # hit points
            if(cur[0] == "G"): goblinHitPoints += 200
            if(cur[0] == "E"): elfHitPoints += 200
            cur.append(-1) # round (when moved)
        cave[(x,y)] = cur

targets = { "G": "E", "E": "G" }

def c(x,y):
    if((x,y) in cave):
        return cave[(x,y)]
    return ["."]

def show():
    for y in range(caveHeight):
        p = ""
        h = ""
        for x in range(caveWidth):
            cur = c(x,y)
            p += cur[0]
            if(cur[0] in "GE"):
                h += cur[0] + "(" + str(cur[1]) + "), "
        print(p + "  " + h)

# Implementation
def getSquareToNearestTarget(x, y, target):
    # BFS
    queue = [(x,y,None,0)]
    coords = { (x,y): True }
    i = 0
    solutions = []
    dist = None
    while(i < len(queue)):
        cur = queue[i]
        if(c(cur[0],cur[1])[0] == target): return cur[2]

        distance = cur[3] + 1
        if(c(cur[0],cur[1]-1)[0] == target):
            origin = [cur[0],cur[1]-1] if cur[2] == None else cur[2]
            if(dist == None or dist == distance):
                dist = distance
                solutions.append([cur[0],cur[1],origin])
        if(c(cur[0]-1,cur[1])[0] == target):
            origin = [cur[0]-1,cur[1]] if cur[2] == None else cur[2]
            if(dist == None or dist == distance):
                dist = distance
                solutions.append([cur[0],cur[1],origin])
        if(c(cur[0]+1,cur[1])[0] == target):
            origin = [cur[0]+1,cur[1]] if cur[2] == None else cur[2]
            if(dist == None or dist == distance):
                dist = distance
                solutions.append([cur[0],cur[1],origin])
        if(c(cur[0],cur[1]+1)[0] == target):
            origin = [cur[0],cur[1]+1] if cur[2] == None else cur[2]
            if(dist == None or dist == distance):
                dist = distance
                solutions.append([cur[0],cur[1],origin])

        if(dist != None and dist < distance):
            break
        
        for d in [[0,-1],[-1,0],[1,0],[0,1]]:
            if(c(cur[0]+d[0],cur[1]+d[1])[0] == "." and
               (cur[0]+d[0],cur[1]+d[1]) not in coords):
                origin = [cur[0]+d[0],cur[1]+d[1]] if cur[2] == None else cur[2]
                queue.append([cur[0]+d[0],cur[1]+d[1],origin,cur[3]+1])
                coords[(cur[0]+d[0],cur[1]+d[1])] = True
        i += 1

    mini = [None, None, None] # x, y, return-square
    for solution in solutions:
        if(mini[1] == None or mini[1] > solution[1] or
           (mini[1] == solution[1] and mini[0] > solution[0])):
            mini = solution
    return mini[2]

def part1(elfAttackPower=3):
    global cave
    global elfHitPoints
    global goblinHitPoints
    
    rounds = 0
    while(1):
        rounds += 1
        for y in range(caveHeight):
            for x in range(caveWidth):
                if(c(x,y)[0] in ".#"):
                    continue

                cur = c(x,y)
                if(cur[2] == rounds): continue
                newx, newy = x,y
                
                # find targets
                target = targets[cur[0]]
                if(target == "G" and goblinHitPoints == 0):
                    return elfHitPoints * (rounds-1)
                if(target == "E" and elfHitPoints == 0):
                    return goblinHitPoints * (rounds-1)

                if(c(x,y-1)[0] != target and
                   c(x-1,y)[0] != target and
                   c(x+1,y)[0] != target and
                   c(x,y+1)[0] != target):
                    # move - search for nearest target
                    square = getSquareToNearestTarget(x,y,target)
                    if(square != None):
                        [newx, newy] = square
                        cave[(newx,newy)] = [cur[0], cur[1], rounds]
                        cave[(x,y)] = ["."]

                # attack
                mini = [None, None, None]
                for d in [[0,-1],[-1,0],[1,0],[0,1]]:
                    cur = c(newx+d[0],newy+d[1])
                    if(cur[0] == target):
                        if(mini[0] == None or mini[0] > cur[1]):
                            mini = [cur[1], newx+d[0], newy+d[1]]
                if(mini[0] != None):
                    target = cave[(mini[1],mini[2])]
                    if(target[0] == "E" and target[1] <= 3):
                        # elf dies
                        cave[(mini[1],mini[2])] = ["."]
                        elfHitPoints -= target[1]
                        if(elfAttackPower > 3): return False
                    elif(target[0] == "G" and target[1] <= elfAttackPower):
                        # goblin dies
                        cave[(mini[1],mini[2])] = ["."]
                        goblinHitPoints -= target[1]
                    else:
                        if(target[0] == "G"):
                            goblinHitPoints -= elfAttackPower
                            cave[(mini[1],mini[2])] = [target[0], target[1]-elfAttackPower, target[2]]
                        else:
                            elfHitPoints -= 3
                            cave[(mini[1],mini[2])] = [target[0], target[1]-3, target[2]]

def part2():
    global cave
    global elfHitPoints
    global goblinHitPoints
    
    for elfAttackPower in range(4,100):
        cave = {}
        goblinHitPoints = 0
        elfHitPoints = 0
        for y in range(caveHeight):
            for x in range(caveWidth):
                cur = [file[y][x]]
                if(cur[0] == "."): continue
                if(cur[0] in "GE"):
                    cur.append(200) # hit points
                    if(cur[0] == "G"): goblinHitPoints += 200
                    if(cur[0] == "E"): elfHitPoints += 200
                    cur.append(-1) # round (when moved)
                cave[(x,y)] = cur

        outcome = part1(elfAttackPower)
        if(outcome != False):
            return outcome

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
