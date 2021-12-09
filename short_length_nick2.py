import random
from main_nick import *

class Length_nick:

    def __init__(self):
        self.displayNick()

    def displayNick(self):
        self.c = Main_nick()
        m = self.c.limitNick()    # 넘겨받음
        n = self.c.limitNic()    # 넘겨받음
        b = self.c.limitLen()    # 넘겨받음

        nick_len = b
        total_len = len(m)

        l = [nick_len, 0, 0, 0]

        if total_len == 2:
            l[0] = random.randrange(1, nick_len)
            l[1] = nick_len - l[0]
        elif total_len == 3:
            l[0] = random.randrange(1, nick_len - 1)
            l[1] = random.randrange(1, nick_len - l[0])
            l[2] = nick_len - l[0] - l[1]
        elif total_len == 4:
            l[0] = random.randrange(1, nick_len - 2)
            l[1] = random.randrange(1, nick_len - l[0] - 1)
            l[2] = random.randrange(1, nick_len - l[0] - l[1])
            l[3] = nick_len - l[0] - l[1] - l[2]

        for i in range(4):
            j = 0
            if n[i] == 0:   # 넘겨줘야함
                continue
            else:
                n[i] = l[j]
                j += 1
        return n
