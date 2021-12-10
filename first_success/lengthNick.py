import random
import copy

from mainNick import *

class LengthNick:

    def __init__(self):
        pass

    def displayNick(self, userLen, chk):
        checked = chk
        cpchecked = copy.deepcopy(checked)

        nickLen = int(userLen)
        for k in checked:
            if k == "None":
                cpchecked.remove("None")
        totalLen = len(cpchecked)

        lst = [0, 0, 0, 0]

        if totalLen == 1:
            lst[0] = nickLen
        elif totalLen == 2:
            lst[0] = random.randrange(1, nickLen)
            lst[1] = nickLen - lst[0]
        elif totalLen == 3:
            lst[0] = random.randrange(1, nickLen - 1)
            lst[1] = random.randrange(1, nickLen - lst[0])
            lst[2] = nickLen - lst[0] - lst[1]
        elif totalLen == 4:
            lst[0] = random.randrange(1, nickLen - 2)
            lst[1] = random.randrange(1, nickLen - lst[0] - 1)
            lst[2] = random.randrange(1, nickLen - lst[0] - lst[1])
            lst[3] = nickLen - lst[0] - lst[1] - lst[2]

        result = [0, 0, 0, 0]

        for i in range(4):
            j = 0
            if checked[i] == "None":
                continue
            else:
                result[i] = lst[j]
                j += 1

        return result
