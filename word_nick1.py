import random
import string

class Word_nick:

    def __init__(self, filename):
        self.lst_kors = []
        self.lst_kor = []
        #f = open(filename, 'r')
        f = open(filename, 'r', encoding = "UTF8")
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            line_kor = line.split()
            self.lst_kors.append(line_kor)

        self.lst_kor = sum(self.lst_kors, [])   # all words in list of self.lst_kor
        self.count = len(self.lst_kor)   # all words count

        #print(self.lst_kors)
        #print(self.lst_kor)
        #print(self.count)

        print('%d words in words_nick.txt' % self.count)

    def randKor(self):
        k = random.randrange(self.count)
        return self.lst_kor[k]   # create word by random

    def randEng(self, cnt_eng):
        cnt = cnt_eng
        engStr = string.ascii_letters
        eng_word = ""
        for i in range(cnt):
            eng_word += random.choice(engStr)
        return eng_word

    def randNum(self, cnt_num):
        cnt = cnt_num
        numStr = string.digits
        num_word = ""
        for i in range(cnt):
            num_word += random.choice(numStr)
        return num_word

    def randPun(self, cnt_pun):
        cnt = cnt_pun
        punStr = string.punctuation
        pun_word = ""
        for i in range(cnt):
            pun_word += random.choice(punStr)
        return pun_word

#if __name__ == '__main__':
    #Word_nick('words_nick.txt')
