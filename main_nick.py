from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

import sys
from word_nick import *

# 글자수, 오류처리(경고창), clicked, 파일 open

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
        #self.createButton.clicked.connect(self.guessClicked)
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

        if self.checkbox1.isChecked():
            self.checked.append("한글")
        if self.checkbox2.isChecked():
            self.checked.append("영어")
        if self.checkbox3.isChecked():
            self.checked.append("숫자")
        if self.checkbox4.isChecked():
            self.checked.append("특수문자")

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


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    screen = Main_nick()
    screen.show()
    sys.exit(app.exec_())
    
