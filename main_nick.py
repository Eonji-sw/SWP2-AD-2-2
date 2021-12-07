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

        self.setGeometry(300, 300, 500, 300)

        layout = QVBoxLayout()

        self.setLayout(layout)
        self.checkbox1 = QCheckBox("한글")
        self.checkbox1.setChecked(False)
        self.checkbox1.setFont(QtGui.QFont('Hack', 15))
        self.checkbox1.toggled.connect(self.checkbox_toggled)

        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox("영어")
        self.checkbox2.setChecked(False)
        self.checkbox2.setFont(QtGui.QFont('Hack', 15))
        self.checkbox2.toggled.connect(self.checkbox_toggled)

        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox("숫자")
        self.checkbox3.setChecked(False)
        self.checkbox3.setFont(QtGui.QFont('Hack', 15))
        self.checkbox3.toggled.connect(self.checkbox_toggled)

        layout.addWidget(self.checkbox3)

        self.checkbox4 = QCheckBox("특수문자")
        self.checkbox4.setChecked(False)
        self.checkbox4.setFont(QtGui.QFont('Hack', 15))
        self.checkbox4.toggled.connect(self.checkbox_toggled)

        layout.addWidget(self.checkbox4)

        ###########################
        self.label = QLabel("[CHECKBOX]")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Hack', 20))

        layout.addWidget(self.label)
        ############################

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

        for item in checked:
            items += "*checked : " + item + "\n"

            self.label.setText(items)


app = QApplication(sys.argv)
screen = Main_nick()
screen.show()
sys.exit(app.exec_())
