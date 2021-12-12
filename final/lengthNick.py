import random

class LengthNick:

    def __init__(self):
        self.lst = [0, 0, 0, 0]

    def displayNick(self, userLen, chk, lachk):
        # Create random length of each option
        checked = chk
        labelchecked = lachk

        nickLen = int(userLen)
        totalLen = len(labelchecked)

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
        result = [0, 0, 0, 0]
        j = 0
        for i in range(4):
            if checked[i] == "None":
                continue
            else:
                result[i] = self.lst[j]
                j += 1

        return result
