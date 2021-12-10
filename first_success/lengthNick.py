import random
import copy

class LengthNick:

    def __init__(self):
        self.lst = [0, 0, 0, 0]
        self.result = [0, 0, 0, 0]

    def displayNick(self, userLen, chk):
        # Create random length of each option
        checked = chk
        cpchecked = copy.deepcopy(checked)

        nickLen = int(userLen)
        for k in checked:
            if k == "None":
                cpchecked.remove("None")
        totalLen = len(cpchecked)

        if totalLen == 1:
            self.lst[0] = nickLen
        elif totalLen == 2:
            self.lst[0] = random.randrange(1, nickLen)
            self.lst[1] = nickLen - self.lst[0]
        elif totalLen == 3:
            self.lst[0] = random.randrange(1, nickLen - 1)
            self.lst[1] = random.randrange(1, nickLen - self.lst[0])
            self.lst[2] = nickLen - self.lst[0] - self.lst[1]
        elif totalLen == 4:
            self.lst[0] = random.randrange(1, nickLen - 2)
            self.lst[1] = random.randrange(1, nickLen - self.lst[0] - 1)
            self.lst[2] = random.randrange(1, nickLen - self.lst[0] - self.lst[1])
            self.lst[3] = nickLen - self.lst[0] - self.lst[1] - self.lst[2]

        # Match option and length
        j = 0
        for i in range(4):
            if checked[i] == "None":
                continue
            else:
                self.result[i] = self.lst[j]
                j += 1

        return self.result
