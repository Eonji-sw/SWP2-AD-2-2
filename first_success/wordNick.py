import random
import string

class WordNick:

    def __init__(self):
        self.finalNick = ""

    def creatKor(self):
        self.lstKors = []
        self.lstKor = []
        f = open('words.txt', 'r')
        lines = f.readlines()
        f.close()

        self.cnt = 0
        for line in lines:
            lineKor = line.split()
            self.lstKors.append(lineKor)

        self.lstKor = sum(self.lstKors, [])   # all words in list of self.lst_kor
        self.cnt = len(self.lstKor)   # all words count

        #print('%d words in words_nick.txt' % self.count)

    def randFun(self, lst):
        if lst[0] != 0:
            self.creatKor()

        # create kor word by random
        kor_word = ""
        for i in range(lst[0]):
            k = random.randrange(self.cnt)
            kor_word += self.lstKor[k]
        # create eng word by random
        eng_word = ""
        engStr = string.ascii_letters
        for i in range(lst[1]):
            eng_word += random.choice(engStr)
        # create num word by random
        numStr = string.digits
        num_word = ""
        for i in range(lst[2]):
            num_word += random.choice(numStr)
        # create pun word by random
        punStr = string.punctuation
        pun_word = ""
        for i in range(lst[3]):
            pun_word += random.choice(punStr)

        self.finalNick = kor_word + eng_word + num_word + pun_word

    def showText(self):
        return self.finalNick
