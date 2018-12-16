# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()

# Implementation
def op(register, instruction):
    [opcode, a, b, c] = instruction.split()
    a,b,c = int(a),int(b),int(c)
    if(opcode == "addr"):
        register[c] = register[a] + register[b]
    elif(opcode == "addi"):
        register[c] = register[a] + b
    elif(opcode == "mulr"):
        register[c] = register[a] * register[b]
    elif(opcode == "muli"):
        register[c] = register[a] * b
    elif(opcode == "banr"):
        register[c] = register[a] & register[b]
    elif(opcode == "bani"):
        register[c] = register[a] & b
    elif(opcode == "borr"):
        register[c] = register[a] | register[b]
    elif(opcode == "bori"):
        register[c] = register[a] | b
    elif(opcode == "setr"):
        register[c] = register[a]
    elif(opcode == "seti"):
        register[c] = a
    elif(opcode == "gtir"):
        register[c] = 1 if a > register[b] else 0
    elif(opcode == "gtri"):
        register[c] = 1 if register[a] > b else 0
    elif(opcode == "gtrr"):
        register[c] = 1 if register[a] > register[b] else 0
    elif(opcode == "eqir"):
        register[c] = 1 if a == register[b] else 0
    elif(opcode == "eqri"):
        register[c] = 1 if register[a] == b else 0
    elif(opcode == "eqrr"):
        register[c] = 1 if register[a] == register[b] else 0
    return register

opcodes = [[] for i in range(16)]
def part1():
    result = 0
    i = 0
    while(i < len(file)-2):
        if(file[i][:6] != "Before"): break
        before = [int(x) for x in file[i].split("[")[1].split("]")[0].split(", ")]
        opid = int(file[i+1].split(" ")[0])
        abc = file[i+1].split(" ",1)[1]
        after = [int(x) for x in file[i+2].split("[")[1].split("]")[0].split(", ")]
        cur = 0
        possibleopcodes = []
        for opcode in ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]:
            rv = op(aoc.copyList(before), opcode + " " + abc)
            if(rv == after):
                cur += 1
                possibleopcodes.append(opcode)
        if(opcodes[opid] == []):
            opcodes[opid] = aoc.copyList(possibleopcodes)
        else:
            for opc in opcodes[opid]:
                if(opc not in possibleopcodes):
                    opcodes[opid].remove(opc)
        if(cur >= 3): result += 1
        i += 4
    return result

def part2():
    # getting number of each opcode
    while(1):
        stop = True
        for i in range(len(opcodes)):
            if(len(opcodes[i]) == 1):
                for j in range(len(opcodes)):
                    if(len(opcodes[j]) > 1 and opcodes[i][0] in opcodes[j]):
                        opcodes[j].remove(opcodes[i][0])
            else:
                stop = False
        if(stop == True): break

    register = [0,0,0,0]
    i = 0
    while(i < len(file)):
        if(file[i][:6] == "Before"):
            i += 4
            continue
        if(file[i] != ""):
            opcode = opcodes[int(file[i].split()[0])][0]
            abc = file[i].split(" ",1)[1]
            register = op(register, opcode + " " + abc) 
        i += 1
    return register[0]

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
