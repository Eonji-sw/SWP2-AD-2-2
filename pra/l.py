import random
import copy

from m import *
from w import *

class L:

    def __init__(self):
        self.leng = ''

    def displayNick(self, le, ap):
        userapp = ap
        userap = copy.deepcopy(userapp)

        nick_len = int(le)
        for k in userapp:
            if k == "None":
                userap.remove("None")
        total_len = len(userap)

        l = [0, 0, 0, 0]

        if total_len == 1:
            l[0] = nick_len
        elif total_len == 2:
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

        kk = [0, 0, 0, 0]

        for i in range(4):
            j = 0
            if userapp[i] == "None":   # 넘겨줘야함
                continue
            else:
                kk[i] = l[j]
                j += 1

        return kk
