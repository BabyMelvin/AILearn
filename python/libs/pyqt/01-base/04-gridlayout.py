from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel('label (0,0)')
        layout.addWidget(label, 0, 0)
        label = QLabel('label (0,1)')
        layout.addWidget(label, 0, 1)
        label = QLabel('label (1,0) spanning 2 columns')
        layout.addWidget(label, 1, 0, 2, 1)
        label = QLabel('label (1,0) spanning 2 rows')
        layout.addWidget(label, 0, 2, 2, 1)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
