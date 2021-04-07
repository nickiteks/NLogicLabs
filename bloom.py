import random as r


class BloomFilter:

    def __init__(self, size, countFunctions):
        self.size = size
        self.data = [False] * size
        self.functions = []
        for i in range(0, countFunctions):
            self.functions.append(self.createHashNumber())
        return

    def addWord(self, word):
        if not self.findWord(word):
            for func in self.functions:
                self.data[self.hashFunction(func, word)] = True
        return

    def findWord(self, word):
        for func in self.functions:
            if not (self.data[self.hashFunction(func, word)]):
                return False
        return True

    def createHashNumber(self):
        hashNumber = r.randint(0, self.size)
        return hashNumber

    def hashFunction(self, hashNumber, word):
        for letter in word:
            hashNumber += ord(letter) * hashNumber
        hashNumber = hashNumber % len(self.data)
        #print(str(hashNumber) + "\t" + word)
        return hashNumber

