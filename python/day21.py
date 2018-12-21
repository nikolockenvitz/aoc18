# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFileLines()
ip = int(file[0].split()[1])
del file[0]

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

def part1():
    i = 0
    register = [0,0,0,0,0,0]
    while(i < len(file)):
        register[ip] = i
        opcode = file[i].split(" ")[0]
        abc = file[i].split(" ",1)[1]
        register = op(aoc.copyList(register), opcode + " " + abc)
        i = register[ip]
        i += 1
        if(i == 28):
            return register[3]

def part2():
    register = [0,0,0,0,0,0]
    line = 6
    r3s = {}
    i = 0
    while(1):
        if(line == 6):
            register[2] = register[3] | 65536
            register[3] = 7637914
            line = 8
        if(line == 8):
            register[1] = register[2] & 255
            register[3] = (((register[3] + register[1]) & 16777215) * 65899) & 16777215
            line = None
        if(line == 18):
            register[5] = (register[1] + 1)*256
            if(register[5] > register[2]):
                register[5] = 1
                register[2] = register[1]
                line = 8
            else:
                register[5] = 0
                register[1] = register[1] + 1
                line = 18
        if(line != None): continue

        if(256 > register[2]):
            register[1] = 1
            if(register[3] in r3s):
                break
            r3s[register[3]] = i
            i += 1
            
            line = 6
        else:
            register[1] = 0
            line = 18
    result = [None, None]
    for k in r3s:
        if(result[0] == None or result[0] < r3s[k]):
            result = [r3s[k], k]
    return result[1]

# Processing
result1 = part1()
result2 = part2()

# Output
aoc.output(result1, result2)
