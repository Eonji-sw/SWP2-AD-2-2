from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

import random

from wordNick import WordNick
from lengthNick import LengthNick

class MainNick(QWidget):

    def __init__(self):
        super().__init__()

        # Display window
        self.setGeometry(800, 300, 400, 400)
        self.setWindowTitle('Nickname creation')

        # Main layout
        layout = QVBoxLayout()
        layout.setSizeConstraint(QLayout.SetFixedSize)

        # Display layout1 for checkbox
        layout1 = QHBoxLayout()
        layout.addLayout(layout1)

        self.checkbox1 = QCheckBox("한글")
        self.checkbox2 = QCheckBox("영어")
        self.checkbox3 = QCheckBox("숫자")
        self.checkbox4 = QCheckBox("특수문자")

        checkboxlst = [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4]
        for i in checkboxlst:
            i.setChecked(False)
            i.setFont(QtGui.QFont('Hack', 15))

            layout1.addWidget(i)

        # Display layout2 for checked state
        layout2 = QHBoxLayout()
        layout.addLayout(layout2)

        # Display select option
        self.label = QLabel("Checked : None")
        self.label.setFont(QtGui.QFont('Hack', 15))

        layout2.addWidget(self.label)

        # Display layout3 for length
        layout3 = QHBoxLayout()
        layout.addLayout(layout3)

        self.len = QLabel('원하는 닉네임의 길이를 입력하세요 : ')
        self.len.setFont(QtGui.QFont('Hack', 15))
        layout3.addWidget(self.len)
        self.lenEdit = QLineEdit()
        self.lenEdit.setFixedSize(50, 25)
        self.lenEdit.setFont(QtGui.QFont('Hack', 13))
        self.lenEdit.setMaxLength(3)
        layout3.addWidget(self.lenEdit)

        # Display layout4 for nickname
        layout4 = QHBoxLayout()
        layout.addLayout(layout4)

        self.nick = QLabel('생성된 닉네임입니다!')
        self.nick.setFont(QtGui.QFont('Hack', 15))
        layout4.addWidget(self.nick)
        self.currentWord = QTextEdit()
        layout.addWidget(self.currentWord)
        self.currentWord.setReadOnly(True)

        # Button for create
        self.createButton = QToolButton()
        self.createButton.setText('생성')
        self.createButton.setFont(QtGui.QFont('Hack', 15))
        self.createButton.clicked.connect(self.createClicked)
        layout4.addWidget(self.createButton)

        self.setLayout(layout)

        # Start creation
        self.startNick = LengthNick()

    def createClicked(self):
        try:
            # Get user input and clear length bar
            userLen = self.lenEdit.text()
            self.lenEdit.clear()

            # Check the check status
            checking = []
            labalcheck = []

            checkboxlst = [(self.checkbox1, "한글"), (self.checkbox2, "영어"), (self.checkbox3, "숫자"), (self.checkbox4, "특수문자")]
            for i, j in checkboxlst:
                if i.isChecked():
                    checking.append(j)
                    labalcheck.append(j)
                else:
                    checking.append("None")

            # Create random length
            if userLen == '':
                userLen = random.randrange(len(labalcheck), 999)

            # Show the check status
            items = ""
            cnt = 0
            for item in labalcheck:
                if cnt != len(labalcheck) - 1:
                    items += item + ', '
                else:
                    items += item
                cnt += 1

                self.label.setText("Checked : " + items)

            # Start creating random length of each option
            self.randLst = self.startNick.displayNick(userLen, checking)
            # Start passing the created random length
            self.wording = WordNick()
            self.wording.randFun(self.randLst)
            # Show a nickname
            self.currentWord.setText(self.wording.showText())
            self.currentWord.setFont(QtGui.QFont('Hack', 15, QtGui.QFont.Bold))
            self.currentWord.setAlignment(Qt.AlignCenter)

        except ValueError:
            self.Warning_event()

    def keyPressEvent(self, e):
        # Press Esc button to end
        if e.key() == Qt.Key_Escape:
            self.close()

    def Warning_event(self):
        # Show error window
        QMessageBox.warning(self, 'Warning Title', 'There\'s a factor that\'s missing!\nPlease try again. :)')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    screen = MainNick()
    screen.show()
    sys.exit(app.exec_())
