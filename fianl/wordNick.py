import random
import string

class WordNick:

    def __init__(self):
        self.finalNick = ""

    def creatKor(self):
        # Arrangement txt file
        self.lstKors = []
        self.lstKor = []
        f = open('words.txt', 'r')
        lines = f.readlines()
        f.close()

        self.cnt = 0
        for line in lines:
            lineKor = line.split()
            self.lstKors.append(lineKor)

        # All words in list of self.lst_kor
        self.lstKor = sum(self.lstKors, [])
        # All words count
        self.cnt = len(self.lstKor)

    def randFun(self, lst):
        if lst[0] != 0:
            self.creatKor()

        # Create kor word by random
        for i in range(lst[0]):
            k = random.randrange(self.cnt)
            self.finalNick += self.lstKor[k]
        # Create eng word by random
        engStr = string.ascii_letters
        for i in range(lst[1]):
            self.finalNick += random.choice(engStr)
        # Create num word by random
        numStr = string.digits
        for i in range(lst[2]):
            self.finalNick += random.choice(numStr)
        # Create pun word by random
        punStr = string.punctuation
        for i in range(lst[3]):
            self.finalNick += random.choice(punStr)

    def showText(self):
        return self.finalNick
