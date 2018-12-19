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

def part1n2(reg0=0):
    register = [reg0,0,0,0,0,0]
    ip = int(file[0].split()[1])
    i = register[ip]
    if(file[0][:3] == "#ip"):
        del file[0]
    while(i < len(file)):
        if(ip != None):
            register[ip] = i
        opcode = file[i].split()[0]
        abc = file[i].split(" ",1)[1]
        register = op(register, opcode + " " + abc)
        if(abc[-1] == "0"): break
        if(ip != None):
            i = register[ip]
        i += 1

    # sum of divisors of value in register[2]
    result = 0
    for k in range(1, register[2]+1):
        if(register[2]%k == 0):
            result += k
    return result

# Processing
result1 = part1n2(0)
result2 = part1n2(1)

# Output
aoc.output(result1, result2)
