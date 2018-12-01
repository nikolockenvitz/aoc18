
PATH_INPUT  = "../input/"
PATH_OUTPUT = "../output/"
IOFILE_PREFIX = ""
IOFILE_SUFFIX = ".txt"

import hashlib
import sys
import os
import re

class AOC:
    def __init__(self, day):
        self.day = day
        print("# "*10 + "Day "+str(self.day) + " #"*10)

        # Filename of input- and output-file
        twoDigitDay = format(self.day, '02d')

        filename = IOFILE_PREFIX
        filename+= twoDigitDay
        filename+= IOFILE_SUFFIX
        
        self.filenameInput  = PATH_INPUT  + filename
        self.filenameOutput = PATH_OUTPUT + filename

    @classmethod
    def getDayFromFilepath(cls, filepath):
        filename = os.path.basename(filepath)
        numbers = re.findall("\d+", filename)
        firstNumber = int(numbers[0])
        return firstNumber

    """
    Input/Output
    """
    def getFile(self, readLines=False):
        f = open(self.filenameInput, "r")
        if(readLines):
            content = f.readlines()
        else:
            content = f.read().strip()
        f.close()
        return content

    def getFileLines(self):
        return self.getFile(readLines=True)

    def output(self, result1, result2, printTerminal=True):
        if(printTerminal):
            print("Result1:", result1)
            print("Result2:", result2)
        f = open(self.filenameOutput, "w")
        f.write(str(result1))
        f.write("\n")
        f.write(str(result2))
        f.close()
        
        if(printTerminal and "idlelib" not in sys.modules): input("")

    """
    Hash
    """
    def hash(self, function, text):
        oHash = function()
        oHash.update(text.encode())
        return oHash.hexdigest()

    def hashSHA1(self, text):
        return self.hash(hashlib.sha1, text)

    def hashSHA256(self, text):
        return self.hash(hashlib.sha256, text)

    def hashSHA512(self, text):
        return self.hash(hashlib.sha512, text)

    def hashMD5(self, text):
        return self.hash(hashlib.md5, text)

