import random
import string

class WordNick:

    def __init__(self):
        self.lstKors = []
        self.lstKor = []
        f = open('words.txt', 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            lineKor = line.split()
            self.lstKors.append(lineKor)

        self.lstKor = sum(self.lstKors, [])   # all words in list of self.lst_kor
        self.count = len(self.lstKor)   # all words count

        #print('%d words in words_nick.txt' % self.count)

    def randFun(self, m):

        kor_word = ""
        for i in range(m[0]):
            k = random.randrange(self.count)
            kor_word += self.lstKor[k]   # create kor word by random

        eng_word = ""
        engStr = string.ascii_letters
        for i in range(m[1]):
            eng_word += random.choice(engStr)   # create eng word by random

        numStr = string.digits
        num_word = ""
        for i in range(m[2]):
            num_word += random.choice(numStr)   # create num word by random

        punStr = string.punctuation
        pun_word = ""
        for i in range(m[3]):
            pun_word += random.choice(punStr)   # create pun word by random

        self.finalNick = kor_word + eng_word + num_word + pun_word

    def showText(self):
        return self.finalNick
