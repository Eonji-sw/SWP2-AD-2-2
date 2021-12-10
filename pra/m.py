from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

from w import *
from l import *

# (글자수), 오류처리(경고창), clicked
# 1) 아무것도 선택을 안했을때 오류
# 2) 선택한 값이 글자수를 초과할때 오류
# 3) 글자수를 입력하지 않았을때 랜덤(len(checked), 100)
# 4) checked 인자 연결
# 5) clicked 연결
# 6) length nick -> word nick

class M(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 400, 400)

        layout = QVBoxLayout()

        # layout1
        layout1 = QHBoxLayout()
        layout.addLayout(layout1)

        self.checkbox1 = QCheckBox("한글")
        self.checkbox1.setChecked(False)
        self.checkbox1.setFont(QtGui.QFont('Hack', 15))

        layout1.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox("영어")
        self.checkbox2.setChecked(False)
        self.checkbox2.setFont(QtGui.QFont('Hack', 15))

        layout1.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox("숫자")
        self.checkbox3.setChecked(False)
        self.checkbox3.setFont(QtGui.QFont('Hack', 15))

        layout1.addWidget(self.checkbox3)

        self.checkbox4 = QCheckBox("특수문자")
        self.checkbox4.setChecked(False)
        self.checkbox4.setFont(QtGui.QFont('Hack', 15))

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
        self.lenEdit = QLineEdit()    # 넘겨줘야함
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
        self.copyButton.clicked.connect(self.copyClicked)
        layout4.addWidget(self.copyButton)

        self.setLayout(layout)

        self.startNick()

    def startNick(self):
        self.ll = L()


    def createClicked(self):
        lengt = self.lenEdit.text()
        appChecked = []

        if self.checkbox1.isChecked():
            appChecked.append("한글")
        else:
            appChecked.append("None")
        if self.checkbox2.isChecked():
            appChecked.append("영어")
        else:
            appChecked.append("None")
        if self.checkbox3.isChecked():
            appChecked.append("숫자")
        else:
            appChecked.append("None")
        if self.checkbox4.isChecked():
            appChecked.append("특수문자")
        else:
            appChecked.append("None")

        self.k = self.ll.displayNick(lengt, appChecked)
        self.ww = W()
        self.ww.randFun(self.k)
        self.currentWord.setText(self.ww.showText())

    def copyClicked(self):
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    screen = M()
    screen.show()
    sys.exit(app.exec_())
