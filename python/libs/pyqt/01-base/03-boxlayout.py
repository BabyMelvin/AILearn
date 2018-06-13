# boxLayout similar to gridLayout only support single row or column

from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        label = QLabel('label 1')
        layout.addWidget(label, 0)
        label = QLabel('label 2')
        layout.addWidget(label, 0)

        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addLayout(layout2)

        label = QLabel('label 3')
        layout2.addWidget(label, 0)
        label = QLabel('label 4')
        layout2.addWidget(label, 0)


app = QApplication(sys.argv)
screen = Window()
screen.showMaximized()
sys.exit(app.exec_())
