from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('hello')
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel('hello world')
        layout.addWidget(label, 0, 0)


app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())
