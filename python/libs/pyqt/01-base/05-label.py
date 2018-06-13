from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel('the story of dale')
        layout.addWidget(label, 0, 0)

        label = QLabel('few people could understand Dale')
        label.setWordWrap(True)
        layout.addWidget(label, 0, 1)


qApp = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(qApp.exec_())
