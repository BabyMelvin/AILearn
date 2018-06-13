from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText("user?")
        layout.addWidget(self.lineedit)
        self.lineedit.returnPressed.connect(self.return_pressed)

    def return_pressed(self):
        print(self.lineedit.text())


qApp = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(qApp.exec_())

