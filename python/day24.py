# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

class Group:
    def __init__(self, army, description, boost=0):
        self.army = army
        self.units = int(description.split(" units")[0])
        self.hitPoints = int(description.split("each with ")[1].split(" hit points")[0])

        self.immunities = []
        self.weaknesses = []
        immunitiesAndWeaknesses = description.split("hit points ")[1].split("with an attack")[0]
        if(immunitiesAndWeaknesses != ""):
            for iw in immunitiesAndWeaknesses[1:].split(")")[0].split(";"):
                if(iw.split()[0] == "weak"):
                    self.weaknesses = iw.split("weak to ")[1].split(", ")
                if(iw.split()[0] == "immune"):
                    self.immunities = iw.split("immune to ")[1].split(", ")

        self.attackDamage = int(description.split("that does ")[1].split()[0])
        self.attackType = description.split("that does ")[1].split()[1]
        self.initiative = int(description.split()[-1])

        if(army == "immune system"):
            self.attackDamage += boost

        self.attacked = False
        self.attacking = None

    def effectivePower(self):
        return self.units * self.attackDamage

groups = {}
initiatives = []
army = None
for line in file:
    if(line == "Immune System:"): army = "immune system"; continue
    if(line == "Infection:"): army = "infection"; continue
    if(line == ""): continue

    cur = Group(army, line)
    groups[cur.initiative] = cur
    initiatives.append(cur.initiative)
initiatives.sort(reverse=True)

# Implementation
def getUnitsForEachArmy():
    immunesystemUnits = 0
    infectionUnits = 0
    for initiative,group in groups.items():
        if(group.army == "immune system"):
            immunesystemUnits += group.units
        else:
            infectionUnits += group.units
    return [immunesystemUnits, infectionUnits]

def targetSelection():
    selectionOrder = []
    for initiative,group in groups.items():
        inserted = False
        for i in range(len(selectionOrder)):
            ep = group.effectivePower()
            if(ep > selectionOrder[i][1] or
               (ep == selectionOrder[i][1] and
                initiative > selectionOrder[i][0])):
                selectionOrder = selectionOrder[:i] + [[initiative,ep]] + selectionOrder[i:]
                inserted = True
                break
        if(not inserted):
            selectionOrder.append([initiative, group.effectivePower()])

    for i,group in groups.items():
        group.attacked = False
        group.attacking = None

    for cur,ep in selectionOrder:
        target = [None, None] # damage, initiative of group
        for i,group in groups.items():
            if(groups[cur].army == group.army): continue
            if(group.attacked): continue
            if(groups[cur].attackType in group.immunities): continue

            damage = groups[cur].effectivePower()
            if(groups[cur].attackType in group.weaknesses):
                damage *= 2
            if(target[0] == None or damage > target[0]):
                target = [damage, i]
            elif(damage == target[0]):
                if(group.effectivePower() > groups[target[1]].effectivePower() or
                   (group.effectivePower() == groups[target[1]].effectivePower() and
                    i > target[1])):
                    target = [damage, i]
        groups[cur].attacking = target[1]
        if(target[1] != None):
            groups[target[1]].attacked = True

def attacking():
    for i in initiatives:
        if(i in groups and groups[i].units > 0):
            target = groups[i].attacking
            if(target != None):
                damage = groups[i].effectivePower()
                if(groups[i].attackType in groups[target].immunities):
                    damage = 0
                if(groups[i].attackType in groups[target].weaknesses):
                    damage *= 2
                groups[target].units -= damage // groups[target].hitPoints

def removeKilledGroups():
    for i in initiatives:
        if(i in groups and groups[i].units <= 0):
            del groups[i]

def part1():
    while(1):
        units = getUnitsForEachArmy()
        if(units[0] == 0): return units[1]
        if(units[1] == 0): return units[0]
        
        targetSelection()
        attacking()
        removeKilledGroups()

def part2():
    global groups
    global initiatives
    for boost in range(1,1000):
        groups = {}
        initiatives = []
        army = None
        for line in file:
            if(line == "Immune System:"): army = "immune system"; continue
            if(line == "Infection:"): army = "infection"; continue
            if(line == ""): continue

            cur = Group(army, line, boost)
            groups[cur.initiative] = cur
            initiatives.append(cur.initiative)
        initiatives.sort(reverse=True)

        last = [None, None]
        while(1):
            units = getUnitsForEachArmy()
            if(units[0] == 0): break
            if(units == last): break
            if(units[1] == 0): return units[0]
            last = aoc.copyList(units)
            
            targetSelection()
            attacking()
            removeKilledGroups()

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
