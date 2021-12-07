from main_nick import *

class Length_nick:
    #pass

    def __init__(self):
        #print(self.main_nick.checked)
        #self.displayNick()
        pass

    def displayNick(self):
        #c = Main_nick()
        #m = c.limitNick()
        #print(m)

        nick_len = 8
        checked_lst = []
        total_len = len(checked_lst)

        if total_len == 1:
            if checked_lst[0] == '한글':
                num_kor = nick_len
            elif checked_lst[0] == '영어':
                num_eng = nick_len
            elif checked_lst[0] == '숫자':
                num_num = nick_len
            elif checked_lst[0] == '특수문자':
                num_char = nick_len
        elif total_len == 2:
            r1 = random.randrange(1, nick_len - len(checked_lst) + 1)
            r2 = nick_len - r1
            if checked_lst[0] == '한글':
                num_kor = r1
            elif checked_lst[0] == '영어':
                num_eng = r1
            elif checked_lst[0] == '숫자':
                num_num = r1
            elif checked_lst[0] == '특수문자':
                num_char = r1
            if checked_lst[1] == '한글':
                num_kor = r2
            elif checked_lst[1] == '영어':
                num_eng = r2
            elif checked_lst[1] == '숫자':
                num_num = r2
            elif checked_lst[1] == '특수문자':
                num_char = r2
        elif total_len == 3:
            r1 = random.randrange(1, nick_len - len(checked_lst) + 1)
            r2 = random.randrange(1, nick_len - len(checked_lst) - r1)
            r3 = nick_len - r1 - r2
            if checked_lst[0] == '한글':
                num_kor = r1
            elif checked_lst[0] == '영어':
                num_eng = r1
            elif checked_lst[0] == '숫자':
                num_num = r1
            elif checked_lst[0] == '특수문자':
                num_char = r1
            if checked_lst[1] == '한글':
                num_kor = r2
            elif checked_lst[1] == '영어':
                num_eng = r2
            elif checked_lst[1] == '숫자':
                num_num = r2
            elif checked_lst[1] == '특수문자':
                num_char = r2
            if checked_lst[2] == '한글':
                num_kor = r3
            elif checked_lst[2] == '영어':
                num_eng = r3
            elif checked_lst[2] == '숫자':
                num_num = r3
            elif checked_lst[2] == '특수문자':
                num_char = r3
        elif total_len == 4:
            num_kor = random.randrange(1, nick_len - len(checked_lst) + 1)
            num_eng = random.randrange(1, nick_len - len(checked_lst) - num_kor)
            num_num = random.randrange(1, nick_len - len(checked_lst) - 1 - num_kor - num_eng)
            num_char = nick_len - num_kor - num_eng - num_num


#if __name__ == '__main__':
#    import sys

#    app = QApplication(sys.argv)
#    screen = Main_nick()
#    screen.show()
#    sys.exit(app.exec_())

#    Length_nick()
