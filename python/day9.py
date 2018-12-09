# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = aoc.getFile().split()
numberOfPlayers = int(file[0])
valueLastMarble = int(file[6])

# Implementation
class Marble:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Circle:
    def __init__(self):
        self.current = Marble(0)
        self.current.prev = self.current
        self.current.next = self.current

    def insert(self, value):
        self.current = self.current.next
        new = Marble(value)
        new.prev = self.current
        new.next = self.current.next
        self.current.next.prev = new
        self.current.next = new
        self.current = new

    def remove(self):
        for i in range(7): self.current = self.current.prev
        value = self.current.value
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.current = self.current.next
        return value

def part1n2(marbles):
    score = [0] + [ 0 for i in range(numberOfPlayers) ]
    currentPlayer = 1
    c = Circle()
    for marble in range(1, marbles + 1):
        currentPlayer += 1
        if(currentPlayer > numberOfPlayers): currentPlayer = 1

        if(marble%23 == 0):
            score[currentPlayer] += marble
            score[currentPlayer] += c.remove()
        else:
            c.insert(marble)
    return max(score)

# Processing
result1 = part1n2(valueLastMarble)
result2 = part1n2(valueLastMarble*100)

# Output
aoc.output(result1, result2)
