from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

from word_nick import *
from length_nick import *

# (글자수), 오류처리(경고창), clicked
# 1) 아무것도 선택을 안했을때 오류
# 2) 선택한 값이 글자수를 초과할때 오류
# 3) 글자수를 입력하지 않았을때 랜덤(len(checked), 100)
# 4) checked 인자 연결
# 5) clicked 연결
# 6) length nick -> word nick

class Main_nick(QWidget):

    def __init__(self):
        super().__init__()

        self.word = Word_nick('words_nick.txt')
        self.initGUI()

    def initGUI(self):

        self.setGeometry(300, 200, 400, 400)

        layout = QVBoxLayout()

        # layout1
        layout1 = QHBoxLayout()
        layout.addLayout(layout1)

        self.checkbox1 = QCheckBox("한글")
        self.checkbox1.setChecked(False)
        self.checkbox1.setFont(QtGui.QFont('Hack', 15))
        self.checkbox1.toggled.connect(self.checkbox_toggled)

        layout1.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox("영어")
        self.checkbox2.setChecked(False)
        self.checkbox2.setFont(QtGui.QFont('Hack', 15))
        self.checkbox2.toggled.connect(self.checkbox_toggled)

        layout1.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox("숫자")
        self.checkbox3.setChecked(False)
        self.checkbox3.setFont(QtGui.QFont('Hack', 15))
        self.checkbox3.toggled.connect(self.checkbox_toggled)

        layout1.addWidget(self.checkbox3)

        self.checkbox4 = QCheckBox("특수문자")
        self.checkbox4.setChecked(False)
        self.checkbox4.setFont(QtGui.QFont('Hack', 15))
        self.checkbox4.toggled.connect(self.checkbox_toggled)

        layout1.addWidget(self.checkbox4)


        # layout2
        layout2 = QHBoxLayout()
        layout.addLayout(layout2)

        # select option
        self.label = QLabel("Checked : None")
        self.label.setFont(QtGui.QFont('Hack', 15))

        layout2.addWidget(self.label)


        # layout3
        layout3 = QHBoxLayout()
        layout.addLayout(layout3)

        self.len = QLabel('원하는 닉네임의 길이를 입력하세요 : ')
        self.len.setFont(QtGui.QFont('Hack', 15))
        layout3.addWidget(self.len)
        self.lenEdit = QLineEdit()
        layout3.addWidget(self.lenEdit)


        # layout4
        layout4 = QHBoxLayout()
        layout.addLayout(layout4)

        self.nick = QLabel('생성된 닉네임입니다!')
        self.nick.setFont(QtGui.QFont('Hack', 15))
        layout4.addWidget(self.nick)
        self.currentWord = QTextEdit()
        layout.addWidget(self.currentWord)
        self.currentWord.setReadOnly(True)

        # create buttons
        self.createButton = QToolButton()
        self.createButton.setText('생성')
        self.createButton.setFont(QtGui.QFont('Hack', 15))
        self.createButton.clicked.connect(self.createClicked)
        layout4.addWidget(self.createButton)

        self.copyButton = QToolButton()
        self.copyButton.setText('복사')
        self.copyButton.setFont(QtGui.QFont('Hack', 15))
        #self.createButton.clicked.connect(self.guessClicked)
        layout4.addWidget(self.copyButton)


        self.setLayout(layout)

    def checkbox_toggled(self):

        self.checked = []
        items = ""

        if self.checkbox1.isChecked() == True:
            self.checked.append("한글")
        if self.checkbox2.isChecked():
            self.checked.append("영어")
        if self.checkbox3.isChecked():
            self.checked.append("숫자")
        if self.checkbox4.isChecked():
            self.checked.append("특수문자")
        if self.checkbox1.isChecked() == False and self.checkbox2.isChecked() == False and self.checkbox3.isChecked() == False and self.checkbox4.isChecked() == False:
            self.checked.append("None")
        print(self.checked)

        #print("Checked: %s" % ", ".join(checked))

        count = 0
        for item in self.checked:
            c = "Checked : "
            if count != len(self.checked) - 1:
                items += item + ', '
            else:
                items += item
            count += 1

            self.label.setText(c + items)

        self.limitNick()

    def limitNick(self):
        #self.c = Main_nick()
        #m = self.c.limitNick()

        nick_len = 8
        checked_lst = self.checked
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
            r1 = random.randrange(1, nick_len)
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
            r1 = random.randrange(1, nick_len - 1)
            r2 = random.randrange(1, nick_len - r1)
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
            num_kor = random.randrange(1, nick_len - 2)
            num_eng = random.randrange(1, nick_len - num_kor - 1)
            num_num = random.randrange(1, nick_len - num_kor - num_eng)
            num_char = nick_len - num_kor - num_eng - num_num

        #return self.checked

    def createClicked(self):
        #self.length = Length_nick()
        #self.currentWord.setText(self.length.displayNick())
        self.currentWord.setText(self.limitNick())





if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    screen = Main_nick()
    screen.show()
    sys.exit(app.exec_())
