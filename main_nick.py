from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
#from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
#from PyQt5.QtWidgets import QLayout, QGridLayout
#from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

import sys
from word_nick import *

# 글자수, 오류처리(경고창), 위젯, clicked, 파일 open

class Main_nick(QWidget):

    def __init__(self):

        super().__init__()

        self.count = 0
        self.initialize()

    def initialize(self):

        self.setGeometry(500, 500, 400, 400)

        #layout = QGridLayout()
        #self.setLayout(layout)
        layout = QVBoxLayout()

        ################## layout1 #################
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

        #######################################

        len = QLabel('원하는 닉네임의 길이를 입력하세요 : ')
        layout.addWidget(len)
        self.lenEdit = QLineEdit()
        #self.nick_lenEdit = QTextEdit()
        layout.addWidget(self.lenEdit)

        # Button for submitting a character
        self.createButton = QToolButton()
        self.createButton.setText('생성')
        #self.createButton.clicked.connect(self.guessClicked)
        layout.addWidget(self.createButton)

        self.createButton = QToolButton()
        self.createButton.setText('복사')
        #self.createButton.clicked.connect(self.guessClicked)
        layout.addWidget(self.createButton)

        nick = QLabel('생성된 닉네임입니다!')
        layout.addWidget(nick)
        self.currentWord = QTextEdit()
        layout.addWidget(self.currentWord)
        self.currentWord.setReadOnly(True)

        # select option
        self.label = QLabel("Selected")
        # self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Hack', 15))

        layout.addWidget(self.label)
        ############################

        self.setLayout(layout)

    def checkbox_toggled(self):

        checked = []

        items = ""

        if self.checkbox1.isChecked():
            checked.append("한글")
        if self.checkbox2.isChecked():
            checked.append("영어")
        if self.checkbox3.isChecked():
            checked.append("숫자")
        if self.checkbox4.isChecked():
            checked.append("특수문자")

        print("* Selected: %s" % ", ".join(checked))

        count = 0
        for item in checked:
            c = "*checked : "
            if count != len(checked) - 1:
                items += item + ', '
            else:
                items += item
            count += 1

            self.label.setText(c + items)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    screen = Main_nick()
    screen.show()
    sys.exit(app.exec_())
