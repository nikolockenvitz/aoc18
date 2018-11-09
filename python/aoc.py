
PATH_INPUT  = "../input/"
PATH_OUTPUT = "../output/"
FILE_PREFIX = ""
FILE_SUFFIX = ".txt"

import hashlib
import sys

class AOC:
    def __init__(self, day):
        self.day = day
        print("# "*10 + "Day "+str(self.day) + " #"*10)

        # Filename of input- and output-file
        name = FILE_PREFIX
        name+= format(self.day, '02d')
        name+= FILE_SUFFIX
        
        self.filenameInput = PATH_INPUT + name
        self.filenameOutput = PATH_OUTPUT + name

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
        return self.getFile(True)

    def output(self, resultA, resultB, printTerminal=True):
        if(printTerminal):
            print("ResultA:", resultA)
            print("ResultB:", resultB)
        f = open(self.filenameOutput, "w")
        f.write(str(resultA))
        f.write("\n")
        f.write(str(resultB))
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

