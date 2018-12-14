# Import and Setup
from aoc import *
DAY = AOC.getDayFromFilepath(__file__)
aoc = AOC(DAY)

# Initialization
result1 = None
result2 = None

# Input
file = int(aoc.getFile())

# Implementation
class Recipe:
    def __init__(self, score):
        self.score = score
        self.prev = None
        self.next = None

class Board:
    def __init__(self):
        self.elf1 = Recipe(3)
        self.elf2 = Recipe(7)
        
        self.elf1.prev = self.elf2
        self.elf1.next = self.elf2
        self.elf2.prev = self.elf1
        self.elf2.next = self.elf1

        self.last = self.elf2
        self.length = 2

        self.result1 = None
        self.result2 = None

    def add(self, recipes):
        for recipe in str(recipes):
            r = Recipe(int(recipe))
            r.prev = self.last
            r.next = self.last.next
            self.last.next = r
            self.last = r
            self.length += 1

            foundInputInRecipes = True
            cur = r
            for i in range(len(str(file))):
                if(str(cur.score) != str(file)[-i-1]):
                    foundInputInRecipes = False
                    break
                cur = cur.prev
            if(foundInputInRecipes and self.result2 == None):
                self.result2 = self.length - len(str(file))

    def move(self, elf1, elf2):
        for i in range(elf1+1):
            self.elf1 = self.elf1.next
        for i in range(elf2+1):
            self.elf2 = self.elf2.next

        if(self.result1 == None and self.length > file + 10):
            cur = self.last
            for i in range(self.length - file):
                cur = cur.prev
            self.result1 = ""
            for i in range(10):
                cur = cur.next
                self.result1 += str(cur.score)

def part1n2():
    board = Board()
    while(1):
        e1 = board.elf1.score
        e2 = board.elf2.score
        s = str(e1+e2)
        board.add(s)
        board.move(e1, e2)

        if(board.result1 != None and
           board.result2 != None):
            return [board.result1, board.result2]

# Processing
[result1, result2] = part1n2()

# Output
aoc.output(result1, result2)
