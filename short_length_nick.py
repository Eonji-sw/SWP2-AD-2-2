import random
from main_nick import *

class Length_nick:
    #pass

    def __init__(self):
        #print(self.main_nick.checked)
        self.displayNick()
        pass

    def displayNick(self):
        self.c = Main_nick()
        m = self.c.limitNick()

        nick_len = 8
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
            if self.appChecked[i] == 0:
                continue
            else:
                self.appChecked[i] = l[j]
                j += 1


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    screen = Main_nick()
    screen.show()
    sys.exit(app.exec_())
